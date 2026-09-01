import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Instagram_Mentalita import config

def test_instagram():
    print("[Debug] Avvio browser per test Instagram...")
    manager = BrowserManager('Instagram_Mentalita', headless=False)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        print("[Debug] Navigo a: https://www.instagram.com/")
        page.goto("https://www.instagram.com/")
        
        print("[Debug] Attendo 10 secondi...")
        time.sleep(10)
        
        # Scatta screenshot
        screenshot_path = os.path.join(root_dir, "instagram_diagnostic.png")
        page.screenshot(path=screenshot_path)
        print(f"[Debug] Screenshot salvato in: {screenshot_path}")
        
        # Verifica se siamo sulla pagina di login o sulla home
        current_url = page.url
        print(f"[Debug] URL attuale: {current_url}")
        
        # Cerca elementi del feed di Instagram o dell'interfaccia home
        create_btn = page.locator('svg[aria-label="Nuovo post"], svg[aria-label="New post"]').first
        is_logged_in = create_btn.is_visible()
        
        if is_logged_in:
            print("[Debug] RISULTATO: Siamo LOGGATI con successo su Instagram!")
        else:
            print("[Debug] RISULTATO: Non siamo loggati o la sessione è scaduta.")
            
    except Exception as e:
        print(f"[Debug] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_instagram()
