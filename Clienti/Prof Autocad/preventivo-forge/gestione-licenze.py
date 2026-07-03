#!/usr/bin/env python3
"""
gestione-licenze.py — Console di controllo abbonamenti PreventivoForge (uso di Max/Claude).

Lo stato di TUTTI i concessionari vive in un Gist GitHub segreto (raggiungibile solo da chi ha
il link). Ogni app legge quel Gist prima di ogni preventivo. Qui lo si comanda con una riga.

Uso:
  python gestione-licenze.py stato                 # mostra lo stato di tutti i concessionari
  python gestione-licenze.py sospendi <id>         # BLOCCA l'app del concessionario
  python gestione-licenze.py attiva  <id>          # sblocca
  python gestione-licenze.py aggiungi <id>         # registra un nuovo concessionario (=active)
  python gestione-licenze.py rimuovi <id>          # toglie un concessionario dalla lista

Config: legge `licenze.config.json` (accanto a questo file, gitignorato) con:
  {"gist_id": "<id-del-gist>", "file": "licenze-preventivoforge.json"}
La crea `nuovo_concessionario.py`/`setup` la prima volta (dopo aver creato il Gist).

Dipende da: GitHub CLI `gh` autenticato (gh auth status).
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

try:  # console UTF-8 (Windows cp1252 va in crash su emoji)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
CONFIG = HERE / "licenze.config.json"
ACTIVE = "active"
SUSPENDED = "suspended"


def _load_config() -> dict:
    if not CONFIG.exists():
        sys.exit(
            "❌ Manca licenze.config.json. Crea prima il Gist segreto con:\n"
            '   gh gist create licenze-preventivoforge.json --desc "PreventivoForge licenze"\n'
            "poi salva qui {\"gist_id\": \"<id>\", \"file\": \"licenze-preventivoforge.json\"}."
        )
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def _gh(args: list[str]) -> str:
    """Esegue gh e ritorna stdout (solleva con messaggio chiaro se fallisce)."""
    try:
        res = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
        return res.stdout
    except FileNotFoundError:
        sys.exit("❌ GitHub CLI 'gh' non trovato. Installa gh e fai 'gh auth login'.")
    except subprocess.CalledProcessError as exc:
        sys.exit(f"❌ gh {' '.join(args)} fallito:\n{exc.stderr.strip()}")


def _read_state(cfg: dict) -> dict:
    raw = _gh(["gist", "view", cfg["gist_id"], "--filename", cfg["file"], "--raw"])
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def _write_state(cfg: dict, state: dict) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        tmp = fh.name
    _gh(["gist", "edit", cfg["gist_id"], "--filename", cfg["file"], tmp])
    Path(tmp).unlink(missing_ok=True)


def _norm(did: str) -> str:
    return (did or "").strip().lower()


def cmd_stato(cfg: dict) -> None:
    state = _read_state(cfg)
    if not state:
        print("(lista vuota)")
        return
    print("Stato concessionari:")
    for k, v in sorted(state.items()):
        icon = "🟢" if str(v).lower() == ACTIVE else "🔴"
        print(f"  {icon} {k}: {v}")


def cmd_set(cfg: dict, did: str, status: str) -> None:
    did = _norm(did)
    state = _read_state(cfg)
    prev = state.get(did, "(assente)")
    state[did] = status
    _write_state(cfg, state)
    verb = "BLOCCATO 🔴" if status == SUSPENDED else "ATTIVATO 🟢"
    print(f"{did}: {prev} → {status}   [{verb}]")
    if status == SUSPENDED:
        print("   L'app del concessionario si bloccherà al prossimo preventivo (entro ~1 min).")
    else:
        print("   L'app tornerà operativa al prossimo preventivo.")


def cmd_rimuovi(cfg: dict, did: str) -> None:
    did = _norm(did)
    state = _read_state(cfg)
    if did in state:
        del state[did]
        _write_state(cfg, state)
        print(f"{did} rimosso dalla lista.")
    else:
        print(f"{did} non era in lista.")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cfg = _load_config()
    cmd = sys.argv[1].lower()
    arg = sys.argv[2] if len(sys.argv) > 2 else ""

    if cmd == "stato":
        cmd_stato(cfg)
    elif cmd == "sospendi":
        if not arg:
            return _err("serve <id> concessionario")
        cmd_set(cfg, arg, SUSPENDED)
    elif cmd in ("attiva", "aggiungi"):
        if not arg:
            return _err("serve <id> concessionario")
        cmd_set(cfg, arg, ACTIVE)
    elif cmd == "rimuovi":
        if not arg:
            return _err("serve <id> concessionario")
        cmd_rimuovi(cfg, arg)
    else:
        return _err(f"comando sconosciuto: {cmd}")
    return 0


def _err(msg: str) -> int:
    print(f"❌ {msg}\n")
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
