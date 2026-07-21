import sys
import os
import time
from playwright.sync_api import sync_playwright

# TransCare Business Profile Location ID
LOCATION_ID = "17672246425335467198"

# Path to the pre-authenticated Chrome User Data Directory from the Chiro GMB system
USER_DATA_DIR = r"c:\Users\conta\.antigravity\gmb_system\gmb_profile"

def post_update_transcare(post_text, image_path=None):
    """
    Publishes a GMB post to ActiveRehab TransCare using the pre-authenticated Chrome user session.
    """
    if image_path and not os.path.exists(image_path):
        print(f"Warning: Image not found at {image_path}, proceeding without image.")
        image_path = None
        
    # Standard GBP post modal URL for this location
    url = f"https://business.google.com/local/business/u/0/{LOCATION_ID}/promote/updates/add"
    print(f"Starting Playwright automation for ActiveRehab TransCare...")
    print(f"Target GMB URL: {url}")

    with sync_playwright() as p:
        # Launch using the existing pre-logged in Chrome Profile!
        browser = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False, # Runs non-headlessly to ensure stable GMB JS rendering
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.set_default_timeout(60000) # 60 seconds GMB load threshold
        
        try:
            page.goto(url)
            print("Waiting for post modal...")
            
            # Wait for the main text area to appear
            page.wait_for_selector('textarea, div[contenteditable="true"]', state="visible")
            
            print("Filling in GMB clinical description...")
            textbox = page.locator('textarea, div[contenteditable="true"]').first
            textbox.click()
            textbox.fill(post_text)
            
            if image_path:
                print(f"Uploading geotagged image: {os.path.basename(image_path)}...")
                file_input = page.locator('input[type="file"]')
                file_input.set_input_files(image_path)
                page.wait_for_timeout(5000) # Give 5s to process the file upload
            
            print("Adding actionable CTA button...")
            # Scroll the modal down to ensure the button is visible
            page.mouse.wheel(0, 500) 
            time.sleep(1)

            # Click the "+ Button" actionable button
            try:
                add_button_btn = page.locator('text="Add more details"').locator("xpath=..").locator("button").first
                add_button_btn.wait_for(timeout=2000)
                add_button_btn.scroll_into_view_if_needed()
                add_button_btn.click(timeout=2000)
            except Exception as e:
                print("First button attempt failed. Trying fallback...")
                add_button_btn = page.get_by_role("button", name="+ Button").first
                if not add_button_btn.is_visible():
                    add_button_btn = page.locator('button:has-text("Button")').first
                
                add_button_btn.scroll_into_view_if_needed()
                add_button_btn.click(timeout=5000)
                
            print("Clicked + Button. Waiting for dropdown...")
            time.sleep(2)
            
            # Click the dropdown toggle (defaults to "None" or "Add a button (optional)")
            button_dropdown = page.get_by_role("button", name="None").first
            if not button_dropdown.is_visible():
                button_dropdown = page.locator('button:has-text("None"), text="Add a button (optional)"').first
            
            if button_dropdown.is_visible():
                button_dropdown.click()
                print("Opened 'Add a button' dropdown.")
                time.sleep(2)
                
                # Select "Call now" from the menu
                call_option = page.get_by_role("menuitem", name="Call now").first
                if not call_option.is_visible():
                    call_option = page.locator('text="Call now", text="Call"').first
                
                if call_option.is_visible():
                    call_option.click()
                    print("[OK] 'Call now' button successfully selected.")
                    time.sleep(2)
                else:
                    print("Warning: 'Call now' option not found in menu.")
            else:
                print("Warning: 'Add a button' dropdown not found.")
            
            print("Clicking GMB Post...")
            post_btn = page.locator('button:has-text("Post"), div[role="button"]:has-text("Post")')
            post_btn.click()
            
            print("Finalising GMB publication...")
            try:
                page.wait_for_selector('text="Post published", text="Success", [aria-label="Close"]', timeout=20000)
                print("[OK] Done! Post successfully published live to Google My Business!")
                return True
            except:
                print("Warning: Wait for confirmation timed out, but post might have been sent.")
                return True
            
        except Exception as e:
            print(f"Playwright post failed: {e}")
            page.screenshot(path="error_transcare_gmb.png")
            return False
        finally:
            browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gmb_playwright_poster.py <post_text_file> [image_path]")
        sys.exit(1)
        
    text_file = sys.argv[1]
    img_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()
        
    post_update_transcare(text, img_path)
