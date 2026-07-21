# Failure Modes — chief-forge
| Fallimento | Sintomo | Prevenzione | Rilevamento | Recupero |
|---|---|---|---|---|
| Scope creep | DoD superata | DoD congelata (ADR-EST-005) | build oltre il file list | `decision` richiesta o revert |
| Riscrivere motore esistente | codice nuovo dove esiste wrap | regola 2 system prompt | review path | wrap + archivia il nuovo |
| Overload Gael | task EOD non chiusi | sequenza rigida P3 | dashboard h19:00 | slittamento dichiarato S5→S4→S6→S3 |
| Segreto in file | chiave committata | .env + lint mentale | grep pre-commit | rotazione chiave + error in memoria |
| Gate "quasi verde" | status ambiguo | regola 3 WF-MASTER | audit gate | marca 🔴 + kill-criterio |
