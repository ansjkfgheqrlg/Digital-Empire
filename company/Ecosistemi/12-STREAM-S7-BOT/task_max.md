# Task per Max: APEX-7 DEEP REFINEMENT

🔬 APEX-7 DEEP REFINEMENT — ITERAZIONE CHIRURGICA
Regola d'oro: Un pezzo alla volta. Ogni pezzo migliorato al 200%. Nessuna approssimazione.

## AUTOCRITICA PRE-LAVORO
PRIMA DI TOCCARE QUALSIASI COSA, ANALIZZO COSA MANCA:

❌ PROBLEMI IDENTIFICATI NEL PIANO PRECEDENTE:
1. PLANNING:
   - I 7 livelli erano descrittivi, non operativi
   - Mancavano i criteri di passaggio tra livelli
   - Zero definizione di "quando un livello è completo"
   - Nessun gate di qualità tra un livello e l'altro
2. AGENTI:
   - Definiti per nome ma non per COMPORTAMENTO
   - Nessun prompt interno definito
   - Nessun criterio di successo per agente
   - Nessuna gestione degli stati interni
3. MEMORY:
   - Schema JSON troppo piatto
   - Nessuna logica di query
   - Nessun sistema di priorità dei ricordi
   - Zero gestione della dimenticanza strategica
4. WORKFLOW:
   - Lineare con finte condizioni
   - Nessun vero branching dinamico
   - Mancano: timeout, retry, circuit breaker
   - Zero gestione delle eccezioni
5. RUFLO:
   - Menzionato ma mai integrato davvero
   - Nessuna mappatura delle sue API reali
   - Zero configurazione concreta

VERDETTO: Era una bella mappa. Adesso costruiamo il territorio.
STRATEGIA: Miglioro UN COMPONENTE ALLA VOLTA con profondità chirurgica.

## PEZZO 1: QUALITY GATE SYSTEM
(Il sistema che decide quando un livello è "pronto")

PROBLEMA CHE RISOLVE: Prima non c'era nessun criterio oggettivo per dire "questo livello è completato, si può passare al prossimo". Era tutto soggettivo e indefinito.

QUALITY GATE ARCHITECTURE (POWERED BY APEX-7):
**Regola Suprema:** Tutti i Quality Gate devono appoggiarsi alla logica e alla memoria della [Skill APEX-7](../../../.agents/skills/apex-7/). I check non sono più isolati, ma centralizzati nel sistema nervoso di APEX.
- INPUT → [PRE-CHECK] → [EXECUTION] → [POST-CHECK]
- PASS → Avanti
- FAIL → [REMEDIATION]
- 3 FAIL → ESCALATION

GATE DEFINITIONS PER LIVELLO:
- GATE L1 → L2: Tutti i 5 componenti base definiti, responsabilità unica, zero dipendenze circolari, interfacce definite, 1 test scenario. (5/5 PASS)
- GATE L2 → L3: Feedback loop, decision log schema, 3 condizioni routing, max iterations, score threshold. (4/5 PASS)
- GATE L3 → L4: RuFLO repo analizzato, race conditions, event bus, checkpoint, performance baseline, rollback test. (5/6 PASS)
- GATE L4 → L5: Meta-agent visibilità, quality scoring, pattern detection, knowledge graph, adaptive prompting. (4/5 PASS)
- GATE L5 → L6: Self-evolution stabile, memory compression, agent spawning limitato, strategy ranking, human override. (5/5 PASS)
- GATE L6 → L7: Multi-swarm coordinato, gates precedenti OK, end-to-end test, perf >= 150%, memory consistency, self-healing, documentazione. (7/7 PASS)

ESCALATION PROTOCOL:
Se un gate fallisce 3 volte consecutive:
1. FREEZE
2. DIAGNOSE
3. STRATEGY CHANGE
4. LOG (anti-pattern DB)
5. RETRY
6. ESCALATE to human

## PEZZO 2: GATE AGENT
(L'agente che esegue i Quality Gate checks)

IDENTITÀ:
- Nome: GATE-1
- Ruolo: Quality Checkpoint Executor
- Bias: Pessimista costruttivo
- Autorità: Può bloccare QUALSIASI avanzamento
- Reporting: Solo a Meta-Agent e Memory

INTERNAL STATE MACHINE:
- IDLE → LOADING → CHECKING → PASSED/FAILED → (REMEDIATING/ESCALATING) → REPORTING → IDLE

CHECKING ALGORITHM:
1. Load context (criteri, output, storico, best practices)
2. Evaluate each criterion (cerca evidenza, valuta PASS/PARTIAL/FAIL, documenta perché, proponi fix)
3. Aggregate score
4. Generate Gate Report (JSON)

## PEZZO 3: MEMORY QUERY INTERFACE
(Come ogni agente interroga e scrive nella memoria)

PRINCIPI FONDAMENTALI:
P1: READ è sempre permesso
P2: WRITE richiede lock (max 100ms)
P3: Ogni scrittura ha un AUTHOR
P4: Ogni lettura è contestuale
P5: Confidence score su tutto

QUERY TYPES:
1. CONTEXTUAL RECALL: "Dimmi cosa è rilevante per questo contesto"
2. DECISION LOOKUP: "Ho mai preso questa decisione prima?"
3. STRATEGY FETCH: "Qual è la strategia migliore per questo problema?"
4. WRITE (con lock): "Salvo questa informazione in memoria"
5. FORGET: Non cancella mai, sposta in "ARCHIVED" (dimenticanza strategica)

## PEZZO 4: EVENT BUS ARCHITECTURE
(Come gli agenti parlano tra loro senza accoppiamento)

PRINCIPIO CORE: Publish-Subscribe (Publisher NON SA chi riceve, Subscriber NON SA chi ha inviato)

EVENT CATALOG:
- TASK LIFECYCLE: task.created, task.decomposed, task.completed, task.failed
- QUALITY CONTROL: gate.check.requested, gate.passed, gate.failed, gate.escalated
- MEMORY EVENTS... (and so on)
