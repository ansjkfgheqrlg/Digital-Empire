"""
Pipeline — Sub-agent CRO-Funnel
Coordina: scraping → analisi → market audit → PDF → email → output.
"""

import os
import csv
import re
from datetime import datetime

from scraper import trova_siti_google_maps
from site_analyzer import filtra_lead_cro
from market_runner import esegui_market_audit, compila_report_markdown
from pdf_generator import genera_pdf
from email_composer import componi_bozze_batch


def esegui_pipeline(output_dir: str, url: str = None, citta: str = None, settore: str = None):
    """
    Pipeline completa CRO-Funnel.
    Modalità 1 (url): analizza un singolo sito
    Modalità 2 (citta + settore): trova e analizza più siti
    """
    data = datetime.now().strftime("%Y-%m-%d")
    leads_dir = os.path.join(output_dir, "leads")
    reports_dir = os.path.join(output_dir, "reports")
    emails_dir = os.path.join(output_dir, "emails")
    for d in [leads_dir, reports_dir, emails_dir]:
        os.makedirs(d, exist_ok=True)

    # Step 1: Ottieni lista siti
    if url:
        # Singolo sito — analisi diretta
        lista_business = [{"website": url, "title": url, "url": url}]
    else:
        lista_business = trova_siti_google_maps(citta, settore)

    if not lista_business:
        print("[CRO-FUNNEL] Nessun business trovato.")
        return

    # Step 2: Analisi CRO e filtraggio (score funnel <= 60)
    leads_qualificati = filtra_lead_cro(lista_business, soglia_score=60)

    if not leads_qualificati:
        print("[CRO-FUNNEL] Nessun lead qualificato (tutti hanno funnel ok).")
        return

    # Step 3 + 4: Market audit + PDF per ogni lead
    leads_con_pdf = []
    for lead in leads_qualificati:
        nome = lead.get("title", lead.get("url", "business"))
        lead_url = lead.get("website") or lead.get("url")
        print(f"\n[CRO-FUNNEL] Elaboro: {nome}")

        # Market audit
        audit_results = esegui_market_audit(lead_url, nome)
        lead["audit_results"] = audit_results

        # Compila Markdown
        report_md = compila_report_markdown(lead, audit_results)

        # Genera PDF
        nome_file = re.sub(r"[^\w\-]", "_", nome)[:40]
        pdf_path = os.path.join(reports_dir, f"{data}-{nome_file}-report.pdf")
        genera_pdf(report_md, pdf_path)
        lead["pdf_path"] = pdf_path
        leads_con_pdf.append(lead)

    # Step 5: Genera bozze email
    leads_finali = componi_bozze_batch(leads_con_pdf)

    # Step 6: Salva output
    csv_path = os.path.join(leads_dir, f"{data}-cro-funnel-leads.csv")
    _salva_csv(leads_finali, csv_path)

    bozze_path = os.path.join(emails_dir, f"{data}-cro-funnel-bozze.txt")
    _salva_bozze(leads_finali, bozze_path)

    print(f"\n[CRO-FUNNEL] Pipeline completata!")
    print(f"  Lead: {csv_path}")
    print(f"  PDF report: {reports_dir}")
    print(f"  Bozze email: {bozze_path}")


def _salva_csv(leads: list[dict], path: str):
    campi = ["title", "website", "address", "phone", "email_trovata",
             "score_funnel", "tempo_caricamento", "ha_cta",
             "ha_form_contatto", "ha_social_proof", "pdf_path"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)
    print(f"[CRO-FUNNEL] CSV salvato: {path}")


def _salva_bozze(leads: list[dict], path: str):
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
    print(f"[CRO-FUNNEL] Bozze salvate: {path}")
