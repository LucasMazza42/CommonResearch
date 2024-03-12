import pandas as pd
import json 
import alphaVantage
import os
import shutil

output_folder = "/Users/lucasmazza/Desktop/CommonResearch/Data/Securities"


#FUNCTION to create a dataframe from raw json 
def create_dataframe(json_data): 

    data = pd.DataFrame(json_data)

    return data

#Function to read from CSV 
def read_data(security): 
    data = pd.read_csv(f'Data/Securities{security}.csv')

    return data

#function to find and write new security data
def write_data(security): 
    json_data = alphaVantage.get_daily_time_series(security, alphaVantage.API_key)
    data = create_dataframe(json_data)
    
    output_file_path = os.path.join(output_folder, f'{security}.csv')

    # Write DataFrame to CSV
    data.to_csv(output_file_path, index=False)
    print(f"CSV file has been written to '{output_file_path}' inside '{output_folder}' folder.")


write_data("MSFT")