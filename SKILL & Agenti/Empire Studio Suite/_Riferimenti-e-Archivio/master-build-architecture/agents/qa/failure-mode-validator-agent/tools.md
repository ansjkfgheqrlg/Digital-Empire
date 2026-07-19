# Failure-Mode-Validator Agent — Tools

## Tool 1: ScanAgentDirectory
**Purpose:** List all agent directories in agents/.
**Input:** agents_root (default: agents/)
**Output:** list of {agent_name, path, category}
```python
def scan_agent_directory(agents_root: str = "agents") -> list[dict]:
    agents = []
    for category in os.listdir(agents_root):
        cat_path = os.path.join(agents_root, category)
        if os.path.isdir(cat_path):
            for agent in os.listdir(cat_path):
                agent_path = os.path.join(cat_path, agent)
                if os.path.isdir(agent_path):
                    agents.append({"name": agent, "path": agent_path, "category": category})
    return agents
```

## Tool 2: ValidateFailureModes
**Purpose:** Check a single agent's failure-modes.md.
**Input:** agent_path
**Output:** {exists, entry_count, has_table, has_si_refs, has_memory_refs, status}
```python
def validate_failure_modes(agent_path: str) -> dict:
    fm_path = os.path.join(agent_path, "failure-modes.md")
    if not os.path.exists(fm_path):
        return {"exists": False, "status": "MISSING"}
    content = open(fm_path).read()
    # Count table rows (lines starting with |)
    table_rows = [l for l in content.split('\n') if l.strip().startswith('|') and '---' not in l and 'Failure' not in l]
    entry_count = len(table_rows)
    has_si_refs = any(x in content.lower() for x in ['si', 'silent', 'failure-detector', 'triage'])
    has_memory_refs = any(x in content.lower() for x in ['memory', 'cp', 'checkpoint', 'p10'])
    status = "COMPLIANT" if entry_count >= 5 and has_si_refs and has_memory_refs else "PARTIAL"
    return {"exists": True, "entry_count": entry_count, "has_table": True,
            "has_si_refs": has_si_refs, "has_memory_refs": has_memory_refs, "status": status}
```

## Tool 3: ValidateAllAgents
**Purpose:** Run validation on all agents.
**Input:** agents_root
**Output:** {total, compliant, partial, missing, details}
```python
def validate_all_agents(agents_root: str = "agents") -> dict:
    agents = scan_agent_directory(agents_root)
    results = []
    for agent in agents:
        result = validate_failure_modes(agent["path"])
        result["agent"] = agent["name"]
        result["category"] = agent["category"]
        results.append(result)
    return {
        "total": len(results),
        "compliant": sum(1 for r in results if r["status"] == "COMPLIANT"),
        "partial": sum(1 for r in results if r["status"] == "PARTIAL"),
        "missing": sum(1 for r in results if r["status"] == "MISSING"),
        "details": results,
    }
```

## Tool 4: MemoryManager (wrapper)
**Purpose:** Log validation run as CP.
**Implementation:** Wraps `scripts/memory_manager.py checkpoint`
