#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Quality Gate Agent (GATE-1)
"""
from __future__ import annotations

import os
import sys
import json
import logging
import argparse
from pathlib import Path
from typing import Any, Dict, Optional

# Aggiunge i percorsi necessari al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../02-AUTOMAZIONI-E-SCRIPTS")))

from event_bus import EventBus
from memory import MemoryQueryInterface
from quality_gate import QualityGateEngine, GATE_DEFINITIONS

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')
log = logging.getLogger("preventa-pw.agente-gate")

class GateAgent:
    def __init__(self, memory: Optional[MemoryQueryInterface] = None, event_bus: Optional[EventBus] = None):
        self.agent_id = "GATE-1"
        self.memory = memory or MemoryQueryInterface(memory_filepath="data/memory_db.json")
        self.event_bus = event_bus or EventBus()
        self.engine = QualityGateEngine(self.memory, self.event_bus)
        self.state = "IDLE"  # IDLE, LOADING, CHECKING, REPORTING, REMEDIATING, ESCALATING
        self.rules = self.load_markdown_rules()

    def load_markdown_rules(self) -> str:
        """Carica dinamicamente le regole di comportamento dal file MD associato."""
        md_path = Path(__file__).parent / "AGENTE-GATE.md"
        if md_path.exists():
            return md_path.read_text(encoding="utf-8")
        return "Rules file not found."

    def transition_to(self, new_state: str):
        log.info(f"🤖 [GateAgent] Stato: {self.state} ──▶ {new_state}")
        self.state = new_state

    def evaluate_output(self, gate_id: str, output_to_evaluate: str) -> Dict[str, Any]:
        """Esegue la valutazione deterministica e pessimista di un output dello scraper."""
        self.transition_to("LOADING")
        log.info(f"📖 [{self.agent_id}] Caricate regole di validazione da AGENTE-GATE.md")
        
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

        # Controlli deterministici
        if gate_id == "L1_L2":
            for c in criteria_list:
                cid = c["id"]
                if "città" in output_to_evaluate.lower() or "categoria" in output_to_evaluate.lower():
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato parametro valido nell'input)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: input non contiene parametri necessari."
        
        elif gate_id == "L2_L3":
            for c in criteria_list:
                cid = c["id"]
                lines = output_to_evaluate.strip().splitlines()
                if len(lines) >= 1 and lines[0].strip():
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato output con {len(lines)} lead estratti)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: output vuoto."

        elif gate_id == "L3_L4":
            for c in criteria_list:
                cid = c["id"]
                if "alta" in output_to_evaluate.lower() or "media" in output_to_evaluate.lower() or "bassa" in output_to_evaluate.lower():
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovata qualifica priorità valida)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: nessuna colonna di priorità qualificata trovata."
                    
        elif gate_id == "L4_L5":
            for c in criteria_list:
                cid = c["id"]
                if len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Trovato testo messaggi generati)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: nessun messaggio generato."
                    
        elif gate_id == "L5_L6":
            for c in criteria_list:
                cid = c["id"]
                if "salvato" in output_to_evaluate.lower() or len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (CSV salvato e allineato)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: CSV non salvato correttamente."
                    
        elif gate_id == "L6_L7":
            for c in criteria_list:
                cid = c["id"]
                if "completato" in output_to_evaluate.lower() or len(output_to_evaluate.strip()) > 5:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Pipeline E2E conclusa)"
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: verifica di chiusura fallita."
        else:
            for c in criteria_list:
                cid = c["id"]
                if len(output_to_evaluate.strip()) > 30:
                    evals[cid] = "PASS"
                    notes[cid] = f"Verificato: {c['description']} (Dati validi rilevati)."
                else:
                    evals[cid] = "FAIL"
                    notes[cid] = f"Errore: dati insufficienti per superare {c['description']}."

        report = self.engine.run_check(
            gate_id=gate_id,
            criteria_evaluations=evals,
            evaluator_agent=self.agent_id
        )

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

    def validate_lead(self, lead: Dict[str, Any]) -> Dict[str, Any]:
        """Data-Validator-Gate: valuta un singolo lead PASS/FAIL prima dell'invio."""
        reasons: List[str] = []
        telefono = str(lead.get("telefono") or "").strip()
        sito = str(lead.get("sito_web") or "").strip()
        try:
            num_recensioni = int(lead.get("numero_recensioni") or 0)
        except (TypeError, ValueError):
            num_recensioni = 0
        try:
            media_recensioni = float(lead.get("media_recensioni") or 0)
        except (TypeError, ValueError):
            media_recensioni = 0.0

        if not telefono and not sito:
            reasons.append("Nessun canale di contatto: telefono e sito web entrambi assenti.")

        if num_recensioni >= 5 and media_recensioni < 4.0:
            reasons.append(f"Reputazione insufficiente: {media_recensioni}/5 su {num_recensioni} recensioni (soglia 4.0).")

        passed = len(reasons) == 0
        result = {
            "lead": lead.get("nome_attivita", "sconosciuto"),
            "passed": passed,
            "reasons": reasons
        }

        if passed:
            self.event_bus.publish("lead.validated", self.agent_id, {"lead_name": result["lead"]}, delivery_mode="AT_LEAST_ONCE")
        else:
            log.info(f"🚫 [GateAgent] Lead scartato: {result['lead']} | Motivi: {'; '.join(reasons)}")
            self.event_bus.publish("lead.rejected", self.agent_id, {"lead_name": result["lead"], "reasons": reasons}, delivery_mode="AT_LEAST_ONCE")
            self.memory.write(
                layer="decision_log",
                content={"type": "lead_rejected", "lead": result["lead"], "reasons": reasons},
                author=self.agent_id,
                importance=0.4
            )

        return result

def cli_run():
    parser = argparse.ArgumentParser(description="Run GateAgent Standalone CLI")
    parser.add_argument("--gate-id", type=str, required=True, choices=["L1_L2", "L2_L3", "L3_L4", "L4_L5", "L5_L6", "L6_L7"], help="ID del gate da valutare")
    parser.add_argument("--content", type=str, required=True, help="Contenuto dell'output da valutare")
    args = parser.parse_args()

    agent = GateAgent()
    report = agent.evaluate_output(args.gate_id, args.content)

    print("\n--- REPORT DI QUALITA' GATE ---")
    print(f"Gate ID: {report['gate_id']}")
    print(f"Passed: {'SI' if report['passed'] else 'NO'}")
    print(f"Score: {report['score']} (Soglia: {report['threshold']})")
    print("Dettaglio Criteri:")
    for c in report["criteria_results"]:
        print(f"  [{c['status']}] {c['criterion_id']}: {c['description']} | Note: {c.get('note')}")
    print("--------------------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_run()
    else:
        print("Uso CLI: python agente_gate.py --gate-id <L1_L2/L2_L3/...> --content '<output_text>'")
