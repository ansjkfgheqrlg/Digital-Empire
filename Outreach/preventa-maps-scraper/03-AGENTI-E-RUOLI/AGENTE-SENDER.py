#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Esecuzione Agente Speditore (Outreach Sender)
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
from agents import SenderAgent

def main():
    parser = argparse.ArgumentParser(description="Esecuzione Standalone Agente Speditore (Outreach)")
    parser.add_argument("--input", type=str, required=True, help="Path file CSV o JSON con i messaggi generati")
    parser.add_argument("--output", type=str, required=True, help="Path file CSV o JSON di output con lo stato degli invii")
    parser.add_argument("--city", type=str, default="Generica", help="Città del lotto di invio")
    parser.add_argument("--wa-limit", type=int, default=15, help="Limite giornaliero invio WhatsApp")
    parser.add_argument("--email-limit", type=int, default=25, help="Limite giornaliero invio Email")
    args = parser.parse_args()

    # Legge i messaggi
    messages = []
    if args.input.endswith(".json"):
        with open(args.input, "r", encoding="utf-8") as f:
            messages = json.load(f)
    elif args.input.endswith(".csv"):
        with open(args.input, "r", encoding="utf-8") as f:
            r = csv.DictReader(f)
            # Reconstruct structured objects if flattened fields exist
            for row in r:
                m = dict(row)
                if "email1_oggetto" in m or "email1_corpo" in m:
                    m["email1"] = {
                        "oggetto_a": m.pop("email1_oggetto", ""),
                        "corpo": m.pop("email1_corpo", "")
                    }
                if "gancio_scelto_num" in m or "gancio_scelto_nome" in m:
                    m["gancio_scelto"] = {
                        "numero": int(m.pop("gancio_scelto_num", 1)),
                        "nome": m.pop("gancio_scelto_nome", "")
                    }
                messages.append(m)
    else:
        print("[-] Errore: formato file non supportato (usa .csv o .json)")
        sys.exit(1)

    event_bus = EventBus()
    agent = SenderAgent(event_bus, daily_whatsapp_limit=args.wa_limit, daily_email_limit=args.email_limit)
    
    # Esegue l'invio
    print(f"[*] Avvio spedizione per {len(messages)} messaggi...")
    sent = agent.send_outreach(messages, city=args.city)
    
    # Salva l'output
    if sent:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        if args.output.endswith(".json"):
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(sent, f, ensure_ascii=False, indent=2)
        else:
            fieldnames = list(sent[0].keys())
            with open(args.output, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                w.writeheader()
                w.writerows(sent)
        print(f"[+] Spedizione completata. Salvati {len(sent)} record in {args.output}")
    else:
        print("[-] Nessun messaggio inviato.")

if __name__ == "__main__":
    main()
