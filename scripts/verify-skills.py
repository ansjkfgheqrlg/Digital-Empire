#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""verify-skills.py — gate di ufficializzazione delle skill di Digital Empire.

Una skill e' UFFICIALE quando:
  1. esiste .claude/skills/<slug>/SKILL.md
  2. il frontmatter YAML e' parsabile (niente BOM, niente ": " non quotato)
  3. name == nome della cartella
  4. description dice COSA fa e QUANDO si attiva (>= 60 caratteri)
  5. e' registrata in company/skills-map.yaml -> ufficializzazione_skill.skill

Uso:
    python scripts/verify-skills.py --check      # exit 1 se anche una sola fallisce
    python scripts/verify-skills.py              # stessa cosa, output esteso

Console Windows in cp1252: nessuna emoji nell'output (regola APEX-7).
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
SKILLS_DIR = os.path.join(ROOT, ".claude", "skills")
MAP_FILE = os.path.join(ROOT, "company", "skills-map.yaml")
MIN_DESC = 60


def read_frontmatter(path):
    """Ritorna (dict, errore). dict None se il frontmatter non e' utilizzabile."""
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
    if not os.path.exists(MAP_FILE):
        return None
    try:
        data = yaml.safe_load(open(MAP_FILE, encoding="utf-8"))
    except Exception:
        return None
    block = (data or {}).get("ufficializzazione_skill") or {}
    return set(e.get("id") for e in (block.get("skill") or []) if isinstance(e, dict))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="modalita' gate, output compatto")
    args = ap.parse_args()

    if not os.path.isdir(SKILLS_DIR):
        print("ERRORE: %s non esiste" % SKILLS_DIR)
        return 2

    registry = registered_slugs()
    failures = []
    checks = 0
    slugs = sorted(d for d in os.listdir(SKILLS_DIR)
                   if os.path.isdir(os.path.join(SKILLS_DIR, d)))

    for slug in slugs:
        path = os.path.join(SKILLS_DIR, slug, "SKILL.md")
        checks += 1
        if not os.path.exists(path):
            failures.append((slug, "manca SKILL.md"))
            continue

        data, err = read_frontmatter(path)
        checks += 1
        if err:
            failures.append((slug, err))
            continue

        checks += 1
        name = str(data.get("name") or "").strip()
        if name != slug:
            failures.append((slug, "name '%s' != cartella '%s'" % (name, slug)))

        checks += 1
        desc = " ".join(str(data.get("description") or "").split())
        if not desc:
            failures.append((slug, "description vuota"))
        elif len(desc) < MIN_DESC:
            failures.append((slug, "description troppo corta (%d < %d caratteri)" % (len(desc), MIN_DESC)))

        if registry is not None:
            checks += 1
            if slug not in registry:
                failures.append((slug, "non registrata in company/skills-map.yaml"))

    if registry is not None:
        orfane = sorted(registry - set(slugs))
        for slug in orfane:
            failures.append((slug, "registrata in skills-map.yaml ma la cartella non esiste"))

    print("SKILL: %d  CHECK: %d  FALLITI: %d" % (len(slugs), checks, len(failures)))
    if failures:
        for slug, why in failures:
            print("  FAIL  %-42s %s" % (slug, why))
        print("GATE SKILL: FAIL")
        return 1

    print("GATE SKILL: PASS %d/%d" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
