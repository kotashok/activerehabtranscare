import os
import sys
import time
import argparse
from playwright.sync_api import sync_playwright

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_FILE = os.path.join(SCRIPT_DIR, "session_state.json")
DEFAULT_URL = "https://labs.google/flow"

def setup_session():
    """
    Launches a visible browser window for the user to complete their Google/Labs login.
    Saves the authenticated session tokens to session_state.json.
    """
    print("\n" + "="*70)
    print("GOOGLE FLOW AUTOMATION - AUTHENTICATION SETUP")
    print("="*70)
    print("1. A visible Chromium browser window will open shortly.")
    print("2. Please log into your Google Account in that window.")
    print("3. Complete any required Two-Factor Authentication (2FA).")
    print("4. Navigate to the Google Flow video creator studio / editor.")
    print("5. Once the editor is fully loaded, return to this terminal.")
    print("="*70 + "\n")

    with sync_playwright() as p:
        # Launch a headful browser
        browser = p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        
        print(f"Navigating to {DEFAULT_URL}...")
        page.goto(DEFAULT_URL)
        
        # Wait for user confirmation in console
        input("--> PRESS ENTER HERE in this console ONLY AFTER you have successfully logged in and are viewing the Google Flow Editor page...")
        
        # Save storage state (cookies, local storage)
        print(f"Saving authentication state to {SESSION_FILE}...")
        context.storage_state(path=SESSION_FILE)
        
        print("Setup complete! Browser context successfully captured.")
        browser.close()

def generate_video(prompt, download_dir=None, headless=False):
    """
    Loads the saved session, enters the prompt into the editor, triggers generation,
    waits for render completion, and downloads the video file.
    """
    if not os.path.exists(SESSION_FILE):
        print(f"[-] Error: Session state file not found at {SESSION_FILE}")
        print("    Please run the setup first: python video_flow_automation.py --setup")
        sys.exit(1)

    if not download_dir:
        download_dir = os.path.dirname(SCRIPT_DIR) # Defaults to website root directory

    print("\n" + "="*70)
    print(f"LAUNCHING VIDEO GENERATION")
    print(f"Prompt: {prompt}")
    print(f"Target Directory: {download_dir}")
    print("="*70 + "\n")

    with sync_playwright() as p:
        # Launch browser with saved context state
        print("Initializing authenticated browser instance...")
        browser = p.chromium.launch(headless=headless, args=["--no-sandbox"])
        context = browser.new_context(
            storage_state=SESSION_FILE,
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()
        
        print(f"Opening Google Flow editor ({DEFAULT_URL})...")
        page.goto(DEFAULT_URL)
        
        # Heuristically wait for the editor page to load
        print("Waiting for page load elements...")
        page.wait_for_load_state("networkidle")
        time.sleep(3) # Safe buffer for complex dynamic SPA hydration

        # HEURISTIC 1: Find the main prompt textarea or input field
        print("Locating prompt entry field...")
        prompt_selectors = [
            "textarea",
            "div[contenteditable='true']",
            "input[type='text']",
            "[placeholder*='prompt']",
            "[placeholder*='describe']",
            "[placeholder*='imagine']",
            "[placeholder*='video']"
        ]
        
        prompt_input = None
        for selector in prompt_selectors:
            try:
                element = page.locator(selector).first
                if element.is_visible() and element.is_enabled():
                    prompt_input = element
                    print(f"[+] Found input field using selector: '{selector}'")
                    break
            except Exception:
                continue

        if not prompt_input:
            print("[-] Error: Could not locate the prompt input field.")
            print("    The Google Flow UI may have changed. Please contact support or adjust selectors.")
            browser.close()
            sys.exit(1)

        # Enter prompt
        prompt_input.fill(prompt)
        print("[+] Custom prompt successfully entered.")
        time.sleep(1)

        # HEURISTIC 2: Find the Generate/Create button
        print("Locating generate button...")
        generate_selectors = [
            "button:has-text('Generate')",
            "button:has-text('Create')",
            "button:has-text('Run')",
            "button[type='submit']",
            "div[role='button']:has-text('Generate')",
            "button:has(.fa-play)"
        ]
        
        gen_button = None
        for selector in generate_selectors:
            try:
                element = page.locator(selector).first
                if element.is_visible():
                    gen_button = element
                    print(f"[+] Found generate button using selector: '{selector}'")
                    break
            except Exception:
                continue

        if not gen_button:
            print("[-] Error: Could not locate the Generate button.")
            browser.close()
            sys.exit(1)

        # Trigger Generation
        print("Triggering video generation...")
        gen_button.click()
        print("[+] Generation request sent. Waiting for video compilation (this may take 1-3 minutes)...")

        # HEURISTIC 3: Monitor render progress or wait until completed
        # Google Flow uses typical spinner/progress or disables/enables buttons
        # We'll monitor for button re-enabling or a download button appearance
        # For security, we'll poll the download button selector
        download_selectors = [
            "button:has-text('Download')",
            "a:has-text('Download')",
            "[aria-label*='download']",
            "[title*='download']",
            ".download-btn",
            "button:has(.fa-download)"
        ]
        
        print("Polling for download links/buttons...")
        download_button = None
        max_wait_seconds = 240 # 4 minutes timeout
        start_time = time.time()
        
        while time.time() - start_time < max_wait_seconds:
            for selector in download_selectors:
                try:
                    element = page.locator(selector).first
                    if element.is_visible():
                        download_button = element
                        print(f"\n[+] Video compilation complete! Found download trigger using: '{selector}'")
                        break
                except Exception:
                    continue
            
            if download_button:
                break
                
            # Print a progress indicator
            elapsed = int(time.time() - start_time)
            print(f"Compiling... {elapsed}s elapsed (polling UI)", end="\r")
            time.sleep(5)

        if not download_button:
            print("\n[-] Error: Video compilation timed out or download button was not found.")
            browser.close()
            sys.exit(1)

        # Download the file using Playwright's download handler
        print("Initiating file transfer...")
        try:
            with page.expect_download(timeout=60000) as download_info:
                download_button.click()
            download = download_info.value
            
            # Save downloaded video to target directory
            filename = f"flow_video_{int(time.time())}.mp4"
            final_path = os.path.join(download_dir, filename)
            download.save_as(final_path)
            
            print("="*70)
            print("[+] SUCCESS!")
            print(f"Video compiled and saved to: {final_path}")
            print("="*70 + "\n")
            
        except Exception as e:
            print(f"\n[-] Error during file download: {e}")
            
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Flow (Labs/VideoFX) AI Video Generation Automation")
    parser.add_argument("--setup", action="store_true", help="Launch headful browser to log into Google and save session state")
    parser.add_argument("--generate", action="store_true", help="Generate video using the stored authenticated session")
    parser.add_argument("--prompt", type=str, help="Cinematic script or description prompt for video generation")
    parser.add_argument("--dir", type=str, help="Output directory where generated .mp4 files will be saved")
    parser.add_argument("--headless", action="store_true", help="Run background browser instead of showing visual window during generation")
    
    args = parser.parse_args()

    if args.setup:
        setup_session()
    elif args.generate:
        if not args.prompt:
            print("[-] Error: Please specify a generation prompt using --prompt \"...\"")
            sys.exit(1)
        generate_video(args.prompt, args.dir, args.headless)
    else:
        parser.print_help()
