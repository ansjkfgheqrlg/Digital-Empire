# Failure Modes — intent-classifier

## FM-01: URL in formato non standard
**Causa:** URL senza https (es. "youtube.com/watch?v=...") o shortenato
**Fix:** Espandi il pattern regex; cerca anche "youtu.be/" senza schema

## FM-02: Messaggio in italiano con link ambiguo
**Causa:** Link a sito non riconoscibile come video (es. notionsite con video embedded)
**Fix:** Se URL presente e non classificabile → INGEST_LINK generico con platform=web

## FM-03: Output non JSON
**Causa:** Agent produce prosa invece di JSON
**Fix:** System prompt richiede esplicitamente solo JSON. In caso di errore, dept-lead riclassifica manualmente.
