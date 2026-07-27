#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Gate-1 — Quality Gate Agent (Deterministic Pipeline Checkpoints)
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

NON duplicare logica qui: l'implementazione dei controlli (evaluate_output, validate_lead) vive
in ../../02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py, condivisa anche da orchestrator.py e run.py.
Questo modulo si limita ad aggiungere il caricamento delle regole da AGENTE.md e la CLI
standalone, per rispettare il pattern cartella-per-agente senza triplicare ~200 righe di logica.

CLI:
    python agente.py --gate-id L1_L2 --content "città: Como, categoria: concessionario auto"
"""
from __future__ import annotations

import os
import sys
import logging
import argparse
from pathlib import Path
from typing import Any, Dict, Optional

# ── Path resolution ──────────────────────────────────────────────────────────
_AGENT_DIR = Path(__file__).parent
_ROOT_DIR  = _AGENT_DIR.parent.parent
_SCRIPTS   = _ROOT_DIR / "02-AUTOMAZIONI-E-SCRIPTS"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from event_bus import EventBus
from memory import MemoryQueryInterface
from gate_agent import GateAgent as _CoreGateAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-gate")


class GateAgent(_CoreGateAgent):
    """
    Estensione "operativa" del GateAgent canonico (02-AUTOMAZIONI-E-SCRIPTS/gate_agent.py):
    stessa logica di valutazione (evaluate_output, validate_lead), più il caricamento delle
    regole comportamentali da AGENTE.md e costruttore con default comodi per uso standalone/CLI.
    Documentazione completa → AGENTE.md.
    """

    def __init__(self, memory: Optional[MemoryQueryInterface] = None, event_bus: Optional[EventBus] = None):
        memory = memory or MemoryQueryInterface(memory_filepath="data/memory_db.json")
        event_bus = event_bus or EventBus()
        super().__init__(memory, event_bus)
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run GateAgent Standalone CLI")
    parser.add_argument("--gate-id", type=str, required=True,
                         choices=["L1_L2", "L2_L3", "L3_L4", "L4_L5", "L5_L6", "L6_L7"],
                         help="ID del gate da valutare")
    parser.add_argument("--content", type=str, required=True, help="Contenuto dell'output da valutare")
    args = parser.parse_args()

    agent = GateAgent()
    report = agent.evaluate_output(args.gate_id, args.content)

    print("\n--- REPORT DI QUALITA' GATE ---")
    print(f"Gate ID: {report['gate_id']}")
    print(f"Passed: {'SI' if report['passed'] else 'NO'}")
    print(f"Score: {report['score']} (Soglia: {report['threshold']})")
    print("Dettaglio Criteri:")
    for c in report["criteria_results"]:
        print(f"  [{c['status']}] {c['criterion_id']}: {c['description']} | Note: {c.get('note')}")
    print("--------------------------------")


if __name__ == "__main__":
    _cli()
