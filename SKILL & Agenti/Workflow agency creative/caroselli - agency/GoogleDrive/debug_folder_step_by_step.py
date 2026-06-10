import os
import sys
import time

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def debug_step():
    print("[*] Avvio BrowserManager per test sequenza...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(8)
        
        # Click Nuovo
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.click(force=True)
        time.sleep(2)
        
        # Click Nuova cartella
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder')").first
        folder_option.click(force=True)
        time.sleep(3)
        page.screenshot(path="confirm_modal_visible.png")
        print("[V] Salvato screenshot del modale di conferma.")
        
        # Click Crea e condividi
        confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
        if confirm_btn.is_visible():
            print("[*] Clicco su Crea e condividi...")
            confirm_btn.click(force=True)
            time.sleep(4)
            page.screenshot(path="after_confirm_clicked.png")
            print("[V] Salvato screenshot dopo il click su Crea e condividi.")
            
            # Cerca se c'è un input nel dom
            inputs = page.locator("input").all()
            print(f"Trovati {len(inputs)} input totali dopo il click.")
            for i, inp in enumerate(inputs):
                try:
                    print(f"Input {i}: Visible={inp.is_visible()}, Type='{inp.get_attribute('type')}', Label='{inp.get_attribute('aria-label')}', Placeholder='{inp.get_attribute('placeholder')}', Value='{inp.get_attribute('value')}'")
                except: pass
                
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    debug_step()
