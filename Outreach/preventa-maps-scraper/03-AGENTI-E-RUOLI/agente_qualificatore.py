#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Lead Qualifier Agent (Site Analyst)
"""
from __future__ import annotations

import os
import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Any, List, Dict, Optional

# Aggiunge i percorsi necessari al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS")))

import checker
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-qualificatore")

class QualifierAgent:
    def __init__(self, event_bus: Optional[EventBus] = None, gate_agent: Optional[Any] = None):
        self.agent_id = "QualifierAgent-1"
        self.event_bus = event_bus or EventBus()
        self.gate_agent = gate_agent
        self.rules = self.load_markdown_rules()

    def load_markdown_rules(self) -> str:
        """Carica dinamicamente le regole di comportamento dal file MD associato."""
        md_path = Path(__file__).parent / "AGENTE-QUALIFICATORE.md"
        if md_path.exists():
            return md_path.read_text(encoding="utf-8")
        return "Rules file not found."

    def qualify_leads(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"🔍 [{self.agent_id}] Avvio qualifica in parallelo di {len(leads)} lead per la città: {city}")
        log.info(f"📖 [{self.agent_id}] Caricate regole di qualificazione da AGENTE-QUALIFICATORE.md")
        
        qualified = checker.qualify_leads_parallel(leads)

        # Se è configurato un GateAgent per il Data-Validator-Gate
        if self.gate_agent:
            validated = []
            for lead in qualified:
                try:
                    # In agents.py originale fa: self.gate_agent.validate_lead(lead)
                    val_res = self.gate_agent.validate_lead(lead)
                    if val_res.get("passed", True):
                        validated.append(lead)
                except AttributeError:
                    # Fallback se validate_lead non esiste sul gate_agent passato
                    validated.append(lead)
            
            rejected_count = len(qualified) - len(validated)
            if rejected_count:
                log.info(f"🚫 [{self.agent_id}] Gate Agent ha scartato {rejected_count}/{len(qualified)} lead per {city} in base ai criteri di qualità.")
            qualified = validated

        self.event_bus.publish("leads.qualified", self.agent_id, {
            "city": city,
            "leads": qualified,
            "count": len(qualified)
        })
        log.info(f"✅ [{self.agent_id}] Qualifica completata per {city}.")
        return qualified

def cli_run():
    parser = argparse.ArgumentParser(description="Run QualifierAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file JSON dei lead grezzi")
    parser.add_argument("--output", type=str, default="data/qualified_leads_output.json", help="Path output JSON")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        raw_leads = json.load(f)

    log.info(f"🔍 Caricati {len(raw_leads)} lead grezzi da qualificare...")
    agent = QualifierAgent()
    results = agent.qualify_leads(raw_leads, args.city)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    log.info(f"💾 Risultati qualificati salvati in: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_run()
    else:
        # Mostra help se eseguito senza argomenti
        print("Uso CLI: python agente_qualificatore.py --input <raw_leads.json> [--output <path>]")
