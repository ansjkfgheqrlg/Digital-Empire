"""
empire.registry.census — scansione totale e inventario del monorepo.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from empire.paths import resolve, repo_root, safe_stdout, info
from empire.schema import Artifact, Provenance

__all__ = ["run_census", "load_census", "save_census"]

EXCL_DIRS = {
    ".git", "node_modules", ".next", "__pycache__", ".cache", ".venv", "venv",
    "env", ".pytest_cache", "packaged-final", "phase7-run", "phase9-regression"
}

# 7 file attesi per lo standard CF-grade (content-forge2.0)
CF_GRADE_FILES = {
    "system-prompt.md", "tools.md", "memory.md", "evals.md", "playbook.md", "failure-modes.md"
}


def _get_git_history(root: Path) -> dict[str, tuple[str, str]]:
    """Restituisce mappa {rel_path_posix: (author, date)} con un solo comando git log."""
    cache: dict[str, tuple[str, str]] = {}
    try:
        proc = subprocess.run(
            ["git", "log", "--name-only", "--format=COMMIT:%an|%aI"],
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False
        )
        if proc.returncode == 0:
            author, date = None, None
            for line in proc.stdout.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("COMMIT:"):
                    parts = line[7:].split("|", 1)
                    author = parts[0] if len(parts) > 0 else "Unknown"
                    date = parts[1] if len(parts) > 1 else ""
                elif author and date:
                    if line not in cache:
                        cache[line] = (author, date)
    except Exception:
        pass
    return cache


def _extract_provenance(content: str, rel_path: str) -> Provenance:
    """Estrae i 4 campi ADR-008 da frontmatter YAML o da commenti/docstring Python/PowerShell."""
    owner, controller, origin, governance = None, None, None, None
    lines = content.splitlines()[:40]
    header_text = "\n".join(lines)

    # Cerca nel frontmatter YAML o nel testo di testata
    for line in lines:
        l_clean = line.strip().lstrip("#/>* -").strip()
        l_lower = l_clean.lower()
        if l_lower.startswith(("owner:", "proprietario:")):
            owner = l_clean.split(":", 1)[1].strip().split("·")[0].split("|")[0].strip()
        if l_lower.startswith(("controllore:", "controller:", "qa:")):
            controller = l_clean.split(":", 1)[1].strip().split("·")[0].split("|")[0].strip()
        if l_lower.startswith(("origine:", "origin:")):
            origin = l_clean.split(":", 1)[1].strip().split("·")[0].split("|")[0].strip()
        if l_lower.startswith(("governo:", "governance:", "mandato:")):
            governance = l_clean.split(":", 1)[1].strip().split("·")[0].split("|")[0].strip()

    # Cerca in righe multiple separate da · (es. docstring python: Owner: Max · Controllore: Claude ...)
    if not (owner and controller and origin and governance):
        for line in lines:
            if "owner:" in line.lower() or "controllore:" in line.lower() or "origine:" in line.lower():
                parts = re.split(r"[·|;]", line)
                for part in parts:
                    p_clean = part.strip().lstrip("#/>* -").strip()
                    p_lower = p_clean.lower()
                    if p_lower.startswith(("owner:", "proprietario:")) and not owner:
                        owner = p_clean.split(":", 1)[1].strip()
                    elif p_lower.startswith(("controllore:", "controller:", "qa:")) and not controller:
                        controller = p_clean.split(":", 1)[1].strip()
                    elif p_lower.startswith(("origine:", "origin:")) and not origin:
                        origin = p_clean.split(":", 1)[1].strip()
                    elif p_lower.startswith(("governo:", "governance:", "mandato:")) and not governance:
                        governance = p_clean.split(":", 1)[1].strip()

    # Cerca nella classica riga > **Legge:** del Registro o simili
    if not governance and "mandato" in header_text.lower():
        governance = "MANDATO-EMPIRE.md"
    if not governance and "adr-008" in header_text.lower():
        governance = "ADR-008"

    return Provenance(
        owner=owner,
        controller=controller,
        origin=origin,
        governance=governance,
        source_file=Path(rel_path) if any((owner, controller, origin, governance)) else None
    )


def _extract_references(content: str) -> list[str]:
    """Estrae riferimenti (link markdown o path citati)."""
    refs = set()
    # Link Markdown standard [label](url)
    for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", content):
        target = match.group(2).strip().split("#")[0].split("?")[0]
        if target and not target.startswith(("http://", "https://", "mailto:", "file://")):
            refs.add(target)
    # Link Obsidian [[target]]
    for match in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content):
        target = match.group(1).strip()
        if target:
            refs.add(target)
    # Path tra backtick (es. `04-AGENTS/PERFORMANCE-CELL.md` o `00-MEMORY/performances/`)
    for match in re.finditer(r"`([a-zA-Z0-9_\-\.\/]+(?:/[a-zA-Z0-9_\-\.\/]+)+)`", content):
        target = match.group(1).strip()
        if target and not target.startswith(("http://", "https://", "mailto:", "file://")):
            refs.add(target)
    return sorted(refs)


def _determine_kind(rel_path: str, is_dir: bool = False) -> str:
    p = rel_path.replace("\\", "/")
    p_lower = p.lower()

    if "ruflo/" in p_lower or ".agents/skills/" in p_lower or ".claude/" in p_lower or "node_modules/" in p_lower:
        return "vendored"
    if p_lower.endswith("/ecosistema.md") or p_lower.endswith("/ecosystem.md") or p_lower.startswith("company/ecosistemi/"):
        if p_lower.endswith(".md") and ("ecosistema" in p_lower or "dossier" in p_lower):
            return "ecosystem"
    if "-department.md" in p_lower or "dipartimento" in p_lower or "/board-csuite/" in p_lower:
        if p_lower.endswith(".md"):
            return "department"
    if "/05-templates-e-kit/" in p_lower or "-template." in p_lower or "/templates/" in p_lower:
        return "template"
    if "/06-dashboard-e-metriche/" in p_lower or p_lower.startswith("dashboard") or "/dashboard" in p_lower or p.split("/")[-1].startswith("LISTA-"):
        if p_lower.endswith((".md", ".html", ".csv", ".json")):
            return "dashboard"
    if "/05-skills/" in p_lower or "/skills/" in p_lower or p_lower.endswith("skill.md"):
        if p_lower.endswith((".md", ".yaml", ".yml", ".py", ".sh")):
            return "skill"
    if "/01-flussi-e-piani/" in p_lower or "/03-workflows/" in p_lower or p.split("/")[-1].startswith("WF-") or p.split("/")[-1].startswith("PLANNING-") or p_lower.endswith("workflows.yaml"):
        return "workflow"
    if p_lower.endswith((".py", ".ps1", ".sh", ".bat", ".cmd", ".js", ".ts")):
        return "script"
    if p_lower.endswith((".md", ".yaml", ".yml", ".txt", ".json", ".toml")):
        if "/04-agents/" in p_lower or "/agenti/" in p_lower or p.split("/")[-1].startswith("AGENTE-") or p.split("/")[-1].startswith("agent-"):
            return "agent"
        return "doc"
    return "asset"


def run_census(root: Path | None = None) -> list[Artifact]:
    """Esegue la scansione totale del monorepo e costruisce l'inventario Artifact."""
    if root is None:
        root = repo_root()

    t0 = time.time()
    git_cache = _get_git_history(root)
    artifacts: list[Artifact] = []
    path_map: dict[str, Artifact] = {}

    for dirpath, dirnames, filenames in os.walk(root):
        # Pota le directory escluse in-place per non entrarci nemmeno
        dirnames[:] = [d for d in dirnames if d not in EXCL_DIRS and not d.startswith(".git")]
        cur_dir = Path(dirpath)

        for fname in filenames:
            if fname.startswith(".git") or fname == "census.json":
                continue
            path = cur_dir / fname
            rel_posix = path.relative_to(root).as_posix()
            kind = _determine_kind(rel_posix)

        try:
            stat = path.stat()
            size = stat.st_size
            mtime = stat.st_mtime
        except Exception:
            size, mtime = 0, 0.0

        author, date_str = git_cache.get(rel_posix, (None, None))

        prov = Provenance()
        refs: list[str] = []
        file_hash = ""
        cf_grade = False

        if kind in ("doc", "agent", "department", "ecosystem", "workflow", "skill", "script", "template", "dashboard", "vendored"):
            try:
                raw_bytes = path.read_bytes()
                file_hash = hashlib.sha256(raw_bytes).hexdigest()[:16]
                if size < 5_000_000:
                    content = raw_bytes.decode("utf-8", errors="replace")
                    prov = _extract_provenance(content, rel_posix)
                    if kind in ("doc", "agent", "department", "ecosystem", "workflow", "skill", "template", "dashboard"):
                        refs = _extract_references(content)
            except Exception:
                pass

        # Verifica cf_grade per agenti
        if kind == "agent":
            parent = path.parent
            if parent.is_dir():
                parent_files = {p.name.lower() for p in parent.glob("*") if p.is_file()}
                if len(CF_GRADE_FILES.intersection(parent_files)) >= 4 or "system-prompt.md" in parent_files:
                    cf_grade = True

        art = Artifact(
            path=Path(rel_posix),
            kind=kind,
            size=size,
            hash=file_hash,
            mtime=mtime,
            git_author=author,
            git_date=date_str,
            references=refs,
            prov=prov
        )
        if hasattr(art, "cf_grade"):
            setattr(art, "cf_grade", cf_grade)

        artifacts.append(art)
        path_map[rel_posix] = art

    # Calcola referenced_by interconnesso
    for rel_posix, art in path_map.items():
        for r in art.references:
            # Risolvi target di massima rispetto ad art.path o root
            target_cand = (Path(rel_posix).parent / r).as_posix().replace("..//", "").lstrip("./")
            # Prova esatto o basename matching
            matched = path_map.get(target_cand) or path_map.get(r.lstrip("/"))
            if not matched:
                # Prova tra tutti se c'è un match con basename.md
                for k_p, target_art in path_map.items():
                    if k_p.endswith("/" + r) or k_p == r or (r.endswith(".md") and k_p.endswith(r)):
                        matched = target_art
                        break
            if matched and rel_posix not in matched.referenced_by:
                matched.referenced_by.append(rel_posix)

    return artifacts


def save_census(artifacts: list[Artifact], out_path: Path | None = None) -> Path:
    if out_path is None:
        out_path = repo_root() / "empire" / ".data" / "census.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = [a.to_dict() for a in artifacts]
    out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path


def load_census(in_path: Path | None = None) -> list[Artifact]:
    if in_path is None:
        in_path = repo_root() / "empire" / ".data" / "census.json"
    if not in_path.exists():
        return run_census()
    raw = json.loads(in_path.read_text(encoding="utf-8"))
    out: list[Artifact] = []
    for item in raw:
        prov_dict = item.get("prov", {})
        prov = Provenance(
            owner=prov_dict.get("owner"),
            controller=prov_dict.get("controller"),
            origin=prov_dict.get("origin"),
            governance=prov_dict.get("governance"),
            source_file=Path(prov_dict["source_file"]) if prov_dict.get("source_file") else None
        )
        art = Artifact(
            path=Path(item["path"]),
            kind=item.get("kind", "doc"),
            size=item.get("size", 0),
            hash=item.get("hash", ""),
            mtime=item.get("mtime", 0.0),
            git_author=item.get("git_author"),
            git_date=item.get("git_date"),
            references=item.get("references", []),
            referenced_by=item.get("referenced_by", []),
            prov=prov
        )
        out.append(art)
    return out


def main() -> int:
    safe_stdout()
    t0 = time.time()
    artifacts = run_census()
    t1 = time.time()
    out = save_census(artifacts)
    counts = {}
    for a in artifacts:
        counts[a.kind] = counts.get(a.kind, 0) + 1
    print(f"Censimento completato in {t1 - t0:.2f} s -> {len(artifacts)} artefatti salvati in {out.as_posix()}")
    for k, v in sorted(counts.items()):
        print(f"  {k:12}: {v:5}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
