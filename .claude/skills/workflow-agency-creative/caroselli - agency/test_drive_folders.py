import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def test_drive_folders():
    print("[*] Avvio BrowserManager per testare la navigazione Google Drive...")
    manager = BrowserManager('GoogleDrive', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        print("[*] Navigazione verso Google Drive...")
        page.goto("https://drive.google.com/drive/my-drive", timeout=60000, wait_until='domcontentloaded')
        time.sleep(8)
        
        page.screenshot(path=os.path.join(root_dir, "drive_home.png"))
        print("[V] Screenshot home salvato in 'drive_home.png'")
        
        # 1. Vediamo se troviamo la cartella Digital Empire
        print("[*] Cerco elementi contenenti 'Digital Empire'...")
        
        candidates = page.locator("text='Digital Empire', [aria-label*='Digital Empire']").all()
        print(f"Trovati {len(candidates)} elementi candidati per 'Digital Empire'")
        
        for idx, el in enumerate(candidates):
            try:
                text = el.inner_text().strip()
                tag = el.evaluate("el => el.tagName")
                box = el.bounding_box()
                print(f"[{idx}] Tag={tag}, Text='{text}', Aria-Label='{el.get_attribute('aria-label')}', Box={box}")
            except Exception as e:
                print(f"[{idx}] Errore: {e}")
                
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_drive_folders()
