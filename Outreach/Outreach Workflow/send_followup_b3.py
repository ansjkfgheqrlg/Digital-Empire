"""
Follow-up Batch 3 — 37 email cold outreach multi-nicchia (batch inviato 2026-05-07)

Professionisti italiani: fisioterapisti, avvocati, psicologi, commercialisti,
palestre, estetica, studi medici, dentisti.

COPY STRATEGY:
- Angolo: domanda binaria + "smetto di scrivere se la risposta è no"
- Lunghezza: <60 parole (pattern interrupt rispetto all'email originale)
- Niente stats, niente pitch — solo una domanda irresistibile
- Stesso oggetto dell'originale → Gmail crea il thread automaticamente
- Usa nicchia + città per personalizzare la parola chiave (pazienti/iscritti/clienti)

QUANDO INVIARE: 2026-05-10 09:00 (giorno 3 dal batch 3)
Come: python send_followup_b3.py
Automatico: python send_followup_b3.py --auto
"""
import json
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = "max.infoproducer@gmail.com"
GMAIL_PASSWORD = "kkgj pnsh vupw rily"
JSON_PATH = "emails_ready.json"
DELAY_SECONDS = 90

BLACKLIST = {
    "assistenza.pazienti@studiobittante.com",
}


def _parola(nicchia: str) -> str:
    """Ritorna pazienti/iscritti/clienti in base alla nicchia."""
    n = nicchia.lower()
    if any(k in n for k in ["fisio", "psico", "medico", "dentist", "chirurg", "clinica",
                              "psicologo", "medic", "studio medico", "estetica"]):
        return "pazienti"
    if any(k in n for k in ["palestra", "yoga", "crossfit", "fitness", "pilates"]):
        return "iscritti"
    return "clienti"


def _nome_breve(page_name: str) -> str:
    for sep in ["|", "—", "-", "/"]:
        if sep in page_name:
            return page_name.split(sep)[0].strip()
    return page_name.strip()[:50]


def _genera_followup(nome: str, citta: str, parola: str) -> str:
    return f"""Ciao,

Qualche giorno fa ho scritto a {nome} riguardo ai {parola} che cercano i vostri servizi a {citta} di sera e non trovano come contattarvi.

Un'unica domanda — e poi smetto di scrivere se la risposta è no: avete già una soluzione in atto, o è ancora un tema aperto?

Puoi vedere come lavoriamo e prenotare una call qui: https://agency-empire-landing.vercel.app

Max | Digital Empire"""


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
    with open(JSON_PATH, encoding="utf-8") as f:
        all_records = json.load(f)

    # Filtra solo record con status "sent" e email valida
    leads = [
        e for e in all_records
        if e.get("status", "").strip().lower() == "sent"
        and e.get("email", "").strip()
        and "@" in e.get("email", "")
    ]

    # Rimuovi blacklist e duplicati
    seen = set(BLACKLIST)
    leads_da_inviare = []
    for e in leads:
        email = e["email"].strip().lower()
        if email in seen:
            continue
        seen.add(email)
        leads_da_inviare.append(e)

    print(f"\nFollow-up Batch 3 — statistiche:")
    print(f"  Record totali nel JSON  : {len(all_records)}")
    print(f"  Con status 'sent'       : {len(leads)}")
    print(f"  Blacklist/duplicati     : {len(leads) - len(leads_da_inviare)}")
    print(f"  Da inviare              : {len(leads_da_inviare)}")

    # Preview delle prime 2 email prima di procedere
    print(f"\n{'─'*55}")
    print("PREVIEW prime 2 email:")
    print(f"{'─'*55}")
    for record in leads_da_inviare[:2]:
        nome = _nome_breve(record["page_name"])
        citta = record.get("citta", "Italia").strip() or "Italia"
        nicchia = record.get("nicchia", "").strip()
        parola = _parola(nicchia)
        oggetto = record["oggetto"]
        corpo = _genera_followup(nome, citta, parola)
        print(f"\nA: {record['email']}")
        print(f"Nicchia: {nicchia}  →  parola: {parola}")
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

    print(f"\nInizio invio follow-up... (delay {DELAY_SECONDS}s tra invii)\n")

    inviati = 0
    errori = 0

    for i, record in enumerate(leads_da_inviare, 1):
        email = record["email"].strip().lower()
        nome = _nome_breve(record["page_name"])
        citta = record.get("citta", "Italia").strip() or "Italia"
        nicchia = record.get("nicchia", "").strip()
        parola = _parola(nicchia)
        oggetto = record["oggetto"]
        corpo = _genera_followup(nome, citta, parola)

        nome_safe = nome.encode("ascii", errors="replace").decode("ascii")
        print(f"[{i:02d}/{len(leads_da_inviare)}] {nome_safe[:45]}")
        print(f"       > {email} ({citta} | {nicchia})")

        ok = _invia(email, oggetto, corpo)
        if ok:
            inviati += 1
            print(f"       OK Inviata")
        else:
            errori += 1

        if i < len(leads_da_inviare):
            time.sleep(DELAY_SECONDS)

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
