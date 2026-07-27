#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Scraper-1 — Playwright Browser Driver Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --city Como --categoria "concessionario auto" --limit 10
"""
from __future__ import annotations

import os
import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Any, List, Dict, Optional

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import browser
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-scraper")


class ScraperAgent:
    """
    Agente APEX-7 responsabile della raccolta lead grezzi da Google Maps via Playwright.
    Documentazione completa → AGENTE.md.
    """

    def __init__(self, page: Any = None, event_bus: Optional[EventBus] = None):
        self.agent_id = "ScraperAgent-1"
        self.page = page
        self.event_bus = event_bus or EventBus()
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def execute_scraping(self, city: str, categoria: str, limit: int) -> List[Dict[str, Any]]:
        log.info(f"🚀 [{self.agent_id}] Avvio scraping per la città: {city} | Categoria: {categoria} | Limit: {limit}")
        self.event_bus.publish("search.started", self.agent_id, {"city": city, "categoria": categoria})

        if not self.page:
            raise ValueError("Errore: Playwright page non inizializzata. Inizializzare l'agente con una pagina valida o usare la CLI.")

        try:
            raw_leads = browser.scrape_city(self.page, city, categoria, limit)
            self.event_bus.publish("leads.extracted", self.agent_id, {
                "city": city,
                "leads": raw_leads,
                "count": len(raw_leads)
            })
            log.info(f"✅ [{self.agent_id}] Scraping completato per {city}. Trovati {len(raw_leads)} lead.")
            return raw_leads
        except Exception as e:
            self.event_bus.publish("run.failed", self.agent_id, {"city": city, "error": str(e)})
            raise e


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run ScraperAgent Standalone CLI")
    parser.add_argument("--city", type=str, default="Como", help="Città da scansionare")
    parser.add_argument("--categoria", type=str, default="concessionario auto", help="Categoria di ricerca")
    parser.add_argument("--limit", type=int, default=2, help="Numero max di risultati")
    parser.add_argument("--output", type=str, default="data/raw_leads_output.json", help="Path output JSON")
    parser.add_argument("--headless", action="store_true", help="Avvia in modalità headless")
    args = parser.parse_args()

    log.info("🔧 Inizializzazione sessione standalone per ScraperAgent...")
    from playwright.sync_api import sync_playwright

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

        agent = ScraperAgent(page=page)
        results = agent.execute_scraping(args.city, args.categoria, args.limit)

        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        log.info(f"💾 Risultati grezzi salvati in: {output_path}")
        br.close()


if __name__ == "__main__":
    _cli()
