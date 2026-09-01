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
        
        doc_option = page.locator("[role='menuitem']:visible").filter(has_text="Documenti Google").first
        if not doc_option.count():
            doc_option = page.locator("[role='menuitem']:visible").filter(has_text="Google Docs").first
            
        try:
            with browser.expect_page(timeout=25000) as new_page_info:
                doc_option.click(force=True)
                
                share_confirm_btn = None
                for _ in range(10):
                    t1 = page.locator("text=Creare in una cartella condivisa?").first
                    t2 = page.locator("text=Create in a shared folder?").first
                    if t1.is_visible() or t2.is_visible():
                        share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
                        break
                    time.sleep(0.5)
                
                if share_confirm_btn and share_confirm_btn.is_visible():
                    share_confirm_btn.click(force=True)
                    
            doc_page = new_page_info.value
            doc_page.wait_for_load_state("domcontentloaded")
            time.sleep(8)
            
            # Print page elements / inputs / classes
            print("=== SEARCHING FOR EDITOR ELEMENTS ===")
            
            # Look for some common editor classes in Google Docs
            classes_to_check = [
                ".docs-texteventtarget",
                ".kix-app-layout",
                "iframe",
                ".kix-lineview",
                ".docs-editor",
                "[contenteditable]",
                ".kix-page-content-wrapper"
            ]
            
            for selector in classes_to_check:
                loc = doc_page.locator(selector)
                count = loc.count()
                print(f"Selector '{selector}': found {count} matches")
                if count > 0:
                    try:
                        print(f"  First element class: '{loc.first.get_attribute('class')}'")
                    except: pass
            
            doc_page.close()
        except Exception as e:
            print(f"FAILED: {e}")
            
        browser.close()

if __name__ == "__main__":
    main()
