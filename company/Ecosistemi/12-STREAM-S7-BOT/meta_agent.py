from typing import Dict, Any
from event_bus import global_bus
from memory_interface import global_memory

class MetaAgent:
    """
    👁️ META-AGENT - Il Direttore Strategico (L1)
    Non interviene nel day-to-day, ma entra in gioco durante le escalation.
    """
    
    def __init__(self, agent_id: str = "META-1"):
        self.agent_id = agent_id
        
        # Ascolta l'allarme generale (task fallito 3 volte)
        global_bus.subscribe("task.escalated", self.handle_escalation)

    def handle_escalation(self, event: Dict[str, Any]):
        """
        Interviene quando l'azienda si blocca.
        """
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        reason = payload.get("reason")
        
        print(f"[{self.agent_id}] [ALLARME] Rilevata ESCALATION per il task {task_id}. Motivo: {reason}")
        print(f"[{self.agent_id}] Fase di DIAGNOSE. Consulto la memoria...")
        
        # Interroga la memoria per vedere lo storico dei gate
        # (In L1 è una ricerca basilare)
        past_reports = global_memory.contextual_recall([task_id, "FAILED"])
        
        print(f"[{self.agent_id}] Trovati {len(past_reports)} record di fallimento passati per questo task.")
        
        # Logica di Strategy Change (mock)
        print(f"[{self.agent_id}] STRATEGY CHANGE: Applico la direttiva 'Semplifica e Riprova'.")
        
        # Scrive la decisione nel Decision Log
        decision = f"Intervento d'emergenza su {task_id}. Cambiata strategia per eccesso di fallimenti."
        global_memory.write("decisions", decision, self.agent_id, importance=0.95)
        
        # In una versione completa, il Meta-Agent modificherebbe il prompt o i parametri
        # e rimetterebbe il task in coda. Per ora, sblocca la situazione forzatamente
        # segnalando all'umano.
        print(f"[{self.agent_id}] 🚨 MAX, il sistema è in stallo sul task {task_id}. Richiesto intervento umano (Human Override).")
        
# Istanziamo il Direttore Strategico
director_meta = MetaAgent()
