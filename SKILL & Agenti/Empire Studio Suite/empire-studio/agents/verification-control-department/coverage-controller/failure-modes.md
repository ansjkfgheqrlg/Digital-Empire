# coverage-controller - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Atomi persi | coverage bassa | soglia + check | atomi assenti nelle note | ri-forge mirato |
| Trace mancanti | atomi senza fonte | trace obbligatoria | campo vuoto | richiedi trace |
| Conteggio errato | metriche sbagliate | matching robusto | incoerenza | ricalcola |
| Soglia inadeguata | passa output povero | soglia >=90% | qualita' bassa | alza la soglia |
| Duplicati contati | coverage gonfiata | dedup prima del conteggio | atomi ripetuti | deduplica |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
