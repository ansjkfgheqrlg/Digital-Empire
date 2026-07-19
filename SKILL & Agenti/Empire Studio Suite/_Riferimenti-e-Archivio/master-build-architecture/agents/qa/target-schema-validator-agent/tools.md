# Target-Schema-Validator Agent — Tools

## Tool 1: LoadSchema
**Purpose:** Load canonical schema for a target type.
**Input:** target_type (agent | skill | plan | memory | workflow)
**Output:** schema dict with required files, sections, fields
```python
SCHEMAS = {
    "agent": {
        "required_files": ["spec.md", "system-prompt.md", "tools.md", "playbook.md",
                          "evals.md", "failure-modes.md", "memory.md"],
        "required_sections": {"system-prompt": ["invariants", "mission"],
                             "tools": ["purpose", "implementation"],
                             "failure-modes": ["table"],
                             "memory": ["mandate", "shared_state", "update_protocol"]},
        "min_file_count": 7,
        "min_fm_entries": 5,
    },
    "skill": {
        "required_files": ["SKILL.md"],
        "required_dirs": ["agents/", "references/", "scripts/", "memory/", "evals/"],
        "required_sections": {"SKILL.md": ["frontmatter", "invariants", "phases", "catalog"]},
        "max_skill_lines": 500,
    },
    "plan": {
        "required_sections": ["vision", "scope", "steps", "agents", "memory", "validation"],
        "min_steps": 3,
    },
    "memory": {
        "required_dirs": ["checkpoints/", "decisions/", "sessions/", "plans/", "architectures/"],
        "required_files": ["MEMORY-INDEX.md"],
    },
    "workflow": {
        "required_sections": ["dag", "nodes", "edges", "handoffs", "error_handling", "runbook"],
        "min_nodes": 2,
    },
}

def load_schema(target_type: str) -> dict:
    return SCHEMAS.get(target_type, {})
```

## Tool 2: ValidateTarget
**Purpose:** Validate a target against its schema.
**Input:** target_path, target_type
**Output:** {status, required, present, missing, details}
```python
def validate_target(target_path: str, target_type: str) -> dict:
    schema = load_schema(target_type)
    result = {"required": [], "present": [], "missing": [], "status": "COMPLIANT"}

    # Check required files
    for f in schema.get("required_files", []):
        result["required"].append(f)
        if os.path.exists(os.path.join(target_path, f)):
            result["present"].append(f)
        else:
            result["missing"].append(f)

    # Check required dirs
    for d in schema.get("required_dirs", []):
        result["required"].append(d)
        if os.path.isdir(os.path.join(target_path, d.rstrip('/'))):
            result["present"].append(d)
        else:
            result["missing"].append(d)

    if result["missing"]:
        result["status"] = "NON-COMPLIANT" if len(result["missing"]) > 2 else "PARTIAL"

    return result
```

## Tool 3: ValidateAllAgents
**Purpose:** Validate all agents against agent schema (PT05).
**Input:** agents_root
**Output:** {total, compliant, partial, non_compliant, details}
```python
def validate_all_agents(agents_root: str = "agents") -> dict:
    schema = load_schema("agent")
    results = []
    for cat in os.listdir(agents_root):
        cat_path = os.path.join(agents_root, cat)
        if not os.path.isdir(cat_path): continue
        for agent in os.listdir(cat_path):
            agent_path = os.path.join(cat_path, agent)
            if not os.path.isdir(agent_path): continue
            files = [f for f in os.listdir(agent_path) if f.endswith('.md')]
            file_count = len(files)
            if file_count >= schema["min_file_count"]:
                status = "COMPLIANT"
            elif file_count >= 4:
                status = "PARTIAL"
            else:
                status = "NON-COMPLIANT"
            results.append({"agent": agent, "category": cat, "file_count": file_count, "status": status})
    return {
        "total": len(results),
        "compliant": sum(1 for r in results if r["status"] == "COMPLIANT"),
        "partial": sum(1 for r in results if r["status"] == "PARTIAL"),
        "non_compliant": sum(1 for r in results if r["status"] == "NON-COMPLIANT"),
        "details": results,
    }
```

## Tool 4: MemoryManager (wrapper)
**Purpose:** Log validation run as CP.
