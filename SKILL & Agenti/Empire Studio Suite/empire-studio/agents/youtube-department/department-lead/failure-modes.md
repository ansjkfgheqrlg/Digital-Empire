# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Input ambiguo (shortened URL) | non si capisce se video o canale | normalizza l'URL e interroga yt-dlp per il tipo | yt-dlp ritorna playlist vs entry singola | espandi l'URL; in dubbio tratta come video singolo |
| Canale enorme | centinaia di video, rischio timeout | cap --max e screening per focus | total_candidates molto alto | batch da 15, avvisa il Conductor, prioritizza per focus |
| Video privato/rimosso | yt-dlp errore extract | ignoreerrors + check ritorno | ingest.json non creato | salta il video, logga in errors, continua con gli altri |
| Focus non matcha nulla | 0 video selezionati | fallback a screening per views/recency | selected==0 | allarga il match o chiedi al Conductor un focus alternativo |
| Mancano i sottotitoli | subs vuoto in ingest.json | richiedi auto-sub multi-lingua | campo subs vuoto | procedi con soli frame + metadata, segnala la limitazione a Vision |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
