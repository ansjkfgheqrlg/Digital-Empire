"""
Pipeline — Sub-agent No-Website
Coordina scraping → qualifica → contatti → messaggi → output.
"""

import os
import csv
from datetime import datetime

from scraper import avvia_scraping_google_maps
from qualifier import qualifica_leads
from contact_finder import estrai_contatti_batch
from message_generator import genera_messaggi_batch


def esegui_pipeline(citta: str, settore: str, output_dir: str):
    """Pipeline completa no-website."""
    data = datetime.now().strftime("%Y-%m-%d")
    leads_dir = os.path.join(output_dir, "leads")
    emails_dir = os.path.join(output_dir, "emails")
    os.makedirs(leads_dir, exist_ok=True)
    os.makedirs(emails_dir, exist_ok=True)

    # Step 1: Scraping
    business_list = avvia_scraping_google_maps(citta, settore)
    if not business_list:
        print("[NO-WEBSITE] Nessun business trovato. Pipeline terminata.")
        return

    # Step 2: Qualifica
    leads_qualificati = qualifica_leads(business_list)

    # Step 3: Estrai contatti (e filtra chi ha email)
    leads_con_contatti = estrai_contatti_batch(leads_qualificati)
    if not leads_con_contatti:
        print("[NO-WEBSITE] Nessun lead con email trovata. Pipeline terminata.")
        return

    # Step 4: Genera messaggi
    leads_con_messaggi = genera_messaggi_batch(leads_con_contatti)

    # Step 5: Salva CSV lead
    csv_path = os.path.join(leads_dir, f"{data}-no-website-leads.csv")
    _salva_csv(leads_con_messaggi, csv_path)

    # Step 6: Salva bozze email
    bozze_path = os.path.join(emails_dir, f"{data}-no-website-bozze.txt")
    _salva_bozze(leads_con_messaggi, bozze_path)

    print(f"\n[NO-WEBSITE] Pipeline completata!")
    print(f"  Lead salvati: {csv_path}")
    print(f"  Bozze email: {bozze_path}")


def _salva_csv(leads: list[dict], path: str):
    campi = ["title", "categoryName", "address", "phone", "email_trovata",
             "score", "fascia", "totalScore", "reviewsCount"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campi, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)
    print(f"[NO-WEBSITE] CSV salvato: {path} ({len(leads)} lead)")


def _salva_bozze(leads: list[dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        for i, lead in enumerate(leads, 1):
            f.write(f"{'='*60}\n")
            f.write(f"LEAD #{i} — {lead.get('title')} | Fascia {lead.get('fascia')} | Score {lead.get('score')}\n")
            f.write(f"Email: {lead.get('email_trovata')} | Tel: {lead.get('telefono_trovato', 'N/D')}\n")
            f.write(f"{'='*60}\n\n")
            f.write("--- EMAIL ---\n")
            f.write(lead.get("bozza_email", "Non generata") + "\n\n")
            if lead.get("bozza_sms"):
                f.write("--- SMS ---\n")
                f.write(lead.get("bozza_sms") + "\n\n")
    print(f"[NO-WEBSITE] Bozze salvate: {path}")
