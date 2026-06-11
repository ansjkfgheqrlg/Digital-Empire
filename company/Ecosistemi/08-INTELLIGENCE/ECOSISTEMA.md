# 🔭 08 — INTELLIGENCE

> **Livello:** L1 · **Priorità:** TRASVERSALE · **Stato:** ATTIVO (wiki + Empire Studio operativi)
> Dossier completo: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §INTELLIGENCE

## Missione

Cervello cognitivo della holding: ingesta conoscenza, la organizza, la rende
interrogabile dagli agenti. **Wiki = fonte di verità umana. AgentDB = indice semantico agenti.**
Ogni operazione logga in `wiki/log.md` (wiki-first, pattern #12).

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Ingestione (Empire Studio) | ingestione video YouTube (frame extraction + analysis + atoms) | `Reparti/Ingestione/` |
| L2.2 | Wiki & Knowledge | gestione `second-brain-vault/wiki/`: INGEST, QUERY, LINT, SYNTHESIS | `Reparti/Wiki/` |
| L2.3 | Memory Empire | enrichment skill, reasoningbank, learning dai fallimenti | `Reparti/Memory-Empire/` |
| L2.4 | Research & Trend | ricerca ICP, competitor, trend mercato, nuove opportunità | `Reparti/Research/` |

## Asset attivi

| Asset | Stato | Path |
|---|---|---|
| Wiki second-brain | ATTIVO | `second-brain-vault/wiki/` |
| Empire Studio pipeline | ATTIVO (usata in sessioni precedenti) | `~/.claude/skills/memory-empire/` |
| Memory Empire skill | ATTIVO | installata globalmente |
| Wiki index | ATTIVO | `second-brain-vault/wiki/index.md` |
| Wiki log | ATTIVO | `second-brain-vault/wiki/log.md` |

## Ingestioni canali YouTube (PENDENTE)

⚠️ **@Legamidiamore** e **@dosementale** — NON ancora ingeriti.
Task 7.0/F-MB1 — sessione dedicata futura. Non farlo in questa sessione.

## Come si collega al Backbone

- **BRAIN:** è il gestore del BRAIN — mantiene AgentDB + wiki bridge + ReasoningBank
- **BUS:** riceve richieste di ricerca da tutti; invia knowledge pack al richiedente
- **GOVERNANCE:** wiki-sync-guard garantisce che ogni operazione loggi in wiki/log.md

## Standard operativo wiki (invariante)

- Ogni sessione: leggi `wiki/index.md` + `wiki/log.md` prima di rispondere
- Ogni nuova entità/progetto/tool/concetto: crea pagina nella categoria giusta
- Ogni operazione: entry in `wiki/log.md` con data e impact
- Cross-link obbligatori: ogni pagina nuova linka ≥ 2-3 pagine esistenti

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` · Aggiornato: 2026-06-11*
