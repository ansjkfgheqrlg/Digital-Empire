"""
EMPIRE FLOW — valutazione dei gate. Il cuore del motore (GEM-06 §4.3).

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)

Regole non negoziabili:
- niente "quasi verde": tre stati soli, PENDING (prima della deadline, non ancora deciso),
  GREEN, RED. Una volta passata la deadline senza verde, RED automatico + on_red applicato.
- green_if è un'espressione valutata su fatti, MAI eval(): mini-valutatore che accetta solo
  '<nome> <op> <numero>' e 'and'/'or' (GEM-06 §4.3, DoD-12).
- un gate `human` non diventa mai verde da solo: serve conferma esplicita con evidenza.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from ..paths import repo_root

__all__ = ["GateResult", "Status", "FACTS_PATH", "load_facts", "save_fact",
           "eval_expression", "evaluate", "evaluate_all"]

Status = Literal["PENDING", "GREEN", "RED"]

FACTS_DIR = repo_root() / "empire" / ".data" / "flow"
FACTS_PATH = FACTS_DIR / "facts.json"

_TOKEN_RE = re.compile(
    r"\s*(?:(?P<op>and|or)|(?P<name>[A-Za-z_][\w]*)\s*(?P<cmp>>=|<=|==|!=|>|<)\s*(?P<num>-?\d+(?:\.\d+)?))",
    re.IGNORECASE,
)

_CMP_FUNCS = {
    ">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b, "!=": lambda a, b: a != b,
    ">": lambda a, b: a > b, "<": lambda a, b: a < b,
}


class ExpressionError(ValueError):
    pass


def _tokenize(expr: str) -> list[tuple]:
    tokens = []
    pos = 0
    while pos < len(expr):
        m = _TOKEN_RE.match(expr, pos)
        if not m or m.end() == pos:
            if expr[pos:].strip() == "":
                break
            raise ExpressionError(f"token non riconosciuto in {expr!r} alla posizione {pos}")
        if m.group("op"):
            tokens.append(("op", m.group("op").lower()))
        else:
            tokens.append(("cmp", (m.group("name"), m.group("cmp"), float(m.group("num")))))
        pos = m.end()
    if not tokens:
        raise ExpressionError(f"espressione vuota: {expr!r}")
    return tokens


def eval_expression(expr: str, facts: dict) -> bool:
    """Mini-valutatore: '<nome> <op> <numero>' combinati con 'and'/'or', valutati
    da sinistra a destra con 'and' a precedenza più alta di 'or' (come in Python).
    NESSUN eval()/exec(): solo confronto numerico su nomi noti. Nome assente in
    facts -> quella comparazione è False (fatto non ancora misurato = non verde).
    """
    tokens = _tokenize(expr)

    def cmp_value(tok):
        name, op, num = tok
        val = facts.get(name)
        if val is None:
            return False
        return _CMP_FUNCS[op](float(val), num)

    # split su 'or' di primo livello, poi ogni gruppo su 'and'
    or_groups: list[list] = [[]]
    for kind, val in tokens:
        if kind == "op" and val == "or":
            or_groups.append([])
        else:
            or_groups[-1].append((kind, val))

    for group in or_groups:
        and_result = True
        for kind, val in group:
            if kind == "op" and val == "and":
                continue
            if kind == "cmp":
                and_result = and_result and cmp_value(val)
        if and_result:
            return True
    return False


def load_facts() -> dict:
    if not FACTS_PATH.exists():
        return {}
    try:
        return json.loads(FACTS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_fact(name: str, value: float, *, source: str) -> None:
    """Scrive un fatto con la sua fonte (mai un numero senza provenienza)."""
    FACTS_DIR.mkdir(parents=True, exist_ok=True)
    data = load_facts()
    data[name] = value
    meta = data.setdefault("_sources", {}) if isinstance(data.get("_sources"), dict) else {}
    data["_sources"] = {**data.get("_sources", {}), name: source}
    FACTS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


@dataclass(slots=True)
class GateResult:
    id: str
    status: Status
    deadline: datetime
    reason: str
    on_red: str = ""


def _check_file(gate) -> tuple[bool, str]:
    p = repo_root() / gate.path
    if not p.exists():
        return False, f"file non trovato: {gate.path}"
    text = p.read_text(encoding="utf-8", errors="replace")
    if gate.must_not_contain and gate.must_not_contain in text:
        return False, f"{gate.path} contiene ancora {gate.must_not_contain!r} (placeholder non sostituito)"
    if gate.must_contain and gate.must_contain not in text:
        return False, f"{gate.path} non contiene {gate.must_contain!r}"
    return True, f"{gate.path} verificato (nessun placeholder residuo)" if gate.must_not_contain else f"{gate.path} OK"


def evaluate(gate, *, now: datetime | None = None, facts: dict | None = None,
             human_confirmed: bool = False) -> GateResult:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.astimezone()
    facts = facts if facts is not None else load_facts()
    past_deadline = now >= gate.deadline

    if gate.type == "human":
        if human_confirmed:
            return GateResult(gate.id, "GREEN", gate.deadline, "confermato manualmente", gate.on_red)
        if past_deadline:
            return GateResult(gate.id, "RED", gate.deadline,
                               "deadline scaduta senza conferma umana esplicita", gate.on_red)
        return GateResult(gate.id, "PENDING", gate.deadline, "in attesa di conferma umana", gate.on_red)

    if gate.type == "file":
        ok, reason = _check_file(gate)
        if ok:
            return GateResult(gate.id, "GREEN", gate.deadline, reason, gate.on_red)
        if past_deadline:
            return GateResult(gate.id, "RED", gate.deadline, reason, gate.on_red)
        return GateResult(gate.id, "PENDING", gate.deadline, reason, gate.on_red)

    if gate.type == "metric":
        ok = eval_expression(gate.green_if, facts) if gate.green_if else False
        if ok:
            return GateResult(gate.id, "GREEN", gate.deadline, f"{gate.green_if} -> vero", gate.on_red)
        if past_deadline:
            return GateResult(gate.id, "RED", gate.deadline,
                               f"{gate.green_if} -> falso alla scadenza", gate.on_red)
        return GateResult(gate.id, "PENDING", gate.deadline, f"{gate.green_if} non ancora vero", gate.on_red)

    return GateResult(gate.id, "PENDING", gate.deadline, f"tipo gate non gestito: {gate.type}", gate.on_red)


def evaluate_all(gates, *, now: datetime | None = None, facts: dict | None = None,
                  confirmed_ids: frozenset[str] = frozenset()) -> list[GateResult]:
    facts = facts if facts is not None else load_facts()
    return [evaluate(g, now=now, facts=facts, human_confirmed=g.id in confirmed_ids) for g in gates]
