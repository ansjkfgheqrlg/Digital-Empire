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
