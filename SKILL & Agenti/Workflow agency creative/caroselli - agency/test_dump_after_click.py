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
        
        # Click confirm button
        print("[*] Clicking ok button...")
        page.evaluate("document.querySelector('div[role=\"alertdialog\"] button[name=\"ok\"]').click()")
        time.sleep(5)
        
        # Dump HTML of body
        print("[*] Saving body HTML...")
        with open("body_after_click.txt", "w", encoding="utf-8") as f:
            f.write(page.evaluate("document.body.innerHTML"))
            
        print("[*] Dump complete. Saved to body_after_click.txt")
        browser.close()

if __name__ == "__main__":
    main()
