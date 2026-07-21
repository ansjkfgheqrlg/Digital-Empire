"""Valida output del builder contro JSON Schema + integrità referenziale custom.

Used by: C3 target-schema-validator-agent.
Part of: content-forge

Usage:
    python scripts/schema_validator.py --target <target> --output-dir <path> [--json]

Exit code:
    0 = PASS
    1 = FAIL
    2 = errore
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.frontmatter import parse as parse_fm
from lib.markdown_tools import extract_headings, extract_wikilinks


VALID_TARGETS = ["doc", "agent", "team", "skill", "workflow", "orchestration", "wiki", "custom", "mkd", "sources"]


def load_schema(schema_dir: Path, target: str) -> dict | None:
    """Carica references/schemas/<target>.schema.json se esiste."""
    p = schema_dir / f"{target}.schema.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def check_required_files(output_dir: Path, required: list[str]) -> list[dict]:
    """Verifica che i file canonici esistano in output_dir."""
    issues = []
    for rel in required:
        if not (output_dir / rel).exists():
            # Cerca anche nelle sotto-cartelle (es. agents/, scripts/)
            matches = list(output_dir.rglob(Path(rel).name))
            if not matches:
                issues.append({
                    "id": f"missing-file-{rel}",
                    "category": "structural",
                    "passed": False,
                    "severity": "error",
                    "evidence": f"File canonico mancante: {rel}",
                    "fix_hint": f"Il builder deve produrre {rel}",
                })
    return issues


def check_frontmatter(file_path: Path, required_keys: list[str]) -> list[dict]:
    """Verifica che il frontmatter abbia le chiavi richieste."""
    issues = []
    if not file_path.exists():
        return issues
    try:
        fm, _ = parse_fm(file_path)
    except Exception as e:
        return [{
            "id": f"frontmatter-parse-{file_path.name}",
            "category": "frontmatter",
            "passed": False, "severity": "error",
            "evidence": f"Parse fallito: {e}",
            "fix_hint": "Frontmatter YAML non valido",
        }]
    if fm is None:
        issues.append({
            "id": f"frontmatter-missing-{file_path.name}",
            "category": "frontmatter",
            "passed": False, "severity": "error",
            "evidence": "Frontmatter assente",
            "fix_hint": "Aggiungere blocco YAML --- ... ---",
        })
        return issues
    for k in required_keys:
        if k not in fm:
            issues.append({
                "id": f"frontmatter-missing-key-{k}",
                "category": "frontmatter",
                "passed": False, "severity": "error",
                "evidence": f"Chiave '{k}' mancante in frontmatter",
                "fix_hint": f"Aggiungere {k}: <valore>",
            })
    return issues


def check_wikilink_integrity_dir(output_dir: Path) -> list[dict]:
    """Per target wiki: verifica che ogni [[link]] punti a file esistente."""
    sys.path.insert(0, str(Path(__file__).parent))
    from lib.obsidian import check_wikilink_integrity
    issues = []
    broken = check_wikilink_integrity(output_dir)
    for b in broken:
        issues.append({
            "id": f"broken-wikilink-{b['target']}",
            "category": "referential",
            "passed": False, "severity": "error",
            "evidence": f"{b['file']} → [[{b['target']}]] non risolve",
            "fix_hint": f"Creare la nota {b['target']}.md o aggiungere alias",
        })
    return issues


def check_skill_md_size(skill_md: Path, max_lines: int = 500) -> list[dict]:
    if not skill_md.exists():
        return []
    lines = skill_md.read_text(encoding="utf-8").count("\n")
    if lines > max_lines:
        return [{
            "id": "skill-md-too-large",
            "category": "custom",
            "passed": False, "severity": "warning",
            "evidence": f"SKILL.md ha {lines} righe (max {max_lines})",
            "fix_hint": "Spostare contenuto in references/ via progressive disclosure",
        }]
    return []


def check_description_pushy(skill_md: Path) -> list[dict]:
    import re
    if not skill_md.exists():
        return []
    fm, _ = parse_fm(skill_md)
    if not fm or "description" not in fm:
        return []
    desc = fm["description"]
    markers = [r"make sure", r"whenever", r"even if", r"always", r"use this"]
    pushy = any(re.search(m, desc, re.I) for m in markers)
    if not pushy:
        return [{
            "id": "description-not-pushy",
            "category": "custom",
            "passed": False, "severity": "warning",
            "evidence": "description non contiene marker pushy anti-undertriggering",
            "fix_hint": "Aggiungere 'Make sure to use this whenever...' o simile",
        }]
    return []


def validate_target(target: str, output_dir: Path, schema_dir: Path) -> dict:
    """Esegui validazione completa per il target."""
    schema = load_schema(schema_dir, target)
    issues: list[dict] = []

    if not schema:
        return {
            "verdict": "FAIL",
            "target": target,
            "schema_version": "unknown",
            "checks": [{
                "id": "schema-not-found",
                "category": "structural",
                "passed": False, "severity": "error",
                "evidence": f"Schema references/schemas/{target}.schema.json non trovato",
                "fix_hint": "Creare lo schema o verificare il nome del target",
            }],
            "summary_counts": {"errors": 1, "warnings": 0, "infos": 0},
        }

    props = schema.get("properties", {})

    # Check required_files
    req_files_spec = props.get("required_files", {})
    required_files = req_files_spec.get("const", []) if isinstance(req_files_spec, dict) else []
    issues.extend(check_required_files(output_dir, required_files))

    # Target-specific custom checks
    if target == "skill":
        skill_md = output_dir / "SKILL.md"
        issues.extend(check_skill_md_size(skill_md))
        issues.extend(check_description_pushy(skill_md))
    if target == "wiki":
        issues.extend(check_wikilink_integrity_dir(output_dir))

    # Frontmatter check per il "main file" (dipende dal target)
    main_file_map = {
        "agent": ("agent.md", ["name", "display_name"]),
        "skill": ("SKILL.md", ["name", "description"]),
        "doc": ("document.md", ["title", "generated_by"]),
    }
    if target in main_file_map:
        fname, keys = main_file_map[target]
        main_path = output_dir / fname
        if not main_path.exists():
            # cerca ricorsivo
            matches = list(output_dir.rglob(fname))
            if matches:
                main_path = matches[0]
        issues.extend(check_frontmatter(main_path, keys))

    # Conta severity
    errors = sum(1 for i in issues if i["severity"] == "error")
    warnings = sum(1 for i in issues if i["severity"] == "warning")

    verdict = "PASS" if errors == 0 and warnings == 0 else ("WARN" if errors == 0 else "FAIL")

    return {
        "verdict": verdict,
        "target": target,
        "schema_version": schema.get("schema_version", "unknown"),
        "checks": issues,
        "summary_counts": {"errors": errors, "warnings": warnings, "infos": 0},
    }




# === Phase 9 — Nuovi check stringenti (PLAN-v6) ===

def check_skill_min_references(skill_dir: Path, min_refs: int = 3) -> list[dict]:
    """Bloccante: una skill con <3 reference è uno scaffold."""
    refs_dir = skill_dir / "references"
    if not refs_dir.exists():
        return [{
            "id": f"skill-no-references-{skill_dir.name}",
            "category": "phase9-depth",
            "passed": False, "severity": "error",
            "evidence": f"{skill_dir.name}: references/ directory missing",
            "fix_hint": "re-spawn O1 (skill-depth-agent) for this skill"
        }]
    refs = list(refs_dir.rglob("*.md"))
    if len(refs) < min_refs:
        return [{
            "id": f"skill-min-{min_refs}-refs-{skill_dir.name}",
            "category": "phase9-depth",
            "passed": False, "severity": "error",
            "evidence": f"{skill_dir.name}: only {len(refs)} references, required {min_refs}+",
            "fix_hint": "re-spawn O1 (skill-depth-agent)"
        }]
    return []


def check_agent_canonical_files(agent_dir: Path, min_files: int = 5) -> list[dict]:
    """Bloccante: agente con <5/7 file canonici è incompleto."""
    canonical = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    present = [f for f in canonical if (agent_dir / f).exists()]
    issues = []
    if len(present) < min_files:
        missing = list(set(canonical) - set(present))
        issues.append({
            "id": f"agent-min-{min_files}-files-{agent_dir.name}",
            "category": "phase9-depth",
            "passed": False, "severity": "error",
            "evidence": f"{agent_dir.name}: {len(present)}/{len(canonical)} files present, required {min_files}+. Missing: {missing}",
            "fix_hint": "re-spawn O2 (agent-depth-agent) for this agent"
        })

    # Check content minimums se file presenti
    if (agent_dir / "agent.md").exists():
        wc = len((agent_dir / "agent.md").read_text().split())
        if wc < 400:
            issues.append({
                "id": f"agent-md-min-400w-{agent_dir.name}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{agent_dir.name}/agent.md: only {wc} words, min 400",
                "fix_hint": "re-spawn O2 to expand agent.md"
            })

    if (agent_dir / "system_prompt.md").exists():
        wc = len((agent_dir / "system_prompt.md").read_text().split())
        if wc < 500:
            issues.append({
                "id": f"sp-min-500w-{agent_dir.name}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{agent_dir.name}/system_prompt.md: only {wc} words, min 500",
                "fix_hint": "re-spawn O2 to expand SP"
            })
        elif wc > 1500:
            issues.append({
                "id": f"sp-max-1500w-{agent_dir.name}",
                "category": "phase9-depth",
                "passed": False, "severity": "warning",
                "evidence": f"{agent_dir.name}/system_prompt.md: {wc} words, max 1500 (lost-in-the-middle risk)",
                "fix_hint": "split SP content into references"
            })

    if (agent_dir / "playbook.md").exists():
        # Count conversation headers (## numero. categoria)
        import re
        content = (agent_dir / "playbook.md").read_text()
        conv_count = len(re.findall(r"^##\s+\d+\.", content, re.MULTILINE))
        if conv_count < 5:
            issues.append({
                "id": f"playbook-min-5-conv-{agent_dir.name}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{agent_dir.name}/playbook.md: only {conv_count} conversations, min 5",
                "fix_hint": "re-spawn O2 to add more playbook conversations"
            })

    if (agent_dir / "failure_modes.md").exists():
        import re
        content = (agent_dir / "failure_modes.md").read_text()
        # Count table rows (lines starting with | fm-)
        fm_count = len(re.findall(r"^\|\s*fm-\d+", content, re.MULTILINE))
        if fm_count < 7:
            issues.append({
                "id": f"failure-modes-min-7-{agent_dir.name}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{agent_dir.name}/failure_modes.md: only {fm_count} failures, min 7",
                "fix_hint": "re-spawn O2 to expand failure_modes table"
            })

    return issues




def check_complex_skill_has_agents(skill_dir: Path) -> list[dict]:
    """Warning: skill con pipeline/stages multipli dovrebbe avere agenti."""
    refs_dir = skill_dir / "references"
    if not refs_dir.exists():
        return []  # already caught by check_skill_min_references

    # Heuristic: skill è "complex" se ha stages/ con >=3 file, o processes/ con >=2
    stages_dir = refs_dir / "stages"
    processes_dir = refs_dir / "processes"

    is_complex = False
    reason = ""
    if stages_dir.exists() and len(list(stages_dir.glob("*.md"))) >= 3:
        is_complex = True
        reason = f"{len(list(stages_dir.glob('*.md')))} stages → multi-stage pipeline"
    elif processes_dir.exists() and len(list(processes_dir.glob("*.md"))) >= 2:
        is_complex = True
        reason = f"{len(list(processes_dir.glob('*.md')))} processes → multi-process workflow"

    if not is_complex:
        return []  # skill semplice, no agenti necessari

    # È complessa: ha agenti?
    agents_dir = skill_dir / "agents"
    if not agents_dir.exists() or len(list(agents_dir.rglob("*.md"))) == 0:
        return [{
            "id": f"complex-skill-no-agents-{skill_dir.name}",
            "category": "phase9-depth",
            "passed": False, "severity": "warning",
            "evidence": f"{skill_dir.name}: complex skill ({reason}) ma senza agenti interni. "
                       f"Skill di questa complessità beneficiano di agenti specialisti (operativi, verificatori, humanizer).",
            "fix_hint": "Considera di aggiungere agents/ con: 1 agente operativo per stage principale + 1 agente QA + 1 agente humanizer (se output testuale)"
        }]
    return []




def check_agent_canonical_files_single_file(agent_dir: Path, slug: str, min_files: int = 5) -> list[dict]:
    """Verifica file canonici per agenti in convention 'single-file con companions' (Phase 9).

    Esempio: agents/operativi/discovery-agent.md + discovery-agent.system_prompt.md + ...
    """
    canonical_suffixes = [
        ".md",                  # main agent file
        ".system_prompt.md",
        ".tools.md",
        ".playbook.md",
        ".failure_modes.md",
        ".eval_cases.json",
        ".README.md",
    ]
    present = [s for s in canonical_suffixes if (agent_dir / f"{slug}{s}").exists()]
    issues = []
    if len(present) < min_files:
        missing = [s for s in canonical_suffixes if s not in present]
        issues.append({
            "id": f"agent-min-{min_files}-files-{slug}",
            "category": "phase9-depth",
            "passed": False, "severity": "error",
            "evidence": f"{slug} ({agent_dir}): {len(present)}/{len(canonical_suffixes)} files present, required {min_files}+. Missing: {missing}",
            "fix_hint": "re-spawn O2 (agent-depth-agent) for this agent"
        })

    # Check content minimums per file principali
    main_file = agent_dir / f"{slug}.md"
    if main_file.exists():
        wc = len(main_file.read_text().split())
        if wc < 400:
            issues.append({
                "id": f"agent-md-min-400w-{slug}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{slug}.md: only {wc} words, min 400",
                "fix_hint": "re-spawn O2 to expand agent.md"
            })

    sp_file = agent_dir / f"{slug}.system_prompt.md"
    if sp_file.exists():
        wc = len(sp_file.read_text().split())
        if wc < 500:
            issues.append({
                "id": f"sp-min-500w-{slug}",
                "category": "phase9-depth",
                "passed": False, "severity": "error",
                "evidence": f"{slug}.system_prompt.md: only {wc} words, min 500",
                "fix_hint": "re-spawn O2 to expand SP"
            })

    return issues


def run_phase9_checks(target: str, output_dir: Path) -> list[dict]:
    """Esegue tutti i check Phase 9 sull'output."""
    all_issues = []

    # Trova tutte le skill (root + nested)
    skill_mds = list(output_dir.rglob("SKILL.md"))
    for skill_md in skill_mds:
        # Skip path di test/build
        import re
        if re.search(r"/(phase\d+-(run|regression)|packaged-final)/", str(skill_md)):
            continue
        all_issues.extend(check_skill_min_references(skill_md.parent))
        all_issues.extend(check_complex_skill_has_agents(skill_md.parent))

    # Trova tutti gli agenti (root + nested) — heuristics multiple
    import re
    skip_pattern = re.compile(r"/(phase\d+-(run|regression)|packaged-final)/")
    found_agent_dirs = set()

    # Heuristic 1: file 'agent.md' (path canonico)
    for agent_md in output_dir.rglob("agent.md"):
        if skip_pattern.search(str(agent_md)):
            continue
        found_agent_dirs.add(agent_md.parent)

    # Heuristic 2: file *-agent.md (Phase 9 convention)
    for f in output_dir.rglob("*-agent.md"):
        if skip_pattern.search(str(f)):
            continue
        # Tratta la cartella + slug come agente
        # Per agenti single-file convention: il file stesso è l'agent.md
        found_agent_dirs.add((f.parent, f.stem))  # tuple per agenti single-file

    # Heuristic 3: qualunque file .md dentro 'agents/' folder (anche sub-folder) che non sia companion file
    COMPANION_SUFFIXES = [".system_prompt.md", ".tools.md", ".playbook.md",
                          ".failure_modes.md", ".eval_cases.json", ".README.md"]
    for f in output_dir.rglob("*.md"):
        if skip_pattern.search(str(f)):
            continue
        # Skip se è companion file
        if any(f.name.endswith(suffix) for suffix in COMPANION_SUFFIXES):
            continue
        # Deve essere dentro una cartella chiamata 'agents' (anche se nested)
        if "agents" not in f.parts:
            continue
        # Skip i file index/readme della cartella agents/ stessa
        if f.name.lower() in ("readme.md", "index.md", "_index.md"):
            continue
        # È un agente
        found_agent_dirs.add((f.parent, f.stem))

    # Check ogni "agente" trovato (potrebbe essere dir tradizionale o single-file slug)
    for entry in found_agent_dirs:
        if isinstance(entry, tuple):
            # Single-file agent convention: cerca file companion con stesso slug
            agent_dir, slug = entry
            all_issues.extend(check_agent_canonical_files_single_file(agent_dir, slug))
        else:
            # Traditional dir convention
            all_issues.extend(check_agent_canonical_files(entry))

    return all_issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--target", required=True, choices=VALID_TARGETS)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--schema-dir", type=Path,
                        default=Path(__file__).parent.parent / "references" / "schemas")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not args.output_dir.exists():
        print(f"ERROR: output-dir non esiste: {args.output_dir}", file=sys.stderr)
        return 2

    result = validate_target(args.target, args.output_dir, args.schema_dir)

    # Phase 9 — Run additional depth checks
    phase9_issues = run_phase9_checks(args.target, args.output_dir)
    if phase9_issues:
        result["checks"].extend(phase9_issues)
        # Re-compute verdict
        errors = sum(1 for c in result["checks"] if c.get("severity") == "error")
        warnings = sum(1 for c in result["checks"] if c.get("severity") == "warning")
        result["summary_counts"] = {"errors": errors, "warnings": warnings, "infos": 0}
        if errors > 0:
            result["verdict"] = "FAIL"
        elif warnings > 0 and result["verdict"] == "PASS":
            result["verdict"] = "WARN"
        result["phase9_checks_run"] = True
        result["phase9_issues_found"] = len(phase9_issues)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}[result["verdict"]]
        c = result["summary_counts"]
        print(f"{icon} Schema validation [{args.target}]: {result['verdict']} "
              f"({c['errors']} errors, {c['warnings']} warnings)")
        for chk in result["checks"]:
            sev_icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}[chk["severity"]]
            print(f"  {sev_icon} {chk['id']}: {chk['evidence']}")
            if chk.get("fix_hint"):
                print(f"     → fix: {chk['fix_hint']}")

    return 0 if result["verdict"] in ("PASS", "WARN") else 1


if __name__ == "__main__":
    sys.exit(main())
