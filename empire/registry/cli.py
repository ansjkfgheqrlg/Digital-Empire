"""
empire.registry.cli — interfaccia a riga di comando dei sottocomandi di anagrafe.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from empire.paths import safe_stdout
from empire.registry import census, orphans, links, dupes, render, gate

__all__ = ["register"]

EXIT_OK, EXIT_BLOCK, EXIT_ERR = 0, 1, 2


def _print_findings(findings, as_json: bool) -> int:
    if as_json:
        print(json.dumps([f.to_dict() for f in findings], indent=2, ensure_ascii=False))
    else:
        blocks = [f for f in findings if f.severity == "block"]
        warns = [f for f in findings if f.severity == "warn"]
        infos = [f for f in findings if f.severity == "info"]
        for f in findings:
            print(f)
            if f.fix:
                print(f"        -> {f.fix}")
        print()
        print(f"  block: {len(blocks)}   warn: {len(warns)}   info/fixable: {len(infos)}"
              f"   totale: {len(findings)}")
    return EXIT_BLOCK if any(f.severity == "block" for f in findings) else EXIT_OK


def _cmd_census(a) -> int:
    safe_stdout()
    artifacts = census.run_census()
    out = census.save_census(artifacts)
    if a.json:
        print(json.dumps({"count": len(artifacts), "path": out.as_posix()}, indent=2, ensure_ascii=False))
    else:
        counts: dict[str, int] = {}
        for art in artifacts:
            counts[art.kind] = counts.get(art.kind, 0) + 1
        print(f"Censimento completato -> {len(artifacts)} artefatti salvati in {out.as_posix()}")
        for k, v in sorted(counts.items()):
            print(f"  {k:12}: {v:5}")
    return EXIT_OK


def _cmd_orphans(a) -> int:
    safe_stdout()
    artifacts = census.load_census()
    if a.workflow:
        artifacts = [art for art in artifacts if str(art.path).startswith(a.workflow)]
    findings = orphans.check_orphans(artifacts)
    return _print_findings(findings, a.json)


def _cmd_links(a) -> int:
    safe_stdout()
    artifacts = census.load_census()
    if a.fix:
        count, diffs = links.apply_links_fix(artifacts, workflow_filter=a.workflow, dry_run=a.dry_run, include_vendored=a.include_vendored)
        if a.json:
            print(json.dumps({"fixed_files": count, "dry_run": a.dry_run, "diff": diffs}, indent=2, ensure_ascii=False))
        else:
            print(f"File con link corretti{' (DRY-RUN diff)' if a.dry_run else ''}: {count}")
            if diffs:
                print("\nDIFF:")
                print(diffs)
            if a.dry_run and count > 0:
                print("\n-> Per applicare davvero le correzioni ai file, aggiungi il flag --no-dry-run")
        return EXIT_OK
    else:
        findings = links.check_links_extended(artifacts, workflow_filter=a.workflow, include_vendored=a.include_vendored)
        return _print_findings(findings, a.json)


def _cmd_dupes(a) -> int:
    safe_stdout()
    artifacts = census.load_census()
    summary = dupes.analyze_duplicates(artifacts)
    out_path, rep_text = dupes.save_duplicates_report(summary)
    if a.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(rep_text)
        print(f"\nReport dettagliato salvato in: {out_path.as_posix()}")
    return EXIT_OK


def _cmd_render(a) -> int:
    safe_stdout()
    artifacts = census.load_census()
    p1, p2 = render.render_all(artifacts)
    if a.json:
        print(json.dumps({"registro": p1.as_posix(), "skills_map": p2.as_posix()}, indent=2, ensure_ascii=False))
    else:
        print(f"Rigenerati con successo:\n  -> {p1.as_posix()}\n  -> {p2.as_posix()}")
    return EXIT_OK


def _cmd_gate(a) -> int:
    safe_stdout()
    findings = gate.run_gate(files=a.files, staged_only=a.staged)
    return _print_findings(findings, a.json)


def register(sub: argparse._SubParsersAction) -> None:
    """Registra il sottocomando `registry` su `python -m empire`."""
    p_reg = sub.add_parser("registry", help="anagrafe d'impresa, integrità collegamenti, gate ADR-008")
    sub_reg = p_reg.add_subparsers(dest="reg_cmd", required=True)

    p_c = sub_reg.add_parser("census", help="esegue la scansione e salva census.json")
    p_c.add_argument("--json", action="store_true")
    p_c.set_defaults(fn=_cmd_census)

    p_o = sub_reg.add_parser("orphans", help="rileva i 4 tipi di orfani")
    p_o.add_argument("--workflow", default=None, help="filtra per cartella (es. WORKFLOW-ESTATE)")
    p_o.add_argument("--json", action="store_true")
    p_o.set_defaults(fn=_cmd_orphans)

    p_l = sub_reg.add_parser("links", help="controlla e corregge i link nei .md")
    p_l.add_argument("--workflow", default=None, help="filtra per cartella")
    p_l.add_argument("--fix", action="store_true", help="genera diff e propone/applica fix per i link fixable")
    p_l.add_argument("--dry-run", dest="dry_run", action="store_true", default=True, help="mostra solo il diff senza modificare (default)")
    p_l.add_argument("--no-dry-run", dest="dry_run", action="store_false", help="applica le modifiche ai file su disco")
    p_l.add_argument("--include-vendored", action="store_true", help="include skill vendorizzate e artefatti di run")
    p_l.add_argument("--json", action="store_true")
    p_l.set_defaults(fn=_cmd_links)

    p_d = sub_reg.add_parser("dupes", help="rileva duplicati tra alberi")
    p_d.add_argument("--json", action="store_true")
    p_d.set_defaults(fn=_cmd_dupes)

    p_r = sub_reg.add_parser("render", help="rigenera sezioni censimento in REGISTRO-IMPRESA e skills-map")
    p_r.add_argument("--json", action="store_true")
    p_r.set_defaults(fn=_cmd_render)

    p_g = sub_reg.add_parser("gate", help="gate bloccante di pre-commit (ADR-008)")
    p_g.add_argument("--staged", action="store_true", help="controlla i file in git staging area")
    p_g.add_argument("--files", nargs="*", default=None, help="lista di path da verificare")
    p_g.add_argument("--json", action="store_true")
    p_g.set_defaults(fn=_cmd_gate)
