import os
import sys
import json
import shutil
import subprocess
from exif_injector import inject_metadata

STATE_FILE = "gmb_posting_state.json"
CAMPAIGN_MAP = [
    "Day 1: Orthopedic Step-Down",
    "Day 2: Neuroplasticity Focus",
    "Day 3: Elderly Fall Prevention",
    "Day 4: Premium Recovery Suites",
    "Day 5: Cardiorespiratory Rehab",
    "Day 6: Dr. Ashok P. Kota Spotlight",
    "Day 7: Hospital-to-Home Transition"
]

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"current_day": 1}

def get_current_campaign_details(day_num):
    # Retrieve the detail map
    from gmb_manager import GMB_CAMPAIGNS
    keys = list(GMB_CAMPAIGNS.keys())
    campaign_key = keys[(day_num - 1) % len(keys)]
    return campaign_key, GMB_CAMPAIGNS[campaign_key]

def main():
    # 1. Run the state machine to advance day and generate today's text & image prompt
    print("Advancing state machine...")
    subprocess.run(["python", "gmb_manager.py"], check=True)
    
    # Read advanced day to determine current campaign assets
    state = load_state()
    # State has advanced, so today's campaign corresponds to (current_day - 2) % len
    day = state["current_day"] - 1
    if day == 0:
        day = len(CAMPAIGN_MAP)
        
    campaign_key, campaign = get_current_campaign_details(day)
    
    print("="*60)
    print(f"Executing GMB Daily Publisher for {campaign_key}")
    print("="*60)
    
    clean_name = campaign_key.lower().replace(":", "").replace(" ", "_").replace("-", "_")
    target_img_name = f"gmb_{clean_name}.jpg"
    
    # Check if the geotagged image exists
    if not os.path.exists(target_img_name):
        print(f"Geotagged image {target_img_name} not found! Defaulting to logo.png")
        target_img_name = "logo.png"
        
    # 2. Run the Playwright GMB Poster to publish directly to Google Business Profile!
    print(f"\nLaunching Playwright automation to publish directly to Google Maps...")
    cmd = ["python", "gmb_playwright_poster.py", "current_gmb_text.txt", target_img_name]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
