---
Type: TOOL
Status: Active
Tags: #architettura #swarm #memory-first #vendor #meta-skill
Created: 2026-07-20
Last updated: 2026-07-20
---

# Master Build Architecture (skill di architettura madre)

## Overview
Skill meta-ricorsiva per progettare architetture complete: swarm multi-agente (Ruflo-style), ecosistemi
di memoria dal passo zero, 7 file canonici per agente, failure-modes di prima classe, traceability
sorgente→output, processo in 10 fasi. Regola d'oro per DE (direttiva Max 2026-07-20):
**l'oggetto è un IMPERO CON PIÙ WORKFLOW, non un workflow** — mai progettare workflow orfani (ADR-008).

## Asset
- **Vendor:** `master-build-architecture/` alla root — ⚠️ versione di riferimento = quella su `main`
  (più completa del clone GitHub: agents/meta + OPERATING-REGISTRY). Clone fresco scartato (CP-20260720-007).
- **Wrapper:** `.claude/skills/master-build-architecture/` — entry `/master-architect <visione> [--target=...]`.
- Knowledge pack: `references/knowledge-pack/` (15 principi, 11 pattern, 9 anti-pattern).

## Applicazione fatta
Revisione architetturale dell'impero → `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md`
(audit sulle 10 invarianti + mappa dei 10 workflow vivi + 12 migliorie MIR con owner/gate/priorità).

## Connessioni
- [[Tool_Forge_Agent_Skill_Reparto]] · [[Tool_Content_Forge_2]] · [[Tool_Copy_Workflow_Orchestration]]
