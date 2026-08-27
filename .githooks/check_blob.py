#!/usr/bin/env python3
"""
Controllo pre-commit sui blob pesanti (B-008).

Blocca un file grosso PRIMA che entri nella storia normale di git, invece di
scoprirlo quando il repo pesa 3 GB e un push da 899 MB muore per rete instabile
(successo davvero, una volta).

Perche' una soglia e non una regola per estensione: le estensioni cambiano, il
peso no. Un .png da 8 KB e' un'icona e va tracciata; un .png da 6 MB e' una
copertina KDP, cioe' un artefatto di pubblicazione che non serve nella storia.

DIPENDENZE: nessuna oltre la stdlib e `git` (stesso motivo di check_memory.py:
un guardrail che puo' rompersi viene disattivato).

Uso:
    python .githooks/check_blob.py           # controlla lo staged (pre-commit)
    python .githooks/check_blob.py --soglia 2  # soglia diversa, in MB
"""
import argparse
import os
import subprocess
import sys

SOGLIA_MB = 5.0
# Deroghe: percorsi che possono superare la soglia perche' sono sorgenti veri,
# non artefatti. Si aggiunge una riga QUI, con il motivo, non si usa --no-verify.
DEROGHE = (
    # (prefisso percorso, motivo)
)

ROSSO = "\033[31m"; GIALLO = "\033[33m"; VERDE = "\033[32m"; RESET = "\033[0m"
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
# Solo ASCII nei messaggi: la console di git-for-windows e' cp1252 e un
# carattere fuori posto ucciderebbe il controllo mentre segnala il guasto.


def git(*args):
    try:
        r = subprocess.run(["git"] + list(args), capture_output=True, check=False)
    except FileNotFoundError:
        return ""
    if r.returncode != 0:
        return ""
    return r.stdout.decode("utf-8", "replace")


def staged():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    return [p for p in out.split("\0") if p]


def in_deroga(path):
    for prefisso, motivo in DEROGHE:
        if path.replace("\\", "/").startswith(prefisso):
            return motivo
    return None


def dimensione_staged(path):
    """Peso del contenuto REALMENTE in staging (non quello su disco)."""
    out = git("cat-file", "-s", ":" + path)
    try:
        return int(out.strip())
    except ValueError:
        try:
            return os.path.getsize(path)
        except OSError:
            return 0


def controlla(soglia_mb=SOGLIA_MB):
    limite = soglia_mb * 1048576
    pesanti = []
    for p in staged():
        n = dimensione_staged(p)
        if n > limite and not in_deroga(p):
            pesanti.append((n, p))

    if not pesanti:
        return 0

    pesanti.sort(reverse=True)
    totale = sum(n for n, _ in pesanti)
    print("\n%s==============================================================%s" % (ROSSO, RESET))
    print("%s  COMMIT BLOCCATO - blob pesanti verso la storia normale%s" % (ROSSO, RESET))
    print("%s==============================================================%s" % (ROSSO, RESET))
    print("\n  %d file oltre %.0f MB (%.1f MB in totale). Una volta committati"
          % (len(pesanti), soglia_mb, totale / 1048576))
    print("  restano nella storia PER SEMPRE, anche se li cancelli dopo.\n")
    for n, p in pesanti:
        print("  %s[X]%s  %7.2f MB  %s" % (ROSSO, RESET, n / 1048576, p))
    print("\n  Cosa fare, in ordine di preferenza:")
    print("    1. E' un artefatto generato (copertina, render, screenshot, export)?")
    print("       -> aggiungilo a .gitignore e tienilo in locale/Drive.")
    print("          git rm --cached -- \"<file>\"")
    print("    2. E' un sorgente vero che DEVE stare nel repo?")
    print("       -> aggiungi una riga a DEROGHE in .githooks/check_blob.py,")
    print("          col motivo scritto. Una deroga motivata vale piu' di un --no-verify.")
    print("    3. Serve condividerlo ma non versionarlo? -> Drive, e nel repo solo il link.")
    print("\n  (in emergenza: git commit --no-verify - ma il repo se lo tiene per sempre)\n")
    return 1


def main():
    ap = argparse.ArgumentParser(description="Blocca blob pesanti verso la storia git (B-008)")
    ap.add_argument("--soglia", type=float, default=SOGLIA_MB, help="soglia in MB (default 5)")
    args = ap.parse_args()
    try:
        return controlla(args.soglia)
    except Exception as e:
        print("%s[!]%s check_blob non ha potuto girare (%s: %s) - commit permesso"
              % (GIALLO, RESET, type(e).__name__, e))
        return 0


if __name__ == "__main__":
    sys.exit(main())
