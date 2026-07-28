"""
Filtra i placeholder e invia solo i lead reali da emails_b6_ready.json.
Operazione atomica: filtro + invio nello stesso processo.
"""
import json
import os
import re
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
GMAIL_ACCOUNT = {"user": os.getenv("GMAIL_USER"), "password": os.getenv("GMAIL_APP_PASSWORD")}
INPUT_FILE = "emails_b6_ready.json"
DELAY_SECONDS = 90

PLACEHOLDER_PATTERNS = [
    r'estetica[a-z]+\d+\.it$',
    r'commercialista[a-z]+\d+\.it$',
    r'studiomedico[a-z]+\d+\.it$',
    r'legale[a-z]+\d+\.it$',
    r'fisio[a-z]+\d+\.it$',
    r'psicologo[a-z]+\d+\.it$',
    r'palestra[a-z]+\d+\.it$',
    r'studio[a-z]+(napoli|roma|milano|torino|firenze|bologna|bari|verona|genova)\d+\.it$',
    r'beauty[a-z]+\d+\.it$',
    r'fit[a-z]+\d+\.it$',
    r'[a-z]+(napoli|roma|milano|torino|firenze|bologna|bari|verona)\d+\.it$',
]

BLACKLIST = {"assistenza.pazienti@studiobittante.com"}


def is_placeholder(email):
    e = email.lower()
    for p in PLACEHOLDER_PATTERNS:
        if re.search(p, e):
            return True
    return False


def send_email(dest, oggetto, corpo):
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = f"Max <{GMAIL_ACCOUNT['user']}>"
        msg["To"] = dest
        msg["Subject"] = oggetto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as srv:
            srv.login(GMAIL_ACCOUNT["user"], GMAIL_ACCOUNT["password"])
            srv.send_message(msg)
        return True
    except Exception as e:
        print(f"         ERRORE SMTP: {e}")
        return False


def flush(data):
    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    dry_run = "--dry-run" in sys.argv

    with open(INPUT_FILE, encoding="utf-8", errors="replace") as f:
        data = json.load(f)

    # Marca tutti i placeholder come skip
    for e in data:
        if e.get("status") == "ready" and is_placeholder(e.get("email", "")):
            e["status"] = "skip_placeholder"

    to_send = [
        e for e in data
        if e.get("status") == "ready"
        and e.get("email", "").lower() not in BLACKLIST
    ]

    print(f"\n{'='*55}")
    print(f"  send_real_b6.py — solo lead reali")
    print(f"{'='*55}")
    print(f"  Da inviare (reali): {len(to_send)}")
    print(f"  Placeholder skippati: {sum(1 for e in data if e.get('status') == 'skip_placeholder')}")
    print(f"{'='*55}\n")

    if not to_send:
        print("Nessun lead reale da inviare.")
        flush(data)
        return

    print("Lead da inviare:")
    for e in to_send:
        print(f"  {e.get('nicchia','?'):15} | {e.get('email','?')}")
    print()

    if dry_run:
        print("DRY-RUN — nessuna email inviata.")
        return

    flush(data)

    inviati = 0
    errori = 0

    for i, item in enumerate(to_send, 1):
        dest = item["email"].strip()
        nome = item.get("page_name", dest)
        print(f"[{i:02d}/{len(to_send)}] {nome[:50]}")
        print(f"         To: {dest}")

        ok = send_email(dest, item["oggetto"], item["corpo"])
        if ok:
            inviati += 1
            item["status"] = "sent"
            print(f"         OK Inviata")
        else:
            errori += 1
            item["status"] = "send_failed"

        flush(data)

        if i < len(to_send):
            print(f"         Attendo {DELAY_SECONDS}s...")
            time.sleep(DELAY_SECONDS)

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
