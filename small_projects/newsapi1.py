import requests
import json
# API endpoint and key
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "5b590ae940cb4685b2a6b3f2cbaea4f9"
 
# Parameters for the API request
params = {
    "country": "us",
    "apiKey": API_KEY
}
 
# Making the API request
response = requests.get(API_URL, params=params)
 
# Checking if the request was successful
if response.status_code == 200:
    # Printing the JSON response
    print(json.dumps(response.json(),indent=5))
    
else:
    print(f"Error: {response.status_code}")