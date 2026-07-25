import time
from typing import Dict, Any, List, Optional, Callable

from event_bus import global_bus
from memory_interface import global_memory


class WorkerAgent:
    """
    🏭 WORKER AGENT — Reparto Esecuzione (Level 2)
    "Faccio il lavoro sporco."

    Rispetto al Level 1: un worker non prende piu' qualunque task che passa.
    Rivendica solo quelli che rientrano nelle sue competenze, cosi' due worker
    sullo stesso bus si dividono il lavoro invece di duplicarlo. Quando fallisce
    lo dichiara sul bus, perche' un fallimento taciuto e' peggio del fallimento.
    """

    def __init__(self, agent_id: str, skills: List[str] = None,
                 claims: List[str] = None, executor: Optional[Callable] = None,
                 work_time_s: float = 0.05):
        self.agent_id = agent_id
        self.state = "IDLE"
        self.skills = skills or ["analysis"]
        # Parole chiave che questo worker rivendica. Vuoto = prende tutto.
        self.claims = claims or []
        self.executor = executor
        self.work_time_s = work_time_s
        self.completed = 0
        self.failed = 0

        global_bus.subscribe("task.created", self.handle_task, subscriber_id=f"{agent_id}.task")

    # ------------------------------------------------------------------ #

    def _is_mine(self, description: str) -> bool:
        if not self.claims:
            return True
        text = description.lower()
        return any(c.lower() in text for c in self.claims)

    def handle_task(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        description = payload.get("description", "")

        if not self._is_mine(description):
            return

        print(f"[{self.agent_id}] Preso in carico {task_id}: {description[:70]}")
        self.state = "WORKING"
        start = time.time()

        try:
            output = self.execute_task(description)
        except Exception as e:
            self.state = "IDLE"
            self.failed += 1
            print(f"[{self.agent_id}] Fallito {task_id}: {type(e).__name__}: {e}")
            global_bus.publish("task.failed", {
                "task_id": task_id,
                "agent_id": self.agent_id,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "retry_count": 0,
            })
            return

        elapsed_ms = int((time.time() - start) * 1000)
        self.state = "IDLE"
        self.completed += 1
        print(f"[{self.agent_id}] {task_id} completato in {elapsed_ms}ms")

        global_bus.publish("task.completed", {
            "task_id": task_id,
            "agent_id": self.agent_id,
            "output": output,
            "quality_score": None,      # lo assegna l'ispettore, non chi ha prodotto
            "time_taken_ms": elapsed_ms,
        })

    def execute_task(self, description: str) -> str:
        """
        L'esecuzione vera. Se e' stato passato un executor lo usa, altrimenti
        consulta la memoria e produce l'artefatto simulato del Level 2.
        """
        if self.executor:
            return self.executor(description)

        time.sleep(self.work_time_s)
        recalled = global_memory.contextual_recall(description.split()[:6], max_results=2)
        note = f" (ho riusato {len(recalled)} ricordi pertinenti)" if recalled else ""
        return f"[OUTPUT] Risultato per: {description}. Skill usate: {self.skills}.{note}"

    def health(self) -> Dict[str, Any]:
        total = self.completed + self.failed
        return {
            "agent_id": self.agent_id,
            "state": self.state,
            "completed": self.completed,
            "failed": self.failed,
            "health_score": self.completed / total if total else 1.0,
        }


# Worker di base, presente in tutte le sessioni
analyst_worker = WorkerAgent(agent_id="WORKER-ANALYST-1", skills=["data_analysis"])
