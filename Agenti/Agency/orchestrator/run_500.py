"""
Run 500 — Digital Empire Agency
Runner multi-città/settore per raccogliere 500 lead totali su tutte e 3 le pipeline.

Uso:
    python orchestrator/run_500.py
    python orchestrator/run_500.py --target 200   # obiettivo personalizzato

Strategia:
    - Itera su combinazioni città/settore predefinite
    - Per ogni combinazione esegue le 3 pipeline (no-website, cro-funnel, ai-implementation)
    - Usa una sottocartella output/run_XX/ per ogni combinazione (evita sovrascritture)
    - Si ferma quando il totale lead nei CSV raggiunge TARGET_LEAD
"""

import argparse
import csv
import os
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, AGENCY_DIR)

# Carica .env PRIMA di qualsiasi import di pipeline (i moduli leggono os.getenv al caricamento)
from dotenv import load_dotenv
load_dotenv(os.path.join(AGENCY_DIR, ".env"))

OUTPUT_DIR = os.path.join(AGENCY_DIR, "output")

TARGET_LEAD_DEFAULT = 500

# Combinazioni città/settore da iterare (variegato e sparso come richiesto)
COMBINAZIONI = [
    ("Milano", "ristoranti"),
    ("Roma", "dentisti"),
    ("Napoli", "avvocati"),
    ("Torino", "palestre"),
    ("Bologna", "hotel"),
    ("Firenze", "parrucchieri"),
    ("Palermo", "fisioterapisti"),
    ("Bari", "agenzie immobiliari"),
    ("Venezia", "estetiste"),
    ("Catania", "meccanici"),
    ("Genova", "ristoranti"),
    ("Verona", "dentisti"),
    ("Modena", "palestre"),
    ("Bergamo", "avvocati"),
    ("Brescia", "hotel"),
    ("Padova", "agenzie immobiliari"),
    ("Taranto", "parrucchieri"),
    ("Reggio Calabria", "ristoranti"),
    ("Parma", "fisioterapisti"),
    ("Messina", "estetiste"),
]


def conta_lead_csv(directory: str) -> int:
    """Conta il totale di righe (lead) in tutti i CSV dentro una directory."""
    totale = 0
    for csv_path in Path(directory).rglob("*-leads.csv"):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                righe = sum(1 for row in reader) - 1  # -1 per intestazione
                totale += max(0, righe)
        except Exception:
            pass
    return totale


def esegui_no_website(citta: str, settore: str, run_output_dir: str):
    sub_dir = os.path.join(AGENCY_DIR, "sub-agents", "no-website")
    if sub_dir not in sys.path:
        sys.path.insert(0, sub_dir)
    # Rimuovi cache modulo precedente per evitare conflitti tra run
    for mod in ["pipeline", "scraper", "qualifier", "contact_finder", "message_generator"]:
        sys.modules.pop(mod, None)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(citta=citta, settore=settore, output_dir=run_output_dir)


def esegui_cro_funnel(citta: str, settore: str, run_output_dir: str):
    sub_dir = os.path.join(AGENCY_DIR, "sub-agents", "cro-funnel")
    if sub_dir not in sys.path:
        sys.path.insert(0, sub_dir)
    for mod in ["pipeline", "scraper", "site_analyzer", "market_runner", "pdf_generator", "email_composer"]:
        sys.modules.pop(mod, None)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(citta=citta, settore=settore, output_dir=run_output_dir)


def esegui_ai_implementation(citta: str, settore: str, run_output_dir: str):
    sub_dir = os.path.join(AGENCY_DIR, "sub-agents", "ai-implementation")
    if sub_dir not in sys.path:
        sys.path.insert(0, sub_dir)
    for mod in ["pipeline", "scraper", "ai_scorer", "proposal_generator"]:
        sys.modules.pop(mod, None)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(citta=citta, settore=settore, output_dir=run_output_dir)


def main():
    parser = argparse.ArgumentParser(description="Runner 500 lead — Digital Empire Agency")
    parser.add_argument("--target", type=int, default=TARGET_LEAD_DEFAULT,
                        help=f"Numero obiettivo di lead (default: {TARGET_LEAD_DEFAULT})")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*60}")
    print(f"[RUN-500] START — {timestamp}")
    print(f"[RUN-500] Obiettivo: {args.target} lead totali")
    print(f"[RUN-500] Combinazioni disponibili: {len(COMBINAZIONI)}")
    print(f"{'='*60}\n")

    totale_lead = conta_lead_csv(OUTPUT_DIR)
    print(f"[RUN-500] Lead già presenti in output/: {totale_lead}")

    for i, (citta, settore) in enumerate(COMBINAZIONI, start=1):
        if totale_lead >= args.target:
            print(f"\n[RUN-500] Obiettivo raggiunto! {totale_lead} lead totali. Stop.")
            break

        print(f"\n{'='*60}")
        print(f"[RUN-500] Combo {i}/{len(COMBINAZIONI)}: {citta} / {settore}")
        print(f"[RUN-500] Lead attuali: {totale_lead} / {args.target}")
        print(f"{'='*60}")

        # Crea sottocartella per questa combinazione (evita sovrascritture)
        run_dir = os.path.join(OUTPUT_DIR, f"run_{i:02d}_{citta.replace(' ', '_')}_{settore}")
        os.makedirs(run_dir, exist_ok=True)

        # Esegui tutte e 3 le pipeline
        try:
            print(f"\n[RUN-500] >> Pipeline NO-WEBSITE")
            esegui_no_website(citta, settore, run_dir)
        except Exception as e:
            print(f"[RUN-500] ERRORE no-website: {e}")

        try:
            print(f"\n[RUN-500] >> Pipeline CRO-FUNNEL")
            esegui_cro_funnel(citta, settore, run_dir)
        except Exception as e:
            print(f"[RUN-500] ERRORE cro-funnel: {e}")

        try:
            print(f"\n[RUN-500] >> Pipeline AI-IMPLEMENTATION")
            esegui_ai_implementation(citta, settore, run_dir)
        except Exception as e:
            print(f"[RUN-500] ERRORE ai-implementation: {e}")

        # Aggiorna conteggio
        totale_lead = conta_lead_csv(OUTPUT_DIR)
        print(f"\n[RUN-500] Totale lead dopo combo {i}: {totale_lead}")

    print(f"\n{'='*60}")
    print(f"[RUN-500] COMPLETATO — {totale_lead} lead totali in output/")
    print(f"[RUN-500] Passo successivo: python orchestrator/batch_send.py")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
