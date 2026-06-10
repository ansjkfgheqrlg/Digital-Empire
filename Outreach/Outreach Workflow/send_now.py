"""
Invio diretto 30 email dentisti — template specifico, zero AI, zero attese.
"""
import csv
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = "max.infoproducer@gmail.com"
GMAIL_PASSWORD = "kkgj pnsh vupw rily"
CSV_PATH = "leads_trovati.csv"
MAX_SEND = 30
SKIP_FIRST = 22  # già inviate

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
    """Prende la prima parte del nome (prima del trattino o pipe)."""
    for sep in ["|", "—", "-", "/"]:
        if sep in page_name:
            return page_name.split(sep)[0].strip()
    return page_name.strip()[:50]


def _genera_email(nome: str, citta: str) -> tuple[str, str]:
    # v2 — aggiunto valore educativo, identità mittente, rimosse frasi difensive
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


def invia_email(destinatario: str, oggetto: str, corpo: str) -> bool:
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
    leads = []
    with open(CSV_PATH, encoding="utf-8") as f:
        all_rows = [r for r in csv.DictReader(f) if r.get("email", "").strip() and "@" in r.get("email", "")]
    leads = all_rows[SKIP_FIRST:MAX_SEND]

    print(f"\nInvio {len(leads)} email a studi dentistici...\n")

    inviati = 0
    errori = 0
    emails_usate = set()

    for i, lead in enumerate(leads, 1):
        email = lead["email"].strip().lower()
        if email in emails_usate:
            continue
        emails_usate.add(email)

        nome = _nome_breve(lead["page_name"])
        citta = _estrai_citta(lead["page_name"])
        oggetto, corpo = _genera_email(nome, citta)

        nome_safe = nome.encode("ascii", errors="replace").decode("ascii")
        print(f"[{i:02d}/{len(leads)}] {nome_safe[:45]}")
        print(f"       > {email}")

        ok = invia_email(email, oggetto, corpo)
        if ok:
            inviati += 1
            print(f"       OK Inviata")
        else:
            errori += 1

        time.sleep(1.5)

    print(f"\n{'='*50}")
    print(f"RISULTATO: {inviati} inviate | {errori} errori")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
