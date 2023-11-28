
import requests

class Api:
    def __init__(self, name_api):
        self.name_api = name_api

def get_api(self):
        api_loot = requests.get(self.name_api)
        api_buy_summary = api_loot.get("sell_summary")
        if api_buy_summary:
            api_price = [summary['pricePerUnit'] for summary in api_buy_summary]
            api_sorted = sorted(api_price, reverse=True)
            if len(api_sorted) >= 4:
                api = sum(api_sorted[:4]) / 4
                api_rounded = round(api)
        return api_rounded
    
    def __str__(self):
        return str(self.get_api())

api_1 = Api('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER')
api_1.get_api()
print(api_1)

