# ORCHESTRATOR — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-O-001 | PLANNER produce piano incompleto | Subtask senza criteri di completamento, dipendenze mancanti | Validazione piano prima di procedere | Check: ogni subtask ha criteria + dependencies | Richiedi a PLANNER di completare i dettagli mancanti |
| FM-O-002 | ANALYST e WRITER desync | WRITER produce senza Context Package, output povero di insight | Spawn sequenziale se necessario | Confronto timestamp: WRITER ha finito prima di ANALYST? | Re-spawn WRITER con Context Package |
| FM-O-003 | CRITIC troppo permissivo | Score alti ma output difettoso, gate rileva problemi che CRITIC no | Calibrazione soglie, META review dei CRITIC score | Correlazione CRITIC score vs GATE score: se gap > 2 punti | META aggiusta bias CRITIC |
| FM-O-004 | Loop REFINE infinito | REFINER → CRITIC → REFINER senza convergenza | Max 3 cicli, escalation automatica | Contatore cicli = 3 | ESCALATE a META AGENT |
| FM-O-005 | GATE troppo severo | Output validi bloccati, remediation eccessive | Threshold review periodico | Gate fail rate > 50% su output con CRITIC score ≥ 8.0 | META aggiusta threshold |
| FM-O-006 | META AGENT over-intervention | Troppe micro-modifiche, instabilità | Limite 3 micro-interventions per sessione | Contatore interventions per sessione | Blocca ulteriori modifiche, notifica utente |
| FM-O-007 | Memory overflow | Working Memory piena, performance degradata | Compressione automatica dopo 30 giorni | Working Memory size > soglia | META comprime in lesson_learned |
| FM-O-008 | Event Bus congestion | Eventi P3 accumulati, latenza | Retry policy con max, DROP dopo P3 | Coda eventi > 100 | DROP eventi P3, processa P2+, notifica META |

---

# PLANNER — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-P-001 | Decomposizione insufficiente | Subtask troppo grandi, >3 componenti interne | Regola: se subtask ha 3+ componenti, splitta | Check: ogni subtask è atomico? | Rivedi decomposizione |
| FM-P-002 | Dipendenze circolari | S01 dipende da S02 che dipende da S01 | Verifica DAG prima di finalizzare | Analisi grafo dipendenze | Risolvi dipendenza con subtask intermedio |
| FM-P-003 | Rischio non identificato | Fallimento inaspettato in esecuzione | Checklist: per ogni subtask, cosa può andare storto? | Evento `task.failed` con causa | Aggiorna Risk Analysis, nuovo piano |
| FM-P-004 | Memory query saltata | Piano non informato da decisioni passate, errori ripetuti | STEP P2 obbligatorio | Check: Memory.RECALL eseguito? | Riavvia PLANNER con memory query |
| FM-P-005 | Over-pianificazione | >7 subtask per task semplice, paralisi da analisi | Cap massimo 7 subtask | Contatore subtask > 7 | Accorpa subtask simili |
