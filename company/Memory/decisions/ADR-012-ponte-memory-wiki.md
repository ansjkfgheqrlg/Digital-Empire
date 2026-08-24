# ADR-012 — Ponte esplicito company/Memory ↔ wiki (memory-wiki-bridge + /sync-wiki-totale)

- **Data:** 2026-08-23
- **Stato:** ATTIVO
- **Decisori:** Max

## Contesto
Digital Empire ha due sistemi di memoria attivi in parallelo: `company/Memory/` (REGOLA ZERO,
CLAUDE.md — checkpoint, ADR, STATO-EMPIRE, sempre rispettato) e la wiki
`second-brain-vault/wiki/` (REGOLA FONDAMENTALE — pensata come vista pubblica/navigabile con
grafo di tutta la conoscenza). Il reparto Memory Empire (`~/.claude/skills/memory-empire/`)
aveva un solo percorso di sync verso la wiki: `wiki-syncer`, attivato SOLO a fine ingestione
Empire Studio (video/tiktok/web/repo esterni). Il lavoro interno (checkpoint chiusi, ADR,
decisioni in STATO-EMPIRE) non passava da nessun agente di sync verso la wiki. Effetto reale
misurato il 2026-08-23: 16 giorni (06→22 agosto), 16 checkpoint di lavoro reale, ZERO entry in
wiki/log.md — il grafo Obsidian non cresceva quanto il lavoro reale avrebbe richiesto.

## Decisione
Aggiunto un secondo percorso di sync esplicito, distinto da quello di Empire Studio:
- Nuovo agente **memory-wiki-bridge** (7-file, reparto `ingestion-archive`, gemello di
  wiki-syncer) — diffa `company/Memory/{checkpoints,decisions}` + `STATO-EMPIRE.md` contro
  `wiki/log.md` + `wiki/index.md`, colma i gap con pagine cross-linkate o entry log.md secondo
  rilevanza, mai overwrite.
- Nuovo comando **`/sync-wiki-totale`** (skill utente, `~/.claude/skills/sync-wiki-totale/`) —
  attiva entrambi i percorsi (memory-wiki-bridge + wiki-syncer su knowledge/ non ancora in
  wiki) e knowledge-cartographer per garantire zero pagine orfane nel grafo. Riporta sempre un
  conteggio MATCH/GAP esplicito.
- `routing-map.md` e `department-lead.md` di ingestion-archive aggiornati con la Pipeline B.

## Alternative scartate
- **Estendere wiki-syncer per coprire anche company/Memory** — scartato: wiki-syncer e' definito
  come "insieme al knowledge-keeper, a fine ingestione" (trigger = Empire Studio); sovraccaricarlo
  con un trigger diverso (chiusura checkpoint) confonde il contratto dell'agente.
- **Cablare il sync automaticamente a ogni chiusura checkpoint (nessun comando)** — scartato per
  ora: coerente con REGOLA nr.4 di Memory Empire ("nessun comando dall'utente") ma rischioso senza
  prima verificare il comportamento su un backfill controllato. Il comando manuale
  `/sync-wiki-totale` resta il modo per attivarlo finche' non e' verificato; l'automazione a fine
  checkpoint e' lasciata come step successivo esplicito (vedi Conseguenze).

## Conseguenze
- Il grafo wiki puo' ora essere riallineato al lavoro reale con un comando, non serve piu' un
  audit manuale come quello del 2026-08-23.
- Backlog B-019 (buco storico pre-luglio 2026, creazione monorepo 2026-06-10 → primo log wiki
  2026-07-04) resta esplicitamente FUORI da questo ADR: va eseguito solo su via libera diretta
  di Max, mai automaticamente da `/sync-wiki-totale`.
- Prossimo passo naturale (non fatto qui): valutare se cablare memory-wiki-bridge come hook
  automatico a fine checkpoint (coerente con REGOLA ZERO), una volta verificato che
  `/sync-wiki-totale` produce risultati puliti (no pagine orfane, no rumore nel grafo).

## Contradiction-check
Verificato contro ADR-002 (memory-first): non contraddetto, anzi rinforzato — questo ADR rende
operativa la regola "nessun task e' fatto finche' non e' salvato in Memory" anche lato wiki.
Nessun conflitto con ADR-006 (ciclo fase 9 passi) o ADR-008 (skills-map/catena controllo).
