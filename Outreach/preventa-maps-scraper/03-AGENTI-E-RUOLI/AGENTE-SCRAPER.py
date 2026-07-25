#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Esecuzione Agente Scraper (Browser Driver)
"""
from __future__ import annotations
import sys
import os
import argparse
import json

# Aggiunge la directory scripts al path per caricare i moduli
SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS"))
sys.path.append(SCRIPTS_DIR)

from event_bus import EventBus
from agents import ScraperAgent

def main():
    parser = argparse.ArgumentParser(description="Esecuzione Standalone Agente Scraper (Maps)")
    parser.add_argument("--city", type=str, required=True, help="Città da scansionare")
    parser.add_argument("--categoria", type=str, default="concessionario auto", help="Categoria Maps")
    parser.add_argument("--limit", type=int, default=10, help="Limite risultati")
    parser.add_argument("--headless", action="store_true", help="Avvia browser in background")
    parser.add_argument("--output", type=str, help="Salva i dati estratti in formato JSON")
    args = parser.parse_args()

    event_bus = EventBus()
    
    from playwright.sync_api import sync_playwright
    
    print(f"[*] Inizializzazione Playwright per {args.city}...")
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
        
        agent = ScraperAgent(page, event_bus)
        results = agent.execute_scraping(args.city, args.categoria, args.limit)
        
        print(f"\n[+] Trovati {len(results)} lead:")
        for r in results:
            print(f" - {r.get('nome_attivita')} | Tel: {r.get('telefono')} | Sito: {r.get('sito_web')}")
            
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"[+] Dati grezzi salvati in {args.output}")
            
        br.close()

if __name__ == "__main__":
    main()
