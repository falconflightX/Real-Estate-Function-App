import requests
import json

local_url = "http://localhost:7071/api/real_estate"
#azure_url = "YOUR_AZURE_URL_PLUS_CODE"

data = [
    {
    'Age': 25,
    'Dist': 251,
    'Num_stores': 5,
    'Lat': 24.9756,
    'Long':121.5521
    }
]

r = requests.post(local_url, json=json.dumps(data))
print(r)
print(r.text)

#r = requests.post(azure_url, json=json.dumps(data))
#print(r)
#print(r.text)