# Failure Modes — qa-extraction-verifier

| # | Rischio del gate stesso | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Falso PASS per schema saltato | jsonschema non installato | nota esplicita nell'issue, non conta come PASS silenzioso |
| 2 | Foto "dichiarate" ma non su disco | gallery vuota a valle | controllo esistenza file per ogni `local_path` |
| 3 | Prezzo 0 o stringa | pricing impossibile a valle | check `isinstance` + `> 0` |
| 4 | `description_de` presente ma spazzatura | testo inutile | non giudica la qualità (compito di Gate B), solo presenza |
| 5 | Path relativi errati | file non trovati falsamente | risolve sempre da `ctx.dir` |

## Limite noto
Gate A verifica **presenza e integrità strutturale**, non la correttezza semantica dei valori
(quello è compito dei gate B/C/D). Non deve diventare un gate "tuttofare".
