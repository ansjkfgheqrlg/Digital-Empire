"""
Process Apify Data — Digital Empire Agency
Scarica i dataset già presenti su Apify (senza costo) e li processa
attraverso le 3 pipeline (no-website, cro-funnel, ai-implementation).

Uso: python orchestrator/process_apify_data.py
"""

import csv
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Forza UTF-8 su Windows (evita charmap crash per caratteri non-latin)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, AGENCY_DIR)

from dotenv import load_dotenv
load_dotenv(os.path.join(AGENCY_DIR, ".env"))

import requests

OUTPUT_DIR = os.path.join(AGENCY_DIR, "output", "recovered")
LEADS_DIR = os.path.join(OUTPUT_DIR, "leads")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")
EMAILS_DIR = os.path.join(OUTPUT_DIR, "emails")

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
APIFY_BASE = "https://api.apify.com/v2"

# Run Apify validi: quelli che funzionano (verificati)
RUN_IDS = [
    "7jsmHZ2SaCEkZ9byh", "OwMvldnkLeWVikl8Z", "5qIYP8D71ru69DioG",
    "VHYAuGXtitMYrTcUf", "n7y5u2py9fHL8PypS",
    "QgLv50ssQf0aUPIII", "8IymQpALTEo5Dp2Ph", "bjV6zxlyvbLC9yTK1",
    "4CxJHev3cQWFxin4p",
]

# Limiti per pipeline (CRO ha market audit = 4 Claude call/lead)
MAX_NO_WEBSITE = 200
MAX_CRO = 40
MAX_AI = 200


# ---------------------------------------------------------------------------
# STEP 1: Scarica tutti i dataset Apify
# ---------------------------------------------------------------------------

def scarica_tutti_dataset() -> list[dict]:
    """Scarica e unifica tutti i business dai run Apify."""
    print(f"\n[PROCESS] Scarico {len(RUN_IDS)} dataset Apify...")
    tutti = []
    visti = set()

    for run_id in RUN_IDS:
        try:
            r = requests.get(f"{APIFY_BASE}/actor-runs/{run_id}?token={APIFY_TOKEN}", timeout=10)
            ds_id = r.json()["data"]["defaultDatasetId"]
            r2 = requests.get(
                f"{APIFY_BASE}/datasets/{ds_id}/items?token={APIFY_TOKEN}&format=json",
                timeout=60,
            )
            items = r2.json()
            nuovi = 0
            for item in items:
                key = str(item.get("title") or "") + "|" + str(item.get("address") or "")
                if key not in visti:
                    visti.add(key)
                    tutti.append(item)
                    nuovi += 1
            print(f"  Run {run_id}: {len(items)} items, {nuovi} nuovi (unici)")
        except Exception as e:
            print(f"  Run {run_id}: ERRORE — {e}")

    print(f"\n[PROCESS] Totale business unici: {len(tutti)}")
    return tutti


# ---------------------------------------------------------------------------
# STEP 2: Pipeline NO-WEBSITE
# ---------------------------------------------------------------------------

def processa_no_website(tutti: list[dict]) -> list[dict]:
    print(f"\n{'='*60}")
    print("[PROCESS] Pipeline NO-WEBSITE")
    print(f"{'='*60}")

    no_website_dir = os.path.join(AGENCY_DIR, "sub-agents", "no-website")
    sys.path.insert(0, no_website_dir)
    for mod in ["qualifier", "contact_finder", "message_generator"]:
        sys.modules.pop(mod, None)

    from qualifier import qualifica_leads
    from contact_finder import estrai_contatti_batch
    from message_generator import genera_messaggi_batch

    # Filtra: solo quelli senza sito web
    senza_sito = [b for b in tutti if not b.get("website")]
    print(f"[NO-WEBSITE] Business senza sito: {len(senza_sito)}")

    # Qualifica
    leads_qualificati = qualifica_leads(senza_sito)
    print(f"[NO-WEBSITE] Lead qualificati: {len(leads_qualificati)}")

    # Limita
    leads_qualificati = leads_qualificati[:MAX_NO_WEBSITE]

    # Contatti
    leads_con_email = estrai_contatti_batch(leads_qualificati)
    if not leads_con_email:
        print("[NO-WEBSITE] Nessun lead con email trovata.")
        return []

    print(f"[NO-WEBSITE] Lead con email: {len(leads_con_email)}")

    # Email
    leads_finali = genera_messaggi_batch(leads_con_email)

    # Salva
    data = datetime.now().strftime("%Y-%m-%d")
    csv_path = os.path.join(LEADS_DIR, f"{data}-no-website-leads.csv")
    bozze_path = os.path.join(EMAILS_DIR, f"{data}-no-website-bozze.txt")

    _salva_csv_no_website(leads_finali, csv_path)
    _salva_bozze_no_website(leads_finali, bozze_path)
    return leads_finali


def _salva_csv_no_website(leads, path):
    campi = ["title", "categoryName", "address", "phone", "email_trovata",
             "score", "fascia", "totalScore", "reviewsCount"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader(); w.writerows(leads)
    print(f"[NO-WEBSITE] CSV: {path} ({len(leads)} lead)")


def _salva_bozze_no_website(leads, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for i, lead in enumerate(leads, 1):
            f.write(f"{'='*60}\n")
            f.write(f"LEAD #{i} — {lead.get('title')} | Fascia {lead.get('fascia')} | Score {lead.get('score')}\n")
            f.write(f"Email: {lead.get('email_trovata')} | Tel: {lead.get('telefono_trovato', 'N/D')}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- EMAIL ---\n")
            f.write(lead.get("bozza_email", "Non generata") + "\n\n")
    print(f"[NO-WEBSITE] Bozze: {path}")


# ---------------------------------------------------------------------------
# STEP 3: Pipeline CRO-FUNNEL
# ---------------------------------------------------------------------------

def processa_cro(tutti: list[dict]) -> list[dict]:
    print(f"\n{'='*60}")
    print("[PROCESS] Pipeline CRO-FUNNEL")
    print(f"{'='*60}")

    cro_dir = os.path.join(AGENCY_DIR, "sub-agents", "cro-funnel")
    sys.path.insert(0, cro_dir)
    for mod in ["site_analyzer", "market_runner", "pdf_generator", "email_composer"]:
        sys.modules.pop(mod, None)

    from site_analyzer import filtra_lead_cro
    from market_runner import esegui_market_audit, compila_report_markdown
    from pdf_generator import genera_pdf
    from email_composer import componi_bozze_batch

    # Filtra: solo quelli CON sito web
    con_sito = [b for b in tutti if b.get("website") or b.get("url")]
    print(f"[CRO] Business con sito: {len(con_sito)}")

    # Analisi CRO score
    leads_qualificati = filtra_lead_cro(con_sito, soglia_score=60)
    print(f"[CRO] Lead con funnel scarso: {len(leads_qualificati)}")

    # Limita (ogni lead = 4 Claude calls)
    leads_qualificati = leads_qualificati[:MAX_CRO]
    print(f"[CRO] Processing (limitato a {MAX_CRO}): {len(leads_qualificati)}")

    # Market audit + PDF
    leads_con_pdf = []
    data = datetime.now().strftime("%Y-%m-%d")
    for lead in leads_qualificati:
        nome = lead.get("title", lead.get("url", "business"))
        lead_url = lead.get("website") or lead.get("url")
        print(f"\n[CRO] Audit: {nome}")

        audit_results = esegui_market_audit(lead_url, nome)
        lead["audit_results"] = audit_results

        report_md = compila_report_markdown(lead, audit_results)

        nome_file = re.sub(r"[^\w\-]", "_", nome)[:40]
        pdf_path = os.path.join(REPORTS_DIR, f"{data}-{nome_file}-report.pdf")
        genera_pdf(report_md, pdf_path)
        lead["pdf_path"] = pdf_path
        leads_con_pdf.append(lead)

    # Email
    leads_finali = componi_bozze_batch(leads_con_pdf)

    # Salva
    csv_path = os.path.join(LEADS_DIR, f"{data}-cro-funnel-leads.csv")
    bozze_path = os.path.join(EMAILS_DIR, f"{data}-cro-funnel-bozze.txt")

    _salva_csv_cro(leads_finali, csv_path)
    _salva_bozze_cro(leads_finali, bozze_path)
    return leads_finali


def _salva_csv_cro(leads, path):
    campi = ["title", "website", "address", "phone", "email_trovata",
             "score_funnel", "tempo_caricamento", "ha_cta", "ha_form_contatto",
             "ha_social_proof", "pdf_path"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader(); w.writerows(leads)
    print(f"[CRO] CSV: {path} ({len(leads)} lead)")


def _salva_bozze_cro(leads, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for i, lead in enumerate(leads, 1):
            f.write(f"{'='*60}\n")
            f.write(f"LEAD #{i} — {lead.get('title')} | Score funnel: {lead.get('score_funnel')}/100\n")
            f.write(f"Sito: {lead.get('website') or lead.get('url')}\n")
            f.write(f"PDF: {lead.get('pdf_path', 'Non generato')}\n")
            f.write(f"Problemi: {', '.join(lead.get('problemi', []))}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- EMAIL (con PDF allegato) ---\n")
            f.write(lead.get("bozza_email", "Non generata") + "\n\n")
    print(f"[CRO] Bozze: {path}")


# ---------------------------------------------------------------------------
# STEP 4: Pipeline AI-IMPLEMENTATION
# ---------------------------------------------------------------------------

def processa_ai(tutti: list[dict]) -> list[dict]:
    print(f"\n{'='*60}")
    print("[PROCESS] Pipeline AI-IMPLEMENTATION")
    print(f"{'='*60}")

    ai_dir = os.path.join(AGENCY_DIR, "sub-agents", "ai-implementation")
    nw_dir = os.path.join(AGENCY_DIR, "sub-agents", "no-website")
    sys.path.insert(0, ai_dir)
    sys.path.insert(0, nw_dir)
    for mod in ["ai_scorer", "proposal_generator", "contact_finder"]:
        sys.modules.pop(mod, None)

    from ai_scorer import filtra_leads_ai
    from proposal_generator import genera_proposte_batch
    from contact_finder import estrai_contatti_batch

    # Scoring AI
    leads_qualificati = filtra_leads_ai(tutti, soglia=40)
    print(f"[AI] Lead qualificati: {len(leads_qualificati)}")
    leads_qualificati = leads_qualificati[:MAX_AI]

    # Contatti
    leads_con_email = estrai_contatti_batch(leads_qualificati)
    if not leads_con_email:
        print("[AI] Nessun lead con email trovata.")
        return []

    print(f"[AI] Lead con email: {len(leads_con_email)}")

    # Email
    leads_finali = genera_proposte_batch(leads_con_email)

    # Salva
    data = datetime.now().strftime("%Y-%m-%d")
    csv_path = os.path.join(LEADS_DIR, f"{data}-ai-implementation-leads.csv")
    bozze_path = os.path.join(EMAILS_DIR, f"{data}-ai-implementation-bozze.txt")

    _salva_csv_ai(leads_finali, csv_path)
    _salva_bozze_ai(leads_finali, bozze_path)
    return leads_finali


def _salva_csv_ai(leads, path):
    campi = ["title", "categoryName", "address", "phone", "email_trovata",
             "ai_score", "ai_soluzione", "totalScore", "reviewsCount", "website"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        w.writeheader(); w.writerows(leads)
    print(f"[AI] CSV: {path} ({len(leads)} lead)")


def _salva_bozze_ai(leads, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for i, lead in enumerate(leads, 1):
            f.write(f"{'='*60}\n")
            f.write(f"LEAD #{i} — {lead.get('title')} | AI Score: {lead.get('ai_score')}/100\n")
            f.write(f"Settore: {lead.get('categoryName') or lead.get('settore_cercato')}\n")
            f.write(f"Soluzione AI: {lead.get('ai_soluzione')}\n")
            f.write(f"Email: {lead.get('email_trovata')} | Tel: {lead.get('telefono_trovato', 'N/D')}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- EMAIL PROPOSTA AI ---\n")
            f.write(lead.get("bozza_email", "Non generata") + "\n\n")
    print(f"[AI] Bozze: {path}")


# ---------------------------------------------------------------------------
# STEP 5: Invio batch automatico
# ---------------------------------------------------------------------------

def invia_batch_automatico():
    """Chiama batch_send.py in modalità automatica (nessuna conferma interattiva)."""
    import smtplib
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mittente = os.getenv("GMAIL_USER") or os.getenv("MITTENTE_EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD") or os.getenv("MITTENTE_EMAIL_PASSWORD")

    if not mittente or not password:
        print("\n[BATCH-SEND] ERRORE: credenziali Gmail mancanti nel .env")
        return

    # Importa parser batch_send
    batch_send_dir = os.path.join(AGENCY_DIR, "orchestrator")
    sys.path.insert(0, batch_send_dir)
    sys.modules.pop("batch_send", None)
    from batch_send import parse_bozze, leggi_csv_leads, trova_bozze_path, invia_email, salva_log

    # Scansiona output/recovered/
    tutti_csv = sorted(Path(OUTPUT_DIR).rglob("*-leads.csv"))
    print(f"\n[BATCH-SEND] CSV trovati: {len(tutti_csv)}")

    da_inviare = []
    for csv_path in tutti_csv:
        tipo = ("cro" if "cro-funnel" in csv_path.name else
                "no-website" if "no-website" in csv_path.name else "ai")
        leads = leggi_csv_leads(str(csv_path))
        bozze_path = trova_bozze_path(str(csv_path))
        if not bozze_path:
            print(f"[BATCH-SEND] Bozze non trovate per: {csv_path.name}")
            continue
        bozze = parse_bozze(bozze_path)

        for lead in leads:
            title = lead.get("title", "").strip()
            email_dest = lead.get("email_trovata", "").strip()
            pdf_path = lead.get("pdf_path", "").strip() if tipo == "cro" else None

            if not email_dest or "@" not in email_dest:
                continue
            if title not in bozze:
                continue

            bozza = bozze[title]
            if not bozza["oggetto"] or not bozza["corpo"]:
                continue

            da_inviare.append({
                "tipo": tipo, "title": title, "email": email_dest,
                "oggetto": bozza["oggetto"], "corpo": bozza["corpo"],
                "pdf_path": pdf_path if pdf_path and os.path.exists(pdf_path or "") else None,
            })

    if not da_inviare:
        print("[BATCH-SEND] Nessuna email pronta per l'invio.")
        return

    cro_c = sum(1 for x in da_inviare if x["tipo"] == "cro")
    nw_c = sum(1 for x in da_inviare if x["tipo"] == "no-website")
    ai_c = sum(1 for x in da_inviare if x["tipo"] == "ai")
    pdf_c = sum(1 for x in da_inviare if x["pdf_path"])

    print(f"\n{'='*60}")
    print(f"[BATCH-SEND] Email da inviare: {len(da_inviare)}")
    print(f"  No-Website: {nw_c} | CRO: {cro_c} (PDF: {pdf_c}) | AI: {ai_c}")
    print(f"  Mittente: {mittente}")
    print(f"{'='*60}")

    log_records = []
    inviati = 0
    errori = 0
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i, item in enumerate(da_inviare, 1):
        ha_pdf = bool(item["pdf_path"])
        stato = "ok"
        errore_msg = ""
        try:
            invia_email(
                mittente=mittente, password=password,
                destinatario=item["email"], oggetto=item["oggetto"],
                corpo=item["corpo"], pdf_path=item["pdf_path"],
            )
            pdf_lbl = " [+PDF]" if ha_pdf else ""
            print(f"  [{i}/{len(da_inviare)}] OK {item['email']} — {item['title'][:35]}{pdf_lbl}")
            inviati += 1
        except Exception as e:
            errore_msg = str(e)
            print(f"  [{i}/{len(da_inviare)}] ERR {item['email']}: {errore_msg}")
            stato = "errore"
            errori += 1

        log_records.append({
            "timestamp": ts, "tipo": item["tipo"], "title": item["title"],
            "email": item["email"], "oggetto": item["oggetto"][:80],
            "ha_pdf": "si" if ha_pdf else "no", "stato": stato, "errore": errore_msg,
        })

    salva_log(log_records)
    print(f"\n{'='*60}")
    print(f"[BATCH-SEND] INVIO COMPLETATO")
    print(f"  Inviate: {inviati} | Errori: {errori}")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    for d in [LEADS_DIR, REPORTS_DIR, EMAILS_DIR]:
        os.makedirs(d, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*60}")
    print(f"[PROCESS] START — {ts}")
    print(f"[PROCESS] Output in: {OUTPUT_DIR}")
    print(f"{'='*60}")

    # Download tutti i dataset Apify (gratis — già pagati)
    tutti = scarica_tutti_dataset()

    if not tutti:
        print("[PROCESS] Nessun dato disponibile. Uscita.")
        return

    # Pipeline no-website
    leads_nw = processa_no_website(tutti)

    # Pipeline CRO (con market audit + PDF)
    leads_cro = processa_cro(tutti)

    # Pipeline AI
    leads_ai = processa_ai(tutti)

    totale = len(leads_nw) + len(leads_cro) + len(leads_ai)
    print(f"\n{'='*60}")
    print(f"[PROCESS] ELABORAZIONE COMPLETATA")
    print(f"  No-Website: {len(leads_nw)} lead")
    print(f"  CRO-Funnel: {len(leads_cro)} lead (con PDF report)")
    print(f"  AI-Impl:    {len(leads_ai)} lead")
    print(f"  TOTALE:     {totale} lead")
    print(f"{'='*60}")

    # Invio email automatico
    print("\n[PROCESS] Avvio invio email...")
    invia_batch_automatico()

    print("\n[PROCESS] WORKFLOW COMPLETATO.")


if __name__ == "__main__":
    main()
