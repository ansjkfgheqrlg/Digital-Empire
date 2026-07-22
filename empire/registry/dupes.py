"""
empire.registry.dupes — rilevamento e quantificazione dei duplicati tra alberi (in particolare DIGITAL-EMPIRE vs WORKFLOW-ESTATE).

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence

from empire.paths import repo_root
from empire.schema import Artifact

__all__ = ["analyze_duplicates", "save_duplicates_report"]


def analyze_duplicates(artifacts: Sequence[Artifact], root: Path | None = None) -> dict[str, Any]:
    """Confronta gli artefatti per hash e calcola spreco in MB, copie più recenti e canoniche candidate."""
    if root is None:
        root = repo_root()

    by_hash: dict[str, list[Artifact]] = {}
    for art in artifacts:
        if art.hash and art.size > 100 and art.kind != "vendored":  # Escludi file minuscoli/vuoti e vendored pure
            by_hash.setdefault(art.hash, []).append(art)

    dupe_groups: list[dict[str, Any]] = []
    total_wasted_bytes = 0
    cf_group: dict[str, Any] | None = None

    for h, group in by_hash.items():
        if len(group) < 2:
            continue

        # Ordina per numero di citazioni (referenced_by) descrescente, poi per mtime più recente
        sorted_group = sorted(group, key=lambda a: (len(a.referenced_by), a.mtime), reverse=True)
        canonical_cand = sorted_group[0]
        most_recent = max(group, key=lambda a: a.mtime)

        wasted = canonical_cand.size * (len(group) - 1)
        total_wasted_bytes += wasted

        paths_posix = [a.path.as_posix() if isinstance(a.path, Path) else str(a.path) for a in group]

        group_info = {
            "hash": h,
            "size_bytes": canonical_cand.size,
            "count": len(group),
            "wasted_bytes": wasted,
            "paths": paths_posix,
            "canonical_candidate": canonical_cand.path.as_posix() if isinstance(canonical_cand.path, Path) else str(canonical_cand.path),
            "most_recent": most_recent.path.as_posix() if isinstance(most_recent.path, Path) else str(most_recent.path)
        }
        dupe_groups.append(group_info)

        # Cerca il gruppo o il cluster associato a content-forge2.0
        if any("content-forge" in p.lower() for p in paths_posix):
            if cf_group is None or len(paths_posix) > len(cf_group["paths"]):
                cf_group = group_info

    # Identificazione mirata e sintetica del cluster content-forge se suddiviso su più file individuali
    cf_copies: list[str] = []
    cf_wasted_approx = 0
    for art in artifacts:
        p_posix = art.path.as_posix() if isinstance(art.path, Path) else str(art.path)
        if "content-forge" in p_posix.lower() and art.path.name.lower() == "skill.md":
            cf_copies.append(p_posix)
            cf_wasted_approx += art.size

    dupe_groups.sort(key=lambda g: g["wasted_bytes"], reverse=True)

    summary = {
        "total_groups": len(dupe_groups),
        "total_wasted_bytes": total_wasted_bytes,
        "total_wasted_mb": round(total_wasted_bytes / (1024 * 1024), 2),
        "cf_cluster": {
            "skill_md_copies": cf_copies,
            "count": len(cf_copies),
            "total_bytes": cf_wasted_approx,
            "representative_hash_group": cf_group
        },
        "groups": dupe_groups
    }
    return summary


def save_duplicates_report(summary: dict[str, Any], out_json: Path | None = None) -> tuple[Path, str]:
    if out_json is None:
        out_json = repo_root() / "empire" / ".data" / "duplicates.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Genera report leggibile Markdown
    lines = [
        "# REPORT ANALISI DUPLICATI TRA ALBERI (`dupes.py`)",
        "",
        f"- **Totale Gruppi Identici:** {summary['total_groups']}",
        f"- **Spazio Sprecato Totale:** {summary['total_wasted_mb']} MB ({summary['total_wasted_bytes']} byte)",
        "",
        "## Focus: Cluster `content-forge2.0` (≥ 4 copie percepite/rilevate)",
        f"Copie di `SKILL.md` per content-forge trovate ({summary['cf_cluster']['count']}):"
    ]
    for c in summary["cf_cluster"]["skill_md_copies"]:
        lines.append(f"  - `{c}`")
    lines.append("")
    lines.append("## Top 15 Gruppi per Spazio Sprecato")
    lines.append("| Hash | Dimensione | Copie | Spreco (MB) | Candidata Canonica (più citata) |")
    lines.append("|---|---|---|---|---|")
    for g in summary["groups"][:15]:
        w_mb = round(g["wasted_bytes"] / (1024 * 1024), 2)
        lines.append(f"| `{g['hash']}` | {g['size_bytes']} | {g['count']} | {w_mb} | `{g['canonical_candidate']}` |")

    lines.append("")
    lines.append("> **NOTA:** Nessun file è stato cancellato conformemente all'anti-pattern §7 di GEM-04. La decisione su quale albero mantenere come canonico (`DIGITAL-EMPIRE/` vs `WORKFLOW-ESTATE/`) è riservata a un ADR di Max.")

    report_text = "\n".join(lines)
    return out_json, report_text
