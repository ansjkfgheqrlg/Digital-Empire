"""
Invio Email via Gmail SMTP

Invia un'email approvata a un lead specifico usando Gmail.
Richiede revisione e approvazione manuale della bozza prima dell'invio.
Aggiorna automaticamente lo stato nel Google Sheets dopo l'invio.

IMPORTANTE: Non inviare mai senza aver prima letto e approvato la bozza.

Uso:
    python implementation/send_emails.py --id NS-MI-20250115143022
    python implementation/send_emails.py --id NS-MI-20250115143022 --oggetto "Il mio oggetto personalizzato"

Input:
    --id: ID del lead (obbligatorio)
    --oggetto: Oggetto email (se non specificato, usa il primo dalla bozza)
    --anteprima: Mostra l'anteprima senza inviare

Output:
    Email inviata al destinatario
    Stato aggiornato in Google Sheets: STATO_OUTREACH=inviato
"""

import os
import sys
import argparse
import smtplib
from datetime import datetime, timedelta
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger
from implementation.utils.sheets_client import crea_client_da_env, INTESTAZIONI_NO_SITO, INTESTAZIONI_FUNNEL_SCARSO

load_dotenv()

CARTELLA_BOZZE = "bozze_email"


def trova_bozza(id_lead: str) -> tuple:
    """
    Trova il file bozza più recente per un lead.

    Args:
        id_lead: ID del lead

    Returns:
        Tupla (percorso_file, testo_completo) o (None, None)
    """
    cartella_bozze = Path(CARTELLA_BOZZE)
    if not cartella_bozze.exists():
        return None, None

    # Cerca in tutte le date
    bozze_trovate = sorted(
        cartella_bozze.glob(f"**/{id_lead}_bozza*.txt"),
        key=lambda p: p.stat().st_mtime,
        reverse=True  # Più recente prima
    )

    if not bozze_trovate:
        return None, None

    percorso = bozze_trovate[0]
    with open(percorso, "r", encoding="utf-8") as f:
        testo = f.read()

    return str(percorso), testo


def estrai_componenti_email(testo_bozza: str) -> dict:
    """
    Estrae oggetto e corpo dalla bozza email.

    Args:
        testo_bozza: Contenuto del file bozza

    Returns:
        Dict con: oggetto_1, oggetto_2, oggetto_3, corpo
    """
    componenti = {
        "oggetto_1": "",
        "oggetto_2": "",
        "oggetto_3": "",
        "corpo": ""
    }

    linee = testo_bozza.split("\n")
    in_corpo = False
    corpo_linee = []

    for linea in linee:
        # Skip commenti (righe che iniziano con #)
        if linea.strip().startswith("#"):
            continue

        if linea.startswith("OGGETTO 1:"):
            componenti["oggetto_1"] = linea.replace("OGGETTO 1:", "").strip()
        elif linea.startswith("OGGETTO 2:"):
            componenti["oggetto_2"] = linea.replace("OGGETTO 2:", "").strip()
        elif linea.startswith("OGGETTO 3:"):
            componenti["oggetto_3"] = linea.replace("OGGETTO 3:", "").strip()
        elif linea.strip() == "---":
            continue
        elif linea.startswith("CORPO EMAIL:"):
            in_corpo = True
        elif in_corpo:
            corpo_linee.append(linea)

    componenti["corpo"] = "\n".join(corpo_linee).strip()

    return componenti


def invia_email_smtp(
    destinatario: str,
    oggetto: str,
    corpo: str,
    mittente_email: str,
    mittente_password: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587
) -> bool:
    """
    Invia un'email via SMTP (Gmail).

    Args:
        destinatario: Email del destinatario
        oggetto: Oggetto email
        corpo: Corpo del testo email
        mittente_email: Email del mittente
        mittente_password: Password app Gmail (NON la password account)
        smtp_server: Server SMTP (default: Gmail)
        smtp_port: Porta SMTP (default: 587 TLS)

    Returns:
        True se inviata con successo
    """
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = oggetto
        msg["From"] = mittente_email
        msg["To"] = destinatario

        # Versione testo plain
        parte_testo = MIMEText(corpo, "plain", "utf-8")
        msg.attach(parte_testo)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(mittente_email, mittente_password)
            server.sendmail(mittente_email, destinatario, msg.as_string())

        return True

    except smtplib.SMTPAuthenticationError:
        raise Exception("Autenticazione Gmail fallita. Usa una 'password per le app', non la password dell'account.")
    except smtplib.SMTPException as e:
        raise Exception(f"Errore SMTP: {e}")
    except Exception as e:
        raise Exception(f"Errore invio email: {e}")


def trova_riga_lead(sheets, id_lead: str) -> tuple:
    """
    Cerca il lead in tutti i tab e restituisce dati + posizione.

    Returns:
        Tupla (tab_nome, intestazioni, num_riga, riga) o (None, None, -1, None)
    """
    configurazioni = [
        ("Lead_NoSito", INTESTAZIONI_NO_SITO),
        ("Lead_FunnelScarso", INTESTAZIONI_FUNNEL_SCARSO)
    ]

    for tab_nome, intestazioni in configurazioni:
        riga, num_riga = sheets.trova_riga_per_id(tab_nome, id_lead)
        if riga:
            return tab_nome, intestazioni, num_riga, riga

    return None, None, -1, None


def main():
    parser = argparse.ArgumentParser(
        description="Invia email approvata a un lead specifico"
    )
    parser.add_argument("--id", required=True, help="ID del lead")
    parser.add_argument("--oggetto", help="Oggetto personalizzato (opzionale)")
    parser.add_argument("--anteprima", action="store_true", help="Mostra anteprima senza inviare")
    args = parser.parse_args()

    logger = get_logger("WF-EMAIL", f"invio_{args.id}")
    logger.info(f"START — Invio email per lead: {args.id}")

    # Leggi credenziali
    mittente_email = os.getenv("MITTENTE_EMAIL")
    mittente_password = os.getenv("MITTENTE_EMAIL_PASSWORD")

    if not mittente_email or not mittente_password:
        logger.error("ERRORE: MITTENTE_EMAIL o MITTENTE_EMAIL_PASSWORD non configurati nel .env")
        sys.exit(1)

    # Connetti Sheets
    sheets = crea_client_da_env()
    if not sheets:
        logger.error("Google Sheets non configurato")
        sys.exit(1)

    # Cerca lead
    tab_nome, intestazioni, num_riga, riga = trova_riga_lead(sheets, args.id)
    if not riga:
        logger.error(f"Lead non trovato: {args.id}")
        sys.exit(1)

    nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA", "?")
    email_dest = riga.get("EMAIL", "")

    if not email_dest:
        logger.error(f"Nessuna email per il lead {args.id}: {nome}")
        sys.exit(1)

    # Verifica stato
    stato_corrente = riga.get("STATO_OUTREACH", "")
    if stato_corrente == "inviato":
        logger.warning(f"Attenzione: {nome} è già stato contattato (stato: {stato_corrente})")
        conferma = input("Vuoi inviare comunque? (s/N): ").strip().lower()
        if conferma != "s":
            logger.info("Invio annullato dall'operatore")
            sys.exit(0)

    # Trova bozza
    percorso_bozza, testo_bozza = trova_bozza(args.id)
    if not testo_bozza:
        logger.error(f"Bozza non trovata per {args.id}. Genera prima con draft_emails.py")
        sys.exit(1)

    # Estrai componenti
    componenti = estrai_componenti_email(testo_bozza)
    oggetto = args.oggetto or componenti["oggetto_1"]
    corpo = componenti["corpo"]

    if not oggetto or not corpo:
        logger.error("Impossibile estrarre oggetto o corpo dalla bozza. Controlla il file bozza.")
        sys.exit(1)

    # Mostra anteprima
    print("\n" + "="*60)
    print(f"ANTEPRIMA EMAIL — {args.id}")
    print("="*60)
    print(f"A: {email_dest} ({nome})")
    print(f"Oggetto: {oggetto}")
    print("-"*60)
    print(corpo)
    print("="*60 + "\n")

    if args.anteprima:
        logger.info("Modalità anteprima — email non inviata")
        sys.exit(0)

    # Conferma prima dell'invio
    conferma = input("Inviare questa email? (s/N): ").strip().lower()
    if conferma != "s":
        logger.info("Invio annullato dall'operatore")
        sys.exit(0)

    # Invia
    logger.info(f"Invio email a {email_dest} ({nome})")
    try:
        invia_email_smtp(
            destinatario=email_dest,
            oggetto=oggetto,
            corpo=corpo,
            mittente_email=mittente_email,
            mittente_password=mittente_password
        )
        logger.info(f"Email inviata con successo a {email_dest}")

    except Exception as e:
        logger.error(f"Errore invio: {e}")
        sys.exit(1)

    # Aggiorna stato in Sheets
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_followup = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    storico = f"{timestamp}: nuovo → inviato"

    sheets.aggiorna_cella(tab_nome, num_riga, "STATO_OUTREACH", "inviato", intestazioni)
    sheets.aggiorna_cella(tab_nome, num_riga, "DATA_ULTIMO_CONTATTO", timestamp, intestazioni)
    sheets.aggiorna_cella(tab_nome, num_riga, "DATA_FOLLOWUP_SCHEDULATO", data_followup, intestazioni)
    sheets.aggiorna_cella(tab_nome, num_riga, "STORICO_STATI", storico, intestazioni)

    logger.info(f"END — Email inviata a {nome} ({email_dest}). Follow-up schedulato: {data_followup}")


if __name__ == "__main__":
    main()
