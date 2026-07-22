"""
EMPIRE MEMORY — ricerca e recall.

Owner: Max · Controllore: Claude · Origine: FORGE (M-A) · Governo: ADR-002 (memory-first)

`recall` e' il comando che rende ADR-002 ESEGUIBILE: prima di lavorare su un argomento,
restituisce in <= 40 righe cio' che l'azienda gia' sa — invece di leggere 1.267 file.

Indice invertito in standard library. Nessuna dipendenza, nessun embedding: se un giorno
servira' la semantica, sara' un ADR.
"""
from __future__ import annotations

import re
from collections import defaultdict

from .model import Atom
from .store import all_atoms

__all__ = ["search", "recall", "build_index"]

_TOKEN = re.compile(r"[a-z0-9][a-z0-9_\-\.]{1,}", re.I)
_STOP = {
    "il", "lo", "la", "i", "gli", "le", "di", "a", "da", "in", "con", "su", "per", "tra", "fra",
    "e", "o", "ma", "che", "non", "un", "una", "del", "della", "dei", "delle", "al", "alla",
    "the", "of", "and", "to", "is", "it", "as", "by",
}

# Priorita' per il recall: cosa deve emergere per primo.
_RECALL_ORDER = ["decision", "error", "pattern", "checkpoint", "plan", "metric", "retro"]


def _tokens(text: str) -> list[str]:
    return [t.lower() for t in _TOKEN.findall(text) if t.lower() not in _STOP]


def build_index(atoms: list[Atom] | None = None) -> dict[str, set[str]]:
    idx: dict[str, set[str]] = defaultdict(set)
    for a in (atoms if atoms is not None else list(all_atoms())):
        for t in set(_tokens(a.searchable())):
            idx[t].add(a.id)
    return idx


def search(query: str, *, kind: str | None = None, limit: int = 20) -> list[tuple[Atom, int]]:
    """Ricerca per termini. Punteggio = quante parole della query compaiono, + bonus nel titolo."""
    terms = _tokens(query)
    if not terms:
        return []
    out: list[tuple[Atom, int]] = []
    for a in all_atoms(kind=kind):
        hay = a.searchable()
        title = a.title.lower()
        score = 0
        for t in terms:
            if t in hay:
                score += 1
                if t in title:
                    score += 2
        if score:
            out.append((a, score))
    # piu' rilevante prima; a parita' di punteggio, il piu' recente
    out.sort(key=lambda x: x[0].ts, reverse=True)
    out.sort(key=lambda x: x[1], reverse=True)
    return out[:limit]


def recall(topic: str, *, max_lines: int = 40) -> str:
    """Cosa devo sapere PRIMA di lavorare su <topic>. Output compatto, <= max_lines righe."""
    hits = search(topic, limit=200)
    if not hits:
        return (f"RECALL «{topic}»: nessun atomo in memoria.\n"
                "Se e' un argomento nuovo, e' normale. Se non lo e', "
                "esegui `python -m empire mem ingest` (l'import storico non e' stato fatto).")

    by_kind: dict[str, list[tuple[Atom, int]]] = defaultdict(list)
    for a, s in hits:
        by_kind[a.kind].append((a, s))

    lines = [f"RECALL «{topic}» — {len(hits)} atomi rilevanti", ""]
    budget = max_lines - 3
    for kind in _RECALL_ORDER + [k for k in by_kind if k not in _RECALL_ORDER]:
        group = by_kind.get(kind)
        if not group or budget <= 2:
            continue
        group.sort(key=lambda x: x[0].ts, reverse=True)
        group.sort(key=lambda x: x[1], reverse=True)
        take = group[: 3 if kind != "decision" else 5]
        lines.append(f"## {kind} ({len(group)})")
        budget -= 1
        for a, _ in take:
            if budget <= 0:
                break
            flag = f" [{a.status}]" if a.status else ""
            lines.append(f"- {a.id}{flag} — {a.title[:110]}")
            budget -= 1
        lines.append("")
        budget -= 1
    return "\n".join(lines).rstrip()
