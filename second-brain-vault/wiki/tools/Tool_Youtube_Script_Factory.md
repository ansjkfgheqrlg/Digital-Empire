---
Type: TOOL
Status: Active
Tags: #skill #youtube #script #w7 #retrofit #mir-5
Created: 2026-07-20
Last updated: 2026-07-20
---

# Skill CRO YouTube Script Factory PRO

## Overview
La **fabbrica degli script del canale YouTube** (W7): per ogni video produce script completo con
7 componenti (Hook, Setup, Credibilità, Contenuto Core, Ricap, CTA, Retention Hooks), da 20 formule
hook/4 categorie, strutture per i 4 tipi video del mix (Anchor 70% · Shift 20% · Conversion/Audit 10%),
CTA a 3 livelli (Preview→Reminder→Finale), ottimizzazione titolo/thumbnail/description e scoring
qualità **45 punti** (11 sezioni) + backlog manager contenuti.

## Dove sta / come si usa
- **Master:** `SKILL & Agenti/SKILL/Skill CRO - Youtube - Lead magnet/Skill-youtube.md` (5.166 righe,
  vincolo ADR-003: intoccato). Per consultare: SEZIONE 6 = cheat sheet operativo (~215r), indice in `spec.md`.
- **Wrap canonico (retrofit MIR-5 sprint 1, 2026-07-20):** `spec.md` · `tools.md` · `playbook.md` ·
  `evals.md` · `failure-modes.md` · `memory/INDEX.md` nella stessa cartella.
- **Tool runtime (estratti 2026-07-20, compilano 3/3):** `tools/genera_script.py` ·
  `tools/checklist_qualita.py` (scoring 45pt + report) · `tools/backlog_manager.py` (mix 70/20/10, piano settimanale).
  Regola deriva: il markdown vince; se cambiano le sezioni 7-9 → ri-estrazione + ricompilazione.

## Deleghe (contratto del gate)
Scrittura script ← questa factory. **Strategia canale/funnel/mix → [[Tool_Youtube_Lead_Machine_Skill]]** ·
**QA copy marketing (APSOC) → [[Tool_Copy_Workflow_Orchestration]]**. La factory non decide strategia né fa APSOC.

## Connessioni
- [[01 - Projects/Project_YouTube_Lead_Machine]] (batch-01: gli script V01-V06 sono prodotti di questo metodo)
- [[Tool_Youtube_Lead_Machine_Skill]] (madre strategica) · [[Concept_YouTube_Funnel_TOFU_MOFU_BOFU]]
- Retrofit per MIR-5 (dossier 18): GATE retro PASS 7/7 → `FORGE-AGENT-SKILL/memory/checkpoints/GATE-retrofit-youtube-script-factory-2026-07-20.md`
