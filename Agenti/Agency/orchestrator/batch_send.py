"""
Batch Send — Digital Empire Agency
Invia tutte le email generate dalle pipeline. Per i lead CRO allega il PDF report.

Funzionamento:
    1. Scansiona output/ ricorsivamente per tutti i file *-leads.csv
    2. Per ogni CSV trova il corrispondente *-bozze.txt (stessa cartella, stessa data/tipo)
    3. Fa il match tra lead (email_trovata, pdf_path) e bozza (oggetto, corpo)
    4. Invia via Gmail SMTP — per lead CRO con PDF: allega il PDF report
    5. Salva log in output/invio_log.csv

Uso:
    python orchestrator/batch_send.py               # Richiede conferma batch prima di inviare
    python orchestrator/batch_send.py --anteprima   # Solo anteprima, non invia
    python orchestrator/batch_send.py --limite 50   # Invia max N email

IMPORTANTE: Una singola conferma viene chiesta prima di avviare l'invio massivo.
"""

import argparse
import csv
import os
import re
import smtplib
import sys
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(AGENCY_DIR, "output")

load_dotenv(os.path.join(AGENCY_DIR, ".env"))


# ---------------------------------------------------------------------------
# PARSING BOZZE
# ---------------------------------------------------------------------------

def parse_bozze(bozze_path: str) -> dict:
    """
    Legge un file bozze .txt e ritorna un dict: title -> {oggetto, corpo}.
    Supporta i formati di tutti e 3 i sub-agent.
    """
    with open(bozze_path, "r", encoding="utf-8") as f:
        content = f.read()

    SEP = "=" * 60
    risultati = {}

    # Split per separatore. Produce chunk alternati: [header, email_section, header, ...]
    raw_chunks = re.split(r"={60}\n?", content)
    chunks = [c.strip() for c in raw_chunks if c.strip()]

    i = 0
    while i < len(chunks):
        chunk = chunks[i]

        # Blocco header: inizia con LEAD #N
        title_match = re.search(r"LEAD #\d+ — (.+?) \|", chunk)
        if title_match:
            title = title_match.group(1).strip()

            # Il blocco email è il chunk successivo
            if i + 1 < len(chunks):
                email_section = chunks[i + 1]

                # Rimuovi marker tipo "--- EMAIL ... ---"
                email_section = re.sub(r"---[^-\n]+---\n?", "", email_section).strip()

                # Estrai OGGETTO
                obj_match = re.search(r"OGGETTO:\s*(.+)", email_section)
                oggetto = obj_match.group(1).strip() if obj_match else ""

                # Estrai CORPO: tutto dopo la riga OGGETTO
                if obj_match:
                    corpo_start = email_section.find(obj_match.group(0)) + len(obj_match.group(0))
                    corpo = email_section[corpo_start:].strip()
                else:
                    corpo = email_section

                risultati[title] = {"oggetto": oggetto, "corpo": corpo}
                i += 2  # Salta sia il header che l'email section
                continue

        i += 1

    return risultati


# ---------------------------------------------------------------------------
# LETTURA CSV
# ---------------------------------------------------------------------------

def leggi_csv_leads(csv_path: str) -> list[dict]:
    """Legge un CSV lead e ritorna lista di dict."""
    leads = []
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads.append(dict(row))
    except Exception as e:
        print(f"[BATCH-SEND] ERRORE lettura CSV {csv_path}: {e}")
    return leads


def trova_bozze_path(csv_path: str) -> str | None:
    """Dato un CSV *-leads.csv, trova il corrispondente *-bozze.txt nella stessa cartella."""
    p = Path(csv_path)
    # output/run_01_.../leads/2024-03-09-no-website-leads.csv
    # → output/run_01_.../emails/2024-03-09-no-website-bozze.txt
    nome_bozze = p.name.replace("-leads.csv", "-bozze.txt")
    emails_dir = p.parent.parent / "emails"
    bozze_path = emails_dir / nome_bozze
    if bozze_path.exists():
        return str(bozze_path)
    return None


# ---------------------------------------------------------------------------
# INVIO EMAIL
# ---------------------------------------------------------------------------

def invia_email(
    mittente: str,
    password: str,
    destinatario: str,
    oggetto: str,
    corpo: str,
    pdf_path: str | None = None,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587,
) -> bool:
    """Invia email via Gmail SMTP. Se pdf_path è fornito, lo allega."""
    msg = MIMEMultipart()
    msg["Subject"] = oggetto
    msg["From"] = mittente
    msg["To"] = destinatario

    msg.attach(MIMEText(corpo, "plain", "utf-8"))

    # Allega PDF se presente (per lead CRO)
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            allegato = MIMEApplication(f.read(), _subtype="pdf")
            nome_file = os.path.basename(pdf_path)
            allegato.add_header("Content-Disposition", "attachment", filename=nome_file)
            msg.attach(allegato)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(mittente, password)
        server.sendmail(mittente, destinatario, msg.as_string())

    return True


# ---------------------------------------------------------------------------
# LOG INVII
# ---------------------------------------------------------------------------

def salva_log(log_records: list[dict]):
    """Salva il log degli invii in output/invio_log.csv."""
    log_path = os.path.join(OUTPUT_DIR, "invio_log.csv")
    campi = ["timestamp", "tipo", "title", "email", "oggetto", "ha_pdf", "stato", "errore"]
    file_esiste = os.path.exists(log_path)
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        if not file_esiste:
            writer.writeheader()
        writer.writerows(log_records)
    print(f"\n[BATCH-SEND] Log invii salvato: {log_path}")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch email sender — Digital Empire Agency")
    parser.add_argument("--anteprima", action="store_true", help="Mostra anteprima senza inviare")
    parser.add_argument("--limite", type=int, default=0,
                        help="Limita invio a N email (0 = nessun limite)")
    args = parser.parse_args()

    # Credenziali Gmail
    mittente = os.getenv("GMAIL_USER") or os.getenv("MITTENTE_EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("MITTENTE_EMAIL_PASSWORD")

    if not args.anteprima and (not mittente or not password):
        print("[BATCH-SEND] ERRORE: GMAIL_USER e GMAIL_APP_PASSWORD mancanti nel .env")
        sys.exit(1)

    # Scansiona tutti i CSV in output/
    tutti_csv = sorted(Path(OUTPUT_DIR).rglob("*-leads.csv"))
    print(f"\n[BATCH-SEND] Trovati {len(tutti_csv)} file CSV in output/")

    # Raccogli tutti i lead con email + bozza
    da_inviare = []

    for csv_path in tutti_csv:
        tipo = "cro" if "cro-funnel" in csv_path.name else \
               "no-website" if "no-website" in csv_path.name else "ai"

        leads = leggi_csv_leads(str(csv_path))
        bozze_path = trova_bozze_path(str(csv_path))

        if not bozze_path:
            print(f"[BATCH-SEND] Bozze non trovate per: {csv_path.name} — SKIP")
            continue

        bozze = parse_bozze(bozze_path)

        for lead in leads:
            title = lead.get("title", "").strip()
            email_dest = lead.get("email_trovata", "").strip()
            pdf_path = lead.get("pdf_path", "").strip() if tipo == "cro" else None

            if not email_dest or "@" not in email_dest:
                continue

            if title not in bozze:
                print(f"[BATCH-SEND] Bozza non trovata per: {title!r} — SKIP")
                continue

            bozza = bozze[title]
            oggetto = bozza["oggetto"]
            corpo = bozza["corpo"]

            if not oggetto or not corpo:
                print(f"[BATCH-SEND] Email vuota per: {title!r} — SKIP")
                continue

            da_inviare.append({
                "tipo": tipo,
                "title": title,
                "email": email_dest,
                "oggetto": oggetto,
                "corpo": corpo,
                "pdf_path": pdf_path if pdf_path and os.path.exists(pdf_path or "") else None,
            })

    if not da_inviare:
        print("[BATCH-SEND] Nessun lead pronto per l'invio. Esegui prima run_500.py.")
        sys.exit(0)

    # Applica limite
    if args.limite > 0:
        da_inviare = da_inviare[: args.limite]

    # Anteprima
    print(f"\n{'='*60}")
    print(f"[BATCH-SEND] Riepilogo email da inviare: {len(da_inviare)}")
    cro_count = sum(1 for x in da_inviare if x["tipo"] == "cro")
    nw_count = sum(1 for x in da_inviare if x["tipo"] == "no-website")
    ai_count = sum(1 for x in da_inviare if x["tipo"] == "ai")
    pdf_count = sum(1 for x in da_inviare if x["pdf_path"])
    print(f"  No-Website:        {nw_count}")
    print(f"  CRO-Funnel:        {cro_count} (di cui con PDF: {pdf_count})")
    print(f"  AI-Implementation: {ai_count}")
    print(f"{'='*60}")

    # Mostra prime 5 email come anteprima
    print("\nPRIMA ANTEPRIMA (prime 5 email):")
    for item in da_inviare[:5]:
        pdf_label = f" [+PDF: {os.path.basename(item['pdf_path'])}]" if item["pdf_path"] else ""
        print(f"  • [{item['tipo'].upper()}] {item['email']} | {item['oggetto'][:60]}{pdf_label}")

    if args.anteprima:
        print("\n[BATCH-SEND] Modalità ANTEPRIMA — nessuna email inviata.")
        sys.exit(0)

    # Conferma unica prima dell'invio massivo
    print(f"\nATTENZIONE: Stai per inviare {len(da_inviare)} email da {mittente}")
    risposta = input("Confermi l'invio? (scrivi 'SI' per procedere): ").strip()
    if risposta.upper() != "SI":
        print("[BATCH-SEND] Invio annullato.")
        sys.exit(0)

    # Invio
    log_records = []
    inviati = 0
    errori = 0
    timestamp_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[BATCH-SEND] Avvio invio — {len(da_inviare)} email...")

    for i, item in enumerate(da_inviare, start=1):
        ha_pdf = bool(item["pdf_path"])
        stato = "ok"
        errore_msg = ""

        try:
            invia_email(
                mittente=mittente,
                password=password,
                destinatario=item["email"],
                oggetto=item["oggetto"],
                corpo=item["corpo"],
                pdf_path=item["pdf_path"],
            )
            pdf_label = " [+PDF]" if ha_pdf else ""
            print(f"  [{i}/{len(da_inviare)}] ✓ {item['email']} — {item['title'][:40]}{pdf_label}")
            inviati += 1
        except Exception as e:
            errore_msg = str(e)
            print(f"  [{i}/{len(da_inviare)}] ✗ ERRORE {item['email']}: {errore_msg}")
            stato = "errore"
            errori += 1

        log_records.append({
            "timestamp": timestamp_run,
            "tipo": item["tipo"],
            "title": item["title"],
            "email": item["email"],
            "oggetto": item["oggetto"][:80],
            "ha_pdf": "si" if ha_pdf else "no",
            "stato": stato,
            "errore": errore_msg,
        })

    # Salva log
    salva_log(log_records)

    print(f"\n{'='*60}")
    print(f"[BATCH-SEND] COMPLETATO")
    print(f"  Email inviate con successo: {inviati}")
    print(f"  Errori:                     {errori}")
    print(f"  Log: {os.path.join(OUTPUT_DIR, 'invio_log.csv')}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
