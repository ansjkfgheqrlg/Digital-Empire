"""
APEX-7 Memory Ecosystem - 5 Layers
Implementazione completa del sistema di memoria stratificata
"""
import json
import sqlite3
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional
import os

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

class APEX7Memory:
    def __init__(self, system_id: str = "apex7-001", domain: str = "default"):
        """domain namespaces every persisted file under data/<domain>/ so multiple
        ecosystems (youtube, stream-s7-bot, ...) can run the same engine without
        sharing state. domain="default" keeps writing to data/ directly (unchanged
        path) so existing callers (carousel-machine, skill-forge, cold-outreach)
        are unaffected."""
        self.system_id = system_id
        self.domain = domain
        self.session_id = str(uuid.uuid4())
        self.data_dir = DATA_DIR if domain == "default" else (DATA_DIR / domain)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.data_dir / "decision_log.db"
        self._init_db()

        # L1 - Working Memory (volatile)
        self.working_memory: Dict[str, Any] = {
            "session_id": self.session_id,
            "domain": self.domain,
            "current_task": None,
            "current_phase": "INIT",
            "active_agents": [],
            "context_variables": {},
            "event_bus": [],
            "checkpoints": []
        }

        # Load persistent layers
        self.strategy_store = self._load_json(self.data_dir / "strategy_store.json", [])
        self.architecture_snapshots = self._load_json(self.data_dir / "architecture_snapshots.json", [])
        self.compressed_knowledge = self._load_json(self.data_dir / "compressed_knowledge.json", {
            "lessons_learned": [],
            "best_practices": [],
            "anti_patterns": [],
            "policies": [],
            "knowledge_graph": {"nodes": [], "edges": []}
        })

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS decisions (
            id TEXT PRIMARY KEY,
            decision TEXT,
            reason TEXT,
            alternatives_rejected TEXT,
            confidence REAL,
            outcome TEXT,
            timestamp TEXT,
            agent TEXT
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS critique_history (
            id TEXT PRIMARY KEY,
            task_id TEXT,
            score REAL,
            dimensions TEXT,
            weaknesses TEXT,
            timestamp TEXT
        )
        """)
        conn.commit()
        conn.close()

    def _load_json(self, path: Path, default):
        if path.exists():
            try:
                return json.loads(path.read_text(encoding='utf-8'))
            except:
                return default
        return default

    def _save_json(self, path: Path, data):
        try:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str), encoding='utf-8')
        except Exception as e:
            # Fallback: try sanitized version
            print(f"[MEMORY SAVE WARN] {e} - trying sanitized")
            sanitized = json.loads(json.dumps(data, default=str, ensure_ascii=False))
            path.write_text(json.dumps(sanitized, indent=2, ensure_ascii=False), encoding='utf-8')

    # === L1 OPERATIONS ===
    def set_task(self, task: str, context: Dict = None):
        self.working_memory["current_task"] = task
        self.working_memory["current_phase"] = "INTAKE"
        if context:
            self.working_memory["context_variables"].update(context)
        self._checkpoint()

    def update_phase(self, phase: str):
        self.working_memory["current_phase"] = phase
        self.working_memory["event_bus"].append({
            "event": "phase_change",
            "to": phase,
            "ts": datetime.now().isoformat()
        })

    def set_active_agents(self, agents: List[str]):
        self.working_memory["active_agents"] = agents

    def _checkpoint(self):
        """Salva stato intermedio per rollback"""
        # Avoid circular reference: store only safe serializable snapshot
        safe_snapshot = {
            "current_task": self.working_memory.get("current_task"),
            "current_phase": self.working_memory.get("current_phase"),
            "active_agents": self.working_memory.get("active_agents", []),
            "context_variables_keys": list(self.working_memory.get("context_variables", {}).keys())
        }
        cp = {
            "id": str(uuid.uuid4())[:8],
            "timestamp": datetime.now().isoformat(),
            "working_memory_snapshot": safe_snapshot,
            "phase": self.working_memory.get("current_phase", "UNKNOWN")
        }
        # In working_memory checkpoints store only id + phase to avoid bloat/circular
        self.working_memory.setdefault("checkpoints", [])
        self.working_memory["checkpoints"].append({"id": cp["id"], "phase": cp["phase"], "timestamp": cp["timestamp"]})
        self.working_memory["checkpoints"] = self.working_memory["checkpoints"][-10:]
        try:
            self._save_json(self.data_dir / f"checkpoint_{cp['id']}.json", cp)
        except Exception as e:
            print(f"[MEMORY CHECKPOINT WARN] {e}")
        return cp["id"]

    def rollback(self, checkpoint_id: str = None):
        if not self.working_memory["checkpoints"]:
            return False
        target = None
        if checkpoint_id:
            target = next((c for c in self.working_memory["checkpoints"] if c["id"] == checkpoint_id), None)
        else:
            target = self.working_memory["checkpoints"][-2] if len(self.working_memory["checkpoints"]) > 1 else None
        
        if target:
            self.working_memory = target["working_memory"]
            self.working_memory["event_bus"].append({
                "event": "rollback",
                "to_checkpoint": target["id"],
                "ts": datetime.now().isoformat()
            })
            return True
        return False

    # === L2 DECISION LOG ===
    def log_decision(self, decision: str, reason: str, alternatives: List[str], confidence: float, agent: str = "meta"):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        dec_id = f"DEC-{str(uuid.uuid4())[:8].upper()}"
        c.execute("""
        INSERT INTO decisions (id, decision, reason, alternatives_rejected, confidence, timestamp, agent)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            dec_id,
            decision,
            reason,
            json.dumps(alternatives, ensure_ascii=False),
            confidence,
            datetime.now().isoformat(),
            agent
        ))
        conn.commit()
        conn.close()
        return dec_id

    def get_recent_decisions(self, limit=20):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM decisions ORDER BY timestamp DESC LIMIT ?", (limit,))
        rows = c.fetchall()
        conn.close()
        return rows

    def log_critique(self, task_id: str, score: float, dimensions: Dict, weaknesses: List[str]):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        cid = str(uuid.uuid4())
        c.execute("""
        INSERT INTO critique_history (id, task_id, score, dimensions, weaknesses, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cid, task_id, score,
            json.dumps(dimensions, ensure_ascii=False),
            json.dumps(weaknesses, ensure_ascii=False),
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()
        return cid

    # === L3 STRATEGY STORE ===
    def save_strategy(self, name: str, description: str, use_cases: List[str], parameters: Dict = None, score: float = None):
        existing = next((s for s in self.strategy_store if s["name"] == name), None)
        if existing:
            existing["times_used"] = existing.get("times_used", 0) + 1
            existing["last_used"] = datetime.now().isoformat()
            if score is not None:
                existing.setdefault("score_history", []).append(score)
                existing["success_rate"] = sum(existing["score_history"]) / len(existing["score_history"])
        else:
            self.strategy_store.append({
                "name": name,
                "description": description,
                "use_cases": use_cases,
                "parameters": parameters or {},
                "times_used": 1,
                "last_used": datetime.now().isoformat(),
                "success_rate": score,
                "score_history": [score] if score else []
            })
        self._save_json(self.data_dir / "strategy_store.json", self.strategy_store)

    def get_best_strategies(self, use_case: str = None, min_score: float = 7.0):
        filtered = self.strategy_store
        if use_case:
            filtered = [s for s in filtered if use_case in s.get("use_cases", []) or use_case == "all"]
        return [s for s in filtered if (s.get("success_rate") or 0) >= min_score or s.get("success_rate") is None]

    # === L4 ARCHITECTURE SNAPSHOTS ===
    def snapshot_architecture(self, version: str, description: str, config: Dict, agents: List[str], metrics: Dict, score: float):
        prev = self.architecture_snapshots[-1] if self.architecture_snapshots else None
        diff = f"Previous: {prev['version'] if prev else 'none'} -> {version}" if prev else "Initial version"
        snap = {
            "version": version,
            "description": description,
            "config": config,
            "agents": agents,
            "workflows": ["apex7_prompt_generation"],
            "performance_metrics": metrics,
            "diff_from_previous": diff,
            "score": score,
            "status": "current",
            "timestamp": datetime.now().isoformat()
        }
        # deprecate old current
        for s in self.architecture_snapshots:
            if s.get("status") == "current":
                s["status"] = "deprecated"
        self.architecture_snapshots.append(snap)
        self._save_json(self.data_dir / "architecture_snapshots.json", self.architecture_snapshots)
        return snap

    # === L5 COMPRESSED KNOWLEDGE + AUTO-COMPRESSION ===
    def compress_memories(self):
        """Regola: sessioni >30gg -> lesson learned, decisioni ripetute >5 -> policy"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT decision, COUNT(*) as cnt FROM decisions GROUP BY decision HAVING cnt > 5")
        repeated = c.fetchall()
        for dec, cnt in repeated:
            policy = f"POLICY: {dec} (ripetuta {cnt} volte) -> standardizza"
            if policy not in self.compressed_knowledge["policies"]:
                self.compressed_knowledge["policies"].append(policy)
        
        # Strategie con score >8 -> best practice, <4 -> anti-pattern
        for strat in self.strategy_store:
            sr = strat.get("success_rate") or 0
            if sr >= 8.0 and strat["name"] not in self.compressed_knowledge["best_practices"]:
                self.compressed_knowledge["best_practices"].append(f"{strat['name']}: {strat['description']}")
            elif sr < 4.0 and sr > 0 and strat["name"] not in self.compressed_knowledge["anti_patterns"]:
                self.compressed_knowledge["anti_patterns"].append(f"{strat['name']}: {strat['description']}")

        conn.close()
        self._save_json(self.data_dir / "compressed_knowledge.json", self.compressed_knowledge)

    def add_lesson(self, lesson: str):
        if lesson not in self.compressed_knowledge["lessons_learned"]:
            self.compressed_knowledge["lessons_learned"].append(lesson)
            self._save_json(self.data_dir / "compressed_knowledge.json", self.compressed_knowledge)

    # === GLOBAL SAVE ===
    def persist(self):
        # Sanitize working_memory to avoid circular/complex
        safe_wm = {
            "session_id": self.working_memory.get("session_id"),
            "current_task": str(self.working_memory.get("current_task",""))[:500],
            "current_phase": self.working_memory.get("current_phase"),
            "active_agents": self.working_memory.get("active_agents", []),
            "checkpoints": self.working_memory.get("checkpoints", [])[-5:],
            "event_bus_count": len(self.working_memory.get("event_bus", [])),
            "context_keys": list(self.working_memory.get("context_variables", {}).keys())
        }
        self._save_json(self.data_dir / f"working_memory_{self.session_id}.json", safe_wm)
        self._save_json(self.data_dir / "strategy_store.json", self.strategy_store)
        self._save_json(self.data_dir / "compressed_knowledge.json", self.compressed_knowledge)
        try:
            decisions_count = len(self.get_recent_decisions(1000))
        except:
            decisions_count = -1
        print(f"[MEMORY] Persisted session {self.session_id} | Decisions: {decisions_count} | Strategies: {len(self.strategy_store)}")

# === INIT WITH SEED DATA FROM YOUR ARCHITECTURE ===
def seed_memory():
    mem = APEX7Memory()
    # Seed from your FASE 3
    mem.log_decision("Ripartire da zero con architettura completa", "Prima risposta era superficiale e reattiva", ["Migliorare incrementale", "Chiedere chiarimenti"], 0.95, "meta")
    mem.log_decision("Usare piramide evolutiva per 7 livelli", "Ogni livello migliora precedente = qualità crescente", ["7 livelli paralleli", "7 sequenziali senza evoluzione"], 0.90, "planner")
    mem.log_decision("5 layer di memoria, non 3", "3 troppo piatti, 5 copre tutti casi d'uso", ["3 layer", "7 layer troppo complesso"], 0.88, "planner")
    mem.log_decision("Integrare RuFLO come orchestrator core", "Performance Rust + task decomposition nativa", ["Orchestrator custom", "Solo Python"], 0.92, "meta")
    
    mem.save_strategy("Piramide Evolutiva", "Ogni livello è il migliore del precedente", ["planning", "architecture"], {"levels": 7}, 8.5)
    mem.save_strategy("Critique-Before-Output", "Auto-critica prima di rilasciare output", ["quality_control", "all_outputs"], {}, 9.0)
    mem.save_strategy("Memory-First Design", "Ogni azione memorizzata con contesto", ["system_design", "persistence"], {}, 8.8)
    
    mem.compressed_knowledge["lessons_learned"] = [
        "Mai rispondere in modo reattivo senza proporre struttura",
        "La memoria è il fondamento di ogni sistema intelligente",
        "Multi-agente > singolo agente per task complessi",
        "Autocritica deve essere sistematica, non opzionale"
    ]
    mem.compressed_knowledge["best_practices"] = [
        "Planning a livelli con evoluzione progressiva",
        "Feedback loop obbligatorio su ogni output",
        "Salvare il PERCHÉ delle decisioni, non solo il COSA"
    ]
    mem.compressed_knowledge["anti_patterns"] = [
        "Risposta piatta senza architettura",
        "Chiedere input senza offrire valore",
        "Output senza auto-valutazione"
    ]
    
    mem.snapshot_architecture("v7.0-APEX", "Full system con swarm + memory + ruflo", {"orchestrator": "ruflo", "memory_layers": 5}, ["planner", "writer", "analyst", "critic", "refiner", "meta"], {"latency_ms": 120, "quality": 8.5}, 8.5)
    mem.persist()
    return mem

if __name__ == "__main__":
    mem = seed_memory()
    print("Memory seeded. Recent decisions:")
    for row in mem.get_recent_decisions(5):
        print(row)
