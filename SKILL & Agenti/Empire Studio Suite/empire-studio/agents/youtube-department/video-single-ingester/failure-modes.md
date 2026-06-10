# video-single-ingester - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Video lunghissimo (3h+) | info pesante, molti capitoli | nessun download in questo stadio | durata enorme | passa a Vision con nota di pianificare molti frame per capitolo |
| Nessun capitolo | chapters vuoto | fallback a frame per % | ingest.json chapters==[] | segnala a frame-extractor di usare intervalli |
| Auto-sub assenti | subs vuoto | richiedi piu' lingue | nessun vtt | procedi solo-visione, dichiara limite |
| Eta'-restricted/login | yt-dlp richiede auth | rileva il caso | errore login nei log | segnala al lead, salta o chiedi alternativa |
| Thumbnail webp non gestita | thumbnail in formato raro | accetta jpg/webp | estensione inattesa | ignora la thumbnail, non bloccante |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
