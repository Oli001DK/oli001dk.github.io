import requests
URL = 'https://api.hypixel.net/skyblock/auctions_ended'
data = requests.get(URL, timeout=1).json()
print(data)
