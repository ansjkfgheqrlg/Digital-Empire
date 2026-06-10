# meta-strategy-manager - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Registry incoerente | strategie in conflitto | validazione coerenza | contraddizioni | riconcilia |
| Duplicati | strategie ridondanti | dedup | strategie simili | fondi |
| Proposte non integrate | improver ignorato | ciclo di integrazione | proposte pendenti | integra o motiva il rifiuto |
| Versioning rotto | versioni confuse | schema vN rigoroso | versioni incoerenti | riallinea il versioning |
| Gap non colmati | tipi senza strategia | monitoraggio gap | richieste senza match | crea nuova strategia |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
