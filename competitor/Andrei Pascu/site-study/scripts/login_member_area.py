# -*- coding: utf-8 -*-
"""
login_member_area.py — login nell'area membri di andrei-copy.com (Member Areas Squarespace).

Legge ANDREI_COPY_EMAIL / ANDREI_COPY_PASSWORD da .env (root del repo), fa login via Playwright,
salva lo storage_state in auth/andrei_copy_state.json (fuori da git) per riuso da site_capture2.py
e da qualsiasi script che debba leggere pagine gated.

Uso:
    python login_member_area.py
    python login_member_area.py --show   (headed, per debug visivo)
"""
import argparse
import os
import re
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)  # site-study/
REPO_ROOT = os.path.normpath(os.path.join(BASE, "..", "..", ".."))
AUTH_DIR = os.path.join(BASE, "auth")  # solo debug (screenshot), mai cookie/credenziali
DASHBOARD_URL = "https://www.andrei-copy.com/armageddon-dashboard"

# La sessione (cookie validi) NON vive nel repo, nemmeno gitignorata: fuori dal disco del
# progetto, in scratchpad locale. Precedente vincolante: runs/andrei-pascu-cs2online-001/
# MASTER-RUN-TRACKER.md "SICUREZZA CREDENZIALI" — password mai su file salvato, sessione
# solo in scratchpad/temp, mai nel repo.
STATE_DIR = os.environ.get(
    "ANDREI_COPY_STATE_DIR",
    os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "claude",
                 "c--Users-Utente-Desktop-qui-tutto-Digital-Empire",
                 "089c840c-dbd9-4a6c-be69-756af5ceb502", "scratchpad", "andrei-copy-auth"),
)
STATE_PATH = os.path.join(STATE_DIR, "andrei_copy_state.json")


def login(headless=True):
    # Credenziali SOLO da variabile d'ambiente della sessione corrente, mai da file salvato
    # su disco (ne' .env, ne' altrove) — vedi STATE_DIR sopra per la fonte della regola.
    email = os.environ.get("ANDREI_COPY_EMAIL")
    password = os.environ.get("ANDREI_COPY_PASSWORD")
    if not email or not password:
        print("[ERRORE] imposta ANDREI_COPY_EMAIL / ANDREI_COPY_PASSWORD come variabili "
              "d'ambiente prima di lanciare lo script (mai in un file salvato)", file=sys.stderr)
        return 1

    os.makedirs(AUTH_DIR, exist_ok=True)
    os.makedirs(STATE_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        pg = ctx.new_page()
        pg.goto(DASHBOARD_URL, wait_until="networkidle", timeout=45000)
        pg.wait_for_timeout(1500)

        # chiudi eventuale banner/cookie
        for etichetta in ["Accetta", "Accept", "Ho capito", "Capito"]:
            try:
                btn = pg.get_by_text(etichetta, exact=True).first
                if btn.is_visible(timeout=800):
                    btn.click(timeout=1500)
                    pg.wait_for_timeout(400)
            except Exception:
                pass

        # apre il form di login: bottone "Accedi"
        try:
            pg.get_by_text("Accedi", exact=True).first.click(timeout=5000)
        except Exception as e:
            print(f"[ERRORE] bottone Accedi non trovato: {e}", file=sys.stderr)
            pg.screenshot(path=os.path.join(AUTH_DIR, "_debug_no_accedi.png"))
            browser.close()
            return 1
        pg.wait_for_timeout(1200)

        # compila email + password nel form che appare (modal, possibilmente in iframe)
        frames = [pg] + list(pg.frames)

        def trova_campo(selettori):
            for fr in frames:
                for sel in selettori:
                    try:
                        loc = fr.locator(sel).first
                        if loc.is_visible(timeout=1500):
                            return loc
                    except Exception:
                        continue
            return None

        campo_email = trova_campo([
            "input[placeholder='E-mail']", "input[type='email']", "input[name='email']",
            "input[autocomplete='email']", "input[id*='email' i]",
        ])
        if campo_email is None:
            print("[ERRORE] campo email non trovato in nessun frame", file=sys.stderr)
            pg.screenshot(path=os.path.join(AUTH_DIR, "_debug_no_email_field.png"))
            browser.close()
            return 1
        campo_email.click()
        campo_email.fill(email)

        campo_pw = trova_campo([
            "input[placeholder='Password']", "input[type='password']",
            "input[autocomplete='current-password']",
        ])
        if campo_pw is None:
            print("[ERRORE] campo password non trovato in nessun frame", file=sys.stderr)
            pg.screenshot(path=os.path.join(AUTH_DIR, "_debug_no_pw_field.png"))
            browser.close()
            return 1
        campo_pw.click()
        campo_pw.fill(password)

        pg.screenshot(path=os.path.join(AUTH_DIR, "_debug_prima_di_submit.png"))

        # submit
        submesso = False
        for sel in ["button[type='submit']", "text=Accedi", "text=Login", "text=Log in"]:
            try:
                el = pg.locator(sel).first
                if el.is_visible(timeout=1000):
                    el.click(timeout=3000)
                    submesso = True
                    break
            except Exception:
                continue
        if not submesso:
            pg.keyboard.press("Enter")

        pg.wait_for_timeout(3000)
        pg.screenshot(path=os.path.join(AUTH_DIR, "_debug_dopo_submit.png"))

        html = pg.content()
        loggato = ("Esci" in html or "Logout" in html or "Il mio account" in html
                   or "solo per i membri" not in html)

        ctx.storage_state(path=STATE_PATH)
        browser.close()

        if loggato:
            print(f"[OK] login riuscito, storage_state salvato in {STATE_PATH}")
            return 0
        else:
            print("[ATTENZIONE] login incerto — controlla gli screenshot in auth/_debug_*.png")
            print(f"storage_state comunque salvato in {STATE_PATH}")
            return 2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true", help="browser headed, per debug visivo")
    a = ap.parse_args()
    sys.exit(login(headless=not a.show))
