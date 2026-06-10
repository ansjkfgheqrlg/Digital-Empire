# memory-auditor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Gap non rilevati | azioni senza memoria passano | audit sistematico | azioni orfane | segnala e richiedi CP |
| Falsi gap | segnala a torto | criteri precisi | segnalazioni errate | ritara i criteri |
| INDEX corrotto | index incoerente | rebuild | conteggi errati | --index |
| Audit non loggato | nessuna traccia | log audit | memory vuota | registra l'audit |
| Audit troppo raro | problemi tardivi | audit periodico | gap accumulati | aumenta la frequenza |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
