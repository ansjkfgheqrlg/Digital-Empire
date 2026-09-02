#!/usr/bin/env python3
"""
Empire Studio - Setup Check
Verifica che il motore (CLI-only, no API) abbia tutti i prerequisiti locali.
Nessun servizio a pagamento: yt-dlp + ffmpeg + python; la "visione" la fa Claude.

Uso: python scripts/setup_check.py
Exit 0 se tutto ok, 1 se manca qualcosa di critico.
"""
import shutil
import subprocess
import sys

CRITICAL = {
    "python": [sys.executable, "--version"],
    "ffmpeg": ["ffmpeg", "-version"],
    "ffprobe": ["ffprobe", "-version"],
}
OPTIONAL = {
    "node": ["node", "--version"],
    "npx": ["npx", "--version"],
}


def probe(name, cmd):
    exe = cmd[0]
    if exe != sys.executable and shutil.which(exe) is None:
        return None
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return (out.stdout or out.stderr).splitlines()[0].strip()
    except Exception as e:
        return f"errore: {e}"


def check_module(mod):
    try:
        __import__(mod)
        return True
    except ImportError:
        return False


def main():
    print("=" * 56)
    print("EMPIRE STUDIO - SETUP CHECK (CLI-only, no API, no paid)")
    print("=" * 56)
    missing = []

    print("\n[CRITICI]")
    for name, cmd in CRITICAL.items():
        v = probe(name, cmd)
        if v is None:
            print(f"  MANCA   {name}")
            missing.append(name)
        else:
            print(f"  OK      {name:8s} {v}")

    print("\n[MODULI PYTHON]")
    has_ytdlp = check_module("yt_dlp")
    print(f"  {'OK' if has_ytdlp else 'MANCA':7s} yt_dlp (pip install --user yt-dlp)")
    if not has_ytdlp:
        missing.append("yt_dlp")
    has_pw = check_module("playwright")
    print(f"  {'OK' if has_pw else 'opz.':7s} playwright (per web-research / fallback frame)")

    print("\n[OPZIONALI]")
    for name, cmd in OPTIONAL.items():
        v = probe(name, cmd)
        print(f"  {'OK' if v else 'opz.':7s} {name:8s} {v or '(assente)'}")

    print("\n[VISIONE]")
    print("  La 'visione' dei frame e' eseguita da Claude Code (modello con")
    print("  visione nativa) che legge i PNG estratti. Nessuna vision API.")

    print("\n" + "=" * 56)
    if missing:
        print(f"INCOMPLETO: mancano {missing}")
        print("Installa con: python -m pip install --user yt-dlp")
        sys.exit(1)
    print("PRONTO: tutti i prerequisiti critici presenti.")
    sys.exit(0)


if __name__ == "__main__":
    main()
