#!/usr/bin/env python3
"""
repo-study-skill / scan_repo.py  (REALE, READ-ONLY)

Scansiona una repo/cartella in SOLA LETTURA e produce una mappa strutturale
(cartelle, tipi di file, entrypoint, README, config) che l'agente repo-deep-study
usera' per il deep study. NON modifica MAI nulla.

Uso:
  python scan_repo.py --path <repo-or-folder> --run <run-id>
Output: runs/<run-id>/repo-structure.json
"""
import argparse
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # .../empire-studio
RUNS = ROOT / "runs"

IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist",
               "build", ".next", ".cache", "vendor", ".idea", ".vscode"}
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mp3", ".zip",
              ".tar", ".gz", ".pdf", ".woff", ".woff2", ".ttf", ".ico", ".exe",
              ".dll", ".so", ".bin", ".pyc"}
ENTRY_HINTS = {"main.py", "index.js", "index.ts", "app.py", "server.py", "cli.py",
               "setup.py", "pyproject.toml", "package.json", "SKILL.md", "README.md",
               "Dockerfile", "Makefile", "requirements.txt"}


def scan(path: Path, max_files=4000):
    dirs, files = 0, 0
    by_ext = {}
    entrypoints = []
    readmes = []
    sample = []
    for p in path.rglob("*"):
        if any(part in IGNORE_DIRS for part in p.parts):
            continue
        if p.is_dir():
            dirs += 1
            continue
        files += 1
        ext = p.suffix.lower() or "(noext)"
        by_ext[ext] = by_ext.get(ext, 0) + 1
        if p.name in ENTRY_HINTS:
            entrypoints.append(str(p.relative_to(path)))
        if p.name.lower().startswith("readme"):
            readmes.append(str(p.relative_to(path)))
        if files <= max_files and ext not in BINARY_EXT and len(sample) < 60:
            sample.append(str(p.relative_to(path)))
        if files > max_files:
            break
    return {
        "scanned_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "path": str(path),
        "counts": {"dirs": dirs, "files": files},
        "by_extension": dict(sorted(by_ext.items(), key=lambda x: -x[1])),
        "entrypoints": sorted(set(entrypoints)),
        "readmes": sorted(set(readmes)),
        "sample_files": sample,
        "readonly": True,
        "note": "Scansione in sola lettura. Nessun file modificato.",
    }


def main():
    ap = argparse.ArgumentParser(description="Scanner repo read-only")
    ap.add_argument("--path", required=True)
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    target = Path(args.path)
    if not target.exists():
        print(f"ERRORE: path inesistente: {target}")
        raise SystemExit(2)
    run_dir = RUNS / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    result = scan(target)
    out = run_dir / "repo-structure.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[scan_repo] {result['counts']['files']} file, {result['counts']['dirs']} cartelle")
    print(f"[scan_repo] entrypoint: {result['entrypoints'][:5]}")
    print(f"[scan_repo] -> {out.relative_to(ROOT)}  (READ-ONLY, originale invariato)")


if __name__ == "__main__":
    main()
