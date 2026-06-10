import os
import sys
import time
from playwright.sync_api import sync_playwright

def main():
    profile_dir = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti\Workflow agency creative\caroselli - agency\GoogleDrive\session_data"
    
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
        
        # Click Nuovo
        print("[*] Clicking Nuovo...")
        nuovo_btn = page.locator("button:has-text('Nuovo'), button:has-text('New'), button[aria-label='Nuovo'], button[aria-label='New']").first
        nuovo_btn.wait_for(state="visible", timeout=15000)
        nuovo_btn.click()
        time.sleep(3)
        
        # Click Nuova cartella
        print("[*] Clicking Nuova cartella...")
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder'), div:has-text('Nuova cartella'), div:has-text('New folder')").first
        folder_option.wait_for(state="visible", timeout=10000)
        folder_option.click()
        time.sleep(4)
        
        # Locate warning dialog
        dialog = page.locator("div[role='alertdialog']").first
        if dialog.is_visible():
            print("[*] Warning dialog is visible. Finding ok button...")
            ok_btn = dialog.locator("button[name='ok']").first
            
            print("[*] Clicking ok button without force...")
            ok_btn.click()
            time.sleep(4)
            page.screenshot(path="after_clean_click.png")
            
            # Check if text input is visible now
            input_name = page.locator("input[aria-label*='cartella']:visible, input[aria-label*='folder']:visible, input[value='Cartella senza titolo']:visible").first
            if input_name.is_visible():
                print("[*] SUCCESS! Rename input is visible!")
                print(f"[*] Input value: {input_name.evaluate('el => el.value')}")
            else:
                print("[X] Rename input is NOT visible.")
                # Print all visible inputs
                inputs = page.locator("input:visible").all()
                for idx, inp in enumerate(inputs):
                    print(f"Visible input {idx}: {inp.evaluate('el => el.outerHTML')}")
        else:
            print("[X] Warning dialog was not visible.")
            
        browser.close()

if __name__ == "__main__":
    main()
