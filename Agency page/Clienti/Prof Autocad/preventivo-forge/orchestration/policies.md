# Policies — PreventivoForge

## Retry & backoff
- **Foto (S1):** 3 tentativi con attesa crescente (1.2s×n) + header `Referer`. Falliti → warning.
- **Navigazione (S1):** `NAV_TIMEOUT_MS` (default 45s). `networkidle` best-effort (8s) non bloccante.
- **Stage generico:** un retry automatico; alla 2ª failure → STOP con report.

## Gate (bloccanti)
Ogni gate rosso ferma la pipeline. **Mai consegna parziale.** Il conductor riporta stage + motivo.
Gate A minimo è built-in in `run.py` finché `qa-extraction-verifier` (Gael) non esiste.

## Fallback
- **Anti-bot (S1):** headful (`PLAYWRIGHT_HEADLESS=false`) + consenso manuale (profilo persistente),
  oppure modo `--manual <html> --foto <dir>`.
- **Config dealer incompleta:** default da `.env`; warning nel report.

## Sicurezza
- Segreti/config SOLO da `.env` (mai hardcoded, mai committati — vedi `.gitignore`).
- Profilo browser persistente in `BROWSER_PROFILE_DIR` (gitignored).
- Nessuna azione esterna oltre lo scraping dell'URL fornito e il download delle sue foto.

## Budget
- Un run per volta. Nessuna scrittura fuori da `runs/<id>/`, `logs/`.
- I file di run pesanti (foto, pdf) sono gitignored; si versiona solo il codice + i JSON piccoli.

## Idempotenza & osservabilità
- Ogni run ha `id` univoco (`AF-YYYYMMDD-HHMMSS-<sourceid>`) → cartella isolata, rilanci non collidono.
- `state.json` (stato per step) + `trace.jsonl` (eventi) + `logs/<run>.log` sempre scritti.
