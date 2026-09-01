import os
import sys
import time
from playwright.sync_api import sync_playwright

def main():
    profile_dir = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti\Workflow agency creative\caroselli - agency\ArenaAI\session_data"
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=True,
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser.pages[0]
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        page.goto(url)
        time.sleep(5)
        
        # Check inputs before clicking
        print("=== INPUTS BEFORE CLICK ===")
        inputs = page.locator("input").all()
        for i, inp in enumerate(inputs):
            try:
                print(f"Input {i}: Type='{inp.get_attribute('type')}', Name='{inp.get_attribute('name')}', Class='{inp.get_attribute('class')}'")
            except: pass
            
        # Click Nuovo
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.click()
        time.sleep(2)
        
        # Check inputs after clicking Nuovo
        print("=== INPUTS AFTER CLICK NUOVO ===")
        inputs = page.locator("input").all()
        for i, inp in enumerate(inputs):
            try:
                print(f"Input {i}: Type='{inp.get_attribute('type')}', Name='{inp.get_attribute('name')}', Class='{inp.get_attribute('class')}'")
            except: pass
            
        browser.close()

if __name__ == "__main__":
    main()
