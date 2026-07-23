"""
EMPIRE — plugin CLI: index, find, show.
Owner: Gael · Origine: FORGE (lotto G-A). Caricato dal loop di plugin di cli.py.
"""
from __future__ import annotations

import json
import sys

from . import index as _index
from . import loader


def cmd_index(a) -> int:
    if a.rebuild:
        data = _index.build_index()
    else:
        data = _index.load_index()
    if a.json:
        print(json.dumps({"counts": {k: len(v) for k, v in data.items()}}, indent=2, ensure_ascii=False))
        return 0
    st = _index.stats()
    print("EMPIRE INDEX")
    for k, v in st["counts"].items():
        print(f"  {k:12} {v}")
    print(f"  cf_grade agenti      {st['agents_cf_grade']}")
    print(f"  agenti senza owner   {st['agents_no_provenance']}")
    return 0


def cmd_find(a) -> int:
    results = _index.search(a.query, kind=a.kind)
    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0
    if not results:
        print(f"nessun risultato per {a.query!r}")
        return 1
    for r in results:
        print(f"[{r['kind']:11}] {r.get('id') or r.get('name')}  ({r.get('path')})")
    print(f"\ntotale: {len(results)}")
    return 0


_KIND_LOADERS = {
    "agent": loader.load_agents,
    "ecosystem": loader.load_ecosystems,
    "workflow": loader.load_workflows,
    "skill": loader.load_skills,
    "department": loader.load_departments,
}


def cmd_show(a) -> int:
    fn = _KIND_LOADERS.get(a.kind)
    if fn is None:
        print(f"tipo sconosciuto: {a.kind}. Noti: {', '.join(_KIND_LOADERS)}", file=sys.stderr)
        return 2
    id_field = "name" if a.kind == "skill" else "id"
    for item in fn():
        if getattr(item, id_field, None) == a.id:
            print(json.dumps(item.to_dict(), indent=2, ensure_ascii=False))
            return 0
    print(f"non trovato: {a.kind} {a.id!r}", file=sys.stderr)
    return 1


def register(sub) -> None:
    p = sub.add_parser("index", help="costruisce/mostra l'indice materializzato")
    p.add_argument("--rebuild", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_index)

    p = sub.add_parser("find", help="ricerca substring su id/nome/path/skill")
    p.add_argument("query")
    p.add_argument("--kind", default=None, choices=list(_index._KIND_LOADERS.keys()))
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_find)

    p = sub.add_parser("show", help="mostra un artefatto per id (es. show agent ops-watchdog)")
    p.add_argument("kind", choices=list(_KIND_LOADERS.keys()))
    p.add_argument("id")
    p.set_defaults(fn=cmd_show)
