import uuid
from typing import Dict, Any
from event_bus import global_bus

class Orchestrator:
    """
    👑 ORCHESTRATOR - L'Amministratore Delegato (L1)
    Assegna task e invoca gli ispettori. Non esegue il lavoro sporco.
    """
    
    def __init__(self, agent_id: str = "ORCHESTRATOR-1"):
        self.agent_id = agent_id
        
        # L'orchestratore ascolta quando i task sono finiti e gli esiti dei gate
        global_bus.subscribe("task.completed", self.handle_task_completed)
        global_bus.subscribe("gate.passed", self.handle_gate_passed)
        global_bus.subscribe("gate.failed", self.handle_gate_failed)
        
        # Mappa per tenere traccia dello stato dei task attivi (task_id -> task_data)
        self.active_tasks: Dict[str, Dict[str, Any]] = {}

    def assign_mission(self, description: str, priority: str = "NORMAL"):
        """
        Punto di ingresso. Tu (Max) chiami questa funzione per dare il via ai lavori.
        """
        task_id = f"TASK-{uuid.uuid4().hex[:6].upper()}"
        
        self.active_tasks[task_id] = {
            "description": description,
            "status": "ASSIGNED",
            "fail_count": 0
        }
        
        print(f"[{self.agent_id}] Nuova Missione: {description}. Assegnato ID: {task_id}")
        
        # Pubblica il task in bacheca affinché un Operaio lo prenda
        global_bus.publish("task.created", {
            "task_id": task_id,
            "description": description,
            "priority": priority
        })

    def handle_task_completed(self, event: Dict[str, Any]):
        """
        L'Operaio ha finito. L'AD chiama l'Ispettore.
        """
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        output = payload.get("output")
        worker_id = payload.get("agent_id")
        
        if task_id in self.active_tasks:
            print(f"[{self.agent_id}] Il task {task_id} è stato completato da {worker_id}. Chiamo l'Ispettore GATE-1.")
            self.active_tasks[task_id]["status"] = "UNDER_INSPECTION"
            
            # Chiede a GATE-1 di controllare l'output
            global_bus.publish("gate.check.requested", {
                "gate_id": f"GATE-L1-{task_id}",
                "output_to_check": output,
                "level": "L1",
                "criteria": [{"name": "Completezza"}, {"name": "Correttezza"}] # Mock criteri
            })

    def handle_gate_passed(self, event: Dict[str, Any]):
        """
        L'Ispettore ha approvato. Missione compiuta.
        """
        payload = event.get("payload", {})
        gate_id = payload.get("gate_id")
        # Estraiamo il task_id dal gate_id (es. GATE-L1-TASK-123)
        task_id = gate_id.replace("GATE-L1-", "")
        
        if task_id in self.active_tasks:
            print(f"[{self.agent_id}] [APPROVATO] L'ispettore ha APPROVATO il task {task_id}. Missione chiusa con successo.")
            self.active_tasks[task_id]["status"] = "DONE"

    def handle_gate_failed(self, event: Dict[str, Any]):
        """
        L'Ispettore ha bocciato. Nel L1 (flusso dritto) l'Orchestrator notifica l'umano o riassegna.
        """
        payload = event.get("payload", {})
        gate_id = payload.get("gate_id")
        remediation = payload.get("remediation_suggestions", [])
        
        task_id = gate_id.replace("GATE-L1-", "")
        
        if task_id in self.active_tasks:
            self.active_tasks[task_id]["fail_count"] += 1
            fail_count = self.active_tasks[task_id]["fail_count"]
            
            print(f"[{self.agent_id}] [BOCCIATO] L'ispettore ha BOCCIATO il task {task_id}. Fallimento #{fail_count}.")
            print(f"[{self.agent_id}] Motivi forniti da Gate-1: {remediation}")
            
            if fail_count >= 3:
                print(f"[{self.agent_id}] [ESCALATION] Il task {task_id} ha fallito 3 volte. FREEZE! Chiamo il Meta-Agent.")
                self.active_tasks[task_id]["status"] = "ESCALATED"
                global_bus.publish("task.escalated", {"task_id": task_id, "reason": "Too many fails"})
            else:
                print(f"[{self.agent_id}] Riassegno il task {task_id} in bacheca con i correttivi.")
                self.active_tasks[task_id]["status"] = "REASSIGNED"
                global_bus.publish("task.created", {
                    "task_id": task_id,
                    "description": self.active_tasks[task_id]["description"] + f" (CORREZIONE: {remediation})",
                    "priority": "HIGH"
                })

# Istanziamo l'Amministratore Delegato
ad_orchestrator = Orchestrator()
