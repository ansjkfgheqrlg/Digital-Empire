# Coverage-Verifier Agent — Tools

## Tool 1: EnumerateSourceAtoms
**Purpose:** List all knowledge atoms from source repositories.
**Input:** scope (knowledge-pack | clones | advisor | skill-creator | user | all)
**Output:** list of {atom_id, source_path, category, summary}
**Implementation:**
```python
def enumerate_source_atoms(scope: str = "all") -> list[dict]:
    """Scan source dirs and extract atoms (principles, patterns, case studies, etc.)."""
    atoms = []
    sources = {
        "knowledge-pack": "references/knowledge-pack/",
        "clones": ["projects/ruflo/", "projects/content-forge2.0/"],
        "advisor": "projects/.agents/skills/context-engineering-advisor/",
        "skill-creator": "projects/content-forge2.0/references/external/skill-creator.md",
    }
    # Walk directories, extract .md files as atoms
    # Each atom = {id, path, category (P/PT/AP/CS/glossary/clone-section), title}
    return atoms
```

## Tool 2: EnumerateOutputAtoms
**Purpose:** List all content atoms in output artifacts.
**Input:** output_path (default: full skill directory)
**Output:** list of {atom_id, file_path, section, source_refs}
**Implementation:**
```python
def enumerate_output_atoms(output_path: str = ".") -> list[dict]:
    """Scan all output .md files and extract sections with their source citations."""
    atoms = []
    for root, dirs, files in os.walk(output_path):
        if '.git' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                # Parse sections, extract traceability headers
                # Each atom = {file, section, cited_sources: [...]}
                pass
    return atoms
```

## Tool 3: CoverageCheck
**Purpose:** Run full coverage analysis.
**Input:** scope, output_path
**Output:** CoverageReport
**Implementation:**
```python
def coverage_check(scope: str = "all", output_path: str = ".") -> dict:
    """
    Compute coverage: for each source atom, count references in outputs.
    Returns: {total, full, partial, orphan, orphan_list, coverage_pct}
    """
    sources = enumerate_source_atoms(scope)
    outputs = enumerate_output_atoms(output_path)
    # Build mapping source → [output references]
    # Classify: full (≥3), partial (1-2), orphan (0)
    report = {
        "total": len(sources),
        "full": 0, "partial": 0, "orphan": 0,
        "orphan_list": [],
        "coverage_pct": 0.0,
    }
    return report
```

## Tool 4: MemoryManager (wrapper)
**Purpose:** Log coverage run as CP in memory/.
**Input:** report dict
**Output:** CP file path
**Implementation:** Wraps `scripts/memory_manager.py checkpoint`

## Activation
- `python scripts/coverage_check.py --scope all` (standalone)
- Invoked by conductor during P6/P7 phases
