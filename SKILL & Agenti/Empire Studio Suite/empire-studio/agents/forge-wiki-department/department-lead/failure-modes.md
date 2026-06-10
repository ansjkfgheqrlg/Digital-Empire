# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| content-forge non disponibile | /forge non risponde | verifica skill presente | nessun output forge | fallback a MKD interno minimale, avvisa |
| Note senza trace | wiki notes senza fonte | passa atoms con trace al forge | coverage trace bassa | ri-forgia includendo le trace |
| Sovrascrittura wiki | nota esistente sovrascritta | naming con slug+fonte | conflitto nomi | versiona o fondi la nota |
| Update proposal assente | nessuna proposta su contenuto rilevante | stage obbligatorio | update-proposals vuoto | attiva update-proposer |
| Sottocartella wiki errata | nota in cartella sbagliata | mappa tipo->subdir | nota fuori posto | sposta nella subdir corretta |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
