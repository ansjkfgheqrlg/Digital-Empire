#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Esecuzione Agente Responder (Reply Classification)
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
from agents import ResponderAgent

def main():
    parser = argparse.ArgumentParser(description="Esecuzione Standalone Agente Responder (Gestione Risposte)")
    parser.add_argument("--lead-id", type=str, required=True, help="ID o telefono del lead")
    parser.add_argument("--reply", type=str, required=True, help="Testo della risposta ricevuta dal lead")
    args = parser.parse_args()

    event_bus = EventBus()
    agent = ResponderAgent(event_bus)
    
    # Esegue l'elaborazione della risposta
    print(f"[*] Classificazione risposta per il lead {args.lead_id}...")
    result = agent.process_reply(args.lead_id, args.reply)
    
    print("\n[+] Esito Classificazione:")
    print(f" - Lead ID: {result['lead_id']}")
    print(f" - Risposta Ricevuta: '{result['reply_received']}'")
    print(f" - Esito Qualificato: {result['esito'].upper()}")
    print(f" - Risposta Suggerita: '{result['suggested_response']}'")

if __name__ == "__main__":
    main()
