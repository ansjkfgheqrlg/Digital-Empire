"""
EMPIRE — loader: trasforma i .md dell'azienda in oggetti empire.schema.

Owner: Gael · Controllore: Claude · Origine: FORGE (lotto G-A, CP-20260722)
Governo: MANDATO Art.8 + ADR-008 (Provenance) + ADR-003 (tollerante, non riscrive)

Realtà misurata campionando 10 schede da fonti diverse (company/Ecosistemi/09-OPERATIONS,
company/Ecosistemi/08-INTELLIGENCE, company/Board-CSuite/CEO-*, company/Ispettorato/agenti,
WORKFLOW-ESTATE/03-AGENTI-E-RUOLI, DIGITAL-EMPIRE/04-AGENTS): il formato NON è uniforme.
  - company/Ecosistemi/*/Agenti/*.md      : niente frontmatter YAML, tabella "| Campo | Valore |"
  - company/Board-CSuite/*/agenti/*.md    : frontmatter YAML (Type/Status/Tags/Created) + blockquote **ID:**
  - company/Ispettorato/agenti/*.md       : frontmatter YAML + bullet "- **ID**:"
  - WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/*.md: niente frontmatter, niente campo ID esplicito
  - DIGITAL-EMPIRE/04-AGENTS/**/*.md      : niente frontmatter, bullet "- **Ruolo:**"
Quindi: load_frontmatter non deve mai fallire, e l'estrazione dei campi prova più pattern
in sequenza prima di arrendersi (None = finding ADR-008, non crash).
"""
from __future__ import annotations

import re
from dataclasses import replace

from .paths import repo_root, resolve, rel
from .schema import Agent, Department, Ecosystem, Workflow, Skill, Provenance

__all__ = [
    "load_frontmatter", "load_agents", "load_departments", "load_ecosystems",
    "load_workflows", "load_skills",
]

_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_YAML_LINE_RE = re.compile(r"^([A-Za-z][\w \-]*):\s*(.*)$")

# prefissi generici, ridondanti col contenuto: si tolgono per ottenere un id pulito
_ID_PREFIXES = ("AGENTE-", "AGENTE_", "AGENT-")

_CF_GRADE_FILES = (
    "agent.md", "system_prompt.md", "tools.md", "playbook.md",
    "failure_modes.md", "eval_cases.json", "README.md",
)

_EXCLUDE_FILENAMES = {"AGENTS-REGISTRY.md", "README.md", "ECOSISTEMA.md", "BACKBONE.md"}


def load_frontmatter(path) -> dict:
    """YAML frontmatter minimale (stdlib-only, niente pyyaml). Tollerante: mai solleva.

    La maggioranza dei file NON ha frontmatter -> restituisce {} (Provenance resta None,
    e' un finding ADR-008 per GEM-04, non un errore di questo loader).
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        lm = _YAML_LINE_RE.match(line)
        if not lm:
            continue
        key, val = lm.group(1).strip(), lm.group(2).strip()
        out[key] = val.strip('"').strip("'")
    return out


def _read(path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _extract_field(text: str, *labels: str) -> str | None:
    """Prova, in ordine, i formati osservati sul campione reale:
    tabella markdown | Label | Valore |, blockquote/bullet **Label:** valore,
    bullet "- **Label**: valore". Ritorna il primo match non vuoto o None.
    """
    for label in labels:
        esc = re.escape(label)
        patterns = (
            rf"^\s*\|\s*{esc}\s*\|\s*`?([^|`\n]+?)`?\s*\|\s*$",
            rf"-\s*\*\*{esc}\*\*:?\s*`?([^\n`|·]+)",
            rf"\*\*{esc}:?\*\*:?\s*`?([^\n`|·]+)",
        )
        for pat in patterns:
            m = re.search(pat, text, re.IGNORECASE | re.MULTILINE)
            if m:
                val = m.group(1).strip().strip("*").strip()
                if val:
                    return val
    return None


def _extract_list_field(text: str, *labels: str) -> list[str]:
    val = _extract_field(text, *labels)
    if not val:
        return []
    parts = re.split(r"[,/·]| e ", val)
    return [p.strip().strip("`") for p in parts if p.strip()]


def _id_from_filename(path) -> str:
    stem = path.stem
    for pref in _ID_PREFIXES:
        if stem.upper().startswith(pref):
            stem = stem[len(pref):]
            break
    return stem.strip("-_") or path.stem


def _title_from_content(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if not m:
        return fallback
    title = m.group(1).strip()
    title = re.split(r"\s+—\s+|\s+-\s+", title, maxsplit=1)
    return title[-1].strip() if len(title) > 1 else title[0].strip()


def _cf_grade(path) -> bool:
    d = path.parent
    return all((d / f).exists() for f in _CF_GRADE_FILES)


def _provenance(path, fm: dict) -> Provenance:
    return Provenance(
        owner=fm.get("Owner") or fm.get("owner"),
        controller=fm.get("Controller") or fm.get("controller") or fm.get("Controllore"),
        origin=fm.get("Origin") or fm.get("origin") or fm.get("Origine"),
        governance=fm.get("Governance") or fm.get("governance") or fm.get("Governo"),
        source_file=path,
        line=1 if fm else None,
    )


def _ecosystem_from_path(path) -> str | None:
    try:
        r = rel(path)
    except Exception:
        return None
    m = re.match(r"company/Ecosistemi/([^/]+)/", r)
    if m:
        return m.group(1)
    m = re.match(r"DIGITAL-EMPIRE/.*", r)
    if m:
        return None
    return None


def _agent_files() -> list:
    seen = set()
    out = []
    patterns = [
        (resolve("ecosistemi"), "**/Agenti/*.md"),
        (resolve("board"), "**/agenti/*.md"),
        (resolve("ispettorato") / "agenti", "*.md"),
        (resolve("wf_agenti"), "*.md"),
        (resolve("estate_agents"), "**/*.md"),
    ]
    for base, pattern in patterns:
        if not base.exists():
            continue
        for p in base.glob(pattern):
            if not p.is_file():
                continue
            if p.name in _EXCLUDE_FILENAMES:
                continue
            rp = p.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            out.append(p)
    return out


def load_agents(ecosystem: str | None = None) -> list[Agent]:
    agents: list[Agent] = []
    for path in _agent_files():
        text = _read(path)
        if not text:
            continue
        fm = load_frontmatter(path)

        agent_id = _extract_field(text, "ID") or _id_from_filename(path)
        name = _title_from_content(text, fallback=_id_from_filename(path))
        eco = _ecosystem_from_path(path) or _extract_field(text, "Ecosistema", "Ecosistemi")
        role = _extract_field(text, "Ruolo", "Tipo")
        tier = _extract_field(text, "Tier modello", "Tier", "Livello")
        dept = _extract_field(text, "Reparto", "Team")
        skills = _extract_list_field(text, "Skill", "Skills", "Tools")
        workflows = _extract_list_field(text, "Workflow", "Workflows")

        if ecosystem and eco != ecosystem:
            continue

        agents.append(Agent(
            id=agent_id,
            name=name,
            path=path,
            ecosystem=eco,
            department=dept,
            role=role,
            tier=tier.lower() if tier else None,
            skills=skills,
            workflows=workflows,
            cf_grade=_cf_grade(path),
            prov=_provenance(path, fm),
        ))
    return agents


def _department_dirs() -> list:
    out = []
    eco_root = resolve("ecosistemi")
    if eco_root.exists():
        for eco_dir in eco_root.iterdir():
            if not eco_dir.is_dir():
                continue
            reparti = eco_dir / "Reparti"
            if reparti.exists():
                out.extend(d for d in reparti.iterdir() if d.is_dir())
    board_root = resolve("board")
    if board_root.exists():
        out.extend(d for d in board_root.iterdir() if d.is_dir())
    return out


def load_departments() -> list[Department]:
    agents_by_source = load_agents()
    depts: list[Department] = []
    for d in _department_dirs():
        try:
            r = rel(d)
        except Exception:
            r = str(d)
        eco = None
        m = re.match(r"company/Ecosistemi/([^/]+)/", r)
        if m:
            eco = m.group(1)
        dept_id = d.name
        dept_agents = [a.id for a in agents_by_source if a.department == dept_id
                       or (a.path.exists() and str(d) in str(a.path))]
        depts.append(Department(
            id=dept_id,
            path=d,
            ecosystem=eco,
            agents=dept_agents,
            prov=Provenance(source_file=d / "README.md" if (d / "README.md").exists() else None),
        ))
    return depts


def load_ecosystems() -> list[Ecosystem]:
    out: list[Ecosystem] = []
    eco_root = resolve("ecosistemi")
    if not eco_root.exists():
        return out
    agents = load_agents()
    for d in sorted(p for p in eco_root.iterdir() if p.is_dir()):
        eco_md = d / "ECOSISTEMA.md"
        backbone_md = d / "BACKBONE.md"
        name = eco_md.exists() and _title_from_content(_read(eco_md), d.name) or d.name
        reparti = d / "Reparti"
        dep_ids = [p.name for p in reparti.iterdir() if p.is_dir()] if reparti.exists() else []
        count = sum(1 for a in agents if a.ecosystem == d.name)
        out.append(Ecosystem(
            id=d.name,
            name=name,
            path=d,
            departments=dep_ids,
            agents_count=count,
            has_backbone=backbone_md.exists(),
            has_ecosistema_md=eco_md.exists(),
            prov=_provenance(eco_md, load_frontmatter(eco_md)) if eco_md.exists() else Provenance(source_file=d),
        ))
    return out


_PATH_REF_RE = re.compile(
    r"`([0-9A-Za-z][\w\-]*(?:/[\w\-. ]+)+/?)`"
    r"|((?:[0-9]{2}-[A-Z][\w\-]*|company|WORKFLOW-ESTATE|DIGITAL-EMPIRE|EmpireDesk)"
    r"(?:/[\w\-. ]+)*\.?(?:md|py|yaml|yml|json|toml)?)"
)


def _extract_referenced_paths(text: str) -> list[str]:
    found: list[str] = []
    for m in _PATH_REF_RE.finditer(text):
        ref = (m.group(1) or m.group(2) or "").strip()
        if not ref or "/" not in ref:
            continue
        if len(ref) > 120:
            continue
        found.append(ref)
    seen = set()
    out = []
    for r in found:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def _workflow_files() -> list:
    seen = set()
    out = []
    candidates = [
        resolve("wf_flussi") if (resolve("estate_wf") / "01-FLUSSI-E-PIANI").exists() else None,
    ]
    bases = [resolve("estate_wf") / "01-FLUSSI-E-PIANI", resolve("estate_flows")]
    for base in bases:
        if not base or not base.exists():
            continue
        for p in base.glob("*.md"):
            rp = p.resolve()
            if rp not in seen:
                seen.add(rp)
                out.append(p)
    return out


def load_workflows() -> list[Workflow]:
    out: list[Workflow] = []
    for path in _workflow_files():
        text = _read(path)
        if not text:
            continue
        fm = load_frontmatter(path)
        wf_id = _extract_field(text, "ID") or path.stem
        owner = _extract_field(text, "Owner", "Proprietario")
        steps = re.findall(r"^#{2,3}\s*(S\d+(?:\.\d+)?[^\n]*)", text, re.MULTILINE)
        gates = re.findall(r"\bgate[s]?\b[^\n]*", text, re.IGNORECASE)[:20]
        out.append(Workflow(
            id=wf_id,
            path=path,
            owner=owner,
            steps=[s.strip() for s in steps],
            gates=[g.strip() for g in gates],
            referenced_paths=_extract_referenced_paths(text),
            prov=_provenance(path, fm),
        ))
    return out


def _skill_dirs() -> list:
    seen = set()
    out = []
    bases = [
        (resolve("skills_project"), "project"),
        (resolve("estate_skills"), "estate"),
        (resolve("wf_skills"), "estate"),
    ]
    for base, scope in bases:
        if not base.exists():
            continue
        for p in base.iterdir():
            if p.is_dir() and p.resolve() not in seen:
                seen.add(p.resolve())
                out.append((p, scope))
    return out


def load_skills() -> list[Skill]:
    out: list[Skill] = []
    for d, scope in _skill_dirs():
        skill_md = d / "SKILL.md"
        out.append(Skill(
            name=d.name,
            path=d,
            scope=scope,
            has_skill_md=skill_md.exists(),
            prov=_provenance(skill_md, load_frontmatter(skill_md)) if skill_md.exists() else Provenance(source_file=d),
        ))
    return out