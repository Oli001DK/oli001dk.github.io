import requests
URL = "https://api.slothpixel.me/api/skyblock/bazaar/HOT_POTATO_BOOK"
response = requests.get(URL)
data = response.json()
buy_summary = data.get("buy_summary")
print(buy_summary)