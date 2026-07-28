"""
Aspetta che la generazione B6 si stabilizzi (nessun nuovo elemento per 90s),
poi invia le email ready fino al limite giornaliero.

Limite oggi: 500 - 65 gia' inviati (29 B5 + 36 B6 prima tranche) = 435

Run: python send_b6_remaining.py
"""
import json
import os
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

B6_FILE        = "emails_b6_ready.json"
ALREADY_SENT   = 65    # 29 B5 + 36 B6 prima tranche
DAILY_LIMIT    = 500
LIMIT_THIS_RUN = DAILY_LIMIT - ALREADY_SENT   # 435
DELAY          = 45

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_APP_PASSWORD")

BLACKLIST = {"assistenza.pazienti@studiobittante.com"}


def _invia(dest, oggetto, corpo):
    try:
        msg = MIMEMultipart("alternative")
        msg["From"]    = f"Max <{GMAIL_USER}>"
        msg["To"]      = dest
        msg["Subject"] = oggetto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as srv:
            srv.login(GMAIL_USER, GMAIL_PASS)
            srv.send_message(msg)
        return True
    except Exception as e:
        print(f"         ERRORE: {e}")
        return False


def _flush(data):
    with open(B6_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _load():
    with open(B6_FILE, encoding="utf-8") as f:
        return json.load(f)


# ─── 1. Attendi stabilizzazione generazione ───────────────────────────────────
print("Attendo stabilizzazione generazione B6 (nessun nuovo elemento per 90s)...")
stable_count = 0
last_count = 0
while True:
    data = _load()
    current = len(data)
    ready = sum(1 for e in data if e.get("status") == "ready")
    sent = sum(1 for e in data if e.get("status") == "sent")
    print(f"  Generati: {current} | Ready: {ready} | Sent: {sent}", end="\r")

    if current == last_count and current > 50:
        stable_count += 1
        if stable_count >= 3:   # 3 × 30s = 90s stabile
            print(f"\nGenerazione completata: {current} email totali.")
            break
    else:
        stable_count = 0
        last_count = current

    time.sleep(30)

# ─── 2. Carica DOPO stabilizzazione (no race condition) ───────────────────────
data = _load()
da_inviare = [
    e for e in data
    if e.get("status") == "ready"
    and e.get("email", "").lower() not in BLACKLIST
][:LIMIT_THIS_RUN]

print(f"\n{'='*55}")
print(f"  B6 remaining — {len(da_inviare)} email da inviare")
print(f"  Limite odierno: {DAILY_LIMIT} (gia' inviati: {ALREADY_SENT})")
print(f"  Delay: {DELAY}s (~{len(da_inviare)*DELAY//60}min tot)")
print(f"{'='*55}\n")

if not da_inviare:
    print("Nessuna email da inviare.")
    sys.exit(0)

# ─── 3. Invia ────────────────────────────────────────────────────────────────
inviati = errori = 0
for i, item in enumerate(da_inviare, 1):
    dest    = item["email"].strip()
    oggetto = item["oggetto"]
    corpo   = item["corpo"]
    nome    = item["page_name"]

    print(f"[{i:03d}/{len(da_inviare)}] {nome[:40]}")
    print(f"         To: {dest}")
    print(f"         Oggetto: {oggetto[:55]}")

    ok = _invia(dest, oggetto, corpo)
    if ok:
        inviati += 1
        item["status"] = "sent"
        print(f"         OK")
    else:
        errori += 1
        item["status"] = "send_failed"

    _flush(data)

    if i < len(da_inviare):
        print(f"         Attendo {DELAY}s...")
        time.sleep(DELAY)

print(f"\n{'='*55}")
print(f"RISULTATO: {inviati} inviate | {errori} errori")
print(f"Totale oggi: {ALREADY_SENT + inviati} / {DAILY_LIMIT}")
print(f"{'='*55}\n")
