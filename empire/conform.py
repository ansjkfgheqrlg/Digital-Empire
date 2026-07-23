"""
EMPIRE — conformità al Mandato.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
Governo: MANDATO Art.8 (6 pilastri) + ADR-003 (wrap) + ADR-008 (intestazione)

Controlli implementati nel seed:
  check_art8()   — i 6 pilastri di una cartella-workflow esistono E non sono vuoti
  check_links()  — ogni path citato nei .md esiste, direttamente o via resolve_legacy()

Estensione consentita: AGGIUNGERE nuove funzioni check_*(). Modificare quelle
esistenti richiede nota di coordinamento in company/Memory/STATO-EMPIRE.md.
"""
from __future__ import annotations

import re
from pathlib import Path

from .paths import iter_files, repo_root, resolve, resolve_legacy, rel
from .schema import Finding

__all__ = ["ART8_PILLARS", "ADR001_ECOSYSTEMS", "is_planning_doc", "is_vendored",
           "check_art8", "check_links",
           "check_adr001", "run_all"]

# ADR-001 — EMPIRE OS e' una holding di ESATTAMENTE 10 ecosistemi.
# I nomi sono canonici: una cartella in company/Ecosistemi/ che non e' in questo elenco
# non e' un ecosistema, e' altro (una skill, un progetto, un import) messo nel posto sbagliato.
ADR001_ECOSYSTEMS = (
    "01-AGENCY", "02-INFO-BUSINESS", "03-CONTENT-FACTORY", "04-MARKETING",
    "05-MULTI-BUSINESS", "06-PLATFORM", "07-FORGE", "08-INTELLIGENCE",
    "09-OPERATIONS", "10-MEMORY", "11-APEX-7-CORE", "12-STREAM-S7-BOT",
    "13-ARENA-APEX"
)

# Mandato Art.8 §8.2 — i 6 pilastri obbligatori di ogni cartella-workflow
ART8_PILLARS = (
    ("01-FLUSSI-E-PIANI", "flussi operativi .md + workflows.yaml"),
    ("02-AUTOMAZIONI-E-SCRIPTS", "codice reale eseguibile (.py/.bat/.ps1)"),
    ("03-AGENTI-E-RUOLI", "schede operative degli agenti/persone"),
    ("04-SKILLS-E-REFERENCE", "SKILL.md e reference operative"),
    ("05-TEMPLATES-E-KIT", "materiali di delivery pronti"),
    ("06-DASHBOARD-E-METRICHE", "cruscotto KPI numerici"),
)

# Riferimenti a path dentro i .md: backtick, oppure token con '/' e estensione nota.
_REF_IN_BACKTICKS = re.compile(r"`([^`\n]{3,160})`")
_LOOKS_LIKE_PATH = re.compile(
    r"^[A-Za-z0-9._\-/ ]+/[A-Za-z0-9._\- ]*(\.(md|py|ya?ml|json|bat|ps1|txt|html|csv))?$"
)
_SKIP_PREFIX = ("http://", "https://", "python ", "python3 ", "cd ", "git ", "$ ", "npm ",
                "pip ", "powershell", "#", "-", "|", "python -m")

# Aree con governo proprio: skill vendorizzate (repo di terzi) e artefatti di run.
# I loro riferimenti interni non sono responsabilita' di Digital Empire.
_VENDORED_PARTS = (".agents", "04-SKILLS-E-REFERENCE", "05-SKILLS", "skills",
                   "node_modules", "assets/templates", "assets/examples")
_RUN_ARTIFACT_PREFIX = ("forge-run-", "phase7-run", "phase9-regression", "packaged-final")


# Documenti di pianificazione: citano per definizione artefatti ancora da costruire.
_PLANNING_PREFIX = ("PIANO-", "PLAN-", "PLANNING-", "ARCHITETTURA-", "ARCHITECTURE-",
                    "ROADMAP", "SPEC", "TASK-", "GEM-", "BRIEF-")
_PLANNING_DIRS = ("Antigravity-Briefs", "plans", "01-PLANNING", "02-ARCHITECTURE", "tasks")


def is_planning_doc(p: Path) -> bool:
    """True se il file e' un piano/brief/spec: i suoi riferimenti sono al futuro, non al presente."""
    name = p.name.upper()
    if name.startswith(_PLANNING_PREFIX):
        return True
    return any(d in p.parts for d in _PLANNING_DIRS)


def is_vendored(p: Path) -> bool:
    """True se il file appartiene a un'area con governo esterno o a un artefatto di run."""
    parts = p.parts
    if any(v in parts for v in _VENDORED_PARTS):
        return True
    return any(part.startswith(_RUN_ARTIFACT_PREFIX) for part in parts)


def _is_candidate_ref(tok: str) -> bool:
    t = tok.strip()
    if len(t) < 4 or "/" not in t:
        return False
    low = t.lower()
    if any(low.startswith(p) for p in _SKIP_PREFIX):
        return False
    if any(c in t for c in "()[]{}<>*?\"'`\\|"):
        return False
    if t.count("/") > 8:
        return False
    return bool(_LOOKS_LIKE_PATH.match(t))


def check_art8(workflow_root: Path | str) -> list[Finding]:
    """Mandato Art.8: i 6 pilastri esistono e NON sono vuoti.

    Un pilastro vuoto => 'Workflow Abusivo / Incompleto' (Art.8 §8.3), severità block.
    """
    root = Path(workflow_root)
    if not root.is_absolute():
        root = repo_root() / root
    out: list[Finding] = []

    if not root.is_dir():
        return [Finding("block", "MANDATO-Art8", root,
                        "cartella-workflow inesistente",
                        "creare la directory radice del workflow (Art.8 §8.1)")]

    for pillar, what in ART8_PILLARS:
        d = root / pillar
        if not d.is_dir():
            out.append(Finding(
                "block", "MANDATO-Art8", d,
                f"pilastro mancante: {pillar} ({what})",
                f"mkdir '{rel(d)}' e popolarlo con materiale reale, non segnaposto"))
            continue
        has_content = any(True for _ in iter_files(d))
        if not has_content:
            out.append(Finding(
                "block", "MANDATO-Art8", d,
                f"pilastro VUOTO: {pillar} ({what}) -> workflow abusivo (Art.8 §8.3)",
                "spostare qui materiale REALE gia' esistente nel monorepo; "
                "vietato riempire con file finti"))
    return out


def check_links(base: Path | str, *, limit_files: int | None = None,
                include_vendored: bool = False) -> list[Finding]:
    """Ogni path citato dentro i .md esiste, direttamente o via resolve_legacy().

    LINK-DEAD    block -> non risolve da nessuna parte, in un documento operativo
    LINK-FIXABLE info  -> risolve via alias legacy (rotto ma riparabile a runtime)
    LINK-PLANNED info  -> non esiste ANCORA, ma il file e' un piano: e' cio' che un piano fa

    Escluse per default: skill vendorizzate e artefatti di run (governo proprio).
    """
    root = Path(base)
    if not root.is_absolute():
        root = repo_root() / root
    out: list[Finding] = []
    seen: set[tuple[str, str]] = set()

    files = list(iter_files(root, suffixes=(".md",)))
    if not include_vendored:
        files = [f for f in files if not is_vendored(f)]
    if limit_files:
        files = files[:limit_files]

    for md in files:
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for tok in _REF_IN_BACKTICKS.findall(line):
                tok = tok.strip()
                if not _is_candidate_ref(tok):
                    continue
                key = (rel(md), tok)
                if key in seen:
                    continue
                seen.add(key)

                direct = (md.parent / tok)
                if direct.exists() or (repo_root() / tok).exists():
                    continue

                fixed = resolve_legacy(tok, cited_from=md)
                if fixed is not None:
                    out.append(Finding(
                        "info", "LINK-FIXABLE", md,
                        f"riferimento rotto ma riparabile: `{tok}`",
                        f"path reale: {rel(fixed)}  (risolto via empire.paths.resolve_legacy)",
                        line=lineno, target=tok))
                elif is_planning_doc(md):
                    # Un piano cita per definizione artefatti non ancora costruiti.
                    # Marcarli 'block' produce rumore e fa smettere di guardare il report.
                    out.append(Finding(
                        "info", "LINK-PLANNED", md,
                        f"artefatto pianificato non ancora esistente: `{tok}`",
                        "atteso: lo crea il lotto che questo piano descrive; "
                        "diventa LINK-DEAD se il piano si chiude senza averlo prodotto",
                        line=lineno, target=tok))
                else:
                    out.append(Finding(
                        "block", "LINK-DEAD", md,
                        f"riferimento inesistente: `{tok}`",
                        "correggere il riferimento o creare l'artefatto mancante",
                        line=lineno, target=tok))
    return out


def check_adr001() -> list[Finding]:
    """ADR-001 (esteso da ADR-009): la holding ha esattamente 13 ecosistemi canonici.

    Espanso per includere i poli strategici: APEX-7, STREAM-S7, ARENA-APEX.
    I nomi sono rigidi per prevenire collisioni e frammentazione.
    """
    out: list[Finding] = []
    try:
        base = resolve("ecosistemi")
    except Exception:
        return out
    if not base.is_dir():
        return [Finding("block", "ADR-001", base, "company/Ecosistemi/ non esiste",
                        "ripristinare la struttura della holding")]

    found = sorted(d.name for d in base.iterdir() if d.is_dir())
    canonical = set(ADR001_ECOSYSTEMS)

    for name in ADR001_ECOSYSTEMS:
        d = base / name
        if not d.is_dir():
            out.append(Finding("block", "ADR-001", d,
                               f"ecosistema canonico mancante: {name}",
                               "ADR-001 impone i 10 ecosistemi: ricrearlo o superare l'ADR"))
            continue
        for req in ("ECOSISTEMA.md", "BACKBONE.md"):
            if not (d / req).is_file():
                out.append(Finding("warn", "ADR-001", d / req,
                                   f"{name}: manca {req}",
                                   "ogni ecosistema ha ECOSISTEMA.md (cos'e') e BACKBONE.md (come regge)"))

    # numeri duplicati: rompono ogni riferimento fatto per prefisso
    by_num: dict[str, list[str]] = {}
    for name in found:
        by_num.setdefault(name.split("-")[0], []).append(name)
    for num, names in sorted(by_num.items()):
        if len(names) > 1:
            out.append(Finding("block", "ADR-001", base,
                               f"numero di ecosistema duplicato {num}: {', '.join(names)}",
                               "rinumerare l'intruso o spostarlo fuori da company/Ecosistemi/"))

    for name in found:
        if name in canonical:
            continue
        d = base / name
        n_agents = len(list((d / "Agenti").glob("*.md"))) if (d / "Agenti").is_dir() else 0
        out.append(Finding(
            "warn", "ADR-001", d,
            f"cartella non prevista da ADR-001: {name} "
            f"({n_agents} agenti, ECOSISTEMA.md={'si' if (d / 'ECOSISTEMA.md').is_file() else 'NO'})",
            "se e' davvero un ecosistema serve un ADR che superi ADR-001; "
            "altrimenti spostarla (es. sotto Genesi-Core/, Guilds/ o il suo workflow)"))
    return out


def run_all(workflow: str | None = None) -> list[Finding]:
    """Tutti i controlli disponibili. Ordinati per severità.

    I controlli sul workflow (Art.8, link) sono per-cartella; check_adr001 riguarda
    la struttura dell'azienda e gira una volta sola.
    """
    findings: list[Finding] = list(check_adr001())
    targets = [workflow] if workflow else ["WORKFLOW-ESTATE"]
    for t in targets:
        try:
            wf_root = resolve(t)
        except Exception:
            wf_root = repo_root() / t
        findings += check_art8(wf_root)
        findings += check_links(wf_root)
    findings.sort(key=lambda f: (f.rank, str(f.path)))
    return findings
