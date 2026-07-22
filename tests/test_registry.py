"""
tests/test_registry.py — suite di test di unità per empire.registry (GEM-04).

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import json
import time
from pathlib import Path
import pytest

from empire.schema import Artifact, Provenance
from empire.registry import census, orphans, links, dupes, render, gate


def test_provenance_extraction():
    """Verifica estrazione corretta da frontmatter YAML e da docstring Python."""
    yaml_content = """---
Owner: Max
Controllore: Claude
Origine: FORGE
Governo: ADR-008
---
# Titolo
"""
    p1 = census._extract_provenance(yaml_content, "doc.md")
    assert p1.owner == "Max"
    assert p1.controller == "Claude"
    assert p1.origin == "FORGE"
    assert p1.governance == "ADR-008"
    assert p1.complete is True

    py_content = '"""\nmodulo di test.\n\nOwner: Max · Controllore: Claude · Origine: FORGE\nGoverno: MANDATO Art.8\n"""\n'
    p2 = census._extract_provenance(py_content, "script.py")
    assert p2.owner == "Max"
    assert p2.controller == "Claude"
    assert p2.origin == "FORGE"
    assert p2.governance == "MANDATO Art.8"
    assert p2.complete is True


def test_census_excludes(tmp_path: Path):
    """Verifica che census ignori .git, node_modules e altre directory escluse."""
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text("git config", encoding="utf-8")
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "pkg.js").write_text("js", encoding="utf-8")
    (tmp_path / "valid.md").write_text("---\nOwner: Max\nControllore: Claude\nOrigine: FORGE\nGoverno: ADR-008\n---\n# OK", encoding="utf-8")

    artifacts = census.run_census(root=tmp_path)
    paths = [a.path.as_posix() if isinstance(a.path, Path) else str(a.path) for a in artifacts]
    assert "valid.md" in paths
    assert not any(".git" in p for p in paths)
    assert not any("node_modules" in p for p in paths)


def test_orphans_cutoff():
    """Verifica la tolleranza temporale: pre-2026-07-19 = warn, post = block per no-provenance."""
    p_pre = Provenance()  # incompleto
    art_pre = Artifact(path=Path("doc_storico.md"), kind="doc", mtime=1700000000.0, prov=p_pre)
    art_post = Artifact(path=Path("doc_nuovo.md"), kind="doc", mtime=1800000000.0, prov=p_pre)

    f_pre = orphans.check_orphans([art_pre])
    f_post = orphans.check_orphans([art_post])

    assert any(f.severity == "warn" and f.rule == "ADR-008" for f in f_pre)
    assert any(f.severity == "block" and f.rule == "ADR-008" for f in f_post)


def test_dupes_wasted():
    """Verifica calcolo dello spreco in byte su gruppi duplicati."""
    art1 = Artifact(path=Path("copy1.md"), kind="doc", size=1000, hash="abcdef", mtime=100.0, referenced_by=["a.md", "b.md"])
    art2 = Artifact(path=Path("copy2.md"), kind="doc", size=1000, hash="abcdef", mtime=200.0, referenced_by=["a.md"])
    art3 = Artifact(path=Path("copy3.md"), kind="doc", size=1000, hash="abcdef", mtime=300.0, referenced_by=[])

    summary = dupes.analyze_duplicates([art1, art2, art3])
    assert summary["total_groups"] == 1
    assert summary["total_wasted_bytes"] == 2000  # 1000 * (3 - 1)
    group = summary["groups"][0]
    assert group["count"] == 3
    assert group["canonical_candidate"] == "copy1.md"  # quello con più citazioni
    assert group["most_recent"] == "copy3.md"


def test_render_preserves_manual(tmp_path: Path):
    """Verifica che render_registro sostituisca solo il contenuto nei marcatori BEGIN/END e non tocchi il manuale."""
    company_dir = tmp_path / "company"
    company_dir.mkdir()
    reg_file = company_dir / "REGISTRO-IMPRESA.md"
    manual_text = """# REGISTRO IMPRESA — PARTE MANUALE
## 1. ORGANI
Testo manuale che non deve cambiare mai.

<!-- EMPIRE-CENSUS:BEGIN (rigenerato, non modificare a mano) -->
vecchia tabella
<!-- EMPIRE-CENSUS:END -->

## Regola di chiusura (da ADR-008)
Testo finale intatto.
"""
    reg_file.write_text(manual_text, encoding="utf-8")

    art = Artifact(path=Path("DIGITAL-EMPIRE/04-AGENTS/test.md"), kind="agent", prov=Provenance(owner="Max", controller="Claude", origin="FORGE", governance="ADR-008"))
    render.render_registro([art], root=tmp_path)

    updated = reg_file.read_text(encoding="utf-8")
    assert "# REGISTRO IMPRESA — PARTE MANUALE" in updated
    assert "Testo manuale che non deve cambiare mai." in updated
    assert "## Regola di chiusura (da ADR-008)" in updated
    assert "vecchia tabella" not in updated
    assert "DIGITAL-EMPIRE/04-AGENTS/test.md" in updated


def test_gate_blocks_new_orphan(tmp_path: Path):
    """Verifica che gate.py blocchi un file markdown nuovo privo di intestazione ADR-008."""
    new_doc = tmp_path / "nuovo.md"
    new_doc.write_text("# Senza frontmatter", encoding="utf-8")

    findings = gate.run_gate(files=["nuovo.md"], root=tmp_path)
    assert any(f.severity == "block" and f.rule == "GATE-ADR008" for f in findings)
