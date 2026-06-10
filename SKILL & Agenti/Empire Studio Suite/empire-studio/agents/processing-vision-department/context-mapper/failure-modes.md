# context-mapper - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| KG piatto | atomi senza relazioni | cerca prerequisiti/esempi | 0 archi | rianalizza le dipendenze |
| Collegamenti errati | relazioni spurie | soglia di confidenza | archi incoerenti | rimuovi i deboli |
| Gap non rilevati | concetti orfani | lista termini citati vs spiegati | termini senza atomo | segnala gap al lead |
| Memoria non consultata | duplica cio' che gia' sa | query knowledge-state | atomi gia' presenti | collega all'esistente invece di duplicare |
| KG troppo grande | esplosione relazioni | cap per rilevanza | archi eccessivi | tieni le relazioni piu' forti |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
