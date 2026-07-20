---
Type: TOOL
Status: Active
Tags: #forge #agenti #skill #mkd #vendor #content-forge
Created: 2026-07-20
Last updated: 2026-07-20
---

# Content-Forge 2.0 (motore di forgia `/forge`)

## Overview
Motore che trasforma contenuti testuali grezzi (transcript YouTube, appunti, brief, cartelle intere) in
artefatti operativi: documenti espansi, agenti, team, skill ufficiali, workflow, orchestrazioni, wiki,
knowledge pack. **Mai riassunti — espande sempre**; produce sempre il **MKD** (Master Knowledge Document)
come base canonica. È il motore del reparto [[Tool_Forge_Agent_Skill_Reparto|FORGE-AGENT-SKILL]].

## Asset
- **Vendor:** `content-forge2.0/` alla root (clone `ansjkfgheqrlg/content-forge2.0`, ADR-009).
  Agenti interni: conductor, pipeline, builders, qa, optimizers, meta, self-improvement.
- **Wrapper:** `.claude/skills/content-forge/` — entry `/forge <sorgente> [--target=agent|team|skill|...]`.
- Invarianti: no summary · invenzioni `➕` · coverage atomi 100% in MKD · scaffolding PLAN→ASK→BUILD →CRITIQUE→ITERATE · progressive disclosure.

## Usi attuali
Motore ufficiale per creare nuovi agenti/skill dell'impero (WF-AGENT-NEW / WF-SKILL-NEW).
Backlog: skill `/youtube-lead-machine` da `Formazzione/Youtube/`.

## Connessioni
- [[Tool_Forge_Agent_Skill_Reparto]] · [[Tool_Master_Build_Architecture]] · [[Tool_Copy_Workflow_Orchestration]]
