import requests
import json
import time

# Load the combined response
file_path = "combined_response.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to fetch infobox detsnails
def fetch_infobox(uri):
    base_url = 'https://meldeplattform-rad.muenchenunterwegs.de'
    url = base_url + uri
    response = requests.get(url)
    return response.json()

# Add infobox details to each feature
total_features = len(data['features'])
for i, feature in enumerate(data['features']):
    infobox_uri = feature['properties'].get('infobox_uri')
    if infobox_uri:
        infobox_data = fetch_infobox(infobox_uri)
        feature['properties']['infobox_data'] = infobox_data
        print(f"Processed {i + 1} of {total_features} elements")
        time.sleep(0.5)  # Sleep to avoid hitting the server too hard

# Save the updated data to a new file
with open('updated_combined_response.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated data saved to updated_combined_response.json")
