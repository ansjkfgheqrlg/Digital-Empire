# site-crawler - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Loop di link | crawl infinito | visited-set + cap | ripetizioni | interrompi al cap |
| Pagine pesanti | timeout render | timeout + lazy load | render lento | screenshot parziale + testo |
| Screenshot inutili | immagini senza valore | cattura solo sezioni chiave | screenshot generici | mirati a UI/diagrammi |
| Contenuto duplicato | stesse pagine | dedup per URL canonico | URL ripetuti | deduplica |
| Cookie/consent | overlay blocca | gestisci banner consent | modale | chiudi/accetta il banner e procedi |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
