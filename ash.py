import requests
import json

URL = 'https://api.hypixel.net/skyblock/auctions'

response = requests.get(URL)
data = response.json()
print(data)