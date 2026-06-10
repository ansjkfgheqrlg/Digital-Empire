#!/usr/bin/env python3
"""
Empire Studio - ruflo_bridge.py

Definisce la topologia swarm di Empire Studio (principi ruflo) ed emette i comandi
di orchestrazione. Quando i tool MCP ruflo sono presenti, il Conductor li usa
(swarm_init / agent_spawn / memory_store). Quando NON lo sono (come ora),
il bridge produce un piano-swarm equivalente che il Conductor esegue via il tool
Task/Agent di Claude Code. Stesso organigramma, stessa pipeline.

Uso:
  python scripts/ruflo_bridge.py --run <run-id> [--topology hierarchical]
Output: runs/<run-id>/swarm-plan.json + comandi stampati.
"""
import argparse
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
AGENTS = ROOT / "agents"

# Topologia: queen=conductor; ogni reparto e' un team; pipeline tra i reparti.
TOPOLOGY = {
    "queen": "conductor/conductor",
    "teams": {
        "ingestion": ["youtube-department", "tiktok-department", "web-department",
                      "projects-repos-workloads-department"],
        "processing": ["processing-vision-department"],
        "forge": ["forge-wiki-department"],
        "governance": ["strategy-department", "verification-control-department",
                       "memory-management-department"],
    },
    "pipeline": ["strategy", "ingestion", "processing", "verification", "forge",
                 "wiki", "update", "memory-close"],
    "patterns": {"command": "hierarchical (queen-led)",
                 "stages": "pipeline (ruflo PT02)",
                 "verification<->memory": "mesh"},
}


def list_dept_agents(dept):
    d = AGENTS / dept
    if not d.exists():
        return []
    return [f"{dept}/{p.name}" for p in d.iterdir() if p.is_dir()]


def ruflo_available():
    # I tool MCP ruflo non sono importabili come modulo; il Conductor li rileva a
    # runtime. Qui assumiamo assenza e produciamo il piano di fallback.
    return False


def build_plan(run_id, topology):
    teams = {}
    for team, depts in TOPOLOGY["teams"].items():
        agents = []
        for dept in depts:
            agents += list_dept_agents(dept)
        teams[team] = agents
    return {
        "run_id": run_id,
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "topology": topology,
        "queen": TOPOLOGY["queen"],
        "teams": teams,
        "pipeline": TOPOLOGY["pipeline"],
        "ruflo_available": ruflo_available(),
        "execution": ("ruflo swarm_init/agent_spawn" if ruflo_available()
                      else "fallback: Conductor orchestra via Task/Agent + memory_manager"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--topology", default="hierarchical")
    args = ap.parse_args()
    plan = build_plan(args.run, args.topology)
    run_dir = RUNS / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "swarm-plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[ruflo_bridge] topologia: {args.topology} (queen={plan['queen']})")
    n = sum(len(v) for v in plan["teams"].values())
    print(f"[ruflo_bridge] {n} agenti in {len(plan['teams'])} team")
    if plan["ruflo_available"]:
        print("[ruflo_bridge] ruflo disponibile -> emetto swarm_init/agent_spawn")
        print(f"  npx ruflo swarm init --topology {args.topology} --memory agentdb")
        for team, agents in plan["teams"].items():
            print(f"  # team {team}: {len(agents)} agent_spawn")
    else:
        print("[ruflo_bridge] ruflo non attivo -> FALLBACK: il Conductor orchestra via Task/Agent")
        print("  (stesso organigramma e pipeline; coordinamento + memory_manager.py)")
    print(f"[ruflo_bridge] piano -> {(run_dir / 'swarm-plan.json').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
