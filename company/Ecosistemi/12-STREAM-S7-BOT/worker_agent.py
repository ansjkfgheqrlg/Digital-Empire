import uuid
import time
from typing import Dict, Any
from event_bus import global_bus

class WorkerAgent:
    """
    🏭 WORKER AGENT - Reparto Esecuzione
    "Faccio il lavoro sporco."
    """
    
    def __init__(self, agent_id: str, skills: list = None):
        self.agent_id = agent_id
        self.state = "IDLE"
        self.skills = skills or ["analysis"]
        
        # In L1, i worker ascoltano task.created per prendere i task direttamente
        # (Dal L2 in poi ascolteranno task.decomposed mandato dal Planner)
        global_bus.subscribe("task.created", self.handle_task)

    def handle_task(self, event: Dict[str, Any]):
        """
        Riceve un task dalla bacheca e lo elabora.
        """
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        description = payload.get("description", "")
        
        print(f"[{self.agent_id}] Ha preso in carico il task {task_id}: {description}")
        self.state = "WORKING"
        
        # Simula il tempo di esecuzione
        start_time = time.time()
        time.sleep(1) # mock execution time
        
        output = self.execute_task(description)
        time_taken_ms = int((time.time() - start_time) * 1000)
        
        print(f"[{self.agent_id}] Task {task_id} completato in {time_taken_ms}ms")
        self.state = "IDLE"
        
        # Pubblica il risultato
        global_bus.publish("task.completed", {
            "task_id": task_id,
            "agent_id": self.agent_id,
            "output": output,
            "quality_score": None, # Verrà calcolato dall'Ispettore (Gate)
            "time_taken_ms": time_taken_ms
        })

    def execute_task(self, description: str) -> str:
        """
        La vera esecuzione del task.
        """
        # In una vera implementazione chiameremmo Claude/Gemini con i prompt di L1.
        # Qui simuliamo la produzione di un output.
        return f"[MOCK OUTPUT] Risultato generato per: {description}. Eseguito usando le skill {self.skills}."

# Esempio di un worker di base pronto per il Level 1
analyst_worker = WorkerAgent(agent_id="WORKER-ANALYST-1", skills=["data_analysis"])
