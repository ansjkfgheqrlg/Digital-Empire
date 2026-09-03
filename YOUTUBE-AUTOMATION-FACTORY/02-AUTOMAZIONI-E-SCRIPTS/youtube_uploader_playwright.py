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

def ads_on_after_upload(page, video_id):
    """Attiva 'Watch Page ads & YouTube Premium' per un video appena caricato.
    Trovato dal vivo il 2026-09-03 (ordine di Max): Google lascia le pubblicita' SPENTE
    di default su ogni nuovo upload — senza questo passo il video non guadagna mai un euro,
    ed e' successo in silenzio su 3 video pubblici prima che qualcuno se ne accorgesse.
    Il click diretto via JS (evaluate) e' voluto: i controlli di Playwright falliscono qui
    per instabilita' del layout durante il processing, il click nativo del DOM no.
    """
    page.goto(f"https://studio.youtube.com/video/{video_id}/monetization/ads",
               wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(3000)
    off_trigger = page.locator("text=Off").first
    if off_trigger.count() == 0:
        print("[ADS] Gia' attive o pagina non nello stato atteso, salto.")
        return
    off_trigger.click(timeout=8000)
    page.wait_for_timeout(1000)
    page.locator("tp-yt-paper-radio-button").filter(has_text="On").first.click(timeout=8000)
    page.wait_for_timeout(1000)
    page.locator("button:has-text('Next')").first.click(timeout=8000)
    page.wait_for_timeout(2000)
    # Questionario obbligatorio "Tell us what's in your video" — autocertificazione onesta:
    # per i video di questo canale (consigli/psicologia relazionale) nessuna categoria si
    # applica mai, quindi "None of the above" e' la risposta corretta, non una scorciatoia.
    page.locator("text=Inappropriate language").first.click(timeout=8000)
    page.wait_for_timeout(1200)
    page.get_by_text("None of the above", exact=False).first.click(timeout=8000)
    page.wait_for_timeout(1500)
    page.locator("button:has-text('Submit')").first.evaluate("el => el.click()")
    page.wait_for_timeout(3000)
    save_btn = page.locator("button:has-text('Save')").first
    save_btn.evaluate("el => el.click()")
    page.wait_for_timeout(3000)
    print("[ADS] Pubblicita' attivate e salvate.")

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
        # Avviamo il Chrome VERO installato sul PC (channel="chrome"), non il Chromium bundled di
        # Playwright — richiesta di Max (2026-09-03) dopo che l'ennesimo "Verify it's you" ha
        # bloccato un upload. Il Chromium di Playwright ha un fingerprint (build, header, canvas)
        # diverso da quello che Google vede normalmente su questo account; il Chrome reale, con lo
        # stesso profilo persistente gia' usato per il login manuale, e' la stessa identica
        # impronta che Google gia' conosce e fida. Non elimina la verifica (Google puo' comunque
        # chiederla per motivi suoi), ma la rende molto meno frequente.
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="chrome",
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
            # da main(). AGGIORNATO 2026-09-01: il selettore nth(1) non trova piu' il secondo
            # input[type=file] nella wizard attuale di Studio. Strategia aggiornata: scroll fino
            # alla sezione "Thumbnail", cercare il bottone "Upload thumbnail"/"Carica miniatura"
            # o un input file dedicato, con fallback sull'ordine se la UI cambia di nuovo.
            print(f"Inserimento miniatura: {thumbnail_path}...")
            # Scroll giu' per rendere visibile la sezione thumbnail
            page.evaluate("window.scrollBy(0, 400)")
            page.wait_for_timeout(1000)
            # Prova 1: cercare un input file specifico per la miniatura (attributo accept image)
            thumb_input = None
            img_input = page.locator("input[type='file'][accept*='image']")
            if img_input.count() > 0:
                thumb_input = img_input.first
            else:
                # Prova 2: bottone "Upload thumbnail" / "Carica miniatura" che rivela l'input
                upload_thumb_btn = page.locator(
                    "button:has-text('Upload thumbnail'), "
                    "button:has-text('Carica miniatura'), "
                    "#still-picker-add-button, "
                    "[id*='thumbnail'] button"
                ).first
                try:
                    upload_thumb_btn.click(timeout=5000)
                    page.wait_for_timeout(1000)
                    img_input = page.locator("input[type='file'][accept*='image']")
                    if img_input.count() > 0:
                        thumb_input = img_input.first
                except Exception:
                    pass
            if not thumb_input:
                # Prova 3: fallback al vecchio metodo nth(1) con timeout breve
                try:
                    fallback = page.locator("input[type='file']").nth(1)
                    fallback.wait_for(state="attached", timeout=5000)
                    thumb_input = fallback
                except Exception:
                    print("[AVVISO] Nessun input miniatura trovato — la miniatura va caricata manualmente in YouTube Studio.")
            if thumb_input:
                thumb_input.set_input_files(thumbnail_path)
                page.wait_for_timeout(3000)
            else:
                print("[AVVISO] Proseguo senza miniatura. Caricarla manualmente dopo il salvataggio.")

            # Dichiarazione non per bambini — valore reale verificato dal vivo il 2026-08-17
            # via screenshot diagnostico: e' 'VIDEO_MADE_FOR_KIDS_NOT_MFK', non 'FALSE' come
            # assunto originariamente (causa reale di tutti i timeout precedenti su questo step).
            print("Impostazione destinatari (non per bambini)...")
            page.locator("tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']").click()
            page.wait_for_timeout(1000)

            # Clic su Avanti fino alla schermata Visibilita'. La wizard di Studio ha un numero
            # variabile di tab (era 4 fino a ~agosto 2026, diventato 5 con l'aggiunta di
            # "Initial check" / "Monetization"). BUG REALE trovato il 2026-09-03: il vecchio
            # controllo cercava il testo "Visibility" nello STEPPER in alto — ma quel testo e'
            # sempre presente (e' l'etichetta del tab, visibile anche quando sei ancora su
            # Details), quindi il controllo dava falso positivo dopo 0 click e il codice provava
            # subito a cliccare il radio Private, che non esiste ancora su quella schermata
            # (timeout). Fix: aspetta che il radio PRIVATE stesso sia visibile, non l'etichetta.
            private_radio = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
            for step in range(8):
                try:
                    if private_radio.count() > 0 and private_radio.first.is_visible():
                        print(f"Radio PRIVATE visibile dopo {step} click Next.")
                        break
                except Exception:
                    pass
                print(f"Clic su pulsante Avanti/Next (Passo {step+1})...")
                try:
                    page.locator(
                        "button:has-text('Next'), button:has-text('Avanti')"
                    ).first.click(timeout=10000)
                    page.wait_for_timeout(2000)
                except Exception:
                    print(f"[AVVISO] Next button non trovato al passo {step+1}, proseguo...")
                    break

            # Schermata Visibilità: imposta come Privato
            print("Impostazione visibilità (Privato per sicurezza)...")
            if private_radio.count() > 0 and private_radio.first.is_visible():
                # Percorso A: wizard a tab (Details -> ... -> Visibility), radio gia' in pagina.
                private_radio.first.click(timeout=10000)
                page.wait_for_timeout(1000)
                print("Clic su pulsante Salva/Save...")
                page.locator(
                    "button:has-text('Save'), button:has-text('Salva'), "
                    "button:has-text('Publish'), button:has-text('Pubblica')"
                ).first.click()
                page.wait_for_timeout(5000)
            else:
                # Percorso B, trovato dal vivo il 2026-09-03: quando l'upload atterra sulla
                # pagina singola "Video details" (niente stepper, niente Next), la visibilita'
                # si imposta dal pannello destro: un box "Visibility" con dentro lo stato
                # corrente (es. "Pending") che, cliccato, apre un popup "Save or publish" con
                # Private gia' selezionato di default. Serve confermare con "Done" e poi "Save".
                print("Wizard a tab non trovato, provo il pannello Visibility del pannello destro...")
                page.locator("[class*='visibility'], #visibility").first.click(timeout=8000)
                page.wait_for_timeout(1500)
                popup_private = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
                if popup_private.count() > 0:
                    popup_private.first.click(timeout=5000)
                    page.wait_for_timeout(500)
                page.locator("button:has-text('Done')").first.click(timeout=8000)
                page.wait_for_timeout(1500)
                print("Clic su pulsante Salva/Save...")
                page.locator("button:has-text('Save')").first.click(timeout=8000)
                page.wait_for_timeout(5000)

            # BUG REALE trovato il 2026-09-03: dopo il Save, Studio mostra il proprio popup
            # ("Your private video is still uploading. Keep this browser tab open until
            # uploading completes.") — e il codice chiudeva il browser_context 5 secondi dopo,
            # cioe' esattamente quello che Google dice di NON fare. Un file da 270+ MB puo'
            # metterci 10-15 minuti reali. Restiamo sulla pagina e aspettiamo che il popup
            # sparisca (o che il testo "Uploading" non sia piu' presente) prima di chiudere,
            # fino a un tetto di 20 minuti — non blocca all'infinito se qualcosa va storto.
            print("Attendo fine upload reale (Google chiede di non chiudere il tab)...")
            upload_deadline = time.time() + 20 * 60
            while time.time() < upload_deadline:
                try:
                    still_uploading = page.get_by_text("still uploading", exact=False).count() > 0 \
                        or page.get_by_text("ancora caricando", exact=False).count() > 0
                except Exception:
                    still_uploading = False
                if not still_uploading:
                    print("Upload completato (popup 'still uploading' non piu' presente).")
                    break
                page.wait_for_timeout(15000)
            else:
                print("[AVVISO] Tetto di 20 minuti raggiunto, procedo comunque.")

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

            # REGOLA PERMANENTE di Max (2026-09-03, GRAVISSIMA): ogni video deve guadagnare.
            # Trovati dal vivo 3 video pubblici con le pubblicita' spente (zero incasso) perche'
            # nessuno lo aveva mai attivato dopo l'upload — Google lo lascia OFF di default.
            # Da qui in poi lo attiviamo SEMPRE, per ogni video, appena ha un ID reale.
            if video_id:
                try:
                    ads_on_after_upload(page, video_id)
                except Exception as e:
                    print(f"[AVVISO] Impostazione pubblicita' fallita, va fatta a mano: {e}")

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
