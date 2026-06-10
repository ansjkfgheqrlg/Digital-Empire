"""
Follow-up Batch 1 — 29 studi dentistici (batch originale inviato 2026-05-06)

COPY STRATEGY:
- Angolo: domanda binaria + "smetto di scrivere se la risposta è no"
- Lunghezza: <60 parole (vs ~160 parole email 1 — pattern interrupt)
- Niente stats, niente pitch — solo una domanda irresistibile
- Stesso oggetto dell'originale → Gmail threada in automatico

QUANDO INVIARE: 2026-05-09 / 10 / 11 (giorno 3-5 dal batch 1)
Come: python send_followup_b1.py
"""
import csv
import re
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = "max.infoproducer@gmail.com"
GMAIL_PASSWORD = "kkgj pnsh vupw rily"
CSV_PATH = "leads_trovati.csv"
MAX_LEADS = 30  # solo il primo batch

BLACKLIST = {
    "assistenza.pazienti@studiobittante.com",
}

# Città non rilevabili da page_name — override manuale
CITTA_OVERRIDE = {
    "info@studiosangottardo.it":          "Milano",
    "farhangh@libero.it":                 "Milano",
    "adc-online@assistenzadentistica.it": "Milano",
    "dentistamilanorizzasrl@gmail.com":   "Milano",
    "info@studiovirzi.com":               "Milano",
    "info@passionsmile.it":               "Milano",
    "info@dentalluc.it":                  "Milano",
    "studiosancisrl@gmail.com":           "Milano",
    "sorrisoitalia@libero.it":            "Milano",
    "dentistaeur@gmail.com":              "Roma",
    "info@studiotomarelli.com":           "Roma",
    "info@dottvincenzorusso.it":          "Roma",
    "info@healthysmileinrome.com":        "Roma",
    "odontoiatriapiccolo@gmail.com":      "Roma",
    "studiodelfinoanzisi@gmail.com":      "Roma",
    "info@alessandrodonzelli.com":        "Roma",
}

CITTA_PATTERN = re.compile(
    r'\b(Milano|Roma|Napoli|Torino|Firenze|Bologna|Venezia|Genova|Palermo|Catania|Bari|Verona)\b',
    re.IGNORECASE,
)


def _estrai_citta(page_name: str) -> str:
    m = CITTA_PATTERN.search(page_name)
    if m:
        return m.group(1).capitalize()
    if " Mi" in page_name or "Milan" in page_name:
        return "Milano"
    return "Italia"


def _nome_breve(page_name: str) -> str:
    for sep in ["|", "—", "-", "/"]:
        if sep in page_name:
            return page_name.split(sep)[0].strip()
    return page_name.strip()[:50]


def _genera_followup(nome: str, citta: str) -> tuple[str, str]:
    # Stesso oggetto dell'email 1 → Gmail crea il thread automaticamente
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
    with open(CSV_PATH, encoding="utf-8") as f:
        all_rows = [r for r in csv.DictReader(f) if r.get("email", "").strip() and "@" in r.get("email", "")]

    leads = all_rows[:MAX_LEADS]
    leads_da_inviare = [r for r in leads if r["email"].strip().lower() not in BLACKLIST]

    print(f"\nFollow-up Batch 1 — statistiche:")
    print(f"  Leads batch 1      : {len(leads)}")
    print(f"  Blacklist saltati  : {len(leads) - len(leads_da_inviare)}")
    print(f"  Da inviare         : {len(leads_da_inviare)}")

    # Preview delle prime 2 email prima di procedere
    print(f"\n{'─'*55}")
    print("PREVIEW prime 2 email:")
    print(f"{'─'*55}")
    for lead in leads_da_inviare[:2]:
        e = lead["email"].strip().lower()
        nome = _nome_breve(lead["page_name"])
        citta = CITTA_OVERRIDE.get(e) or _estrai_citta(lead["page_name"])
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

    for i, lead in enumerate(leads_da_inviare, 1):
        email = lead["email"].strip().lower()
        nome = _nome_breve(lead["page_name"])
        citta = CITTA_OVERRIDE.get(email) or _estrai_citta(lead["page_name"])
        oggetto, corpo = _genera_followup(nome, citta)

        nome_safe = nome.encode("ascii", errors="replace").decode("ascii")
        print(f"[{i:02d}/{len(leads_da_inviare)}] {nome_safe[:45]}")
        print(f"       > {email} ({citta})")

        ok = _invia(email, oggetto, corpo)
        if ok:
            inviati += 1
            print(f"       OK Inviata")
        else:
            errori += 1

        time.sleep(2.0)  # leggermente più lento del batch 1

    print(f"\n{'='*55}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
