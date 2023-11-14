import requests
URL = 'https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER'
response = requests.get(URL, timeout=1)
data = response.json()
buy_summary = data.get("sell_summary")
print(buy_summary)