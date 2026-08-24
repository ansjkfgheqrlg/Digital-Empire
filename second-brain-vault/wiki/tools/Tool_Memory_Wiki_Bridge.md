---
Type: TOOL
Status: Active
Tags: #memory #wiki #memory-empire #infrastruttura
Created: 2026-08-23
Last updated: 2026-08-23
---

# memory-wiki-bridge + /sync-wiki-totale

## Overview
Ponte esplicito tra i due sistemi di memoria di Digital Empire: `company/Memory/` (REGOLA
ZERO — checkpoint, ADR, STATO-EMPIRE, sempre rispettato) e questa wiki (REGOLA FONDAMENTALE —
vista pubblica/navigabile con grafo). Prima di questo tool, solo il contenuto ingerito da
Empire Studio (video/tiktok/web) aveva un percorso automatico verso la wiki; il lavoro interno
non ne aveva nessuno.

## Dettagli
Causa reale, non ipotetica: il 2026-08-23 e' stato trovato un buco di 16 giorni (06→22 agosto)
tra checkpoint chiusi in `company/Memory/` (16 reali) e entry in `wiki/log.md` (zero) — colmato
a mano quello stesso giorno (vedi [[tools/Tool_Pipeline_Libri_KDP]] ed [[entities/Entity_The_Quiet_Hours_Libro_KDP]],
entrambe backfillate in quella sessione) e documentato nella entry `## 2026-08-23` di `log.md`.
Questo tool rende quel tipo di audit ripetibile con un comando invece che a mano.

Componenti:
- **memory-wiki-bridge** — agente 7-file (`~/.claude/skills/memory-empire/departments/
  ingestion-archive/memory-wiki-bridge/`), gemello dell'agente `wiki-syncer` esistente ma con
  trigger diverso: non fine-ingestione Empire Studio, ma diff esplicito company/Memory ↔ wiki.
- **`/sync-wiki-totale`** — comando (`~/.claude/skills/sync-wiki-totale/`) che attiva il bridge +
  `wiki-syncer` (per knowledge/ non ancora in wiki) + `knowledge-cartographer` (verifica che
  nessuna pagina nuova resti orfana nel grafo). Riporta sempre un conteggio MATCH/GAP esplicito,
  mai un "fatto" senza numeri.
- **ADR-012** (`company/Memory/decisions/ADR-012-ponte-memory-wiki.md`) — decisione registrata:
  sync resta on-demand (comando manuale), non automatico ad ogni checkpoint, finche' non
  verificato pulito su un ciclo reale.

Scope deliberatamente escluso: il backlog storico B-019 (buco pre-luglio 2026, dalla creazione
del monorepo 06-06-2026 al primo log wiki 04-07-2026) NON viene toccato da questo tool in
automatico — richiede via libera esplicita di Max, come gia' deciso per il gap di agosto.

## Connessioni
- [[projects/Piano_Maestro_EMPIRE_OS|PIANO MAESTRO EMPIRE OS]] — ecosistema 10 MEMORY, REGOLA ZERO
- [[tools/Tool_Nerve_Solve_Orchestration_Layer|NERVE-SOLVE]] — altro sistema nervoso della holding, stesso principio di meccanismo esplicito invece di regola sola
- `second-brain-vault/wiki/log.md` — entry `2026-08-23` (buco 16gg trovato e colmato a mano, causa identica risolta qui in modo permanente)
