import requests
import json

#MTG API Documentation
#URL: https://docs.magicthegathering.io/#documentationgetting_started

# The API endpoint
url = "https://api.magicthegathering.io/v1/cards/386616"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(json.dumps(response_json, indent=4))