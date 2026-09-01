import os
import sys
import time

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def run_debug():
    print("[*] Avvio BrowserManager per debug creazione cartella...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(10)
        page.screenshot(path="real_step_1_home.png")
        
        # Clicca Nuovo
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.click(force=True)
        time.sleep(3)
        page.screenshot(path="real_step_2_clicked_nuovo.png")
        
        # Clicca Nuova cartella
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder')").first
        folder_option.click(force=True)
        time.sleep(3)
        page.screenshot(path="real_step_3_clicked_folder_option.png")
        
        # Controlla modal condivisione
        share_title = page.locator("text=Creare in una cartella condivisa?").first
        print(f"[*] share_title.is_visible() = {share_title.is_visible()}")
        if share_title.is_visible():
            print("[*] Rilevato modale cartella condivisa. Clicco 'Crea e condividi'...")
            share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
            share_confirm_btn.click(force=True)
            time.sleep(3)
            page.screenshot(path="real_step_4_after_share_confirm.png")
            
        # Trova gli input visibili
        print("\n--- INPUT VISIBILI ORA ---")
        inputs = page.locator("input").all()
        for i, inp in enumerate(inputs):
            try:
                print(f"Input {i}: Visible={inp.is_visible()}, Type='{inp.get_attribute('type')}', Label='{inp.get_attribute('aria-label')}', Placeholder='{inp.get_attribute('placeholder')}', Value='{inp.get_attribute('value')}'")
            except: pass
            
        # Inserisci il nome
        input_name = page.locator("input[aria-label*='cartella']:visible, input[aria-label*='folder']:visible, input[value='Cartella senza titolo']:visible, input[value='Cartella senza nome']:visible, input[value='Untitled folder']:visible").first
        if input_name.is_visible():
            print("[*] Trovato input specifico. Inserisco testo...")
            input_name.fill("Test_Real_Folder")
            time.sleep(2)
            page.screenshot(path="real_step_5_filled_name.png")
            
            # Clicca crea
            create_btn = page.locator("dialog button:has-text('Crea'), dialog button:has-text('Create'), button:has-text('Crea'):visible, button:has-text('Create'):visible").last
            print(f"[*] Clicco su crea: text='{create_btn.inner_text().strip()}'")
            create_btn.click(force=True)
            time.sleep(5)
            page.screenshot(path="real_step_6_after_create.png")
        else:
            print("[X] Input specifico NON visibile!")
            
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    run_debug()
