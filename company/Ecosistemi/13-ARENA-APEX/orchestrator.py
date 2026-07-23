#!/usr/bin/env python3
"""
Digital Empire — APEX Orchestrator v2.0
========================================
Ispirato ai pattern di RuFLO (swarm, memory, workflow) ma implementato
come sistema autonomo per Arena.ai.

Usa:
  python3 orchestrator.py status           → Stato del sistema
  python3 orchestrator.py memory [layer]   → Leggi un layer di memoria
  python3 orchestrator.py workflow [name]  → Esegui un workflow (dry-run)
  python3 orchestrator.py critique <file>  → Valuta qualità di un output
  python3 orchestrator.py decision <cosa> <perché> → Registra una decisione
  python3 orchestrator.py snapshot         → Salva snapshot architettura
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
MEMORY_DIR = BASE_DIR / "memory"
WORKFLOWS_DIR = BASE_DIR / "workflows"
PROMPTS_DIR = BASE_DIR / "prompts"
OUTPUT_DIR = BASE_DIR / "output"
CONFIG_FILE = BASE_DIR / "config" / "system.json"

QUALITY_THRESHOLD = 7.5
MAX_REFINEMENT_LOOPS = 3

QUALITY_DIMENSIONS = {
    "completezza": {"weight": 0.25, "threshold": 8},
    "precisione": {"weight": 0.25, "threshold": 8},
    "creativita": {"weight": 0.20, "threshold": 7},
    "actionability": {"weight": 0.20, "threshold": 8},
    "coerenza": {"weight": 0.10, "threshold": 9},
}


# ─── Memory System ───────────────────────────────────────────────────────────

class MemorySystem:
    """5-layer memory system inspired by RuFLO's AgentDB."""

    LAYERS = {
        "working": "memory/working/context.json",
        "decisions": "memory/decisions/log.json",
        "strategies": "memory/strategies/store.json",
        "architecture": "memory/architecture/snapshots.json",
        "knowledge": "memory/knowledge/base.json",
    }

    def __init__(self, base_dir: Path):
        self.base = base_dir

    def read(self, layer: str) -> dict:
        """Read a memory layer. Returns empty dict if file doesn't exist."""
        if layer not in self.LAYERS:
            raise ValueError(f"Unknown layer: {layer}. Valid: {list(self.LAYERS.keys())}")
        path = self.base / self.LAYERS[layer]
        if not path.exists():
            return {}
        with open(path) as f:
            return json.load(f)

    def write(self, layer: str, data: dict):
        """Write to a memory layer."""
        if layer not in self.LAYERS:
            raise ValueError(f"Unknown layer: {layer}")
        path = self.base / self.LAYERS[layer]
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)

    def append_decision(self, what: str, why: str, confidence: float = 0.85, tags: list = None):
        """Append a decision to the decision log."""
        log = self.read("decisions")
        entries = log.get("entries", [])
        new_id = f"DEC-{len(entries) + 1:03d}"
        entry = {
            "id": new_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "decision": what,
            "reason": why,
            "alternatives_rejected": [],
            "confidence": confidence,
            "outcome": None,
            "tags": tags or [],
        }
        entries.append(entry)
        log["entries"] = entries
        self.write("decisions", log)
        return new_id

    def update_strategy_usage(self, strategy_name: str):
        """Increment usage counter for a strategy."""
        store = self.read("strategies")
        for s in store.get("strategies", []):
            if s["name"] == strategy_name:
                s["times_used"] = s.get("times_used", 0) + 1
                s["last_used"] = datetime.now(timezone.utc).isoformat()
                break
        self.write("strategies", store)

    def get_policies(self) -> list:
        """Get active policies from knowledge base."""
        kb = self.read("knowledge")
        return kb.get("policies", [])

    def get_best_practices(self) -> list:
        """Get best practices from knowledge base."""
        kb = self.read("knowledge")
        return kb.get("best_practices", [])

    def get_anti_patterns(self) -> list:
        """Get anti-patterns to avoid."""
        kb = self.read("knowledge")
        return kb.get("anti_patterns", [])


# ─── Quality Scoring ────────────────────────────────────────────────────────

class QualityScorer:
    """Multi-dimensional quality scoring with weighted average."""

    def __init__(self):
        self.dimensions = QUALITY_DIMENSIONS

    def score(self, scores: dict) -> dict:
        """
        Calculate weighted quality score.
        scores: {"completezza": 8, "precisione": 7, ...}
        Returns: {"total": 7.65, "dimensions": {...}, "passes": True/False}
        """
        total = 0.0
        details = {}
        all_pass = True

        for dim, config in self.dimensions.items():
            value = scores.get(dim, 0)
            weighted = value * config["weight"]
            total += weighted
            passes = value >= config["threshold"]
            if not passes:
                all_pass = False
            details[dim] = {
                "score": value,
                "weight": config["weight"],
                "weighted_contribution": round(weighted, 2),
                "threshold": config["threshold"],
                "passes": passes,
            }

        return {
            "total": round(total, 2),
            "dimensions": details,
            "passes": total >= QUALITY_THRESHOLD,
            "threshold": QUALITY_THRESHOLD,
            "all_dimensions_pass": all_pass,
        }


# ─── Workflow Engine ─────────────────────────────────────────────────────────

class WorkflowEngine:
    """Execute workflow definitions with routing and critique loops."""

    def __init__(self, base_dir: Path, memory: MemorySystem):
        self.base = base_dir
        self.memory = memory

    def load_workflow(self, workflow_id: str) -> dict:
        """Load a workflow definition."""
        path = self.base / "workflows" / f"{workflow_id}-workflow.json"
        if not path.exists():
            # Try finding by name
            for f in (self.base / "workflows").glob("*-workflow.json"):
                data = json.loads(f.read_text())
                if data.get("workflow_id") == workflow_id:
                    return data
            raise FileNotFoundError(f"Workflow not found: {workflow_id}")
        with open(path) as f:
            return json.load(f)

    def list_workflows(self) -> list:
        """List all available workflows."""
        workflows = []
        for f in sorted((self.base / "workflows").glob("*-workflow.json")):
            with open(f) as fh:
                data = json.load(fh)
                workflows.append({
                    "id": data.get("workflow_id"),
                    "name": data.get("name"),
                    "stream": data.get("stream"),
                    "stages": len(data.get("stages", [])),
                })
        return workflows

    def describe_workflow(self, workflow_id: str) -> str:
        """Generate human-readable workflow description."""
        wf = self.load_workflow(workflow_id)
        lines = [
            f"═══ {wf['name']} v{wf['version']} ═══",
            f"Stream: {wf['stream']}",
            f"Trigger: {wf['trigger']}",
            f"Description: {wf['description']}",
            "",
            "STAGES:",
        ]
        for i, stage in enumerate(wf.get("stages", []), 1):
            agent = stage.get("agent", "unassigned")
            lines.append(f"  {i}. [{agent.upper()}] {stage['name']}")
            for action in stage.get("actions", []):
                lines.append(f"     → {action}")
            if "routing" in stage:
                lines.append(f"     ⤷ Routing: {json.dumps(stage['routing'])}")
        return "\n".join(lines)


# ─── Agent Roles ─────────────────────────────────────────────────────────────

AGENT_ROLES = {
    "planner": {
        "emoji": "📋",
        "name": "Planner Agent",
        "responsibilities": [
            "Decompose user input into structured briefs",
            "Identify objectives, triggers, constraints",
            "Check memory for relevant past patterns",
            "Assign priorities and route tasks",
        ],
    },
    "writer": {
        "emoji": "✍️",
        "name": "Writer Agent",
        "responsibilities": [
            "Generate content using prompt templates",
            "Apply brand tone and style guidelines",
            "Inject memory context into outputs",
            "Produce draft SKILL.md, email sequences, carousel briefs",
        ],
    },
    "analyst": {
        "emoji": "🔬",
        "name": "Analyst Agent",
        "responsibilities": [
            "Research target audiences and markets",
            "Find patterns in memory (past campaigns, results)",
            "Web search for competitive intelligence",
            "Build customer profiles and pain point maps",
        ],
    },
    "critic": {
        "emoji": "🔍",
        "name": "Critic Agent",
        "responsibilities": [
            "Score outputs on quality dimensions",
            "Identify specific weaknesses",
            "Compare against best practices in memory",
            "Gate quality: pass (≥7.5) / refine / restart",
        ],
    },
    "refiner": {
        "emoji": "🔧",
        "name": "Refiner Agent",
        "responsibilities": [
            "Apply critique feedback to drafts",
            "Strengthen weak dimensions",
            "Preserve what works, fix what doesn't",
            "Max 3 refinement iterations before restart",
        ],
    },
    "meta": {
        "emoji": "👁️",
        "name": "Meta Agent (Orchestrator)",
        "responsibilities": [
            "Observe all other agents' outputs",
            "Route workflow based on quality scores",
            "Save decisions and update memory",
            "Present final output to user",
        ],
    },
}


# ─── CLI Commands ────────────────────────────────────────────────────────────

def cmd_status():
    """Show system status."""
    config = json.loads((BASE_DIR / "config" / "system.json").read_text())
    memory = MemorySystem(BASE_DIR)

    print("╔══════════════════════════════════════════════════════╗")
    print("║         DIGITAL EMPIRE — APEX Orchestrator v2.0     ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  System: {config['system_id']:<42} ║")
    print(f"║  Version: {config['version']:<41} ║")
    print(f"║  Brand: {config['brand']['name']:<43} ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  MEMORY LAYERS                                       ║")

    for layer, path in MemorySystem.LAYERS.items():
        full_path = BASE_DIR / path
        exists = "✅" if full_path.exists() else "❌"
        size = f"{full_path.stat().st_size}B" if full_path.exists() else "N/A"
        print(f"║    {exists} {layer:<14} {size:<25}             ║")

    print("╠══════════════════════════════════════════════════════╣")
    print("║  AGENTS                                              ║")
    for agent_id, info in AGENT_ROLES.items():
        print(f"║    {info['emoji']} {info['name']:<36}          ║")

    print("╠══════════════════════════════════════════════════════╣")
    print("║  WORKFLOWS                                           ║")
    engine = WorkflowEngine(BASE_DIR, memory)
    for wf in engine.list_workflows():
        print(f"║    ▶ {wf['id']:<20} Stream {wf['stream']}  ({wf['stages']} stages) ║")

    print("╠══════════════════════════════════════════════════════╣")
    print("║  STRATEGIES (from memory)                            ║")
    strategies = memory.read("strategies").get("strategies", [])
    for s in strategies:
        used = s.get("times_used", 0)
        print(f"║    • {s['name']:<30} used: {used:<12}      ║")

    print("║                                                      ║")
    print("║  Quality Threshold: 7.5/10                           ║")
    print("║  Max Refinement Loops: 3                             ║")
    print("╚══════════════════════════════════════════════════════╝")


def cmd_memory(layer=None):
    """Read memory layer."""
    memory = MemorySystem(BASE_DIR)
    if layer:
        data = memory.read(layer)
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Available layers:", list(MemorySystem.LAYERS.keys()))
        print("\nUse: python3 orchestrator.py memory <layer>")


def cmd_workflow(workflow_id=None):
    """Describe or list workflows."""
    memory = MemorySystem(BASE_DIR)
    engine = WorkflowEngine(BASE_DIR, memory)
    if workflow_id:
        print(engine.describe_workflow(workflow_id))
    else:
        print("Available workflows:\n")
        for wf in engine.list_workflows():
            print(f"  ▶ {wf['id']:<25} {wf['name']}")
        print(f"\nUse: python3 orchestrator.py workflow <id>")


def cmd_decision(what: str, why: str):
    """Record a decision."""
    memory = MemorySystem(BASE_DIR)
    dec_id = memory.append_decision(what, why)
    print(f"✅ Decision recorded: {dec_id}")
    print(f"   What: {what}")
    print(f"   Why: {why}")


def cmd_snapshot():
    """Save architecture snapshot."""
    memory = MemorySystem(BASE_DIR)
    snapshots = memory.read("architecture")
    existing = snapshots.get("snapshots", [])
    
    new_snapshot = {
        "version": f"v{len(existing) + 1}.0",
        "date": datetime.now(timezone.utc).isoformat(),
        "description": "Manual snapshot via orchestrator",
        "score": None,
        "status": "current",
        "components": [
            f"Memory layers: {len(MemorySystem.LAYERS)}",
            f"Agents: {len(AGENT_ROLES)}",
            f"Workflows: {len(list((BASE_DIR / 'workflows').glob('*-workflow.json')))}",
            f"Prompts: {len(list((BASE_DIR / 'prompts').glob('*.md')))}",
        ],
    }
    
    # Mark previous as archived
    for s in existing:
        if s.get("status") == "current":
            s["status"] = "archived"
    
    existing.append(new_snapshot)
    snapshots["snapshots"] = existing
    memory.write("architecture", snapshots)
    print(f"✅ Snapshot saved: {new_snapshot['version']}")


def cmd_policies():
    """Show active policies."""
    memory = MemorySystem(BASE_DIR)
    policies = memory.get_policies()
    print("═══ ACTIVE POLICIES ═══\n")
    for p in policies:
        print(f"  📌 {p['name']}")
        print(f"     Rule: {p['rule']}")
        print(f"     Since: {p['enforced_since']}")
        print()


def cmd_anti_patterns():
    """Show anti-patterns to avoid."""
    memory = MemorySystem(BASE_DIR)
    patterns = memory.get_anti_patterns()
    print("═══ ANTI-PATTERNS (AVOID) ═══\n")
    for p in patterns:
        print(f"  ❌ {p}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "status":
        cmd_status()
    elif cmd == "memory":
        layer = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_memory(layer)
    elif cmd == "workflow":
        wf_id = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_workflow(wf_id)
    elif cmd == "decision":
        if len(sys.argv) < 4:
            print("Usage: python3 orchestrator.py decision '<what>' '<why>'")
            return
        cmd_decision(sys.argv[2], sys.argv[3])
    elif cmd == "snapshot":
        cmd_snapshot()
    elif cmd == "policies":
        cmd_policies()
    elif cmd == "anti-patterns":
        cmd_anti_patterns()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
