---
Type: TOOL
Status: Active
Tags: #copy #apsoc #workflow #marketing #vendor
Created: 2026-06-15
Last updated: 2026-07-20
---

# Copy Workflow Orchestration Layer (motore copy ufficiale)

## Overview
Sistema multi-agente per copy persuasivo professionale basato su framework **APSOC**
(Attenzione → Problema → Soluzione → Obiezioni → CTA). Team di 8 agenti (A1 briefing, A2 target,
A3-A7 scrittura sequenziale, A8 QA reviewer con score ≥85). Owner: 04-MARKETING / L2-1 Copywriting.

## Stato dell'asset (agg. 2026-07-20 — ADR-009)
- **Motore vendored ufficiale:** `copy-workflow/` alla root (clone `gh repo clone ansjkfgheqrlg/copy-workflow`).
- **Wrapper skill:** `.claude/skills/copy-workflow/` → entry point `/copywriting`
  (modalità: full, ad, sales-page, email, vsl, social, headline, objections, avatar, funnel, review).
- Skill interne: `copy-workflow/skills/` (apsoc-builder, copy-review, funnel-designer, headline-forge,
  objections-forge, target-avatar) · workflow: `copy-workflow/workflows/` (6).
- **ADR-003:** wrap, mai riscrittura (diff vendor = 0 verificato nei gate FORGE-AGENT-SKILL).

## Regola d'uso
Ogni copy dell'impero passa di qui (MIR-2 da `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md`).
Prima applicazione: review APSOC del kit YouTube → `Formazzione/Youtube/COPY-REVIEW-APSOC.md` (score 78-84 → 90-93).

## Connessioni
- [[Tool_Content_Forge_2]] · [[Tool_Master_Build_Architecture]] · [[Tool_Forge_Agent_Skill_Reparto]]
- [[Concept_APSOC_Formula]] · [[Concept_Conversion_Rate_Moltiplicatore]]
