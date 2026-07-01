---
Type: PROJECT
Status: Active
Tags: #cliente #automotive #workflow #preventivi #mobile-de #multi-tenant
Created: 2026-06-30
Last updated: 2026-07-01
---

# Project — Prof Autocad · PreventivoForge

## Overview
Primo **cliente ufficiale** di Digital Empire: **Prof Autocad**, concessionario auto che importa
dalla Germania. Costruiamo **PreventivoForge**: workflow che trasforma un **annuncio mobile.de
(tedesco)** in un **preventivo italiano (PDF)** — foto + scheda + descrizione tradotte e copy
migliorato, **prezzo finale nel titolo** (`esposto ×1.03 +1500 +1500`). **Multi-concessionaria.**

## Dettagli
- Codice/SPEC: `Clienti/Prof Autocad/preventivo-forge/` (architettura `00-ARCHITETTURA-WORKFLOW.md`).
- Pipeline: S1 scraping (Playwright) → S2 parsing → GateA → S3 traduci+copy → GateB → S4 prezzo →
  GateC → S5 PDF preventivo → GateD.
- Team: 5 agenti operativi + 4 verificatori + conductor; skill regia `/preventivo-auto`.
- Build 50/50: **Max = Half A** (acquisizione/dati/prezzo/regia, ✅ fatta e testata) ·
  **Gael = Half B** (traduzione+copy, PDF, QA — handoff in `preventivo-forge/HANDOFF-GAEL.md`).
- Metodo: `architect-agent` (RBI) + `content-forge` (agenti 7-file) + repo `master-build-architecture`.

## Stato
Half A runnable e testata (Max). **Half B COMPLETA e verificata (Gael, 2026-07-01, CP-20260701-001):**
S3 traduzione+copy (glossario DE→IT deterministico ~150 termini), S5 render PDF (Playwright + template
Jinja2), QA Gate A/B/C/D bloccanti, 3 RULES, 6 agenti CF-grade (42 file). Test end-to-end reale
`run.py --manual` (BMW 320d) → PDF 63 KB, 4 gate ALL GREEN, prezzo 26.900→30.707 € (ricalcolo indipendente),
PDF ispezionato. Confine ADR-003 rispettato (run.py/schema/Half A non toccati). Traduzione deterministica → €0 API.
- **Pending (Max):** wiring gate B/C/D in `run.py`; primo run su URL mobile.de REALE.
- Riferimento formato preventivo: PDF "Preventivo BMW Z4" del cliente (da rifornire per allineare lo stile).

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- Memory: `company/Memory/checkpoints/CP-20260630-002.md`, `company/Memory/STATO-EMPIRE.md`
- Skill motore: [[content-forge]] · copywriting · cro-copy-architect · playwright-dev · architect-agent
