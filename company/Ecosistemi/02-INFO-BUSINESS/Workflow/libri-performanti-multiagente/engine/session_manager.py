"""
Session Manager (PIANO-KDP-67, CP1) — salva/carica sessioni Playwright reali per
Amazon e LM Arena.

Perché il login non può essere 100% automatico la prima volta: Amazon e LM Arena hanno
captcha/2FA — scriptare un login alla cieca è inaffidabile e rischioso (rischio ban).
Prima esecuzione: apre un browser VISIBILE sulla homepage del sito, Gael fa login a mano
(può navigare liberamente nella finestra), poi conferma nel terminale — a quel punto lo
storage_state (cookie + localStorage) viene salvato su disco. Esecuzioni successive:
sessione caricata da disco, browser headless, nessun login richiesto.

Uso diretto (test):
    python -m engine.session_manager          # crea le sessioni mancanti (interattivo)
    python -m engine.session_manager --check   # verifica solo se le sessioni esistono (non apre nulla)
"""
from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import BrowserContext, Playwright, sync_playwright

from . import config


def _ensure_session(playwright: Playwright, site_name: str, home_url: str, session_path: Path) -> bool:
    """Garantisce che esista una sessione salvata per `site_name`.
    Ritorna True se la sessione era già presente, False se è stata appena creata."""
    if session_path.exists():
        print(f"[{site_name}] sessione trovata: {session_path}")
        return True

    print(f"\n[{site_name}] NESSUNA sessione salvata trovata.")
    print(f"[{site_name}] Apro un browser visibile su {home_url} — fai login a mano "
          f"(username/password/2FA), poi torna qui.")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(home_url, wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)

    input(f"\n>>> [{site_name}] Premi INVIO qui nel terminale DOPO aver completato il login "
          f"nel browser aperto...\n")

    session_path.parent.mkdir(parents=True, exist_ok=True)
    context.storage_state(path=str(session_path))
    print(f"[{site_name}] sessione salvata in {session_path}")
    browser.close()
    return False


def ensure_amazon_session(playwright: Playwright) -> bool:
    return _ensure_session(playwright, "Amazon", config.AMAZON_BASE_URL, config.AMAZON_SESSION_PATH)


def ensure_lmarena_session(playwright: Playwright) -> bool:
    return _ensure_session(playwright, "LM Arena", config.LMARENA_BASE_URL, config.LMARENA_SESSION_PATH)


def load_context(playwright: Playwright, session_path: Path, headless: bool = True) -> BrowserContext:
    """Carica un browser context con la sessione salvata su disco.
    Solleva FileNotFoundError esplicito se la sessione non esiste — mai un browser
    silenziosamente sloggato che finge di funzionare."""
    if not session_path.exists():
        raise FileNotFoundError(
            f"Sessione non trovata: {session_path}. "
            f"Esegui prima: python -m engine.session_manager"
        )
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(storage_state=str(session_path))
    return context


def sessions_status() -> dict:
    """Stato delle sessioni SENZA aprire nessun browser — solo controllo file su disco."""
    return {
        "amazon": {"path": str(config.AMAZON_SESSION_PATH), "exists": config.AMAZON_SESSION_PATH.exists()},
        "lmarena": {"path": str(config.LMARENA_SESSION_PATH), "exists": config.LMARENA_SESSION_PATH.exists()},
    }


if __name__ == "__main__":
    if "--check" in sys.argv:
        status = sessions_status()
        for site, info in status.items():
            stato = "OK" if info["exists"] else "MANCANTE"
            print(f"{site}: {stato} ({info['path']})")
        sys.exit(0)

    with sync_playwright() as p:
        amazon_existed = ensure_amazon_session(p)
        lmarena_existed = ensure_lmarena_session(p)

    print("\n=== CP1: stato sessioni ===")
    print(f"Amazon: {'già presente' if amazon_existed else 'creata ora'}")
    print(f"LM Arena: {'già presente' if lmarena_existed else 'creata ora'}")
