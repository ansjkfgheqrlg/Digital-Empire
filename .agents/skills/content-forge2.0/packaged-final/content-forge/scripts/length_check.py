"""Length check: verifica che output >= sorgente per target che lo richiedono (doc, wiki, MKD).

Used by: C1 coverage-verifier-agent, A5 mkd-builder-agent (self-critique).
Part of: content-forge

Usage:
    python scripts/length_check.py <source_path> <output_dir> [--min-ratio 1.0] [--json]

Exit code:
    0 = OK (ratio >= min_ratio)
    1 = FAIL (ratio < min_ratio)
    2 = errore
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.markdown_tools import word_count


def count_words_in_path(path: Path) -> int:
    """Conta parole in un file o ricorsivamente in una cartella (.md/.txt)."""
    if path.is_file():
        return word_count(path.read_text(encoding="utf-8", errors="ignore"))
    elif path.is_dir():
        total = 0
        for f in path.rglob("*"):
            if f.is_file() and f.suffix in (".md", ".txt", ".markdown"):
                total += word_count(f.read_text(encoding="utf-8", errors="ignore"))
        return total
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("source_path", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--min-ratio", type=float, default=1.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    if not args.source_path.exists():
        print(f"ERROR: source non esiste: {args.source_path}", file=sys.stderr)
        return 2
    if not args.output_dir.exists():
        print(f"ERROR: output_dir non esiste: {args.output_dir}", file=sys.stderr)
        return 2

    source_words = count_words_in_path(args.source_path)
    output_words = count_words_in_path(args.output_dir)
    ratio = (output_words / source_words) if source_words > 0 else 0.0
    passed = ratio >= args.min_ratio

    result = {
        "source_path": str(args.source_path),
        "output_dir": str(args.output_dir),
        "source_words": source_words,
        "output_words": output_words,
        "ratio": round(ratio, 3),
        "min_ratio": args.min_ratio,
        "passed": passed,
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = "✅" if passed else "❌"
        print(f"{icon} source={source_words}w  output={output_words}w  ratio={ratio:.2f}x  (min={args.min_ratio}x)")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
