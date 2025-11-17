"""
Google Events API: A Quick Start Example
See more at: https://apify.com/johnvc/google-events-api---access-google-events-data

This script demonstrates how to use the Google Events API Actor
to search Google Events and retrieve structured event data.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "q": "events in South Bend Indiana",
    "location": "South Bend, Indiana",
    "advanced": "date:today",
    "max_pages": 1,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-events-api---access-google-events-data").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)


for each in range(0, 10):
    # Run the Actor and wait for it to finish
    run = client.actor("johnvc/google-events-api---access-google-events-data").call(run_input=run_input)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)
