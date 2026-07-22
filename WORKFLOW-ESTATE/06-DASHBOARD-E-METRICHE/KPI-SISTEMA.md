---
Owner: Max
Controllore: Claude
Origine: FORGE (GEM-04)
Governo: MANDATO Art.8 + ADR-008
---

# 🎯 KPI-SISTEMA — SPECIFICA NUMERICA DEI PERFORMANCE INDICATORS

> **Governo Art.8 §8.3:** Specifica formale dei KPI quantificati e reali del sistema Empire e del Workflow Estate. Ogni KPI è legato a una metrica di controllo esatta e a un gate automatico.

## 1. KPI DI REVENUE & CONVERSIONE (S1..S6)

### KPI-REV-01: Tasso di Chiusura Concessionari (S1)
- **Definizione:** Rapporto tra preventivi/demo erogati via PreventivoForge e contratti di anticipo luglio firmati.
- **Formula:** `(Contratti Firmati / Demo Erogate) * 100`
- **Target:** `≥ 28.5%` (su 7 lead caldi, minimo 2 chiusure).
- **Sorgente Dati:** Registro chiamate A8-Closing + record PreventivoForge.

### KPI-REV-02: Conversione Funnel Manuale (S2)
- **Definizione:** Percentuale di visitatori unici della landing page `empire-premium-style` che completano il checkout del Manuale Claude Code per il Business.
- **Formula:** `(Acquirenti / Sessioni Uniche Landing) * 100`
- **Target:** `≥ 3.2%` (con traffico caldo/tepido da outreach e bio).
- **Sorgente Dati:** Stripe Analytics + PostHog / Server Logs.

---

## 2. KPI DI PERFORMANCE AUTOMAZIONI (ENGINE & S3..S5)

### KPI-ENG-01: Tempo Totale di Scansione Censimento (`census.py`)
- **Definizione:** Tempo impiegato dal modulo `empire.registry.census` per inventariare e validare l'intero monorepo (oltre 58.000 file totali, ~11.600 artefatti gestiti).
- **Target:** `< 5.0 secondi` (ottenuto tramite potatura `os.walk` in-place di `.git` e `node_modules`).
- **Sorgente Dati:** `census.json` (campo `scan_time_sec`).

### KPI-ENG-02: Indice di Tolleranza Provenance (ADR-008)
- **Definizione:** Percentuale di file creati o modificati dopo la data di cutoff (`2026-07-19`) che possiedono un frontmatter YAML o docstring Python completa e conforme ad ADR-008.
- **Target:** `100%` (Gate bloccante 🔴 per ogni nuovo file privo di provenienza).
- **Sorgente Dati:** `python -m empire registry orphans --json`.

### KPI-OUT-01: Score APSOC sui Copy e Kit di Delivery
- **Definizione:** Punteggio di rispondenza ai 5 stadi del framework di Andrei Pascu (Attention -> Problem -> Solution -> Offer -> Close) per i template in `05-TEMPLATES-E-KIT/`.
- **Target:** `≥ 92%` (misurato tramite la Checklist APSOC `checklist_APSOC.md`).
- **Sorgente Dati:** `evals` degli agenti di copy (`cro-copy-architect`).
