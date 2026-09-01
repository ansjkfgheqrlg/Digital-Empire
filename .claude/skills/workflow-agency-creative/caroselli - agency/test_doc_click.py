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
            
        print(f"Found doc option: {doc_option.inner_text()}")
        
        try:
            # Let's wait for page to open
            with browser.expect_page(timeout=25000) as new_page_info:
                doc_option.click(force=True)
                
                # Attendi fino a 5 secondi per il modale di condivisione
                share_confirm_btn = None
                for _ in range(10):
                    t1 = page.locator("text=Creare in una cartella condivisa?").first
                    t2 = page.locator("text=Create in a shared folder?").first
                    if t1.is_visible() or t2.is_visible():
                        share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
                        break
                    time.sleep(0.5)
                
                if share_confirm_btn and share_confirm_btn.is_visible():
                    print("Clicking share confirm button...")
                    share_confirm_btn.click(force=True)
                    
            new_page = new_page_info.value
            print(f"SUCCESS: Page opened! Title: {new_page.title()}, URL: {new_page.url}")
            new_page.close()
        except Exception as e:
            print(f"FAILED: {e}")
            page.screenshot(path="test_doc_click_failed.png")
            
        browser.close()

if __name__ == "__main__":
    main()
