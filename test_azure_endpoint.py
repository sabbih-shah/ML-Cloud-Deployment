import requests
import json

# azure endpoint url
url = "insert_endpoint_url_here"

with open('data/sample_input.json') as f:
    payload = json.load(f)
    payload = json.dumps(payload)

headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
