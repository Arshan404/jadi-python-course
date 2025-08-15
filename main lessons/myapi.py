import requests
import json

api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)
print(response)
print(response.text)
json_data = response.json()
print(json_data)
print(json_data['number'])
print(json_data['people'])
for thsi_person in json_data['people']:
    print(thsi_person['name'] , thsi_person['craft'])