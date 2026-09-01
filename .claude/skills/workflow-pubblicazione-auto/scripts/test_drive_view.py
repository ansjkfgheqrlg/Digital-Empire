import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Google_Drive import config

def test_drive():
    print("[Debug] Avvio browser per test Drive...")
    manager = BrowserManager('Google_Drive', headless=False)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        print(f"[Debug] Navigo a: {config.DRIVE_MENTALITA_URL}")
        page.goto(config.DRIVE_MENTALITA_URL)
        
        print("[Debug] Attendo 15 secondi per il caricamento completo...")
        time.sleep(15)
        
        # Stampa titolo pagina e URL corrente
        print(f"[Debug] Titolo pagina: {page.title()}")
        print(f"[Debug] URL attuale: {page.url}")
        
        # Scattiamo uno screenshot per capire cosa vede il browser
        screenshot_path = os.path.join(root_dir, "drive_screenshot.png")
        page.screenshot(path=screenshot_path)
        print(f"[Debug] Screenshot salvato in: {screenshot_path}")
        
        # Cerchiamo elementi con aria-label
        print("[Debug] Ricerca elementi con aria-label:")
        elements = page.locator('[aria-label]')
        count = elements.count()
        print(f"[Debug] Trovati {count} elementi con aria-label.")
        
        labels = []
        for i in range(min(count, 50)):
            label = elements.nth(i).get_attribute("aria-label")
            if label:
                labels.append(label)
        
        print("[Debug] Primi 50 aria-label trovati:")
        for label in labels:
            if ".mp4" in label.lower() or "video" in label.lower() or "reel" in label.lower():
                print(f" -> [MATCH] {label}")
            else:
                print(f" -> {label}")
                
        # Cerca testi generici nella pagina
        body_text = page.locator('body').inner_text()
        print(f"[Debug] Lunghezza testo della pagina: {len(body_text)} caratteri.")
        print("[Debug] Primi 500 caratteri di testo della pagina:")
        print(body_text[:500])
        
    except Exception as e:
        print(f"[Debug] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_drive()
