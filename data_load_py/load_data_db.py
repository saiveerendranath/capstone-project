import pandas as pd
import mysql.connector

# Step 1: Read the CSV file
csv_file_path = '/Users/saiveerendranath/Documents/Final_Sem_Project/files/armslengthsales_2022_valid_20230404.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',        # your database host
    user='root',    # your database username
    password='Sai1028@',# your database password
    database='propertydb' # your target database
)

cursor = connection.cursor()



# Step 4: Insert CSV data into MySQL
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO your_table_name (column1_name, column2_name, column3_name)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))

connection.commit()

print("CSV file has been uploaded successfully!")

# Step 5: Close connection
cursor.close()
connection.close()
