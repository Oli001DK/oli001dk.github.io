import requests

data = requests.get("https://api.hypixel.net/skyblock/auctions").json()
auctions = data["auctions"]
items = []

for auction in auctions:
    try:
        if auction["bin"] and "Flower of Truth" in auction["item_name"]:
            items.append([auction["item_name"], auction["starting_bid"], auction["category"]])
    except KeyError:
        pass

items.sort(key = lambda x:x[1])

for item in items:
    print(item)
print(data["auctions"])
