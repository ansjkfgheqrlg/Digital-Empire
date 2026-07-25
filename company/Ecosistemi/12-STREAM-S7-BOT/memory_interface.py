import os
import json
import uuid
import time
import math
import datetime
from typing import Dict, Any, List, Optional
from event_bus import global_bus

# Sopra questa somiglianza due scritture sono considerate la stessa cosa.
DUPLICATE_THRESHOLD = 0.95
# Sotto questa somiglianza due decisioni non sono confrontabili.
DECISION_SIMILARITY_THRESHOLD = 0.75
# Una strategia usata meno di questo numero di volte non ha statistica affidabile.
MIN_USES_FOR_RANKING = 3
# Oltre questa eta' in giorni un record mai letto e' candidato all'archivio.
STALE_AFTER_DAYS = 90


def _tokens(text: str) -> set:
    return {t for t in "".join(c.lower() if c.isalnum() else " " for c in str(text)).split() if len(t) > 2}


def _similarity(a: str, b: str) -> float:
    """Somiglianza per insiemi di parole. Non e' semantica, ma non mente sul proprio grado."""
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


class MemoryInterface:
    """
    🧠 MEMORY QUERY INTERFACE — APEX-7 (Level 2)
    "La memoria non e' un database. E' un cervello."

    Cinque modi di interrogarla, uno solo di cambiarla:
      TYPE 1  contextual_recall   cosa e' rilevante adesso
      TYPE 2  decision_lookup     ho gia' deciso questa cosa in passato?
      TYPE 3  strategy_fetch      cosa ha funzionato per problemi come questo?
      TYPE 4  write               salva, con lock e con autore
      TYPE 5  forget              archivia, mai cancella

    Principi: la lettura non blocca mai, la scrittura sempre; ogni record porta
    il suo autore; ogni risposta porta il suo grado di fiducia.
    """

    def __init__(self, persist_path: Optional[str] = None):
        self.storage: Dict[str, List[Dict[str, Any]]] = {
            "strategies": [],
            "decisions": [],
            "knowledge": [],
            "gate_reports": [],
            "metrics": [],
            "patterns": [],
        }
        self.write_lock = False
        # Indice invertito parola -> [record_id]: evita la scansione totale
        # quando i record diventano migliaia.
        self._index: Dict[str, List[str]] = {}
        self._by_id: Dict[str, Dict[str, Any]] = {}
        self.persist_path = persist_path or os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "memory_store.json"
        )
        self.stats = {"reads": 0, "writes": 0, "duplicates_skipped": 0,
                      "archived": 0, "lock_timeouts": 0}

    # ------------------------------------------------------------------ #
    # Lock — la lettura non lo prende mai, la scrittura sempre
    # ------------------------------------------------------------------ #

    def _acquire_lock(self, timeout_ms: int = 100) -> bool:
        start = time.time()
        while self.write_lock:
            if (time.time() - start) * 1000 > timeout_ms:
                self.stats["lock_timeouts"] += 1
                return False
            time.sleep(0.001)
        self.write_lock = True
        return True

    def _release_lock(self):
        self.write_lock = False

    # ------------------------------------------------------------------ #
    # Indice
    # ------------------------------------------------------------------ #

    def _index_record(self, record: Dict[str, Any]):
        self._by_id[record["id"]] = record
        for tok in _tokens(record.get("content", "")):
            self._index.setdefault(tok, []).append(record["id"])

    def _rebuild_index(self):
        self._index.clear()
        self._by_id.clear()
        for records in self.storage.values():
            for r in records:
                self._index_record(r)

    # ------------------------------------------------------------------ #
    # TYPE 4 — WRITE (con lock)
    # ------------------------------------------------------------------ #

    def write(self, layer: str, content: Any, author: str, importance: float = 0.5,
              confidence: float = 0.9, tags: List[str] = None,
              ttl_days: Optional[int] = None) -> Optional[str]:
        """
        Salva un record: prende il lock, scarta i doppioni, scrive con i metadati
        completi e avvisa il bus. Ritorna l'id nuovo, o quello del record
        esistente se la scrittura era un duplicato.
        """
        if not self._acquire_lock():
            raise TimeoutError("Impossibile acquisire il lock per scrivere in memoria.")

        try:
            existing = self._find_duplicate(layer, content)
            if existing:
                self.stats["duplicates_skipped"] += 1
                existing["access_count"] += 1
                return existing["id"]

            mem_id = f"MEM-{uuid.uuid4().hex[:8].upper()}"
            record = {
                "id": mem_id,
                "timestamp": datetime.datetime.now().isoformat(),
                "author_agent": author,
                "importance": importance,
                "confidence": confidence,
                "tags": tags or [],
                "content": content,
                "status": "ACTIVE",
                "ttl_days": ttl_days,
                "access_count": 0,
                "last_accessed": None,
                "version": 1,
            }

            self.storage.setdefault(layer, []).append(record)
            self._index_record(record)
            self.stats["writes"] += 1

            global_bus.publish("memory.updated", {
                "layer": layer,
                "mem_id": mem_id,
                "author": author,
                "type": "CREATE",
            })

            return mem_id
        finally:
            self._release_lock()

    def _find_duplicate(self, layer: str, content: Any) -> Optional[Dict[str, Any]]:
        for r in self.storage.get(layer, []):
            if r.get("status") != "ACTIVE":
                continue
            if _similarity(r.get("content", ""), content) >= DUPLICATE_THRESHOLD:
                return r
        return None

    # ------------------------------------------------------------------ #
    # TYPE 1 — CONTEXTUAL RECALL
    # ------------------------------------------------------------------ #

    def contextual_recall(self, keywords: List[str], min_confidence: float = 0.60,
                          max_results: int = 5, layers: List[str] = None) -> List[Dict[str, Any]]:
        """
        Cosa e' rilevante per quello che sto facendo adesso.
        Ordina per rilevanza x freschezza x fiducia x importanza: un ricordo
        pertinente ma vecchio e incerto perde contro uno meno pertinente ma solido.
        """
        self.stats["reads"] += 1
        query = " ".join(str(k) for k in keywords)
        candidate_ids = set()
        for tok in _tokens(query):
            candidate_ids.update(self._index.get(tok, []))

        allowed_ids = None
        if layers:
            allowed_ids = {r["id"] for l in layers for r in self.storage.get(l, [])}

        scored = []
        for rid in candidate_ids:
            r = self._by_id.get(rid)
            if r is None or r.get("status") != "ACTIVE":
                continue
            if allowed_ids is not None and rid not in allowed_ids:
                continue
            confidence = r.get("confidence", 0.9)
            if confidence < min_confidence:
                continue

            relevance = _similarity(r.get("content", ""), query)
            if relevance == 0:
                continue
            age_days = self._age_days(r)
            recency = math.exp(-age_days / 30.0)   # mezza vita di circa tre settimane
            score = relevance * (0.4 + 0.6 * recency) * confidence * (0.5 + 0.5 * r.get("importance", 0.5))

            scored.append({
                "id": r["id"],
                "content": r["content"],
                "source_layer": self._layer_of(r),
                "relevance_score": round(relevance, 3),
                "confidence": confidence,
                "age_days": round(age_days, 1),
                "author_agent": r["author_agent"],
                "final_score": round(score, 4),
            })

        scored.sort(key=lambda x: x["final_score"], reverse=True)
        results = scored[:max_results]

        for res in results:
            rec = self._by_id[res["id"]]
            rec["access_count"] += 1
            rec["last_accessed"] = datetime.datetime.now().isoformat()

        return results

    def _age_days(self, record: Dict[str, Any]) -> float:
        try:
            ts = datetime.datetime.fromisoformat(record["timestamp"])
            return (datetime.datetime.now() - ts).total_seconds() / 86400.0
        except Exception:
            return 0.0

    def _layer_of(self, record: Dict[str, Any]) -> str:
        for layer, records in self.storage.items():
            if any(r["id"] == record["id"] for r in records):
                return layer
        return "unknown"

    # ------------------------------------------------------------------ #
    # TYPE 2 — DECISION LOOKUP
    # ------------------------------------------------------------------ #

    def decision_lookup(self, decision_description: str,
                        similarity_threshold: float = DECISION_SIMILARITY_THRESHOLD) -> Dict[str, Any]:
        """
        Ho gia' preso questa decisione, e com'e' andata?
        Serve a non ripetere una scelta che e' gia' costata cara una volta.
        """
        self.stats["reads"] += 1
        matches = []
        for r in self.storage.get("decisions", []):
            if r.get("status") != "ACTIVE":
                continue
            content = r["content"]
            text = content.get("decision", "") if isinstance(content, dict) else str(content)
            sim = _similarity(text, decision_description)
            if sim >= similarity_threshold:
                outcome = content.get("outcome", "UNKNOWN") if isinstance(content, dict) else "UNKNOWN"
                matches.append({
                    "id": r["id"],
                    "original_decision": text,
                    "similarity": round(sim, 3),
                    "outcome": outcome,
                    "decided_by": r["author_agent"],
                    "age_days": round(self._age_days(r), 1),
                    "should_reuse": outcome == "SUCCESS",
                    "adaptation_needed": None if outcome == "SUCCESS"
                    else "Esito passato non positivo: cambiare approccio invece di ripetere",
                })

        matches.sort(key=lambda m: m["similarity"], reverse=True)
        return {"similar_decisions_found": len(matches), "decisions": matches}

    def record_decision(self, decision: str, author: str, outcome: str = "PENDING",
                        rationale: str = "", alternatives: List[str] = None) -> str:
        """Scrittura tipizzata nel Decision Log: qui la forma libera non serve a nessuno."""
        return self.write("decisions", {
            "decision": decision,
            "outcome": outcome,
            "rationale": rationale,
            "alternatives": alternatives or [],
        }, author, importance=0.9)

    def close_decision(self, decision_id: str, outcome: str) -> bool:
        """Chiude una decisione con il suo esito reale. Senza questo il lookup e' cieco."""
        rec = self._by_id.get(decision_id)
        if not rec or not isinstance(rec.get("content"), dict):
            return False
        rec["content"]["outcome"] = outcome
        rec["version"] += 1
        return True

    # ------------------------------------------------------------------ #
    # TYPE 3 — STRATEGY FETCH
    # ------------------------------------------------------------------ #

    def register_strategy(self, name: str, problem_type: str, author: str,
                          parameters: Dict[str, Any] = None, constraints: List[str] = None,
                          warnings: List[str] = None) -> str:
        return self.write("strategies", {
            "name": name,
            "problem_type": problem_type,
            "parameters": parameters or {},
            "constraints": constraints or [],
            "warnings": warnings or [],
            "times_used": 0,
            "times_succeeded": 0,
        }, author, importance=0.8)

    def record_strategy_outcome(self, strategy_name: str, success: bool) -> bool:
        """Ogni uso aggiorna la statistica della strategia: il ranking nasce da qui."""
        for r in self.storage.get("strategies", []):
            c = r["content"]
            if isinstance(c, dict) and c.get("name") == strategy_name:
                c["times_used"] += 1
                if success:
                    c["times_succeeded"] += 1
                r["version"] += 1
                if c["times_used"] >= 5 and self._success_rate(c) < 0.30:
                    self.forget(r["id"], reason="low_success_rate")
                return True
        return False

    @staticmethod
    def _success_rate(content: Dict[str, Any]) -> float:
        used = content.get("times_used", 0)
        return content.get("times_succeeded", 0) / used if used else 0.5

    def strategy_fetch(self, problem_type: str, constraints: List[str] = None) -> Dict[str, Any]:
        """
        Qual e' la strategia migliore per questo problema.
        Ordina per success_rate misurato, con penalita' alle strategie vecchie e
        a quelle usate troppo poche volte per dire qualcosa di serio.
        """
        self.stats["reads"] += 1
        constraints = constraints or []
        ranked = []

        for r in self.storage.get("strategies", []):
            if r.get("status") != "ACTIVE":
                continue
            c = r["content"]
            if not isinstance(c, dict):
                continue
            declared = c.get("problem_type", "")
            if declared != problem_type and _similarity(declared, problem_type) < 0.3:
                continue
            if constraints and not set(constraints).issubset(set(c.get("constraints", []))):
                continue

            success_rate = self._success_rate(c)
            age_penalty = 0.9 if self._age_days(r) > 30 else 1.0
            confidence_penalty = 1.0 if c.get("times_used", 0) >= MIN_USES_FOR_RANKING else 0.7
            score = success_rate * age_penalty * confidence_penalty

            ranked.append({
                "name": c["name"],
                "success_rate": round(success_rate, 3),
                "times_used": c.get("times_used", 0),
                "parameters": c.get("parameters", {}),
                "warnings": c.get("warnings", []),
                "ranking_score": round(score, 3),
                "statistically_solid": c.get("times_used", 0) >= MIN_USES_FOR_RANKING,
            })

        ranked.sort(key=lambda s: s["ranking_score"], reverse=True)
        return {
            "recommended_strategy": ranked[0] if ranked else None,
            "alternatives": ranked[1:4],
            "total_candidates": len(ranked),
        }

    # ------------------------------------------------------------------ #
    # TYPE 5 — FORGET (dimenticanza strategica)
    # ------------------------------------------------------------------ #

    def forget(self, mem_id: str, reason: str, superseded_by: str = None) -> bool:
        """
        Un ricordo obsoleto o dannoso non si cancella: si archivia con il motivo e
        con cosa lo sostituisce. Cancellarlo farebbe perdere anche la traccia
        dell'errore, che e' la parte utile.
        """
        if not self._acquire_lock():
            raise TimeoutError("Impossibile acquisire il lock.")
        try:
            rec = self._by_id.get(mem_id)
            if rec is None:
                return False
            rec["status"] = "ARCHIVED"
            rec["archived_at"] = datetime.datetime.now().isoformat()
            rec["reason"] = reason
            rec["superseded_by"] = superseded_by
            self.stats["archived"] += 1
            return True
        finally:
            self._release_lock()

    def sweep_stale(self, author: str = "MEMORY-KEEPER") -> int:
        """Archivia cio' che ha passato i 90 giorni senza essere mai letto."""
        archived = 0
        for records in list(self.storage.values()):
            for r in list(records):
                if r.get("status") != "ACTIVE":
                    continue
                if self._age_days(r) > STALE_AFTER_DAYS and r.get("access_count", 0) == 0:
                    self.forget(r["id"], reason="stale_never_accessed")
                    archived += 1
        if archived:
            global_bus.publish("memory.compression.triggered", {
                "records_archived": archived,
                "reason": "stale_never_accessed",
                "by": author,
            })
        return archived

    # ------------------------------------------------------------------ #
    # Persistenza tra sessioni
    # ------------------------------------------------------------------ #

    def checkpoint(self, path: Optional[str] = None) -> str:
        """Fotografa la memoria su disco: una sessione interrotta non perde nulla."""
        target = path or self.persist_path
        snapshot = {
            "saved_at": datetime.datetime.now().isoformat(),
            "storage": self.storage,
            "stats": self.stats,
        }
        with open(target, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, ensure_ascii=False, indent=2, default=str)
        return target

    def restore(self, path: Optional[str] = None) -> bool:
        """Riprende la memoria da un checkpoint e ricostruisce l'indice."""
        target = path or self.persist_path
        if not os.path.exists(target):
            return False
        with open(target, "r", encoding="utf-8") as f:
            snapshot = json.load(f)
        self.storage = snapshot.get("storage", self.storage)
        self.stats.update(snapshot.get("stats", {}))
        self._rebuild_index()
        return True

    # ------------------------------------------------------------------ #
    # Diagnostica
    # ------------------------------------------------------------------ #

    def get_stats(self) -> Dict[str, Any]:
        return {
            **self.stats,
            "layers": {l: len(r) for l, r in self.storage.items()},
            "active_records": sum(1 for rs in self.storage.values() for r in rs if r.get("status") == "ACTIVE"),
            "archived_records": sum(1 for rs in self.storage.values() for r in rs if r.get("status") == "ARCHIVED"),
            "index_terms": len(self._index),
            "lock_held": self.write_lock,
        }


global_memory = MemoryInterface()
