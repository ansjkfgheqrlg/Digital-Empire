# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Preventa Maps Scraper modular runner CLI.
"""
from __future__ import annotations

import argparse
import csv
import logging
import os
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Assicuriamo che la cartella degli script sia sul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import browser
import checker
import sheets

from event_bus import EventBus
from memory import MemoryQueryInterface
from gate_agent import GateAgent
from agents import ScraperAgent, QualifierAgent, SheetsAgent, QAAgent, DebugAgent, Conductor

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.run")

DEFAULT_CITIES = ["Milano", "Bergamo", "Brescia"]
DEFAULT_CATEGORIA = "concessionario auto"

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

def normalize_key(name, addr, phone):
    phone_n = re.sub(r'\s+', '', (phone or ''))
    if phone_n:
        return f"tel:{phone_n}"
    return f"name:{(name or '').lower().strip()}|{(addr or '').lower().strip()}"

import re

def save_csv(leads: List[Dict], output_path: str, only_alta: bool = False):
    if not leads:
        log.warning("Nessun lead da salvare.")
        return [], []

    deduped = {}
    for row in leads:
        key = normalize_key(row.get("nome_attivita",""), row.get("indirizzo",""), row.get("telefono",""))
        if key not in deduped:
            deduped[key] = row
        else:
            existing = deduped[key]
            if len(row.get("sito_web","")) > len(existing.get("sito_web","")):
                deduped[key] = row

    final = list(deduped.values())

    if only_alta:
        final_filtered = [r for r in final if r.get("priorita_lead") == "ALTA"]
        log.info(f"Filtro --only-alta: {len(final_filtered)} ALTA su {len(final)} totali")
    else:
        final_filtered = final

    order = {"ALTA":0, "MEDIA":1, "BASSA":2}
    final_sorted = sorted(final, key=lambda x: (order.get(x.get("priorita_lead","BASSA"),2), x.get("numero_recensioni",0)))
    filtered_sorted = sorted(final_filtered, key=lambda x: (order.get(x.get("priorita_lead","BASSA"),2), x.get("numero_recensioni",0)))

    fieldnames = ["nome_attivita","indirizzo","telefono","sito_web","ha_sito","numero_recensioni","media_recensioni","ha_ads_attive","priorita_lead","citta_ricerca","categoria","note_qualifica","maps_url","data_estrazione"]

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(final_sorted)

    log.info(f"\n✓ CSV completo salvato: {output_path} | {len(final_sorted)} lead unici (da {len(leads)} estratti)")
    from collections import Counter
    c = Counter([r["priorita_lead"] for r in final_sorted])
    log.info(f"Distribuzione priorità (completo): {dict(c)}")

    alta_path = None
    if only_alta:
        alta_path = str(Path(output_path).with_name(Path(output_path).stem + "_SOLO_ALTA.csv"))
        with open(alta_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            w.writeheader()
            w.writerows(filtered_sorted)
        log.info(f"✓ CSV SOLO ALTA salvato: {alta_path} | {len(filtered_sorted)} lead")

    return final_sorted, filtered_sorted

def load_cities(args):
    cities = []
    if args.input:
        p = Path(args.input)
        if not p.exists():
            log.error(f"File input non trovato: {args.input}")
            sys.exit(1)
        cities = [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip() and not l.strip().startswith("#")]
    elif args.cities:
        raw = args.cities
        if "," in raw:
            cities = [c.strip() for c in raw.split(",") if c.strip()]
        else:
            cities = [c.strip() for c in raw.split() if c.strip()]
    else:
        cities = DEFAULT_CITIES
    return cities

def main():
    parser = argparse.ArgumentParser(description="Preventa Maps Scraper - Playwright ONLY + Sheets + Filtro ALTA")
    parser.add_argument("--cities", type=str, help="Lista città separate da virgola: Milano,Bergamo,Brescia")
    parser.add_argument("--input", type=str, help="File txt con una città per riga")
    parser.add_argument("--categoria", type=str, default=DEFAULT_CATEGORIA)
    parser.add_argument("--output", type=str, default="data/leads_concessionari.csv")
    parser.add_argument("--limit", type=int, default=25, help="Max risultati per città")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--only-alta", action="store_true", help="Salva solo lead priorita ALTA nel CSV (e crea file _SOLO_ALTA.csv)")
    parser.add_argument("--sheet-id", type=str, default=os.getenv("GOOGLE_SHEET_ID",""), help="ID Google Sheet per push auto (dalla URL)")
    parser.add_argument("--sheets-creds", type=str, default=os.getenv("GOOGLE_SHEETS_CREDS_PATH","credentials.json"), help="Path file JSON service account")
    parser.add_argument("--sheets-worksheet", type=str, default="Foglio1", help="Nome worksheet")
    parser.add_argument("--sheets-push-alta", action="store_true", help="Se push su Sheets, pusha solo ALTA (consigliato)")
    args = parser.parse_args()

    cities = load_cities(args)
    log.info(f"Città: {cities} | Categoria: {args.categoria} | Limit: {args.limit} | only-alta={args.only_alta}")

    headless = args.headless and not args.headed
    if not args.headless and not args.headed:
        headless = False
        log.info("Modalità: HEADED visibile (più stabile). Usa --headless per server.")

    # Inizializza i moduli APEX-7
    event_bus = EventBus()
    event_bus.clear()  # Pulisce eventuali stati precedenti
    memory = MemoryQueryInterface()
    gate_agent = GateAgent(memory, event_bus)
    qa_agent = QAAgent(gate_agent, event_bus)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        br = p.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--lang=it-IT,it",
            ]
        )
        context = br.new_context(
            viewport={"width": 1366, "height": 850},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="it-IT"
        )
        page = context.new_page()

        # Istanziazione degli agenti
        scraper_agent = ScraperAgent(page, event_bus)
        qualifier_agent = QualifierAgent(event_bus)
        debug_agent = DebugAgent(page, event_bus)

        sheets_agent = None
        if args.sheet_id:
            sheets_agent = SheetsAgent(
                event_bus=event_bus,
                sheet_id=args.sheet_id,
                creds_path=args.sheets_creds,
                push_only_alta=args.sheets_push_alta,
                worksheet_name=args.sheets_worksheet
            )

        conductor = Conductor(
            event_bus=event_bus,
            scraper_agent=scraper_agent,
            qualifier_agent=qualifier_agent,
            sheets_agent=sheets_agent,
            qa_agent=qa_agent,
            output_csv_path=args.output,
            only_alta=args.only_alta
        )

        for i, city in enumerate(cities):
            conductor.run_city_workflow(city, args.categoria, args.limit)
            if i < len(cities)-1:
                pausa = browser.random_delay(3.0, 6.0)
                log.info(f"Pausa prima prossima città...")

        br.close()

    log.info("\n✅ FATTO. Workflow dello Scraper APEX-7 terminato.")
    log.info(f"File: {args.output}")
    if args.only_alta:
        log.info(f"File solo ALTA: {Path(args.output).with_name(Path(args.output).stem + '_SOLO_ALTA.csv')}")

if __name__ == "__main__":
    main()
