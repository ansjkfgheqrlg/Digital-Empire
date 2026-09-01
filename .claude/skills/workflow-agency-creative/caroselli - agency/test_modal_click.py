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
        
        # Listen to console log messages
        page.on("console", lambda msg: print(f"[Browser Console] {msg.text}"))
        
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
        
        # Find active alertdialog
        dialog = page.locator("div[role='alertdialog']").first
        if dialog.is_visible():
            print("[*] Dialog is visible. Finding ok button...")
            ok_btn = dialog.locator("button[name='ok']").first
            
            # Print state before click
            print(f"[*] ok button tagName: {ok_btn.evaluate('el => el.tagName')}")
            print(f"[*] ok button text: {ok_btn.evaluate('el => el.textContent')}")
            print(f"[*] ok button attributes: {ok_btn.evaluate('el => JSON.stringify(Array.from(el.attributes).map(a => ({name: a.name, value: a.value})))')}")
            
            # Save HTML before click
            with open("before_click.txt", "w", encoding="utf-8") as f:
                f.write(page.content())
                
            print("[*] Clicking ok button...")
            ok_btn.click() # Clean click
            
            # Capture screenshots and HTML changes
            for i in range(1, 11):
                time.sleep(0.5)
                page.screenshot(path=f"after_click_{i}.png")
                # Check active elements
                active_el_html = page.evaluate("document.activeElement ? document.activeElement.outerHTML.substring(0, 150) : 'None'")
                print(f"[*{i*0.5}s] Active element: {active_el_html}")
                
            with open("after_click_final.txt", "w", encoding="utf-8") as f:
                f.write(page.content())
        else:
            print("[*] Dialog was not visible!")
            
        browser.close()

if __name__ == "__main__":
    main()
