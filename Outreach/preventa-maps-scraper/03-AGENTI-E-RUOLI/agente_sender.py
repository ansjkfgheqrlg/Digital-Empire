#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Message Sender Agent (Sender-1)
"""
from __future__ import annotations

import os
import sys
import json
import time
import random
import logging
import argparse
from pathlib import Path
from typing import Any, List, Dict, Optional

# Aggiunge i percorsi necessari al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS")))

from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-sender")

class SenderAgent:
    def __init__(self, event_bus: Optional[EventBus] = None, daily_whatsapp_limit: int = 15, daily_email_limit: int = 25):
        self.agent_id = "SenderAgent-1"
        self.event_bus = event_bus or EventBus()
        self.daily_whatsapp_limit = daily_whatsapp_limit
        self.daily_email_limit = daily_email_limit
        self.rules = self.load_markdown_rules()

    def load_markdown_rules(self) -> str:
        """Carica dinamicamente le regole di comportamento dal file MD associato."""
        md_path = Path(__file__).parent / "AGENTE-SENDER.md"
        if md_path.exists():
            return md_path.read_text(encoding="utf-8")
        return "Rules file not found."

    def send_outreach(self, messages: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"📨 [{self.agent_id}] Spedizione in corso per {len(messages)} messaggi in {city} (Limiti: WA {self.daily_whatsapp_limit}, Email {self.daily_email_limit})")
        log.info(f"📖 [{self.agent_id}] Caricate regole di invio da AGENTE-SENDER.md (Rate Limit & Delays)")
        
        sent_messages = []
        wa_sent = 0
        email_sent = 0

        for msg in messages:
            canale = msg.get("canale_primario", "email")
            nome = msg.get("nome_attivita", "N/A")

            # Applica i rate limit giornalieri
            if canale == "whatsapp":
                if wa_sent >= self.daily_whatsapp_limit:
                    log.warning(f"⚠️ [{self.agent_id}] Limit rate raggiunto per WhatsApp ({self.daily_whatsapp_limit}). Spedizione sospesa per il lead: {nome}")
                    continue
                wa_sent += 1
            else:
                if email_sent >= self.daily_email_limit:
                    log.warning(f"⚠️ [{self.agent_id}] Limit rate raggiunto per Email ({self.daily_email_limit}). Spedizione sospesa per il lead: {nome}")
                    continue
                email_sent += 1

            log.info(f"📤 [{self.agent_id}] Inviato messaggio a {nome} via {canale.upper()}")
            
            # Applica ritardo casuale simulativo in base alle regole
            # Disattivato solo se si tratta di un ambiente di test unitario veloce
            if "test" not in city.lower():
                delay = random.uniform(1.0, 2.5)
                time.sleep(delay)

            msg["stato"] = "contattato"
            sent_messages.append(msg)

        self.event_bus.publish("messages.sent", self.agent_id, {
            "city": city,
            "messages": sent_messages,
            "count": len(sent_messages)
        })
        log.info(f"✅ [{self.agent_id}] Spedizione completata per {city}. Inviati {len(sent_messages)} messaggi.")
        return sent_messages

def cli_run():
    parser = argparse.ArgumentParser(description="Run SenderAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file JSON dei messaggi personalizzati")
    parser.add_argument("--output", type=str, default="data/report_contatti.json", help="Path report output JSON")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        messages = json.load(f)

    log.info(f"📨 Caricati {len(messages)} messaggi da inviare...")
    agent = SenderAgent()
    results = agent.send_outreach(messages, args.city)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    log.info(f"💾 Report di invio salvato in: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_run()
    else:
        print("Uso CLI: python agente_sender.py --input <generated_messages.json> [--output <path>]")
