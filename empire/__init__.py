"""
EMPIRE — core runtime di Digital Empire.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
Governo: company/Mandato/MANDATO-EMPIRE.md + ADR-003 + ADR-008

Il livello eseguibile dell'azienda: rende gli artefatti descritti in Markdown
interrogabili, validabili e misurabili da codice.

    from empire import repo_root, resolve, resolve_legacy
    from empire.conform import check_art8, check_links

CLI:  python -m empire status
"""
from __future__ import annotations

from .paths import (  # noqa: F401
    EmpireRootNotFound, UnknownAlias, repo_root, resolve, resolve_legacy,
    iter_files, rel, safe_stdout, info,
)
from .config import MissingSecret, get_secret, has_secret, data_dir  # noqa: F401
from .schema import (  # noqa: F401
    Provenance, Agent, Department, Ecosystem, Workflow, Skill, Artifact, Finding,
)

__version__ = "0.1.0"
__all__ = [
    "__version__",
    "EmpireRootNotFound", "UnknownAlias", "MissingSecret",
    "repo_root", "resolve", "resolve_legacy", "iter_files", "rel", "safe_stdout", "info",
    "get_secret", "has_secret", "data_dir",
    "Provenance", "Agent", "Department", "Ecosystem", "Workflow", "Skill", "Artifact", "Finding",
]
