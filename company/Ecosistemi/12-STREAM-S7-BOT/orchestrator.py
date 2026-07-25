import uuid
import time
from typing import Dict, Any, Optional

from event_bus import global_bus
from memory_interface import global_memory
from quality_gates import MAX_ATTEMPTS_BEFORE_ESCALATION

# Tetto ai giri di correzione di uno stesso task. Oltre questo il problema non
# e' l'esecuzione: e' la richiesta.
MAX_REMEDIATION_ITERATIONS = MAX_ATTEMPTS_BEFORE_ESCALATION


class Orchestrator:
    """
    👑 ORCHESTRATOR — L'Amministratore Delegato (Level 2)

    Assegna il lavoro, chiama l'ispettore, decide se rimandare indietro o
    escalare. Non esegue: se si mettesse a produrre non potrebbe piu' giudicare
    con onesta' quello che ha prodotto.

    Rispetto al Level 1: tiene una mappa gate->task invece di ricavare l'id
    dalla stringa, misura quanto dura ogni missione e registra ogni decisione
    di riassegnazione nel Decision Log.
    """

    def __init__(self, agent_id: str = "ORCHESTRATOR-1", level: str = "L1"):
        self.agent_id = agent_id
        self.level = level
        self.active_tasks: Dict[str, Dict[str, Any]] = {}
        # gate_id -> task_id: l'id non si deduce piu' spezzando una stringa
        self.gate_to_task: Dict[str, str] = {}

        global_bus.subscribe("task.completed", self.handle_task_completed, subscriber_id=f"{agent_id}.completed")
        global_bus.subscribe("gate.passed", self.handle_gate_passed, subscriber_id=f"{agent_id}.passed")
        global_bus.subscribe("gate.failed", self.handle_gate_failed, subscriber_id=f"{agent_id}.failed")
        global_bus.subscribe("gate.escalated", self.handle_gate_escalated, subscriber_id=f"{agent_id}.gate_esc")

    # ------------------------------------------------------------------ #
    # Ingresso
    # ------------------------------------------------------------------ #

    def assign_mission(self, description: str, priority: str = "NORMAL",
                       gate_level: Optional[str] = None) -> str:
        """Punto di ingresso: Max chiama questa e il sistema si mette in moto."""
        task_id = f"TASK-{uuid.uuid4().hex[:6].upper()}"

        # Prima di partire: questa decisione l'abbiamo gia' presa?
        prior = global_memory.decision_lookup(description)
        if prior["similar_decisions_found"]:
            top = prior["decisions"][0]
            print(f"[{self.agent_id}] Gia' affrontato qualcosa di simile "
                  f"({top['similarity']:.0%}, esito {top['outcome']}). Ne tengo conto.")

        self.active_tasks[task_id] = {
            "description": description,
            "status": "ASSIGNED",
            "fail_count": 0,
            "started_at": time.time(),
            "gate_level": gate_level or self.level,
        }

        print(f"[{self.agent_id}] Nuova Missione: {description}. Assegnato ID: {task_id}")

        global_bus.publish("task.created", {
            "task_id": task_id,
            "description": description,
            "priority": priority,
        })
        return task_id

    # ------------------------------------------------------------------ #
    # Ciclo di controllo
    # ------------------------------------------------------------------ #

    def handle_task_completed(self, event: Dict[str, Any]):
        """L'operaio ha finito: prima di dire bravo, si chiama l'ispettore."""
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        task = self.active_tasks.get(task_id)
        if not task:
            return

        level = task["gate_level"]
        gate_id = f"GATE-{level}-{task_id}"
        self.gate_to_task[gate_id] = task_id
        task["status"] = "UNDER_INSPECTION"

        print(f"[{self.agent_id}] Task {task_id} completato da {payload.get('agent_id')}. "
              f"Chiamo l'ispettore sul gate {level}.")

        global_bus.publish("gate.check.requested", {
            "gate_id": gate_id,
            "output_to_check": payload.get("output"),
            "level": level,
        })

    def handle_gate_passed(self, event: Dict[str, Any]):
        report = event.get("payload", {})
        task_id = self.gate_to_task.get(report.get("gate_id"))
        task = self.active_tasks.get(task_id)
        if not task:
            return

        elapsed_ms = int((time.time() - task["started_at"]) * 1000)
        task["status"] = "DONE"
        task["duration_ms"] = elapsed_ms

        print(f"[{self.agent_id}] [APPROVATO] {task_id} chiuso in {elapsed_ms}ms "
              f"(score {report.get('score')} su soglia {report.get('threshold')}).")

        self._record_metric("current", elapsed_ms, task_id)

    def handle_gate_failed(self, event: Dict[str, Any]):
        """
        Bocciato: si rimanda indietro con i correttivi, ma non all'infinito.
        Al terzo giro il task viene congelato e passa al Meta-Agent.
        """
        report = event.get("payload", {})
        task_id = self.gate_to_task.get(report.get("gate_id"))
        task = self.active_tasks.get(task_id)
        if not task:
            return

        task["fail_count"] += 1
        n = task["fail_count"]
        remediation = report.get("remediation_suggestions", [])

        print(f"[{self.agent_id}] [BOCCIATO] {task_id}, fallimento #{n}. "
              f"Score {report.get('score')} sotto {report.get('threshold')}.")
        for fix in remediation[:3]:
            print(f"[{self.agent_id}]   correttivo: {fix}")

        if n >= MAX_REMEDIATION_ITERATIONS:
            task["status"] = "ESCALATED"
            print(f"[{self.agent_id}] [FREEZE] {task_id} bocciato {n} volte. Passo al Meta-Agent.")
            global_memory.record_decision(
                decision=f"Congelato {task_id} dopo {n} bocciature",
                author=self.agent_id,
                outcome="ESCALATED",
                rationale="; ".join(remediation[:3]) or "nessun correttivo utile fornito",
            )
            global_bus.publish("task.escalated", {
                "task_id": task_id,
                "reason": f"{n} bocciature consecutive sullo stesso gate",
            })
            return

        task["status"] = "REASSIGNED"
        global_memory.record_decision(
            decision=f"Riassegnato {task_id} con correttivi (giro {n})",
            author=self.agent_id,
            outcome="PENDING",
            rationale="; ".join(remediation[:3]),
        )
        global_bus.publish("task.created", {
            "task_id": task_id,
            "description": f"{task['description']} (CORREZIONE #{n}: {'; '.join(remediation[:3])})",
            "priority": "HIGH",
        })

    def handle_gate_escalated(self, event: Dict[str, Any]):
        """L'ispettore ha escalato di sua iniziativa: l'AD prende atto e congela."""
        report = event.get("payload", {})
        task_id = self.gate_to_task.get(report.get("gate_id"))
        if task_id and task_id in self.active_tasks:
            self.active_tasks[task_id]["status"] = "ESCALATED"
            print(f"[{self.agent_id}] Il gate ha escalato {task_id}. Avanzamento bloccato.")

    # ------------------------------------------------------------------ #
    # Misure
    # ------------------------------------------------------------------ #

    def _record_metric(self, kind: str, value_ms: int, task_id: str):
        global_memory.write("metrics", {
            "kind": kind, "value_ms": value_ms, "task_id": task_id,
        }, self.agent_id, importance=0.6)

    def set_baseline(self, value_ms: int, note: str = "") -> str:
        """Fissa il metro di paragone. Senza baseline, 'piu' veloce' non vuol dire niente."""
        return global_memory.write("metrics", {
            "kind": "baseline", "value_ms": value_ms, "note": note,
        }, self.agent_id, importance=0.9)

    def status(self) -> Dict[str, Any]:
        counts: Dict[str, int] = {}
        for t in self.active_tasks.values():
            counts[t["status"]] = counts.get(t["status"], 0) + 1
        return {"tasks": len(self.active_tasks), "by_status": counts}


ad_orchestrator = Orchestrator()
