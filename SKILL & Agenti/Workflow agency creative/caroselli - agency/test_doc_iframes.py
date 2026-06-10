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
            time.sleep(15)
            
            print(f"=== LISTING ALL {len(doc_page.frames)} FRAMES ===")
            for i, frame in enumerate(doc_page.frames):
                print(f"Frame {i}: Name='{frame.name}', URL='{frame.url}'")
                try:
                    loc = frame.locator(".docs-texteventtarget")
                    count = loc.count()
                    print(f"  Inside Frame {i}: found {count} matches for '.docs-texteventtarget'")
                except Exception as fe:
                    print(f"  Error searching in Frame {i}: {fe}")
                    
            doc_page.close()
        except Exception as e:
            print(f"FAILED: {e}")
            
        browser.close()

if __name__ == "__main__":
    main()
