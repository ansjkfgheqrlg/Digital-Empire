---
Type: PROJECT
Status: Active
Tags: #cliente #automotive #workflow #preventivi #mobile-de #multi-tenant
Created: 2026-06-30
Last updated: 2026-06-30
---

# Cliente — Prof Autocad (Automotive)

## Overview
**Primo cliente ufficiale di Digital Empire.** Concessionario / rivenditore auto che importa
auto dalla Germania (mobile.de) e le rivende in Italia.

## Cosa costruiamo
**PreventivoForge** — un workflow che trasforma un **annuncio straniero** (mobile.de, tedesco)
in un **PREVENTIVO italiano** (PDF) pronto per il cliente finale: foto, scheda tecnica e
descrizione tradotte + copy migliorato, e **prezzo finale calcolato nel titolo**.

> **Multi-tenant by design:** lo stesso workflow serve **molte concessionarie**. Ogni
> concessionaria ha la sua config (prezzo, logo, contatti, template) in
> `preventivo-forge/concessionarie/<id>/`. La prima è **prof-autocad**.

## Deliverable attivo
- [preventivo-forge/](preventivo-forge/) — il workflow completo (multi-agente).
  Architettura: [preventivo-forge/00-ARCHITETTURA-WORKFLOW.md](preventivo-forge/00-ARCHITETTURA-WORKFLOW.md).
  Handoff Half B (Gael): [preventivo-forge/HANDOFF-GAEL.md](preventivo-forge/HANDOFF-GAEL.md).

## Regola prezzo (confermata Max 2026-06-30, per-concessionaria)
`finale = round(esposto_mobile_de × 1.03 + 1500 + 1500)` → scritto nel **titolo**.
Es: esposto 18.000 € → **21.540 €**. (Parametri per dealer in `concessionarie/<id>/config.json`.)

## Stato build
- **Half A (Max): FATTO il core runnable** — scraper, parser, pricer, regia `run.py`, schema, multi-tenant. Testato.
- **Half B (Gael): DA FARE** — traduzione+copy (S3), PDF preventivo (S5), 4 agenti QA. Vedi HANDOFF-GAEL.md.

## Riferimento formato preventivo
Modello target = il PDF preventivo del cliente (es. "Preventivo BMW Z4"). ⚠️ Da rifornire a Max
(era su path WhatsApp temporaneo): metterlo in `concessionarie/prof-autocad/_riferimenti/`.

## Connessioni
- Skill motore: `content-forge`, `copywriting`, `cro-copy-architect`, `playwright-dev`, `architect-agent`
- Coordinamento build 50/50 Max↔Gael: `company/Memory/STATO-EMPIRE.md`
