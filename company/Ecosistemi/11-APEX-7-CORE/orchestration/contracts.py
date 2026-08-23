"""
APEX-7 Orchestration Layer — Contratti di stato e risultato dei gate.

Due primitive, entrambe immutabili:
  - StateSnapshot: nodo di una catena Merkle SHA-256. Ogni fase della pipeline
    ne produce uno agganciato al precedente; se qualcuno riscrive uno stato a
    posteriori la catena non torna piu'.
  - GateResult: esito di un quality gate, costruito SEMPRE da GateCheck reali.
    Non esiste un modo di dichiarare "passed" senza passare i controlli.

Stdlib + dataclass, come il resto di 11-APEX-7-CORE (nessuna dipendenza nuova).
"""
from __future__ import annotations

import hashlib
import json
import math
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple


# ─────────────────────────────────────────────────────────────────────────────
# Catena di stato
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class StateSnapshot:
    """Nodo immutabile di una catena Merkle. Si crea solo via create()."""
    state_id: str
    parent_hash: Optional[str]
    phase_id: str
    timestamp_utc: float
    data_payload: Dict[str, Any]
    state_hash: str

    @classmethod
    def create(
        cls,
        phase_id: str,
        payload: Dict[str, Any],
        parent_hash: Optional[str] = None,
    ) -> "StateSnapshot":
        ts = time.time()
        canonical = json.dumps(
            {"parent": parent_hash, "phase": phase_id, "data": payload, "ts": ts},
            sort_keys=True,
            default=str,
        )
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        return cls(
            state_id=f"SNAP_{digest[:12]}",
            parent_hash=parent_hash,
            phase_id=phase_id,
            timestamp_utc=ts,
            data_payload=dict(payload),
            state_hash=digest,
        )

    def chain_to(self, phase_id: str, payload: Dict[str, Any]) -> "StateSnapshot":
        return StateSnapshot.create(phase_id, payload, parent_hash=self.state_hash)

    def verify_link(self, parent: Optional["StateSnapshot"]) -> bool:
        """True se questo snapshot e' davvero agganciato a `parent`."""
        if parent is None:
            return self.parent_hash is None
        return self.parent_hash == parent.state_hash

    def to_dict(self) -> Dict[str, Any]:
        return {
            "state_id": self.state_id,
            "parent_hash": self.parent_hash,
            "phase_id": self.phase_id,
            "timestamp_utc": self.timestamp_utc,
            "state_hash": self.state_hash,
        }


def verify_chain(snapshots: Tuple[StateSnapshot, ...]) -> bool:
    """Verifica che una sequenza di snapshot sia una catena intatta."""
    if not snapshots:
        return False
    if snapshots[0].parent_hash is not None:
        return False
    for parent, child in zip(snapshots, snapshots[1:]):
        if not child.verify_link(parent):
            return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
# Esito dei gate
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class GateCheck:
    """Un singolo controllo. `passed` deve venire da un predicato reale."""
    check_id: str
    description: str
    passed: bool
    detail: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "check_id": self.check_id,
            "description": self.description,
            "passed": self.passed,
            "detail": self.detail,
        }


@dataclass(frozen=True)
class GateResult:
    """
    Esito di un gate. Costruito solo da `build()`, che calcola score e passed
    dai check: non e' possibile dichiarare un esito che i check non sostengono.
    """
    gate_id: str
    level: int
    passed: bool
    score: float
    threshold: float
    checks: Tuple[GateCheck, ...]
    duration_ms: float = 0.0

    @classmethod
    def build(
        cls,
        gate_id: str,
        level: int,
        threshold: float,
        checks: Tuple[GateCheck, ...],
        duration_ms: float = 0.0,
    ) -> "GateResult":
        if not checks:
            raise ValueError(f"{gate_id}: un gate senza check non e' un gate")
        passed_n = sum(1 for c in checks if c.passed)
        score = passed_n / len(checks)
        return cls(
            gate_id=gate_id,
            level=level,
            # soglia E zero fallimenti: nessun credito parziale mascherato
            passed=(score >= threshold) and (passed_n == len(checks)),
            score=score,
            threshold=threshold,
            checks=tuple(checks),
            duration_ms=duration_ms,
        )

    @property
    def failures(self) -> Tuple[GateCheck, ...]:
        return tuple(c for c in self.checks if not c.passed)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "gate_id": self.gate_id,
            "level": self.level,
            "passed": self.passed,
            "score": round(self.score, 4),
            "threshold": self.threshold,
            "checks_total": len(self.checks),
            "checks_passed": sum(1 for c in self.checks if c.passed),
            "failures": [c.to_dict() for c in self.failures],
            "duration_ms": round(self.duration_ms, 3),
        }


class GateBlocked(RuntimeError):
    """Sollevata quando un gate bloccante non passa. Porta con se' l'esito."""

    def __init__(self, result: GateResult):
        self.result = result
        motivi = "; ".join(f"{c.check_id}: {c.detail or c.description}" for c in result.failures)
        super().__init__(f"{result.gate_id} BLOCCATO ({result.score:.0%} < {result.threshold:.0%}) — {motivi}")


# ─────────────────────────────────────────────────────────────────────────────
# Utilita' numeriche condivise
# ─────────────────────────────────────────────────────────────────────────────

def is_finite_number(v: Any) -> bool:
    """True solo per int/float reali e finiti. bool e' escluso di proposito."""
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return False
    return math.isfinite(float(v))


def new_run_id(prefix: str = "RUN") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"
