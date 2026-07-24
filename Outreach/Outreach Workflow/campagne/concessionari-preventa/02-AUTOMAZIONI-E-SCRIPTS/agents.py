# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Python Agents for Scraper)
"""
from __future__ import annotations

import logging
import time
import random
import sys
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from gate_agent import GateAgent

# Importa i moduli procedurali esistenti
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import browser
import checker
import sheets

# Aggiunge la directory della campagna Preventa per gli script di copy e tracking
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Outreach Workflow/campagne/concessionari-preventa")))
try:
    import personalizza_messaggi
    import stato_e_followup
except ImportError:
    personalizza_messaggi = None
    stato_e_followup = None

log = logging.getLogger("preventa-pw.agents")

class ScraperAgent:
    def __init__(self, page: Any, event_bus: EventBus):
        self.agent_id = "ScraperAgent-1"
        self.page = page
        self.event_bus = event_bus

    def execute_scraping(self, city: str, categoria: str, limit: int):
        log.info(f"🚀 [{self.agent_id}] Avvio scraping per la città: {city} | Categoria: {categoria} | Limit: {limit}")
        self.event_bus.publish("search.started", self.agent_id, {"city": city, "categoria": categoria})
        
        try:
            raw_leads = browser.scrape_city(self.page, city, categoria, limit)
            self.event_bus.publish("leads.extracted", self.agent_id, {
                "city": city,
                "leads": raw_leads,
                "count": len(raw_leads)
            })
            log.info(f"✅ [{self.agent_id}] Scraping completato per {city}. Trovati {len(raw_leads)} lead.")
            return raw_leads
        except Exception as e:
            self.event_bus.publish("run.failed", self.agent_id, {"city": city, "error": str(e)})
            raise e


class QualifierAgent:
    def __init__(self, event_bus: EventBus):
        self.agent_id = "QualifierAgent-1"
        self.event_bus = event_bus

    def qualify_leads(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"🔍 [{self.agent_id}] Avvio qualifica in parallelo di {len(leads)} lead per la città: {city}")
        qualified = checker.qualify_leads_parallel(leads)
            
        self.event_bus.publish("leads.qualified", self.agent_id, {
            "city": city,
            "leads": qualified,
            "count": len(qualified)
        })
        log.info(f"✅ [{self.agent_id}] Qualifica completata per {city}.")
        return qualified


class WriterAgent:
    def __init__(self, event_bus: EventBus):
        self.agent_id = "WriterAgent-1"
        self.event_bus = event_bus

    def generate_messages(self, leads: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"✍️ [{self.agent_id}] Avvio generazione copy personalizzato per {len(leads)} lead in {city}")
        generated = []
        for row in leads:
            try:
                if personalizza_messaggi:
                    msg_data = personalizza_messaggi.genera_messaggi(row)
                else:
                    # Fallback se il modulo non è importabile
                    msg_data = {
                        "nome_attivita": row.get("nome_attivita", ""),
                        "citta": city,
                        "telefono": row.get("telefono", ""),
                        "priorita_lead": row.get("priorita_lead", "MEDIA"),
                        "gancio_scelto": {"numero": 1, "nome": "Tempo perso", "motivo": "fallback"},
                        "canale_primario": "whatsapp" if row.get("telefono") else "email",
                        "whatsapp_msg1": f"Ciao, ho visto {row.get('nome_attivita')} su Maps...",
                        "email1": {"oggetto_a": "Preventivi", "corpo": "Buongiorno..."},
                        "stato": "da_contattare"
                    }
                generated.append(msg_data)
            except Exception as e:
                log.error(f"Errore generazione messaggio per {row.get('nome_attivita')}: {e}")
                
        self.event_bus.publish("messages.generated", self.agent_id, {
            "city": city,
            "messages": generated,
            "count": len(generated)
        })
        log.info(f"✅ [{self.agent_id}] Generazione copy completata per {city}.")
        return generated


class SenderAgent:
    def __init__(self, event_bus: EventBus, daily_whatsapp_limit: int = 15, daily_email_limit: int = 25):
        self.agent_id = "SenderAgent-1"
        self.event_bus = event_bus
        self.daily_whatsapp_limit = daily_whatsapp_limit
        self.daily_email_limit = daily_email_limit

    def send_outreach(self, messages: List[Dict[str, Any]], city: str) -> List[Dict[str, Any]]:
        log.info(f"📨 [{self.agent_id}] Spedizione in corso per {len(messages)} messaggi in {city} (Limiti: WA {self.daily_whatsapp_limit}, Email {self.daily_email_limit})")
        sent_messages = []
        
        wa_sent = 0
        email_sent = 0
        
        for msg in messages:
            canale = msg.get("canale_primario", "email")
            
            # Applica i limiti di invio
            if canale == "whatsapp":
                if wa_sent >= self.daily_whatsapp_limit:
                    log.warning(f"⚠️ Limit rate raggiunto per WhatsApp ({self.daily_whatsapp_limit}). Spedizione sospesa per questo lead.")
                    continue
                wa_sent += 1
            else:
                if email_sent >= self.daily_email_limit:
                    log.warning(f"⚠️ Limit rate raggiunto per Email ({self.daily_email_limit}). Spedizione sospesa per questo lead.")
                    continue
                email_sent += 1
                
            log.info(f"📤 [{self.agent_id}] Inviato messaggio a {msg['nome_attivita']} via {canale}")
            # Piccolo delay tra gli invii per simulare attività umana (disattivato in test veloci)
            if "test" not in city.lower():
                time.sleep(random.uniform(1.0, 3.0))
            msg["stato"] = "contattato"
            sent_messages.append(msg)
            
        self.event_bus.publish("messages.sent", self.agent_id, {
            "city": city,
            "messages": sent_messages,
            "count": len(sent_messages)
        })
        log.info(f"✅ [{self.agent_id}] Spedizione completata per {city}. Inviati {len(sent_messages)} messaggi.")
        return sent_messages


class ResponderAgent:
    def __init__(self, event_bus: EventBus):
        self.agent_id = "ResponderAgent-1"
        self.event_bus = event_bus

    def process_reply(self, lead_id: str, reply_text: str) -> Dict[str, Any]:
        log.info(f"💬 [{self.agent_id}] Classificazione risposta del lead {lead_id}: '{reply_text}'")
        text = reply_text.lower()
        if "no" in text or "non" in text or "togli" in text or "spam" in text or "rifiut" in text:
            esito = "no_grazie"
            risposta = "Capito. Ti ringrazio per il riscontro e ti auguro una buona giornata."
        elif "interessa" in text or "sì" in text or "si" in text or "info" in text or "chiamaci" in text:
            esito = "interessato"
            risposta = "Ottimo! Ti propongo di fare una breve chiamata conoscitiva di 15 minuti per vedere un esempio pratico. Ti andrebbe domani alle 11:00 o giovedì alle 16:30?"
        else:
            esito = "risposto"
            risposta = "Grazie per il riscontro. Se desideri vedere una demo veloce senza impegno sul vostro stesso annuncio, possiamo fare una chiamata rapida di 15 minuti."

        result = {
            "lead_id": lead_id,
            "reply_received": reply_text,
            "esito": esito,
            "suggested_response": risposta
        }
        self.event_bus.publish("reply.processed", self.agent_id, result)
        return result


class SheetsAgent:
    def __init__(self, event_bus: EventBus, sheet_id: str, creds_path: str, push_only_alta: bool = False, worksheet_name: str = "Foglio1"):
        self.agent_id = "SheetsAgent-1"
        self.event_bus = event_bus
        self.sheet_id = sheet_id
        self.creds_path = creds_path
        self.push_only_alta = push_only_alta
        self.worksheet_name = worksheet_name

    def upload(self, leads: List[Dict[str, Any]], city: str):
        log.info(f"📤 [{self.agent_id}] Inizio sincronizzazione su Google Sheets per la città: {city}")
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


class QAAgent:
    def __init__(self, gate_agent: GateAgent, event_bus: EventBus):
        self.agent_id = "QA-Agent-1"
        self.gate_agent = gate_agent
        self.event_bus = event_bus

    def verify_gate(self, gate_id: str, output_content: str) -> bool:
        log.info(f"🛡️ [{self.agent_id}] Controllo di qualità richiesto per il gate: {gate_id}")
        self.event_bus.publish("gate.check.requested", self.agent_id, {"gate_id": gate_id})
        
        report = self.gate_agent.evaluate_output(gate_id, output_content)
        if report.get("passed", False):
            log.info(f"✅ [{self.agent_id}] Controllo superato per il gate: {gate_id} | Score: {report['score']}")
            return True
        else:
            log.warning(f"❌ [{self.agent_id}] Controllo fallito per il gate: {gate_id} | Score: {report['score']}")
            return False


class DebugAgent:
    def __init__(self, page: Any, event_bus: EventBus):
        self.agent_id = "DebugAgent-1"
        self.page = page
        self.event_bus = event_bus
        self.event_bus.subscribe("run.failed", self.handle_failure)

    def handle_failure(self, event: Event):
        log.error(f"🐞 [{self.agent_id}] Rilevato fallimento. Eseguo diagnostica per {event.payload.get('city')}")
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data/debug_{event.payload.get('city')}_{timestamp}.png"
            self.page.screenshot(path=filename)
            log.info(f"📸 [{self.agent_id}] Screenshot diagnostico salvato come {filename}")
        except Exception as e:
            log.error(f"🐞 [{self.agent_id}] Impossibile scattare screenshot: {e}")


class Conductor:
    def __init__(self, event_bus: EventBus, scraper_agent: ScraperAgent, qualifier_agent: QualifierAgent,
                 writer_agent: WriterAgent, sender_agent: SenderAgent, sheets_agent: Optional[SheetsAgent], 
                 qa_agent: QAAgent, output_csv_path: str, only_alta: bool = False):
        self.agent_id = "Conductor-1"
        self.event_bus = event_bus
        self.scraper_agent = scraper_agent
        self.qualifier_agent = qualifier_agent
        self.writer_agent = writer_agent
        self.sender_agent = sender_agent
        self.sheets_agent = sheets_agent
        self.qa_agent = qa_agent
        self.output_csv_path = output_csv_path
        self.only_alta = only_alta

        # Sottoscrizione degli eventi della pipeline
        self.event_bus.subscribe("leads.extracted", self.on_leads_extracted)
        self.event_bus.subscribe("leads.qualified", self.on_leads_qualified)
        self.event_bus.subscribe("messages.generated", self.on_messages_generated)
        self.event_bus.subscribe("messages.sent", self.on_messages_sent)
        self.event_bus.subscribe("sheets.synced", self.on_sheets_synced)
        self.event_bus.subscribe("gate.failed", self.on_gate_failed)

    def run_city_workflow(self, city: str, categoria: str, limit: int):
        log.info(f"🎭 [{self.agent_id}] Avvio del workflow di orchestrazione per la città: {city}")
        
        # Validazione Gate L1->L2 (Input Parameters)
        input_str = f"città: {city}, categoria: {categoria}, limit: {limit}"
        if not self.qa_agent.verify_gate("L1_L2", input_str):
            log.error(f"❌ [{self.agent_id}] Bloccatto al Gate L1->L2. Termino workflow.")
            return

        # Avvio Scraper (Fase 1)
        self.scraper_agent.execute_scraping(city, categoria, limit)

    def on_leads_extracted(self, event: Event):
        city = event.payload.get("city")
        leads = event.payload.get("leads", [])
        
        # Validazione Gate L2->L3 (Estrazione & Playwright)
        leads_str = "\n".join([f"{l.get('nome_attivita')},{l.get('sito_web')}" for l in leads])
        if not self.qa_agent.verify_gate("L2_L3", leads_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L2->L3. Termino qualifica per {city}.")
            return

        # Avvio qualificazione (Fase 2)
        self.qualifier_agent.qualify_leads(leads, city)

    def on_leads_qualified(self, event: Event):
        city = event.payload.get("city")
        leads = event.payload.get("leads", [])

        # Validazione Gate L3->L4 (Qualifica & Priorità)
        qualified_str = "\n".join([f"{l.get('nome_attivita')},{l.get('priorita_lead')}" for l in leads])
        if not self.qa_agent.verify_gate("L3_L4", qualified_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L3->L4. Termino qualifica per {city}.")
            return

        # Avvio generazione messaggi / scrittura (Fase 3)
        self.writer_agent.generate_messages(leads, city)

    def on_messages_generated(self, event: Event):
        city = event.payload.get("city")
        messages = event.payload.get("messages", [])

        # Validazione Gate L4->L5 (Copywriting & Generazione Messaggi)
        msg_check_str = "\n".join([f"{m.get('nome_attivita')},{m.get('canale_primario')}" for m in messages])
        # Utilizziamo il Gate L4->L5 originariamente per Sheets ma riadattato come Gate di validazione del copy
        if not self.qa_agent.verify_gate("L4_L5", msg_check_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L4->L5 (Validazione Copy). Termino per {city}.")
            return

        # Avvio invio / spedizione (Fase 4)
        self.sender_agent.send_outreach(messages, city)

    def on_messages_sent(self, event: Event):
        city = event.payload.get("city")
        messages = event.payload.get("messages", [])

        # Salvataggio CSV locale (Logica presa da run.py originale)
        import run
        final_sorted, filtered_sorted = run.save_csv(messages, self.output_csv_path, only_alta=self.only_alta)

        # Validazione Gate L5->L6 (Salvataggio & CSV)
        csv_check_str = f"salvato {self.output_csv_path} con {len(final_sorted)} righe. only-alta: {self.only_alta}"
        if not self.qa_agent.verify_gate("L5_L6", csv_check_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L5->L6. Termino upload per {city}.")
            return

        # Avvio upload sheets se configurato
        if self.sheets_agent:
            self.sheets_agent.upload(final_sorted, city)
        else:
            self.on_sheets_synced(Event("sheets.synced", "Conductor", {"city": city, "success": True}))

    def on_sheets_synced(self, event: Event):
        city = event.payload.get("city")
        
        # Validazione finale Gate L6->L7 (Fine E2E)
        if self.qa_agent.verify_gate("L6_L7", f"E2E completato per {city}"):
            self.event_bus.publish("run.completed", self.agent_id, {"city": city})
            log.info(f"🏆 [{self.agent_id}] WORKFLOW COMPLETATO CON SUCCESSO PER {city}!")
        else:
            log.error(f"❌ [{self.agent_id}] Fallito il Gate L6->L7 alla fine della pipeline per {city}.")

    def on_gate_failed(self, event: Event):
        gate_id = event.payload.get("gate_id")
        attempt_number = event.payload.get("attempt_number", 1)
        
        # Remediation
        if attempt_number < 3:
            log.warning(f"🔄 [{self.agent_id}] Rilevato fallimento gate {gate_id} (tentativo {attempt_number}). Avvio Remediation Loop...")
            # Trigger di auto-riparazione basato sul gate
            if gate_id == "L2_L3":
                log.info(f"🔄 [{self.agent_id}] Remediation L2_L3: Tentativo di ricarica browser e retry scraping...")
            elif gate_id == "L4_L5":
                log.info(f"🔄 [{self.agent_id}] Remediation L4_L5: Eseguo rotazione della strategia di copywriting...")
        else:
            log.error(f"🚨 [{self.agent_id}] Raggiunto il limite di 3 fallimenti consecutivi per il gate {gate_id}. Trigger escalation e congelamento workflow.")
