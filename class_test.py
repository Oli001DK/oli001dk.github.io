import requests


class Api: 
    def __init__(self, name_api):
        self.name_api = name_api

    def get_hypixel_api(self):
        api_loot = requests.get(self.name_api, timeout = 1)
        api_buy_summary = api_loot.json().get("buy_summary")
        api_price = [summary['pricePerUnit'] for summary in api_buy_summary]
        api_sorted = sorted(api_price, reverse=True)
        api = sum(api_sorted[:4]) / 4
        api_rounded = round(api)
        return api_rounded

    def __str__(self):
        return str(self.get_hypixel_api())

api_1 = Api('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER')
api_1.get_hypixel_api()
print(api_1)
