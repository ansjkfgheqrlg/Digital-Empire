import os
import sys
import time
import glob

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def test_upload_button():
    print("[*] Avvio BrowserManager per testare l'upload degli allegati...")
    manager = BrowserManager('ArenaAI', headless=True)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        url = "https://arena.ai/"
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(5)
        
        # 1. Setup completo
        visible_btn = None
        for btn in page.locator("button, p, span").all():
            try:
                if btn.is_visible() and btn.inner_text().strip() == "Battle Mode":
                    visible_btn = btn
                    break
            except:
                pass
        if visible_btn:
            visible_btn.click(force=True)
            time.sleep(2)
            
        for opt in page.locator("[role='option']").all():
            try:
                if opt.is_visible() and opt.inner_text().strip().startswith("Direct"):
                    opt.click(force=True)
                    break
            except:
                pass
        time.sleep(4)
        
        # Attiva Image Modality
        image_btn = page.locator("button[aria-label='Image'], button[title='Image']").first
        if image_btn.is_visible():
            image_btn.click(force=True)
            time.sleep(3)
        else:
            image_btn2 = page.locator("button[data-modality-button='true']").first
            if image_btn2.is_visible():
                image_btn2.click(force=True)
                time.sleep(3)
                
        # 2. Cerca file di contesto
        allegati_files = glob.glob(os.path.join(config.ALLEGATI_DIR, "*.*"))
        if not allegati_files:
            print("[X] Nessun file trovato in 'allegati di contesto (slide)'!")
            return
            
        print(f"[V] Trovati {len(allegati_files)} file da caricare: {allegati_files}")
        
        # 3. Trova l'input type=file o il bottone Add files
        print("[*] Cerco di attivare il file chooser...")
        
        # Vediamo se c'è un input type=file
        file_inputs = page.locator("input[type='file']").all()
        print(f"Trovati {len(file_inputs)} input di tipo file in DOM.")
        
        upload_success = False
        try:
            with page.expect_file_chooser(timeout=5000) as fc_info:
                # Prova ad avviare cliccando sul bottone visivo di upload (paperclip)
                add_files_btn = page.locator("button:has-text('Add files'), button[aria-label='Add files and more']").first
                if add_files_btn.is_visible():
                    print("[V] Clicco sul pulsante Add files...")
                    add_files_btn.click(force=True)
                else:
                    print("[*] Bottone Add files non trovato o non visibile, provo con l'input file nascosto...")
                    page.locator("input[type='file']").first.click(force=True)
                    
            fc_info.value.set_files(allegati_files[:2]) # Carica solo i primi 2 per test
            print("[V] File inviati al file chooser con successo!")
            time.sleep(5)
            upload_success = True
        except Exception as e:
            print(f"[X] Fallimento nell'usare expect_file_chooser: {e}")
            
        page.screenshot(path=os.path.join(root_dir, "arena_upload_test.png"))
        print("[V] Screenshot salvato in 'arena_upload_test.png'")
        
    except Exception as e:
        print(f"[X] Errore: {e}")
    finally:
        manager.close()

if __name__ == "__main__":
    test_upload_button()
