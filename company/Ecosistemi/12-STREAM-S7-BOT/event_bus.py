import uuid
from typing import Callable, Dict, List, Any
import datetime

class EventBus:
    """
    ⚡ EVENT BUS - APEX-7 Core Communication Layer
    "Nessun agente chiama un altro direttamente"
    """
    
    def __init__(self):
        # Mappa: event_type -> list of subscriber callbacks
        self.subscribers: Dict[str, List[Callable]] = {}
        # Log di tutti gli eventi passati (utile per il Meta-Agent)
        self.event_log: List[Dict[str, Any]] = []

    def subscribe(self, event_type: str, callback: Callable):
        """
        Un agente si iscrive per ascoltare un tipo di evento.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type: str, payload: Dict[str, Any]):
        """
        Un agente pubblica un evento sulla bacheca. Non sa chi lo riceverà.
        """
        event = {
            "event_id": f"EVT-{uuid.uuid4().hex[:8].upper()}",
            "event_type": event_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "payload": payload
        }
        
        # Salva nel log globale
        self.event_log.append(event)
        
        # Consegna a tutti gli iscritti
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                try:
                    # In Level 1 eseguiamo in modo sincrono per semplicità, 
                    # in L3+ diventerà asincrono con code e retry.
                    callback(event)
                except Exception as e:
                    # Se un subscriber fallisce, logghiamo ma non blocchiamo l'Event Bus
                    print(f"[EVENT BUS ERROR] Il subscriber per {event_type} ha fallito: {str(e)}")

    def get_history(self, event_type: str = None) -> List[Dict[str, Any]]:
        """
        Permette al Meta-Agent di leggere lo storico della bacheca.
        """
        if event_type:
            return [e for e in self.event_log if e["event_type"] == event_type]
        return self.event_log

# Istanza globale dell'Event Bus (Singleton per il Level 1)
global_bus = EventBus()
