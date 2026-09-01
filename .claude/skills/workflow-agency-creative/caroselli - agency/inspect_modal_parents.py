import os
import sys
import time
import json
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
        nuovo_btn.click(force=True)
        time.sleep(3)
        
        # Click Nuova cartella
        print("[*] Clicking Nuova cartella...")
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder'), div:has-text('Nuova cartella'), div:has-text('New folder')").first
        folder_option.wait_for(state="visible", timeout=10000)
        folder_option.click(force=True)
        time.sleep(4)
        
        # Locate the warning text
        warning_el = page.locator("text=Creare in una cartella condivisa?").first
        
        with open("modal_parents.txt", "w", encoding="utf-8") as f:
            if warning_el.is_visible():
                f.write("[*] Warning element is visible.\n\n")
                
                info = warning_el.evaluate("""el => {
                    let res = [];
                    let curr = el;
                    for (let i = 0; i < 8; i++) {
                        if (!curr) break;
                        res.push({
                            level: i,
                            tagName: curr.tagName,
                            className: curr.className,
                            role: curr.getAttribute('role'),
                            html_start: curr.outerHTML ? curr.outerHTML.substring(0, 300) : null
                        });
                        curr = curr.parentElement;
                    }
                    return res;
                }""")
                
                f.write(json.dumps(info, indent=2))
            else:
                f.write("[*] Warning element is NOT visible in DOM.\n")
                
        print("[*] Dump complete. Saved to modal_parents.txt")
        browser.close()

if __name__ == "__main__":
    main()
