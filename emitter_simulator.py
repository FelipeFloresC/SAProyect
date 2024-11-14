import csv
import requests
import json

URL = 'http://localhost:8000/car_manager/create-metrics/'

csv_file_path = 'cleaned output/test.csv'

def send_row(row):
    try:
        message = { 
                    "car" : 1,
                    "user" : 1,
                     "data": json.dumps(row)
                }
        
        response = requests.post(URL, message)
        
        if response.status_code == 201:
            print(f"Successfully sent row: {row}")
        else:
            print(f"Failed to send row: {row} - Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending row: {row} - Error: {e}")
        return False


with open(csv_file_path, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        send_row(row)
        if send_row(row) == False:
            break



