# Failure modes — op-parser

| Failure | Sintomo | Prevenzione | Rilevazione | Recupero |
|---|---|---|---|---|
| Prezzo non parsato | `price_listed_eur=null` | JSON-LD offers + fallback `price_text` + `_to_float` | Gate A / S4 | warning; verifica annuncio |
| Numero migliaia sbagliato | 28.900 → 28.9 | `_to_float` gestione `.`/`,` DE | test unit | correggi `_to_float`; ricontrolla |
| Enum DE non mappata | valore tedesco in `fuel/gearbox` | mappe + fallback valore originale | ispezione | estendi mappa (non bloccante) |
| Schema non valido | `_schema_errors` non vuoto | tipi corretti, `additionalProperties:false` | `validate_against_schema` | correggi campo; se critico stop |
| Marca/modello vuoti | JSON-LD e DOM poveri | fallback dal titolo | warning | migliora scraper/label |
| Potenza kW/CV assente | `power_*` null | regex "Leistung" + derivazione | ispezione | ok se davvero assente (null) |
| equipment tradotto per errore | testo IT in `equipment_de` | confine: parser non traduce | review | rimuovi traduzione (spetta a S3) |
