"""
Invia le email da emails_ready.json.
Legge il file, mostra un riepilogo, chiede conferma, poi invia una per una.
Aggiorna lo status in tempo reale dopo ogni invio.

Run:
  python send_ready.py
  python send_ready.py --dry-run   # mostra lista senza inviare
"""
import json
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─── MULTI-ACCOUNT ROUND-ROBIN ───────────────────────────────────────────────
# Per ogni account Gmail occorre una App Password (NON la password normale).
# Come ottenerla: Google Account → Sicurezza → Verifica in due passaggi → App password
# Crea una App Password con nome "Mail" e copia le 16 lettere (es. "aaaa bbbb cccc dddd").
# Sostituisci ACCOUNT2_EMAIL / ACCOUNT3_EMAIL con le email reali e le relative App Password.
GMAIL_ACCOUNTS = [
    {"user": "max.infoproducer@gmail.com",  "password": "kkgj pnsh vupw rily"},
    {"user": "ACCOUNT2_EMAIL",              "password": "ACCOUNT2_APP_PASSWORD"},
    {"user": "ACCOUNT3_EMAIL",              "password": "ACCOUNT3_APP_PASSWORD"},
]

# Solo account con email reale (esclude placeholder)
_ACTIVE_ACCOUNTS = [a for a in GMAIL_ACCOUNTS if "@" in a["user"] and a["user"] != "ACCOUNT2_EMAIL" and a["user"] != "ACCOUNT3_EMAIL"]

INPUT_PATH     = next((sys.argv[sys.argv.index("--input")+1] for i,a in enumerate(sys.argv) if a=="--input"), "emails_ready.json")
DELAY_SECONDS  = 90    # ~40 email/ora — più sicuro per reputazione account

# DELIVERABILITY: limite giornaliero per singola mailbox Gmail.
# Superare 50/giorno brucia la reputazione e causa "Message blocked".
# Per volumi maggiori: aggiungere più account Gmail (round-robin orizzontale).
DAILY_LIMIT_PER_ACCOUNT = 50

BLACKLIST = {
    "assistenza.pazienti@studiobittante.com",
}


# ─── SMTP ────────────────────────────────────────────────────────────────────

def _invia(destinatario: str, oggetto: str, corpo: str, account_idx: int = 0) -> bool:
    account  = _ACTIVE_ACCOUNTS[account_idx % len(_ACTIVE_ACCOUNTS)]
    user     = account["user"]
    password = account["password"]
    try:
        msg = MIMEMultipart("alternative")
        msg["From"]    = f"Max <{user}>"
        msg["To"]      = destinatario
        msg["Subject"] = oggetto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as srv:
            srv.login(user, password)
            srv.send_message(msg)
        return True
    except Exception as e:
        print(f"         ERRORE SMTP: {e}")
        return False


def _flush(data: list):
    with open(INPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    auto    = "--auto" in sys.argv

    with open(INPUT_PATH, encoding="utf-8") as f:
        all_emails = json.load(f)

    da_inviare = [
        e for e in all_emails
        if e.get("status") == "ready"
        and e.get("email", "").lower() not in BLACKLIST
    ]
    gia_inviate  = sum(1 for e in all_emails if e.get("status") == "sent")
    con_errori   = sum(1 for e in all_emails if "error" in e.get("status", ""))

    print(f"\n{'='*55}")
    print(f"  emails_ready.json — riepilogo")
    print(f"{'='*55}")
    print(f"  Da inviare   : {len(da_inviare)}")
    print(f"  Già inviate  : {gia_inviate}")
    print(f"  Con errori   : {con_errori}")
    print(f"  Blacklist    : {len(BLACKLIST)} indirizzi bloccati")
    print(f"  Delay        : {DELAY_SECONDS}s tra invii (~{len(da_inviare)*DELAY_SECONDS//60}min tot)")
    print(f"{'='*55}\n")

    if not da_inviare:
        print("Nessuna email da inviare.")
        return

    # Preview prime 3
    print("ANTEPRIMA prime 3 email:\n")
    for e in da_inviare[:3]:
        print(f"  [{e['nicchia']}] {e['page_name']}")
        print(f"  To     : {e['email']}")
        print(f"  Oggetto: {e['oggetto']}")
        print()

    if dry_run:
        print("DRY-RUN: nessuna email inviata. Rimuovi --dry-run per inviare.")
        return

    if not auto:
        risposta = input(f"Inviare {len(da_inviare)} email? [s/N] ").strip().lower()
        if risposta not in ("s", "si", "sì", "y", "yes"):
            print("Annullato.")
            return
    else:
        print(f"AUTO: invio {len(da_inviare)} email senza conferma interattiva.\n")

    # Applica limite giornaliero
    if len(da_inviare) > DAILY_LIMIT_PER_ACCOUNT:
        print(f"ATTENZIONE: {len(da_inviare)} email pronte, ma limite giornaliero = {DAILY_LIMIT_PER_ACCOUNT}.")
        print(f"Invio solo le prime {DAILY_LIMIT_PER_ACCOUNT}. Esegui di nuovo domani per le restanti.\n")
        da_inviare = da_inviare[:DAILY_LIMIT_PER_ACCOUNT]

    print(f"\nInizio invio ({len(da_inviare)} email, cap {DAILY_LIMIT_PER_ACCOUNT}/giorno)...\n")

    inviati = 0
    errori  = 0

    for i, item in enumerate(da_inviare, 1):
        dest    = item["email"].strip()
        oggetto = item["oggetto"]
        corpo   = item["corpo"]
        nome    = item["page_name"]

        account_idx = i - 1
        account_user = _ACTIVE_ACCOUNTS[account_idx % len(_ACTIVE_ACCOUNTS)]["user"]
        print(f"[{i:02d}/{len(da_inviare)}] {nome[:45]}")
        print(f"         To     : {dest}")
        print(f"         Oggetto: {oggetto[:60]}")
        print(f"         From   : {account_user}")

        ok = _invia(dest, oggetto, corpo, account_idx=account_idx)
        if ok:
            inviati += 1
            item["status"] = "sent"
            print(f"         OK Inviata")
        else:
            errori += 1
            item["status"] = "send_failed"

        _flush(all_emails)

        if i < len(da_inviare):
            print(f"         Attendo {DELAY_SECONDS}s...")
            time.sleep(DELAY_SECONDS)

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"Log aggiornato: {INPUT_PATH}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
