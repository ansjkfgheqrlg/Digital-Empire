#!/usr/bin/env python3
"""
Bootstrap del login reale a Fliki (app.fliki.ai) — UNA TANTUM.

Pivot da API a Playwright (Max, 2026-08-20): l'API Fliki ha lasciato 3+ generazioni reali
bloccate in 'queued' per ore, senza mai passare a 'processing' e senza errore esplicito, sia
in parallelo che una alla volta con lock attivo — dashboard Fliki confermata a posto (nessun
problema di credito/piano). Causa non diagnosticabile oltre questo punto lato API. Si passa
all'automazione della UI web, che passa dagli stessi percorsi reali che usa un umano.

Apre un Chrome VISIBILE su un profilo persistente dedicato (chrome-profile-fliki, separato
dai profili YouTube: account/servizio diverso). L'operatore umano digita email+password nella
finestra vera; questo script non tocca mai le credenziali — stesso principio di
legamidiamore_login.py, nessuna eccezione anche qui.

Dopo il primo login il profilo resta salvato: le run successive (generazione video reale via
Playwright) possono riusare la stessa sessione senza richiedere login ogni volta.

Uso:
    python fliki_login.py
"""
import os
import sys

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-fliki")

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
        page.goto("https://app.fliki.ai/login", wait_until="domcontentloaded", timeout=60000)

        print("\n" + "=" * 70)
        print("FINESTRA CHROME APERTA — completa il login a Fliki a mano:")
        print("  1. Inserisci le tue credenziali Fliki (email/password o Google, come preferisci).")
        print("  2. Se chiede verifica aggiuntiva, completala normalmente.")
        print("  3. Aspetto fino a 15 minuti che l'URL esca dalla pagina di login.")
        print("=" * 70 + "\n")

        try:
            # Non conosco ancora i selettori reali della dashboard Fliki (mai esplorata via
            # browser prima d'ora): l'unico segnale affidabile senza scoperta live e' l'URL che
            # lascia /login. Una volta dentro, il prossimo script fara' la scoperta live dei
            # selettori veri (stesso approccio gia' funzionante su youtube_uploader_playwright.py).
            page.wait_for_url(lambda url: "/login" not in url, timeout=900000)
            print("[+] Login completato — sessione salvata nel profilo persistente.")
            print(f"[+] URL corrente: {page.url}")
            screenshot_path = os.path.join(FACTORY_DIR, "memory", "fliki_login.png")
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
