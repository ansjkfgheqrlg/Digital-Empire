"""
Pipeline — Sub-agent AI-Implementation
Coordina: scraping → scoring AI → proposta → email → output.
"""

import os
import csv
from datetime import datetime

from scraper import trova_business_multi_settore, trova_business_settore
from ai_scorer import filtra_leads_ai
from proposal_generator import genera_proposte_batch

# Importa contact finder dall'outreach esistente per estrarre email
import sys
AGENCY_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(AGENCY_DIR, "sub-agents", "no-website"))
from contact_finder import estrai_contatti_batch


def esegui_pipeline(citta: str, settore: str = None, output_dir: str = None):
    """
    Pipeline completa AI-Implementation.
    Se settore specificato: cerca solo quel settore.
    Altrimenti: cerca tutti i settori AI-ready.
    """
    data = datetime.now().strftime("%Y-%m-%d")
    leads_dir = os.path.join(output_dir, "leads")
    emails_dir = os.path.join(output_dir, "emails")
    os.makedirs(leads_dir, exist_ok=True)
    os.makedirs(emails_dir, exist_ok=True)

    # Step 1: Scraping
    if settore:
        lista_business = trova_business_settore(citta, settore)
    else:
        lista_business = trova_business_multi_settore(citta)

    if not lista_business:
        print("[AI-IMPL] Nessun business trovato.")
        return

    # Step 2: Scoring AI e filtraggio (score >= 40)
    leads_qualificati = filtra_leads_ai(lista_business, soglia=40)

    if not leads_qualificati:
        print("[AI-IMPL] Nessun lead qualificato per AI.")
        return

    # Step 3: Estrai contatti (tieni solo chi ha email)
    leads_con_contatti = estrai_contatti_batch(leads_qualificati)

    if not leads_con_contatti:
        print("[AI-IMPL] Nessun lead con email valida trovata.")
        return

    # Step 4: Genera proposte AI personalizzate
    leads_finali = genera_proposte_batch(leads_con_contatti)

    # Step 5: Salva output
    csv_path = os.path.join(leads_dir, f"{data}-ai-implementation-leads.csv")
    _salva_csv(leads_finali, csv_path)

    bozze_path = os.path.join(emails_dir, f"{data}-ai-implementation-bozze.txt")
    _salva_bozze(leads_finali, bozze_path)

    print(f"\n[AI-IMPL] Pipeline completata!")
    print(f"  Lead: {csv_path}")
    print(f"  Bozze: {bozze_path}")


def _salva_csv(leads: list[dict], path: str):
    campi = ["title", "categoryName", "address", "phone", "email_trovata",
             "ai_score", "ai_soluzione", "totalScore", "reviewsCount", "website"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)
    print(f"[AI-IMPL] CSV salvato: {path} ({len(leads)} lead)")


def _salva_bozze(leads: list[dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        for i, lead in enumerate(leads, 1):
            f.write(f"{'='*60}\n")
            f.write(f"LEAD #{i} — {lead.get('title')} | AI Score: {lead.get('ai_score')}/100\n")
            f.write(f"Settore: {lead.get('categoryName') or lead.get('settore_cercato')}\n")
            f.write(f"Soluzione AI: {lead.get('ai_soluzione')}\n")
            f.write(f"Email: {lead.get('email_trovata')} | Tel: {lead.get('telefono_trovato', 'N/D')}\n")
            segnali = lead.get("ai_segnali", [])
            f.write(f"Segnali: {', '.join(segnali[:3])}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- EMAIL PROPOSTA AI ---\n")
            f.write(lead.get("bozza_email", "Non generata") + "\n\n")
    print(f"[AI-IMPL] Bozze salvate: {path}")
