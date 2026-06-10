---
Type: TOOL
Status: Active
Tags: #skill #agency #smma #outreach #scaling #claude-code
Created: 2026-06-03
Last updated: 2026-06-03
---

# Tool — Agency Scalping (Skill Claude Code)

## Overview
Skill operativa installata ufficialmente in Claude Code (`~/.claude/skills/agency-scalping/`, v2.0.0) che guida l'utente dall'idea grezza di agenzia al business operativo (clienti, revenue, team, automazione). Estratta da 63.000+ parole di sorgenti reali (Eric Siu, guide IMA/SMMA/CRO). Architettura three-level (Conductor + Specialists + Tools) con memory system e progressive disclosure.

## Dettagli
- **Nome skill**: `agency-scalping` · **Versione**: 2.0.0 · **Tipo**: interactive
- **Invocazione**: `/agency-scalp [--fase=<1-9>] [--target=<...>] [--mode=<...>]` oppure trigger naturale ("voglio aprire un'agenzia", "come trovo clienti", "SMMA", "scalare l'agenzia").
- **9 Pilastri**: Nicchia · Offerta · Outreach · Vendita · Delivery · Team · Scaling · Modelli · Mindset.
- **Output installabili**: agenti AI (outreach/vendita/delivery), workflow, ecosistemi multi-agente, piani operativi.
- **Struttura** (129 file): `SKILL.md` kernel ≤500 righe + `agents/` (builders, domain, pipeline, optimizers, qa, self-improvement) + `references/domain/` (9 pillar) + `skill-planning-knowledge-pack/` (principi/pattern/anti-pattern/processi) + `scripts/` (coverage/schema/lint/memory) + `evals/` + `memory/`.

## Installazione & Distribuzione
- **Sorgente**: `SKILL & Agenti/Skill scalping agency/workspace-019e8de1-...zip` (workspace con vendor di build: ruflo, content-forge2.0, product-manager-skills — esclusi dall'install).
- **Install ufficiale**: estratta la sola cartella `agency-scalping/` in `C:\Users\Utente\.claude\skills\agency-scalping\` → attiva globalmente in tutte le sessioni Claude Code.
- **GitHub**: repo **privato dedicato** `ansjkfgheqrlg/agency-scalping` (solo questo account, branch `main`, 129 file). NON pushata sui due repo abituali (richiesta esplicita "solo nel Github ansjkfgheqrlg").

## Connessioni
- [[Tool_Copy_Workflow_Orchestration]] — altra skill orchestration con architettura agenti simile (APSOC)
- [[Framework_Cold_Outreach_APSOC]] — il pilastro Outreach si appoggia allo stesso framework
- [[Tool_ClaudeFlow_Orchestration]] — pattern three-level/swarm ispiratore dell'architettura
