import requests
molten_powder_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER', timeout=1)
molten_powder_data = molten_powder_response.json()
buy_summary = molten_powder_data.get("sell_summary")
if buy_summary:
    molten_powder_price = [summary['pricePerUnit'] for summary in buy_summary]
    molten_powder_sorted = sorted(molten_powder_price, reverse=True)
    if len(molten_powder_sorted) >= 4:
        molten_powder = sum(molten_powder_sorted[:4]) / 4
        molten_powder_rounded = round(molten_powder)
        print(molten_powder_rounded, "Pr item in  Sell order")
