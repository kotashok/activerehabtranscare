import os
import sys
import json
import requests
from google.oauth2.credentials import Credentials

# Location info for ActiveRehab TransCare
BUSINESS_PROFILE_ID = "17672246425335467198"
PLACE_ID = "ChIJI2SXH5eFyzsRKbr2bY4gzAE"

# Path to the existing authenticated token from the Chiro GMB system
TOKEN_PATH = r"c:\Users\conta\.antigravity\gmb_system\token.json"
SCOPES = ["https://www.googleapis.com/auth/business.manage"]

def get_transcare_credentials():
    """Load the existing authenticated token and refresh it dynamically if expired."""
    from google.auth.transport.requests import Request
    
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError(
            f"Authenticated GMB token not found at: {TOKEN_PATH}\n"
            "Please make sure the gmb_system is authenticated."
        )
    
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing GMB access token...")
            try:
                creds.refresh(Request())
                # Save refreshed token back to preserve it
                with open(TOKEN_PATH, "w") as f:
                    f.write(creds.to_json())
                print("Token refreshed and saved successfully!")
            except Exception as ex:
                print(f"Failed to refresh token: {ex}")
                raise ex
                
    return creds

def publish_post_to_gmb(post_text, image_url=None):
    """
    Publish a post directly to the ActiveRehab TransCare GMB profile using the Business Profile ID.
    Google Local Posts Endpoint:
    https://mybusiness.googleapis.com/v4/accounts/{accountId}/locations/{locationId}/localPosts
    """
    creds = get_transcare_credentials()
    
    # 1. Discover Account Name automatically (e.g. accounts/108xxx)
    headers = {"Authorization": f"Bearer {creds.token}"}
    try:
        resp = requests.get(
            "https://mybusinessaccountmanagement.googleapis.com/v1/accounts",
            headers=headers,
            timeout=15
        )
        print(f"Account Management API status: {resp.status_code}")
        if resp.status_code == 200:
            accounts = resp.json().get("accounts", [])
            if accounts:
                account_name = accounts[0]["name"]
            else:
                raise RuntimeError("No GMB accounts found.")
        else:
            print(f"Account Management API failed: {resp.text}")
            # Fallback to legacy
            resp = requests.get(
                "https://mybusiness.googleapis.com/v4/accounts",
                headers=headers,
                timeout=15
            )
            print(f"Legacy API status: {resp.status_code}")
            if resp.status_code == 200:
                accounts = resp.json().get("accounts", [])
                if accounts:
                    account_name = accounts[0]["name"]
                else:
                    raise RuntimeError("No GMB accounts found.")
            else:
                print(f"Legacy API failed: {resp.text}")
                raise RuntimeError(f"GMB API calls failed. Statuses: {resp.status_code}")
    except Exception as e:
        print(f"Account discovery error: {e}")
        raise e

    # Build the full location name
    # The GMB location ID corresponds to the Business Profile ID or the raw location resource name.
    # We will build: accounts/{accountId}/locations/{businessProfileId}
    location_name = f"{account_name}/locations/{BUSINESS_PROFILE_ID}"
    url = f"https://mybusiness.googleapis.com/v4/{location_name}/localPosts"
    
    # 2. Build the GMB post payload
    payload = {
        "languageCode": "en",
        "summary": post_text[:1500],  # GMB strict character limit
        "callToAction": {
            "actionType": "BOOK",
            "url": "https://wa.me/918106822020",  # Direct WhatsApp CTA
        },
        "topicType": "STANDARD",
    }
    
    # If a live image URL is provided, attach it as media
    if image_url:
        payload["media"] = [
            {
                "mediaFormat": "PHOTO",
                "sourceUrl": image_url
            }
        ]

    print(f"Publishing GMB Post directly to Location: {location_name}...")
    print(f"API Endpoint: {url}")
    
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }
    
    resp = requests.post(url, headers=headers, json=payload)
    
    if resp.status_code == 200:
        print("[OK] CONGRATULATIONS! THE GMB POST IS LIVE ON GOOGLE MAPS!")
        return resp.json()
    else:
        error_msg = resp.json().get("error", {}).get("message", resp.text)
        print(f"Failed to post directly to GMB: {error_msg}")
        raise RuntimeError(f"GMB API Error {resp.status_code}: {error_msg}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gmb_direct_poster.py <post_text_file> [image_url]")
        sys.exit(1)
        
    text_file = sys.argv[1]
    img_url = sys.argv[2] if len(sys.argv) > 2 else None
    
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()
        
    publish_post_to_gmb(text, img_url)
