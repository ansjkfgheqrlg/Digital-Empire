# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| TikTok senza sottotitoli | subs vuoto | fallback a sola visione | nessun vtt | frame densi + audio se disponibile |
| Watermark/qualita' bassa | frame poco leggibili | miglior formato disponibile | frame sfocati | estrai piu' frame, scegli i nitidi |
| Profilo grande | troppi video | cap + trend-scout | molti entry | seleziona i top per rilevanza |
| Contenuto effimero | video rimosso | ingest tempestivo | 404 | salta, logga in errors |
| Durata brevissima | pochi secondi | frame ogni 2-3s | durata <10s | estrai comunque 4-6 frame chiave |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
