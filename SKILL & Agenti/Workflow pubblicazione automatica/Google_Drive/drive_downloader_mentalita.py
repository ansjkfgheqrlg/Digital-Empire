import time
import sys
import os
import json

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
from Google_Drive import config

# Usiamo un file storico separato per i video
HISTORY_PATH = os.path.join(os.path.dirname(__file__), "published_history_mentalita.json")

def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(history_list):
    with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(history_list, f, indent=4)

def download_next_video(headless=True):
    print(f"[Drive] Avvio ricerca nuovi Video/Reel Mentalità Brutale...")
    history = load_history()
    
    # IMPORTANTE: Usiamo la STESSA cartella di sessione di Google Drive (perché l'account è lo stesso)
    manager = BrowserManager('Google_Drive', headless=headless)
    
    downloaded_folder_path = None
    topic_name = None
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        # 1. Naviga direttamente alla cartella dei Reel
        print(f"[Drive] Apertura cartella Reel: {config.DRIVE_MENTALITA_URL}")
        page.goto(config.DRIVE_MENTALITA_URL)
        page.wait_for_load_state('domcontentloaded')
        time.sleep(10) # Drive è pesante da caricare
        
        # 2. Trova i file video (sono righe nella lista di Drive)
        # In Drive, i nomi dei file sono in elementi con aria-label
        # Cerchiamo tutti gli elementi che potrebbero essere file video
        print("[Drive] Scansione contenuti...")
        
        # Cerchiamo elementi che terminano con estensioni video comuni
        # Nota: Drive usa aria-label="Nomefile.mp4"
        locators = page.locator('div[aria-label$=".mp4"], div[aria-label$=".mov"], div[aria-label$=".MP4"]')
        count = locators.count()
        
        if count == 0:
            # Fallback: prova a cercare elementi generici e filtra per testo
            print("[Drive] Nessun file .mp4 trovato col selettore rapido. Provo scansione profonda...")
            locators = page.locator('div[role="row"]')
            count = locators.count()

        # Lista di nomi da ignorare (es. cartelle di servizio)
        ignore_list = ["Pubblicati", "pubblicati", "Cartella", "Folder"]

        for i in range(count):
            label = locators.nth(i).get_attribute("aria-label")
            if not label:
                # Se usiamo il fallback role="row", dobbiamo cercare il testo dentro
                label = locators.nth(i).inner_text().split('\n')[0]
            
            # Se la label è vuota o è una cartella da ignorare, saltiamo
            if not label or any(ignore_word in label for ignore_word in ignore_list):
                continue
            
            # In Drive, i file video di solito non hanno "Cartella" nell'aria-label.
            # Pulizia nome file
            clean_name = label.replace('.mp4', '').replace('.mov', '').replace('.MP4', '').strip()
            if not clean_name:
                # Se l'utente ha chiamato il file letteralmente ".mp4", togliendo l'estensione rimane vuoto.
                # In questo caso, usiamo la label originale come nome.
                clean_name = label.strip()
            
            if clean_name not in history:
                print(f"[Drive] Trovato nuovo video da pubblicare: {label}")
                topic_name = clean_name
                target_locator = locators.nth(i)
                
                # 3. Seleziona il file e clicca Download
                print(f"[Drive] Avvio download di: {label}")
                # Clic normale per focalizzare l'elemento
                target_locator.click()
                time.sleep(1)
                
                try:
                    # 1. Tenta di cliccare sui tre puntini se visibili, altrimenti tasto destro
                    more_actions_btn = target_locator.locator('button[aria-label="Altre azioni"], button[aria-label="More actions"]').first
                    if more_actions_btn.is_visible(timeout=2000):
                        print("[Drive] Clicco sui tre puntini (Altre azioni)...")
                        more_actions_btn.click()
                    else:
                        print("[Drive] Tre puntini non trovati, uso il tasto destro...")
                        target_locator.click(button="right")
                    
                    time.sleep(2) # Aspettiamo che il menu si apra
                    
                    # 2. Cerca l'opzione Scarica (usando un selettore testo flessibile)
                    print("[Drive] Cerco il bottone 'Scarica' nel menu...")
                    download_btn = page.locator('text="Scarica"').last
                    if not download_btn.is_visible(timeout=2000):
                        download_btn = page.locator('text="Download"').last
                    
                    # 3. Avvia il download e gestisci eventuale popup "Scarica comunque" (Virus Scan)
                    with page.expect_download(timeout=90000) as download_info:
                        download_btn.click()
                        time.sleep(2)
                        
                        # Controlla se appare il fastidioso popup di Google Drive per i file di grandi dimensioni
                        virus_btn = page.locator('button:has-text("Scarica comunque"), button:has-text("Download anyway")').first
                        try:
                            if virus_btn.is_visible(timeout=3000):
                                print("[Drive] Rilevato popup 'Scarica comunque', lo clicco...")
                                virus_btn.click()
                        except:
                            pass
                    
                    download = download_info.value
                    
                    # 4. Salvataggio
                    downloaded_folder_path = os.path.join(root_dir, "downloads_temp", "mentalita", topic_name)
                    os.makedirs(downloaded_folder_path, exist_ok=True)
                    video_path = os.path.join(downloaded_folder_path, label)
                    
                    # Se il nome estratto non ha l'estensione, forziamola a mp4
                    if not video_path.lower().endswith('.mp4') and not video_path.lower().endswith('.mov'):
                        video_path += ".mp4"
                        
                    download.save_as(video_path)
                    print(f"[Drive] Download completato: {video_path}")
                    
                    history.append(topic_name)
                    save_history(history)
                    break
                    
                except Exception as e_down:
                    print(f"[Drive] Errore durante il download col menu: {e_down}")
                    # Fallback estremo: Scorciatoia da tastiera 'd'
                    try:
                        print("[Drive] Tento download estremo con scorciatoia 'd'...")
                        with page.expect_download(timeout=90000) as download_info:
                            page.keyboard.press("d")
                            time.sleep(2)
                            # Controllo popup anche qui
                            virus_btn = page.locator('button:has-text("Scarica comunque"), button:has-text("Download anyway")').first
                            try:
                                if virus_btn.is_visible(timeout=3000):
                                    print("[Drive] Rilevato popup 'Scarica comunque', lo clicco...")
                                    virus_btn.click()
                            except:
                                pass
                                
                        download = download_info.value
                        
                        downloaded_folder_path = os.path.join(root_dir, "downloads_temp", "mentalita", topic_name)
                        os.makedirs(downloaded_folder_path, exist_ok=True)
                        video_path = os.path.join(downloaded_folder_path, label)
                        if not video_path.lower().endswith('.mp4') and not video_path.lower().endswith('.mov'):
                            video_path += ".mp4"
                            
                        download.save_as(video_path)
                        print(f"[Drive] Download completato con scorciatoia: {video_path}")
                        history.append(topic_name)
                        save_history(history)
                        break
                    except Exception as e_kbd:
                        print(f"[Drive] Fallito anche con scorciatoia: {e_kbd}")
                        continue

        if not topic_name:
            print("[Drive] Nessun nuovo video trovato o tutti già pubblicati.")
            return None, None
            
    except Exception as e:
        print(f"[Drive] Errore generale: {e}")
    finally:
        manager.close()
        
    return downloaded_folder_path, topic_name

if __name__ == "__main__":
    download_next_video(headless=False)
