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
        
        # Find active alertdialog
        dialog = page.locator("div[role='alertdialog']").first
        
        with open("dialog_buttons.txt", "w", encoding="utf-8") as f:
            if dialog.is_visible():
                f.write("[*] alertdialog is visible.\n\n")
                
                # Dump dialog outerHTML
                f.write("=== FULL DIALOG HTML ===\n")
                f.write(dialog.evaluate("el => el.outerHTML"))
                f.write("\n\n")
                
                # Find all buttons
                buttons = dialog.locator("button, [role='button'], div[class*='button']").all()
                f.write(f"=== FOUND {len(buttons)} BUTTON-LIKE ELEMENTS ===\n")
                
                btn_info = []
                for idx, btn in enumerate(buttons):
                    try:
                        btn_info.append({
                            "index": idx,
                            "tagName": btn.evaluate("el => el.tagName"),
                            "className": btn.evaluate("el => el.className"),
                            "role": btn.evaluate("el => el.getAttribute('role')"),
                            "text": btn.evaluate("el => el.textContent"),
                            "outerHTML": btn.evaluate("el => el.outerHTML")
                        })
                    except Exception as e:
                        btn_info.append({"index": idx, "error": str(e)})
                        
                f.write(json.dumps(btn_info, indent=2))
            else:
                f.write("[*] alertdialog is NOT visible in DOM.\n")
                
        print("[*] Dump complete. Saved to dialog_buttons.txt")
        browser.close()

if __name__ == "__main__":
    main()
