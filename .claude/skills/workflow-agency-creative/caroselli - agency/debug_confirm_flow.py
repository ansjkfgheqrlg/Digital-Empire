import os
import sys
import time
from playwright.sync_api import sync_playwright

def main():
    profile_dir = r"C:\Users\Utente\AppData\Local\Google\Chrome\User Data"
    
    with sync_playwright() as p:
        print("[*] Launching browser...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser.pages[0]
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        print(f"[*] Navigating to {url}...")
        page.goto(url)
        time.sleep(6)
        page.screenshot(path="confirm_flow_1_home.png")
        
        # Click Nuovo
        print("[*] Clicking Nuovo...")
        nuovo_btn = page.locator("button:has-text('Nuovo'), button:has-text('New'), button[aria-label='Nuovo'], button[aria-label='New']").first
        nuovo_btn.wait_for(state="visible", timeout=15000)
        nuovo_btn.click() # no force
        time.sleep(3)
        page.screenshot(path="confirm_flow_2_nuovo_menu.png")
        
        # Click Nuova cartella
        print("[*] Clicking Nuova cartella...")
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder'), div:has-text('Nuova cartella'), div:has-text('New folder')").first
        folder_option.wait_for(state="visible", timeout=10000)
        folder_option.click() # no force
        time.sleep(4)
        page.screenshot(path="confirm_flow_3_modal.png")
        
        # Click Crea e condividi
        share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
        if share_confirm_btn.is_visible():
            print("[*] Clicking Crea e condividi cleanly...")
            share_confirm_btn.click() # no force!
            
            # Take screenshots every second for 6 seconds
            for i in range(1, 7):
                time.sleep(1)
                page.screenshot(path=f"confirm_flow_4_after_click_{i}.png")
                print(f"[*] Saved screenshot after {i} seconds.")
        else:
            print("[*] Modal button not visible!")
            
        browser.close()

if __name__ == "__main__":
    main()
