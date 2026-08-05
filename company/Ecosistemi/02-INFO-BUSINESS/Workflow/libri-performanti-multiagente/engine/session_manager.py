"""
Session Manager (PIANO-KDP-67, CP1) — salva/carica sessioni Playwright reali per
Amazon e LM Arena.

APPROCCIO (rivisto il 2026-08-05 dopo 2 tentativi reali falliti): un login OAuth "Accedi
con Google" fatto DENTRO un browser pilotato da Playwright viene bloccato da Google
("Questo browser o questa app potrebbero non essere sicuri") — verificato sia con il
Chromium bundlato sia con Chrome reale (channel="chrome"). Non è un bug risolvibile con
selettori migliori: è una protezione anti-automazione di Google.

Fix adottato: invece di un login NUOVO dentro l'automazione, si riusa un profilo Chrome
GIÀ autenticato (quello di tutti i giorni dell'utente). Il profilo scelto da Gael è
"Profile 8" (max.infoproducer@gmail.com). Il profilo originale NON viene MAI scritto: se
ne fa una copia (esclusa cache/estensioni, solo i dati di sessione) in
sessions/chrome_profile_copy/, e Playwright lancia un `launch_persistent_context` su
QUELLA copia. Se il profilo copiato è già loggato su Amazon/LM Arena, non serve nessun
login — se non lo è, Gael può comunque loggarsi lì (non più bloccato da Google, perché è
un profilo con storico reale, non un browser vuoto appena creato dall'automazione).

Uso diretto (test):
    python -m engine.session_manager          # crea le sessioni mancanti (interattivo)
    python -m engine.session_manager --check   # verifica solo se le sessioni esistono (non apre nulla)
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

from playwright.sync_api import BrowserContext, Playwright, sync_playwright

from . import config


def _copy_chrome_profile_if_needed() -> Path:
    """Copia (una volta sola) il profilo Chrome sorgente scelto da Gael in
    sessions/chrome_profile_copy/, escludendo cache/estensioni. Il profilo originale
    viene SOLO letto, mai scritto. Ritorna il path della copia (root "User Data")."""
    dest_root = config.CHROME_PROFILE_COPY_DIR
    dest_profile = dest_root / "Default"
    if dest_profile.exists():
        print(f"[chrome-profile] copia già presente: {dest_root}")
        return dest_root

    source_profile = config.CHROME_USER_DATA_ROOT / config.CHROME_SOURCE_PROFILE_NAME
    source_local_state = config.CHROME_USER_DATA_ROOT / "Local State"
    if not source_profile.exists():
        raise FileNotFoundError(
            f"Profilo Chrome sorgente non trovato: {source_profile}. "
            f"Controlla config.CHROME_SOURCE_PROFILE_NAME."
        )

    print(f"[chrome-profile] copio {source_profile} -> {dest_profile} (esclusa cache)...")

    def _ignore(dir_path: str, names: list[str]) -> set[str]:
        return {n for n in names if n in config.CHROME_COPY_EXCLUDE_DIRS}

    dest_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_profile, dest_profile, ignore=_ignore, dirs_exist_ok=True)
    if source_local_state.exists():
        shutil.copy2(source_local_state, dest_root / "Local State")

    size_mb = sum(f.stat().st_size for f in dest_root.rglob("*") if f.is_file()) / (1024 * 1024)
    print(f"[chrome-profile] copia completata: {size_mb:.1f} MB (originale mai scritto)")
    return dest_root


def _ensure_session(playwright: Playwright, site_name: str, home_url: str, session_path: Path,
                     profile_dir: Path) -> bool:
    """Garantisce che esista una sessione salvata per `site_name`, usando il profilo
    Chrome copiato (già autenticato, non bloccato da Google come un browser vuoto).
    Ritorna True se la sessione era già presente, False se è stata appena creata."""
    if session_path.exists():
        print(f"[{site_name}] sessione trovata: {session_path}")
        return True

    print(f"\n[{site_name}] NESSUNA sessione salvata trovata.")
    print(f"[{site_name}] Apro Chrome con il profilo copiato (già autenticato) su {home_url}...")
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir),
        headless=False,
        channel="chrome",
        args=["--start-maximized", "--profile-directory=Default"],
        no_viewport=True,
    )
    page = context.pages[0] if context.pages else context.new_page()
    page.bring_to_front()
    page.goto(home_url, wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)
    page.bring_to_front()
    print(f"[{site_name}] Se il profilo era già loggato, dovresti vedere l'account collegato "
          f"direttamente. Se NON lo è, fai login ora — qui non dovrebbe essere bloccato "
          f"(profilo con storico reale, non un browser vuoto).")

    input(f"\n>>> [{site_name}] Premi INVIO qui nel terminale DOPO aver verificato/completato "
          f"il login nel browser aperto...\n")

    session_path.parent.mkdir(parents=True, exist_ok=True)
    context.storage_state(path=str(session_path))
    print(f"[{site_name}] sessione salvata in {session_path}")
    context.close()
    return False


def ensure_amazon_session(playwright: Playwright, profile_dir: Path) -> bool:
    return _ensure_session(playwright, "Amazon", config.AMAZON_BASE_URL, config.AMAZON_SESSION_PATH, profile_dir)


def ensure_lmarena_session(playwright: Playwright, profile_dir: Path) -> bool:
    return _ensure_session(playwright, "LM Arena", config.LMARENA_BASE_URL, config.LMARENA_SESSION_PATH, profile_dir)


def load_context(playwright: Playwright, session_path: Path, headless: bool = True) -> BrowserContext:
    """Carica un browser context con la sessione salvata su disco (uso normale, dopo CP1).
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

    profile_dir = _copy_chrome_profile_if_needed()

    with sync_playwright() as p:
        amazon_existed = ensure_amazon_session(p, profile_dir)
        lmarena_existed = ensure_lmarena_session(p, profile_dir)

    print("\n=== CP1: stato sessioni ===")
    print(f"Amazon: {'già presente' if amazon_existed else 'creata ora'}")
    print(f"LM Arena: {'già presente' if lmarena_existed else 'creata ora'}")
