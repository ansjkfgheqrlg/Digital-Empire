import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Instagram import config

def publish(file_path, caption, headless=True):
    print(f"[Instagram] Inizio pubblicazione...")
    manager = BrowserManager('Instagram', headless=headless)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://www.instagram.com/")
        page.wait_for_load_state('domcontentloaded')
        time.sleep(5)
        
        # Gestione Popup (es. "Attiva le notifiche" -> "Non ora")
        try:
            not_now_btn = page.locator('button:has-text("Non ora"), button:has-text("Not Now")').first
            if not_now_btn.is_visible(timeout=3000):
                not_now_btn.click()
                time.sleep(1)
        except Exception:
            pass
        
        # Aggiunta tag default se presente nel config
        if hasattr(config, 'DEFAULT_HASHTAGS') and config.DEFAULT_HASHTAGS:
            caption = f"{caption}\n\n{config.DEFAULT_HASHTAGS}"
            
        create_btn = page.locator('svg[aria-label="Nuovo post"], svg[aria-label="New post"]').first
        if not create_btn.is_visible():
            create_btn = page.locator('a[href="#"]').filter(has_text="Crea").first
            if not create_btn.is_visible():
                create_btn = page.locator('a[href="#"]').filter(has_text="Create").first
        
        # Force=True forza il click anche se l'elemento sembra parzialmente coperto da un div invisibile
        create_btn.click(force=True)
        time.sleep(2)
        
        with page.expect_file_chooser(timeout=60000) as fc_info:
            select_btn = page.locator('button:has-text("Seleziona dal computer"), button:has-text("Select from computer")').first
            select_btn.wait_for(state="visible", timeout=30000)
            select_btn.click(force=True)
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        time.sleep(2)
        
        page.get_by_role("button", name="Avanti").click()
        time.sleep(2)
        page.get_by_role("button", name="Avanti").click()
        time.sleep(2)
        
        caption_area = page.get_by_role("textbox", name="Scrivi una didascalia...")
        caption_area.fill(caption)
        time.sleep(2)
        
        page.get_by_role("button", name="Condividi").click()
        
        print("[Instagram] Condivisione in corso...")
        page.get_by_text("Il tuo post è stato condiviso.").wait_for(timeout=60000)
        print("[Instagram] Post pubblicato con successo!")
        time.sleep(3)
        
    except Exception as e:
        print(f"[Instagram] Errore: {e}")
    finally:
        manager.close()
