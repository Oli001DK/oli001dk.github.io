import requests

#Blaze rod  = EB
#Glowstone  = EG
#nether wart
#red sand block = RS
#mycelium block
#magma cream = MC

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

EG_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_GLOWSTONE', timeout=1)
EG_data = EG_response.json()
EG_buy_summary = EG_data.get("sell_summary")
if EG_buy_summary:
    EG_price = [summary['pricePerUnit'] for summary in EG_buy_summary]
    EG_sorted = sorted(EG_price, reverse=True)
    if len(EG_sorted) >= 4:
        EG = sum(EG_sorted[:4]) / 4
        EG_rounded = round(EG)
        print(EG_rounded, "Enchanted Glowstone pr i Sell order")
        
EB_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_BLAZE_ROD', timeout=1)
EB_data = EB_response.json()
EB_buy_summary = EB_data.get("sell_summary")
if EB_buy_summary:
    EB_price = [summary['pricePerUnit'] for summary in EB_buy_summary]
    EB_sorted = sorted(EB_price, reverse=True)
    if len(EB_sorted) >= 4:
        EB = sum(EB_sorted[:4]) / 4
        EB_rounded = round(EB)
        print(EB_rounded, "Enchanted Blaze rod pr i Sell order")
             
RS_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_RED_SAND_CUBE', timeout=1)
RS_data = RS_response.json()
RS_buy_summary = RS_data.get("sell_summary")
if RS_buy_summary:
    RS_price = [summary['pricePerUnit'] for summary in RS_buy_summary]
    RS_sorted = sorted(RS_price, reverse=True)
    if len(RS_sorted) >= 4:
        RS = sum(RS_sorted[:4]) / 4
        RS_rounded = round(RS)
        print(RS_rounded, "Enchanted Red Sand Cube pr i Sell order")

MC_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/WHIPPED_MAGMA_CREAM', timeout=1)
MC_data = MC_response.json()
MC_buy_summary = MC_data.get("sell_summary")
if MC_buy_summary:
    MC_price = [summary['pricePerUnit'] for summary in MC_buy_summary]
    MC_sorted = sorted(MC_price, reverse=True)
    if len(MC_sorted) >= 4:
        MC = sum(MC_sorted[:4]) / 4
        MC_rounded = round(MC)
        print(MC_rounded, "Whipped magma cream pr i Sell order")