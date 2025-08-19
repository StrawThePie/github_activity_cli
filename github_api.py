import os
import requests
from dotenv import load_dotenv

def fetch_user_events(username, page=1):
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GitHub token not found.")
        return []

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/users/{username}/events/public?page={page}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error: {errh}")
        return []
    except requests.exceptions.ConnectionError as errc:
        print("Error connecting:", errc)
        return []
    except requests.exceptions.Timeout as errt:
        print("Timeout error:", errt)
        return []
    except requests.exceptions.RequestException as err:
        print("Request error:", err)
        return []

    return response.json() if response.status_code == 200 else []
