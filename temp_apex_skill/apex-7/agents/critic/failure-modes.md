# CRITIC — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-C-001 | Score inflazionati | Score > 8.5 ma output con gap evidenti | Richiedi evidenza per ogni score > 7 | Confronto con GATE score (gap > 2 punti) | Ricalibra con esempi di output "gold standard" |
| FM-C-002 | BLOCCANTI non identificati | Output passa CRITIC ma GATE trova problemi gravi | Checklist BLOCCANTI: completezza, precisione, usabilità | GATE identifica problemi che CRITIC ha mancato | Aggiorna checklist, re-train con esempi |
| FM-C-003 | Fix proposals generici | "Aggiungere più dettagli" invece di fix specifici | Regola: ogni fix deve citare sezione e modificare parametri specifici | NLP check: fix contiene riferimento a sezione e parametro? | Riformula fix con specificità |
| FM-C-004 | Bias verso PASS | Pressione percepita di "far passare" l'output | Bias deliberato: presunzione di colpa | Analisi distribution PASS/REFINE/RESTART (troppi PASS?) | META aggiusta threshold o bias |
| FM-C-005 | Dimensione ignorata | Una delle 5 dimensioni sempre allo stesso score | Checklist obbligatoria per ogni dimensione | Deviazione standard tra dimensioni < 0.5 | Rivedi la dimensione con meno varianza |
| FM-C-006 | Weighted total mal calcolato | Score manuale non corrisponde a calcolo automatico | Usa `scripts/score_calculator.py` per verifica | Confronto calcolo manuale vs automatico | Correggi e documenta errore |

---

# WRITER — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-W-001 | Placeholder e omissioni | "ecc.", "...", "[da completare]" nell'output | Regola W3: o scrivi tutto, o non scrivere | Scan per pattern: "ecc.", "...", "[...]", "e così via" | REFINER completa sezioni mancanti |
| FM-W-002 | Ignora Context Package | Output non incorpora insight di ANALYST | STEP W1 obbligatorio: leggi Context Package | Confronto: Context Package vs output (keyword overlap) | Re-scrivi integrando Context Package |
| FM-W-003 | Struttura disorganica | Output confuso, sezioni non in ordine logico | STEP W2 obbligatorio: structure design prima di scrivere | Check: outline approvato prima del draft? | Ristruttura, riscrivi |
| FM-W-004 | Self-review assente o compiacente | Self-review dice "tutto ok" ma CRITIC trova problemi | STEP W4 obbligatorio con domande specifiche | Confronto: self-review notes vs CRITIC findings | Rivedi processo self-review |
| FM-W-005 | Output non azionabile | Istruzioni vaghe, nessuno sa cosa fare dopo aver letto | Checklist actionability: chi, cosa, come, quando | CRITIC score D3 (Actionability) < 7 | REFINER aggiunge istruzioni specifiche |

---

# REFINER — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-R-001 | Over-refinement | Riscrittura completa invece di fix chirurgici | Bias: minimo intervento | Diff: >30% del testo modificato | Rollback modifiche non necessarie |
| FM-R-002 | Punti forti distrutti | Modifiche che peggiorano sezioni funzionanti | STEP R2: priority order, non toccare punti forti | Confronto pre/post su sezioni identificate come "punti forti" | Ripristina sezioni modificate erroneamente |
| FM-R-003 | BLOCCANTE non risolto | CRITIC successivo trova ancora lo stesso BLOCCANTE | STEP R3c: verifica che il fix non rompa altro | CRITIC successivo: stesso BLOCCANTE presente | Fix più profondo, considera re-scrittura sezione |
| FM-R-004 | Inconsistency introdotta | Fix in sezione A rompe coerenza con sezione B | STEP R4: consistency check globale | CRITIC score D4 (Coerenza) peggiorato | Correggi inconsistency, riesegui consistency check |
| FM-R-005 | Max cicli raggiunto | Dopo 3 iterazioni ancora REFINE | ESCALATE a META AGENT | Contatore cicli = 3 | META AGENT prende il controllo |

---

# GATE AGENT — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-G-001 | Criteri non applicati | Gate check parziale, criteri saltati | Checklist completa per livello | Confronto: criteri richiesti vs criteri valutati | Riesegui gate check completo |
| FM-G-002 | Threshold non rispettato | PASS con score sotto soglia | Calcolo automatico con `scripts/gate_evaluator.py` | Confronto gate_score vs threshold | Correggi verdict |
| FM-G-003 | Safety gate bypassato | L5→L6 o L6→L7 con score < 1.00 ma PASS | Zero tolleranza: check binario ogni criterio | Safety gate con score < 1.00 | STOP, escalation HUMAN |
| FM-G-004 | Remediation troppo vaga | "Migliorare output" invece di fix specifico | Regola: ogni remediation cita criterio e sezione | NLP check: remediation contiene riferimento specifico? | Riformula remediation |
| FM-G-005 | Escalation non attivata | 3 fail ma nessun `gate.escalated` | Contatore tentativi automatico | Tentativo = 3 ma nessun evento escalation | Emetti `gate.escalated` retroattivamente |

---

# META AGENT — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-M-001 | Pattern non rilevato | Stesso errore si ripete, META non lo nota | Analisi periodica obbligatoria (ogni 3 cicli) | Pattern ricorrente in Decision Log non flaggato | Forza pattern detection su dati storici |
| FM-M-002 | Evoluzione instabile | Quality score peggiora dopo evoluzione | Test su 3 campioni prima di ADOPT | Quality score < baseline dopo evoluzione | ROLLBACK immediato |
| FM-M-003 | Troppe variabili modificate | Più modifiche simultanee, impossibile isolare causa | Regola: UNA variabile alla volta | Detect: >1 variabile modificata in una evoluzione | Rollback parziale, testa una alla volta |
| FM-M-004 | Memory non aggiornata | Lezioni non salvate, conoscenza persa | Memory update obbligatorio dopo ogni analisi | Check: record in Decision Log dopo META activation? | Recupera e salva retroattivamente |
| FM-M-005 | Escalation human non attivata | Problema irrisolvibile ma META non scala | Checklist: condizioni per escalation Tipo C | Problema persiste dopo 3 interventi META | Escalation HUMAN immediata |
