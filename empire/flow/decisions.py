"""
EMPIRE FLOW — decisioni a "default più veto" (ADR-EST-006).

Owner: Claude · Origine: FORGE (LOTTO 2 completamento Workflow Estate, CP-20260723)

## Perché questo modulo esiste

Il 23/07 `flow gates` dava **Gate-DEC rosso**. Il motivo non era che la decisione non
fosse stata presa: DEC-EST-001 (prezzo del Manuale) era ATTIVA per regola dal 21/07 h20:00,
quando il veto è scaduto senza opposizione. Il motivo era che **nessuno aveva scritto il
fatto corrispondente**. Un gate rosso perché il lavoro manca e un gate rosso perché il dato
non è stato registrato sono indistinguibili dall'esterno — ed è il difetto più pericoloso di
un cruscotto, perché insegna a non fidarsi dei rossi.

Questo modulo chiude quel buco applicando la regola, non aggirandola.

## La regola (ADR-EST-006)

Ogni decisione ha un default e una scadenza di veto:
- **veto registrato** prima della scadenza -> la decisione NON diventa attiva (fatto = 0)
- **scadenza passata senza veto** -> il default diventa ATTIVO (fatto = 1)
- **prima della scadenza, nessun veto** -> IN_ATTESA, nessun fatto scritto

Il veto è un atto umano esplicito e tracciato (`flow veto <id> --actor <chi> --reason <perche>`):
il silenzio vale assenso, ma il dissenso deve essere registrato da qualcuno con un nome.
Senza il comando di veto questo modulo sarebbe una macchina che dice sempre di sì — e non
sarebbe "default più veto", sarebbe solo "default".
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal

from . import gate as _gate
from . import state as _state

__all__ = ["DecisionStatus", "fact_name_for", "veto_key", "register_veto",
           "is_vetoed", "evaluate", "apply_all"]

State = Literal["ATTIVA", "VETO", "IN_ATTESA"]

_NUM_RE = re.compile(r"(\d+)\s*$")


@dataclass(slots=True)
class DecisionStatus:
    id: str
    topic: str
    default: str
    veto_deadline: datetime | None
    fact: str
    state: State
    reason: str


def fact_name_for(decision: dict) -> str:
    """Nome del fatto da scrivere quando la decisione è attiva.

    Preferisce il campo esplicito `fact:` del workflows.yaml. In sua assenza lo deriva
    dal numero finale dell'id (DEC-EST-001 -> dec_001_attiva), che è la convenzione già
    usata dal `green_if` di Gate-DEC. La derivazione resta solo come rete di sicurezza:
    la forma esplicita è preferibile perché rende il legame gate<->decisione leggibile
    nel file invece che nascosto in questo codice.
    """
    explicit = (decision.get("fact") or "").strip()
    if explicit:
        return explicit
    m = _NUM_RE.search(str(decision.get("id", "")))
    num = m.group(1) if m else "000"
    return f"dec_{num}_attiva"


def veto_key(decision_id: str) -> str:
    return f"veto_{decision_id}"


def is_vetoed(decision_id: str) -> bool:
    return _state.is_done(veto_key(decision_id))


def register_veto(decision_id: str, *, actor: str, reason: str) -> tuple[bool, str]:
    """Registra un veto umano. Idempotente: due volte non duplica.

    Non controlla la scadenza di proposito: un veto tardivo va comunque registrato,
    perché la storia deve restare vera. Sarà `evaluate` a dire che è arrivato dopo.
    """
    key = veto_key(decision_id)
    if _state.is_done(key):
        h = _state.history(key)
        return False, f"veto gia' registrato il {h[-1].ts}"
    if not reason.strip():
        return False, "un veto senza motivazione non e' registrabile (serve --reason)"
    _state.record(key, to_status="DONE", actor=actor, evidence=reason,
                  note=f"veto su {decision_id}")
    return True, f"veto registrato su {decision_id} da {actor}"


def _parse_deadline(raw) -> datetime | None:
    if raw is None:
        return None
    if isinstance(raw, datetime):
        dt = raw
    else:
        try:
            dt = datetime.fromisoformat(str(raw).strip())
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return dt


def evaluate(decisions: list[dict], *, now: datetime | None = None) -> list[DecisionStatus]:
    now = now or datetime.now(timezone.utc).astimezone()
    out: list[DecisionStatus] = []
    for d in decisions or []:
        did = str(d.get("id", "?"))
        deadline = _parse_deadline(d.get("veto_deadline"))
        fact = fact_name_for(d)

        if is_vetoed(did):
            h = _state.history(veto_key(did))
            who = h[-1].actor if h else "?"
            why = h[-1].evidence if h else ""
            state: State = "VETO"
            reason = f"veto registrato da {who}: {why}"
        elif deadline is None:
            state = "IN_ATTESA"
            reason = "nessuna scadenza di veto dichiarata nel file"
        elif now >= deadline:
            state = "ATTIVA"
            reason = f"veto scaduto il {deadline.isoformat()} senza opposizione registrata (ADR-EST-006)"
        else:
            state = "IN_ATTESA"
            reason = f"veto aperto fino al {deadline.isoformat()}"

        out.append(DecisionStatus(
            id=did, topic=str(d.get("topic", "")), default=str(d.get("default", "")),
            veto_deadline=deadline, fact=fact, state=state, reason=reason,
        ))
    return out


def apply_all(decisions: list[dict], *, now: datetime | None = None,
              write: bool = True) -> list[DecisionStatus]:
    """Valuta e scrive i fatti corrispondenti. Idempotente.

    ATTIVA -> fatto 1 · VETO -> fatto 0 (esplicito: la decisione è stata fermata,
    non semplicemente non misurata) · IN_ATTESA -> nessun fatto scritto, perché
    "non ancora deciso" non è un numero e fingere uno zero lo confonderebbe con un veto.
    """
    statuses = evaluate(decisions, now=now)
    if not write:
        return statuses
    for s in statuses:
        if s.state == "ATTIVA":
            _gate.save_fact(s.fact, 1, source=f"{s.id}: {s.reason}")
        elif s.state == "VETO":
            _gate.save_fact(s.fact, 0, source=f"{s.id}: {s.reason}")
    return statuses
