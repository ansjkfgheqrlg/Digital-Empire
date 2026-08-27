#!/usr/bin/env python3
"""
Attiva i controlli pre-commit del monorepo su QUESTA macchina.

    python .githooks/installa.py            # attiva
    python .githooks/installa.py --stato    # dice solo se sono attivi
    python .githooks/installa.py --rimuovi  # disattiva

Perche' serve un comando invece che "basta clonare": git non versiona
`.git/hooks/`, quindi un hook committato non si attiva da solo su nessun'altra
macchina. `core.hooksPath` risolve: punta git a `.githooks/`, che INVECE e'
versionato — cosi' Max e Gael eseguono lo stesso controllo, e aggiornarlo per
tutti e' un commit normale.

Va lanciato una volta per macchina (per clone, in realta').
"""
import argparse
import os
import stat
import subprocess
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = ".githooks"


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RADICE,
                       capture_output=True, text=True, check=False)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def stato():
    _, val, _ = git("config", "--get", "core.hooksPath")
    return val


def main():
    ap = argparse.ArgumentParser(description="Attiva i controlli pre-commit del monorepo")
    ap.add_argument("--stato", action="store_true")
    ap.add_argument("--rimuovi", action="store_true")
    args = ap.parse_args()

    attuale = stato()

    if args.stato:
        if attuale == HOOKS:
            print("[OK] controlli ATTIVI (core.hooksPath = %s)" % attuale)
            return 0
        print("[X]  controlli NON attivi (core.hooksPath = %r)" % (attuale or "non impostato"))
        print("     attivali con:  python .githooks/installa.py")
        return 1

    if args.rimuovi:
        git("config", "--unset", "core.hooksPath")
        print("[OK] controlli disattivati su questa macchina.")
        return 0

    if attuale and attuale != HOOKS:
        print("[!]  core.hooksPath era gia' impostato a %r: lo sovrascrivo con %r."
              % (attuale, HOOKS))

    rc, _, err = git("config", "core.hooksPath", HOOKS)
    if rc != 0:
        print("[X]  non sono riuscito a impostare core.hooksPath: %s" % err)
        return 1

    # Su Unix il bit di esecuzione serve; su Windows e' innocuo.
    hook = os.path.join(RADICE, HOOKS, "pre-commit")
    if os.path.exists(hook):
        st = os.stat(hook).st_mode
        os.chmod(hook, st | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print("[OK] controlli pre-commit ATTIVI su questa macchina.")
    print("     - collisioni ID checkpoint (B-009)")
    print("     - CRLF nei file di company/Memory (B-028)")
    print("     - blob pesanti fuori dalla storia normale (B-008)")
    print("\n     Verifica:  python .githooks/installa.py --stato")
    print("     Emergenza: git commit --no-verify")
    return 0


if __name__ == "__main__":
    sys.exit(main())
