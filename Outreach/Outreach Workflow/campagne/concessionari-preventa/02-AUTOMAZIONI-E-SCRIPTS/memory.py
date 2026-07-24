# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Memory Query Interface)
"""
from __future__ import annotations

import json
import logging
import os
import time
import uuid
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple

log = logging.getLogger("preventa-pw.memory")

class MemoryQueryInterface:
    _lock = threading.Lock()
    _file_lock = threading.Lock()

    def __init__(self, memory_filepath: str = "data/memory_db.json"):
        self.memory_filepath = memory_filepath
        os.makedirs(os.path.dirname(self.memory_filepath), exist_ok=True)
        self._initialize_db()

    def _initialize_db(self):
        """Inizializza il file JSON se non esiste."""
        if not os.path.exists(self.memory_filepath):
            # Record di strategie pre-configurate per la rotazione
            default_strategies = [
                {
                    "id": "STR-001",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "author_agent": "system",
                    "layer": "strategy_store",
                    "importance": 0.8,
                    "access_count": 0,
                    "version": 1,
                    "status": "ACTIVE",
                    "content": {
                        "name": "Gancio A (Tempo Perso)",
                        "tags": ["copywriting", "whatsapp", "email"],
                        "success_rate": 0.72,
                        "times_used": 15,
                        "parameters": {"gancio_numero": 1},
                        "warnings": []
                    }
                },
                {
                    "id": "STR-002",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "author_agent": "system",
                    "layer": "strategy_store",
                    "importance": 0.8,
                    "access_count": 0,
                    "version": 1,
                    "status": "ACTIVE",
                    "content": {
                        "name": "Gancio B (Cliente Perso su WhatsApp)",
                        "tags": ["copywriting", "whatsapp"],
                        "success_rate": 0.85,
                        "times_used": 22,
                        "parameters": {"gancio_numero": 2},
                        "warnings": []
                    }
                },
                {
                    "id": "STR-003",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "author_agent": "system",
                    "layer": "strategy_store",
                    "importance": 0.8,
                    "access_count": 0,
                    "version": 1,
                    "status": "ACTIVE",
                    "content": {
                        "name": "Gancio C (PDF Brutto / Brand)",
                        "tags": ["copywriting", "email"],
                        "success_rate": 0.65,
                        "times_used": 8,
                        "parameters": {"gancio_numero": 3},
                        "warnings": []
                    }
                }
            ]
            
            with open(self.memory_filepath, "w", encoding="utf-8") as f:
                json.dump({
                    "strategy_store": default_strategies,
                    "decision_log": [],
                    "general_knowledge": [],
                    "task_outputs": [],
                    "leads_store": []
                }, f, indent=4)

    def _read_db(self) -> Dict[str, List[Dict[str, Any]]]:
        """Legge la memoria dal file JSON (nessun lock di scrittura richiesto)."""
        with self._file_lock:
            try:
                with open(self.memory_filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                log.error(f"Errore lettura DB Memoria: {e}")
                return {"strategy_store": [], "decision_log": [], "general_knowledge": [], "task_outputs": []}

    def _write_db(self, data: Dict[str, List[Dict[str, Any]]], author: str, timeout_ms: int = 100) -> bool:
        """Scrive la memoria con acquisizione del lock e timeout."""
        start_time = time.time()
        acquired = False
        while time.time() - start_time < (timeout_ms / 1000.0):
            if self._lock.acquire(blocking=False):
                acquired = True
                break
            time.sleep(0.005)

        if not acquired:
            log.warning(f"Lock di scrittura memoria non acquisito entro {timeout_ms}ms da {author}. Abort.")
            return False

        try:
            with self._file_lock:
                with open(self.memory_filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
            return True
        except Exception as e:
            log.error(f"Errore scrittura DB Memoria: {e}")
            return False
        finally:
            self._lock.release()

    def write(self, layer: str, content: Dict[str, Any], author: str, importance: float = 0.5, ttl_days: Optional[int] = None) -> Optional[str]:
        """Salva un'informazione in memoria con metadati automatici."""
        db = self._read_db()
        if layer not in db:
            db[layer] = []

        # Check duplicati esatti (similarity > 0.95 -> skip)
        for existing in db[layer]:
            if existing.get("status") != "ARCHIVED" and existing.get("content") == content:
                log.debug("Contenuto identico già presente. Salto scrittura.")
                return existing.get("id")

        mem_id = f"MEM-{uuid.uuid4().hex[:8].upper()}"
        ttl_val = None
        if ttl_days is not None:
            ttl_val = (datetime.utcnow() + timedelta(days=ttl_days)).isoformat() + "Z"

        record = {
            "id": mem_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "author_agent": author,
            "layer": layer,
            "importance": importance,
            "ttl": ttl_val,
            "access_count": 0,
            "last_accessed": None,
            "version": 1,
            "status": "ACTIVE",
            "content": content
        }

        db[layer].append(record)
        success = self._write_db(db, author=author)
        if success:
            log.info(f"💾 [Memory] Scritto record {mem_id} in {layer} da {author}")
            return mem_id
        return None

    def contextual_recall(self, current_task: str, current_agent: str, max_results: int = 5) -> Dict[str, Any]:
        """Estrae i ricordi più rilevanti basati su task, agente, recency e confidence."""
        t0 = time.time()
        db = self._read_db()
        all_records = []
        for layer, records in db.items():
            for r in records:
                if r.get("status") == "ACTIVE":
                    all_records.append(r)

        keywords = [w.lower() for w in current_task.split() if len(w) > 3]
        results = []

        for r in all_records:
            content_str = json.dumps(r.get("content", {})).lower()
            # Calcolo rilevanza basale basata su keywords
            matches = sum(1 for kw in keywords if kw in content_str)
            if len(keywords) == 0:
                relevance = 0.1
            else:
                relevance = matches / len(keywords)

            # Confidence score
            confidence = r.get("importance", 0.5) * 0.9 + (1.0 / (r.get("access_count", 0) + 1)) * 0.1
            
            # Recency in giorni
            ts_str = r.get("timestamp", "").replace("Z", "")
            try:
                age_days = (datetime.utcnow() - datetime.fromisoformat(ts_str)).days
            except Exception:
                age_days = 0
            
            recency_multiplier = max(0.1, 1.0 - (age_days / 90.0))

            final_score = relevance * recency_multiplier * confidence

            if final_score > 0.1 or matches > 0:
                # Incrementa il contatore di accessi
                r["access_count"] = r.get("access_count", 0) + 1
                r["last_accessed"] = datetime.utcnow().isoformat() + "Z"
                
                results.append({
                    "id": r["id"],
                    "source_layer": r["layer"],
                    "content": r["content"],
                    "relevance_score": round(final_score, 2),
                    "confidence": round(confidence, 2),
                    "age_days": age_days,
                    "author_agent": r["author_agent"]
                })

        # Aggiorna il DB con i nuovi access_count (senza bloccare)
        self._write_db(db, author="memory_recall_updater")

        # Ordina per score decrescente
        results = sorted(results, key=lambda x: x["relevance_score"], reverse=True)[:max_results]
        
        return {
            "results": results,
            "query_time_ms": int((time.time() - t0) * 1000),
            "total_searched": len(all_records),
            "returned": len(results)
        }

    def decision_lookup(self, decision_description: str, similarity_threshold: float = 0.75) -> Dict[str, Any]:
        """Verifica se una decisione simile è già stata registrata nel Decision Log."""
        db = self._read_db()
        decisions = db.get("decision_log", [])
        keywords = [w.lower() for w in decision_description.split() if len(w) > 3]
        
        matches_found = []
        for r in decisions:
            if r.get("status") == "ARCHIVED":
                continue
            content = r.get("content", {})
            desc = content.get("decision_description", "").lower()
            
            # Similitudine basata su keyword
            m_count = sum(1 for kw in keywords if kw in desc)
            similarity = m_count / len(keywords) if keywords else 0.0
            
            if similarity >= similarity_threshold:
                matches_found.append({
                    "id": r["id"],
                    "original_decision": content.get("decision_description"),
                    "similarity": round(similarity, 2),
                    "outcome": content.get("outcome", "PENDING"),
                    "should_reuse": content.get("outcome") == "SUCCESS",
                    "adaptation_needed": content.get("adaptation_needed", "")
                })
                
        return {
            "similar_decisions_found": len(matches_found),
            "decisions": sorted(matches_found, key=lambda x: x["similarity"], reverse=True)
        }

    def strategy_fetch(self, problem_type: str, constraints: Optional[List[str]] = None) -> Dict[str, Any]:
        """Estrae la strategia migliore per un problema dato dal Strategy Store."""
        db = self._read_db()
        strategies = db.get("strategy_store", [])
        candidates = []
        
        for r in strategies:
            if r.get("status") == "ARCHIVED":
                continue
            content = r.get("content", {})
            tags = content.get("tags", [])
            
            if problem_type.lower() in [t.lower() for t in tags]:
                # Applica constraints
                match_constraints = True
                if constraints:
                    strat_constraints = content.get("constraints", [])
                    for c in constraints:
                        if c.lower() not in [sc.lower() for sc in strat_constraints]:
                            match_constraints = False
                            break
                            
                if match_constraints:
                    candidates.append(r)
                    
        if not candidates:
            return {"recommended_strategy": None, "alternatives": []}
            
        # Ordina per success_rate (da content) e recency
        def sort_key(x):
            c_data = x.get("content", {})
            return c_data.get("success_rate", 0.0)
            
        candidates_sorted = sorted(candidates, key=sort_key, reverse=True)
        best = candidates_sorted[0]
        alts = candidates_sorted[1:]
        
        return {
            "recommended_strategy": {
                "id": best["id"],
                "name": best["content"].get("name"),
                "success_rate": best["content"].get("success_rate", 0.0),
                "times_used": best["content"].get("times_used", 0),
                "parameters": best["content"].get("parameters", {}),
                "warnings": best["content"].get("warnings", [])
            },
            "alternatives": [
                {
                    "id": a["id"],
                    "name": a["content"].get("name"),
                    "success_rate": a["content"].get("success_rate", 0.0)
                } for a in alts
            ]
        }

    def forget(self, record_id: str, reason: str, superseded_by_id: Optional[str] = None) -> bool:
        """Archiviazione strategica di un record per obsolescenza o fallimento."""
        db = self._read_db()
        found = False
        
        for layer, records in db.items():
            for r in records:
                if r.get("id") == record_id:
                    r["status"] = "ARCHIVED"
                    r["archived_at"] = datetime.utcnow().isoformat() + "Z"
                    r["forget_reason"] = reason
                    if superseded_by_id:
                        r["superseded_by"] = superseded_by_id
                    found = True
                    break
            if found:
                break
                
        if found:
            success = self._write_db(db, author="strategic_forgetter")
            if success:
                log.info(f"🧹 [Memory] Record {record_id} archiviato. Causa: {reason}")
                return True
        return False

    def write_lead(self, lead_id: str, lead_data: Dict[str, Any], author: str) -> bool:
        """Salva o aggiorna lo stato di un lead nel layer leads_store."""
        db = self._read_db()
        if "leads_store" not in db:
            db["leads_store"] = []
            
        # Trova se il lead esiste già
        found = False
        for record in db["leads_store"]:
            if record.get("id") == lead_id:
                record["content"].update(lead_data)
                record["timestamp"] = datetime.utcnow().isoformat() + "Z"
                record["author_agent"] = author
                record["version"] = record.get("version", 1) + 1
                found = True
                break
                
        if not found:
            record = {
                "id": lead_id,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "author_agent": author,
                "layer": "leads_store",
                "importance": 0.5,
                "access_count": 0,
                "version": 1,
                "status": "ACTIVE",
                "content": lead_data
            }
            db["leads_store"].append(record)
            
        return self._write_db(db, author=author)

    def get_lead(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Recupera i dati di un singolo lead dal leads_store."""
        db = self._read_db()
        for record in db.get("leads_store", []):
            if record.get("id") == lead_id and record.get("status") == "ACTIVE":
                return record["content"]
        return None
