#!/usr/bin/env python3
"""
Bootstrap del login reale per @Legamidiamore — UNA TANTUM.

Apre un Chrome VISIBILE su un profilo persistente dedicato (separato da
chrome-profile-youtube, usato solo per scraping anonimo: due account Google diversi non
devono condividere sessione). L'operatore umano digita email+password nella finestra vera;
questo script non tocca mai le credenziali — le conosce solo chi le digita a schermo.

Dopo il primo login il profilo resta salvato: le run successive (upload reale, audit Studio)
possono girare headless riusando la stessa sessione, stesso pattern gia' in uso per
arena_thumbnail.py e youtube_uploader_playwright.py.

Uso:
    python legamidiamore_login.py
"""
import os
import sys
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")

# Senza User-Agent esplicito, YouTube Studio mostra un interstiziale "browser non supportato"
# al posto della dashboard (bug reale trovato il 2026-08-05, vedi legamidiamore_session_check.py)
# — stesso fix qui per coerenza, cosi' non ricompare al primo controllo dopo il login.
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def main():
    os.makedirs(PROFILE_DIR, exist_ok=True)
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
            user_agent=USER_AGENT,
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)

        print("\n" + "=" * 70)
        print("FINESTRA CHROME APERTA — completa il login a mano:")
        print("  1. Email:    legamidamore55@gmail.com")
        print("  2. Password: quella che hai gia' (non scritta qui)")
        print("  3. Se Google chiede verifica in due passaggi, completala normalmente.")
        print("  4. Aspetto fino a 15 minuti che la dashboard di Studio si apra da sola.")
        print("=" * 70 + "\n")

        try:
            # La dashboard reale di Studio ha sempre questo elemento; comparire qui prova
            # login riuscito, non solo redirect intermedio.
            page.wait_for_selector("ytcp-header, #entity-name", timeout=900000)
            print("[+] Login completato — sessione salvata nel profilo persistente.")
            titolo = page.title()
            print(f"[+] Pagina corrente: {titolo}")
            screenshot_path = os.path.join(FACTORY_DIR, "memory", "legamidiamore_studio_login.png")
            page.screenshot(path=screenshot_path)
            print(f"[+] Screenshot di conferma salvato: {screenshot_path}")
        except Exception as e:
            print(f"[!] Timeout o errore in attesa del login: {e}")
            print("    Il profilo resta comunque salvato con qualunque progresso fatto: "
                 "rilancia lo script per continuare da dove interrotto.")
        finally:
            context.close()


if __name__ == "__main__":
    main()
