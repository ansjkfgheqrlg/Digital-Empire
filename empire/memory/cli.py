"""
EMPIRE MEMORY — sottocomandi `python -m empire mem ...`

Owner: Max · Controllore: Claude · Origine: FORGE (M-A)

Registrato via il loop di plugin di empire/cli.py: questo file non modifica la CLI base.
"""
from __future__ import annotations

import json
import sys

from . import ingest as _ingest
from . import state as _state
from .model import Atom, KINDS
from .render import render, write_view
from .search import recall as _recall, search as _search
from .store import all_atoms, read as _read, stats as _stats, write as _write

EXIT_OK, EXIT_ERR = 0, 2


def _dump(obj) -> int:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))
    return EXIT_OK


def cmd_write(a) -> int:
    body = a.body or ""
    if body == "-":
        body = sys.stdin.read()
    atom = Atom(
        kind=a.kind, title=a.title, body=body, actor=a.actor or "", task=a.task or "",
        workflow=a.workflow or "", ecosystem=a.eco or "", status=a.status or "",
        refs=a.refs or [], artifacts=a.artifacts or [],
    )
    got = _write(atom)
    print(f"scritto {got.id}  ({got.kind})  {got.title}")
    if a.view:
        p = write_view(got)
        print(f"vista:  {p}")
    return EXIT_OK


def cmd_read(a) -> int:
    atom = _read(a.id)
    if not atom:
        print(f"atomo non trovato: {a.id}", file=sys.stderr)
        return EXIT_ERR
    if a.json:
        return _dump(atom.to_dict())
    print(render(atom))
    return EXIT_OK


def cmd_list(a) -> int:
    rows = [x for x in all_atoms(kind=a.kind) if not a.since or x.ts[:10] >= a.since]
    rows.sort(key=lambda x: x.ts, reverse=True)
    rows = rows[: a.limit]
    if a.json:
        return _dump([r.to_dict() for r in rows])
    for r in rows:
        flag = f"[{r.status}]" if r.status else ""
        print(f"{r.id:22} {r.ts[:10]} {r.kind:10} {flag:12} {r.title[:80]}")
    print(f"\n  {len(rows)} atomi")
    return EXIT_OK


def cmd_search(a) -> int:
    hits = _search(a.query, kind=a.kind, limit=a.limit)
    if a.json:
        return _dump([{"score": s, **at.to_dict()} for at, s in hits])
    for at, s in hits:
        print(f"[{s:2}] {at.id:22} {at.kind:10} {at.title[:90]}")
    print(f"\n  {len(hits)} risultati")
    return EXIT_OK


def cmd_recall(a) -> int:
    print(_recall(a.topic, max_lines=a.lines))
    return EXIT_OK


def cmd_status(a) -> int:
    s = _stats()
    if a.json:
        return _dump(s)
    print("MEMORY STATUS")
    print(f"  archivio   {s['path']}")
    print(f"  atomi      {s['total']}")
    for k, v in s["by_kind"].items():
        print(f"    {k:12} {v}")
    if s["last"]:
        print(f"  ultimo     {s['last']['id']} — {s['last']['title'][:70]}")
    if s["total"] == 0:
        print("\n  archivio vuoto: esegui `python -m empire mem ingest --dry-run` per vedere "
              "quanti atomi verrebbero importati dai sistemi esistenti.")
    return EXIT_OK


def cmd_render(a) -> int:
    atom = _read(a.id)
    if not atom:
        print(f"atomo non trovato: {a.id}", file=sys.stderr)
        return EXIT_ERR
    p = write_view(atom, overwrite=a.force)
    print(f"vista scritta: {p}")
    return EXIT_OK


def cmd_ingest(a) -> int:
    rep = _ingest.ingest_all(dry_run=not a.apply)
    print(rep)
    if not a.apply:
        print("\n  DRY-RUN: nulla e' stato scritto. Rilancia con --apply per importare davvero.")
    return EXIT_OK


def cmd_state(a) -> int:
    block = _state.prepend(write=a.write)
    print(block)
    if a.write:
        print("\n  scritto in company/Memory/STATO-EMPIRE.md (solo dentro i marcatori)")
    return EXIT_OK


def register(sub) -> None:
    p = sub.add_parser("mem", help="memoria dell'azienda (atomi, ricerca, recall)")
    ms = p.add_subparsers(dest="memcmd", required=True)

    q = ms.add_parser("write", help="scrive un atomo")
    q.add_argument("--kind", required=True, choices=sorted(KINDS))
    q.add_argument("--title", required=True)
    q.add_argument("--body", default="", help="testo integrale; '-' legge da stdin")
    q.add_argument("--actor"); q.add_argument("--task"); q.add_argument("--workflow")
    q.add_argument("--eco"); q.add_argument("--status")
    q.add_argument("--refs", nargs="*"); q.add_argument("--artifacts", nargs="*")
    q.add_argument("--view", action="store_true", help="scrive anche la vista Markdown")
    q.set_defaults(fn=cmd_write)

    q = ms.add_parser("read", help="legge un atomo")
    q.add_argument("id"); q.add_argument("--json", action="store_true")
    q.set_defaults(fn=cmd_read)

    q = ms.add_parser("list", help="elenca atomi")
    q.add_argument("--kind", choices=sorted(KINDS)); q.add_argument("--since")
    q.add_argument("--limit", type=int, default=30); q.add_argument("--json", action="store_true")
    q.set_defaults(fn=cmd_list)

    q = ms.add_parser("search", help="ricerca full-text")
    q.add_argument("query"); q.add_argument("--kind", choices=sorted(KINDS))
    q.add_argument("--limit", type=int, default=20); q.add_argument("--json", action="store_true")
    q.set_defaults(fn=cmd_search)

    q = ms.add_parser("recall", help="cosa sapere PRIMA di lavorare su un argomento (ADR-002)")
    q.add_argument("topic"); q.add_argument("--lines", type=int, default=40)
    q.set_defaults(fn=cmd_recall)

    q = ms.add_parser("status", help="stato dell'archivio")
    q.add_argument("--json", action="store_true"); q.set_defaults(fn=cmd_status)

    q = ms.add_parser("render", help="rigenera la vista Markdown di un atomo")
    q.add_argument("id"); q.add_argument("--force", action="store_true")
    q.set_defaults(fn=cmd_render)

    q = ms.add_parser("ingest", help="import storico dei sistemi di memoria esistenti")
    q.add_argument("--apply", action="store_true", help="senza questo flag e' un dry-run")
    q.set_defaults(fn=cmd_ingest)

    q = ms.add_parser("state", help="blocco riassuntivo per STATO-EMPIRE.md")
    q.add_argument("--write", action="store_true")
    q.set_defaults(fn=cmd_state)
