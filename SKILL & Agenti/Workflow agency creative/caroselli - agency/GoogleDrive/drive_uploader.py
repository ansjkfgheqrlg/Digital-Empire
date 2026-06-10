import os
import sys
import time

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def upload_carousel(local_folder_path, topic_name, descrizione="", headless=False):
    print(f"[Drive] Avvio procedura di upload per: {topic_name}")
    manager = BrowserManager('GoogleDrive', headless=headless)
    
    try:
        context = manager.get_context()
        page = manager.new_page(context)
        
        # Navigazione diretta verso la cartella finale fornita dall'utente
        target_url = "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq"
        print(f"[Drive] Navigazione diretta verso la cartella: {target_url}")
        page.goto(target_url, timeout=60000, wait_until='domcontentloaded')
        
        # Attendi che il pulsante "Nuovo" sia visibile ed abilitato (non aria-disabled="true")
        print("[Drive] Attesa caricamento completo di Google Drive...")
        try:
            page.wait_for_load_state("networkidle", timeout=12000)
        except:
            pass
        time.sleep(5) 
        
        nuovo_btn = page.locator("button[aria-label='Nuovo'], button:has-text('Nuovo'), button:has-text('New')").first
        nuovo_btn.wait_for(state="visible", timeout=35000)
        
        for i in range(30):
            is_disabled = nuovo_btn.get_attribute("aria-disabled")
            if is_disabled != "true":
                break
            time.sleep(1)
        time.sleep(4) 
        
        # Crea la nuova cartella per il carosello
        print(f"[Drive] Creazione della nuova cartella: {topic_name}")
        
        folder_created = False
        for attempt in range(3):
            try:
                nuovo_btn.wait_for(state="visible", timeout=10000)
                nuovo_btn.click(force=True)
                time.sleep(3)
                
                folder_option = page.locator("[role='menuitem']:visible").filter(has_text="Nuova cartella").first
                if not folder_option.count():
                    folder_option = page.locator("[role='menuitem']:visible").filter(has_text="New folder").first
                folder_option.wait_for(state="visible", timeout=8000)
                folder_option.click(force=True)
                time.sleep(3)
                
                share_title = page.locator("text=Creare in una cartella condivisa?").first
                if share_title.is_visible():
                    share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
                    share_confirm_btn.click(force=True)
                    time.sleep(3)
                
                input_name = page.locator("input[aria-label*='cartella']:visible, input[aria-label*='folder']:visible, input[value='Cartella senza titolo']:visible, input[value='Cartella senza nome']:visible, input[value='Untitled folder']:visible").first
                input_name.wait_for(state="visible", timeout=10000)
                input_name.fill(topic_name)
                time.sleep(2)
                
                create_btn = page.locator("dialog button:has-text('Crea'), dialog button:has-text('Create'), button:has-text('Crea'):visible, button:has-text('Create'):visible").last
                create_btn.wait_for(state="visible", timeout=5000)
                create_btn.click(force=True)
                time.sleep(6)
                folder_created = True
                print("[Drive] Cartella creata con successo.")
                break
            except Exception as loop_err:
                print(f"[Drive] Errore nel tentativo {attempt+1}: {loop_err}. Riprovo...")
                page.keyboard.press("Escape")
                time.sleep(3)
                
        if not folder_created:
            raise Exception("Impossibile creare la nuova cartella su Google Drive.")

        # Entra nella nuova cartella
        print(f"[Drive] Entro nella cartella {topic_name}...")
        new_folder = page.locator(
            f'div[role="gridcell"] div[aria-label*="{topic_name}"],'
            f'div[role="row"] span:has-text("{topic_name}"),'
            f'div[role="gridcell"] span:has-text("{topic_name}"),'
            f'div[role="gridcell"] div:has-text("{topic_name}")'
        ).first
        new_folder.wait_for(state="visible", timeout=15000)
        new_folder.dblclick(force=True)
        time.sleep(6)
        
        # Carica i file contenuti nella cartella locale
        print(f"[Drive] Inizio upload dei file...")
        files_to_upload = [os.path.join(local_folder_path, f) for f in os.listdir(local_folder_path) if os.path.isfile(os.path.join(local_folder_path, f))]
        
        if files_to_upload:
            nuovo_btn.wait_for(state="visible", timeout=25000)
            nuovo_btn.click(force=True)
            time.sleep(3)
            
            upload_option = page.locator("[role='menuitem']:visible").filter(has_text="Caricamento di file").first
            if not upload_option.count():
                upload_option = page.locator("[role='menuitem']:visible").filter(has_text="File upload").first
            upload_option.wait_for(state="visible", timeout=15000)
            
            with page.expect_file_chooser() as fc_info:
                upload_option.click(force=True)
            file_chooser = fc_info.value
            file_chooser.set_files(files_to_upload)
            
            print(f"[Drive] Upload in corso di {len(files_to_upload)} file. Attesa 20s...")
            time.sleep(20) 
            print("[Drive] Upload dei file locali completato.")
            
        # Creazione del documento Google Docs nativo
        if descrizione:
            try:
                print("[Drive] Creazione del documento Google Docs nativo...")
                nuovo_btn.click(force=True)
                time.sleep(3)
                
                doc_option = page.locator("[role='menuitem']:visible").filter(has_text="Documenti Google").first
                if not doc_option.count():
                    doc_option = page.locator("[role='menuitem']:visible").filter(has_text="Google Docs").first
                doc_option.wait_for(state="visible", timeout=10000)
                
                with context.expect_page() as new_page_info:
                    doc_option.click(force=True)
                    share_confirm_btn = None
                    for _ in range(10):
                        t1 = page.locator("text=Creare in una cartella condivisa?").first
                        t2 = page.locator("text=Create in a shared folder?").first
                        if t1.is_visible() or t2.is_visible():
                            share_confirm_btn = page.locator("button:has-text('Crea e condividi'), button:has-text('Create and share')").first
                            break
                        time.sleep(0.5)
                    if share_confirm_btn and share_confirm_btn.is_visible():
                        share_confirm_btn.click(force=True)
                doc_page = new_page_info.value
                
                print("[Drive] Attesa caricamento editor Google Docs...")
                doc_page.wait_for_load_state("domcontentloaded")
                time.sleep(12)
                
                # Rinomina
                title_input = doc_page.locator("input.docs-title-input").first
                title_input.wait_for(state="visible", timeout=20000)
                title_input.click(force=True)
                time.sleep(2)
                doc_page.keyboard.press("Control+A")
                doc_page.keyboard.type("Descrizione Post")
                doc_page.keyboard.press("Enter")
                time.sleep(2)
                
                # Focus e Type
                print("[Drive] Incollo il testo della descrizione...")
                try:
                    editor = doc_page.locator(".docs-texteventtarget").first
                    editor.wait_for(state="attached", timeout=10000)
                    editor.focus()
                    time.sleep(1)
                except:
                    print("[Drive] Fallback: click al centro dell'editor per il focus...")
                    doc_page.mouse.click(600, 450)
                    time.sleep(1)
                
                doc_page.keyboard.type(descrizione)
                time.sleep(8)
                doc_page.close()
                print("[Drive] [V] Google Docs creato con successo!")
            except Exception as doc_err:
                print(f"[Drive] Attenzione: Errore Google Doc ({doc_err}). descrizione.txt è caricato.")
            
    except Exception as e:
        print(f"[Drive] Errore critico Drive: {e}")
    finally:
        manager.close()
