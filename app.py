from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import requests
import pandas as pd
import geopy.distance
from geopy.geocoders import Nominatim
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend like ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Needed for OPTIONS, POST, etc.
    allow_headers=["*"],  # Allow all headers
)

HBGR_pipeline = joblib.load('/Users/saiveerendranath/Documents/Final_Sem_Project/dump_model/HGBR_pipeline.pkl')

class InputData(BaseModel):
    Address : str
    FinishedSqft : float
    Bdrms : int
    Fbath : int
    Hbath : int
    Stories : int
    Year_Built : int
    Style : str

geolocator = Nominatim(user_agent="osm_data_extractor")
overpass_url = "http://overpass-api.de/api/interpreter"
radius = 10000
categories = {
    "Tsp": '["highway"]',
    "Atr": '["tourism"]',
    "Edc": '["amenity"="school"]',
    "Hth": '["amenity"="hospital"]',
    "Rst": '["amenity"="restaurant"]',
    "Rtl": '["shop"]'
}

def fetch_osm_data(lat, lon, category, tag):
    query = f"""
    [out:json];
    (
      node{tag}(around:{radius},{lat},{lon});
    );
    out center;
    """

    response = requests.get(overpass_url, params={'data': query})
    if response.status_code == 200:
        json_data = response.json()
        nodes = json_data.get("elements", [])

        count = len(nodes)
        distances = [
            geopy.distance.distance((lat, lon), (node["lat"], node["lon"])).meters
            for node in nodes
        ]
        avg_distance = sum(distances) / count if count > 0 else 0

        return count, avg_distance
    else:
        print(f"Failed to fetch data for {category}")
        return 0, 0
    
def fetch_coordinates(address):
    print("getting into fetch Coordinates ", address)
    try:
        # Convert address to latitude and longitude
        location = geolocator.geocode(address, timeout=10)
        if location:
            lat, lon = location.latitude, location.longitude
            print(f"Geocoded: {address} -> ({lat}, {lon})")
        else:
            print(f"Could not geocode address: {address}")

        # Extract data for each category
        result = {"Address": address, "Latitude": lat, "Longitude": lon}
        for cat, tag in categories.items():
            print("Getting into Fetch OSM Data for Category: ", cat)
            count, avg_dist = fetch_osm_data(lat, lon, cat, tag)
            result[f"{cat}Num"] = count
            result[f"{cat}Dst"] = avg_dist

        # Append result to data list
        return result

    except Exception as e:
        print(f"Error processing address {address}: {e}")


@app.get("/home")
def homePage():
    return "Hello World"

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert the input list into a numpy array and reshape for prediction
        input_data = data.dict()
        result  =  fetch_coordinates(input_data["Address"])
        
        feature_names = [
    'FinishedSqft', 'Bdrms', 'Fbath', 'Hbath', 'Stories', 'Year_Built',
    'TspNum_fixed', 'TspDst_fixed', 'AtrNum_fixed', 'AtrDst_fixed',
    'EdcNum_fixed', 'EdcDst_fixed', 'HthNum_fixed', 'HthDst_fixed',
    'RstNum_fixed', 'RstDst_fixed', 'RtlNum_fixed', 'RtlDst_fixed',
    'Style' 
]

        features = [
            input_data["FinishedSqft"], #1
            input_data["Bdrms"], #2
            input_data["Fbath"], #3
            input_data["Hbath"], #4
            input_data["Stories"], #5
            input_data["Year_Built"], #6
            result['TspNum'], #7
            result['TspDst'], #8
            result['AtrNum'], #9
            result['AtrDst'], #10
            result['EdcNum'], #11
            result['EdcDst'], #12
            result['HthNum'], #13
            result['HthDst'], #14
            result['RstNum'], #15
            result['RstDst'], #16
            result['RtlNum'], #17
            result['RtlDst'], #18
            input_data["Style"] #19
        ]

        
        input_df = pd.DataFrame([features], columns=feature_names)
        

        # Make prediction using the pipeline
        print("Started Predicting")
        prediction = HBGR_pipeline.predict(input_df)
        print("predicted value: ", prediction[0])
        pred_sale_price = f"{prediction[0]:.2f}"

        #Setting up mySQL Connection
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sai1028@",
        database="propertydb"
        )

        cursor = conn.cursor(dictionary=True)

        query = "select * from property;"


        
        # Return the prediction result
        return {"prediction": prediction.tolist()}



    except Exception as e:
        return {"error": str(e)}
    
@app.get("/properties")
def get_properties():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sai1028@",
        database="propertydb"
        )  # your DB config
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Latitude, Longitude, Style, pred_sale_price FROM property;")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
