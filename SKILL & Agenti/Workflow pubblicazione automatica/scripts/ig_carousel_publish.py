#!/usr/bin/env python3
"""
Digital Empire Instagram Carousel Publisher
Credenziali: Instagram/config.py (IG_USERNAME, IG_PASSWORD)

python ig_carousel_publish.py --list
python ig_carousel_publish.py --auto [--visible]
python ig_carousel_publish.py --folder "Content factory" [--visible]
"""

import os, sys, json, time, argparse
from pathlib import Path
from datetime import datetime

SCRIPT_DIR    = Path(__file__).parent.resolve()
WORKFLOW_DIR  = SCRIPT_DIR.parent
IG_SESSION    = WORKFLOW_DIR / "Instagram" / "session_data"
PUBLISHED_LOG = WORKFLOW_DIR / "published.json"
CAROSELLI_DIR = Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Lancio corso skill beast\Page\caroselli - Agency\Nuovi")
VALID_EXT     = {'.png', '.jpg', '.jpeg', '.webp'}

import importlib.util as _ilu
_cfg = WORKFLOW_DIR / "Instagram" / "config.py"
if _cfg.exists():
    _spec = _ilu.spec_from_file_location("ig_config", str(_cfg))
    _mod  = _ilu.module_from_spec(_spec)      # type: ignore[arg-type]
    _spec.loader.exec_module(_mod)             # type: ignore[union-attr]
    IG_USERNAME: str = _mod.IG_USERNAME
    IG_PASSWORD: str = _mod.IG_PASSWORD
else:
    IG_USERNAME = os.environ.get("IG_USERNAME", "")
    IG_PASSWORD = os.environ.get("IG_PASSWORD", "")

# ---- log helpers ----
def load_pub():
    return json.loads(PUBLISHED_LOG.read_text("utf-8")) if PUBLISHED_LOG.exists() else {}

def save_pub(d):
    PUBLISHED_LOG.write_text(json.dumps(d, indent=2, ensure_ascii=False), "utf-8")

def mark_pub(folder, url=""):
    d = load_pub()
    d[folder.name] = {"folder": str(folder), "published_at": datetime.now().isoformat(), "url": url}
    save_pub(d)
    print(f"[LOG] Marcato pubblicato: {folder.name}")

# ---- folder helpers ----
def get_imgs(folder):
    return sorted([f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in VALID_EXT])

def get_cap(folder):
    c = folder / "caption.txt"
    return c.read_text("utf-8").strip() if c.exists() else ""

def is_ready(folder):
    ii = get_imgs(folder)
    if not ii: return False, "no immagini"
    if not get_cap(folder): return False, "no caption.txt"
    if len(ii) > 10: return False, f"troppe img ({len(ii)})"
    return True, f"{len(ii)} img OK"

# ---- list ----
def cmd_list():
    pub = load_pub()
    folders = sorted([f for f in CAROSELLI_DIR.iterdir() if f.is_dir()])
    print(f"\n{'NOME':<32} {'IMG':>4}  CAP  STATO")
    print("-" * 60)
    for f in folders:
        ni = len(get_imgs(f))
        cap_ok = "SI" if get_cap(f) else "NO"
        if f.name in pub:
            stato = "PUBBLICATO " + pub[f.name].get("published_at", "")[:10]
        else:
            ok, msg = is_ready(f)
            stato = "PRONTO" if ok else msg
        print(f"{f.name:<32} {ni:>4}   {cap_ok}  {stato}")
    print()

# ---- publisher ----
def dismiss_popups(pg):
    for txt in ["Non ora", "Salta", "Ignora"]:
        try:
            b = pg.get_by_role("button", name=txt)
            if b.is_visible(timeout=1500):
                b.first.click()
                time.sleep(0.8)
        except Exception:
            pass

def do_login(pg):
    if pg.locator('input[name="username"]').count() > 0:
        print("[IG] Login in corso...")
        pg.fill('input[name="username"]', IG_USERNAME)
        pg.fill('input[name="password"]', IG_PASSWORD)
        pg.get_by_role("button", name="Accedi").click()
        pg.wait_for_url("https://www.instagram.com/**", timeout=30000)
        time.sleep(3)
        dismiss_popups(pg)
        print("[IG] Login OK")

def publish(folder, visible=False):
    ii  = get_imgs(folder)
    cap = get_cap(folder)
    print(f"\n{'='*55}")
    print(f"[IG] {folder.name} — {len(ii)} slide")
    print(f"[IG] Caption: {cap[:60]}...")
    print(f"{'='*55}")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERRORE: pip install playwright && python -m playwright install chromium")
        return False

    IG_SESSION.mkdir(parents=True, exist_ok=True)
    files = [str(i) for i in ii]

    with sync_playwright() as p:
        # Usa Chrome reale + anti-detection (come Core/browser_manager.py)
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(IG_SESSION),
            headless=not visible,
            viewport={"width": 1280, "height": 900},
            channel="chrome",
            args=["--disable-blink-features=AutomationControlled"],
            ignore_default_args=["--enable-automation"],
            locale="it-IT",
        )
        pg = ctx.new_page()
        pg.goto("https://www.instagram.com/", wait_until="networkidle", timeout=30000)
        time.sleep(2)
        dismiss_popups(pg)
        do_login(pg)

        if "login" in pg.url:
            print("[IG] ERRORE: login fallito")
            ctx.close()
            return False

        # Crea nuovo post
        print("[IG] Crea nuovo post...")
        clicked = False
        for sel in ['svg[aria-label="Nuovo post"]', '[aria-label="New post"]']:
            try:
                b = pg.locator(sel).first
                if b.is_visible(timeout=2500):
                    b.click()
                    clicked = True
                    break
            except Exception:
                pass
        if not clicked:
            pg.get_by_role("link", name="Crea").click()
        time.sleep(2)

        # Upload
        print(f"[IG] Upload {len(files)} immagini...")
        with pg.expect_file_chooser(timeout=12000) as fc:
            b = pg.get_by_text("Seleziona dal computer")
            if not b.is_visible(timeout=3000):
                b = pg.get_by_role("button", name="Seleziona dal computer")
            b.click()
        fc.value.set_files(files)
        time.sleep(4)

        # Formato originale
        for lbl in ["Formato originale", "Originale"]:
            try:
                b = pg.get_by_role("button", name=lbl)
                if b.is_visible(timeout=2000):
                    b.click()
                    time.sleep(1)
                    break
            except Exception:
                pass

        # Avanti x2
        for step in ["crop", "filtri"]:
            print(f"[IG] Avanti ({step})...")
            pg.get_by_role("button", name="Avanti").click()
            time.sleep(2)

        # Caption
        print("[IG] Inserisco caption...")
        for sel in ['textarea[aria-label*="didascalia"]', '[aria-label*="caption"]', 'div[role="textbox"]']:
            try:
                b = pg.locator(sel).first
                if b.is_visible(timeout=2500):
                    b.click()
                    b.fill(cap)
                    break
            except Exception:
                pass
        time.sleep(2)

        # Condividi
        print("[IG] Condividi...")
        pg.get_by_role("button", name="Condividi").click()

        # Attendi conferma
        success = False
        try:
            pg.get_by_text("Il tuo post e stato condiviso").wait_for(timeout=90000)
            success = True
        except Exception:
            try:
                pg.wait_for_url("https://www.instagram.com/", timeout=20000)
                success = True
            except Exception as e:
                print(f"[IG] FALLITO: {e}")
                pg.screenshot(path=str(WORKFLOW_DIR / "debug_ig.png"))

        ctx.close()
        if success:
            print("[IG] POST PUBBLICATO!")
        return success

# ---- main ----
def main():
    ap = argparse.ArgumentParser(description="DE Instagram Carousel Publisher")
    ap.add_argument("--folder")
    ap.add_argument("--auto",    action="store_true")
    ap.add_argument("--list",    action="store_true")
    ap.add_argument("--visible", action="store_true")
    args = ap.parse_args()

    if args.list:
        cmd_list()
        return

    folder = None
    if args.folder:
        folder = CAROSELLI_DIR / args.folder
        if not folder.exists():
            print(f"Cartella non trovata: {folder}")
            sys.exit(1)
    elif args.auto:
        pub = load_pub()
        for f in sorted(CAROSELLI_DIR.iterdir()):
            if not f.is_dir() or f.name in pub:
                if f.is_dir() and f.name in pub:
                    print(f"[SKIP] Gia pubblicato: {f.name}")
                continue
            ok, msg = is_ready(f)
            if ok:
                folder = f
                print(f"[AUTO] Selezionato: {f.name} ({msg})")
                break
            else:
                print(f"[SKIP] Non pronto ({msg}): {f.name}")
        if not folder:
            print("Tutti i caroselli pronti sono gia stati pubblicati.")
            return
    else:
        ap.print_help()
        return

    pub = load_pub()
    if folder.name in pub:
        print(f"STOP: '{folder.name}' gia pubblicato!")
        sys.exit(1)

    ok, msg = is_ready(folder)
    if not ok:
        print(f"STOP: {msg}")
        sys.exit(1)

    if publish(folder, visible=args.visible):
        mark_pub(folder)
        print(f"\nOK — {folder.name} pubblicato!")
    else:
        print(f"\nFALLITO — {folder.name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
