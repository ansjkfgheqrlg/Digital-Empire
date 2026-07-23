"""
EMPIRE — plugin CLI: agents, ecosystems, workflows, skills.
Owner: Gael · Origine: FORGE (lotto G-A). Caricato dal loop di plugin di cli.py, zero edit a cli.py.
"""
from __future__ import annotations

import json

from . import loader


def _emit(items, as_json: bool, fields: tuple[str, ...]) -> int:
    if as_json:
        print(json.dumps([it.to_dict() for it in items], indent=2, ensure_ascii=False))
        return 0
    if not items:
        print("(nessun risultato)")
        return 0
    for it in items:
        row = " | ".join(str(getattr(it, f, "")) for f in fields)
        print(row)
    print(f"\ntotale: {len(items)}")
    return 0


def cmd_agents(a) -> int:
    items = loader.load_agents(ecosystem=a.eco)
    return _emit(items, a.json, ("id", "name", "ecosystem", "role", "tier"))


def cmd_ecosystems(a) -> int:
    items = loader.load_ecosystems()
    return _emit(items, a.json, ("id", "name", "agents_count", "has_backbone", "has_ecosistema_md"))


def cmd_departments(a) -> int:
    items = loader.load_departments()
    return _emit(items, a.json, ("id", "ecosystem"))


def cmd_workflows(a) -> int:
    items = loader.load_workflows()
    return _emit(items, a.json, ("id", "owner"))


def cmd_skills(a) -> int:
    items = loader.load_skills()
    if a.missing:
        items = [s for s in items if not s.has_skill_md]
    return _emit(items, a.json, ("name", "scope", "has_skill_md"))


def register(sub) -> None:
    p = sub.add_parser("agents", help="elenca gli agenti dell'azienda")
    p.add_argument("--eco", default=None, help="filtra per ecosistema (es. 09-OPERATIONS)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_agents)

    p = sub.add_parser("ecosystems", help="elenca gli ecosistemi")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_ecosystems)

    p = sub.add_parser("departments", help="elenca i reparti")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_departments)

    p = sub.add_parser("workflows", help="elenca i workflow (Markdown, non lo yaml eseguibile)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_workflows)

    p = sub.add_parser("skills", help="elenca le skill")
    p.add_argument("--missing", action="store_true", help="solo skill senza SKILL.md")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_skills)