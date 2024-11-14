import csv
import requests

import datetime


URL = 'https://example.com/api/data'

csv_file_path = 'cleaned output/test.csv'



def send_row(row):
    try:
        message = { 
                    "patente" : "BT-OF-87",
                    "user" : "will afton",
                    "timestamp": datetime.datetime.now() ,
                    "data" : row,
                }
        
        response = requests.post(URL, json=row)
        
        if response.status_code == 200:
            print(f"Successfully sent row: {row}")
        else:
            print(f"Failed to send row: {row} - Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending row: {row} - Error: {e}")


with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        send_row(row)



