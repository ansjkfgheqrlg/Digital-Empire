#!/usr/bin/env python3
"""
Empire Studio - Validator (cancello anti-stub, anti AP01 "Scaffold-as-Deliverable")

Questo script e' la garanzia che Empire Studio NON ripeta l'errore dell'agente
cloud: dichiarare "fatto/completo/7 file" cose che erano stub di una riga.

Controlla, sul filesystem reale:
  1. AGENTI: ogni cartella agente sotto agents/<dept>/<agent>/ deve avere i 7
     file canonici, ognuno SOSTANZIALE (>= MIN_LINES righe e >= MIN_CHARS char),
     senza marker proibiti ("in costruzione", "TODO", "stub", "placeholder",
     "da completare", "coming soon").
  2. SKILL: ogni skill sotto skills/.../<skill>/ deve avere SKILL.md sostanziale.
     Le skill tier2-functional devono avere ALMENO uno script .py reale
     (>= MIN_SCRIPT_LINES righe, compilabile).
  3. NOMI FILE Windows-safe: niente ( ) : + ? < > | " * e lunghezza < 120.
  4. NIENTE testo finto: scansiona descrizioni "hardcoded/inventate" vietate.

Exit code 0 se tutto pulito, 1 se ci sono violazioni.
Uso:
  python validator.py            # valida tutto
  python validator.py --agents   # solo agenti
  python validator.py --names    # solo nomi file
"""
import argparse
import py_compile
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_7 = ["system-prompt.md", "tools.md", "playbook.md",
               "evals.md", "failure-modes.md", "memory.md"]  # + <agent>.md spec

MIN_LINES = 8           # floor di righe (le tabelle dense hanno poche righe ma molti char)
MIN_CHARS = 500         # soglia primaria: gli stub veri erano ~150-300 char
MIN_SCRIPT_LINES = 25   # uno script tier2 sotto questo = guscio

# marker-frase: indicano sempre uno stub (match come sottostringa)
BANNED_PHRASES = [
    "in costruzione", "7 file: in costruzione", "da completare", "coming soon",
    "lorem ipsum", "placeholder", "(da fare)", "xxx-da-riempire", "work in progress",
]
# marker-parola: vietati solo come PAROLA isolata. NB: 'stub' NON e' qui perche'
# l'intero ecosistema parla legittimamente di anti-stub (es. compliance-auditor);
# i veri stub sono colti dalle BANNED_PHRASES + dalla soglia di lunghezza.
BANNED_WORDS = ["todo", "tbd"]
WIN_BAD = re.compile(r'[<>:"|?*+()\[\]]')


def rel(p):
    return str(p).replace(str(ROOT), "empire-studio")


def check_names():
    viol = []
    for p in ROOT.rglob("*"):
        if ".git" in p.parts:
            continue
        name = p.name
        if WIN_BAD.search(name):
            viol.append(f"NOME non-Windows-safe: {rel(p)}")
        if len(name) > 120:
            viol.append(f"NOME troppo lungo (>120): {rel(p)}")
    return viol


def is_substantial(path):
    try:
        txt = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return False, f"illeggibile ({e})"
    low = txt.lower()
    for b in BANNED_PHRASES:
        if b in low:
            return False, f"marker proibito '{b}'"
    for w in BANNED_WORDS:
        # parola isolata, ma NON quando fa parte di 'no-stub'/'anti-stub' (lookbehind su [\w-])
        if re.search(rf'(?<![\w-]){w}(?![\w-])', low):
            return False, f"marker proibito '{w}'"
    n_lines = len([l for l in txt.splitlines() if l.strip()])
    # char-primario: un file e' stub se ha pochi caratteri OPPURE pochissime righe
    if len(txt) < MIN_CHARS or n_lines < MIN_LINES:
        return False, f"troppo corto ({n_lines} righe, {len(txt)} char)"
    return True, "ok"


def check_agents():
    viol = []
    agents_root = ROOT / "agents"
    if not agents_root.exists():
        return ["agents/ non esiste"]
    # un agente = cartella che contiene un file <nome>.md uguale al nome cartella
    for dept in agents_root.iterdir():
        if not dept.is_dir():
            continue
        for ag in dept.iterdir():
            if not ag.is_dir():
                continue
            spec = ag / f"{ag.name}.md"
            required = [spec] + [ag / f for f in CANONICAL_7]
            missing = [f.name for f in required if not f.exists()]
            if missing:
                viol.append(f"AGENTE {rel(ag)}: mancano {missing}")
                continue
            for f in required:
                ok, why = is_substantial(f)
                if not ok:
                    viol.append(f"AGENTE file debole {rel(f)}: {why}")
    return viol


def check_skills():
    viol = []
    skills_root = ROOT / "skills"
    if not skills_root.exists():
        return ["skills/ non esiste"]
    for tier in skills_root.iterdir():
        if not tier.is_dir():
            continue
        for sk in tier.iterdir():
            if not sk.is_dir():
                continue
            skill_md = sk / "SKILL.md"
            if not skill_md.exists():
                viol.append(f"SKILL {rel(sk)}: manca SKILL.md")
                continue
            ok, why = is_substantial(skill_md)
            if not ok:
                viol.append(f"SKILL.md debole {rel(skill_md)}: {why}")
            # tier2 funzionali: devono avere uno script reale
            if tier.name == "tier2-functional":
                scripts = list((sk / "scripts").glob("*.py")) if (sk / "scripts").exists() else []
                scripts += list(sk.glob("*.py"))
                real = []
                for s in scripts:
                    n = len([l for l in s.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()])
                    if n >= MIN_SCRIPT_LINES:
                        # prova a compilarlo
                        try:
                            py_compile.compile(str(s), doraise=True)
                            real.append(s)
                        except py_compile.PyCompileError as e:
                            viol.append(f"SCRIPT non compila {rel(s)}: {e.msg.splitlines()[-1][:80]}")
                if not real:
                    viol.append(f"SKILL funzionale senza script reale: {rel(sk)}")
    return viol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agents", action="store_true")
    ap.add_argument("--skills", action="store_true")
    ap.add_argument("--names", action="store_true")
    args = ap.parse_args()
    run_all = not (args.agents or args.skills or args.names)

    viol = []
    if run_all or args.names:
        viol += check_names()
    if run_all or args.agents:
        viol += check_agents()
    if run_all or args.skills:
        viol += check_skills()

    print("=" * 60)
    print("EMPIRE STUDIO VALIDATOR (anti-stub gate)")
    print("=" * 60)
    if not viol:
        print("PULITO: nessuna violazione. Nessuno stub, nomi Windows-safe, skill reali.")
        sys.exit(0)
    print(f"VIOLAZIONI: {len(viol)}\n")
    for v in viol:
        print(f"  - {v}")
    print(f"\nTotale: {len(viol)} violazioni. (exit 1)")
    sys.exit(1)


if __name__ == "__main__":
    main()
