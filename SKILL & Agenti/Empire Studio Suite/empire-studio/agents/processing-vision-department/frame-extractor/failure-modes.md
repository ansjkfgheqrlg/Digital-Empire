# frame-extractor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Frame neri/transizioni | PNG quasi neri | evita 0s esatto; usa +1s | varianza pixel bassa | estrai a +/-2s |
| Download formato assente | nessun mp4 <=360p | fallback a 'worst' | nessun file video | prova formato alternativo |
| ffmpeg seek impreciso | frame a tempo sbagliato | -ss prima di -i (veloce) accettabile | timestamp incoerente | seek accurato (-ss dopo -i) per i frame chiave |
| Video troppo lungo | download lento/pesante | low-res + cap frame | durata enorme | scarica solo segmenti chiave se possibile |
| Disco pieno | scrittura PNG fallisce | pulizia run vecchie | errore I/O | libera spazio, riprova |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
