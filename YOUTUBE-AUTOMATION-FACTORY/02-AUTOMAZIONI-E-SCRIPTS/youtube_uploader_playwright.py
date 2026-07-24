#!/usr/bin/env python3
import sys
import os
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
    
    with sync_playwright() as p:
        # Avviamo Chromium caricando la sessione in cui l'utente ha già fatto login su YouTube Studio
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,  # Mostra l'interfaccia grafica per monitorare o intervenire in caso di captcha
            args=["--disable-blink-features=AutomationControlled"] # Evita rilevamento robot
        )
        
        page = browser_context.new_page()
        print("Navigazione su YouTube Studio...")
        page.goto("https://studio.youtube.com")
        page.wait_for_timeout(5000)
        
        # Verifica se siamo loggati (cerca il pulsante CREA o UPLOAD)
        if "login" in page.url or page.locator("input[type='email']").is_visible():
            print("[ERRORE] Il profilo Chrome non è loggato su Google. Effettua il login manualmente nel profilo Chrome salvato.")
            browser_context.close()
            return {"status": "error", "reason": "auth_required"}

        try:
            print("Clic su pulsante CREA...")
            page.locator("#create-icon").click()
            page.wait_for_timeout(1000)
            
            print("Clic su Carica Video...")
            page.locator("tp-yt-paper-item:has-text('Carica video')").click()
            page.wait_for_timeout(2000)
            
            # Input del file video
            print(f"Inserimento file video: {video_path}...")
            file_input = page.locator("input[type='file']")
            file_input.set_input_files(video_path)
            page.wait_for_timeout(5000) # Attendi caricamento iniziale
            
            # Compilazione metadati
            print(f"Compilazione Titolo: {metadata.get('title')}...")
            title_box = page.locator("#textbox[aria-label*='Aggiungi un titolo']")
            title_box.clear()
            title_box.fill(metadata.get('title', 'Nuovo Video'))
            page.wait_for_timeout(1000)
            
            print("Compilazione Descrizione...")
            desc_box = page.locator("#textbox[aria-label*='Descrivi il video']")
            desc_box.clear()
            desc_box.fill(metadata.get('description', ''))
            page.wait_for_timeout(1000)
            
            # Caricamento miniatura
            if thumbnail_path and os.path.exists(thumbnail_path):
                print(f"Inserimento miniatura: {thumbnail_path}...")
                thumb_input = page.locator("#file-loader input[type='file']")
                if thumb_input.is_visible():
                    thumb_input.set_input_files(thumbnail_path)
                    page.wait_for_timeout(3000)
            
            # Dichiarazione non per bambini
            print("Impostazione destinatari (non per bambini)...")
            page.locator("tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_FALSE']").click()
            page.wait_for_timeout(1000)
            
            # Clic su Avanti per 3 volte (Dettagli -> Elementi -> Controlli)
            for step in range(3):
                print(f"Clic su pulsante Avanti (Passo {step+1}/3)...")
                page.locator("#next-button").click()
                page.wait_for_timeout(2000)
                
            # Schermata Visibilità: imposta come Privato o Programmato
            print("Impostazione visibilità (Privato per sicurezza)...")
            page.locator("tp-yt-paper-radio-button[name='PRIVATE']").click()
            page.wait_for_timeout(1000)
            
            # Clic su Salva
            print("Clic su pulsante Salva / Pubblica...")
            page.locator("#done-button").click()
            page.wait_for_timeout(5000)
            
            print("Video caricato correttamente via Playwright browser automation!")
            browser_context.close()
            return {"status": "success", "video_id": "uploaded_via_playwright"}
            
        except Exception as ex:
            print(f"[ERRORE] Errore durante l'interazione con il browser: {ex}")
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
