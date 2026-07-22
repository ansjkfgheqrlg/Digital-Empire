"""
empire.registry.gate — gate pre-commit/CI per prevenire nuovi orfani o link rotti (ADR-008).

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Sequence

from empire.paths import repo_root, resolve_legacy, safe_stdout
from empire.registry.census import _extract_provenance, _extract_references
from empire.schema import Finding

__all__ = ["run_gate"]


def _get_staged_files(root: Path) -> list[str]:
    """Restituisce i file pronti per il commit (`git diff --cached --name-only --diff-filter=ACM`)."""
    try:
        proc = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False
        )
        if proc.returncode == 0:
            return [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    except Exception:
        pass
    return []


def run_gate(files: Sequence[str] | None = None, staged_only: bool = False, root: Path | None = None) -> list[Finding]:
    """Esegue controlli bloccanti su un set di file (o sullo staging git)."""
    if root is None:
        root = repo_root()

    if staged_only and files is None:
        files = _get_staged_files(root)
    elif files is None:
        files = []

    findings: list[Finding] = []

    for rel_str in files:
        rel_posix = rel_str.replace("\\", "/")
        path = root / rel_posix
        if not path.is_file():
            continue

        # Controlla solo file markdown o di codice rilevante per la governance
        if not rel_posix.endswith((".md", ".yaml", ".yml", ".py", ".sh", ".ps1")):
            continue
        # Escludi indici, fixture e vendored pure
        name_lower = path.name.lower()
        if name_lower in ("readme.md", "index.md", "changelog.md", "license", "registro-impresa.md", "skills-map.yaml"):
            continue
        if "/tests/" in rel_posix.lower() or "/fixtures/" in rel_posix.lower() or "ruflo/" in rel_posix.lower() or ".agents/skills/" in rel_posix.lower():
            continue

        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        # 1. Verifica Provenance (ADR-008) bloccante su file nuovi o modificati
        prov = _extract_provenance(content, rel_posix)
        missing = prov.missing
        if missing:
            findings.append(Finding(
                severity="block",
                rule="GATE-ADR008",
                path=Path(rel_posix),
                message=f"[PRE-COMMIT BLOCK] file modificato/nuovo privo di intestazione ADR-008 completa (mancano: {', '.join(missing)})",
                fix="Aggiungi in testa: Owner, Controllore, Origine, Governo"
            ))

        # 2. Verifica link (solo per i .md)
        if rel_posix.endswith(".md"):
            refs = _extract_references(content)
            for r in refs:
                resolved = resolve_legacy(r, cited_from=path)
                if resolved is None:
                    findings.append(Finding(
                        severity="block",
                        rule="GATE-LINK-DEAD",
                        path=Path(rel_posix),
                        message=f"[PRE-COMMIT BLOCK] nuovo link rotto/inesistente e irrisolvibile: `{r}`",
                        target=r,
                        fix="Correggi il link o aggiungi il file prima di fare commit"
                    ))

    return sorted(findings, key=lambda f: (f.rank, str(f.path)))
