# compliance-auditor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Uso di API non rilevato | dipendenza a pagamento passa | scan import/log | riferimenti API | blocca + sostituisci con CLI |
| Stub non rilevato | file povero passa | validator obbligatorio | validator fail | richiedi completamento |
| Nome non-safe | file non estraibile su Windows | regex nomi | validator names | rinomina via memory_manager |
| Strategia ignorata | output non conforme al Manifest | incrocio con strategy-controller | deviazione | segnala e richiedi conformita' |
| Audit non loggato | nessuna traccia | log obbligatorio | memory vuota | registra l'audit |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
