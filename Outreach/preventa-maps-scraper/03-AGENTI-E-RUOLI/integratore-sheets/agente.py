#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGENTE: Sheets-1 — Google Sheets Integration Agent
Owner: GAEL · Controllore: A2-QA · Versione: 2.0
Governo: APEX-7 Framework · preventa-maps-scraper

Documentazione completa: ./AGENTE.md

CLI:
    python agente.py --input data/leads.csv --sheet-id <ID> [--creds credentials.json]
"""
from __future__ import annotations

import os
import sys
import csv
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

import sheets
from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-integratore-sheets")


class SheetsAgent:
    """
    Agente APEX-7 responsabile della sincronizzazione dei lead finali su Google Sheets (deduplica
    e batching delegati al modulo condiviso `sheets.py`). Documentazione completa → AGENTE.md.
    """

    def __init__(self, event_bus: Optional[EventBus] = None, sheet_id: str = "", creds_path: str = "credentials.json",
                 push_only_alta: bool = False, worksheet_name: str = "Foglio1"):
        self.agent_id = "SheetsAgent-1"
        self.event_bus = event_bus or EventBus()
        self.sheet_id = sheet_id
        self.creds_path = creds_path
        self.push_only_alta = push_only_alta
        self.worksheet_name = worksheet_name
        self.rules = self._load_rules()

    def _load_rules(self) -> str:
        md = _AGENT_DIR / "AGENTE.md"
        return md.read_text(encoding="utf-8") if md.exists() else "Rules not found"

    def upload(self, leads: List[Dict[str, Any]], city: str):
        log.info(f"📤 [{self.agent_id}] Inizio sincronizzazione su Google Sheets per la città: {city}")

        if not self.sheet_id:
            log.warning(f"⚠️ [{self.agent_id}] GOOGLE_SHEET_ID non impostato. Salto sincronizzazione Sheets per {city}.")
            self.event_bus.publish("sheets.synced", self.agent_id, {"city": city, "success": True})
            return

        try:
            sheets.upload_to_google_sheets(
                leads=leads,
                sheet_id=self.sheet_id,
                creds_path=self.creds_path,
                push_only_alta=self.push_only_alta,
                worksheet_name=self.worksheet_name
            )
            self.event_bus.publish("sheets.synced", self.agent_id, {"city": city, "success": True})
            log.info(f"✅ [{self.agent_id}] Caricamento Google Sheets completato per {city}.")
        except Exception as e:
            self.event_bus.publish("run.failed", self.agent_id, {"city": city, "error": str(e)})
            raise e


# ── CLI Standalone ────────────────────────────────────────────────────────────
def _cli() -> None:
    parser = argparse.ArgumentParser(description="Run SheetsAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file CSV dei lead qualificati")
    parser.add_argument("--sheet-id", type=str, required=True, help="ID dello Sheet di Google (dalla URL)")
    parser.add_argument("--creds", type=str, default="credentials.json", help="Path al file JSON delle credenziali")
    parser.add_argument("--worksheet", type=str, default="Foglio1", help="Nome del foglio di lavoro")
    parser.add_argument("--only-alta", action="store_true", help="Carica solo lead a priorità ALTA")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    leads = []
    with open(input_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    log.info(f"📤 Caricati {len(leads)} lead da CSV per caricamento su Google Sheets...")
    agent = SheetsAgent(
        sheet_id=args.sheet_id,
        creds_path=args.creds,
        push_only_alta=args.only_alta,
        worksheet_name=args.worksheet
    )
    agent.upload(leads, args.city)


if __name__ == "__main__":
    _cli()
