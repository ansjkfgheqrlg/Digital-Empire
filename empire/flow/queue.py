"""
EMPIRE FLOW — coda risorse: max 1 swarm pesante, ordine di precedenza (GEM-06 §4.5).

Owner: Gael · Origine: FORGE (lotto G-C, CP-20260722)

Regole letterali da WF-MASTER.md §"Regole di orchestrazione":
- max 1 swarm pesante (Opus) alla volta
- ordine di precedenza S1 > S2 > S6 > S5, il resto degrada a esecuzione singola
- revenue-first: a parità di dipendenze soddisfatte vince il task con EUR/h più alto
- budget-guard (CLAUDE.md): sotto il 20% di risorse di sessione, rifiuta nuovi avvii pesanti
"""
from __future__ import annotations

from dataclasses import dataclass

__all__ = ["PRECEDENCE_ORDER", "SwarmRequest", "admit"]

PRECEDENCE_ORDER = ["S1", "S2", "S6", "S5"]


@dataclass(slots=True)
class SwarmRequest:
    stream: str            # "S1".."S6"
    requested_by: str
    eur_ora: float = 0.0   # per il criterio revenue-first a parità di precedenza


def _rank(stream: str) -> int:
    try:
        return PRECEDENCE_ORDER.index(stream)
    except ValueError:
        return len(PRECEDENCE_ORDER)  # non in lista -> ultima posizione


def admit(requests: list[SwarmRequest], *, budget_pct: float = 100.0) -> tuple[SwarmRequest | None, list[SwarmRequest]]:
    """Data una lista di richieste di swarm pesante simultanee, decide quale parte
    e mette le altre in coda, nell'ordine S1 > S2 > S6 > S5 (poi EUR/h decrescente).
    Sotto il 20% di budget di sessione, rifiuta TUTTI i nuovi avvii pesanti
    (budget-guard, CLAUDE.md) restituendo (None, tutte le richieste in coda).
    """
    if not requests:
        return None, []
    if budget_pct < 20.0:
        return None, list(requests)

    ordered = sorted(requests, key=lambda r: (_rank(r.stream), -r.eur_ora))
    winner, *rest = ordered
    return winner, rest
