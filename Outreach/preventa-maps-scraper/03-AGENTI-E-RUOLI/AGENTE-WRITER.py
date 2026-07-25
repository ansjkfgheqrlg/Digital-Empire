#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Esecuzione Agente Scrittore (Copywriting Outreach)
"""
from __future__ import annotations
import sys
import os
import argparse
import csv
import json

# Aggiunge la directory scripts al path per caricare i moduli
SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS"))
sys.path.append(SCRIPTS_DIR)

from event_bus import EventBus
from agents import WriterAgent

def main():
    parser = argparse.ArgumentParser(description="Esecuzione Standalone Agente Scrittore")
    parser.add_argument("--input", type=str, required=True, help="Path file CSV o JSON dei lead qualificati")
    parser.add_argument("--output", type=str, required=True, help="Path file CSV o JSON di output dei copy generati")
    parser.add_argument("--city", type=str, default="Generica", help="Città del lotto di lead")
    args = parser.parse_args()

    # Legge i lead dall'input
    leads = []
    if args.input.endswith(".json"):
        with open(args.input, "r", encoding="utf-8") as f:
            leads = json.load(f)
    elif args.input.endswith(".csv"):
        with open(args.input, "r", encoding="utf-8") as f:
            r = csv.DictReader(f)
            leads = [dict(row) for row in r]
    else:
        print("[-] Errore: formato file non supportato (usa .csv o .json)")
        sys.exit(1)

    event_bus = EventBus()
    agent = WriterAgent(event_bus)
    
    # Esegue la generazione del copy
    print(f"[*] Avvio generazione copy per {len(leads)} lead...")
    messages = agent.generate_messages(leads, city=args.city)
    
    # Salva in formato idoneo
    if messages:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        if args.output.endswith(".json"):
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=2)
        else:
            # Flatten dicts for csv writing if nested email dict exists
            flat_messages = []
            for m in messages:
                flat = m.copy()
                if isinstance(flat.get("email1"), dict):
                    flat["email1_oggetto"] = flat["email1"].get("oggetto_a", "")
                    flat["email1_corpo"] = flat["email1"].get("corpo", "")
                    del flat["email1"]
                if "gancio_scelto" in flat and isinstance(flat["gancio_scelto"], dict):
                    flat["gancio_scelto_num"] = flat["gancio_scelto"].get("numero", 1)
                    flat["gancio_scelto_nome"] = flat["gancio_scelto"].get("nome", "")
                    del flat["gancio_scelto"]
                flat_messages.append(flat)
                
            fieldnames = list(flat_messages[0].keys())
            with open(args.output, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(flat_messages)
        print(f"[+] Generazione copy completata. Salvati {len(messages)} record in {args.output}")
    else:
        print("[-] Nessun copy generato.")

if __name__ == "__main__":
    main()
