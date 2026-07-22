"""
empire.registry.links — controllo e riparazione facoltativa dei riferimenti nei .md.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-003 + ADR-008
"""
from __future__ import annotations

import difflib
import os
import re
from pathlib import Path
from typing import Sequence

from empire.conform import is_vendored
from empire.paths import repo_root, resolve_legacy
from empire.schema import Artifact, Finding

__all__ = ["check_links_extended", "apply_links_fix"]


def check_links_extended(artifacts: Sequence[Artifact], workflow_filter: str | None = None, root: Path | None = None, include_vendored: bool = False) -> list[Finding]:
    """Verifica approfondita dei link estraendo lo stato: OK, ambiguous, fixable o dead-end."""
    if root is None:
        root = repo_root()

    findings: list[Finding] = []

    for art in artifacts:
        if not include_vendored and is_vendored(art.path):
            continue
        p_posix = art.path.as_posix() if isinstance(art.path, Path) else str(art.path)
        if workflow_filter and not p_posix.startswith(workflow_filter):
            continue
        if art.kind not in ("doc", "workflow", "agent", "department", "ecosystem", "skill", "template", "dashboard"):
            continue

        abs_file = root / art.path
        if not abs_file.is_file():
            continue

        try:
            content = abs_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        # Estrai target con linea e testo intero per contesto
        for line_idx, line in enumerate(content.splitlines(), 1):
            # Cerca link markdown, obsidian o path tra backtick in questa linea
            matches = list(re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", line)) + list(re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", line)) + list(re.finditer(r"`([a-zA-Z0-9_\-\.\/]+(?:/[a-zA-Z0-9_\-\.\/]+)+)`", line))
            for match in matches:
                target = match.group(match.lastindex or 1).strip().split("#")[0].split("?")[0]
                if not target or target.startswith(("http://", "https://", "mailto:", "file://")):
                    continue

                # 1. Esiste relativo al file che lo cita?
                rel_to_file = (abs_file.parent / target).resolve()
                if rel_to_file.exists():
                    continue  # OK

                # 2. Esiste relativo alla radice?
                rel_to_root = (root / target.lstrip("./")).resolve()
                if rel_to_root.exists():
                    # Esiste dalla root ma scritto senza path corretto rispetto a file: ambiguous/info
                    cand_rel = rel_to_root.relative_to(root).as_posix()
                    findings.append(Finding(
                        severity="info",
                        rule="LINK-AMBIGUOUS",
                        path=art.path,
                        line=line_idx,
                        message=f"riferimento dalla root o ambiguo: `{target}`",
                        target=target,
                        fix=f"path radice esatto: {cand_rel}"
                    ))
                    continue

                # 3. Risolve via resolve_legacy?
                legacy_res = resolve_legacy(target, cited_from=abs_file)
                if legacy_res and legacy_res.exists():
                    try:
                        fix_path = legacy_res.relative_to(root).as_posix()
                    except ValueError:
                        fix_path = legacy_res.as_posix()
                    findings.append(Finding(
                        severity="info",
                        rule="LINK-FIXABLE",
                        path=art.path,
                        line=line_idx,
                        message=f"riferimento rotto ma riparabile: `{target}`",
                        target=target,
                        fix=f"path reale: {fix_path}"
                    ))
                    continue

                # 4. Dead-end
                findings.append(Finding(
                    severity="block",
                    rule="LINK-DEAD",
                    path=art.path,
                    line=line_idx,
                    message=f"riferimento inesistente: `{target}`",
                    target=target,
                    fix="correggi il riferimento o crea l'artefatto mancante"
                ))

    return sorted(findings, key=lambda f: (f.rank, str(f.path), f.line or 0))


def apply_links_fix(artifacts: Sequence[Artifact], workflow_filter: str | None = None, root: Path | None = None, dry_run: bool = True, include_vendored: bool = False) -> tuple[int, str]:
    """Applica o simula in dry_run le riparazioni ai file con rule LINK-FIXABLE."""
    if root is None:
        root = repo_root()

    findings = check_links_extended(artifacts, workflow_filter=workflow_filter, root=root, include_vendored=include_vendored)
    fixables = [f for f in findings if f.rule == "LINK-FIXABLE" and f.target and f.fix.startswith("path reale: ")]

    diffs: list[str] = []
    fixed_files_count = 0

    # Raggruppa per file
    by_file: dict[Path, list[Finding]] = {}
    for f in fixables:
        by_file.setdefault(f.path, []).append(f)

    for rel_path, file_findings in by_file.items():
        abs_path = root / rel_path
        if not abs_path.is_file():
            continue
        try:
            old_lines = abs_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        except Exception:
            continue

        new_lines = list(old_lines)
        for f in file_findings:
            if not f.line or f.line > len(new_lines) or not f.target:
                continue
            real_target = f.fix.replace("path reale: ", "").strip()
            # Calcola path relativo corretto rispetto a abs_path.parent se possibile
            try:
                real_abs = root / real_target
                new_rel = os.path.relpath(real_abs, abs_path.parent).replace("\\", "/")
            except Exception:
                new_rel = real_target

            line_idx = f.line - 1
            # Sostituisci il link nella riga
            line_str = new_lines[line_idx]
            # Sostituzione mirata al target tra parentesi, quadri o backtick
            if f"({f.target})" in line_str:
                new_lines[line_idx] = line_str.replace(f"({f.target})", f"({new_rel})")
            elif f"[[{f.target}]]" in line_str:
                new_lines[line_idx] = line_str.replace(f"[[{f.target}]]", f"[[{new_rel}]]")
            elif f"`{f.target}`" in line_str:
                new_lines[line_idx] = line_str.replace(f"`{f.target}`", f"`{new_rel}`")

        if new_lines != old_lines:
            fixed_files_count += 1
            diff = "".join(difflib.unified_diff(
                old_lines, new_lines,
                fromfile=f"a/{rel_path.as_posix()}",
                tofile=f"b/{rel_path.as_posix()}"
            ))
            diffs.append(diff)
            if not dry_run:
                abs_path.write_text("".join(new_lines), encoding="utf-8")

    return fixed_files_count, "\n".join(diffs)
