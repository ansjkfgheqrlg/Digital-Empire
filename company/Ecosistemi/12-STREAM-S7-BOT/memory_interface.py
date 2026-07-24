import uuid
import datetime
import time
from typing import Dict, Any, List
from event_bus import global_bus

class MemoryInterface:
    """
    🧠 MEMORY QUERY INTERFACE - APEX-7
    "La memoria non è un database. È un cervello."
    """
    
    def __init__(self):
        # Database in memoria (per il Level 1)
        self.storage: Dict[str, List[Dict[str, Any]]] = {
            "strategies": [],
            "decisions": [],
            "knowledge": []
        }
        self.write_lock = False
    
    def _acquire_lock(self, timeout_ms: int = 100) -> bool:
        start = time.time()
        while self.write_lock:
            if (time.time() - start) * 1000 > timeout_ms:
                return False
            time.sleep(0.01)
        self.write_lock = True
        return True

    def _release_lock(self):
        self.write_lock = False

    def write(self, layer: str, content: Any, author: str, importance: float = 0.5) -> str:
        """
        TYPE 4: WRITE (con lock)
        """
        if not self._acquire_lock():
            raise TimeoutError("Impossibile acquisire il lock per scrivere in memoria.")
            
        try:
            mem_id = f"MEM-{uuid.uuid4().hex[:8].upper()}"
            record = {
                "id": mem_id,
                "timestamp": datetime.datetime.now().isoformat(),
                "author_agent": author,
                "importance": importance,
                "content": content,
                "status": "ACTIVE"
            }
            
            if layer not in self.storage:
                self.storage[layer] = []
            
            self.storage[layer].append(record)
            
            # Pubblica l'evento sulla bacheca
            global_bus.publish("memory.updated", {
                "layer": layer,
                "mem_id": mem_id,
                "author": author
            })
            
            return mem_id
        finally:
            self._release_lock()

    def contextual_recall(self, keywords: List[str], min_confidence: float = 0.6) -> List[Dict[str, Any]]:
        """
        TYPE 1: CONTEXTUAL RECALL
        In L1, facciamo una ricerca testuale basilare.
        """
        results = []
        for layer, records in self.storage.items():
            for r in records:
                if r.get("status") == "ARCHIVED":
                    continue
                content_str = str(r.get("content", "")).lower()
                if any(kw.lower() in content_str for kw in keywords):
                    results.append(r)
        return results

    def forget(self, mem_id: str, reason: str, superseded_by: str = None):
        """
        TYPE 5: FORGET (dimenticanza strategica)
        Non cancella, ma archivia.
        """
        if not self._acquire_lock():
            raise TimeoutError("Impossibile acquisire il lock.")
            
        try:
            for layer, records in self.storage.items():
                for r in records:
                    if r.get("id") == mem_id:
                        r["status"] = "ARCHIVED"
                        r["archived_at"] = datetime.datetime.now().isoformat()
                        r["reason"] = reason
                        r["superseded_by"] = superseded_by
                        return True
            return False
        finally:
            self._release_lock()

global_memory = MemoryInterface()
