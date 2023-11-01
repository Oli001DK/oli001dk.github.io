import requests
URL = 'https://api.hypixel.net/skyblock/auctions'

response = requests.get(URL, timeout=1).json()
print(response)