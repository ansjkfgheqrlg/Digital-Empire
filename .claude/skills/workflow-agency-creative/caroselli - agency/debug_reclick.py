import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def run_debug():
    print("[*] Avvio BrowserManager per debug ricarica/riclicca...")
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
        time.sleep(2.5)
        
        # Click Nuova cartella
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder')").first
        folder_option.click(force=True)
        time.sleep(3)
        page.screenshot(path="reclick_step_1_modal.png")
        
        # Click Crea e condividi
        share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
        if share_confirm_btn.is_visible():
            print("[*] Modal visibile. Clicco Crea e condividi...")
            share_confirm_btn.click(force=True)
            time.sleep(4) # lascia svanire il backdrop
            page.screenshot(path="reclick_step_2_dismissed.png")
            
            # Riapri Nuovo
            print("[*] Clicco su Nuovo...")
            nuovo_btn.click(force=True)
            time.sleep(3)
            page.screenshot(path="reclick_step_3_clicked_nuovo.png")
            
            # Click Nuova cartella
            print("[*] Clicco su Nuova cartella...")
            folder_option.click(force=True)
            time.sleep(3.5)
            page.screenshot(path="reclick_step_4_after_reclick.png")
            
            # Controlla input
            inputs = page.locator("input").all()
            for i, inp in enumerate(inputs):
                try:
                    if inp.is_visible():
                        print(f"Input {i}: Visible={inp.is_visible()}, Value='{inp.get_attribute('value')}', Label='{inp.get_attribute('aria-label')}'")
                except: pass
        else:
            print("[*] Modal non visibile.")
            
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    run_debug()
