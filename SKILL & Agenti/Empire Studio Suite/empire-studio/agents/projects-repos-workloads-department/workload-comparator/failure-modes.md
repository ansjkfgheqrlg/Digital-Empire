# workload-comparator - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Proposte generiche | vaghe | ancora a workflow specifico | nessun target | specifica file/agente |
| Falsa applicabilita' | pattern non trasferibile | valuta contesto | match forzato | scarta |
| Trace mancante | manca il 'da dove' | trace al progetto | trace vuota | aggiungi fonte |
| Modifica accidentale | tocca workflow esistenti | solo proposta | diff | annulla, resta read-only |
| Ignora i propri reparti | non considera Empire Studio stesso | includi self-improvement | nessuna proposta interna | valuta anche i reparti interni |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
