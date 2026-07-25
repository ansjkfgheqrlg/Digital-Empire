#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008 + APEX-7 Art.9

Agente Orchestratore — Entry Point Standalone per la Pipeline Completa
=======================================================================
Lancia l'intero ecosistema agenti in sequenza orchestrata:
  ScraperAgent → QualifierAgent → WriterAgent → SenderAgent → SheetsAgent
con GateAgent GATE-1 a ogni transizione di fase e MetaOptimizer finale.

Uso CLI:
  python agente_orchestratore.py --city Milano --categoria "concessionario auto" --limit 15
  python agente_orchestratore.py --cities "Milano,Bergamo,Brescia" --headless --sheet-id <ID>
  python agente_orchestratore.py --input cities.txt --only-alta --sheets-push-alta
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path
from typing import List

# ──────────────────────────────────────────────────────────────────────────────
# PATH SETUP — ordine fondamentale: prima gli agenti, poi gli script
# ──────────────────────────────────────────────────────────────────────────────
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SCRIPTS_DIR = os.path.join(_ROOT, "02-AUTOMAZIONI-E-SCRIPTS")
_AGENTS_DIR = os.path.join(_ROOT, "03-AGENTI-E-RUOLI")

for _p in [_SCRIPTS_DIR, _AGENTS_DIR]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

# ──────────────────────────────────────────────────────────────────────────────
# IMPORT MODULI CORE
# ──────────────────────────────────────────────────────────────────────────────
from event_bus import EventBus
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine
from gate_agent import GateAgent
from meta_optimization import MetaOptimizer
import browser as browser_module

# ──────────────────────────────────────────────────────────────────────────────
# IMPORT AGENTI UFFICIALI (da 03-AGENTI-E-RUOLI/)
# ──────────────────────────────────────────────────────────────────────────────
from agente_scraper import ScraperAgent
from agente_qualificatore import QualifierAgent
from agente_writer import WriterAgent
from agente_sender import SenderAgent
from agente_responder import ResponderAgent
from agente_integratore_sheets import SheetsAgent
from agente_gate import GateAgent as OfficialGateAgent

# ──────────────────────────────────────────────────────────────────────────────
# IMPORT ORCHESTRATORE
# ──────────────────────────────────────────────────────────────────────────────
from agents import QAAgent, Conductor, DebugAgent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("preventa-pw.orchestratore")

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────
def load_cities(args: argparse.Namespace) -> List[str]:
    """Carica la lista delle città da --city, --cities o --input."""
    if args.input:
        p = Path(args.input)
        if not p.exists():
            log.error(f"❌ File input non trovato: {args.input}")
            sys.exit(1)
        return [l.strip() for l in p.read_text(encoding="utf-8").splitlines()
                if l.strip() and not l.strip().startswith("#")]
    if args.cities:
        return [c.strip() for c in args.cities.replace(",", " ").split() if c.strip()]
    if args.city:
        return [args.city.strip()]
    return ["Milano"]  # Default fallback


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Preventa Maps Scraper — Orchestratore Agenti APEX-7",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python agente_orchestratore.py --city Milano --limit 10
  python agente_orchestratore.py --cities "Milano,Bergamo" --headless --only-alta
  python agente_orchestratore.py --input cities.txt --sheet-id <ID> --sheets-push-alta
        """
    )
    # Input cities
    city_grp = p.add_mutually_exclusive_group()
    city_grp.add_argument("--city",   type=str, help="Singola città da scansionare")
    city_grp.add_argument("--cities", type=str, help="Più città separate da virgola: Milano,Bergamo")
    city_grp.add_argument("--input",  type=str, help="File .txt con una città per riga")
    # Search params
    p.add_argument("--categoria",   type=str, default="concessionario auto", help="Categoria Google Maps")
    p.add_argument("--limit",       type=int, default=25,                    help="Max lead per città (default: 25)")
    # Browser
    p.add_argument("--headless",    action="store_true",  help="Modalità headless (per server)")
    p.add_argument("--headed",      action="store_true",  help="Modalità headed visibile (default)")
    # Output
    p.add_argument("--output",      type=str, default="data/leads_concessionari.csv", help="Path CSV output")
    p.add_argument("--only-alta",   action="store_true", help="Salva/carica solo lead priorità ALTA")
    # Google Sheets
    p.add_argument("--sheet-id",    type=str, default=os.getenv("GOOGLE_SHEET_ID", ""),
                   help="ID dello Sheet Google (o via env GOOGLE_SHEET_ID)")
    p.add_argument("--sheets-creds", type=str, default=os.getenv("GOOGLE_SHEETS_CREDS_PATH", "credentials.json"),
                   help="Path credenziali JSON service account")
    p.add_argument("--sheets-worksheet", type=str, default="Foglio1")
    p.add_argument("--sheets-push-alta", action="store_true", help="Carica su Sheets solo i lead ALTA")
    # Rate limits sender
    p.add_argument("--wa-limit",    type=int, default=15, help="Limite giornaliero WhatsApp (default: 15)")
    p.add_argument("--email-limit", type=int, default=25, help="Limite giornaliero Email (default: 25)")
    # Memory
    p.add_argument("--memory-path", type=str, default="data/memory_db.json", help="Path database memoria APEX-7")
    return p


# ──────────────────────────────────────────────────────────────────────────────
# ENTRY POINT PRINCIPALE
# ──────────────────────────────────────────────────────────────────────────────
def main():
    parser = build_argparser()
    args = parser.parse_args()
    cities = load_cities(args)

    headless = args.headless and not args.headed
    if not args.headless and not args.headed:
        headless = False
        log.info("🖥️  Modalità: HEADED visibile (più stabile). Usa --headless per server senza display.")

    log.info(f"🚀 Preventa Orchestratore avviato")
    log.info(f"   Città    : {cities}")
    log.info(f"   Categoria: {args.categoria}")
    log.info(f"   Limit    : {args.limit}")
    log.info(f"   Headless : {headless}")
    log.info(f"   Output   : {args.output}")
    log.info(f"   Only-Alta: {args.only_alta}")

    # ── Inizializzazione infrastruttura APEX-7 ──────────────────────────────
    event_bus = EventBus()
    event_bus.clear()
    memory = MemoryQueryInterface(memory_filepath=args.memory_path)
    gate_agent = OfficialGateAgent(memory=memory, event_bus=event_bus)
    qa_agent = QAAgent(gate_agent=gate_agent, event_bus=event_bus)
    meta_optimizer = MetaOptimizer(memory=memory)

    # ── Avvio Playwright ────────────────────────────────────────────────────
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--lang=it-IT,it",
            ],
        )
        context = browser.new_context(
            viewport={"width": 1366, "height": 850},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="it-IT",
        )
        page = context.new_page()

        # ── Istanziazione agenti ──────────────────────────────────────────
        scraper_agent   = ScraperAgent(page=page, event_bus=event_bus)
        qualifier_agent = QualifierAgent(event_bus=event_bus, gate_agent=gate_agent)
        writer_agent    = WriterAgent(event_bus=event_bus)
        sender_agent    = SenderAgent(
            event_bus=event_bus,
            daily_whatsapp_limit=args.wa_limit,
            daily_email_limit=args.email_limit,
        )
        debug_agent = DebugAgent(page=page, event_bus=event_bus)  # noqa: F841

        sheets_agent = None
        if args.sheet_id:
            sheets_agent = SheetsAgent(
                event_bus=event_bus,
                sheet_id=args.sheet_id,
                creds_path=args.sheets_creds,
                push_only_alta=args.sheets_push_alta,
                worksheet_name=args.sheets_worksheet,
            )
            log.info(f"📊 SheetsAgent configurato → Sheet ID: {args.sheet_id[:12]}...")
        else:
            log.info("ℹ️  Google Sheets non configurato (nessun --sheet-id). Solo output CSV locale.")

        conductor = Conductor(
            event_bus=event_bus,
            scraper_agent=scraper_agent,
            qualifier_agent=qualifier_agent,
            writer_agent=writer_agent,
            sender_agent=sender_agent,
            sheets_agent=sheets_agent,
            qa_agent=qa_agent,
            meta_optimizer=meta_optimizer,
            output_csv_path=args.output,
            only_alta=args.only_alta,
        )

        # ── Esecuzione per ogni città ─────────────────────────────────────
        for i, city in enumerate(cities):
            log.info(f"\n{'─'*60}")
            log.info(f"🏙️  [{i+1}/{len(cities)}] Avvio workflow per: {city.upper()}")
            log.info(f"{'─'*60}")
            conductor.run_city_workflow(city, args.categoria, args.limit)

            if i < len(cities) - 1:
                pausa = browser_module.random_delay(3.0, 6.0)
                log.info("⏳ Pausa inter-città in corso...")

        browser.close()

    log.info("\n" + "═" * 60)
    log.info("✅  PIPELINE APEX-7 COMPLETATA.")
    log.info(f"   Output CSV : {args.output}")
    if args.only_alta:
        from pathlib import Path as P
        alta_path = str(P(args.output).with_name(P(args.output).stem + "_SOLO_ALTA.csv"))
        log.info(f"   Solo ALTA  : {alta_path}")
    log.info("═" * 60)


if __name__ == "__main__":
    main()
