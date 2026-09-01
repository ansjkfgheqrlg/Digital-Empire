import os
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
        
        # Click Nuovo
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.click()
        time.sleep(2)
        
        # Find all elements with role menuitem
        print("=== MENU ITEMS ===")
        menu_items = page.locator("[role='menuitem']").all()
        for i, item in enumerate(menu_items):
            try:
                print(f"Item {i}: Text='{item.inner_text()}', Class='{item.get_attribute('class')}'")
            except: pass
            
        # Try to click "Caricamento di file" option and expect file chooser
        upload_option = page.locator("[role='menuitem']:visible").filter(has_text="Caricamento di file").first
        if not upload_option.count():
            upload_option = page.locator("[role='menuitem']:visible").filter(has_text="File upload").first
            
        if upload_option.count():
            print(f"Found upload option: {upload_option.inner_text()}")
            try:
                with page.expect_file_chooser(timeout=10000) as fc_info:
                    upload_option.click(force=True)
                print("SUCCESS: File chooser triggered!")
            except Exception as e:
                print(f"FAILED to trigger file chooser: {e}")
        else:
            print("Upload option not found!")
            
        browser.close()

if __name__ == "__main__":
    main()
