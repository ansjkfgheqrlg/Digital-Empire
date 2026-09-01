"""Lint anti-riassunto.

Cerca parole-bandiera vietate ("in sintesi", "riassumendo", "TL;DR", ecc.) e pattern di compressione.
Riconosce contesti meta-comunicativi legittimi (citazioni in PLAN/conventions) e li skippa.

Used by: C1 coverage-verifier-agent (indirettamente), self-critique dei builder.
Part of: content-forge

Usage:
    python scripts/no_summary_lint.py <target> [--language it,en] [--json]

Exit code:
    0 = nessun smell trovato
    1 = smell trovati
    2 = errore
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FORBIDDEN_PHRASES_IT = [
    r"\bin\s+sintesi\b",
    r"\briassumendo\b",
    r"\bin\s+breve\b",
    r"\bin\s+conclusione\b",
    r"\bper\s+farla\s+breve\b",
    r"\bdunque\s*,\s+i\s+tre\b",
    r"\bi\s+(?:tre|quattro|cinque)\s+punti\s+chiave\b",
]
FORBIDDEN_PHRASES_EN = [
    r"\bin\s+summary\b",
    r"\bto\s+summarize\b",
    r"\bin\s+short\b",
    r"\bthe\s+(?:three|four|five)\s+key\s+points\b",
]
TLDR = r"\btl;?dr\b"


# Marker che indicano "menzione legittima" (citazione, anti-pattern doc, ecc.)
LEGITIMATE_CONTEXT_MARKERS = [
    "evita", "evitare", "non usare", "vietato", "vietate",
    "anti-pattern", "anti pattern", "forbidden", "do not use",
    "scaffold", "menzione", "menzioni",
    # I file PLAN parlano di riassunti come anti-pattern
    "PLAN", "convention",
]
WINDOW_CHARS = 200  # finestra di contesto attorno al match


def _is_legitimate_mention(text: str, offset: int, file_path: Path) -> bool:
    """True se l'occorrenza è meta-comunicativa (legittima)."""
    # 1. Whitelist by filename
    name = file_path.name.lower()
    if name.startswith("plan") or name == "readme.md":
        return True
    if "conventions/anti-patterns" in str(file_path).replace("\\", "/"):
        return True
    if "no_summary" in name or "no-summary" in name:
        return True
    # 2. Whitelist by context window
    start = max(0, offset - WINDOW_CHARS)
    end = min(len(text), offset + WINDOW_CHARS)
    window = text[start:end].lower()
    return any(m.lower() in window for m in LEGITIMATE_CONTEXT_MARKERS)


def lint_text(text: str, file_path: Path, languages: list[str]) -> list[dict]:
    """Cerca smell, escludendo menzioni legittime."""
    smells = []
    patterns = []
    if "it" in languages:
        patterns += FORBIDDEN_PHRASES_IT
    if "en" in languages:
        patterns += FORBIDDEN_PHRASES_EN
    patterns.append(TLDR)  # multilingua

    compiled = [(p, re.compile(p, re.I)) for p in patterns]

    for pattern, regex in compiled:
        for m in regex.finditer(text):
            if _is_legitimate_mention(text, m.start(), file_path):
                continue
            line_no = text[:m.start()].count("\n") + 1
            snippet_start = max(0, m.start() - 40)
            snippet_end = min(len(text), m.end() + 40)
            smells.append({
                "file": str(file_path),
                "line": line_no,
                "offset": m.start(),
                "match": m.group(0),
                "pattern": pattern,
                "snippet": text[snippet_start:snippet_end].replace("\n", " "),
            })
    return smells


def lint_path(target: Path, languages: list[str]) -> list[dict]:
    """Lint un file o ricorsivamente una cartella."""
    all_smells = []
    if target.is_file():
        if target.suffix in (".md", ".txt", ".markdown"):
            text = target.read_text(encoding="utf-8", errors="ignore")
            all_smells.extend(lint_text(text, target, languages))
    elif target.is_dir():
        for f in target.rglob("*"):
            if f.is_file() and f.suffix in (".md", ".txt", ".markdown"):
                text = f.read_text(encoding="utf-8", errors="ignore")
                all_smells.extend(lint_text(text, f, languages))
    return all_smells


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("target", type=Path, help="File o directory da analizzare")
    parser.add_argument("--language", default="it,en", help="Comma-separated language codes")
    parser.add_argument("--json", action="store_true", help="Output JSON su stdout")
    args = parser.parse_args(argv)

    if not args.target.exists():
        print(f"ERROR: path non esiste: {args.target}", file=sys.stderr)
        return 2

    languages = [l.strip() for l in args.language.split(",") if l.strip()]
    smells = lint_path(args.target, languages)

    if args.json:
        print(json.dumps({"total_smells": len(smells), "smells": smells}, indent=2, ensure_ascii=False))
    else:
        if not smells:
            print(f"✅ Nessuno smell anti-riassunto trovato in {args.target}")
        else:
            print(f"⚠️  Trovati {len(smells)} smell:")
            for s in smells:
                print(f"  {s['file']}:{s['line']} → '{s['match']}'")
                print(f"     ...{s['snippet']}...")

    return 1 if smells else 0


if __name__ == "__main__":
    sys.exit(main())
