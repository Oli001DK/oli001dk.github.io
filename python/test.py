import requests

#Blaze rod  = EB
#Glowstone  = EG
#nether wart = NW
#red sand block = RS
#mycelium block = MB
#magma cream = MC

craft_antal = input("Hvor mange skal der craftes ")
mp_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/MOLTEN_POWDER', timeout=1)
mp_data = mp_response.json()
mp_buy_summary = mp_data.get("sell_summary")
if mp_buy_summary:
    mp_price = [summary['pricePerUnit'] for summary in mp_buy_summary]
    mp_sorted = sorted(mp_price, reverse=True)
    if len(mp_sorted) >= 4:
        mp = sum(mp_sorted[:4]) / 4
        mp_rounded = round(mp)
        print(mp_rounded, "Molten powder pr i Sell order")

DA_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/DERELICT_ASHE', timeout=1)
DA_data = DA_response.json()
DA_sell_summary = DA_data.get("sell_summary")
if DA_sell_summary:
    DA_price = [summary['pricePerUnit'] for summary in DA_sell_summary]
    DA_sorted = sorted(DA_price, reverse=True)
    if len(DA_sorted) >= 4:
        da = sum(DA_sorted[:4]) / 4
        DA_rounded = round(da)
        print(DA_rounded, "Derelict Ash Pr i Sell order")

EG_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_GLOWSTONE', timeout=1)
EG_data = EG_response.json()
EG_buy_summary = EG_data.get("sell_summary")
if EG_buy_summary:
    EG_price = [summary['pricePerUnit'] for summary in EG_buy_summary]
    EG_sorted = sorted(EG_price, reverse=True)
    if len(EG_sorted) >= 4:
        eg = sum(EG_sorted[:4]) / 4
        EG_rounded = round(eg)
        print(EG_rounded, "Enchanted Glowstone pr i Sell order")
        
EB_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_BLAZE_ROD', timeout=1)
EB_data = EB_response.json()
EB_buy_summary = EB_data.get("sell_summary")
if EB_buy_summary:
    EB_price = [summary['pricePerUnit'] for summary in EB_buy_summary]
    EB_sorted = sorted(EB_price, reverse=True)
    if len(EB_sorted) >= 4:
        eb = sum(EB_sorted[:4]) / 4
        EB_rounded = round(eb)
        print(EB_rounded, "Enchanted Blaze rod pr i Sell order")
             
RS_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_RED_SAND_CUBE', timeout=1)
RS_data = RS_response.json()
RS_buy_summary = RS_data.get("sell_summary")
if RS_buy_summary:
    RS_price = [summary['pricePerUnit'] for summary in RS_buy_summary]
    RS_sorted = sorted(RS_price, reverse=True)
    if len(RS_sorted) >= 4:
        rs = sum(RS_sorted[:4]) / 4
        RS_rounded = round(rs)
        print(RS_rounded, "Enchanted Red Sand Cube pr i Sell order")

MC_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/WHIPPED_MAGMA_CREAM', timeout=1)
MC_data = MC_response.json()
MC_buy_summary = MC_data.get("sell_summary")
if MC_buy_summary:
    MC_price = [summary['pricePerUnit'] for summary in MC_buy_summary]
    MC_sorted = sorted(MC_price, reverse=True)
    if len(MC_sorted) >= 4:
        mc = sum(MC_sorted[:4]) / 4
        MC_rounded = round(mc)
        print(MC_rounded, "Whipped magma cream pr i Sell order")
        
MB_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/ENCHANTED_MYCELIUM_CUBE', timeout=1)
MB_data = MB_response.json()
MB_buy_summary = MB_data.get("sell_summary")
if MB_buy_summary:
    MB_price = [summary['pricePerUnit'] for summary in MB_buy_summary]
    MB_sorted = sorted(MB_price, reverse=True)
    if len(MB_sorted) >= 4:
        mb = sum(MB_sorted[:4]) / 4
        MB_rounded = round(mb)
        print(MB_rounded, "Enchanted Mycelium cube pr i Sell order")

NW_response = requests.get('https://api.slothpixel.me/api/skyblock/bazaar/MUTANT_NETHER_STALK', timeout=1)
NW_data = NW_response.json()
NW_buy_summary = NW_data.get("sell_summary")
if NW_buy_summary:
    NW_price = [summary['pricePerUnit'] for summary in NW_buy_summary]
    NW_sorted = sorted(NW_price, reverse=True)
    if len(NW_sorted) >= 4:
        nw = sum(NW_sorted[:4]) / 4
        NW_rounded = round(nw)
        print(NW_rounded, "Mutant Nether Wart pr i Sell order")
        
#Blaze rod  = EB
#Glowstone  = EG
#nether wart = NW
#red sand block = RS
#mycelium block = MB
#magma cream = M

