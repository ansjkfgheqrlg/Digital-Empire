import os
import sys
import time

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def debug_drive():
    print("[*] Avvio BrowserManager per ispezionare Google Drive...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(10)
        
        # Salviamo uno screenshot
        page.screenshot(path="drive_debug_home.png")
        print("[V] Screenshot home salvato.")
        
        # Stampiamo tutti gli elementi con testo o aria-label
        print("\n--- ELEMENTI CON TESTO IN DRIVE ---")
        for el in page.locator("div, span, a, button").all():
            try:
                if el.is_visible():
                    text = el.inner_text().strip()
                    aria = el.get_attribute("aria-label") or ""
                    if text or aria:
                        if "advertising" in text.lower() or "advertising" in aria.lower() or "brucia" in text.lower():
                            box = el.bounding_box()
                            print(f"Elem: Text='{text}', Aria='{aria}', Tag='{el.evaluate('e => e.tagName')}', Box={box}")
            except:
                pass
                
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    debug_drive()
