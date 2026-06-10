"""
resend_failed.py — Reinvia le email fallite nell'ultimo log di invio.
Uso: python resend_failed.py
"""
import csv, json, os, sys, time
from pathlib import Path
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
load_dotenv(Path(__file__).parent / ".env")

BASE    = Path(__file__).parent
LOGDIR  = BASE / "output"
BK_FILE = LOGDIR / "emails_post_bibbia.json"

# ── Trova il log di oggi ──────────────────────────────────────────────────────
logs = sorted(LOGDIR.glob("*_invio_log.csv"), reverse=True)
if not logs:
    print("Nessun log trovato in output/")
    sys.exit(1)
log_path = logs[0]
print(f"[RESEND] Log: {log_path.name}")

# ── Leggi email fallite ───────────────────────────────────────────────────────
fallite = []
with open(log_path, newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        if row.get("stato", "").strip().lower() != "inviata":
            fallite.append(row["email"].strip().lower())

print(f"[RESEND] {len(fallite)} email da reinviare")
if not fallite:
    print("Nessun errore nel log — tutto ok!")
    sys.exit(0)

# ── Recupera corpo email dal backup ──────────────────────────────────────────
if not BK_FILE.exists():
    print(f"Backup email non trovato: {BK_FILE}")
    sys.exit(1)

tutte = json.loads(BK_FILE.read_text(encoding="utf-8"))
da_inviare = [e for e in tutte if e.get("email", "").strip().lower() in set(fallite)]
print(f"[RESEND] Trovate {len(da_inviare)}/{len(fallite)} email nel backup")

if not da_inviare:
    print("Nessuna email trovata nel backup — niente da reinviare.")
    sys.exit(0)

# ── Invio SMTP con reconnect automatico ──────────────────────────────────────
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

gmail_user = os.getenv("GMAIL_USER", "").strip()
gmail_pass = os.getenv("GMAIL_APP_PASSWORD", "").strip()

def apri_connessione():
    s = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
    s.ehlo(); s.starttls(); s.login(gmail_user, gmail_pass)
    return s

print(f"\n[RESEND] Avvio reinvio da {gmail_user}\n")
server = apri_connessione()
inviati, errori = 0, 0

for i, em in enumerate(da_inviare, 1):
    dest    = em["email"]
    oggetto = em.get("oggetto", "")
    corpo   = em.get("corpo", "")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = oggetto
    msg["From"]    = gmail_user
    msg["To"]      = dest
    msg["Reply-To"] = gmail_user
    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    try:
        server.sendmail(gmail_user, dest, msg.as_string())
        inviati += 1
        print(f"[RESEND] {i}/{len(da_inviare)} ✓ {dest[:50]}")
    except Exception as e:
        errori += 1
        print(f"[RESEND] {i}/{len(da_inviare)} ✗ {dest[:50]} — {e}")
        # Riconnetti e riprova
        try:
            server = apri_connessione()
            server.sendmail(gmail_user, dest, msg.as_string())
            inviati += 1
            errori -= 1
            print(f"[RESEND]   → retry OK")
        except Exception as e2:
            print(f"[RESEND]   → retry fallito: {e2}")

    if i % 50 == 0 and i < len(da_inviare):
        try: server.quit()
        except: pass
        server = apri_connessione()
        print(f"[RESEND] Riconnessione SMTP ({i}/{len(da_inviare)})")

    if i < len(da_inviare):
        time.sleep(3.5)

try: server.quit()
except: pass

print(f"\n[RESEND] Completato: {inviati} reinviate, {errori} errori")
