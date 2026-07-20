---
Type: TOOL
Status: Active
Tags: #forge #reparto #agenti #skill #adr-009 #canonici-7
Created: 2026-07-20
Last updated: 2026-07-20
---

# FORGE-AGENT-SKILL — Reparto officina agenti & skill

## Overview
Nuovo reparto operativo dell'impero (ADR-009, direttiva Max 2026-07-20): crea **NUOVI AGENTI e NUOVE SKILL**
per tutti gli ecosistemi, standard CF-grade (7 file canonici: spec, system-prompt, tools, playbook, evals,
failure-modes, memory), con gate bloccante e intestazione ADR-008 obbligatoria. Sotto l'egida di 06b-FORGE
(L2.1 SKILL-WORKS / L2.2 AGENT-WORKS).

## Asset
- **Sede:** `FORGE-AGENT-SKILL/` (root) — README (missione + DONE WHEN), agents/ (roster: fas-conductor,
  fas-agent-smith, fas-skill-smith, fas-qa-gate), workflows/ (WF-AGENT-NEW, WF-SKILL-NEW),
  rules/ (R1 mai riassunti · R2 7 canonici · R3 failure-modes · R4 niente orfani ADR-008), memory/.
- **Motori (wrap ADR-003):** [[Tool_Content_Forge_2]] (`/forge`) · [[Tool_Master_Build_Architecture]] (metodo).

## Flusso
Richiesta capability (contratto 06b §1.2) → RECALL anti-duplicazione → MKD (/forge) → FORGE-PLAN →
BUILD 7 file → GATE fas-qa-gate (7 controlli bloccanti) → registrazione REGISTRO-IMPRESA + skills-map → CP.

## Connessioni
- [[Piano_Maestro_EMPIRE_OS]] · `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md` (MIR-5 retrofit)
- [[Tool_Content_Forge_2]] · [[Tool_Master_Build_Architecture]] · [[Tool_Copy_Workflow_Orchestration]]
