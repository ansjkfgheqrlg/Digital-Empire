# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 5-Layer Memory Ecosystem (Plan 1)
"""
from __future__ import annotations
import logging
import json
import os
import time
import threading
from datetime import datetime
from typing import Dict, List, Any, Optional

log = logging.getLogger("preventa-pw.memory")

class MemoryQueryInterface:
    def __init__(self, run_id: Optional[str] = None, base_dir: Optional[str] = None):
        self.run_id = run_id or f"yt-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.base_dir = base_dir or r"c:\Users\olhad\Desktop\Digital Empire\YOUTUBE-AUTOMATION-FACTORY\memory"
        
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "runs"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "decisions"), exist_ok=True)
        
        self.state_file = os.path.join(self.base_dir, "runs", f"run_{self.run_id}.json")
        self.decision_log_path = os.path.join(self.base_dir, "decision_log.json")
        self.strategy_store_path = os.path.join(self.base_dir, "strategy_store.json")
        self.snapshots_path = os.path.join(self.base_dir, "architecture_snapshots.json")
        self.learned_rules_path = os.path.join(self.base_dir, "learned_rules.json")
        self.perf_logs_path = os.path.join(self.base_dir, "performance_logs.json")
        
        self._lock_file = os.path.join(self.base_dir, ".lock")
        self._thread_local = threading.local()
        self.initialize_files()

    def initialize_files(self):
        """Inizializza i file di memoria con dati strutturati se non esistono."""
        self._acquire_lock()
        try:
            # Layer 3: Strategy Store
            if not os.path.exists(self.strategy_store_path):
                self._save_json_noblock(self.strategy_store_path, [
                    {"name": "Piramide Evolutiva", "success_rate": 0.95, "times_used": 1},
                    {"name": "Critique-Before-Output", "success_rate": 0.92, "times_used": 1},
                    {"name": "SEO-First optimization", "success_rate": 0.88, "times_used": 0}
                ])
                
            # Layer 4: Architecture Snapshots
            if not os.path.exists(self.snapshots_path):
                self._save_json_noblock(self.snapshots_path, [
                    {"version": "v1.0-APEX", "description": "APEX-7 Swarm Layout with 6 Specialists", "score": 8.5, "status": "current"}
                ])

            # Layer 5: Learned Rules
            if not os.path.exists(self.learned_rules_path):
                self._save_json_noblock(self.learned_rules_path, {
                    "blacklisted_topics": ["gaming_news"],
                    "minimum_ctr_threshold": 5.0,
                    "retry_parameters": {"max_retries": 3, "cooldown_seconds": 1}
                })

            # Working Memory
            if not os.path.exists(self.state_file):
                self._save_json_noblock(self.state_file, {
                    "run_id": self.run_id,
                    "current_phase": 1,
                    "created_at": datetime.now().isoformat()
                })
        finally:
            self._release_lock()

    def _acquire_lock(self, timeout: float = 5.0):
        """Acquisisce un lock di scrittura tramite file system."""
        start = time.time()
        while True:
            try:
                # Se il file lock esiste da più di 10 secondi, consideralo obsoleto
                try:
                    if os.path.exists(self._lock_file):
                        if time.time() - os.path.getmtime(self._lock_file) > 10.0:
                            os.remove(self._lock_file)
                except OSError:
                    pass
                
                with open(self._lock_file, "x"):
                    break
            except (FileExistsError, PermissionError):
                if time.time() - start > timeout:
                    raise TimeoutError("Impossibile acquisire il lock del database di memoria.")
                time.sleep(0.02)

    def _release_lock(self):
        """Rilascia il lock di scrittura."""
        try:
            if os.path.exists(self._lock_file):
                os.remove(self._lock_file)
        except Exception:
            pass

    def _load_json_noblock(self, path: str, default: Any) -> Any:
        if not os.path.exists(path):
            return default
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default

    def _save_json_noblock(self, path: str, data: Any):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_working_memory(self) -> Dict[str, Any]:
        self._acquire_lock()
        try:
            data = self._load_json_noblock(self.state_file, {})
            # Salva copia immutabile originale
            self._thread_local.original_data = json.loads(json.dumps(data))
            return data
        finally:
            self._release_lock()

    def save_working_memory(self, data: Dict[str, Any]):
        original = getattr(self._thread_local, "original_data", {})
        delta = {k: v for k, v in data.items() if k not in original or original[k] != v}
        
        self._acquire_lock()
        try:
            current = self._load_json_noblock(self.state_file, {})
            current.update(delta)
            self._save_json_noblock(self.state_file, current)
        finally:
            self._release_lock()

    def log_decision(self, decision_id: str, decision: str, reason: str, rejected: List[str], confidence: float):
        """Storicizza una decisione nel decision log (Layer 2)."""
        self._acquire_lock()
        try:
            log_data = self._load_json_noblock(self.decision_log_path, [])
            record = {
                "id": decision_id,
                "run_id": self.run_id,
                "decision": decision,
                "reason": reason,
                "alternatives_rejected": rejected,
                "confidence": confidence,
                "timestamp": datetime.now().isoformat()
            }
            log_data.append(record)
            self._save_json_noblock(self.decision_log_path, log_data)
            
            # Crea anche file .md
            dec_dir = os.path.join(self.base_dir, "decisions")
            md_path = os.path.join(dec_dir, f"{decision_id}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(f"# Decisione {decision_id}\n\n")
                f.write(f"- **Data**: {record['timestamp']}\n")
                f.write(f"- **Run ID**: {record['run_id']}\n")
                f.write(f"- **Scelta**: {decision}\n")
                f.write(f"- **Razionale**: {reason}\n")
                f.write(f"- **Alternative Rifiutate**: {', '.join(rejected)}\n")
                f.write(f"- **Confidence**: {confidence * 100}%\n")
                
            # Comprimi memoria se necessario
            self.compress_memory()
        finally:
            self._release_lock()

    def compress_memory(self):
        """Comprime il decision log se supera le 50 voci, archiviando le più vecchie per prevenire token bloat (L6)."""
        log_data = self._load_json_noblock(self.decision_log_path, [])
        if len(log_data) > 50:
            log.info("🧹 [Memory] Il log decisionale supera le 50 voci. Avvio archiviazione...")
            to_archive = log_data[:30]
            remaining = log_data[30:]
            
            # Salva nell'archivio storico
            archive_path = os.path.join(self.base_dir, f"decision_log_archive_{self.run_id}.json" if "test-yt" in self.run_id else "decision_log_archive.json")
            archive_data = self._load_json_noblock(archive_path, [])
            archive_data.extend(to_archive)
            self._save_json_noblock(archive_path, archive_data)
            
            # Aggiorna il log attivo
            self._save_json_noblock(self.decision_log_path, remaining)
            log.info(f"🧹 [Memory] Archiviate {len(to_archive)} decisioni vecchie. Rimanenti nel log attivo: {len(remaining)}")
