#!/usr/bin/env python3
"""
Memory Empire - audit_log.py  (REALE - registro e ROLLBACK delle modifiche)

Lista tutte le modifiche fatte da Memory Empire ad altre skill e permette il
rollback dal backup. Garantisce che il potere di modificare altre skill sia
sempre tracciato e reversibile.

Uso:
  python scripts/audit_log.py --list
  python scripts/audit_log.py --rollback <id>
"""
import argparse
import re
import shutil
from pathlib import Path

ME = Path(__file__).resolve().parent.parent
ENR = ME / "memory" / "enrichments"
BAK = ENR / "backups"


def parse_log(p: Path):
    txt = p.read_text(encoding="utf-8", errors="replace")
    def g(k):
        m = re.search(rf"\*\*{k}:\*\*\s*(.+)", txt)
        return m.group(1).strip() if m else ""
    return {"id": p.stem.replace("ENR-", ""), "target": g("Target"),
            "backup": g("Backup"), "fonte": g("Fonte")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--rollback", help="id dell'arricchimento da annullare")
    args = ap.parse_args()

    ENR.mkdir(parents=True, exist_ok=True)
    logs = sorted(ENR.glob("ENR-*.md"))

    if args.rollback:
        target_log = ENR / f"ENR-{args.rollback}.md"
        if not target_log.exists():
            print(f"ERRORE: nessun arricchimento con id {args.rollback}")
            raise SystemExit(2)
        info = parse_log(target_log)
        bak = ME / info["backup"] if info["backup"] else None
        tgt = Path(info["target"])
        if bak and bak.exists() and tgt.exists():
            shutil.copy2(bak, tgt)
            print(f"[rollback] {tgt.name} ripristinato dal backup {bak.name}")
            target_log.rename(ENR / f"ROLLED-{args.rollback}.md")
            print(f"[rollback] log marcato come annullato (ROLLED-{args.rollback})")
        else:
            print(f"ERRORE: backup o target mancante ({bak}, {tgt})")
            raise SystemExit(2)
        return

    # default: list
    print(f"Modifiche di Memory Empire ad altre skill: {len(logs)}")
    for p in logs:
        info = parse_log(p)
        print(f"  - id={info['id']} · target={info['target']} · fonte={info['fonte']}")
    if not logs:
        print("  (nessuna modifica registrata)")
    print("\nRollback: python scripts/audit_log.py --rollback <id>")


if __name__ == "__main__":
    main()
