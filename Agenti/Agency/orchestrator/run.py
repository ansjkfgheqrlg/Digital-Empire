"""
Orchestrator — Digital Empire Agency
Punto di ingresso unico per tutte le pipeline.

Uso:
    python run.py --pipeline no-website --citta "Milano" --settore "ristoranti"
    python run.py --pipeline cro-funnel --url "https://esempio.com"
    python run.py --pipeline ai-implementation --citta "Roma" --settore "avvocati"
    python run.py --pipeline full --citta "Napoli" --settore "dentisti"
"""

import argparse
import sys
import os
from datetime import datetime

# Aggiungi le cartelle dei sub-agenti al path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, AGENCY_DIR)

OUTPUT_DIR = os.path.join(AGENCY_DIR, "output")
LEADS_DIR = os.path.join(OUTPUT_DIR, "leads")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")
EMAILS_DIR = os.path.join(OUTPUT_DIR, "emails")


def crea_struttura_output():
    """Crea le cartelle di output se non esistono."""
    for cartella in [LEADS_DIR, REPORTS_DIR, EMAILS_DIR]:
        os.makedirs(cartella, exist_ok=True)


def esegui_no_website(citta: str, settore: str):
    print(f"\n[ORCHESTRATOR] Avvio pipeline NO-WEBSITE → {citta} / {settore}")
    sub_agent_dir = os.path.join(AGENCY_DIR, "sub-agents", "no-website")
    sys.path.insert(0, sub_agent_dir)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(citta=citta, settore=settore, output_dir=OUTPUT_DIR)


def esegui_cro_funnel(url: str = None, citta: str = None, settore: str = None):
    print(f"\n[ORCHESTRATOR] Avvio pipeline CRO-FUNNEL → {url or f'{citta}/{settore}'}")
    sub_agent_dir = os.path.join(AGENCY_DIR, "sub-agents", "cro-funnel")
    sys.path.insert(0, sub_agent_dir)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(url=url, citta=citta, settore=settore, output_dir=OUTPUT_DIR)


def esegui_ai_implementation(citta: str, settore: str):
    print(f"\n[ORCHESTRATOR] Avvio pipeline AI-IMPLEMENTATION → {citta} / {settore}")
    sub_agent_dir = os.path.join(AGENCY_DIR, "sub-agents", "ai-implementation")
    sys.path.insert(0, sub_agent_dir)
    from pipeline import esegui_pipeline  # type: ignore
    esegui_pipeline(citta=citta, settore=settore, output_dir=OUTPUT_DIR)


def main():
    parser = argparse.ArgumentParser(description="Digital Empire Agency Orchestrator")
    parser.add_argument("--pipeline", choices=["no-website", "cro-funnel", "ai-implementation", "full"], required=True)
    parser.add_argument("--citta", default=None)
    parser.add_argument("--settore", default=None)
    parser.add_argument("--url", default=None, help="URL sito (solo per cro-funnel)")
    args = parser.parse_args()

    crea_struttura_output()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[ORCHESTRATOR] Start — {timestamp}")
    print(f"[ORCHESTRATOR] Pipeline: {args.pipeline}")

    if args.pipeline == "no-website":
        if not args.citta or not args.settore:
            print("ERRORE: --citta e --settore richiesti per no-website")
            sys.exit(1)
        esegui_no_website(args.citta, args.settore)

    elif args.pipeline == "cro-funnel":
        if not args.url and not (args.citta and args.settore):
            print("ERRORE: --url oppure --citta + --settore richiesti per cro-funnel")
            sys.exit(1)
        esegui_cro_funnel(url=args.url, citta=args.citta, settore=args.settore)

    elif args.pipeline == "ai-implementation":
        if not args.citta or not args.settore:
            print("ERRORE: --citta e --settore richiesti per ai-implementation")
            sys.exit(1)
        esegui_ai_implementation(args.citta, args.settore)

    elif args.pipeline == "full":
        if not args.citta or not args.settore:
            print("ERRORE: --citta e --settore richiesti per pipeline full")
            sys.exit(1)
        esegui_no_website(args.citta, args.settore)
        esegui_cro_funnel(citta=args.citta, settore=args.settore)
        esegui_ai_implementation(args.citta, args.settore)

    print(f"\n[ORCHESTRATOR] Pipeline completata. Output in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
