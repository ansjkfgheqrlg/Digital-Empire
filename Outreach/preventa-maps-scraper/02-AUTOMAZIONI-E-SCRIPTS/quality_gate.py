# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Quality Gate System)
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

from event_bus import EventBus
from memory import MemoryQueryInterface

log = logging.getLogger("preventa-pw.quality_gate")

# Definizioni dei criteri per il ciclo di vita dello scraper Maps
GATE_DEFINITIONS = {
    "L1_L2": {
        "name": "Gate L1 -> L2 (Inizializzazione & Parametri)",
        "threshold": 1.0,  # 3/3
        "criteria": [
            {"id": "C1", "description": "Categoria di ricerca definita e non vuota"},
            {"id": "C2", "description": "Almeno una città di destinazione specificata"},
            {"id": "C3", "description": "Limite di risultati per città configurato correttamente"}
        ]
    },
    "L2_L3": {
        "name": "Gate L2 -> L3 (Estrazione & Playwright Scraper)",
        "threshold": 1.0,  # 3/3
        "criteria": [
            {"id": "C1", "description": "Il browser Playwright si è avviato senza blocchi"},
            {"id": "C2", "description": "I lead estratti contengono almeno Nome e Indirizzo"},
            {"id": "C3", "description": "Nessun captcha o blocco di rete ha interrotto il run"}
        ]
    },
    "L3_L4": {
        "name": "Gate L3 -> L4 (Qualificazione & Audit)",
        "threshold": 0.80,  # 4/5
        "criteria": [
            {"id": "C1", "description": "Presenza o assenza del sito web verificata"},
            {"id": "C2", "description": "Verifica del FB Pixel o Google Tag Manager eseguita"},
            {"id": "C3", "description": "Numero e media delle recensioni estratte e convertite"},
            {"id": "C4", "description": "Priorità (ALTA/MEDIA/BASSA) assegnata a ciascun lead"},
            {"id": "C5", "description": "Note di qualifica compilate in base allo score del sito"}
        ]
    },
    "L4_L5": {
        "name": "Gate L4 -> L5 (Integrazione & Google Sheets)",
        "threshold": 1.0,  # 3/3
        "criteria": [
            {"id": "C1", "description": "Connessione alle API di Google Sheets riuscita"},
            {"id": "C2", "description": "Deduplica dei telefoni eseguita con successo"},
            {"id": "C3", "description": "Nuove righe inserite correttamente nel foglio"}
        ]
    },
    "L5_L6": {
        "name": "Gate L5 -> L6 (Salvataggio & CSV)",
        "threshold": 1.0,  # 3/3
        "criteria": [
            {"id": "C1", "description": "File CSV locale salvato nel percorso configurato"},
            {"id": "C2", "description": "File leads_SOLO_ALTA.csv generato seonly-alta è True"},
            {"id": "C3", "description": "Dati ordinati con priorità ALTA per prima"}
        ]
    },
    "L6_L7": {
        "name": "Gate L6 -> L7 (APEX E2E Scraper Complete)",
        "threshold": 1.0,  # 4/4
        "criteria": [
            {"id": "C1", "description": "Tutti i moduli (Scraper, Qualifier, Sheets) hanno terminato con successo"},
            {"id": "C2", "description": "Tutti i gate di controllo intermedi superati"},
            {"id": "C3", "description": "I dati finali corrispondono alla specifica di schema"},
            {"id": "C4", "description": "Log di telemetria scritto in memoria senza errori non gestiti"}
        ]
    }
}

class QualityGateEngine:
    def __init__(self, memory: MemoryQueryInterface, event_bus: EventBus):
        self.memory = memory
        self.event_bus = event_bus
        self._gate_attempts: Dict[str, int] = {}

    def run_check(self, gate_id: str, criteria_evaluations: Dict[str, str], evaluator_agent: str) -> Dict[str, Any]:
        """Esegue la validazione dei criteri del gate corrente."""
        if gate_id not in GATE_DEFINITIONS:
            raise ValueError(f"Gate {gate_id} non definito.")

        definition = GATE_DEFINITIONS[gate_id]
        criteria_list = definition["criteria"]
        threshold = definition["threshold"]

        pass_count = 0.0
        partial_count = 0.0
        fail_count = 0.0
        criteria_results = []

        for crit in criteria_list:
            crit_id = crit["id"]
            eval_result = criteria_evaluations.get(crit_id, "FAIL").upper()
            
            if eval_result == "PASS":
                pass_count += 1
            elif eval_result == "PARTIAL":
                partial_count += 0.5
            else:
                fail_count += 1

            criteria_results.append({
                "criterion_id": crit_id,
                "description": crit["description"],
                "status": eval_result
            })

        total = len(criteria_list)
        score = (pass_count + partial_count) / total
        passed = score >= threshold

        self._gate_attempts[gate_id] = self._gate_attempts.get(gate_id, 0) + 1
        attempt_number = self._gate_attempts[gate_id]

        report = {
            "gate_id": gate_id,
            "gate_name": definition["name"],
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "score": round(score, 2),
            "threshold": threshold,
            "passed": passed,
            "attempt_number": attempt_number,
            "criteria_results": criteria_results,
            "evaluator": evaluator_agent
        }

        # Pubblica gli eventi sul bus
        if passed:
            self._gate_attempts[gate_id] = 0
            self.event_bus.publish(
                event_type="gate.passed",
                publisher=evaluator_agent,
                payload=report,
                delivery_mode="EXACTLY_ONCE"
            )
            self.memory.write(
                layer="decision_log",
                content={"type": "gate_check", "gate_id": gate_id, "outcome": "SUCCESS", "report": report},
                author=evaluator_agent,
                importance=0.8
            )
        else:
            self.event_bus.publish(
                event_type="gate.failed",
                publisher=evaluator_agent,
                payload=report,
                delivery_mode="EXACTLY_ONCE"
            )
            self.memory.write(
                layer="decision_log",
                content={"type": "gate_check", "gate_id": gate_id, "outcome": "FAIL", "report": report},
                author=evaluator_agent,
                importance=0.8
            )

            if attempt_number >= 3:
                self._escalate(gate_id, report, evaluator_agent)

        return report

    def _escalate(self, gate_id: str, report: Dict[str, Any], evaluator_agent: str):
        """Esegue il protocollo di escalation in caso di 3 fallimenti consecutivi dello scraper."""
        log.warning(f"🚨 [Escalation] Il gate {gate_id} ha fallito {report['attempt_number']} volte consecutive!")
        diagnosis = f"Tentativo fallito per punteggio {report['score']} inferiore alla soglia {report['threshold']}."
        
        # Log del fallimento
        self.memory.write(
            layer="decision_log",
            content={
                "type": "escalation",
                "gate_id": gate_id,
                "attempts": report["attempt_number"],
                "diagnosis": diagnosis,
                "strategy_applied": "Strategia Ricarica Pagina (Fallback)"
            },
            author="quality_gate_system",
            importance=0.9
        )
        
        self.event_bus.publish(
            event_type="gate.escalated",
            publisher="quality_gate_system",
            payload={
                "gate_id": gate_id,
                "total_attempts": report["attempt_number"],
                "diagnosis": diagnosis,
                "recommended_strategy_change": "Riavvia browser con ritardo esteso"
            },
            delivery_mode="EXACTLY_ONCE"
        )
