import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from LinkedIn import config

def publish(file_path, caption, headless=True):
    print(f"[LinkedIn] Inizio pubblicazione...")
    manager = BrowserManager('LinkedIn', headless=headless)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_load_state('networkidle')
        
        # Clicca su "Avvia un post"
        start_post_btn = page.locator('button:has-text("Avvia un post"), button:has-text("Start a post")').first
        if not start_post_btn.is_visible():
             # Fallback selettore
             start_post_btn = page.locator('span:has-text("Avvia un post"), span:has-text("Start a post")').first
        start_post_btn.click()
        time.sleep(2)

        # Seleziona il caricamento di un documento (LinkedIn preferisce PDF per i caroselli)
        # Se è un'immagine/video, si clicca sul tasto Media. Assumiamo che per i caroselli sia PDF o Immagini.
        # Adatteremo questo in base al file fornito.
        add_media_btn = page.locator('button[aria-label="Aggiungi file multimediale"], button[aria-label="Add media"]').first
        if not add_media_btn.is_visible():
             add_media_btn = page.get_by_role("button", name="Aggiungi file multimediale")

        with page.expect_file_chooser() as fc_info:
            add_media_btn.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        time.sleep(3)
        
        # Clicca Successivo/Avanti
        next_btn = page.locator('button:has-text("Successivo"), button:has-text("Next")').first
        if next_btn.is_visible():
            next_btn.click()
        time.sleep(2)
        
        # Inserisci la caption
        caption_area = page.locator('div[role="textbox"]')
        caption_area.fill(caption)
        time.sleep(2)
        
        # Clicca Pubblica
        post_btn = page.locator('button:has-text("Pubblica"), button:has-text("Post")').first
        post_btn.click()
        
        print("[LinkedIn] Pubblicazione in corso...")
        time.sleep(5) # Attendi l'animazione di completamento
        print("[LinkedIn] Post pubblicato con successo!")
        
    except Exception as e:
        print(f"[LinkedIn] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    pass
