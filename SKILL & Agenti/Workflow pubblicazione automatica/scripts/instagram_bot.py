import time
import os
from .browser_manager import BrowserManager

def publish_to_instagram(file_path, caption, headless=True):
    print(f"[Instagram] Inizio pubblicazione...")
    manager = BrowserManager(headless=headless)
    
    try:
        context = manager.get_context('instagram')
        page = context.new_page()
        
        # 1. Vai alla homepage
        page.goto("https://www.instagram.com/")
        page.wait_for_load_state('networkidle')
        
        # 2. Clicca su "Crea" (Nuovo post)
        # Nota: I selettori di Instagram cambiano spesso. Questo usa l'aria-label o il testo.
        create_btn = page.locator('svg[aria-label="Nuovo post"]').first
        if not create_btn.is_visible():
            create_btn = page.get_by_role("link", name="Crea")
        
        create_btn.click()
        time.sleep(2)
        
        # 3. Carica il file
        # Instagram usa un input file nascosto
        with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="Seleziona dal computer").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        time.sleep(2)
        
        # 4. Prosegui (clicca "Avanti" due volte)
        # Clicca Avanti per il crop
        page.get_by_role("button", name="Avanti").click()
        time.sleep(2)
        
        # Clicca Avanti per i filtri
        page.get_by_role("button", name="Avanti").click()
        time.sleep(2)
        
        # 5. Inserisci la caption
        # Seleziona l'area di testo (aria-label "Scrivi una didascalia...")
        caption_area = page.get_by_role("textbox", name="Scrivi una didascalia...")
        caption_area.fill(caption)
        time.sleep(2)
        
        # 6. Clicca "Condividi"
        page.get_by_role("button", name="Condividi").click()
        
        # Attendi che il post sia condiviso
        print("[Instagram] Condivisione in corso...")
        page.get_by_text("Il tuo post è stato condiviso.").wait_for(timeout=60000)
        print("[Instagram] Post pubblicato con successo!")
        
        time.sleep(3)
        
    except Exception as e:
        print(f"[Instagram] Errore durante la pubblicazione: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    # Test (solo a scopo di debug)
    # publish_to_instagram("percorso/al/file.mp4", "Caption di prova", headless=False)
    pass
