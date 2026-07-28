# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Campaign Orchestrator CLI (Plan 2)
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime

# Assicuriamo che la directory degli script sia sul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from event_bus import EventBus
from memory import MemoryQueryInterface
from gate_agent import GateAgent
from meta_optimization import MetaOptimizer
from agents import (
    ScraperAgent,
    QualifierAgent,
    WriterAgent,
    SenderAgent,
    AreusAgent,
    QAAgent,
    DebugAgent,
    Conductor
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.orchestrator")

def main():
    parser = argparse.ArgumentParser(description="APEX-7 Preventa Campaign Orchestrator CLI")
    parser.add_argument("--cities", type=str, help="Lista città separate da e.g. Milano,Bergamo")
    parser.add_argument("--categoria", type=str, default="concessionario auto")
    parser.add_argument("--output", type=str, default="data/leads_concessionari.csv")
    parser.add_argument("--limit", type=int, default=2, help="Max risultati per città (default basso per sicurezza)")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--only-alta", action="store_true", help="Salva solo lead priorità ALTA")
    parser.add_argument("--no-areus", action="store_true", help="Disattiva il push su Areus")
    parser.add_argument("--areus-state-path", type=str, default="", help="Override path del JSON condiviso con EmpireDesk")
    parser.add_argument("--mock-scrape", action="store_true", help="Simula lo scraping e usa dati finti per evitare blocchi Google")
    args = parser.parse_args()

    # Inizializzazione infrastruttura
    event_bus = EventBus()
    memory = MemoryQueryInterface(memory_filepath="data/memory_db.json")
    gate_agent = GateAgent(memory, event_bus)
    qa_agent = QAAgent(gate_agent, event_bus)
    meta_optimizer = MetaOptimizer(memory)

    # Parsing città
    cities = []
    if args.cities:
        cities = [c.strip() for c in args.cities.split(",") if c.strip()]
    else:
        cities = ["Como"] # Default di test

    log.info(f"🎭 [Orchestrator] Avvio campagna per città: {cities} | Mock: {args.mock_scrape}")

    # Definiamo gli agenti
    qualifier_agent = QualifierAgent(event_bus, gate_agent=gate_agent)
    writer_agent = WriterAgent(event_bus)
    sender_agent = SenderAgent(event_bus)
    
    areus_agent = None
    if not args.no_areus:
        areus_agent = AreusAgent(
            event_bus=event_bus,
            state_path=args.areus_state_path,
            push_only_alta=args.only_alta
        )

    if args.mock_scrape:
        # In modalità Mock, simuliamo lo scraping senza Playwright
        class MockPage:
            pass
            
        mock_page = MockPage()
        scraper_agent = ScraperAgent(mock_page, event_bus)
        
        # Override del metodo di scraping con dati finti
        def mock_execute_scraping(city: str, categoria: str, limit: int):
            log.info(f"🧪 [Mock] Generazione di 3 lead finti per {city}")
            event_bus.publish("search.started", scraper_agent.agent_id, {"city": city, "categoria": categoria})
            time_str = datetime.utcnow().isoformat() + "Z"
            mock_leads = [
                {
                    "nome_attivita": f"Auto {city} Srl",
                    "indirizzo": f"Via Roma 1, {city}",
                    "telefono": "+3902123456",
                    "sito_web": "http://www.auto-roma-test.it",
                    "numero_recensioni": 5,
                    "media_recensioni": 3.8,
                    "maps_url": "https://maps.google.com/test1",
                    "data_estrazione": time_str,
                    "citta_ricerca": city,
                    "categoria": categoria
                },
                {
                    "nome_attivita": f"Garage {city} di Rossi",
                    "indirizzo": f"Via Milano 42, {city}",
                    "telefono": "+3902987654",
                    "sito_web": "", # Nessun sito -> ALTA
                    "numero_recensioni": 12,
                    "media_recensioni": 4.2,
                    "maps_url": "https://maps.google.com/test2",
                    "data_estrazione": time_str,
                    "citta_ricerca": city,
                    "categoria": categoria
                }
            ]
            event_bus.publish("leads.extracted", scraper_agent.agent_id, {
                "city": city,
                "leads": mock_leads,
                "count": len(mock_leads)
            })
            
        scraper_agent.execute_scraping = mock_execute_scraping
        debug_agent = None
        
        conductor = Conductor(
            event_bus=event_bus,
            scraper_agent=scraper_agent,
            qualifier_agent=qualifier_agent,
            writer_agent=writer_agent,
            sender_agent=sender_agent,
            areus_agent=areus_agent,
            qa_agent=qa_agent,
            meta_optimizer=meta_optimizer,
            output_csv_path=args.output,
            only_alta=args.only_alta
        )

        for city in cities:
            conductor.run_city_workflow(city, args.categoria, args.limit)
            
    else:
        # Esecuzione reale con Playwright (multi-istanza)
        from playwright.sync_api import sync_playwright
        import concurrent.futures
        
        def run_single_city(city: str):
            log.info(f"🌐 [Browser-Thread] Avvio browser Playwright per {city}")
            with sync_playwright() as p:
                br = p.chromium.launch(
                    headless=args.headless,
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
                
                # Ciascun thread ha il suo scraper_agent e conductor locale per evitare conflitti di pagina
                thread_scraper_agent = ScraperAgent(page, event_bus)
                thread_debug_agent = DebugAgent(page, event_bus)
                
                # Suffix del CSV di output per evitare collisioni di scrittura concorrente
                city_output_path = args.output.replace(".csv", f"_{city}.csv")
                
                thread_conductor = Conductor(
                    event_bus=event_bus,
                    scraper_agent=thread_scraper_agent,
                    qualifier_agent=qualifier_agent,
                    writer_agent=writer_agent,
                    sender_agent=sender_agent,
                    areus_agent=areus_agent,
                    qa_agent=qa_agent,
                    meta_optimizer=meta_optimizer,
                    output_csv_path=city_output_path,
                    only_alta=args.only_alta
                )
                
                thread_conductor.run_city_workflow(city, args.categoria, args.limit)
                br.close()
                log.info(f"🌐 [Browser-Thread] Browser chiuso e salvato in {city_output_path}")

        # Esecuzione in parallelo con ThreadPoolExecutor (max 2 istanze concorrenti per stabilità)
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(cities), 2)) as executor:
            executor.map(run_single_city, cities)

if __name__ == "__main__":
    main()
