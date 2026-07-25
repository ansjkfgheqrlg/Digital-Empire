#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Incoming Reply Handler Agent (Responder-1)
"""
from __future__ import annotations

import os
import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Any, Dict, Optional

# Aggiunge i percorsi necessari al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS")))

from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-responder")

class ResponderAgent:
    def __init__(self, event_bus: Optional[EventBus] = None):
        self.agent_id = "ResponderAgent-1"
        self.event_bus = event_bus or EventBus()
        self.rules = self.load_markdown_rules()

    def load_markdown_rules(self) -> str:
        """Carica dinamicamente le regole di comportamento dal file MD associato."""
        md_path = Path(__file__).parent / "AGENTE-RESPONDER.md"
        if md_path.exists():
            return md_path.read_text(encoding="utf-8")
        return "Rules file not found."

    def process_reply(self, lead_id: str, reply_text: str) -> Dict[str, Any]:
        log.info(f"💬 [{self.agent_id}] Classificazione risposta del lead {lead_id}: '{reply_text}'")
        log.info(f"📖 [{self.agent_id}] Caricate regole di classificazione da AGENTE-RESPONDER.md")
        
        text = reply_text.lower().strip()
        
        # Logica di classificazione dell'intento
        if "no" in text or "non" in text or "togli" in text or "spam" in text or "rifiut" in text or "cancella" in text or "basta" in text:
            esito = "no_grazie"
            risposta = "Capito. Ti ringrazio per il riscontro e ti auguro una buona giornata."
        elif "prezzo" in text or "costo" in text or "tariffa" in text or "quanto costa" in text or "funziona" in text or "compatibile" in text:
            esito = "domanda_obiezione"
            risposta = "Capisco la domanda. Preventa non sostituisce il tuo gestionale ma vi si affianca in 2 minuti. Riguardo ai costi, abbiamo una licenza a canone mensile super accessibile e disdetta libera. Ti andrebbe domani alle 11:00 o giovedì alle 16:30 per vederlo veloce su schermo in 15 minuti?"
        elif "interessa" in text or "sì" in text or "si" in text or "info" in text or "chiamaci" in text or "ok" in text or "va bene" in text or "chiamata" in text:
            esito = "interessato"
            risposta = "Ottimo! Ti propongo di fare una breve chiamata conoscitiva di 15 minuti per vedere un esempio pratico sul vostro stesso annuncio. Ti andrebbe domani alle 11:00 o giovedì alle 16:30?"
        else:
            esito = "risposto"
            risposta = "Grazie per il riscontro. Se desideri vedere una demo veloce senza impegno sul vostro stesso annuncio, possiamo fare una chiamata rapida di 15 minuti su schermo."

        result = {
            "lead_id": lead_id,
            "reply_received": reply_text,
            "esito": esito,
            "suggested_response": risposta
        }
        
        self.event_bus.publish("reply.processed", self.agent_id, result)
        return result

def cli_run():
    parser = argparse.ArgumentParser(description="Run ResponderAgent Standalone CLI")
    parser.add_argument("--lead-id", type=str, required=True, help="ID o Telefono del lead")
    parser.add_argument("--text", type=str, required=True, help="Testo della risposta ricevuta dal lead")
    args = parser.parse_args()

    agent = ResponderAgent()
    result = agent.process_reply(args.lead_id, args.text)

    print("\n--- RISULTATO CLASSIFICAZIONE ---")
    print(f"Lead ID: {result['lead_id']}")
    print(f"Risposta Ricevuta: '{result['reply_received']}'")
    print(f"Esito Classificato: {result['esito'].upper()}")
    print(f"Risposta Consigliata:\n{result['suggested_response']}")
    print("---------------------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_run()
    else:
        print("Uso CLI: python agente_responder.py --lead-id <id> --text '<messaggio>'")
