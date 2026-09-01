#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""verify-agents.py — gate di ufficializzazione degli agenti di Digital Empire.

Gemello di scripts/verify-skills.py. Un agente e' UFFICIALE quando:
  1. esiste <dir>/<slug>.md
  2. il frontmatter YAML e' parsabile (niente BOM, niente ": " non quotato in scalari plain)
  3. name == nome del file
  4. description dice cosa fa e quando si attiva (>= 40 caratteri)
  5. se e' di progetto, e' censito in company/Backbone/Identity-HR/registro-agenti.yaml

Copre due cartelle:
  .claude/agents/          agenti di progetto (prevalgono a parita' di nome)
  ~/.claude/agents/        agenti globali

Uso:
    python scripts/verify-agents.py --check     # exit 1 se anche uno solo fallisce
    python scripts/verify-agents.py --solo-progetto

Console Windows in cp1252: nessuna emoji nell'output.
"""
import argparse
import os
import sys

try:
    import yaml
except ImportError:
    print("ERRORE: manca PyYAML (pip install pyyaml)")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.join(ROOT, ".claude", "agents")
GLOB_DIR = os.path.join(os.path.expanduser("~"), ".claude", "agents")
REG_FILE = os.path.join(ROOT, "company", "Backbone", "Identity-HR", "registro-agenti.yaml")
MIN_DESC = 40


def read_frontmatter(path):
    raw = open(path, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        return None, "BOM UTF-8 in testa al file (il frontmatter non viene letto)"
    text = raw.decode("utf-8", "replace").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None, "manca il frontmatter YAML"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "frontmatter non chiuso"
    try:
        data = yaml.safe_load(text[4:end])
    except Exception as exc:
        return None, "YAML non parsabile: %s" % str(exc).split("\n")[0]
    if not isinstance(data, dict):
        return None, "il frontmatter non e' una mappa YAML"
    return data, None


def registered_slugs():
    if not os.path.exists(REG_FILE):
        return None
    try:
        data = yaml.safe_load(open(REG_FILE, encoding="utf-8"))
    except Exception:
        return None
    block = (data or {}).get("agenti_ufficiali") or {}
    return set(e.get("id") for e in (block.get("agenti") or []) if isinstance(e, dict))


def audit(directory, registry):
    """Ritorna (numero agenti, numero check, lista fallimenti)."""
    if not os.path.isdir(directory):
        return 0, 0, []
    slugs = sorted(f[:-3] for f in os.listdir(directory) if f.endswith(".md"))
    failures = []
    checks = 0

    for slug in slugs:
        path = os.path.join(directory, slug + ".md")
        checks += 1
        data, err = read_frontmatter(path)
        if err:
            failures.append((slug, err))
            continue

        checks += 1
        name = str(data.get("name") or "").strip()
        if name != slug:
            failures.append((slug, "name '%s' != file '%s'" % (name, slug)))

        checks += 1
        desc = " ".join(str(data.get("description") or "").split())
        if not desc:
            failures.append((slug, "description vuota"))
        elif len(desc) < MIN_DESC:
            failures.append((slug, "description troppo corta (%d < %d caratteri)" % (len(desc), MIN_DESC)))

        if registry is not None:
            checks += 1
            if slug not in registry:
                failures.append((slug, "non censito in registro-agenti.yaml"))

    return len(slugs), checks, failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="modalita' gate")
    ap.add_argument("--solo-progetto", action="store_true", help="ignora ~/.claude/agents/")
    args = ap.parse_args()

    registry = registered_slugs()
    total = 0
    total_checks = 0
    all_fail = []

    n, c, f = audit(PROJ_DIR, registry)
    print("PROGETTO  .claude/agents/        %3d agenti" % n)
    total += n
    total_checks += c
    all_fail += [("progetto", s, w) for s, w in f]

    if not args.solo_progetto:
        # gli agenti globali non devono stare nel registro del monorepo
        n, c, f = audit(GLOB_DIR, None)
        print("GLOBALE   ~/.claude/agents/      %3d agenti" % n)
        total += n
        total_checks += c
        all_fail += [("globale", s, w) for s, w in f]

    if registry is not None:
        proj_slugs = set(f[:-3] for f in os.listdir(PROJ_DIR) if f.endswith(".md")) \
            if os.path.isdir(PROJ_DIR) else set()
        for slug in sorted(registry - proj_slugs):
            all_fail.append(("registro", slug, "censito nel registro ma il file non esiste"))

    print("AGENTI: %d  CHECK: %d  FALLITI: %d" % (total, total_checks, len(all_fail)))
    if all_fail:
        for scope, slug, why in all_fail:
            print("  FAIL  [%-9s] %-38s %s" % (scope, slug, why))
        print("GATE AGENTI: FAIL")
        return 1

    print("GATE AGENTI: PASS %d/%d" % (total_checks, total_checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
