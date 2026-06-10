"""
Follow-up Batch 2 — 72 studi dentistici (batch inviato 2026-05-07)

Stessa copy strategy di send_followup_b1.py.

QUANDO INVIARE: 2026-05-11 / 12 (giorno 4-5 dal batch 2)
Come: python send_followup_b2.py
"""
import csv
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = "max.infoproducer@gmail.com"
GMAIL_PASSWORD = "kkgj pnsh vupw rily"
CSV_PATH = "leads_100.csv"

BLACKLIST = {
    "assistenza.pazienti@studiobittante.com",
}


def _genera_followup(nome: str, citta: str) -> tuple[str, str]:
    oggetto = f"{nome} — quanti pazienti vi cercano la sera e non riescono a contattarvi?"

    corpo = f"""Ciao,

Qualche giorno fa vi ho scritto dei pazienti che cercano uno studio dentistico a {citta} di sera e non trovano come prenotare.

Un'unica domanda — e poi smetto di scrivere se la risposta è no: avete già una soluzione in atto per questo, o è ancora un tema aperto?

Max | Digital Empire"""

    return oggetto, corpo


def _invia(destinatario: str, oggetto: str, corpo: str) -> bool:
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = f"Max <{GMAIL_USER}>"
        msg["To"] = destinatario
        msg["Subject"] = oggetto
        msg.attach(MIMEText(corpo, "plain", "utf-8"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"  ERRORE: {e}")
        return False


def main():
    seen_emails = set(BLACKLIST)
    leads_validi = []

    with open(CSV_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            email = row.get("email", "").strip().lower()
            if not email or "@" not in email:
                continue
            if row.get("ha_prenotazione_online", "").strip().upper() == "SI":
                continue
            if email in seen_emails:
                continue
            seen_emails.add(email)
            leads_validi.append(row)

    print(f"\nFollow-up Batch 2 — statistiche:")
    print(f"  Da inviare: {len(leads_validi)}")

    # Preview
    print(f"\n{'─'*55}")
    print("PREVIEW prime 2 email:")
    print(f"{'─'*55}")
    for lead in leads_validi[:2]:
        nome = lead["page_name"].strip()
        citta = lead["citta"].strip() or "Italia"
        oggetto, corpo = _genera_followup(nome, citta)
        print(f"\nA: {lead['email']}")
        print(f"Oggetto: {oggetto}")
        print(f"---\n{corpo}\n---")

    print(f"\n{'─'*55}")
    auto = "--auto" in sys.argv
    if auto:
        print("Modalità automatica — invio senza conferma.")
    else:
        risposta = input("Confermi invio a tutti? [sì/no]: ").strip().lower()
        if risposta not in ("sì", "si", "s", "yes", "y"):
            print("Invio annullato.")
            return

    print(f"\nInizio invio follow-up...\n")
    inviati = 0
    errori = 0

    for i, lead in enumerate(leads_validi, 1):
        email = lead["email"].strip().lower()
        nome = lead["page_name"].strip()
        citta = lead["citta"].strip() or "Italia"
        oggetto, corpo = _genera_followup(nome, citta)

        nome_safe = nome.encode("ascii", errors="replace").decode("ascii")
        print(f"[{i:02d}/{len(leads_validi)}] {nome_safe[:45]}")
        print(f"       > {email} ({citta})")

        ok = _invia(email, oggetto, corpo)
        if ok:
            inviati += 1
            print(f"       OK Inviata")
        else:
            errori += 1

        time.sleep(2.0)

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
