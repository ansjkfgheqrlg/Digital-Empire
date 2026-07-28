"""
Aspetta che B5 finisca, poi invia le prime 472 email di B6.
Limite giornaliero: 500 email (28 B5 + 472 B6).

Run:
  python send_chain_b6.py
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

B5_FILE   = "emails_b5_ready.json"
B6_FILE   = "emails_b6_ready.json"
LIMIT_B6  = 472   # 500 - 28 B5
DELAY     = 45    # secondi tra invii

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


def _flush(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── 1. Attendi fine B5 ───────────────────────────────────────────────────────
print("Monitoro B5...")
while True:
    if os.path.exists(B5_FILE):
        with open(B5_FILE, encoding="utf-8") as f:
            b5 = json.load(f)
        remaining = sum(1 for e in b5 if e.get("status") == "ready")
        sent5 = sum(1 for e in b5 if e.get("status") == "sent")
        print(f"  B5: {sent5} sent, {remaining} ready", end="\r")
        if remaining == 0:
            print(f"\nB5 completata: {sent5} email inviate.")
            break
    time.sleep(10)

# ─── 2. Attendi generazione B6 ───────────────────────────────────────────────
print("Monitoro generazione B6...")
while True:
    if os.path.exists(B6_FILE):
        with open(B6_FILE, encoding="utf-8") as f:
            b6 = json.load(f)
        ready = sum(1 for e in b6 if e.get("status") == "ready")
        print(f"  B6 generate: {len(b6)} totali, {ready} ready", end="\r")
        # Considera completa se non cresce per 30 secondi
        if len(b6) >= 10:  # almeno partita
            prev = len(b6)
            time.sleep(30)
            with open(B6_FILE, encoding="utf-8") as f:
                b6_check = json.load(f)
            if len(b6_check) == prev:
                print(f"\nB6 generazione terminata: {len(b6_check)} email.")
                b6 = b6_check
                break
    else:
        time.sleep(10)

# ─── 3. Invia fino a LIMIT_B6 email ──────────────────────────────────────────
da_inviare = [
    e for e in b6
    if e.get("status") == "ready"
    and e.get("email", "").lower() not in BLACKLIST
][:LIMIT_B6]

print(f"\n{'='*55}")
print(f"  B6 — Invio {len(da_inviare)} email (limite {LIMIT_B6})")
print(f"  Delay: {DELAY}s (~{len(da_inviare)*DELAY//60}min tot)")
print(f"{'='*55}\n")

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

    _flush(B6_FILE, b6)

    if i < len(da_inviare):
        print(f"         Attendo {DELAY}s...")
        time.sleep(DELAY)

print(f"\n{'='*55}")
print(f"RISULTATO B6: {inviati} inviate | {errori} errori")
print(f"Totale oggi: {sent5 + inviati} / 500")
print(f"{'='*55}\n")
