"""
empire.registry.orphans — rilevamento dei 4 tipi di orfano nel monorepo.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import datetime
from pathlib import Path
from typing import Sequence

from empire.paths import resolve, repo_root, resolve_legacy
from empire.schema import Artifact, Finding, Provenance

__all__ = ["check_orphans"]

# Data cutoff promulgazione ADR-008 (2026-07-19)
ADR008_CUTOFF_TIMESTAMP = datetime.datetime(2026, 7, 19, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp()

ENTRY_POINTS = {
    "empire/cli.py", "empire/schema.py", "empire/paths.py", "empire/config.py", "empire/conform.py",
    "company/REGISTRO-IMPRESA.md", "company/skills-map.yaml", "company/Mandato/MANDATO-EMPIRE.md",
    "company/Memory/STATO-EMPIRE.md", "PIANO-MAESTRO/16-PIANO-ESTATE-REVENUE.md"
}


def _is_excluded_from_orphans(art: Artifact) -> bool:
    """Verifica esclusioni dai falsi positivi per orfani (SPEC §3)."""
    if art.kind in ("vendored", "template", "asset"):
        return True
    p_posix = art.path.as_posix() if isinstance(art.path, Path) else str(art.path)
    p_lower = p_posix.lower()
    name = art.path.name if isinstance(art.path, Path) else Path(p_posix).name
    name_lower = name.lower()

    if name_lower in ("readme.md", "index.md", "changelog.md", "license", "registro-impresa.md", "skills-map.yaml"):
        return True
    if "/tests/" in p_lower or "/fixtures/" in p_lower or "/.data/" in p_lower or "/logs/" in p_lower:
        return True
    if name_lower.startswith("cp-") or "checkpoints/" in p_lower or "forge-run-" in p_lower:
        return True
    if "/05-templates-e-kit/" in p_lower or "/templates/" in p_lower or "-template." in p_lower:
        return True
    return False


def _is_registered(art: Artifact, reg_text: str, skills_text: str) -> bool:
    p_posix = art.path.as_posix() if isinstance(art.path, Path) else str(art.path)
    name = art.path.name if isinstance(art.path, Path) else Path(p_posix).name
    if p_posix in reg_text or name in reg_text:
        return True
    if p_posix in skills_text or name in skills_text or art.path.stem in skills_text:
        return True
    return False


def check_orphans(artifacts: Sequence[Artifact], root: Path | None = None) -> list[Finding]:
    """Scandisce gli artefatti restituendo le violazioni d'anagrafe (orphans)."""
    if root is None:
        root = repo_root()

    findings: list[Finding] = []

    # Carica testi registro per controllo unregistered
    reg_path = root / "company" / "REGISTRO-IMPRESA.md"
    skills_path = root / "company" / "skills-map.yaml"
    reg_text = reg_path.read_text(encoding="utf-8", errors="replace") if reg_path.exists() else ""
    skills_text = skills_path.read_text(encoding="utf-8", errors="replace") if skills_path.exists() else ""

    for art in artifacts:
        if _is_excluded_from_orphans(art):
            continue

        p_posix = art.path.as_posix() if isinstance(art.path, Path) else str(art.path)

        # 1. no-provenance (ADR-008)
        missing = art.prov.missing
        if missing:
            # Verifica cutoff temporale (2026-07-19)
            is_post_cutoff = False
            if art.mtime >= ADR008_CUTOFF_TIMESTAMP:
                is_post_cutoff = True
            elif art.git_date and "2026-07-19" <= art.git_date[:10]:
                is_post_cutoff = True

            sev = "block" if is_post_cutoff else "warn"
            msg = f"intestazione ADR-008 incompleta (mancano: {', '.join(missing)})"
            if not is_post_cutoff:
                msg += " [storico pre-19/07 -> tolleranza warn]"
            
            findings.append(Finding(
                severity=sev,
                rule="ADR-008",
                path=art.path,
                message=msg,
                fix="aggiungi frontmatter YAML: Owner, Controllore, Origine, Governo"
            ))

        # 2. unreferenced
        if not art.referenced_by and p_posix not in ENTRY_POINTS and art.kind not in ("dashboard", "ecosystem"):
            findings.append(Finding(
                severity="warn",
                rule="ORPHAN-UNREF",
                path=art.path,
                message="artefatto non referenziato da nessun altro file nel monorepo",
                fix="collegalo da un indice di reparto, dal REGISTRO-IMPRESA o da STATO-EMPIRE.md"
            ))

        # 3. unregistered (solo per artefatti maggiori: agenti, dipartimenti, workflow, skill)
        if art.kind in ("agent", "department", "workflow", "skill", "ecosystem"):
            if not _is_registered(art, reg_text, skills_text):
                findings.append(Finding(
                    severity="warn",
                    rule="UNREGISTERED",
                    path=art.path,
                    message=f"artefatto maggiore ({art.kind}) assente da REGISTRO-IMPRESA.md e da skills-map.yaml",
                    fix="registralo eseguendo python -m empire registry render"
                ))

        # 4. dead-end (riferimenti inesistenti estratti dall'artefatto)
        for ref in art.references:
            resolved = resolve_legacy(ref, cited_from=root / art.path)
            if resolved is None:
                findings.append(Finding(
                    severity="block",
                    rule="LINK-DEAD",
                    path=art.path,
                    message=f"riferimento inesistente o irrisolvibile: `{ref}`",
                    target=ref,
                    fix="correggi il link o crea l'artefatto mancante"
                ))

    return sorted(findings, key=lambda f: (f.rank, str(f.path)))
