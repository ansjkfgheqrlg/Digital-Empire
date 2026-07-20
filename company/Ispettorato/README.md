---
Type: ORGAN
Status: Active (M1 — fondamenta)
Tags: #ispettorato #performance #autocritica #anti-recidiva #ADR-008
Created: 2026-07-20
Last updated: 2026-07-20
---

# ISPETTORATO GENERALE — Performance & Autocritica

> Spec completa: `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md`. Owner build: **MAX**.
> Direttiva Max (2026-07-04, estesa 2026-07-20): report dopo ogni run, analisi al millimetro,
> mai lo stesso errore due volte, **e** studio dei cicli di correzione per fare meglio al
> primo colpo, **e** studio di cosa esce bene — non solo di cosa esce male.

## Cos'è

L'organo trasversale che misura le performance dell'Impero. NON produce, NON corregge da solo:
**rileva, registra, assegna, verifica.** Indipendente da chi costruisce (come CF-R6, come A10).

## Stato build (M1→M5, dossier 15 §10)

- ✅ **M1 — Fondamenta dati** (questo commit): struttura + REGISTRO-ERRORI migrato (10 voci
  reali) + REGISTRO-REVISIONI seed + REGISTRO-SUCCESSI seed + KPI empire-wide.
- ⬜ M2 — Pilota PreventivoForge (trace JSONL reale).
- ⬜ M3 — Reparto CF-grade (11 agenti, 5 workflow) via FORGE.
- ⬜ M4 — Aggancio Impero (RECALL/RETRO, handoff MAXIMILIAN/Board/Sentinelle).
- ⬜ M5 — Estensione (telemetria outreach, report settimanale, hook post-run).

## Le 4 domande a cui risponde OGNI run

1. **Cosa è successo** (run-report completo, mai muta).
2. **È già successo prima** (REGISTRO-ERRORI — recidiva = gate ROSSO).
3. **Quante correzioni sono servite** (REGISTRO-REVISIONI — obiettivo: N cala nel tempo).
4. **È uscito bene al primo colpo?** (REGISTRO-SUCCESSI — pattern da ripetere, non solo errori).

## Struttura

```
registro/   REGISTRO-ERRORI.md · REGISTRO-REVISIONI.md · REGISTRO-SUCCESSI.md · REGISTRO-DECISIONI-ALTIRANGHI.md
telemetry/  runs/<workflow>/<run-id>.jsonl · daily/<data>.md
report/     run/ · daily/ · escalation/
kpi/        definizioni + soglie
agenti/     11 agenti CF-grade (M3) · workflow/ 5 WF (M3)
```

## Connessioni
- [[15-DOSSIER-ISPETTORATO]] · spec completa e vincolante
- [[ARCHITETTURA]] · `company/Ispettorato/ARCHITETTURA.md`
- [[REGISTRO-ERRORI]] · `registro/REGISTRO-ERRORI.md`
- [[ADR-008]] · catena intestazione — questo organo è intestato in `REGISTRO-IMPRESA.md`
- [[MAXIMILIAN]] · `company/MAXIMILIAN/` — riceve i report per il 5-bis
