import requests
import os

# Replace with your actual API key
api_key = 'Enter API Key'

# File to store the last event ID
last_event_file = "last_event_id.txt"


# Function to read the last event ID from the file
def get_last_event_id():
    if os.path.exists(last_event_file):
        with open(last_event_file, 'r') as file:
            return int(file.read().strip())
    return None


# Function to save the last event ID to the file
def save_last_event_id(event_id):
    with open(last_event_file, 'w') as file:
        file.write(str(event_id))


# Get the last event ID or start from a default ID
start_id = get_last_event_id() or 191458158  # Replace with a default ID if needed

# Set the API endpoint and parameters
url = 'https://dc1api.adminbyrequest.com/events'
params = {
    "startid": start_id
}

# Set the headers with the API key
headers = {
    'apikey': f'{api_key}'
}

# Make the GET request to the Events API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    events = response.json()
    if events:
        # Process the events as needed
        for event in events:
            print(event)
        # Save the last event ID to the file
        save_last_event_id(events[-1].get('id'))
    else:
        print("No new events found.")
else:
    print(f'Error: {response.status_code} - {response.text}')
