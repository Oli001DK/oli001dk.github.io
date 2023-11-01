import json
import os
import requests
from tqdm import tqdm
DD = 200

from colorama import Fore, Style

# API endpoint for auction house data
URL = "https://api.hypixel.net/skyblock/auctions"

# Send GET request to the API
response = requests.get(URL)

# Check if the request was successful
if DD == 200:
    data = response.json

    # Check if the request was successful
    if data['success']:
        total_pages = data['totalPages']
        item_info = {}

        auction_count = 0
        bin_count = 0

        # Create a progress bar
        progress_bar = tqdm(total=total_pages, desc='Fetching Auction Data', unit='page')

        # Initialize variables to track failed items
        failed_items = []

        # Iterate through each page of auction data
        for page in range(1, total_pages + 1):
            # Send GET request for each page
            page_url = f"{URL}&page={page}"
            page_response = requests.get(page_url)

            # Check if the request was successful
            if page_response.status_code == 200:
                page_data = page_response.json()

                # Check if the page contains auctions
                if 'auctions' in page_data:
                    # Iterate through each auction on the page
                    for auction in page_data['auctions']:
                        if auction['bin']:
                            bin_count += 1
                        else:
                            auction_count += 1

                        item_uuid = auction['uuid']
                        item_name = auction['item_name']
                        price = auction['starting_bid']
                        seller_uuid = auction['auctioneer']
                        enchantments = auction['item_lore'] if 'item_lore' in auction else 'None'

                        if item_name not in item_info:
                            item_info[item_name] = []

                        item_info[item_name].append((item_uuid, price, seller_uuid, enchantments))

                else:
                    print(f"No auctions found on page {page}")

            else:
                failed_items.extend(page_data.get('auctions', []))
                continue

            # Update the progress bar
            progress_bar.update()

        # Close the progress bar
        progress_bar.close()

        total_count = auction_count + bin_count

        # Sort items by quantity and price
        sorted_items = sorted(item_info.items(), key=lambda x: (sum([1 for _, _, _, _ in x[1]]), x[0]), reverse=True)

        # Save item names, prices, seller UUIDs, and enchantments in a text file
        output_file_path = os.path.join(os.path.dirname(__file__), 'item_info.txt')
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for item_name, info in sorted_items:
                output_file.write(f"{item_name}\n")

                # Sort the prices by descending order
                sorted_info = sorted(info, key=lambda x: x[1], reverse=True)

                for item_uuid, price, seller_uuid, enchantments in sorted_info:
                    # Filter items based on enchantments list
                    filtered_enchantments = [enchant for enchant in enchantments_list if enchant in enchantments]

                    # Check if the item contains any of the specified enchantments
                    if filtered_enchantments:
                        output_file.write(f"Price: {price} | Seller UUID: {seller_uuid} | Item UUID: {item_uuid} | Enchantments: {', '.join(filtered_enchantments)}\n")

                output_file.write("\n")

        # Format the page ranges
        page_ranges = []
        prev_page = 0
        for item in failed_items:
            page = item.get('page', 0)
            if not page_ranges or page != prev_page + 1:
                page_ranges.append([page])
            else:
                page_ranges[-1].append(page)
            prev_page = page

        page_range_str = ', '.join([f"{pages[0]}-{pages[-1]}" if len(pages) > 1 else str(pages[0]) for pages in page_ranges])

        print(f"Auction Count: {auction_count}")
        print(f"BIN Count: {bin_count}")
        print(f"Total Count: {total_count}")
        if failed_items:
            print(f"{Fore.RED}Failed to retrieve data for item(s):")
            for item in failed_items:
                print(f"Item UUID: {item['uuid']} | Item Name: {item['item_name']}")
            print(Style.RESET_ALL)
        #print(f"Data retrieved from page(s): {page_range_str}")
        print(f"Item information saved to {output_file_path}")

    else:
        print("Request to the Hypixel API was not successful.")

else:
    print("Failed to connect to the Hypixel API.")
