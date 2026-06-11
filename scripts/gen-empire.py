#!/usr/bin/env python
"""
gen-empire.py — Generatore struttura EMPIRE OS
Crea o aggiorna lo scaffolding di company/ basandosi sul Piano Maestro.

Uso:
    python scripts/gen-empire.py               # verifica + crea mancanti
    python scripts/gen-empire.py --check       # solo check, nessuna scrittura
    python scripts/gen-empire.py --target gruppo   # rigenera solo GRUPPO.md
    python scripts/gen-empire.py --list        # lista tutto quello che dovrebbe esistere

Ispirato a gen-group.py di AION GROUP (CF Exponium).
NON tocca i file esistenti: crea solo i mancanti (safe to re-run).
"""

import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
COMPANY = ROOT / "company"

# ── Struttura attesa (verifica gate F1) ─────────────────────────────────────

REQUIRED_FILES = [
    "company/GRUPPO.md",
    "company/Mandato/MANDATO-EMPIRE.md",
    "company/Board-CSuite/README.md",
    "company/Board-CSuite/CEO-Empire-Conductor.md",
    "company/Board-CSuite/COO.md",
    "company/Board-CSuite/CTO.md",
    "company/Board-CSuite/CMO.md",
    "company/Board-CSuite/CRO.md",
    "company/Board-CSuite/CFO.md",
    "company/Board-CSuite/Chief-Forge.md",
    "company/Backbone/README.md",
    "company/Backbone/Bus/README.md",
    "company/Backbone/Brain/README.md",
    "company/Backbone/Governance/README.md",
    "company/Backbone/Identity-HR/README.md",
    "company/Backbone/Observability/README.md",
    "company/Backbone/Coordination/README.md",
    "company/Guilds/README.md",
    "company/Guilds/Prompt-Guild/README.md",
    "company/Guilds/Copy-APSOC-Guild/README.md",
    "company/Guilds/Quality-Guild/README.md",
    "company/Guilds/Cost-Guild/README.md",
    "company/Guilds/Design-Guild/README.md",
    "company/Sentinels/README.md",
    "company/Sentinels/Cost-Sentinel/README.md",
    "company/Sentinels/Quality-Sentinel/README.md",
    "company/Sentinels/Drift-Sentinel/README.md",
    "company/Sentinels/Security-Sentinel/README.md",
    "company/Sentinels/BrandVoice-Sentinel/README.md",
    "company/Gerarchia/README.md",
    "company/Memory/INDEX.md",
    "company/Memory/STATO-EMPIRE.md",
]

ECOSISTEMI = [
    "01-AGENCY",
    "02-INFO-BUSINESS",
    "03-CONTENT-FACTORY",
    "04-MARKETING",
    "05-MULTI-BUSINESS",
    "06-PLATFORM",
    "07-FORGE",
    "08-INTELLIGENCE",
    "09-OPERATIONS",
    "10-MEMORY",
]

ECO_SUBDIRS = ["Reparti", "Workflow", "Funzioni", "Agenti"]

for eco in ECOSISTEMI:
    REQUIRED_FILES.append(f"company/Ecosistemi/{eco}/ECOSISTEMA.md")
    REQUIRED_FILES.append(f"company/Ecosistemi/{eco}/BACKBONE.md")
    for sub in ECO_SUBDIRS:
        pass  # le sottocartelle vengono create ma non richiedono file specifici al gate F1


# ── Helpers ──────────────────────────────────────────────────────────────────

def check_structure(verbose=True):
    """Verifica l'esistenza di tutti i file/cartelle richiesti. Ritorna (pass, fail)."""
    passed = []
    failed = []
    for rel_path in REQUIRED_FILES:
        full = ROOT / rel_path
        if full.exists():
            passed.append(rel_path)
        else:
            failed.append(rel_path)

    # Verifica cartelle ecosistema
    for eco in ECOSISTEMI:
        for sub in ECO_SUBDIRS:
            d = COMPANY / "Ecosistemi" / eco / sub
            if d.exists():
                passed.append(f"company/Ecosistemi/{eco}/{sub}/")
            else:
                failed.append(f"company/Ecosistemi/{eco}/{sub}/")

    if verbose:
        print("\n" + "="*60)
        print("  EMPIRE OS - Verifica struttura company/")
        print("="*60)
        for f in failed:
            print("  MANCANTE: " + f)
        print("\n  PASS: {}  |  FAIL: {}".format(len(passed), len(failed)))
        if not failed:
            print("  [OK] Gate F1: VERDE - struttura completa")
        else:
            print("  [FAIL] Gate F1: ROSSO - {} elementi mancanti".format(len(failed)))
        print("="*60 + "\n")

    return passed, failed


def create_missing(dry_run=False):
    """Crea le cartelle e i file README mancanti (placeholder minimale)."""
    _, failed = check_structure(verbose=False)
    created = []

    for rel_path in failed:
        full = ROOT / rel_path
        if rel_path.endswith("/"):
            if not dry_run:
                full.mkdir(parents=True, exist_ok=True)
            created.append(f"  MKDIR: {rel_path}")
        else:
            parent = full.parent
            if not dry_run:
                parent.mkdir(parents=True, exist_ok=True)
                if not full.exists():
                    full.write_text(
                        f"# {full.stem}\n\n> Da compilare — file creato dal generatore gen-empire.py\n",
                        encoding="utf-8"
                    )
            created.append(f"  CREA: {rel_path}")

    if created:
        print(f"Creati {len(created)} elementi mancanti:")
        for c in created:
            print(c)
    else:
        print("Nessun elemento mancante da creare.")

    return created


def list_structure():
    """Stampa l'albero company/ previsto."""
    print("\nStruttura attesa company/ (gate F1):")
    for f in REQUIRED_FILES:
        print(f"  {f}")
    for eco in ECOSISTEMI:
        for sub in ECO_SUBDIRS:
            print(f"  company/Ecosistemi/{eco}/{sub}/")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="gen-empire.py — EMPIRE OS scaffold generator")
    parser.add_argument("--check", action="store_true", help="Solo verifica, nessuna scrittura")
    parser.add_argument("--list", action="store_true", help="Lista struttura attesa")
    parser.add_argument("--target", help="Target specifico (es: gruppo, mandato)")
    args = parser.parse_args()

    if args.list:
        list_structure()
        return

    if args.check:
        passed, failed = check_structure(verbose=True)
        sys.exit(0 if not failed else 1)

    if args.target == "gruppo":
        print("Rigenera GRUPPO.md: usa il template in company/GRUPPO.md — non sovrascrive se esiste.")
        return

    # Default: verifica + crea mancanti
    passed, failed = check_structure(verbose=True)
    if failed:
        print(f"Creo {len(failed)} elementi mancanti...")
        create_missing()
        # Ri-verifica
        _, still_failed = check_structure(verbose=False)
        if not still_failed:
            print("\n✅ Struttura completata. Gate F1 pronto.")
        else:
            print(f"\n⚠️ Ancora {len(still_failed)} mancanti (possibile problema di permessi).")
    else:
        print("✅ Struttura già completa.")


if __name__ == "__main__":
    main()
