#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Campaign Outreach Runner (G-A4)

Loads qualified leads from CSV, generates personalized copy using the campaign modules,
simulates sending the first touchpoint, and records the contacted state in the memory database.
"""
import os
import sys
import csv
import json
import time
import random
from datetime import datetime
from pathlib import Path

# Aggiunge i percorsi necessari al path di sistema
SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "02-AUTOMAZIONI-E-SCRIPTS")
sys.path.append(SCRIPTS_DIR)

CAMPAIGN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Outreach Workflow/campagne/concessionari-preventa"))
sys.path.append(CAMPAIGN_DIR)

from memory import MemoryQueryInterface
import areus
import personalizza_messaggi

def main():
    print("🎬 Inizializzazione Outreach Runner per concessionari...")
    
    # Path dei file
    input_csv = "data/leads_concessionari.csv"
    output_report_json = "data/report_contatti.json"
    memory_db_path = "data/memory_db.json"
    
    if not os.path.exists(input_csv):
        print(f"❌ Errore: File dei lead non trovato in {input_csv}. Esegui prima lo scraper.")
        sys.exit(1)
        
    # Inizializza l'interfaccia di memoria
    memory = MemoryQueryInterface(memory_filepath=memory_db_path)
    
    # Legge i lead da CSV
    leads = []
    with open(input_csv, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
            
    print(f"📖 Letti {len(leads)} lead da {input_csv}.")
    
    report_contatti = []
    contatti_effettuati = 0
    
    print("\n--- INIZIO SPEDIZIONE OUTREACH ---")
    for i, lead in enumerate(leads):
        nome = lead.get("nome_attivita", "").strip()
        telefono = lead.get("telefono", "").strip()
        priorita = lead.get("priorita_lead", "BASSA").strip()
        
        # Filtriamo per priorità ALTA e MEDIA (le BASSA sono già digitalizzate e non richiedono pitch)
        if priorita not in ("ALTA", "MEDIA"):
            print(f"⏭️ Salto {nome} (Priorità: {priorita} - già digitalizzato)")
            continue
            
        print(f"\n[{i+1}/{len(leads)}] Elaborazione lead: {nome} (Priorità: {priorita})")
        
        # 1. Generazione Copy
        msg_data = personalizza_messaggi.genera_messaggi(lead)
        
        canale = msg_data.get("canale_primario", "email")
        destinatario = telefono if canale == "whatsapp" else lead.get("sito_web", "Email form")
        
        # 2. Simulazione Invio
        print(f"📤 [SenderAgent-1] Invio in corso via {canale.upper()} a {destinatario}...")
        
        if canale == "whatsapp":
            print(f"   [Testo WhatsApp]: {msg_data['whatsapp_msg1']}")
        else:
            print(f"   [Oggetto Email]: {msg_data['email1']['oggetto_a']}")
            print(f"   [Corpo Email]: {msg_data['email1']['corpo']}")
            
        # Simula il ritardo di invio umano
        time.sleep(random.uniform(1.0, 2.5))
        
        # 3. Aggiorna lo stato nel record di contatto
        msg_data["stato"] = "contattato"
        msg_data["data_primo_contatto"] = datetime.utcnow().strftime("%Y-%m-%d")
        msg_data["ultimo_step_inviato"] = "msg1"
        msg_data["data_ultimo_invio"] = datetime.utcnow().strftime("%Y-%m-%d")
        
        # 4. Scrive il lead nella memoria persistente per consentire il loop di ottimizzazione
        lead_key = personalizza_messaggi.normalizza_telefono(telefono) or nome.lower().strip()
        memory.write_lead(lead_key, msg_data, author="outreach_runner")

        # Aggiorna lo stage in Areus (CRM EmpireDesk): freddo -> contattato
        if telefono:
            areus.mark_contacted(telefono, canale=canale)

        report_contatti.append(msg_data)
        contatti_effettuati += 1
        print(f"✅ Messaggio inviato con successo a {nome}!")
        
    print("\n--- FINE SPEDIZIONE OUTREACH ---")
    
    # 5. Salva il report contatti
    with open(output_report_json, "w", encoding="utf-8") as f:
        json.dump(report_contatti, f, ensure_ascii=False, indent=4)
        
    print(f"\n💾 Report contatti salvato in: {output_report_json}")
    print(f"📊 Totale contatti effettuati: {contatti_effettuati}")
    
    # Stampa tabella riassuntiva per log
    print("\nRIEPILOGO CONTATTI:")
    print(f"{'Nome Attività':<40} | {'Canale':<10} | {'Gancio':<25} | {'Stato':<12}")
    print("-" * 95)
    for c in report_contatti:
        print(f"{c['nome_attivita'][:38]:<40} | {c['canale_primario']:<10} | {c['gancio_scelto']['nome'][:23]:<25} | {c['stato']:<12}")

if __name__ == "__main__":
    main()
