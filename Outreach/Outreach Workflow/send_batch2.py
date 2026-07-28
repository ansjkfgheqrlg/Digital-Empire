"""
Batch 2 — invio email studi dentistici da leads_100.csv
Formato CSV: page_name, email, citta, website, telefono, ha_prenotazione_online, note

Run: python send_batch2.py
Modifica SKIP_FIRST per riprendere da dove ti sei fermato.
"""
import csv
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
CSV_PATH = "leads_100.csv"

# Cambia questi due valori per controllare il batch:
# - SKIP_FIRST: quanti lead saltare (già inviati in run precedenti)
# - BATCH_SIZE: quante email inviare in questa run
SKIP_FIRST = 0
BATCH_SIZE = 72

BLACKLIST = {
    "assistenza.pazienti@studiobittante.com",
}


def _genera_email(nome: str, citta: str) -> tuple[str, str]:
    oggetto = f"{nome} — quanti pazienti vi cercano la sera e non riescono a contattarvi?"

    corpo = f"""Ho cercato studi dentistici a {citta} e ho trovato {nome}. Per prenotare: solo telefono.

Il 62% delle ricerche mediche avviene tra le 18 e le 22, quando gli studi sono chiusi. Senza prenotazione online, quei pazienti — che vorrebbero venire da voi — finiscono dove trovano il pulsante "prenota adesso". Non per preferenza, per comodità.

Stima concreta per uno studio con il vostro traffico: 15-20 pazienti al mese che non tornano. Il reminder automatico SMS riduce i no-show del 30-35% — ogni appuntamento saltato vale mediamente €120-150 di agenda persa.

Ecco come funziona: il paziente sceglie uno slot disponibile, conferma in 30 secondi, riceve un reminder 48h prima. Gli studi dentistici che usano questo sistema lo impostano una volta e smettono di pensarci.

Sono Max — lavoro con studi medici e dentistici in Italia per chiudere questo tipo di gap. Prima analizzo ogni caso, poi (e solo allora) propongo qualcosa.

Ti chiedo 20 minuti per mostrarti quello che ho trovato nel vostro caso specifico.

Ha senso fare quella chiamata?

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
    # Carica CSV e filtra
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Deduplicazione email + skip SI prenotazione + blacklist
    seen_emails = set(BLACKLIST)
    leads_validi = []
    skippati_si = 0
    skippati_dup = 0

    for row in rows:
        email = row.get("email", "").strip().lower()
        if not email or "@" not in email:
            continue
        if row.get("ha_prenotazione_online", "").strip().upper() == "SI":
            skippati_si += 1
            continue
        if email in seen_emails:
            skippati_dup += 1
            continue
        seen_emails.add(email)
        leads_validi.append(row)

    totale_unici = len(leads_validi)
    batch = leads_validi[SKIP_FIRST: SKIP_FIRST + BATCH_SIZE]

    print(f"\nLeads 100 — statistiche:")
    print(f"  Totale righe CSV   : {len(rows)}")
    print(f"  Già con prenotaz.  : {skippati_si} (skippati)")
    print(f"  Duplicati rimossi  : {skippati_dup}")
    print(f"  Unici da inviare   : {totale_unici}")
    print(f"  Già saltati        : {SKIP_FIRST}")
    print(f"  Questo batch       : {len(batch)}")
    print(f"  Rimasti dopo batch : {totale_unici - SKIP_FIRST - len(batch)}")
    print(f"\nInizio invio...\n")

    inviati = 0
    errori = 0

    for i, lead in enumerate(batch, 1):
        email = lead["email"].strip().lower()
        nome = lead["page_name"].strip()
        citta = lead["citta"].strip() or "Italia"
        oggetto, corpo = _genera_email(nome, citta)

        nome_safe = nome.encode("ascii", errors="replace").decode("ascii")
        print(f"[{i:02d}/{len(batch)}] {nome_safe[:45]}")
        print(f"       > {email} ({citta})")

        ok = _invia(email, oggetto, corpo)
        if ok:
            inviati += 1
            print(f"       OK Inviata")
        else:
            errori += 1

        time.sleep(1.5)

    print(f"\n{'='*55}")
    print(f"RISULTATO  : {inviati} inviate | {errori} errori")
    print(f"PROSSIMO RUN: imposta SKIP_FIRST = {SKIP_FIRST + inviati}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
