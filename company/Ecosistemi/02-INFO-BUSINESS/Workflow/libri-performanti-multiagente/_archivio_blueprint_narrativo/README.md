# Archivio — Blueprint narrativo NON funzionante

**Spostato qui:** 2026-08-05, PIANO-KDP-67 CP11. **NON cancellato** (default del piano: archiviare,
non cancellare), ma **nessun file qui dentro è usato dal motore reale** (`../engine/`).

## Cosa c'è qui e perché

- `workflow_architecture/`, `official_claude_architecture/`, `architettura_sincrona/`,
  `architettura_completa_7_livelli/` — le 4 varianti di un'architettura a 95+ agenti
  consegnate in due zip successivi (2026-08-03 e 2026-08-05). Verificato sul codice reale,
  non sui documenti che le descrivono: **zero automazione reale**. Playwright sempre
  simulato (un commento mai eseguito, in tutte le varianti), zero righe di codice che
  parlano con LM Arena, zero gestione sessioni, script "genera libro" che copiava sempre
  lo stesso file template. Dettaglio completo dell'audit in
  [CP-20260805-001](../../../../../Memory/checkpoints/CP-20260805-001.md).
- `gen_*.py`, `append_detailed.py` — gli script che hanno generato le varianti sopra
  (meta-generatori, non parte del motore).
- `ARCHITETTURA_COMPLETA_FINALE.md`, `WORKFLOW-BLUEPRINT-Completo.md` — la documentazione
  narrativa che descrive l'architettura a 95 agenti. Contiene anche riferimenti a una
  "Official Claude Code Managed Agents API" (`managed-agents-2026-04-01`) che non risulta
  esistere nella superficie reale delle API Anthropic — **non affidarsi a questi documenti
  come fondamento tecnico**, sono lasciati solo come riferimento storico di cosa era stato
  proposto.
- `bozza_manuale_abbandonata_output/` — introduzione + 2 capitoli di un libro
  ("The AI Career Pivot") scritti a mano da Claude in chat, prima che Gael correggesse
  esplicitamente l'approccio ("no, non devi farlo te, deve farlo il workflow", 2026-08-04/05).
  Lasciati come possibile riferimento di stile/qualità per CP5 (Book Writer), non come
  contenuto da pubblicare.

## Cosa sostituisce tutto questo

Il motore reale è in [`../engine/`](../engine/) — moduli Python testati con esecuzione reale
ad ogni checkpoint, vedi [`../PIANO-KDP-67.md`](../PIANO-KDP-67.md).
