"""
Pre-flight verifier — exit 0 = OK, exit 1 = problema.
Controlla: Playwright, sessione IG, caroselli pronti, published.json.
"""
import sys, json
from pathlib import Path

SCRIPT_DIR    = Path(__file__).parent.resolve()
WORKFLOW_DIR  = SCRIPT_DIR.parent
CAROSELLI_DIR = Path(r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\Lancio corso skill beast\Page\caroselli - Agency\Nuovi")
PUBLISHED_LOG = WORKFLOW_DIR / "published.json"
IG_SESSION    = WORKFLOW_DIR / "Instagram" / "session_data"
VALID_EXT     = {'.png', '.jpg', '.jpeg', '.webp'}

errors   = []
warnings = []

def ok(msg):  print(f"  [OK]  {msg}")
def err(msg): print(f"  [ERR] {msg}"); errors.append(msg)
def wrn(msg): print(f"  [WRN] {msg}"); warnings.append(msg)

print("\n=== DIGITAL EMPIRE — PRE-FLIGHT HEALTH CHECK ===\n")

# 1. Playwright
try:
    __import__("playwright.sync_api")
    ok("Playwright installato")
except Exception:
    err("Playwright mancante — esegui: pip install playwright && python -m playwright install chromium")

# 2. Chrome reale disponibile
import subprocess
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
chrome_found = any(Path(p).exists() for p in chrome_paths)
if chrome_found:
    ok("Google Chrome trovato")
else:
    wrn("Google Chrome non trovato — userà Chromium (meno stealth)")

# 3. Instagram session_data esiste e non è vuota
if IG_SESSION.exists() and any(IG_SESSION.iterdir()):
    ok(f"Sessione Instagram trovata: {IG_SESSION}")
else:
    err(f"Sessione Instagram mancante — esegui: python Instagram/setup_session.py")

# 4. published.json leggibile
pub = {}
if PUBLISHED_LOG.exists():
    try:
        pub = json.loads(PUBLISHED_LOG.read_text("utf-8"))
        ok(f"published.json OK — {len(pub)} caroselli già pubblicati")
    except json.JSONDecodeError as e:
        err(f"published.json corrotto: {e}")
else:
    ok("published.json non esiste ancora (fresh start OK)")

# 5. Directory caroselli
if not CAROSELLI_DIR.exists():
    err(f"Directory caroselli mancante: {CAROSELLI_DIR}")
else:
    ok(f"Directory caroselli: {CAROSELLI_DIR}")

    # 6. Almeno un carosello PRONTO
    pronto = []
    non_pronto = []
    for f in sorted(CAROSELLI_DIR.iterdir()):
        if not f.is_dir() or f.name in pub:
            continue
        imgs = [x for x in f.iterdir() if x.suffix.lower() in VALID_EXT]
        cap  = (f / "caption.txt").exists()
        if imgs and cap:
            pronto.append(f.name)
        else:
            motivo = "no img" if not imgs else "no caption"
            non_pronto.append(f"{f.name} ({motivo})")

    if pronto:
        ok(f"{len(pronto)} caroselli PRONTI: {', '.join(pronto)}")
    else:
        err("Nessun carosello PRONTO da pubblicare")
    if non_pronto:
        wrn(f"Non pronti: {', '.join(non_pronto[:3])}")

# 7. logs folder scrivibile
log_dir = WORKFLOW_DIR / "logs"
try:
    log_dir.mkdir(exist_ok=True)
    test_file = log_dir / ".write_test"
    test_file.write_text("ok")
    test_file.unlink()
    ok(f"Cartella logs scrivibile: {log_dir}")
except Exception as e:
    err(f"Cartella logs non scrivibile: {e}")

# --- Risultato ---
print()
if errors:
    print(f"HEALTH CHECK FALLITO — {len(errors)} errori, {len(warnings)} warning")
    for e in errors:
        print(f"  ! {e}")
    sys.exit(1)
elif warnings:
    print(f"HEALTH CHECK OK con {len(warnings)} warning — sistema pronto")
    sys.exit(0)
else:
    print("HEALTH CHECK PERFETTO — tutto OK")
    sys.exit(0)
