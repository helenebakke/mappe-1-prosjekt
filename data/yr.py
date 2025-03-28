import requests
import json
data = json.loads(response.text)

response = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58")
data = response.json()
temperatures = [entry['temperature'] for entry in data['weather']]
