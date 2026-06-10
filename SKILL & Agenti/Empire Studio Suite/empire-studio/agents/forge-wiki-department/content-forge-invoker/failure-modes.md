# content-forge-invoker - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Input forge incompleto | forge ignora i frame | includi visual timeline | note senza riferimenti visivi | re-includi le descrizioni frame |
| MKD saltato | nessun MKD | richiedi MKD always | MKD mancante | ri-invoca forzando lo stage MKD |
| Slug collidente | nome gia' usato | slug con fonte+data | conflitto | rinomina lo slug |
| Coverage bassa | atomi persi nelle note | coverage check | atomi non presenti | ri-forgia con enfasi sugli atomi mancanti |
| content-forge assente | skill non trovata | check presenza | errore invocazione | fallback MKD interno |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
