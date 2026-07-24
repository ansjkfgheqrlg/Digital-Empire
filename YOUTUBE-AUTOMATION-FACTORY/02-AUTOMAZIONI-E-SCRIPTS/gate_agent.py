# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 GATE-1 Agent (Plan 1)
"""
from __future__ import annotations

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

from event_bus import EventBus, Event
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine

log = logging.getLogger("preventa-pw.gate_agent")

class GateAgent:
    def __init__(self, event_bus: EventBus, memory: MemoryQueryInterface):
        self.agent_id = "GATE-1"
        self.event_bus = event_bus
        self.memory = memory
        self.engine = QualityGateEngine()
        
        # Gestione dello stato dell'agente (L5)
        self.state = "IDLE"  # IDLE, LOADING, CHECKING, REPORTING, REMEDIATING, ESCALATING
        self.failures_count: Dict[str, int] = {}
        
        # Iscrizione alla richiesta di controllo del gate
        self.event_bus.subscribe("gate.check.requested", self.on_check_requested)

    def transition_to(self, new_state: str):
        log.info(f"🤖 [{self.agent_id}] Stato: {self.state} ──▶ {new_state}")
        self.state = new_state

    def verify_gate(self, gate_id: str, content: str) -> bool:
        """Metodo di validazione sincrono."""
        self.transition_to("LOADING")
        self.transition_to("CHECKING")
        
        passed, score, reasons = self.engine.evaluate_gate(gate_id, content)
        
        self.transition_to("REPORTING")
        
        # Costruzione report
        attempt = self.failures_count.get(gate_id, 0)
        if not passed:
            attempt += 1
            self.failures_count[gate_id] = attempt
        else:
            self.failures_count[gate_id] = 0  # Resetta i tentativi falliti su successo

        report = {
            "gate_id": gate_id,
            "passed": passed,
            "score": score,
            "attempt_number": attempt,
            "reasons": reasons,
            "threshold": 1.0 if gate_id != "L5_L6" else 0.7
        }

        # Scrive nella memoria
        self.memory.log_decision(
            decision_id=f"DEC-{gate_id}-{int(datetime.now().timestamp())}",
            decision=f"Esito Gate {gate_id}: {'PASS' if passed else 'FAIL'}",
            reason=f"Verifica dei criteri completata con score {score}. " + (f"Rilevati errori: {', '.join(reasons)}" if not passed else "Nessuna anomalia."),
            rejected=[],
            confidence=score
        )

        if passed:
            self.event_bus.publish(
                event_type="gate.passed",
                publisher=self.agent_id,
                payload=report
            )
            self.transition_to("IDLE")
            log.info(f"✅ [{self.agent_id}] Controllo superato per il gate: {gate_id} | Score: {score}")
            return True
        else:
            self.event_bus.publish(
                event_type="gate.failed",
                publisher=self.agent_id,
                payload=report
            )
            
            if attempt >= 3:
                self.transition_to("ESCALATING")
                self._escalate(gate_id, report)
            else:
                self.transition_to("REMEDIATING")
                self.transition_to("IDLE")
                
            log.warning(f"❌ [{self.agent_id}] Controllo fallito per il gate: {gate_id} | Tentativo {attempt} | Score: {score}")
            return False

    def on_check_requested(self, event: Event):
        gate_id = event.payload.get("gate_id")
        content = event.payload.get("content")
        if gate_id and content is not None:
            self.verify_gate(gate_id, content)

    def _escalate(self, gate_id: str, report: Dict[str, Any]):
        """Esegue il protocollo di escalation in caso di 3 fallimenti consecutivi."""
        log.warning(f"🚨 [{self.agent_id}] [Escalation] Il gate {gate_id} ha fallito {report['attempt_number']} volte consecutive!")
        diagnosis = f"Tentativo fallito per punteggio {report['score']} inferiore alle regole strutturali."
        
        self.event_bus.publish(
            event_type="gate.escalated",
            publisher=self.agent_id,
            payload={
                "gate_id": gate_id,
                "total_attempts": report["attempt_number"],
                "diagnosis": diagnosis,
                "recommended_strategy_change": "Ricalibra parametri input o controlla Fliki / Script"
            },
            delivery_mode="EXACTLY_ONCE"
        )
