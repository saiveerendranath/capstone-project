# Data Folder

This folder contains all the datasets and related information used in the capstone project "Dynamic Property Price Prediction: A Predictive System for Smart Real-Estate Decision." The data has been meticulously collected, processed, and structured to facilitate property price forecasting and livability factor analysis.
Data Collection

The datasets were sourced from authoritative organizations and publicly available data sources:
- City of Milwaukee Property Sales Data:
	  - Dataset: Property Sales Data.
    - Source: City of Milwaukee.
    - Description:
        - Provides detailed transaction information, including property features (e.g., square footage, number of rooms) and sale prices.
        - Covers residential property transactions for the year 2022.
- OpenStreetMap (OSM) Livability Data:
    - Dataset: Amenities and Infrastructure Data.
    - Source: OpenStreetMap Overpass API.
    - Description:
       - Provides data on key livability factors (e.g., transportation, schools, healthcare facilities, retail amenities).
       - Includes geographic coordinates (latitude, longitude) for nearby amenities to align with property data.


## Data Description
| Column Name       | Description                                                             | Data Type |
| ----------------- | ----------------------------------------------------------------------- | --------- |
| `PropertyID`      | Unique identifier for each property                                     | `int`     |
| `PropType`        | Type of property (e.g., Residential, Commercial, Manufacturing)         | `object`  |
| `taxkey`          | Tax key associated with the property                                    | `int64`   |
| `Address`         | Full address of the property                                            | `object`  |
| `CondoProject`    | The condominium project name, if applicable                             | `object`  |
| `District`        | District in which the property is located                               | `int`     |
| `nbhd`            | Neighborhood code for the property                                      | `int`     |
| `Style`           | Style or design of the property (e.g., Ranch, Office Building)          | `object`  |
| `Extwall`         | Exterior wall material of the property                                  | `object`  |
| `Stories`         | Number of stories in the property                                       | `float`   |
| `Year_Built`      | Year the property was built                                             | `float`   |
| `Rooms`           | Total number of rooms in the property                                   | `float`   |
| `Units`           | Number of units in the property (for multi-unit buildings)              | `int`     |
| `bdrms`           | Number of bedrooms in the property                                      | `float`   |
| `Fbath`           | Number of full bathrooms in the property                                | `float`   |
| `Hbath`           | Number of half bathrooms in the property                                | `float`   |
| `Sale_Date`       | Date when the property was sold                                         | `object`  |
| `Sale_Price`      | Sale price of the property                                              | `float`   |  |

  
## Data Integration Process

The following flowchart illustrates how the data was merged and processed for analysis:
- Merge Criteria:
   - Shared keys: Property address (or geolocation), year, and relevant amenities.
   - Aligned property sales data with livability and geolocation data.
- Segmentation:
   - Divided into National, Regional, and Metro-Regional datasets for more granular analysis.
-	Filtering:
	 - Focused on key property features such as:
	    - Square footage
      - Number of rooms
      - Property type (e.g., single-family homes, condos)
   - Focused on the following livability factors:
      - Proximity to transportation hubs
      - Proximity to schools and healthcare facilities
      - Retail amenities

## Files in this folder:

- armslengthsales_2022_valid_20230404:
    - Comprehensive dataset after preprocessing and merging.
    - Includes data across all regions and key property and livability features.
    - Key features include:
      - Property prices (Sale_price).
      - Property features (e.g., square footage, number of rooms).

- osm_data_with_addresses:
    -Filtered dataset focusing on:
      - Key livability features affecting property prices.
    - Used for focused analysis, including demand forecasting and price elasticity studies.
