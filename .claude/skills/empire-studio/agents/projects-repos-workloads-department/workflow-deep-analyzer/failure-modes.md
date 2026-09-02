# workflow-deep-analyzer - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Solo 'cosa' senza 'perche'' | descrizione piatta | obbligo di rationale | nessuna decisione spiegata | analizza le motivazioni |
| Valutazione assente | nessun giudizio forza/debolezza | sezione valutazione obbligatoria | manca la sezione | aggiungi punti forti/deboli con esempi |
| Modifica originale | file toccato | sola lettura | diff | ripristina |
| Trace mancante | claim senza file:sezione | trace obbligatoria | trace vuota | ancora a file/sezione |
| Confronto principi assente | nessun riferimento a pattern noti | usa knowledge-pack | nessun pattern citato | collega a P/PT/AP rilevanti |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
