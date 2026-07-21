"""Per il target wiki: normalizza slug, verifica integrità wikilink, genera MOC.

Used by: B7 wiki-builder-agent.
Part of: content-forge

Usage:
    python scripts/obsidian_packager.py <vault_import_dir> [--check-only] [--moc-style categorical] [--json]

Exit code:
    0 = OK
    1 = wikilink rotti trovati
    2 = errore
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.obsidian import check_wikilink_integrity, build_alias_index, slugify


def normalize_slugs(vault_dir: Path, style: str = "kebab") -> list[dict]:
    """Verifica che ogni filename rispetti la slug convention."""
    issues = []
    for f in vault_dir.rglob("*.md"):
        # Skippa file speciali che hanno naming custom legittimo
        if f.name.startswith("MOC ") or f.name == "_Index.md" or f.parent.name == "_meta" or f.name == "README.md":
            continue
        expected = slugify(f.stem, style=style)
        if expected != f.stem:
            issues.append({
                "file": str(f.relative_to(vault_dir)),
                "current_slug": f.stem,
                "expected_slug": expected,
            })
    return issues


def build_moc_categorical(vault_dir: Path, topic: str = "Imported Content") -> str:
    """Genera MOC categorical (concept/framework/procedure/example/glossary)."""
    categories = {
        "concepts": ("🌱 Concetti", "concepts"),
        "frameworks": ("🧠 Framework e modelli", "frameworks"),
        "procedures": ("🛠 Procedure", "procedures"),
        "examples": ("📚 Esempi", "examples"),
        "glossary": ("📖 Glossario", "glossary"),
    }

    lines = [
        f"---",
        f"title: MOC — {topic}",
        f"tags: [moc, source/forge-import]",
        f"---",
        "",
        f"# MOC — {topic}",
        "",
        "> Map of Content auto-generata da `content-forge`. Riorganizza secondo preferenze.",
        "",
    ]

    for cat_dir, (label, _) in categories.items():
        dir_path = vault_dir / cat_dir
        if not dir_path.exists():
            continue
        notes = sorted([p for p in dir_path.glob("*.md")])
        if not notes:
            continue
        lines.append(f"## {label}")
        lines.append("")
        for note in notes:
            lines.append(f"- [[{note.stem}]]")
        lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("vault_import_dir", type=Path)
    parser.add_argument("--check-only", action="store_true", help="Solo verifica integrità")
    parser.add_argument("--moc-style", default="categorical",
                        choices=["categorical", "tag-based", "flat"])
    parser.add_argument("--topic", default="Imported Content", help="Topic per MOC title")
    parser.add_argument("--slug-style", default="kebab", choices=["kebab", "snake", "title"])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not args.vault_import_dir.exists():
        print(f"ERROR: dir non esiste: {args.vault_import_dir}", file=sys.stderr)
        return 2

    result = {
        "vault_dir": str(args.vault_import_dir),
        "check_only": args.check_only,
    }

    # 1. Check wikilink integrity (sempre)
    broken = check_wikilink_integrity(args.vault_import_dir)
    result["broken_wikilinks"] = broken
    result["broken_count"] = len(broken)

    # 2. Slug consistency
    slug_issues = normalize_slugs(args.vault_import_dir, style=args.slug_style)
    result["slug_issues"] = slug_issues
    result["slug_issues_count"] = len(slug_issues)

    # 3. Total notes / aliases
    aliases = build_alias_index(args.vault_import_dir)
    result["total_notes"] = len(list(args.vault_import_dir.rglob("*.md")))
    result["total_aliases"] = len(aliases)

    # 4. (Optional) Generate MOC
    if not args.check_only and args.moc_style == "categorical":
        moc_content = build_moc_categorical(args.vault_import_dir, topic=args.topic)
        moc_path = args.vault_import_dir / f"MOC - {args.topic}.md"
        moc_path.write_text(moc_content, encoding="utf-8")
        result["moc_written"] = str(moc_path)

    verdict = "PASS" if not broken and not slug_issues else "FAIL"
    result["verdict"] = verdict

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = "✅" if verdict == "PASS" else "❌"
        print(f"{icon} Obsidian packager: {result['total_notes']} notes, {result['total_aliases']} aliases")
        print(f"   Broken wikilinks: {result['broken_count']}")
        print(f"   Slug issues: {result['slug_issues_count']}")
        if result.get("moc_written"):
            print(f"   MOC written: {result['moc_written']}")
        if broken:
            print("\nBroken wikilinks (first 10):")
            for b in broken[:10]:
                print(f"  {b['file']} → [[{b['target']}]]")

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
