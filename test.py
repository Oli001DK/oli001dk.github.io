import requests
response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER', timeout=1)
data = response.json()
buy_summary = data.get("sell_summary")
if buy_summary:
    prices_per_unit = [summary['pricePerUnit'] for summary in buy_summary]
    sorted_prices = sorted(prices_per_unit, reverse=True)
    if len(sorted_prices) >= 4:
        molten_powder = sum(sorted_prices[:4]) / 4
        molten_powder_rounded = round(molten_powder)
        print(molten_powder_rounded, "Sell order")
