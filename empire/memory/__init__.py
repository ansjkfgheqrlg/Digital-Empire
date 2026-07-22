"""
EMPIRE MEMORY — memoria unica dell'azienda (M-A / brief GEM-02).

Owner: Max · Controllore: Claude · Origine: FORGE · Governo: ADR-002 (memory-first)

Due livelli, una sola scrittura:
  operativo (verita')  empire/.data/memory/atoms.jsonl   append-only, indicizzato
  narrativo (vista)    company/Memory/**.md              leggibile da Max e Gael

Se divergono si rigenera la vista dagli atomi, mai il contrario.
Archiviazione INTEGRALE (skill memory-empire): il body non si riassume mai.

    from empire.memory import Atom, write, read, search, recall

ATTENZIONE ai nomi: `search`, `render` e `parse` esportati qui sono FUNZIONI e coprono i
moduli omonimi. `from empire.memory import search` restituisce la funzione, non il modulo
`empire.memory.search`. Usa sempre le funzioni: sono l'API pubblica.
"""
from __future__ import annotations

from .model import Atom, AtomError, KINDS, PREFIX, now_iso  # noqa: F401
from .store import write, write_many, read, all_atoms, next_id, stats, atoms_path, IdLockTimeout  # noqa: F401
from .render import render, parse, write_view, target_path  # noqa: F401
from .search import search, recall, build_index  # noqa: F401
from .ingest import ingest_all  # noqa: F401
from .state import build_block, prepend  # noqa: F401

__all__ = [
    "Atom", "AtomError", "KINDS", "PREFIX", "now_iso",
    "write", "read", "all_atoms", "next_id", "stats", "atoms_path", "IdLockTimeout",
    "render", "parse", "write_view", "target_path",
    "search", "recall", "build_index", "ingest_all", "build_block", "prepend",
]
