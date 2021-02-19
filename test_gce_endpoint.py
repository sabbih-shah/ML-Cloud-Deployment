import json
import requests

url = "http://0.0.0.0:5000/predict"

with open('data/sample_input.json') as f:
    payload = json.load(f)
    payload = json.dumps(payload)


headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)