#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Qualifier-1 — Lead Qualifier Agent (Site Analyst)
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --input data/raw_leads.json --city Como
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

import checker
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-qualificatore")


class QualifierAgent:
    """
    Agente APEX-7 responsabile della qualifica parallela dei lead grezzi (priorità ALTA/MEDIA/BASSA)
    e, se collegato a un GateAgent, del filtro Data-Validator-Gate prima che il lead entri nella
    pipeline di contatto. Documentazione completa → AGENTE.md.
    """

    def __init__(self, event_bus: Optional[EventBus] = None, gate_agent: Optional[Any] = None):
        self.agent_id = "QualifierAgent-1"
        self.event_bus = event_bus or EventBus()
        self.gate_agent = gate_agent
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def qualify_leads(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"🔍 [{self.agent_id}] Avvio qualifica in parallelo di {len(leads)} lead per la città: {city}")
        qualified = checker.qualify_leads_parallel(leads)

        # Data-Validator-Gate: se un GateAgent è configurato, filtra i lead qualificati
        if self.gate_agent:
            validated = []
            for lead in qualified:
                try:
                    val_res = self.gate_agent.validate_lead(lead)
                    if val_res.get("passed", True):
                        validated.append(lead)
                except AttributeError:
                    # Fallback se il gate_agent passato non implementa validate_lead
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


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
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
    _cli()
