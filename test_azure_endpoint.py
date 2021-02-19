import requests
import json

# azure endpoint url
url = "http://51921deb-5316-4825-9c2e-a49fb127c77f.westeurope.azurecontainer.io/score"

with open('data/sample_input.json') as f:
    payload = json.load(f)
    payload = json.dumps(payload)

headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
