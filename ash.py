import requests

URL = 'https://api.hypixel.net/skyblock/bazaar'

response = requests.get(URL)
data = response.json()
print(data)