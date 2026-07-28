# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Python Agents - Facade Layer)

ARCHITETTURA:
  Questo modulo è il punto di ingresso ufficiale per tutti gli agenti APEX-7.
  Ogni classe eredita dall'implementazione canonica presente in 03-AGENTI-E-RUOLI/
  e aggiunge esclusivamente la logica di orchestrazione del Conductor.

  NON duplicare logica qui: ogni cambiamento al comportamento di un agente
  va effettuato nel rispettivo file 03-AGENTI-E-RUOLI/agente_*.py.
"""
from __future__ import annotations

import importlib.util
import logging
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from gate_agent import GateAgent
from meta_optimization import MetaOptimizer

# Directory degli agenti ufficiali (pattern cartella-per-agente, es. 03-AGENTI-E-RUOLI/writer/agente.py)
_AGENTS_DIR = Path(os.path.dirname(__file__)).parent / "03-AGENTI-E-RUOLI"


def _load_agente(folder_name: str, module_name: str):
    """Carica <folder_name>/agente.py come modulo con nome unico (evita collisioni: ogni
    cartella ha un file chiamato identicamente 'agente.py')."""
    path = _AGENTS_DIR / folder_name / "agente.py"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


# --- Import delle implementazioni ufficiali da 03-AGENTI-E-RUOLI (cartella-per-agente) ---
ScraperAgent = _load_agente("scraper", "agente_scraper").ScraperAgent
QualifierAgent = _load_agente("qualificatore", "agente_qualificatore").QualifierAgent
WriterAgent = _load_agente("writer", "agente_writer").WriterAgent
SenderAgent = _load_agente("sender", "agente_sender").SenderAgent
ResponderAgent = _load_agente("responder", "agente_responder").ResponderAgent
SheetsAgent = _load_agente("integratore-sheets", "agente_integratore_sheets").SheetsAgent
OfficialGateAgent = _load_agente("gate", "agente_gate").GateAgent

log = logging.getLogger("preventa-pw.agents")


class QAAgent:
    """
    Wrapper di orchestrazione che delega le valutazioni di qualità al GateAgent ufficiale.
    Non implementa logica propria: è un adattatore per il Conductor.
    """
    def __init__(self, gate_agent: GateAgent, event_bus: EventBus):
        self.agent_id = "QA-Agent-1"
        self.gate_agent = gate_agent
        self.event_bus = event_bus

    def verify_gate(self, gate_id: str, output_content: str) -> bool:
        log.info(f"🛡️ [{self.agent_id}] Controllo di qualità richiesto per il gate: {gate_id}")
        self.event_bus.publish("gate.check.requested", self.agent_id, {"gate_id": gate_id})

        report = self.gate_agent.evaluate_output(gate_id, output_content)
        if report.get("passed", False):
            log.info(f"✅ [{self.agent_id}] Gate {gate_id} superato | Score: {report['score']}")
            return True
        else:
            log.warning(f"❌ [{self.agent_id}] Gate {gate_id} fallito | Score: {report['score']}")
            return False


class DebugAgent:
    """
    Agente di diagnostica che intercetta gli eventi run.failed e cattura screenshot Playwright.
    """
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
    """
    Orchestratore principale della pipeline APEX-7.
    Coordina il flusso: Scraper → Qualifier → Writer → Sender → Sheets → Gate E2E.
    Implementa il pattern event-driven: ogni fase reagisce all'evento pubblicato da quella precedente.
    """
    def __init__(self, event_bus: EventBus, scraper_agent: ScraperAgent, qualifier_agent: QualifierAgent,
                 sheets_agent: Optional[SheetsAgent], qa_agent: QAAgent, output_csv_path: str,
                 writer_agent: Optional[WriterAgent] = None, sender_agent: Optional[SenderAgent] = None,
                 meta_optimizer: Optional[MetaOptimizer] = None, only_alta: bool = False):
        self.agent_id = "Conductor-1"
        self.event_bus = event_bus
        self.scraper_agent = scraper_agent
        self.qualifier_agent = qualifier_agent
        self.writer_agent = writer_agent
        self.sender_agent = sender_agent
        self.sheets_agent = sheets_agent
        self.qa_agent = qa_agent
        self.meta_optimizer = meta_optimizer
        self.output_csv_path = output_csv_path
        self.only_alta = only_alta
        self.all_rows: List[Dict[str, Any]] = []

        # Sottoscrizione degli eventi della pipeline
        self.event_bus.subscribe("leads.extracted", self.on_leads_extracted)
        self.event_bus.subscribe("leads.qualified", self.on_leads_qualified)
        self.event_bus.subscribe("messages.generated", self.on_messages_generated)
        self.event_bus.subscribe("messages.sent", self.on_messages_sent)
        self.event_bus.subscribe("sheets.synced", self.on_sheets_synced)
        self.event_bus.subscribe("gate.failed", self.on_gate_failed)

    def run_city_workflow(self, city: str, categoria: str, limit: int):
        log.info(f"🎭 [{self.agent_id}] Avvio del workflow di orchestrazione per la città: {city}")

        # Validazione Gate L1→L2 (Input Parameters)
        input_str = f"città: {city}, categoria: {categoria}, limit: {limit}"
        if not self.qa_agent.verify_gate("L1_L2", input_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L1→L2. Termino workflow.")
            return

        # Avvio Scraper (Fase 1)
        self.scraper_agent.execute_scraping(city, categoria, limit)

    def on_leads_extracted(self, event: Event):
        city = event.payload.get("city")
        leads = event.payload.get("leads", [])

        # Validazione Gate L2→L3 (Estrazione & Playwright)
        leads_str = "\n".join([f"{l.get('nome_attivita')},{l.get('sito_web')}" for l in leads])
        if not self.qa_agent.verify_gate("L2_L3", leads_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L2→L3. Termino qualifica per {city}.")
            return

        # Avvio qualificazione (Fase 2)
        self.qualifier_agent.qualify_leads(leads, city)

    def on_leads_qualified(self, event: Event):
        city = event.payload.get("city")
        leads = event.payload.get("leads", [])

        # Validazione Gate L3→L4 (Qualifica & Priorità)
        qualified_str = "\n".join([f"{l.get('nome_attivita')},{l.get('priorita_lead')}" for l in leads])
        if not self.qa_agent.verify_gate("L3_L4", qualified_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L3→L4. Termino per {city}.")
            return

        if self.writer_agent and self.sender_agent:
            self.writer_agent.generate_messages(leads, city)
        else:
            log.info(f"✉️ [{self.agent_id}] Nessun writer/sender configurato: salvo i lead qualificati per {city}.")
            self._finalize_and_save(leads, city)

    def on_messages_generated(self, event: Event):
        city = event.payload.get("city")
        messages = event.payload.get("messages", [])

        # Validazione Gate L4→L5 (Copywriting & Messaggi)
        msg_check_str = "\n".join([f"{m.get('nome_attivita')},{m.get('canale_primario')}" for m in messages])
        if not self.qa_agent.verify_gate("L4_L5", msg_check_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L4→L5 (Validazione Copy). Termino per {city}.")
            return

        # Avvio invio (Fase 4)
        self.sender_agent.send_outreach(messages, city)

    def on_messages_sent(self, event: Event):
        city = event.payload.get("city")
        messages = event.payload.get("messages", [])
        self._finalize_and_save(messages, city)

    def _finalize_and_save(self, rows: List[Dict[str, Any]], city: str):
        import run
        # Accumula tra le città: save_csv scrive in overwrite, quindi va richiamato sempre
        # con lo storico completo, altrimenti l'ultima città processata cancella le precedenti.
        self.all_rows.extend(rows)
        final_sorted, filtered_sorted = run.save_csv(self.all_rows, self.output_csv_path, only_alta=self.only_alta)

        # Validazione Gate L5→L6 (Salvataggio CSV)
        csv_check_str = f"salvato {self.output_csv_path} con {len(final_sorted)} righe. only-alta: {self.only_alta}"
        if not self.qa_agent.verify_gate("L5_L6", csv_check_str):
            log.error(f"❌ [{self.agent_id}] Bloccato al Gate L5→L6. Termino upload per {city}.")
            return

        if self.sheets_agent:
            self.sheets_agent.upload(final_sorted, city)
        else:
            self.on_sheets_synced(Event("sheets.synced", "Conductor", {"city": city, "success": True}))

    def on_sheets_synced(self, event: Event):
        city = event.payload.get("city")

        # Validazione finale Gate L6→L7 (Fine E2E)
        if self.qa_agent.verify_gate("L6_L7", f"E2E completato per {city}"):
            self.event_bus.publish("run.completed", self.agent_id, {"city": city})
            log.info(f"🏆 [{self.agent_id}] WORKFLOW COMPLETATO CON SUCCESSO PER {city}!")

            if self.meta_optimizer:
                try:
                    result = self.meta_optimizer.run_optimization_loop()
                    self.event_bus.publish("meta.optimized", self.agent_id, result)
                    log.info(f"📈 [{self.agent_id}] Ciclo di auto-miglioramento eseguito: {result.get('status')}")
                except Exception as e:
                    log.error(f"⚠️ [{self.agent_id}] Errore nel ciclo di meta-ottimizzazione: {e}")
        else:
            log.error(f"❌ [{self.agent_id}] Fallito il Gate L6→L7 alla fine della pipeline per {city}.")

    def on_gate_failed(self, event: Event):
        gate_id = event.payload.get("gate_id")
        attempt_number = event.payload.get("attempt_number", 1)

        if attempt_number < 3:
            log.warning(f"🔄 [{self.agent_id}] Fallimento gate {gate_id} (tentativo {attempt_number}). Avvio Remediation Loop...")
            if gate_id == "L2_L3":
                log.info(f"🔄 [{self.agent_id}] Remediation L2_L3: retry scraping con browser reload...")
            elif gate_id == "L4_L5":
                log.info(f"🔄 [{self.agent_id}] Remediation L4_L5: rotazione strategia copywriting...")
        else:
            log.error(f"🚨 [{self.agent_id}] Raggiunto limite 3 fallimenti per gate {gate_id}. Escalation workflow congelato.")
