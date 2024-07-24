import requests
import json
import time

# Load the combined response
file_path = "combined_response.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# Function to fetch infobox details
def fetch_infobox(uri):
    base_url = 'https://meldeplattform-rad.muenchenunterwegs.de'
    url = base_url + uri
    response = requests.get(url)
    return response.json()

# Function to fetch message details
def fetch_message_details(uri):
    base_url = 'https://meldeplattform-rad.muenchenunterwegs.de'
    url = base_url + uri
    response = requests.get(url)
    return response.json()

# Add infobox and message details to each feature
total_features = len(data['features'])
slim_export = []

for i, feature in enumerate(data['features']):
    infobox_uri = feature['properties'].get('infobox_uri')
    if infobox_uri:
        infobox_data = fetch_infobox(infobox_uri)
        feature['properties']['infobox_data'] = infobox_data
        
        # Fetch message details using the self link in infobox_data
        self_uri = infobox_data['data']['json']['links']['self']['href']
        message_details = fetch_message_details(self_uri)
        feature['properties']['message_details'] = message_details
        
        # Append message details to slim export
        slim_export.append(message_details)
        
        print(f"Processed infobox {i + 1} of {total_features} elements")
        print(f"Processed message details {i + 1} of {total_features} elements")
        time.sleep(0.5)  # Sleep to avoid hitting the server too hard

# Save the updated data to a new file
with open('updated_combined_response_with_conversation.json', 'w') as file:
    json.dump(data, file, indent=4)

# Save the slim export to a new file
with open('slim_export.json', 'w') as file:
    json.dump(slim_export, file, indent=4)

print("Updated data saved to updated_combined_response_with_conversation.json")
print("Slim export saved to slim_export.json")
