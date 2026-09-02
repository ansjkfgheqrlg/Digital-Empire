#!/usr/bin/env python3
"""
Empire Studio - package.py

Crea un pacchetto ZIP PULITO e Windows-safe di Empire Studio, pronto per essere
estratto senza errore 0x80070057 e aperto con Claude Code.

Esclude: __pycache__, *.pyc, .git, i video scaricati e i frame PNG delle run
(pesanti/binari), mantenendo pero' gli artefatti testuali di prova.
Verifica che nessun nome file contenga caratteri non-Windows-safe.

Uso: python scripts/package.py [--with-runs]
Output: packaged/empire-studio-clean.zip
"""
import argparse
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "packaged"
WIN_BAD = re.compile(r'[<>:"|?*+()\[\]]')

SKIP_DIRS = {"__pycache__", ".git", ".pytest_cache", "node_modules"}
SKIP_EXT = {".pyc"}
# binari pesanti nelle run (li rigenera la pipeline)
RUN_BINARY = {".mp4", ".webm", ".mkv", ".m4v", ".png", ".jpg", ".jpeg", ".webp"}


def should_skip(path: Path, with_runs):
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    if path.suffix.lower() in SKIP_EXT:
        return True
    if "runs" in path.parts:
        if not with_runs:
            return True
        if path.suffix.lower() in RUN_BINARY:
            return True
    if path.name.endswith(".zip"):
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-runs", action="store_true", help="includi gli artefatti testuali delle run")
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "empire-studio-clean.zip"

    files, bad = [], []
    for p in ROOT.rglob("*"):
        if p.is_dir() or should_skip(p, args.with_runs):
            continue
        rel = p.relative_to(ROOT)
        if WIN_BAD.search(p.name) or len(p.name) > 120:
            bad.append(str(rel))
            continue
        files.append((p, rel))

    if bad:
        print(f"ATTENZIONE: {len(bad)} nomi NON Windows-safe (esclusi):")
        for b in bad[:10]:
            print(f"  - {b}")

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p, rel in files:
            # arcname con prefisso empire-studio/ e separatori forward-slash
            arc = "empire-studio/" + str(rel).replace("\\", "/")
            z.write(p, arc)

    size_kb = out.stat().st_size // 1024
    print(f"[package] {len(files)} file -> {out.relative_to(ROOT)} ({size_kb} KB)")
    print(f"[package] nomi non-safe esclusi: {len(bad)}")
    print(f"[package] estrai con 7-Zip o Esplora risorse in un percorso corto (es. C:\\EmpireStudio)")


if __name__ == "__main__":
    main()
