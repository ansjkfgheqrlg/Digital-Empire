# Failure Modes — workflow-router

## FM-01: yt_ingest.py fallisce (URL non accessibile)
**Fix:** Logga errore, segnala a dept-lead. Non continuare senza ingest.json.

## FM-02: run-id con caratteri non-Windows-safe
**Fix:** Sanifica: lowercase, solo a-z 0-9 trattino. Tronca a 30 char.

## FM-03: frame_extractor.py senza --interval
**Fix:** Sempre aggiungi `--interval 2` di default. Se il video ha capitoli densi (<5s tra capitoli), usa `--interval 1`.
