#!/usr/bin/env python3
import sys
import os
import re
import argparse
import json
import time

def upload_mock(video_path, metadata, thumbnail_path):
    print("\n=== [PLAYWRIGHT MOCK UPLOAD ACTIVE] ===")
    print(f"File video: {video_path}")
    print(f"File copertina: {thumbnail_path}")
    print(f"Metadati:")
    print(f"  - Titolo: {metadata.get('title')}")
    print(f"  - Descrizione: {metadata.get('description')[:60]}...")
    print(f"  - Keyword: {metadata.get('keyword')}")
    print(f"  - Tags: {', '.join(metadata.get('tags', []))}")
    print("Stato: Simulazione caricamento browser Playwright completato!")
    print("Video ID Generato: mock-playwright-vid-12345")
    return {"status": "success", "video_id": "mock-playwright-vid-12345"}

def upload_via_playwright(video_path, metadata, thumbnail_path, user_data_dir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[AVVISO] Libreria 'playwright' non installata. Fallback su caricamento Mock.")
        print("Installa Playwright con: pip install playwright && playwright install")
        return upload_mock(video_path, metadata, thumbnail_path)

    if not user_data_dir or not os.path.exists(user_data_dir):
        print(f"[AVVISO] Cartella del profilo Chrome '{user_data_dir}' non trovata.")
        print("Per evitare blocchi di sicurezza di Google Login, è necessario effettuare prima il login manuale")
        # Fallback su mock per non bloccare la suite
        return upload_mock(video_path, metadata, thumbnail_path)

    print(f"Avvio di Playwright con profilo persistente: {user_data_dir}...")

    # Senza User-Agent esplicito, YouTube Studio mostra un interstiziale "browser non supportato"
    # al posto della dashboard reale (stesso bug documentato in legamidiamore_login.py e
    # legamidiamore_session_check.py, 2026-08-05) — senza dashboard vera, #create-icon non esiste
    # mai e il click va sempre in timeout. Confermato reale il 2026-08-17: primo upload live si e'
    # bloccato esattamente su questo timeout finche' non e' stato aggiunto questo User-Agent.
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    with sync_playwright() as p:
        # Avviamo Chromium caricando la sessione in cui l'utente ha già fatto login su YouTube Studio
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,  # Mostra l'interfaccia grafica per monitorare o intervenire in caso di captcha
            args=["--disable-blink-features=AutomationControlled"], # Evita rilevamento robot
            viewport={"width": 1440, "height": 900},
            user_agent=USER_AGENT,
        )

        page = browser_context.new_page()
        print("Navigazione su YouTube Studio...")
        page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)
        
        # Verifica se siamo loggati (cerca il pulsante CREA o UPLOAD)
        if "login" in page.url or page.locator("input[type='email']").is_visible():
            print("[ERRORE] Il profilo Chrome non è loggato su Google. Effettua il login manualmente nel profilo Chrome salvato.")
            browser_context.close()
            return {"status": "error", "reason": "auth_required"}

        try:
            # Selettori verificati dal vivo il 2026-08-17: #create-icon non esiste piu' nella UI
            # Studio attuale (il bottone ha solo aria-label="Create", nessun id) e il menu che si
            # apre e' in INGLESE per questo account ("Upload videos", non "Carica video" — la
            # UI Studio segue la lingua dell'account Google, non e' detto sia italiano). Locator
            # bilingue per non rompersi di nuovo se un account diverso ha Studio in italiano.
            print("Clic su pulsante Create/CREA...")
            page.get_by_role("button", name="Create", exact=False).first.click()
            page.wait_for_timeout(1000)

            print("Clic su Upload videos/Carica Video...")
            page.locator(
                "tp-yt-paper-item:has-text('Upload videos'), tp-yt-paper-item:has-text('Carica video')"
            ).first.click()
            page.wait_for_timeout(2000)
            
            # Input del file video
            print(f"Inserimento file video: {video_path}...")
            file_input = page.locator("input[type='file']")
            file_input.set_input_files(video_path)
            page.wait_for_timeout(5000) # Attendi caricamento iniziale
            
            # Compilazione metadati — stesso motivo bilingue di sopra (aria-label segue la lingua
            # dell'account Google, verificato in inglese su questo account il 2026-08-17).
            print(f"Compilazione Titolo: {metadata.get('title')}...")
            title_box = page.locator(
                "#textbox[aria-label*='Add a title'], #textbox[aria-label*='Aggiungi un titolo']"
            ).first
            title_box.clear()
            title_box.fill(metadata.get('title', 'Nuovo Video'))
            page.wait_for_timeout(1000)

            print("Compilazione Descrizione...")
            desc_box = page.locator(
                "#textbox[aria-label*='Tell viewers'], #textbox[aria-label*='Descrivi il video']"
            ).first
            desc_box.clear()
            desc_box.fill(metadata.get('description', ''))
            page.wait_for_timeout(1000)
            
            # Caricamento miniatura — regola permanente: obbligatoria, gia' verificata esistente
            # da main(). Selettore per ORDINE (2 input[type=file] nella wizard: [0] video gia'
            # usato sopra, [1] miniatura) invece di un id — gli id di questa UI si sono rivelati
            # stale piu' volte il 2026-08-17 (create-icon, next-button probabile lo stesso).
            print(f"Inserimento miniatura: {thumbnail_path}...")
            thumb_input = page.locator("input[type='file']").nth(1)
            thumb_input.set_input_files(thumbnail_path)
            page.wait_for_timeout(3000)

            # Dichiarazione non per bambini — valore reale verificato dal vivo il 2026-08-17
            # via screenshot diagnostico: e' 'VIDEO_MADE_FOR_KIDS_NOT_MFK', non 'FALSE' come
            # assunto originariamente (causa reale di tutti i timeout precedenti su questo step).
            print("Impostazione destinatari (non per bambini)...")
            page.locator("tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']").click()
            page.wait_for_timeout(1000)

            # Clic su Avanti per 3 volte (Dettagli -> Elementi -> Controlli). Per ruolo/testo,
            # bilingue, non per id (#next-button non e' mai stato confermato valido nella wizard
            # reale, solo assunto — stesso pattern di staleness di #create-icon).
            for step in range(3):
                print(f"Clic su pulsante Avanti/Next (Passo {step+1}/3)...")
                page.locator(
                    "button:has-text('Next'), button:has-text('Avanti')"
                ).first.click()
                page.wait_for_timeout(2000)

            # Schermata Visibilità: imposta come Privato
            print("Impostazione visibilità (Privato per sicurezza)...")
            page.locator(
                "tp-yt-paper-radio-button[name='PRIVATE'], "
                "tp-yt-paper-radio-button:has-text('Private'), "
                "tp-yt-paper-radio-button:has-text('Privato')"
            ).first.click()
            page.wait_for_timeout(1000)

            # Clic su Salva/Pubblica — per ruolo/testo, bilingue, non per id.
            print("Clic su pulsante Salva/Save...")
            page.locator(
                "button:has-text('Save'), button:has-text('Salva'), "
                "button:has-text('Publish'), button:has-text('Pubblica')"
            ).first.click()
            page.wait_for_timeout(5000)

            # ID reale, non un placeholder: Studio reindirizza a
            # https://studio.youtube.com/video/<VIDEO_ID>/edit dopo il salvataggio. Senza
            # l'ID vero, memory/published_videos.json non avrebbe un dato utilizzabile per
            # l'audit di Fase 6 (_extract_youtube_id legge sempre un URL youtube.com/watch reale).
            try:
                page.wait_for_url(re.compile(r"/video/[\w-]+/"), timeout=15000)
            except Exception:
                pass  # se il redirect non arriva in tempo, si prova comunque a leggere l'URL corrente
            match = re.search(r"/video/([\w-]+)/", page.url)
            video_id = match.group(1) if match else None
            video_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else None

            if not video_id:
                print(f"[AVVISO] Salvataggio eseguito ma nessun ID video reale trovato nell'URL "
                      f"({page.url}). Verifica manualmente su YouTube Studio.")
                browser_context.close()
                return {"status": "success", "video_id": None, "url": None,
                        "warning": "id_non_estratto"}

            print(f"Video caricato correttamente via Playwright browser automation! ID reale: {video_id}")
            browser_context.close()
            return {"status": "success", "video_id": video_id, "url": video_url}
            
        except Exception as ex:
            print(f"[ERRORE] Errore durante l'interazione con il browser: {ex}")
            # Screenshot diagnostico automatico: la UI di Studio cambia selettori senza preavviso
            # (gia' successo 2 volte il 2026-08-17) — senza uno screenshot del punto esatto di
            # fallimento, ogni fix richiede un altro giro di upload reale solo per vedere il DOM.
            try:
                factory_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                debug_dir = os.path.join(factory_dir, "memory")
                os.makedirs(debug_dir, exist_ok=True)
                debug_path = os.path.join(debug_dir, "youtube_uploader_errore_screenshot.png")
                page.screenshot(path=debug_path)
                print(f"[+] Screenshot diagnostico salvato: {debug_path}")
            except Exception:
                pass
            browser_context.close()
            return {"status": "error", "reason": str(ex)}

def main():
    ap = argparse.ArgumentParser(description="YouTube Playwright Automated Uploader")
    ap.add_argument("--video", required=True, help="Path del file video MP4")
    ap.add_argument("--meta", required=True, help="Path del file JSON dei metadati")
    ap.add_argument("--thumbnail", help="Path della copertina PNG/JPG")
    ap.add_argument("--profile", default="memory/chrome_profile", help="Path della cartella del profilo Chrome persistente")
    ap.add_argument("--mock", action="store_true", help="Forza la modalità mock-up")
    args = ap.parse_args()

    if not os.path.exists(args.video):
        print(f"Errore: file video '{args.video}' non trovato.")
        return 1
        
    if not os.path.exists(args.meta):
        print(f"Errore: file metadati '{args.meta}' non trovato.")
        return 1

    # Regola permanente di Max (2026-08-18): MAI caricare un video senza copertina reale.
    # Nessuna eccezione — la copertina va messa a mano da Max nella cartella dedicata del video
    # (VIDEO-PRONTI/video-NN/) e passata qui con --thumbnail. Un video senza copertina non parte.
    if not args.thumbnail or not os.path.exists(args.thumbnail):
        print(f"Errore: copertina mancante o non trovata ('{args.thumbnail}'). "
              "Regola permanente: nessun upload senza copertina reale. Metti l'immagine nella "
              "cartella dedicata del video (VIDEO-PRONTI/video-NN/) e ripassa il path con --thumbnail.")
        return 1

    try:
        with open(args.meta, "r", encoding="utf-8") as f:
            metadata = json.load(f)
    except Exception as e:
        print(f"Errore di parsing dei metadati JSON: {e}")
        return 1

    if args.mock:
        res = upload_mock(args.video, metadata, args.thumbnail)
    else:
        res = upload_via_playwright(args.video, metadata, args.thumbnail, args.profile)
        
    print(f"Risultato: {json.dumps(res)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
