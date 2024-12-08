import requests
import json

def fetchAPI(venueId):
    # venueId = "42911d00f964a520f5231fe3"
    versioning = "%2020231010"
    oauth_token = "URKT0K1X0DOFMRKYKKYVVPGI1GIWVBRFCTP005RJFH1JKS0C"
    url = f"https://api.foursquare.com/v2/venues/{venueId}/?v={versioning}&oauth_token={oauth_token}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return json.loads(response.text)