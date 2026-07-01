# Failure modes — op-scraper

| Failure | Sintomo | Prevenzione | Rilevazione | Recupero |
|---|---|---|---|---|
| Blocco anti-bot | pagina blocco/vuota | profilo persistente + UA + consenso | `_looks_blocked()` | headful + consenso manuale, o `--manual` |
| Consenso non cliccato | contenuto nascosto | selettori multipli + iframe | pochi dati estratti | aggiungi selettore; headful |
| Foto lazy non caricate | poche `image_urls` | scroll ripetuto | conteggio basso vs gallery | aumenta scroll; retry |
| Foto 403 | download fallito | header `Referer` | eccezione requests | 3 retry; warning se persiste |
| JSON-LD cambiato/assente | `jsonld=[]` | fallback DOM | `_extract_jsonld` warning | il parser usa DOM; segnala a Max |
| Selettori DOM cambiati | `attributes` vuoto | label DE multiple | warning | aggiorna `GERMAN_LABELS`/selettori |
| Playwright mancante | ImportError | requirements + install | RuntimeError | installa o usa `--manual` |
