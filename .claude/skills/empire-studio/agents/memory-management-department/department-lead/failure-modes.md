# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Aggiornamenti saltati | azioni senza CP | checklist post-azione | memory-auditor | CP retroattivi |
| INDEX disallineato | index non riflette i file | rebuild periodico | conteggi errati | memory_manager --index |
| Categoria sbagliata | bug in checkpoints | mappa evento->categoria | file fuori posto | rilocare nella categoria giusta |
| Nomi non-safe | file non estraibili | solo via manager | validator names | rigenera nome safe |
| Propagazione mancante | stato incoerente | update-propagator | stati divergenti | propaga gli aggiornamenti |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
