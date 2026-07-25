#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Esecuzione Agente Qualificatore
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
from agents import QualifierAgent

def main():
    parser = argparse.ArgumentParser(description="Esecuzione Standalone Agente Qualificatore")
    parser.add_argument("--input", type=str, required=True, help="Path file CSV o JSON con i lead grezzi")
    parser.add_argument("--output", type=str, required=True, help="Path file CSV di output per i lead qualificati")
    parser.add_argument("--city", type=str, default="Generica", help="Città del lotto di lead")
    args = parser.parse_args()

    # Legge i lead grezzi dall'input
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
    agent = QualifierAgent(event_bus)
    
    # Esegue la qualifica
    print(f"[*] Avvio qualificazione di {len(leads)} lead...")
    qualified = agent.qualify_leads(leads, city=args.city)
    
    # Salva i lead qualificati nel file di output CSV
    if qualified:
        # Assicura le intestazioni corrette
        fieldnames = ["nome_attivita","indirizzo","telefono","sito_web","ha_sito","numero_recensioni","media_recensioni","ha_ads_attive","priorita_lead","citta_ricerca","categoria","note_qualifica","maps_url","data_estrazione"]
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            w.writeheader()
            w.writerows(qualified)
        print(f"[+] Qualifica completata. Salvati {len(qualified)} lead in {args.output}")
    else:
        print("[-] Nessun lead qualificato.")

if __name__ == "__main__":
    main()
