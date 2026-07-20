---
Type: PROJECT
Status: Active
Tags: #mentalita-brutale #instagram #automation #content-factory #meta-api
Created: 2026-07-20
Last updated: 2026-07-20
---

# Mentalità Brutale — Social Operating System (MB-OS)

## Overview

Tenant operativo API-first che automatizza `@mentalita.brutale` da Intelligence a produzione, QA indipendente, scheduling, pubblicazione Meta, Insights e apprendimento. Nasce per chiudere lo stream S4 del Piano Estate: la pagina si riattiva solo quando l'operatività può raggiungere `CERTIFIED_AUTO` senza password nel codice, pubblicazioni duplicate o pattern inventati.

## Architettura

MB-OS non duplica l'azienda: orchestra capability esistenti.

- P&L: 05-MULTI-BUSINESS.
- Produzione: 03-CONTENT-FACTORY CF-R1→R5.
- QA: CF-R6 indipendente.
- Pubblicazione: CF-R7, Instagram Graph API v25.0 configurabile.
- Apprendimento: CF-R8 + Marketing Analytics.
- Ingestione video: [[Empire_Studio]].
- Nuove capability: Chief-Forge → ARCHITETTURA → FORGE.
- Memoria: SQLite locale + [[projects/Piano_Maestro_EMPIRE_OS|EMPIRE OS Memory]].

## Authorization

Percorso scelto: Business Login for Instagram, account professionale owner-managed. Scope core:

- `instagram_business_basic`
- `instagram_business_content_publish`
- `instagram_business_manage_insights`

Token/app secret vivono solo in `.env` locale o secret manager. Le password che erano presenti nel publisher legacy sono state rimosse dai file correnti ma devono essere ruotate, perché Git history equivale a compromissione.

## Autonomia

```text
SHADOW → SUPERVISED → CERTIFIED_AUTO → PAUSED
```

Target: `CERTIFIED_AUTO`; stato iniziale: `SHADOW`. Certificazione: ≥5 dry-run, token health, canary publish, post-check, Insights e secret scan. Dopo la certificazione non serve review umana per-post; restano 5 gate automatici, cap, idempotenza e kill switch.

## Strategia baseline

28 giorni: 28 post, 16 Reel + 12 caroselli. Due hook, due slot, CTA bilanciate; metric snapshot a +48h e +7d. Pattern promossi solo con n≥3 e confronto nello stesso formato.

## Stato video

Nel checkout non esistono file video tracciati. Il Drive legacy espone un file `.mp4`, ma non è stato osservato integralmente in questa fase. Perciò i timing Reel sono ipotesi e il Reel Pattern Extractor resta bloccato fino a ingestione Empire Studio con frame e transcript reali.

## Path

- Sistema: `Page IG - Mentalità Brutale/OPERATING-SYSTEM/`
- Skill: `.claude/skills/mentalita-brutale-operator/`
- Runbook: `Page IG - Mentalità Brutale/OPERATING-SYSTEM/architecture/06-RUNBOOK.md`
- Runtime: `Page IG - Mentalità Brutale/OPERATING-SYSTEM/runtime/`

## Connessioni

- [[Empire_Studio]]
- [[projects/Piano_Maestro_EMPIRE_OS|Piano Maestro EMPIRE OS]]
- [[tools/Tool_ClaudeFlow_Orchestration|Ruflo / Multi-Agent Orchestration]]
- [[03 - Resources/tools/Memory_Empire|Memory Empire]]
