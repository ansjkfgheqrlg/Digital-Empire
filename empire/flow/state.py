"""
EMPIRE FLOW — stato persistente per step, append-only (GEM-06 §4.4).

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)

empire/.data/flow/state/<step_id>.json = lista di transizioni. Lo stato corrente
è sempre DERIVATO dal log (ultima transizione), mai un campo mutato in place —
così il log resta la fonte di verità unica e ricostruibile (DoD-11).
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from ..paths import repo_root

__all__ = ["Transition", "STATE_DIR", "record", "history", "current_status",
           "is_done", "reset_all"]

STATE_DIR = repo_root() / "empire" / ".data" / "flow" / "state"


@dataclass(slots=True)
class Transition:
    ts: str
    step: str
    from_status: str
    to_status: str
    actor: str
    evidence: str = ""
    note: str = ""


def _path(step_id: str) -> Path:
    safe = step_id.replace("/", "_")
    return STATE_DIR / f"{safe}.json"


def history(step_id: str) -> list[Transition]:
    p = _path(step_id)
    if not p.exists():
        return []
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return [Transition(**r) for r in raw]


def current_status(step_id: str) -> str:
    h = history(step_id)
    return h[-1].to_status if h else "OPEN"


def is_done(step_id: str) -> bool:
    return current_status(step_id) == "DONE"


def record(step_id: str, *, to_status: str, actor: str, evidence: str = "", note: str = "") -> Transition:
    """Aggiunge una transizione. NON sovrascrive mai la storia (append-only)."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    h = history(step_id)
    from_status = h[-1].to_status if h else "OPEN"
    t = Transition(
        ts=datetime.now(timezone.utc).astimezone().isoformat(),
        step=step_id, from_status=from_status, to_status=to_status,
        actor=actor, evidence=evidence, note=note,
    )
    raw = [asdict(x) for x in h] + [asdict(t)]
    _path(step_id).write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    return t


def reset_all() -> None:
    """Cancella lo stato DERIVATO (per dimostrare DoD-11: ricostruibile dal log).
    Qui il log stesso è lo stato — non c'è cache separata da invalidare oltre
    a se stesso, quindi 'reset' = azzerare il log di uno o più step per test.
    """
    if STATE_DIR.exists():
        for f in STATE_DIR.glob("*.json"):
            f.unlink()
