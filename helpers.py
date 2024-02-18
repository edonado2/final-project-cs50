import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def make_api_call(endpoint, headers=None, params=None):
    base_url = "https://api.themoviedb.org/3/"
    url = base_url + endpoint
    api_key = os.getenv("TOKEN")  # Retrieve API key from environment variables

    try:
        # Include the API key in the headers
        headers = headers or {}
        headers["Authorization"] = f"Bearer {api_key}"
        headers["accept"] = "application/json"
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error making API call:", e)
        return None
