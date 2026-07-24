import json
import datetime
from typing import Dict, Any, List
from event_bus import global_bus
from memory_interface import global_memory

class GateAgent:
    """
    🔍 GATE AGENT (GATE-1) - Quality Checkpoint Executor
    "Io non creo. Io giudico. Senza pietà."
    """
    
    def __init__(self, agent_id: str = "GATE-1"):
        self.agent_id = agent_id
        self.state = "IDLE"
        
        # Si iscrive all'Event Bus per ascoltare richieste di ispezione
        global_bus.subscribe("gate.check.requested", self.handle_check_requested)

    def handle_check_requested(self, event: Dict[str, Any]):
        """
        Handler per l'evento gate.check.requested.
        """
        self.state = "LOADING"
        payload = event.get("payload", {})
        gate_id = payload.get("gate_id")
        output_to_check = payload.get("output_to_check")
        level = payload.get("level")
        
        # Nella realtà questi criteri verrebbero caricati dal DB dei Gate
        criteria = payload.get("criteria", [])
        
        print(f"[{self.agent_id}] Inizio ispezione per il Gate {gate_id}...")
        
        report = self.evaluate(gate_id, criteria, output_to_check)
        
        if report["result"] == "PASSED":
            global_bus.publish("gate.passed", report)
        else:
            global_bus.publish("gate.failed", report)
            
        self.state = "IDLE"

    def evaluate(self, gate_id: str, criteria: List[Dict[str, Any]], output_to_check: Any) -> Dict[str, Any]:
        """
        L'algoritmo di Checking in 4 step.
        """
        self.state = "CHECKING"
        
        criteria_results = []
        score = 0.0
        
        # Mock della valutazione (in APEX reale qui chiameremmo Gemini/Claude con il prompt interno)
        # Per L1, controlliamo banalmente che l'output non sia vuoto e se passa i mock.
        for c in criteria:
            criterion_name = c.get("name")
            
            # Simuliamo una logica di ispezione: "Il dubbio = FAIL"
            if not output_to_check:
                status = "FAIL"
                evidence = "L'output fornito è vuoto o nullo."
                fix = "Fornire un output valido che contenga l'implementazione richiesta."
            else:
                status = "PASS"
                evidence = f"Trovata implementazione relativa a {criterion_name}."
                fix = None
                
            criteria_results.append({
                "criterion": criterion_name,
                "status": status,
                "evidence": evidence,
                "fix": fix,
                "confidence": 0.95
            })
            
            if status == "PASS":
                score += 1.0
            elif status == "PARTIAL":
                score += 0.5
                
        total_criteria = len(criteria) if criteria else 1
        final_score = score / total_criteria
        
        threshold = 1.0  # Per passare serve 100% in L1
        result = "PASSED" if final_score >= threshold else "FAILED"
        
        self.state = "REPORTING"
        
        report = {
            "gate_id": gate_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "gate_agent": self.agent_id,
            "result": result,
            "score": final_score,
            "threshold": threshold,
            "criteria_results": criteria_results,
            "remediation_suggestions": [r["fix"] for r in criteria_results if r["fix"]],
            "attempt_number": 1,
            "next_action": "PROCEED" if result == "PASSED" else "REMEDIATE"
        }
        
        # Salva il report nella Memoria
        global_memory.write("gate_reports", report, self.agent_id, importance=0.9)
        
        return report

# Istanziamo il Gate Agent globale per il Level 1
gate_1 = GateAgent("GATE-1")
