---
Type: TOOL
Status: Active
Tags: #outreach #agenti #cold-dm #whatsapp #linkedin #email
Created: 2026-07-30
Last updated: 2026-07-30
---

# Tool: Outreach Message Team

## Overview
Team di 4 agenti (generato via `/content-forge` il 2026-07-30) che scrive e valida
messaggi di cold outreach (LinkedIn DM, WhatsApp, email) applicando sempre
[[Framework_Barnum_Rainbow_5Pilastri]]. Nessun messaggio esce senza passare dal
gatekeeper.

## Dettagli

**Percorso**: `Outreach/agents/outreach-message-team/`

**Topologia**: Gatekeeper + Pipeline.
`case-study-forge` (decide l'offerta di valore gratuito) → `message-writer` (scrive il
draft) → `rule-keeper` (valida/respinge contro i 5 Pilastri, non negoziabile) →
`followup-sequencer` (gestisce la cadenza a 3 tentativi, 20%/40%/30%).

**Agenti** (ognuno con 7 file canonici: agent.md, system_prompt.md, tools.md,
playbook.md, failure_modes.md, eval_cases.json, README.md):
- `rule-keeper` — gatekeeper/coordinator, potere di veto assoluto
- `message-writer` — copywriter, applica Barnum/Rainbow + variabile hard-coded di nicchia
- `case-study-forge` — costruisce l'offerta di valore anticipato (reale o "artificiale")
- `followup-sequencer` — gestisce i 3 tentativi di follow-up, mai oltre

**Stato condiviso**: `Outreach/knowledge/outreach-message-team-state/<lead_id>.json`

**Già applicato in produzione**: `Outreach/Outreach Workflow/campagne/concessionari-preventa/personalizza_messaggi.py`
ha già il "Gancio 4 — Import/annunci esteri" che implementa lo stesso principio
(variabile hard-coded di nicchia, ignora priorita_lead) — vedi
[[project_preventivoforge_fabbrica]] e `company/Memory/checkpoints/CP-20260729-007.md`.

## Connessioni
- [[Framework_Barnum_Rainbow_5Pilastri]]
- [[Framework_Cold_Outreach_APSOC]]
- [[project_outreach_system]]
