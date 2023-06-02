import urllib.request
import json
import requests
url = "https://pokeapi.co/api/v2/"

# trace ("Calling", url)
response = requests.get(url) # Get data from the URL
response.raise_for_status()


data = response.json()
# print(data)

for key in data.keys():
  print("key: {} | data: {}".format(key,data[key]))

print(data["ability"])

