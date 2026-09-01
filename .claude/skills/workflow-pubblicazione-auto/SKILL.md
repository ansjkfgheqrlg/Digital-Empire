---
name: workflow-pubblicazione-auto
description: "Sistema operativo di pubblicazione automatica Digital Empire. Gestisce creazione, revisione e pubblicazione contenuti su Instagram e TikTok per Digital Empire (CRO) e Mentalita Brutale (KDP/mindset)."
---

# Workflow Pubblicazione Automatica

Sistema operativo di pubblicazione per Digital Empire.

## Quando usarla

USE THIS SKILL when the user wants to:
- Publish content automatically to Instagram or TikTok
- Run the daily publication workflow
- Check content readiness before publishing
- Manage multi-brand publishing (Digital Empire + Mentalita Brutale)

## Brand

1. **Digital Empire** — CRO, Landing Page, formazione. Tone: diretto, sincero, orientato alla formazione.
2. **Mentalita Brutale** — Storia, mindset, libri KDP. Tone: autoritario, storico, affascinante.

## Regole

- Workflow deterministico — usa sempre le skill, mai "a intuito"
- 90% Valore, 10% Vendita
- CTA principale Digital Empire: "Briefing Call Gratuita"
- Esegui `check_ready.py` prima di pubblicare, poi `push_social.py`

## Struttura

- `main_orchestrator.py` — Orchestratore principale
- `pubblica.py` — Script pubblicazione
- `run_daily.py` — Scheduler giornaliero
- `Instagram/`, `LinkedIn/`, `TikTok/` — Asset per piattaforma
