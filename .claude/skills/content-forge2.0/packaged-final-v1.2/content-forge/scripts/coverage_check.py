"""Verifica copertura: per ogni atomo in kg.json, cerca match (lessicale + opzionalmente semantico) negli output del builder.

Used by: C1 coverage-verifier-agent.
Part of: content-forge

Usage:
    python scripts/coverage_check.py <kg_path> <output_dir> [--threshold 0.90] [--semantic] [--json]

Exit code:
    0 = OK (rate >= threshold)
    1 = FAIL
    2 = errore
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.kg_loader import load_kg
from lib.atom_matcher import lexical_coverage_rate, semantic_coverage_rate, semantic_match_available


def collect_output_text(output_dir: Path) -> str:
    """Concatena tutto il testo dei file markdown/txt nell'output_dir."""
    parts = []
    for f in output_dir.rglob("*"):
        if f.is_file() and f.suffix in (".md", ".txt", ".markdown"):
            parts.append(f.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("kg_path", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--threshold", type=float, default=0.90)
    parser.add_argument("--semantic", action="store_true",
                        help="Aggiunge semantic match (richiede sentence-transformers)")
    parser.add_argument("--semantic-threshold", type=float, default=0.6)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not args.kg_path.exists():
        print(f"ERROR: kg.json non trovato: {args.kg_path}", file=sys.stderr)
        return 2
    if not args.output_dir.exists():
        print(f"ERROR: output_dir non esiste: {args.output_dir}", file=sys.stderr)
        return 2

    try:
        kg = load_kg(args.kg_path)
    except Exception as e:
        print(f"ERROR: caricamento KG fallito: {e}", file=sys.stderr)
        return 2

    output_text = collect_output_text(args.output_dir)
    if not output_text:
        print(f"ERROR: nessun file di testo trovato in {args.output_dir}", file=sys.stderr)
        return 2

    # Lexical coverage (sempre)
    lex = lexical_coverage_rate(kg.atoms, output_text)

    result: dict = {
        "verdict": "PASS" if lex["rate"] >= args.threshold else "FAIL",
        "threshold_used": args.threshold,
        "kg_path": str(args.kg_path),
        "output_dir": str(args.output_dir),
        "atoms_total": len(kg.atoms),
        "lexical": {
            "rate": round(lex["rate"], 3),
            "covered": lex["covered"],
            "partial": lex["partial"],
            "missing_count": lex["missing_count"],
            "missing_ids": lex["missing_ids"][:50],  # cap per leggibilità
        },
    }

    # Semantic (opzionale)
    if args.semantic:
        if not semantic_match_available():
            result["semantic"] = {"available": False,
                                  "note": "sentence-transformers non installato"}
        else:
            sem = semantic_coverage_rate(kg.atoms, output_text,
                                          threshold=args.semantic_threshold)
            if sem:
                result["semantic"] = {
                    "available": True,
                    "rate": round(sem["rate"], 3),
                    "covered": sem["covered"],
                    "missing_count": sem["missing_count"],
                    "model": sem["model"],
                    "threshold": sem["threshold"],
                }
                # Verdict combinato: lessicale OR semantico
                combined_rate = max(lex["rate"], sem["rate"])
                result["combined_rate"] = round(combined_rate, 3)
                result["verdict"] = "PASS" if combined_rate >= args.threshold else "FAIL"

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = "✅" if result["verdict"] == "PASS" else "❌"
        print(f"{icon} Coverage: {result['lexical']['rate']:.2%} (lexical) | "
              f"threshold={args.threshold} | "
              f"covered={result['lexical']['covered']}/{result['atoms_total']} "
              f"partial={result['lexical']['partial']} missing={result['lexical']['missing_count']}")
        if args.semantic and result.get("semantic", {}).get("available"):
            print(f"   Semantic: {result['semantic']['rate']:.2%}")

    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
