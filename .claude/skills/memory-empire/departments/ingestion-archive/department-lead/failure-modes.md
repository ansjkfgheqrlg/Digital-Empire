# Failure Modes — ingestion-archive / department-lead

## FM-01: video-analysis.md assente
**Causa:** Empire Studio non ha completato la visione
**Fix:** Segnala a routing-dispatch. Non archiviare senza visione reale.

## FM-02: atoms.json con 0 atomi
**Causa:** video-analysis.md troppo generico o vuoto
**Fix:** Genera manualmente leggendo il VTT + video-analysis.md

## FM-03: wiki-syncer fallisce
**Causa:** wiki path non trovato
**Fix:** Verifica path wiki in second-brain-vault/wiki/. Usa wiki_writer.py se disponibile.
