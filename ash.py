import requests
URL = 'https://api.hypixel.net/skyblock/auctions'

response = requests.get(URL, timeout=1)
data = response.json
list(data)
print(data)
