import requests
import time
import json
import math

def fetch_data(left, bottom, right, top, zoom=18, rows=200):
    url = 'https://meldeplattform-rad.muenchenunterwegs.de/api/v1/domain/210/message/geojson'
    params = {
        'sort': '-created',
        'rows': rows,
        'visible_map': 1,
        'pageid': 1,
        'zoom': zoom,
        'left': left,
        'bottom': bottom,
        'right': right,
        'top': top
    }
    response = requests.get(url, params=params)
    return response.json()

def scrape_entire_area(left, bottom, right, top, zoom=18, rows=200, tile_size=0.025):
    all_features = []

    # Calculate the number of tiles in each dimension
    num_tiles_x = math.ceil((right - left) / tile_size)
    num_tiles_y = math.ceil((top - bottom) / tile_size)
    total_tiles = num_tiles_x * num_tiles_y
    tile_count = 0

    current_left = left
    while current_left < right:
        current_right = min(current_left + tile_size, right)
        current_bottom = bottom
        while current_bottom < top:
            current_top = min(current_bottom + tile_size, top)

            tile_count += 1
            print(f"Fetching tile {tile_count} of {total_tiles}")

            data = fetch_data(current_left, current_bottom, current_right, current_top, zoom, rows)
            all_features.extend(data['features'])

            current_bottom = current_top
            time.sleep(1)  # To avoid hitting the server too hard

        current_left = current_right

    return {
        "type": "FeatureCollection",
        "features": all_features
    }

# Define the area boundaries
left = 11.266473
bottom = 47.9782469
right = 11.7345382
top = 48.3258461

# Scrape the entire area
scraped_data = scrape_entire_area(left, bottom, right, top, zoom=18, rows=200, tile_size=0.025)

# Save the combined results to a file
with open('combined_response.json', 'w') as file:
    json.dump(scraped_data, file, indent=4)
