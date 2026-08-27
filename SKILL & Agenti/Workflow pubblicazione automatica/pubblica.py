#!/usr/bin/env python3
"""
pubblica.py - UN comando per pubblicare una cartella di contenuti gia' pronti
sul canale giusto. (TASK-PUBLISHER-W1)

    python pubblica.py "<cartella>"                 # dry-run VERIFICATO (default)
    python pubblica.py "<cartella>" --live          # pubblica DAVVERO

La cartella e' un output gia' pronto (es. un prodotto dell'Arsenale Caroselli):
slide_01.png ... slide_NN.png + caption.txt. Non genera contenuto, non tocca
i motori: li WRAPPA (ADR-003).

Motore reale usato per il --live: scripts/ig_carousel_publish.py::publish(),
l'unico publisher del folder che (a) fa il login, (b) gestisce il carosello
multi-slide, (c) restituisce un esito onesto True/False.
NON usa Instagram/instagram_publisher.py::publish(): quello ingoia le
eccezioni e "riesce" sempre (vedi DIAGNOSI-PUBLISHER.md).

Regola di casa: nessun PASS finto. L'exit code e' 0 solo se il verdetto e'
davvero PASS. Il dry-run non e' una stampa: apre il browser reale e verifica
lo stato di sessione/login prima di dichiarare qualsiasi cosa.
"""
import argparse
import json
import os
import re
import struct
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORKFLOW_DIR = Path(__file__).parent.resolve()
PUBLISHED_LOG = WORKFLOW_DIR / "published.json"
DIAGNOSTICA = WORKFLOW_DIR / "_diagnostica"

ESTENSIONI_IMG = {".png", ".jpg", ".jpeg"}
ESTENSIONI_SOSPETTE = {".webp", ".gif", ".bmp"}

# Limiti reali di Instagram (non inventati: sono quelli che fanno fallire l'upload)
MAX_SLIDE = 10
MAX_CAPTION = 2200
MAX_HASHTAG = 30
MAX_MB = 8.0
RATIO_MIN = 0.80   # 4:5 verticale
RATIO_MAX = 1.91   # 1.91:1 orizzontale

# ---------------------------------------------------------------- canali
# Stato REALE verificato il 2026-08-27, non aspirazionale.
CANALI = {
    "instagram": {
        "account": "@digitalempireagency.e",
        "cartella_sessione": "Instagram",
        "url": "https://www.instagram.com/",
        "pronto": True,
        "nota": "publisher reale con login + carosello + esito onesto",
    },
    "linkedin": {
        "account": "Digital Empire",
        "cartella_sessione": "LinkedIn",
        "url": "https://www.linkedin.com/feed/",
        "pronto": False,
        "nota": "LinkedIn/linkedin_publisher.py importa, ma nessuna session_data "
                "e mai eseguito end-to-end: non lo dichiaro pronto senza una prova",
    },
    "instagram_mentalita": {
        "account": "@mentalita.brutale",
        "cartella_sessione": "Instagram_Mentalita",
        "url": "https://www.instagram.com/",
        "pronto": False,
        "nota": "publisher Reel presente ma nessuna session_data e mai testato qui",
    },
    "tiktok": {
        "account": "Codice dei Potenti",
        "cartella_sessione": "TikTok",
        "url": "https://www.tiktok.com/",
        "pronto": False,
        "nota": "TikTok/tiktok_publisher.py NON importa: 'import config' invece di "
                "'from TikTok import config' (ModuleNotFoundError)",
    },
}


def rileva_canale(cartella):
    """Routing cartella -> canale, secondo le catene descritte in REGOLE.md."""
    p = str(cartella).lower()
    if "mentalita" in p or "brutale" in p:
        return "instagram_mentalita"
    if "potenti" in p:
        return "tiktok"
    return "instagram"


# ---------------------------------------------------------------- helper
def ordina_naturale(files):
    def chiave(f):
        n = re.findall(r"\d+", f.stem)
        return (int(n[-1]) if n else 0, f.name)
    return sorted(files, key=chiave)


def trova_slide(cartella):
    return ordina_naturale([f for f in cartella.iterdir()
                            if f.is_file() and f.suffix.lower() in ESTENSIONI_IMG])


def sottocartelle_con_slide(cartella):
    return [d for d in sorted(cartella.iterdir()) if d.is_dir() and trova_slide(d)]


def dimensioni(path):
    """Legge larghezza/altezza dagli header reali (PNG/JPEG). None se illeggibile."""
    try:
        with open(path, "rb") as fh:
            head = fh.read(26)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                w, h = struct.unpack(">II", head[16:24])
                return w, h
            if head[:2] == b"\xff\xd8":
                fh.seek(2)
                while True:
                    b = fh.read(1)
                    if not b:
                        return None
                    if b != b"\xff":
                        continue
                    marker = fh.read(1)
                    while marker == b"\xff":
                        marker = fh.read(1)
                    if marker in (b"\xc0", b"\xc1", b"\xc2", b"\xc3"):
                        fh.read(3)
                        h, w = struct.unpack(">HH", fh.read(4))
                        return w, h
                    ln = struct.unpack(">H", fh.read(2))[0]
                    fh.seek(ln - 2, 1)
    except (OSError, struct.error):
        return None
    return None


def carica_log():
    if PUBLISHED_LOG.exists():
        try:
            return json.loads(PUBLISHED_LOG.read_text("utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def segna_pubblicato(cartella, canale):
    d = carica_log()
    d[cartella.name] = {
        "folder": str(cartella),
        "canale": canale,
        "published_at": datetime.now().isoformat(timespec="seconds"),
    }
    PUBLISHED_LOG.write_text(json.dumps(d, indent=2, ensure_ascii=False), "utf-8")


# ---------------------------------------------------------------- preflight
def preflight(cartella, forza):
    """Controlli reali sui byte. Ritorna (errori, avvisi, slide, caption)."""
    errori, avvisi = [], []

    slide = trova_slide(cartella)
    sospetti = [f for f in cartella.iterdir()
                if f.is_file() and f.suffix.lower() in ESTENSIONI_SOSPETTE]
    if sospetti:
        avvisi.append("%d file in formato non accettato da IG (%s): ignorati"
                      % (len(sospetti), ", ".join(sorted({f.suffix for f in sospetti}))))

    if not slide:
        errori.append("nessuna slide .png/.jpg nella cartella")
    elif len(slide) > MAX_SLIDE:
        errori.append("%d slide: Instagram ne accetta max %d" % (len(slide), MAX_SLIDE))

    ratios = []
    for f in slide:
        mb = f.stat().st_size / 1048576
        if mb > MAX_MB:
            errori.append("%s: %.1fMB, oltre il limite di %.1fMB" % (f.name, mb, MAX_MB))
        dim = dimensioni(f)
        if dim is None:
            errori.append("%s: header immagine illeggibile o file corrotto" % f.name)
            continue
        w, h = dim
        r = w / h
        ratios.append(round(r, 3))
        if not (RATIO_MIN <= r <= RATIO_MAX):
            errori.append("%s: %dx%d (ratio %.2f) fuori dal range IG %.2f-%.2f"
                          % (f.name, w, h, r, RATIO_MIN, RATIO_MAX))
    if ratios and len(set(ratios)) > 1:
        avvisi.append("slide con proporzioni diverse %s: IG le forzera' tutte a "
                      "quella della prima (taglio)" % sorted(set(ratios)))

    cap_file = cartella / "caption.txt"
    caption = ""
    if not cap_file.exists():
        errori.append("caption.txt assente")
    else:
        caption = cap_file.read_text("utf-8").strip()
        if not caption:
            errori.append("caption.txt vuoto")
        if len(caption) > MAX_CAPTION:
            errori.append("caption %d caratteri, oltre il limite IG %d"
                          % (len(caption), MAX_CAPTION))
        n_tag = len(re.findall(r"#\w+", caption))
        if n_tag > MAX_HASHTAG:
            errori.append("%d hashtag, oltre il limite IG %d" % (n_tag, MAX_HASHTAG))

    log = carica_log()
    if cartella.name in log:
        msg = ("gia' pubblicato il %s su %s"
               % (log[cartella.name].get("published_at", "?"),
                  log[cartella.name].get("canale", "?")))
        if forza:
            avvisi.append(msg + " (--force: procedo lo stesso)")
        else:
            errori.append(msg + " - usa --force per ripubblicare")

    return errori, avvisi, slide, caption


# ---------------------------------------------------------------- sessione
def verifica_sessione(canale, visible):
    """Apre il browser REALE e dice la verita' sullo stato di login.
    Ritorna (autenticato: True/False/None, dettaglio: str)."""
    info = CANALI[canale]
    cartella_sessione = WORKFLOW_DIR / info["cartella_sessione"] / "session_data"

    if not cartella_sessione.exists():
        return False, ("session_data ASSENTE (%s/session_data): nessuna sessione "
                       "salvata su questa macchina" % info["cartella_sessione"])

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None, "playwright non installato: impossibile verificare"

    DIAGNOSTICA.mkdir(exist_ok=True)
    try:
        with sync_playwright() as p:
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=str(cartella_sessione),
                headless=not visible,
                viewport={"width": 1280, "height": 900},
                channel="chrome",
                args=["--disable-blink-features=AutomationControlled"],
                ignore_default_args=["--enable-automation"],
                locale="it-IT",
            )
            pg = ctx.new_page()
            pg.goto(info["url"], wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(5000)
            shot = DIAGNOSTICA / ("sessione_%s_%s.png" % (canale, datetime.now().strftime("%Y%m%d-%H%M%S")))
            pg.screenshot(path=str(shot))
            corrente = pg.url
            # Instagram loggato-fuori usa name="email"/"pass" sulla home e
            # name="username" su /accounts/login/. LinkedIn usa session_key.
            # Verificato dal vivo il 2026-08-27: la home NON ha piu' "username".
            ha_login = pg.locator(
                'input[name="username"], input[name="email"], '
                'input[name="pass"], input[name="session_key"]').count() > 0
            ha_post = pg.locator(
                'svg[aria-label="Nuovo post"], svg[aria-label="New post"]').count() > 0
            ctx.close()
    except Exception as e:
        return None, "browser non avviabile: %s: %s" % (type(e).__name__, str(e)[:150])

    prova = "url=%s | screenshot=%s" % (corrente, shot.name)
    if ha_login or "login" in corrente:
        return False, "NON autenticato: form di login presente. %s" % prova
    if ha_post:
        return True, "autenticato: bottone 'Nuovo post' presente. %s" % prova
    return None, "stato ambiguo: ne' login ne' 'Nuovo post'. %s" % prova


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(
        description="Pubblica una cartella di contenuti gia' pronti sul canale giusto.")
    ap.add_argument("cartella", help="Cartella con slide_*.png + caption.txt")
    ap.add_argument("--canale", choices=sorted(CANALI), default=None,
                    help="Forza il canale (default: dedotto dal percorso)")
    ap.add_argument("--live", action="store_true",
                    help="Pubblica DAVVERO. Senza questo flag: dry-run verificato.")
    ap.add_argument("--visible", action="store_true", help="Mostra il browser")
    ap.add_argument("--no-browser", action="store_true",
                    help="Salta la verifica di sessione (solo controlli sui file)")
    ap.add_argument("--force", action="store_true",
                    help="Ripubblica anche se gia' in published.json")
    args = ap.parse_args()

    cartella = Path(args.cartella).expanduser().resolve()
    print("=" * 72)
    print(" PUBBLICA - %s" % ("LIVE" if args.live else "DRY-RUN VERIFICATO"))
    print("=" * 72)
    print("Cartella : %s" % cartella)

    if not cartella.is_dir():
        print("\n[X] Cartella inesistente.\n\nVERDETTO: FAIL")
        return 1

    if not trova_slide(cartella):
        figlie = sottocartelle_con_slide(cartella)
        if figlie:
            print("\n[!] Nessuna slide qui dentro, ma queste sottocartelle ne hanno:")
            for d in figlie:
                print("      %s  (%d slide)" % (d.name, len(trova_slide(d))))
            print("\n    Rilancia il comando puntando a una di queste.")
        else:
            print("\n[X] Nessuna slide, ne' qui ne' nelle sottocartelle.")
        print("\nVERDETTO: FAIL")
        return 1

    canale = args.canale or rileva_canale(cartella)
    info = CANALI[canale]
    print("Canale   : %s -> %s%s" % (canale, info["account"],
                                     "" if args.canale is None else " (forzato)"))

    # --- 1. preflight sui file
    print("\n-- 1. CONTROLLO CONTENUTO --")
    errori, avvisi, slide, caption = preflight(cartella, args.force)
    for f in slide:
        d = dimensioni(f)
        d = ("%dx%d" % d) if d else "???"
        print("   [OK] %-18s %10s  %.2fMB" % (f.name, d, f.stat().st_size / 1048576))
    if caption:
        n_tag = len(re.findall(r"#\w+", caption))
        print("   [OK] %-18s %d caratteri, %d hashtag" % ("caption.txt", len(caption), n_tag))
    for a in avvisi:
        print("   [!]  %s" % a)
    for e in errori:
        print("   [X]  %s" % e)

    if errori:
        print("\nVERDETTO: FAIL - %d problema/i bloccante/i sul contenuto." % len(errori))
        return 1
    print("   => %d slide + caption: contenuto valido per Instagram." % len(slide))

    # --- 2. canale implementato?
    print("\n-- 2. CANALE --")
    if not info["pronto"]:
        print("   [X]  '%s' NON e' pronto: %s" % (canale, info["nota"]))
        print("\nVERDETTO: FAIL - contenuto ok, canale non utilizzabile oggi.")
        print("           Puoi forzare un canale pronto con --canale instagram.")
        return 1
    print("   [OK] '%s' ha un publisher reale (%s)." % (canale, info["nota"]))

    # --- 3. sessione
    print("\n-- 3. SESSIONE BROWSER --")
    if args.no_browser:
        autenticato, dettaglio = None, "verifica saltata (--no-browser)"
        print("   [!]  %s" % dettaglio)
    else:
        autenticato, dettaglio = verifica_sessione(canale, args.visible)
        simbolo = {True: "[OK]", False: "[X] ", None: "[!] "}[autenticato]
        print("   %s %s" % (simbolo, dettaglio))

    # --- 4. esito
    print("\n-- 4. ESITO --")
    if not args.live:
        print("   Dry-run: non e' stato pubblicato nulla (nessun post creato).")
        if autenticato is True:
            print("   Tutto verificato: contenuto valido, canale pronto, sessione attiva.")
            print("   Pronto per il --live.")
            print("\nVERDETTO: PASS (dry-run verificato, pronto a pubblicare)")
            return 0
        print("   Contenuto e canale sono verificati; la SESSIONE no.")
        print("   Manca: %s" % dettaglio)
        print("   Serve un login una tantum:")
        print("      python %s/setup_session.py" % info["cartella_sessione"])
        print("\nVERDETTO: PASS PARZIALE - contenuto pronto, sessione da fare "
              "(nessun PASS finto)")
        return 2

    # --- LIVE
    if autenticato is not True and not args.no_browser:
        print("   [X]  --live rifiutato: la sessione non risulta autenticata.")
        print("        Pubblicare adesso significherebbe sbattere sul login.")
        print("\nVERDETTO: FAIL - live non tentato di proposito.")
        return 1

    print("   --live attivo: pubblicazione REALE su %s..." % info["account"])
    sys.path.insert(0, str(WORKFLOW_DIR / "scripts"))
    import ig_carousel_publish as motore          # noqa: E402
    ok = motore.publish(cartella, visible=args.visible)

    if ok:
        segna_pubblicato(cartella, canale)
        print("\nVERDETTO: PASS - pubblicato su %s e segnato in published.json"
              % info["account"])
        return 0
    print("\nVERDETTO: FAIL - il motore ha riportato un fallimento (nessun post).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
