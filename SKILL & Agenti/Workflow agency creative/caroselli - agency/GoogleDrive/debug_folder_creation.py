import os
import sys
import time

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def debug_creation():
    print("[*] Avvio BrowserManager per debug creazione cartella...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        print(f"[*] Navigazione verso: {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(10)
        page.screenshot(path="step_1_home.png")
        
        # Clicca Nuovo
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.wait_for(state="visible", timeout=30000)
        nuovo_btn.click(force=True)
        time.sleep(3)
        page.screenshot(path="step_2_clicked_nuovo.png")
        
        # Clicca Nuova cartella
        folder_option = page.locator("span:has-text('Nuova cartella'), span:has-text('New folder'), div:has-text('Nuova cartella'), div:has-text('New folder')").first
        folder_option.wait_for(state="visible", timeout=10000)
        folder_option.click(force=True)
        time.sleep(3)
        page.screenshot(path="step_3_clicked_folder_option.png")
        
        # Inserisci nome
        input_name = page.locator("input[aria-label='Nome cartella']:visible, input[aria-label='Folder name']:visible, input[value='Cartella senza nome']:visible, input[value='Untitled folder']:visible, input[type='text']:visible").first
        input_name.wait_for(state="visible", timeout=10000)
        input_name.fill("Test_Debug_Folder")
        time.sleep(2)
        page.screenshot(path="step_4_filled_name.png")
        
        # Clicca Crea
        create_btn = page.locator("button:has-text('Crea'), button:has-text('Create')").first
        create_btn.wait_for(state="visible", timeout=10000)
        create_btn.click(force=True)
        time.sleep(6)
        page.screenshot(path="step_5_clicked_create.png")
        
        # Ricarica pagina e controlla se esiste
        page.reload(wait_until="domcontentloaded")
        time.sleep(10)
        page.screenshot(path="step_6_after_reload.png")
        
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    debug_creation()
