import time
import os
from .browser_manager import BrowserManager

def publish_to_tiktok(file_path, caption, headless=True):
    print(f"[TikTok] Inizio pubblicazione...")
    manager = BrowserManager(headless=headless)
    
    try:
        context = manager.get_context('tiktok')
        page = context.new_page()
        
        # 1. Vai alla pagina di upload
        page.goto("https://www.tiktok.com/creator-center/upload?from=upload")
        page.wait_for_load_state('networkidle')
        time.sleep(5) # Attendi il caricamento dell'iframe o dell'interfaccia
        
        # TikTok spesso inserisce la logica di upload dentro un iframe
        # Cerchiamo l'iframe di caricamento se presente
        iframe_element = page.locator('iframe[data-tt="Upload_index_iframe"]')
        if iframe_element.is_visible():
            frame = iframe_element.content_frame
        else:
            frame = page # Se non c'è iframe, usa la pagina principale

        # 2. Carica il file
        with frame.expect_file_chooser() as fc_info:
            # Cerca il pulsante "Select video"
            frame.get_by_text("Select video").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        
        print("[TikTok] Attendere completamento upload...")
        time.sleep(10) # Tempo indicativo per upload, in una versione più robusta si controlla la UI
        
        # 3. Inserisci la caption
        # Seleziona l'editor di testo (contenteditable)
        caption_area = frame.locator('.DraftEditor-editorContainer div[contenteditable="true"]')
        # Svuota prima
        caption_area.clear()
        caption_area.fill(caption)
        time.sleep(2)
        
        # 4. Pubblica
        # Clicca il pulsante Post
        post_btn = frame.get_by_role("button", name="Post")
        post_btn.click()
        
        print("[TikTok] Cliccato Pubblica. Attendo conferma...")
        # Attendi notifica di successo
        time.sleep(5)
        print("[TikTok] Video pubblicato con successo!")
        
    except Exception as e:
        print(f"[TikTok] Errore durante la pubblicazione: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    pass
