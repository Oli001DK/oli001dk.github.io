import requests
craft_antal = input("Hvor mange skal der craftes ")
molten_powder_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER', timeout=1)
molten_powder_data = molten_powder_response.json()
molten_powder_buy_summary = molten_powder_data.get("sell_summary")
if molten_powder_buy_summary:
    molten_powder_price = [summary['pricePerUnit'] for summary in molten_powder_buy_summary]
    molten_powder_sorted = sorted(molten_powder_price, reverse=True)
    if len(molten_powder_sorted) >= 4:
        molten_powder = sum(molten_powder_sorted[:4]) / 4
        molten_powder_rounded = round(molten_powder)
        print(molten_powder_rounded, "Moltenn powder pr i Sell order")

DERELICT_ASHE_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/DERELICT_ASHE', timeout=1)
DA_data = DERELICT_ASHE_response.json()
DA_sell_summary = DA_data.get("sell_summary")
if DA_sell_summary:
    DA_price = [summary['pricePerUnit'] for summary in DA_sell_summary]
    DA_sorted = sorted(DA_price, reverse=True)
    if len(DA_sorted) >= 4:
        DA = sum(DA_sorted[:4]) / 4
        DA_rounded = round(DA)
        print(DA_rounded, "Derelict Ash Pr i Sell order")
