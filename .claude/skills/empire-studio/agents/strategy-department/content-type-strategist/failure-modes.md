# content-type-strategist - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Tipo mal classificato | regole sbagliate | segnali multipli | output incoerente | riclassifica |
| Stile wiki errato | nota non adatta al tipo | mappa tipo->stile | nota fuori stile | correggi lo stile |
| Tipo misto | contenuto ibrido | consenti combinazioni | piu' tipi | strategia combinata |
| Generico | regole vaghe | regole specifiche per tipo | nessun dettaglio | dettaglia |
| Ignora il focus utente | non allineato | rispetta --focus | mismatch focus | riallinea al focus |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
