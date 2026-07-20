# MB-OS Fase 002 — Analisi, Brainstorming e Planning

> Data: 2026-07-20 · Stato: piano esecutivo · Modalità runtime: `SHADOW` · Nessun side effect.

## Metodo

Questa fase separa volutamente quattro momenti che non vanno confusi:

1. **ANALISI** — cosa esiste davvero, cosa manca, quali vincoli sono provati.
2. **BRAINSTORMING** — divergenza: 64 possibilità senza innamorarsi della prima idea.
3. **CONVERGENZA** — matrici pesate: cosa entra, cosa aspetta, cosa viene scartato.
4. **PLANNING** — dipendenze, owner, gate, numeri, calendario e Definition of Done.

Il planning non sostituisce l'evidence. Tutto ciò che dipende da Reel non ancora osservati, dati performance assenti o decisioni commerciali è marcato `IPOTESI`, `DA MISURARE` o `DECISIONE OWNER`.

## Documenti

| Ordine | Documento | Funzione |
|---:|---|---|
| 1 | `01-ANALISI-AS-IS.md` | Diagnosi del sistema attuale e colli di bottiglia |
| 2 | `02-BRAINSTORMING-MASTER.md` | 64 idee in 8 domini, senza censura prematura |
| 3 | `03-DECISION-MATRIX.md` | Scoring, scelte architetturali, shortlist e scarti |
| 4 | `04-PIANO-ESECUTIVO-90-GIORNI.md` | Roadmap F0→F9, critical path, owner, gate, KPI |
| 5 | `05-CALENDAR-28D-SEED.md` | 28 brief seed bilanciati per baseline |
| 6 | `06-BUSINESS-MODEL-PLAN.md` | Motore economico, ladder offerte, attribuzione e gate |
| 7 | `PLAN.json` | Task board machine-readable per scheduler/EmpireDesk |

## Conclusione esecutiva

La soluzione scelta non è “un bot Instagram”. È un **tenant business autonomo ma certificato**:

```text
EVIDENCE → CONTENT IP → PRODUZIONE → QA → META API → INSIGHTS
    ↑                                                    ↓
    └──────────── MEMORY / LEARNING / FORGE ─────────────┘
                              ↓
                AUDIENCE → LEAD POSSEDUTO → OFFERTA → REVENUE
```

### Sequenza non negoziabile

1. Bonifica sicurezza e 2FA.
2. Ingestione video reale + rights ledger.
3. OAuth Meta e media hosting HTTPS.
4. Produzione buffer + 5 dry-run.
5. Canary supervisionato + Insights a 48h.
6. Certificazione `CERTIFIED_AUTO`.
7. Baseline 28 giorni: 28 post, 56 snapshot.
8. Distillazione pattern n≥3.
9. Funnel e monetizzazione solo con attribution pronta.
10. Productizzazione multi-pagina solo dopo prova sul tenant interno.

## Numeri del piano

- 8 domini di brainstorming.
- 64 idee generate.
- 16 iniziative valutate nella matrice.
- 10 fasi F0→F9.
- 32 task nel board machine-readable.
- 28 contenuti seed: 16 Reel + 12 caroselli.
- 56 snapshot Insights pianificati: +48h e +168h.
- 5 quality gate bloccanti.
- 4 modalità di autonomia.
- 1 critical path verso il live.

## Vincoli attivi

- ADR-003: wrap, non riscrittura.
- ADR-009: autonomia solo dopo certificazione.
- B-009: rotazione credenziali prima di qualsiasi live.
- Video pattern: nessuna skill prima di ≥10 Reel integrali e ≥120 frame letti.
- Nessun token, password o app secret in Git/chat.
- Nessun KPI assoluto inventato prima della baseline.
