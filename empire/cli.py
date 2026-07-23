"""
EMPIRE — interfaccia a riga di comando.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
Governo: MANDATO Art.8 + ADR-008

Uso:  python -m empire <comando>

Comandi del seed (funzionanti):
  status                 stato del runtime e della radice
  paths [alias]          alias logici -> path reali, con esistenza verificata
  links <workflow>       riferimenti rotti e riparabili nei .md
  art8 <workflow>        i 6 pilastri del Mandato Art.8
  adr001                 la holding ha esattamente 10 ecosistemi (ADR-001)
  conform <workflow>     art8 + links
  doctor                 tutto; exit 1 se esistono finding 'block'

Comandi in costruzione (GEM-01 lotto Gael): agents, ecosystems, workflows, skills, index, find, show
"""
from __future__ import annotations

import argparse
import json
import sys

from .paths import safe_stdout, info, resolve, config_data
from . import conform as _conform

safe_stdout()

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
        print(f"  block: {len(blocks)}   warn: {len(warns)}   info(riparabili): {len(infos)}"
              f"   totale: {len(findings)}")
    return EXIT_BLOCK if any(f.severity == "block" for f in findings) else EXIT_OK


def cmd_status(a) -> int:
    i = info()
    print("EMPIRE CORE RUNTIME")
    print(f"  versione     {i.version}")
    print(f"  radice       {i.root}")
    print(f"  marker       {i.marker}")
    print(f"  alias        {i.aliases}")
    missing = [k for k in config_data()["alias"] if not resolve(k).exists()]
    print(f"  alias rotti  {len(missing)}" + (f"  -> {', '.join(missing)}" if missing else ""))
    print()
    print("  moduli seed  paths, config, schema, conform, cli")
    print("  in corso     loader, index (Gael) · memory, inspect (Claude) · flow (Gael)")
    return EXIT_OK


def cmd_paths(a) -> int:
    aliases = config_data()["alias"]
    keys = [a.alias] if a.alias else sorted(aliases)
    rows = []
    for k in keys:
        if k not in aliases:
            print(f"alias sconosciuto: {k}", file=sys.stderr)
            return EXIT_ERR
        p = resolve(k)
        rows.append((k, "OK " if p.exists() else "MANCA", aliases[k]))
    if a.json:
        print(json.dumps({k: {"path": v, "exists": s == "OK "} for k, s, v in rows},
                         indent=2, ensure_ascii=False))
        return EXIT_OK
    w = max(len(k) for k, _, _ in rows)
    for k, s, v in rows:
        print(f"  {s} {k.ljust(w)}  {v}")
    return EXIT_OK


def cmd_links(a) -> int:
    return _print_findings(_conform.check_links(a.workflow), a.json)


def cmd_art8(a) -> int:
    return _print_findings(_conform.check_art8(a.workflow), a.json)


def cmd_adr001(a) -> int:
    return _print_findings(sorted(_conform.check_adr001(), key=lambda f: f.rank), a.json)


def cmd_conform(a) -> int:
    f = _conform.check_art8(a.workflow) + _conform.check_links(a.workflow)
    f.sort(key=lambda x: (x.rank, str(x.path)))
    return _print_findings(f, a.json)


def cmd_doctor(a) -> int:
    print("EMPIRE DOCTOR\n")
    findings = _conform.run_all(a.workflow)
    rc = _print_findings(findings, a.json)
    if not a.json:
        print()
        print("  exit 1 = ci sono problemi bloccanti. E' il comportamento atteso"
              " finche' GEM-03/04 non li chiudono.")
    return rc


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="python -m empire",
                                 description="Empire core runtime — Digital Empire")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("status", help="stato del runtime")
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("paths", help="alias logici -> path reali")
    p.add_argument("alias", nargs="?")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_paths)

    p = sub.add_parser("links", help="riferimenti rotti nei .md")
    p.add_argument("workflow", nargs="?", default="WORKFLOW-ESTATE")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_links)

    p = sub.add_parser("art8", help="6 pilastri del Mandato Art.8")
    p.add_argument("workflow", nargs="?", default="WORKFLOW-ESTATE")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_art8)

    p = sub.add_parser("adr001", help="ADR-001: la holding ha esattamente 10 ecosistemi")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_adr001)

    p = sub.add_parser("conform", help="art8 + links")
    p.add_argument("workflow", nargs="?", default="WORKFLOW-ESTATE")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_conform)

    p = sub.add_parser("doctor", help="tutti i controlli, exit 1 se block")
    p.add_argument("--workflow", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_doctor)

    _register_plugins(sub)
    return ap


# Ogni lotto aggiunge i propri sottocomandi nel PROPRIO modulo, esponendo
# register(sub). Cosi' nessuno modifica questo file e non ci sono collisioni
# di merge tra Max, Gael e Gemini.
_PLUGIN_MODULES = (
    "empire.loader_cli",    # Gael  — agents, ecosystems, workflows, skills
    "empire.index_cli",     # Gael  — index, find, show
    "empire.flow.cli",      # Gael  — flow *
    "empire.memory.cli",    # Claude — mem *
    "empire.inspect.cli",   # Claude — inspect *
    "empire.registry.cli",  # Gemini — registry *
    "empire.dash.cli",      # Gemini — dash *
)


def _register_plugins(sub) -> None:
    import importlib
    for name in _PLUGIN_MODULES:
        try:
            mod = importlib.import_module(name)
        except ImportError:
            continue          # lotto non ancora costruito: normale
        reg = getattr(mod, "register", None)
        if callable(reg):
            try:
                reg(sub)
            except Exception as e:  # noqa: BLE001
                print(f"ATTENZIONE: {name}.register() ha fallito: {e}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    a = ap.parse_args(argv)
    try:
        return a.fn(a)
    except Exception as e:  # noqa: BLE001 — la CLI non deve mai mostrare uno stacktrace nudo
        print(f"ERRORE: {type(e).__name__}: {e}", file=sys.stderr)
        return EXIT_ERR


if __name__ == "__main__":
    raise SystemExit(main())
