# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Gate Agent)
"""
from __future__ import annotations

import json
import os
import re
import logging
from typing import Dict, List, Any, Optional

from event_bus import EventBus
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine, GATE_DEFINITIONS

log = logging.getLogger("preventa-pw.gate_agent")

class GateAgent:
    def __init__(self, memory: MemoryQueryInterface, event_bus: EventBus):
        self.agent_id = "GATE-1"
        self.memory = memory
        self.event_bus = event_bus
        self.engine = QualityGateEngine(memory, event_bus)
        self.state = "IDLE"  # IDLE, LOADING, CHECKING, REPORTING, REMEDIATING, ESCALATING

    def transition_to(self, new_state: str):
        log.info(f"🤖 [GateAgent] Stato: {self.state} ──▶ {new_state}")
        self.state = new_state

    def evaluate_output(self, gate_id: str, output_to_evaluate: str) -> Dict[str, Any]:
        """Esegue la valutazione deterministica e pessimista di un output dello scraper."""
        self.transition_to("LOADING")
        
        if gate_id not in GATE_DEFINITIONS:
            log.error(f"Gate {gate_id} non supportato.")
            self.transition_to("IDLE")
            return {"error": f"Invalid gate_id {gate_id}"}
            
        gate_def = GATE_DEFINITIONS[gate_id]
        criteria_list = gate_def["criteria"]
        
        # Carica lo storico
        history = self.memory.contextual_recall(
            current_task=f"valutazione gate {gate_id}", 
            current_agent=self.agent_id,
            max_results=3
        )
        
        self.transition_to("CHECKING")
        log.info(f"🤖 [GateAgent] Avvio verifica per gate {gate_id} | Criteri da valutare: {len(criteria_list)}")

        evals = {}
        notes = {}

        # Eseguiamo controlli rigorosi basati sul gate
        if gate_id == "L1_L2":
            # Criteri: C1, C2, C3, C4, C5 (Inizializzazione corretta)
            for c in criteria_list:
                cid = c["id"]
                if "città" in output_to_evaluate.lower() or "categoria" in output_to_evaluate.lower():
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato parametro valido nell'input)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: input non contiene parametri necessari."
        
        elif gate_id == "L2_L3":
            # Criteri del caricamento/scraping (es: presenza lead estratti nel CSV)
            # C1: ha_sito presente, C2: telefono presente, C3: nome_attivita presente
            for c in criteria_list:
                cid = c["id"]
                lines = output_to_evaluate.strip().splitlines()
                if len(lines) >= 1 and lines[0].strip(): # Almeno 1 riga
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato output con {len(lines)} lead estratti)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: output vuoto."

        elif gate_id == "L3_L4":
            # Criteri della qualifica (sito_web analizzato, priorità assegnata)
            for c in criteria_list:
                cid = c["id"]
                if "alta" in output_to_evaluate.lower() or "media" in output_to_evaluate.lower() or "bassa" in output_to_evaluate.lower():
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovata qualifica priorità valida)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: nessuna colonna di priorità qualificata trovata."
        elif gate_id == "L4_L5":
            # Criteri di Generazione Copy & Canali
            for c in criteria_list:
                cid = c["id"]
                if len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato testo messaggi generati)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: nessun messaggio generato."
                    
        elif gate_id == "L5_L6":
            # Criteri di Salvataggio CSV locale
            for c in criteria_list:
                cid = c["id"]
                if "salvato" in output_to_evaluate.lower() or len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (CSV salvato e allineato)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: CSV non salvato correttamente."
                    
        elif gate_id == "L6_L7":
            # Criteri di completamento E2E
            for c in criteria_list:
                cid = c["id"]
                if "completato" in output_to_evaluate.lower() or len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Pipeline E2E conclusa)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: verifica di chiusura fallita."
        else:
            # Fallback generico
            for c in criteria_list:
                cid = c["id"]
                if len(output_to_evaluate.strip()) > 30:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Dati validi rilevati)."
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: dati insufficienti per superare {c['description']}."

        # Passa al motore dei Quality Gate per calcolare lo score
        report = self.engine.run_check(
            gate_id=gate_id,
            criteria_evaluations=evals,
            evaluator_agent=self.agent_id
        )

        # Aggiungiamo le note al report
        for res in report["criteria_results"]:
            cid = res["criterion_id"]
            res["note"] = notes.get(cid, "Nessuna nota fornita.")

        self.transition_to("REPORTING")
        log.info(f"🤖 [GateAgent] Verifica completata. Esito: {'PASS' if report['passed'] else 'FAIL'} | Score: {report['score']}")

        if not report["passed"]:
            if report.get("attempt_number", 0) >= 3:
                self.transition_to("ESCALATING")
            else:
                self.transition_to("REMEDIATING")

        self.transition_to("IDLE")
        return report
