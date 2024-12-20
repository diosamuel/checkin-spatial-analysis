import requests
import json
# from bs4 import BeautifulSoup
# def fetchUser(userId):
#     API_PATH = f"http://foursquare.com/user/{userId}"
#     response = requests.get(API_PATH)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     name_element = soup.find(class_="name")
#     if name_element:
#         name = name_element.text
#         return name
import os
import json
import requests

def fetchAPI(venueId):
    # Check if the file already exists in the datasets/ folder
    file_path = f"dataset/{venueId}.json"
    if os.path.exists(file_path):
        # print(f"Data for venue ID {venueId} already exists. Fetch skipped.")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Load the JSON data from the file
        return data  # Return the data from the file

    # Define API parameters
    versioning = "20231010"  # No need for '%20' in the string
    oauth_token = "URKT0K1X0DOFMRKYKKYVVPGI1GIWVBRFCTP005RJFH1JKS0C"
    url = f"https://api.foursquare.com/v2/venues/{venueId}/?v={versioning}&oauth_token={oauth_token}"
    headers = {"accept": "application/json"}

    # Fetch data from the API
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse response JSON
        data = response.json()

        # Save JSON data to file
        # os.makedirs("datasets", exist_ok=True)  # Ensure the datasets/ folder exists
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data for venue ID {venueId} has been saved.")
        return data
    else:
        print(f"Failed to fetch data for venue ID {venueId}. Status code: {response.status_code}")
        return None
