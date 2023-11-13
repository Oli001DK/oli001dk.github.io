import requests
URL = 'https://api.slothpixel.me/api/skyblock/bazaar/HOT_POTATO_BOOK'
data = requests.get(URL, timeout=1).json()
print(data)