import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Instagram_Mentalita import config

def publish(file_path, caption, headless=True):
    print(f"[Instagram Mentalità] Inizio pubblicazione Reel...")
    manager = BrowserManager('Instagram_Mentalita', headless=headless)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://www.instagram.com/")
        page.wait_for_load_state('domcontentloaded')
        time.sleep(5)
        
        # Gestione Popup
        try:
            not_now_btn = page.locator('button:has-text("Non ora"), button:has-text("Not Now")').first
            if not_now_btn.is_visible(timeout=3000):
                not_now_btn.click()
                time.sleep(1)
        except:
            pass
            
        create_btn = page.locator('svg[aria-label="Nuovo post"], svg[aria-label="New post"]').first
        if not create_btn.is_visible():
            create_btn = page.locator('a[href="#"]').filter(has_text="Crea").first
            if not create_btn.is_visible():
                create_btn = page.locator('a[href="#"]').filter(has_text="Create").first
        
        create_btn.click(force=True)
        time.sleep(3)
        
        # Gestione del sottomenu di Instagram (Post, Video in diretta, ecc.)
        modal_opened = False
        try:
            print("[Instagram Mentalità] Ricerca del pulsante 'Post' nel sottomenu...")
            post_spans = page.locator('span').filter(has_text="Post")
            count = post_spans.count()
            
            for i in range(count):
                span = post_spans.nth(i)
                if span.is_visible():
                    print(f"[Instagram Mentalità] Tento il clic sullo span 'Post' visibile ind. {i}...")
                    span.click()
                    time.sleep(3)
                    
                    # Controlla se la modale è apparsa
                    select_btn = page.locator('button:has-text("Seleziona dal computer"), button:has-text("Select from computer")').first
                    if select_btn.is_visible():
                        print("[Instagram Mentalità] Modale di caricamento aperta con successo!")
                        modal_opened = True
                        break
                    else:
                        print("[Instagram Mentalità] Modale non aperta, provo il prossimo span...")
                        # Se non si è aperta, riapriamo il menu
                        create_btn.click(force=True)
                        time.sleep(2)
        except Exception as e_submenu:
            print(f"[Instagram Mentalità] Errore durante la navigazione del sottomenu: {e_submenu}")
            
        # Fallback se il sottomenu non era presente o non è stato attivato dal ciclo
        if not modal_opened:
            print("[Instagram Mentalità] Avvio fallback standard per modale di caricamento...")
            
        with page.expect_file_chooser(timeout=60000) as fc_info:
            select_btn = page.locator('button:has-text("Seleziona dal computer"), button:has-text("Select from computer")').first
            select_btn.wait_for(state="visible", timeout=30000)
            select_btn.click()
        
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        time.sleep(4) # Caricamento video richiede più tempo
        
        # Gestione Aspect Ratio per Reel (9:16)
        try:
            page.locator('svg[aria-label="Seleziona proporzioni"]').click()
            time.sleep(1)
            page.locator('span:has-text("9:16")').click()
            time.sleep(1)
        except:
            print("[Instagram Mentalità] Avviso: Impossibile impostare aspect ratio 9:16 manualmente.")

        # Clicchiamo su "Avanti" finché è presente (può essere 1 o 2 volte a seconda del layout)
        for step in range(2):
            try:
                avanti_btn = page.locator('div[role="button"]:has-text("Avanti"), button:has-text("Avanti"), [role="button"]:has-text("Avanti")').first
                if avanti_btn.is_visible(timeout=5000):
                    print(f"[Instagram Mentalità] Clicco su 'Avanti' (passo {step+1})...")
                    avanti_btn.click()
                    time.sleep(3)
                else:
                    print(f"[Instagram Mentalità] Pulsante 'Avanti' non visibile, procedo.")
                    break
            except Exception as e_avanti:
                print(f"[Instagram Mentalità] Info 'Avanti' passo {step+1}: {e_avanti}")
                break
        
        caption_area = page.get_by_role("textbox", name="Scrivi una didascalia...")
        caption_area.fill(caption)
        time.sleep(2)
        
        try:
            page.get_by_role("button", name="Condividi", exact=True).click()
        except:
            page.get_by_role("button", name="Condividi").first.click()
        
        print("[Instagram Mentalità] Condivisione Reel in corso...")
        # Attendiamo la conferma con diversi testi alternativi possibili o la sparizione della modale
        try:
            page.locator('text="Il tuo post è stato condiviso.", text="Il tuo reel è stato condiviso.", text="condiviso", text="condiviso."').first.wait_for(timeout=60000)
            print("[Instagram Mentalità] Reel pubblicato e confermato con successo!")
        except Exception as e_wait:
            print(f"[Instagram Mentalità] Attesa messaggio specifico superata ({e_wait}), verifichiamo la chiusura della modale...")
            time.sleep(5)
            # Se la modale non è più visibile, consideriamo la pubblicazione completata con successo
            create_modal = page.locator('div[role="dialog"]').first
            if not create_modal.is_visible():
                print("[Instagram Mentalità] La modale si è chiusa. Reel pubblicato con successo!")
            else:
                print("[Instagram Mentalità] Avviso: la modale è ancora aperta. Verificare manualmente lo stato.")
        time.sleep(3)
        
    except Exception as e:
        print(f"[Instagram Mentalità] Errore: {e}")
    finally:
        manager.close()
