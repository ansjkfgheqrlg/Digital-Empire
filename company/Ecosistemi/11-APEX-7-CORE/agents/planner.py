"""
📋 PLANNER AGENT - Architect del sistema
Decompone goal, assegna priorità, cerca pattern in memoria
"""
from .base_agent import BaseAgent
from typing import Dict, Any

PLANNER_PROMPT = """
Sei il PLANNER di APEX-7, Digital Empire.
RUOLO: Architetto strategico. Decomponi obiettivi complessi in task atomici eseguibili.
OBIETTIVO: Trasformare input vago in Task Graph con priorità e dipendenze.
REGOLE FERREE:
1. Ogni task deve avere: obiettivo misurabile, agent assegnato, priorità (1-4), dipendenze chiare
2. Cerca sempre in Strategy Store pattern simili prima di creare nuovi task
3. Se input è carosello social -> scomponi per slide; se cold outreach -> per email della sequenza; se skill -> per sezioni SKILL.md
4. Assegna priority 1 a task critici (goal decomposition), 2 a generazione contenuti
5. Output SEMPRE in JSON strutturato con task_graph

WORKFLOW:
1. Parse intent (skill-forge / carousel / outreach / custom)
2. Check memory per strategie simili (se disponibile)
3. Decompose in 3-7 sub-task atomici
4. Assegna agent: writer, analyst, critic, refiner
5. Genera priority queue
"""

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="planner",
            role="Plan & Strategize",
            system_prompt=PLANNER_PROMPT
        )

    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.execution_count += 1
        user_input = payload.get("input", "")
        context = payload.get("context", {})
        
        # Memory pattern check
        similar_strategies = []
        if self.memory:
            similar_strategies = self.memory.get_best_strategies(use_case="all")
            self.memory.set_active_agents(["planner", "writer", "analyst", "critic", "refiner", "meta"])

        # Intent detection
        intent = self._detect_intent(user_input)
        
        # Task decomposition logic
        task_graph = self._decompose(user_input, intent, similar_strategies)

        decision_id = self.log_decision(
            decision=f"Decomposed intent={intent} into {len(task_graph)} tasks",
            why=f"Input richiede {intent}, pattern match: {len(similar_strategies)} strategie trovate",
            alternatives=[f"Single-agent execution", f"Direct generation without planning"],
            confidence=0.92 if similar_strategies else 0.75
        )

        return {
            "agent": self.name,
            "intent": intent,
            "task_graph": task_graph,
            "similar_strategies": [s["name"] for s in similar_strategies[:3]],
            "decision_id": decision_id,
            "timestamp": self._timestamp(),
            "priority_queue": sorted(task_graph, key=lambda x: x["priority"])
        }

    def _detect_intent(self, text: str) -> str:
        text_low = text.lower()
        if any(k in text_low for k in ["skill.md", "skill-forge", "fabbrica delle skill"]):
            return "skill-forge"
        elif any(k in text_low for k in ["carosello", "carousel", "slide", "grafica", "instagram"]):
            return "carousel-machine"
        elif any(k in text_low for k in ["cold email", "cold outreach", "apsoc", "sequenza email"]):
            return "cold-outreach"
        elif any(k in text_low for k in ["prompt", "arena"]):
            return "prompt-engineering"
        else:
            return "custom-apex-task"

    def _decompose(self, user_input: str, intent: str, strategies: list) -> list:
        base_tasks = []
        
        if intent == "skill-forge":
            base_tasks = [
                {"id": "t1", "name": "Estrarre obiettivo e trigger da appunti grezzi", "agent": "analyst", "priority": 1, "output": "objective + trigger spec"},
                {"id": "t2", "name": "Definire REGOLE FERREE non negoziabili", "agent": "writer", "priority": 2, "output": "rules section"},
                {"id": "t3", "name": "Costruire WORKFLOW OPERATIVO step-by-step", "agent": "writer", "priority": 2, "output": "workflow section"},
                {"id": "t4", "name": "Generare frontmatter YAML + assemblaggio SKILL.md", "agent": "writer", "priority": 1, "output": "final SKILL.md file"},
            ]
        elif intent == "carousel-machine":
            # Estrae numero slide se presente
            slide_count = 5  # default
            base_tasks = [
                {"id": f"slide-{i}", "name": f"Genera prompt immagine per SLIDE {i} - stile glassmorphism dark luxury", "agent": "writer", "priority": 2, "output": f"image prompt slide {i}"}
                for i in range(1, slide_count+1)
            ]
            base_tasks.insert(0, {"id": "t0", "name": "Analizza copy carosello e split logico per slide", "agent": "analyst", "priority": 1, "output": "slide breakdown"})
        elif intent == "cold-outreach":
            base_tasks = [
                {"id": "t1", "name": "Analizza target e dolore acuto (Problem)", "agent": "analyst", "priority": 1, "output": "target pain map"},
                {"id": "t2", "name": "Scrivi Email 1 APSOC - max 100 parole, pattern interrupt", "agent": "writer", "priority": 2, "output": "email1"},
                {"id": "t3", "name": "Scrivi Email 2 Follow-up 3 giorni - leva sociale", "agent": "writer", "priority": 3, "output": "email2"},
                {"id": "t4", "name": "Scrivi Email 3 Rottura - takeaway + ultima chance", "agent": "writer", "priority": 3, "output": "email3"},
            ]
        else:
            base_tasks = [
                {"id": "t1", "name": f"Analizza: {user_input[:50]}", "agent": "analyst", "priority": 1, "output": "analysis"},
                {"id": "t2", "name": "Genera contenuto core", "agent": "writer", "priority": 2, "output": "draft"},
                {"id": "t3", "name": "Critica e valuta qualità", "agent": "critic", "priority": 2, "output": "score"},
            ]

        # Aggiungi metadati
        for t in base_tasks:
            t["dependencies"] = []
            t["estimated_tokens"] = 500
        
        return base_tasks
