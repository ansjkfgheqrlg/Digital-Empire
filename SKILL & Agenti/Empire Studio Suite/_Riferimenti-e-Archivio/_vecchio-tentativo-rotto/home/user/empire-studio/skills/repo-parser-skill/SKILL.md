---
name: repo-parser-skill
description: 'CLI-only parser for GitHub/local repos and workflow reports in Empire Studio 4th department (projects-repos-workloads). Extracts structure, code, docs, decisions without modifying originals. Feeds deep analyzer + content-forge.'
---
# repo-parser-skill

**Purpose:** Deep CLI parsing of repos/reports for 4th dept. Build file tree, extract functions, headers, "perché" comments, architecture signals. Read-only.

**Scripts:** scripts/parse_repo.py (find, cat targeted, python ast for py files, md header parser, grep for decision keywords)

**Templates:** repo-structure-template.json , atom-extract-template.md

**Principles:** Trace every extraction to exact file:lines. "studiarlo nei minimi dettagli" via exhaustive but prioritized parse.

**Rules:** Never write to source. Output to /tmp/ or memory/projects-state/. Support large repos with sampling + prioritization (README first).

**Integration:** Used by workflow-deep-analyzer-agent, repo-deep-study-agent, workflow-report-parser-skill. Then to project-knowledge-extractor.

**Version:** v1.0 Empire Studio

**Trace:** "quarto reparto... studiarlo... non lo devi modificare... CLI"
