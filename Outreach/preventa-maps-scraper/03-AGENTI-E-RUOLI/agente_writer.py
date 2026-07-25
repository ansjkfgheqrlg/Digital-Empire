#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Outbound Copywriting Agent (Writer-1)
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

CAMPAIGN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Outreach Workflow/campagne/concessionari-preventa"))
sys.path.append(CAMPAIGN_DIR)

try:
    import personalizza_messaggi
except ImportError:
    personalizza_messaggi = None

from event_bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-writer")

class WriterAgent:
    def __init__(self, event_bus: Optional[EventBus] = None):
        self.agent_id = "WriterAgent-1"
        self.event_bus = event_bus or EventBus()
        self.rules = self.load_markdown_rules()

    def load_markdown_rules(self) -> str:
        """Carica dinamicamente le regole di comportamento dal file MD associato."""
        md_path = Path(__file__).parent / "AGENTE-WRITER.md"
        if md_path.exists():
            return md_path.read_text(encoding="utf-8")
        return "Rules file not found."

    def generate_messages(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"✍️ [{self.agent_id}] Avvio generazione copy personalizzato per {len(leads)} lead in {city}")
        log.info(f"📖 [{self.agent_id}] Caricate regole di scrittura da AGENTE-WRITER.md (APSOC)")
        
        generated = []
        for row in leads:
            try:
                if personalizza_messaggi:
                    # Usa il modulo di campagna ufficiale per generare i messaggi personalizzati
                    msg_data = personalizza_messaggi.genera_messaggi(row)
                else:
                    # Fallback locale in caso di assenza dei file di campagna
                    nome_attivita = row.get("nome_attivita", "").strip()
                    telefono = row.get("telefono", "").strip()
                    priorita = row.get("priorita_lead", "MEDIA").strip().upper()
                    canale_primario = "whatsapp" if telefono else "email"
                    
                    msg_data = {
                        "nome_attivita": nome_attivita,
                        "citta": city,
                        "telefono": telefono,
                        "priorita_lead": priorita,
                        "gancio_scelto": {"numero": 1, "nome": "Tempo perso", "motivo": "fallback"},
                        "canale_primario": canale_primario,
                        "whatsapp_msg1": f"Ciao, ho visto {nome_attivita} su Maps. Perdiamo 20-30 min a preventivo?",
                        "email1": {"oggetto_a": "Preventivi velocizzati", "corpo": f"Buongiorno {nome_attivita}..."},
                        "stato": "da_contattare"
                    }
                generated.append(msg_data)
            except Exception as e:
                log.error(f"❌ Errore generazione messaggio per {row.get('nome_attivita', 'N/A')}: {e}")

        self.event_bus.publish("messages.generated", self.agent_id, {
            "city": city,
            "messages": generated,
            "count": len(generated)
        })
        log.info(f"✅ [{self.agent_id}] Generazione copy completata per {city}.")
        return generated

def cli_run():
    parser = argparse.ArgumentParser(description="Run WriterAgent Standalone CLI")
    parser.add_argument("--input", type=str, required=True, help="Path file JSON dei lead qualificati")
    parser.add_argument("--output", type=str, default="data/generated_messages.json", help="Path output JSON")
    parser.add_argument("--city", type=str, default="Como", help="Città di riferimento per log")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ File input non trovato: {input_path}")
        sys.exit(1)

    with open(input_path, encoding="utf-8") as f:
        qualified_leads = json.load(f)

    log.info(f"✍️ Caricati {len(qualified_leads)} lead qualificati per la generazione del copy...")
    agent = WriterAgent()
    results = agent.generate_messages(qualified_leads, args.city)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    log.info(f"💾 Messaggi personalizzati salvati in: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_run()
    else:
        print("Uso CLI: python agente_writer.py --input <qualified_leads.json> [--output <path>]")
