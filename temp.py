# -*- coding: utf-8 -*-
"""
Spyder Editor

This script downloads biological activity data from the USDA Phytochemical Database, 
saves the files to disk, and processes the downloaded CSV files.
"""

import os
import requests as req
import pubchempy as pcp
import pandas as pd
import glob
from pandas.errors import EmptyDataError

# Create directories for saving the downloaded files and for processing
try:
    os.mkdir("bioact")
except FileExistsError:
    pass

try:
    os.mkdir("SDFS")
except FileExistsError:
    pass

# Base URL and endpoint for the USDA Phytochemical Database CSV export
base = 'https://phytochem.nal.usda.gov'
mid = '/biological-activities-chemicals-csv-export'

# Download biological activity data CSV files (1 to 5)
for bio in range(1, 6):
    file_path = f"bioact/{bio}.csv"
    
    # Check if the file already exists
    if os.path.isfile(file_path):
        print(f"{bio} already downloaded")
    else:
        # Construct the URL for each CSV file
        url = f"{base}{mid}/{bio}/all?page&_format=csv"
        
        # Send a GET request to download the CSV
        res = req.get(url)
        
        # Save the CSV to the 'bioact' directory
        with open(file_path, "wb") as csv:
            csv.write(res.content)
        print(f"Downloading {bio}")

# Process downloaded CSV files and store data in 'SDFS'
csv_files = glob.glob('bioact/*.csv')
lig =[]
for file in csv_files:
    try:
        # Read each CSV into a pandas DataFrame
        temp_df = pd.read_csv(file)
        
        # Process the DataFrame (you can customize this part)
        # For now, just save the DataFrame in a new folder as an example
        output_file = f"SDFS/{os.path.basename(file)}"
        temp_df.to_csv(output_file, index=False)
        lig.append(temp_df)
        
    except EmptyDataError:
        print(f"{file} is empty. Skipping...")

    except Exception as e:
        print(f"Error processing {file}: {e}")
        
df = pd.concat(lig, axis=0, ignore_index=True)

for name in df['Chemical Name']:
    compounds = pcp.get_compounds(name,'name')
    for compound in compounds:
        cid = compound.cid
        print(cid)
        
        pcp.download('SDF','SDFS/'+ str(cid)+'.sdf',cid,'cid')
        print("Downloading "+ str(cid))
