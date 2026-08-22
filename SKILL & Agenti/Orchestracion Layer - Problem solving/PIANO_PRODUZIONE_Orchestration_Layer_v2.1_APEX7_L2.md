# Orchestration Layer Architect v2.1 — Piano di produzione APEX-7 · Livello 2

**Data:** 11 agosto 2026  
**Ambito:** integrazione del prompt “APEX-7 Deep Refinement” nell'Orchestration Layer Architect  
**Runtime vincolante:** Python 3.11+ con `asyncio` puro; stato durevole esterno  
**Artefatto operativo associato:** [`SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md`](SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md)  
**Audit di baseline:** [`AUDIT_Orchestration_Layer_Architect_v2.0.md`](AUDIT_Orchestration_Layer_Architect_v2.0.md)  
**Piano radice:** [`PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7.md`](PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7.md)  
**Piano genitore:** [`PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7_L1.md`](PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7_L1.md)  
**Livello:** **L2/7 — dipendenze eseguibili, critical path e parallelismo realistico**  
**Regola di versione:** questo file eredita integralmente L1 e introduce un solo miglioramento tematico addizionale.

---

## 0. Verdetto

APEX-7 contiene idee riutilizzabili, ma **non può essere incorporato letteralmente**. La versione fornita confonde design, runtime, governance, giudizio LLM e garanzie distribuite; inoltre assegna punteggi e percentuali di completamento senza evidenza eseguibile.

L'integrazione v2.1 conserva la disciplina centrale:

> **selezionare un componente, congelare la baseline, raffinarlo in profondità, provarlo localmente e contro regressione, promuoverlo solo con evidenza.**

Corregge però i punti pericolosi:

- un punteggio medio non compensa un fallimento critico;
- il Gate Agent non è l'unica autorità;
- la memoria non usa un lock globale da 100 ms come garanzia distribuita;
- il bus non promette genericamente exactly-once;
- le API RuFLO non verificate non entrano nell'architettura;
- il self-evolution non muta direttamente la produzione;
- `asyncio` resta il motore di concorrenza, PostgreSQL la fonte di verità durevole.

### Stato reale dopo questa integrazione

| Area | Stato |
|---|---|
| System prompt integrato | **DESIGN CANDIDATE** |
| Architettura target | **DEFINITA, NON IMPLEMENTATA** |
| Runtime durevole | **NON PROVATO** |
| Builder multi-agente | **NON PROVATO** |
| Quality gates eseguibili | **NON PROVATI** |
| Self-evolution controllato | **NON IMPLEMENTATO** |
| RuFLO adapter | **OPZIONALE, DA VALIDARE** |
| Production readiness | **BLOCKED** |
| Impegno su data/costo | **NON AUTORIZZATO: input critici mancanti** |

I valori “55%”, “8.5/10”, “8.7/10”, “9.0/10” e “9.2/10” del prompt APEX-7 sono **rimossi dal processo decisionale**. Non costituiscono metriche, test o prova di readiness.

### Registro del Livello 1 — unico miglioramento introdotto

**Tema:** rendere falsificabili effort, capacità, calendario e condizioni necessarie per impegnare una data.  
**Non modificato in L1:** architettura logica, contratti, gate, rollout e disposizione RuFLO del piano genitore.  
**Perché è il primo intervento:** un piano tecnicamente ricco ma sostenuto da una durata non difendibile è una promessa, non un piano.

#### 1. Baseline brutalmente sincera

Oggi esistono specifiche e audit, non un prodotto. Non esiste ancora evidenza nel workspace di:

- repository runtime compilabile;
- schema PostgreSQL migrato e testato;
- worker con lease/CAS e crash recovery;
- adapter di produzione qualificati;
- benchmark rappresentativo;
- staging, on-call o restore drill;
- team nominato e allocato;
- budget approvato;
- RuFLO clonato, pinato, ispezionato o sottoposto a POC.

Di conseguenza:

1. una data di produzione **non è impegnabile**;
2. la stima precedente di 20–24 settimane per il G7 completo è troppo ottimistica rispetto all'evidenza disponibile;
3. “molti agenti” non è un acceleratore dimostrato: aumenta coordinamento, costo, conflitti, superficie d'attacco e non-determinismo;
4. `gh repo clone ruvnet/ruflo` scarica sorgenti: non attiva né qualifica uno swarm e non prova compatibilità, sicurezza o durabilità;
5. il primo collo di bottiglia non è il numero di agenti, ma la catena state → claim → side effect → transition → recovery.

#### 2. Classificazione delle basi di stima

| Voce | Stato L1 | Conseguenza |
|---|---|---|
| 43 finding | **FATTO:** 43 `OPEN`, inclusi 15 P0 | nessuna readiness; effort minimo significativo |
| Runtime esistente | **NON PROVATO** | stima trattata come greenfield |
| Workload e side effect | **IGNOTI** | performance, idempotenza e rischio non calibrabili |
| Team e seniority | **IGNOTI** | capacità nominale non utilizzabile per commitment |
| Infrastruttura CI/CD, DB, broker, OTel | **IGNOTA** | make/buy e lead time non quantificabili |
| Vincoli compliance/data residency | **IGNOTI** | security lead time potenzialmente sottostimato |
| RuFLO | **OPZIONALE, NON QUALIFICATO** | zero credito di accelerazione nel forecast |
| F6 evolution | **FUORI CRITICAL PATH** | nessun credito per il go-live core |

Un ignoto critical non viene sostituito con un valore favorevole. Si usa un intervallo conservativo o si blocca il commitment.

#### 3. Calcolatore di realismo del forecast

Questo calcolatore stima calendario; **non** calcola production readiness e non può rendere verde un gate.

```text
C_eff = FTE_nominali × fattore_focus
T_capacity = effort_person_week / C_eff
T_forecast = max(T_capacity, critical_path_floor) + lead_time_esterno
```

Regole L1:

- `fattore_focus = 0,60–0,72`: il resto copre coordinamento, review, incidenti, ferie, hiring e supporto;
- effort core G1–G7, esclusa F6: **170 PW P50; 220 PW P80**;
- `critical_path_floor = 30 settimane`: alcuni test, soak, review e migrazioni non si comprimono aggiungendo persone;
- `lead_time_esterno = 4–8 settimane`, sovrapponibile solo in parte, per security, ambienti, procurement e approvazioni;
- se workload, team committed o piattaforma esistente restano ignoti, il forecast è una **range di pianificazione**, non una data.

| Scenario | Capacità effettiva usata | Forecast G7 | Giudizio L1 |
|---|---:|---:|---|
| 4–6 FTE nominali, media 5, focus 0,65 | 3,25 PW/settimana | **56–76 settimane** | realistico ma lento; alto rischio di dipendenze su singoli |
| 6–8 FTE nominali, media 7, focus 0,70 | 4,90 PW/settimana | **39–53 settimane** | scenario raccomandato minimo per full scope |
| 9–11 FTE esperti, piattaforma già matura | 7,2–8,0 PW/settimana | **34–38 settimane** | possibile solo dopo prova di baseline e forte leadership |
| 20–24 settimane | capacità e critical path incompatibili con gli ignoti attuali | **NON CREDIBILE per G7 completo** | ammissibile solo riducendo scope a foundation/durable-core RC, non produzione piena |

I valori non devono essere sommati meccanicamente alle durate di fase: rappresentano il forecast integrato con capacità, parallelismo limitato e attese esterne.

#### 4. Effort envelope per fase

| Fase | Effort P50–P80 | Calendario non comprimibile dominante |
|---|---:|---|
| F0 | 12–18 PW | ownership, threat model, workload e decisioni |
| F1 | 18–26 PW | bootstrap, contratti, CI, schema e migrazioni |
| F2 | 38–52 PW | correttezza concorrente, crash windows, restore |
| F3 | 34–48 PW | auth, eventing, data lifecycle, resilienza, telemetry |
| F4 | 28–40 PW | harness, registry, sandbox, gate ed eval deterministici |
| F5 | 22–30 PW | benchmark, chaos, staging soak e runbook drill |
| F7 | 18–26 PW | canary, approval, osservazione e rollback readiness |
| **Core totale** | **170–240 PW** | il planning calculator usa 170 P50 e 220 P80; 240 è coda di rischio |
| F6 opzionale | 16–28 PW separati | nessun credito sul critical path core |

#### 5. Regola anti-falsa-accelerazione dello swarm

Prima del G4, il forecast assegna a RuFLO e allo swarm **accelerazione = 0**. Dopo un POC, un beneficio può essere contabilizzato soltanto se:

- è misurato sul benchmark del progetto, non su demo;
- include costo di orchestrazione, review e rework;
- non aumenta false acceptance, incidenti di sandbox o provenance gap;
- mantiene Native Asyncio Harness come fallback;
- il limite di agenti cresce per esperimento: `2 → 4 → 8`; nessun salto a “tantissimi agenti” senza curve di throughput e qualità;
- il numero massimo deriva dal punto in cui il throughput marginale netto diventa nullo, non da una capacità dichiarata dal framework.

#### 6. Condizioni per rendere impegnabile il forecast

Il forecast può passare da range a commitment solo quando F0 produce:

- workload catalog con classi di rischio e volumi;
- inventory di repository, infrastruttura e servizi riusabili;
- team nominato con allocazione settimanale e skill coverage;
- make/buy decision per DB, broker, secrets, OTel e CI/CD;
- compliance/security lead time;
- dipendenze esterne con owner e date;
- stima bottom-up rivista per ogni epic;
- contingency esplicita e owner del rischio.

**Gate L1:** `PASS` documentale perché il piano espone calcolo, assunzioni e range; **BLOCKED per commitment** finché gli otto input sopra non esistono.

#### 7. Registro critico pubblico

| Affermazione | Obiezione più forte | Decisione L1 | Condizione che la smentisce |
|---|---|---|---|
| Più agenti accelerano | coordinamento e rework possono superare il lavoro utile | nessun credito prima di benchmark | speedup netto ripetibile con guardrail invariati |
| 20–24 settimane bastano | 15 P0 e durable recovery richiedono lavoro seriale e soak | rifiutata per G7 completo | baseline matura provata + scope ridotto o capacità eccezionale |
| RuFLO abilita la produzione | clone e swarm non sono runtime durevole né release control | adapter opzionale dopo G4 | POC dimostra contratti, isolamento, export e fallback |
| 4–6 persone sono sufficienti | forse sì, ma calendario e key-person risk crescono | 56–76 settimane come range prudente | team/prodotto esistente riducono effort misurato |

#### 8. Autocritica del Livello 1

- L'effort è ancora top-down: senza repo e workload può sbagliare anche del 30–50%.
- I fattori focus sono ipotesi, non timesheet del team reale.
- La stima non include un programma di certificazione regolatoria specifico.
- Il forecast non autorizza assunzioni, budget o release.
- Il Livello 1 migliora l'onestà del calendario, ma non riduce nessuno dei 43 finding.

**Backtrack L1:** se il repository o la piattaforma esistente mostrano evidenza sostanziale, ricalcolare effort; se emergono side effect regolati o safety-critical, ampliare la coda P80 e il lead time esterno.

### Registro del Livello 2 — unico miglioramento introdotto

**Tema:** sostituire la sequenza di macro-fasi con un grafo di dipendenze eseguibile, WIP limitato e critical path calcolato.  
**Non modificato in L2:** effort envelope L1, architettura target, contratti, gate, SLO, rollout e ruolo opzionale di RuFLO.  
**Perché serve:** L1 stimava capacità e incertezza, ma non dimostrava quali attività potessero davvero sovrapporsi. Senza dipendenze esplicite, il parallelismo viene quasi sempre sovrastimato.

#### 1. Autopsia critica del piano L1

L1 ha migliorato l'onestà della stima, ma conserva quattro debolezze:

1. il critical path `F0 → F1 → F2 → F3 → F4 → F5 → F7` è troppo grossolano;
2. F4 dichiara dipendenza da F1 e parzialmente da F2, mentre il diagramma lo colloca interamente dopo F3;
3. security, data lifecycle e sandbox sono prerequisiti trasversali, non un blocco da completare una sola volta;
4. la formula di capacità non include abbastanza costo di handoff, attese di evidence review e rework tra stream.

Conclusione: le range L1 restano utili come capacity envelope, ma sono insufficienti per il calendario. L2 le sostituisce con la previsione guidata dal grafo.

#### 2. Tipi di dipendenza vincolanti

| Tipo | Significato | Regola di avvio |
|---|---|---|
| `HARD` | contratto, schema o funzione necessaria | il predecessore deve avere exit criteria verdi |
| `EVIDENCE` | prova richiesta per non costruire su un'assunzione | evidence ref fresca e legata all'artifact hash |
| `AUTHORITY` | decisione o approvazione non delegabile | owner nominato e decision record firmato |
| `ENVIRONMENT` | ambiente, account, secret, DB, broker o capacità | smoke test dell'ambiente completato |

“Quasi finito”, branch locale, mock non rappresentativo o approvazione verbale non soddisfano una dipendenza. Un package può iniziare in discovery, ma non entrare in build/promozione senza i predecessori richiesti.

#### 3. Work-package DAG del core

Le durate sono intervalli calendario per lo scenario di riferimento **6–8 FTE nominali**, con lane riservate e WIP massimo. Non sono commitment.

| WP | Contenuto | Durata | Predecessori vincolanti | Exit evidence |
|---|---|---:|---|---|
| **W0** | workload, authority, threat model, ADR, RACI | 4–5 sett. | nessuno | catalogo workload, risk class, owner, decisioni firmate |
| **W1** | package, CI, strict contracts, schema/migration baseline | 4–6 sett. | W0 `HARD/AUTHORITY` | build riproducibile, schema compatibility, bootstrap fail-fast |
| **W2** | state machine, PostgreSQL repository, CAS e atomic claim | 6–8 sett. | W1 `HARD/ENVIRONMENT` | state/concurrency suite verde |
| **W3** | lease, idempotency, crash recovery, resume, reconciliation | 6–8 sett. | W2 `HARD/EVIDENCE` | crash-window, restore e unknown-outcome suite verdi |
| **W4** | authz, tenant/data controls, retention, secret/log policy | 5–7 sett. | W0 + W1 `HARD/AUTHORITY` | adversarial isolation e leakage suite verdi |
| **W5** | inbox/outbox, event compatibility, resilienza e OTel | 6–9 sett. | W2 + W4 `HARD` | replay, broker outage, redaction e trace propagation verdi |
| **W6** | agent/prompt registry, native harness, artifact/evidence store | 5–7 sett. | W1 `HARD` | envelope/schema/budget/provenance suite verde |
| **W7** | Gate Engine, semantic evaluator, sandbox e durable agent jobs | 6–8 sett. | W3 + W4 + W6 `HARD/EVIDENCE` | false-pass, injection, budget/cycle e recovery suite verdi |
| **W8** | hardening integrato runtime/control plane | 4–6 sett. | W5 + W7 `HARD` | end-to-end fault matrix senza blocker |
| **W9** | eval, capacity, chaos, seven-day soak e runbook drills | 7–10 sett. | W8 `HARD/ENVIRONMENT` | G5 evidence bundle e staging sign-off |
| **W10** | release candidate, restore/rollback e approval pack | 4–6 sett. | W9 `EVIDENCE/AUTHORITY` | signed manifest, rollback drill, on-call readiness |
| **W11** | canary progressivo, osservazione e closure | 4–6 sett. | W10 `HARD/AUTHORITY` | G7, post-deploy verification e closure firmata |
| **WX** | evolution/RuFLO POC | 4–7 sett. | W7; eval harness disponibile | decisione separata `ADOPT_SHADOW/DEFER/REJECT` |

`WX` è fuori dal critical path e non può sottrarre owner critici a W8–W11. Se usa le stesse persone senza capacità aggiuntiva, viene rinviato.

#### 4. Grafo e parallelismo ammesso

```text
W0 → W1 → W2 → W3 ───────────────┐
      │     │                     │
      │     └──────→ W5 ─────────┤
      ├──→ W4 ──────↑       ┌────┴→ W8 → W9 → W10 → W11
      └──→ W6 ─────────→ W7 ┘
                         └────→ WX   # opzionale, capacità separata
```

Interpretazione realistica:

- W4 e W6 possono sovrapporsi a W2/W3, ma competono per security, contracts e review;
- W5 non parte realmente prima che W2 stabilizzi transazioni e W4 definisca data/security policy;
- W7 non può dichiarare job “durevoli” prima delle prove W3;
- W8 è un merge gate tecnico, non una formalità amministrativa;
- W9 include tempo di osservazione: più agenti non comprimono un soak di sette giorni;
- W10/W11 dipendono da autorità e finestre operative esterne al team di sviluppo.

#### 5. Critical Path Method

Per il grafo L2, il percorso dominante è:

```text
W0 → W1 → W2 → W3 → W7 → W8 → W9 → W10 → W11
```

Calcolo sulla range dichiarata:

```text
lower = 4 + 4 + 6 + 6 + 6 + 4 + 7 + 4 + 4 = 45 settimane
upper = 5 + 6 + 8 + 8 + 8 + 6 + 10 + 6 + 6 = 63 settimane
```

W4 e W6 non risultano sul percorso aritmetico dominante soltanto se ricevono capacità dedicata. Se security o platform sono condivisi part-time, possono diventare il critical path reale.

#### 6. Correzione del forecast L1

Per scalare la capacità senza fingere che tutto sia parallelizzabile:

```text
T(C) = max(T_ref × (serial_fraction + parallel_fraction × C_ref / C), fast_track_floor)
serial_fraction = 0,30
parallel_fraction = 0,70
C_ref = 4,90 PW/settimana
fast_track_floor = 36 settimane
```

La frazione seriale include review, migration ordering, fault integration, soak, approval e canary. Il modello è diagnostico, non un commitment.

| Scenario | Forecast L1 | Forecast L2 | Verdetto critico |
|---|---:|---:|---|
| 4–6 FTE nominali | 56–76 sett. | **61–85 sett.** | L1 sottostimava queueing e handoff |
| 6–8 FTE nominali | 39–53 sett. | **45–63 sett.** | nuova baseline raccomandata |
| 9–11 FTE esperti + piattaforma matura | 34–38 sett. | **36–47 sett.** | rendimenti decrescenti e floor seriale |
| 20–24 settimane | non credibile | **rifiutato** | impossibile per full G7 senza eliminare scope o prove |

L2 è più lento di L1 perché espone lavoro che L1 aggregava: integration hardening, evidence queue, restore/rollback pack e canary closure.

#### 7. WIP e allocazione minima

Sono consentiti al massimo **tre stream maggiori** contemporanei e una sola promozione safety-critical per change set.

| Lane | Capacità minima nello scenario 6–8 FTE | Non può essere azzerata durante |
|---|---:|---|
| Runtime/Data | 2,0–2,5 FTE | W2–W5, W8 |
| Control Plane/Eval | 1,5–2,0 FTE | W6–W9 |
| Platform/SRE | 1,0–1,5 FTE | W1–W5, W8–W11 |
| Security/Data governance | 0,8–1,0 FTE | W0, W4, W7–W11 |
| QA/Eval | 0,8–1,0 FTE | da W2 a W11 |
| Product/Domain authority | 0,3–0,5 FTE | W0, W9–W11 |

Le allocazioni si sovrappongono per competenza, non si sommano come persone automaticamente disponibili. Se una persona copre due lane, il piano registra il conflitto e riduce il WIP.

#### 8. Regole anti-parallelismo fittizio

1. Nessun package apre più del 20% del lavoro downstream prima dell'exit evidence del predecessore.
2. Un blocker `HARD` congela build/promozione downstream; non viene nascosto come “rischio accettato”.
3. Rework superiore al 15% dell'effort settimanale per due settimane forza riduzione WIP.
4. Review queue p95 oltre tre giorni rende security/platform un collo di bottiglia esplicito.
5. Una modifica a state/event/security contract invalida le evidence downstream collegate all'hash precedente.
6. F6/RuFLO non usa capacità del critical path senza una decisione di replan approvata.
7. Non si aumenta il numero di agenti per compensare una dipendenza umana, ambientale o di autorità.

#### 9. Registro critico pubblico L2

| Affermazione ereditata | Obiezione più forte | Decisione L2 | Condizione di smentita |
|---|---|---|---|
| F3 precede interamente F4 | registry/harness possono iniziare dopo F1 | sostituita con DAG W4–W7 | dependency evidence mostra un vincolo più forte |
| 6–8 FTE: 39–53 settimane | capacity math non include abbastanza handoff/rework | corretta a 45–63 | dati di throughput reali riducono le durate WP |
| Più persone comprimono il piano | 30% del percorso è seriale o time-bound | rendimenti decrescenti espliciti | automazione provata riduce la frazione seriale |
| RuFLO può correre in parallelo | usa gli stessi owner di gate/security/eval | solo con capacità separata | staffing aggiuntivo nominato e POC isolato |

#### 10. Autocritica del Livello 2

- Le durate WP sono ancora stime top-down: il DAG è più onesto, non ancora calibrato da throughput reale.
- La frazione seriale 0,30 è un'ipotesi; può crescere con compliance o dipendenze aziendali.
- Il grafo non modella festività, hiring, procurement specifico o incidenti operativi.
- W4 security potrebbe diventare dominante; il CPM statico non cattura bene resource contention.
- L2 non chiude finding e non rende eseguibile il runtime.

**Gate L2:** struttura delle dipendenze e aritmetica CPM verificabili; **BLOCKED per commitment** finché F0 non conferma workload, persone, ambienti e owner.  
**Backtrack L2:** se una dependency review trova un predecessore mancante o una lane condivisa supera il 75% di allocazione, aggiornare DAG, CPM e forecast prima di iniziare il package interessato.

---

## 1. Integrazione dei sette componenti APEX-7

| Componente APEX-7 | Idea riusabile | Ridisegno obbligatorio | Elemento rifiutato |
|---|---|---|---|
| **1. Quality Gate System** | Gate espliciti, criteri, evidenza e remediation | Policy-as-code versionata; criteri blocking/non-blocking; `NOT_PROVEN`; waiver con owner/scadenza; artifact hash | Media ponderata che rende verde un rosso safety-critical; “dubbio=FAIL” senza distinguere prova mancante da fallimento |
| **2. Gate Agent** | Revisore dedicato e stato di valutazione | Split tra `GatePolicyEngine` deterministico e `GateEvaluatorAgent` semantico; remediation separata; timeout, budget, escalation | Autorità assoluta del solo LLM; auto-remediation con diritto di promozione; retry sullo stesso artefatto |
| **3. Memory Query Interface** | Query cross-agente, semantica, deduplica, pattern | PostgreSQL/MVCC; ACL tenant; provenance; retention/erasure; hybrid search; poisoning defense; vector index opzionale | Lock globale 100 ms come garanzia; “mai cancellare”; consistenza forte dichiarata senza protocollo |
| **4. Event Bus** | Envelope, catalogo eventi, correlation e retry | Outbox/inbox transazionali; at-least-once; consumer idempotenti; schema registry; ordering per aggregate; quarantine sicura | Exactly-once generico; payload sensibili duplicati; ordinamento globale implicito |
| **5. RuFLO Map** | Possibile meta-harness per coordinamento agenti | Adapter opzionale CLI/MCP, pin esatto, sandbox, contract test, fallback e exit strategy | `ruflo.AgentRuntime`, `WorkflowEngine`, `Router`, plugin Python e YAML APEX non verificati come API ufficiali |
| **6. Agent Prompt Templates** | Struttura identity/context/task/constraints/output/success | Prompt registry con hash/versione/owner; tool grants; input non fidato delimitato; schema output; budget; eval suite | Prompt come controllo sufficiente; output LLM trattato come trusted; un unico meta-agent onnipotente |
| **7. Self-Evolution Engine** | Osservare metriche, proporre cambiamenti, confrontare baseline | Observe → propose → offline eval → adversarial eval → shadow → approval → canary → monitor → rollback | Mutazione diretta della configurazione live; auto-approvazione; soglia “+5%” senza significatività/guardrail |

### Mappatura dei sette prompt-agente APEX

| Ruolo originale | Ruolo v2.1 | Correzione |
|---|---|---|
| Planner Agent | `PlanCoordinator` | pianifica e ordina; non approva policy o release |
| Writer Agent | `PythonBuilder` + `ADR/DocumentationWriter` | codice e documentazione hanno contratti, test e provenance distinti |
| Analyst Agent | `FlowArchitect` + `TestScenarioDesigner` | analisi architetturale separata dalla costruzione e dai test |
| Critic Agent | `SemanticReviewer` | critica semantica; non sovrascrive verifiche deterministiche |
| Refiner Agent | remediation worker versionato | modifica un componente per ciclo e produce un nuovo artifact hash |
| Gate Agent | `GateEvaluatorAgent` + `GatePolicyEngine` | giudizio LLM separato dall'autorità deterministica |
| Meta-Agent | `RequestClassifier` + `PlanCoordinator` + `PolicyDecisionPoint` + `FinalAssembler` | il God Agent viene eliminato e l'autorità distribuita |

### Decisione complessiva

- **Conservare:** disciplina di refinement, gate progressivi, registry agenti/prompt, event catalog, memoria interrogabile, esperimenti.
- **Riscrivere:** semantica dei gate, Gate Agent, consistenza della memoria, event delivery, evoluzione.
- **Isolare:** RuFLO dietro un port opzionale.
- **Rifiutare:** punteggi autoassegnati, garanzie impossibili, API inventate/non provate e modifiche autonome alla produzione.

---

## 2. Decisioni architetturali vincolanti

### AD-01 — Tre piani distinti

```text
Builder Control Plane
    usa NERVE-SOLVE per framing/design
    produce artefatti/policy/evidenza
                │
                ▼
        Release Control
                │
                ▼
Durable Workflow Runtime
    esegue solo versioni approvate
```

- **NERVE-SOLVE:** controllo cognitivo del problem solving.
- **Builder Control Plane:** genera e verifica.
- **Workflow Runtime:** esegue e recupera.

Nessun meta-agent possiede tutte e tre le autorità.

### AD-02 — `asyncio` puro, durabilità esterna

`asyncio` governa task, concorrenza e I/O nel worker. PostgreSQL governa identità, workflow, step, lease, idempotenza, inbox, outbox, audit e recovery. Redis può ottimizzare, ma non è la fonte autorevole.

### AD-03 — Garanzia realistica

```text
at-least-once execution/delivery
+ stable idempotency key
+ atomic local transition
+ downstream deduplication where available
+ reconciliation for ambiguous outcomes
```

### AD-04 — Gate deterministico sopra giudizio semantico

Il Gate Evaluator LLM produce findings; il Gate Policy Engine calcola l'esito su report firmati. Un reviewer semantico non può annullare un failure deterministico bloccante.

### AD-05 — Safety non compensabile

Perdita dati, side effect duplicati ad alto impatto, auth/tenant isolation, secret/PII leakage, recovery e rollback non possono essere mediati con criteri estetici o di costo.

### AD-06 — Memoria come dato non fidato

La similarità non prova verità. Ogni memoria ha fonte, tenant, trust, validità, retention e stato. I record possono essere quarantinati, superseded o cancellati.

### AD-07 — Eventi con outbox/inbox

Il commit dello stato e la registrazione outbox avvengono nella stessa transazione locale. I consumer deduplicano con `event_id` e/o versione aggregato.

### AD-08 — Evoluzione disaccoppiata dal go-live

Il primo rilascio può osservare e proporre, ma non deve auto-mutare. L'attivazione di canary evolutivi è una release successiva e separata.

### AD-09 — RuFLO non è nel critical path

Il sistema deve restare pienamente operativo con `NativeAsyncioAgentHarness`. RuFLO è un adapter sostituibile; nessun workflow durevole dipende dal suo stato interno.

### AD-10 — Un componente promosso per ciclo

Il lavoro può parallelizzare test e raccolta prove, ma un change set promuove un solo componente architetturale. Se il gate fallisce, si torna alla fase responsabile, non si accumulano ulteriori modifiche.

### AD-11 — Contratti e configurazioni versionati

Prompt, agent profile, workflow, evento, gate, policy, schema e migrazione hanno versione semantica, hash, owner e compatibilità dichiarata.

### AD-12 — Nessun completamento con check rosso

`FAIL`, `NOT_PROVEN` o `ERROR` su un criterio bloccante produce `BLOCKED`. Un break-glass operativo non viene rappresentato come `PASS`.

---

## 3. Architettura target

```text
┌───────────────────────────────────────────────────────────────────────┐
│ API / COMMAND INTAKE                                                  │
│ authenticate → authorize → validate → normalize → request dedupe      │
└───────────────────────────────┬───────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ BUILDER CONTROL PLANE                                                 │
│ triage → select component → plan → generate → deterministic verify    │
│ → semantic review → APEX gate → artifact manifest → release request   │
│                                                                       │
│ PromptRegistry | AgentRegistry | GatePolicy | EvidenceStore           │
│ EvolutionProposal | optional RufloMCPAdapter                          │
└───────────────────────────────┬───────────────────────────────────────┘
                                │ approved versioned artifacts
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ RELEASE CONTROL                                                       │
│ signatures | policy decision | migrations | rollout | rollback        │
└───────────────────────────────┬───────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ DURABLE ASYNCIO WORKFLOW RUNTIME                                      │
│ scheduler | worker pool | lease heartbeat/reaper | step executor      │
│ idempotency | retry policy | circuit/bulkhead | Saga | reconciler     │
└──────────────┬─────────────────────────────┬──────────────────────────┘
               │                             │
               ▼                             ▼
┌──────────────────────────┐     ┌─────────────────────────────────────┐
│ PORTS / ADAPTERS         │     │ POSTGRESQL SOURCE OF TRUTH          │
│ HTTP, broker, object     │     │ workflow/step/lease/idempotency     │
│ store, secret manager    │     │ inbox/outbox/gate/evidence/audit    │
└──────────────────────────┘     └─────────────────────────────────────┘
```

### Struttura repository proposta

```text
src/orchestration_layer/
├── control_plane/
│   ├── intake/
│   ├── planning/
│   ├── agents/
│   ├── prompts/
│   ├── gates/
│   ├── artifacts/
│   └── evolution/
├── domain/
│   ├── workflow.py
│   ├── step.py
│   ├── events.py
│   ├── gate.py
│   └── errors.py
├── application/
│   ├── start_workflow.py
│   ├── claim_step.py
│   ├── complete_step.py
│   ├── reconcile.py
│   └── evaluate_gate.py
├── ports/
│   ├── workflow_repository.py
│   ├── artifact_store.py
│   ├── memory_store.py
│   ├── event_bus.py
│   ├── agent_harness.py
│   ├── clock.py
│   └── external_service.py
├── adapters/
│   ├── postgres/
│   ├── object_store/
│   ├── http/
│   ├── broker/
│   ├── llm/
│   └── ruflo_mcp/          # extra opzionale
├── runtime/
│   ├── scheduler.py
│   ├── worker.py
│   ├── leases.py
│   ├── executor.py
│   ├── outbox.py
│   └── reconciler.py
├── resilience/
├── security/
├── observability/
├── contracts/
└── config/

tests/
├── unit/
├── property/
├── state_machine/
├── concurrency/
├── recovery/
├── contract/
├── integration/
├── security/
├── agent_eval/
└── chaos/
```

---

## 4. Contratti minimi da implementare

### 4.1 Gate run

```text
gate_run_id, gate_id, gate_version, policy_hash,
artifact_hashes, evidence_bundle_hash, status,
criterion_results[], score_advisory, waiver_refs[],
started_at, completed_at, evaluator_provenance
```

Stati criterio: `PASS | FAIL | NOT_PROVEN | ERROR | WAIVED`.  
Stati gate: `PENDING | EVALUATING | PASS | BLOCKED | CONDITIONAL | ERROR`.

### 4.2 Workflow e step

```text
WorkflowInstance:
workflow_id, request_id, tenant_id, definition_name,
definition_version, status, version, deadline_at,
created_at, updated_at

StepState:
step_id, step_name, step_version, status, attempt,
idempotency_key, lease_owner, lease_expires_at,
started_at, deadline_at, retry_at, result_ref,
error_code, compensation_status, version
```

### 4.3 Idempotency record

```text
idempotency_key, tenant_id, operation_type,
status: CLAIMED|RUNNING|SUCCEEDED|FAILED|UNKNOWN,
owner_id, lease_expires_at, result_ref,
downstream_key, version, retention_until
```

La chiave non contiene il numero di tentativo.

### 4.4 Agent result

```text
schema_version, task_id, correlation_id, agent_profile_id,
prompt_hash, policy_hash, status, artifact_refs,
findings, evidence_refs, assumptions, risks,
retryable, confidence, usage, provenance
```

### 4.5 Evolution proposal

```text
proposal_id, component_id, baseline_hash, candidate_hash,
risk_class, hypothesis, changed_parameters,
offline_eval_ref, regression_eval_ref, shadow_eval_ref,
human_approval_ref, rollout_plan, rollback_plan,
status, owner, expires_at
```

---

## 5. RuFLO — fact-check e decisione

### 5.1 Evidenza ufficiale corrente

La documentazione ufficiale consultata descrive RuFLO come meta-harness centrato sul package npm, con superfici MCP, CLI, plugin e componenti WASM; il documento di status elenca esplicitamente tali superfici e comandi come `agent`, `swarm`, `memory`, `doctor` e `verify` ([STATUS ufficiale](https://github.com/ruvnet/ruflo/blob/main/docs/STATUS.md)).

La guida ufficiale del repository per agenti/Codex distingue coordinamento ed esecuzione: RuFLO registra e coordina, mentre l'host/agent esegue il lavoro; non è quindi sufficiente assumere che `agent spawn` equivalga a un worker Python durevole ([AGENTS.md ufficiale](https://github.com/ruvnet/ruflo/blob/main/AGENTS.md)).

Al 11 agosto 2026, la release list ufficiale indica `v3.36.0` come latest. La stessa release documenta correzioni recenti per write dichiarate riuscite ma non persistite e lost update concorrenti nella memoria ([releases ufficiali](https://github.com/ruvnet/ruflo/releases)). Questo non dimostra che RuFLO sia inutilizzabile; dimostra che l'integrazione va pinata, testata e tenuta fuori dal sistema autorevole.

Nelle fonti ufficiali consultate **non è stato trovato un contratto per le classi Python-like** `ruflo.AgentRuntime`, `WorkflowEngine`, `Router`, `MemoryPlugin`, `EventBusPlugin`, né per il file `apex7_workflow.ruflo.yaml` proposto. L'assenza dalla ricerca non prova inesistenza assoluta, ma rende queste superfici **non verificate e quindi non ammissibili** nel design di produzione.

### 5.2 Ruolo consentito

```text
AgentHarnessPort
├── NativeAsyncioAgentHarness     # riferimento e fallback
└── RufloMCPAdapter               # opzionale, sandboxed, non autorevole
```

Usi ammessi:

- coordinamento di worker generativi nel Builder Control Plane;
- discovery/routing sperimentale;
- memoria non autorevole per pattern;
- strumenti di sviluppo in sandbox.

Usi vietati:

- source of truth di workflow, gate, idempotenza o audit;
- autorità di deploy o modifica policy;
- gestione esclusiva di side effect di produzione;
- dipendenza necessaria al resume del runtime;
- installazione/upgrade con `@latest` nel critical path.

### 5.3 Proof of concept obbligatoria

| Test | Pass |
|---|---|
| Pin e riproducibilità | versione/tag/digest esatti; installazione ripetibile e SBOM generata |
| CLI/MCP contract | 100% dei comandi/tool usati rispettano schema e codici d'errore documentati |
| Failure isolation | kill/hang/malformed output non corrompono il control plane; timeout e fallback funzionano |
| Security | tool, filesystem, network e secret scope limitati; nessun accesso al DB autorevole |
| State export | artifact/result recuperabili fuori da RuFLO; nessun lock-in sul critical state |
| Load/cost | overhead entro budget approvato su benchmark rappresentativo |
| Upgrade | nuova versione testata in shadow; nessun auto-upgrade |
| Exit | disabilitazione dell'adapter non cambia la correttezza del runtime |

Se uno dei primi cinque criteri fallisce, l'esito è `DEFER/REJECT`, non “integra e correggi dopo”.

---

## 6. Piano di produzione

### Assunzione di pianificazione

La stima L2 sostituisce la range L1 dopo aver applicato il grafo di dipendenze e il costo di handoff/rework. Per il full scope G1–G7, la baseline prudente è **45–63 settimane con 6–8 FTE nominali**, **61–85 settimane con 4–6 FTE**, oppure **36–47 settimane con 9–11 FTE esperti e piattaforma matura**. Nessuna data è impegnabile prima della chiusura degli input F0 e della conferma del work-package DAG. Tech lead/runtime, backend, platform/SRE, security, QA/eval e product/domain ownership devono essere coperti esplicitamente; una persona può coprire più ruoli, ma non crea capacità aggiuntiva.

### Critical path

```text
W0/F0 → W1/F1 → W2/F2 → W3/F2 ───────────────┐
          │          │                         │
          │          └→ W5/F3 ────────────────┤
          ├→ W4/F3 ─────↑              ┌──────┴→ W8 → W9/F5 → W10/F7 → W11/F7
          └→ W6/F4 ─────────────→ W7/F4┘
                                     └→ WX/F6  # opzionale, capacità separata

Critical path calcolato: W0→W1→W2→W3→W7→W8→W9→W10→W11.
F6 evolution/RuFLO non blocca il core e non riceve capacità dal critical path.
```

In caso di conflitto, il DAG W0–W11, i tipi di dipendenza e le exit evidence L2 prevalgono sulle righe riassuntive di dipendenza delle macro-fasi F0–F7.

### F0 — Freeze, separazione e threat model — effort L1: 12–18 PW

**Dipendenze:** nessuna.  
**Obiettivo:** trasformare i 43 finding in backlog verificabile e congelare le decisioni.

**Deliverable:**

- `governance.md`, `runtime_architecture.md`, `agent_registry.yaml`;
- `gate_policy.yaml`, `handoff.schema.json`, `event.schema.json`;
- glossario normativo;
- data classification e retention matrix;
- threat model: prompt injection, tenant leak, memory poisoning, side effect duplication, event replay, supply chain;
- ADR AD-01…AD-12;
- RACI e on-call ownership;
- benchmark workload e SLO target approvati;
- backlog con ogni P0/P1/P2, owner e acceptance test.

**Gate/failure:**

- fail se un componente non ha owner;
- fail se Builder, NERVE-SOLVE e Runtime non sono separati;
- fail se un requisito critical non è tradotto in test/policy;
- fail se lo stato corrente conserva una dichiarazione “Production Ready” non qualificata o priva di evidenza; la dicitura resta ammessa solo come condizione futura nei go-live criteria.

**Human approval:** Tech Lead, Security, Data Owner e Product Owner.

### F1 — Package compilabile, contratti e CI — effort L1: 18–26 PW

**Dipendenze:** F0 completata e baseline Foundation approvata; il `PASS` finale di G1 arriva all'uscita di F1.  
**Obiettivo:** passare da snippet a progetto eseguibile.

**Deliverable:**

- package installabile con composition root;
- Pydantic strict contracts e config validate al bootstrap;
- error taxonomy e public error envelope;
- Clock port UTC/monotonic;
- schema/version registry;
- migrazioni PostgreSQL iniziali;
- CI riproducibile con lockfile e SBOM;
- documentazione eseguibile/testata.

**CI minimo:**

```text
ruff check
ruff format --check
pyright --strict oppure mypy --strict
pytest unit + property
schema validation
secret scan
SAST/dependency audit
package import/build smoke test
```

**Gate/failure:** zero errori import/type; nessun extra field accettato nei contratti pubblici; configurazioni impossibili rifiutate al bootstrap.

### F2 — Durable correctness core — effort L1: 38–52 PW

**Dipendenze:** F1.  
**Obiettivo:** implementare la catena di correttezza prima dei pattern accessori.

**Deliverable:**

- request identity stabile e `load_or_create` atomico;
- workflow/step state immutabile e versionato;
- repository PostgreSQL con compare-and-swap;
- lease, heartbeat, reaper e fair claim;
- idempotency store con chiave stabile;
- resume/replay di step completati;
- stati `UNKNOWN`, `DEGRADED`, `PAUSED`, `CANCELLED`, `TIMED_OUT`, `MANUAL_INTERVENTION`;
- reconciler per esiti esterni ambigui;
- state transition event log;
- backup/restore iniziale.

**Gate/failure:**

- 100 richieste concorrenti con la stessa key producono un solo effetto osservabile nel downstream idempotente di test;
- nessun lost update con CAS;
- kill del worker in ogni crash window recupera o porta a `UNKNOWN`, mai a falso successo;
- resume da ogni stato non terminale;
- RPO zero per transizioni già committate;
- failure di restore, reconciliation o lease test blocca F3.

### F3 — Eventi, memoria, resilienza, sicurezza e observability — effort L1: 34–48 PW

**Dipendenze:** F2.  
**Obiettivo:** integrare gli altri componenti senza compromettere il durable core.

**Deliverable eventi:**

- transactional outbox/inbox;
- event schema registry e compatibilità;
- consumer idempotenti;
- ordering per aggregate/partition;
- backoff+jitter, quarantine e replay auditato.

**Deliverable memoria:**

- PostgreSQL/pgvector opzionale;
- ACL tenant/purpose, provenance e trust level;
- retention/erasure/legal hold;
- hybrid query, dedup, contradiction e poisoning checks.

**Deliverable resilienza:**

- error classifier transient/permanent/ambiguous;
- deadline end-to-end;
- retry allowlist e `Retry-After`;
- circuit breaker HALF_OPEN corretto;
- bulkhead solo dove giustificato;
- Saga serializzabile, persistita e recuperabile;
- DLQ separata dalla quarantine.

**Deliverable security/observability:**

- JWT issuer/audience/algoritmo/JWKS e authorization context;
- tool sandbox e input non fidato delimitato;
- log/trace/metric redaction;
- OTel `service.name`, propagation, bounded cardinality e flush;
- audit append-only con integrità.

**Gate/failure:**

- zero cross-tenant read/write in suite avversariale;
- zero PII/secret nei sample di log, trace, metriche, memory ed eventi;
- duplicate event delivery non duplica la transition;
- crash tra DB commit e publish viene recuperato dall'outbox;
- nessun retry su auth, validation o domain rejection;
- una sola probe autorizzata in HALF_OPEN;
- compensation failure produce `MANUAL_INTERVENTION` e runbook link.

### F4 — Builder multi-agente e APEX gates — effort L1: 28–40 PW

**Dipendenze:** F1; artifact/evidence store; F2 per job durevoli.  
**Obiettivo:** rendere reali registry, routing, prompt e gate.

**Deliverable:**

- agent registry machine-readable;
- `AgentHarnessPort` e `NativeAsyncioAgentHarness`;
- task/result envelope validati;
- deadline, token/cost budget, max handoff depth e cycle detection;
- prompt registry con hash, owner, tool grants ed eval version;
- artifact/evidence store;
- deterministic verifier pipeline;
- semantic reviewer separato;
- Gate Policy Engine e Gate Evaluator;
- waiver, expiration, audit e human escalation;
- Final Assembler senza autorità di sovrascrivere failure.

**Gate/failure:**

- output schema invalido viene rifiutato;
- prompt injection non ottiene tool grant o authority escalation;
- budget/cycle limit arresta il job con partial result sicuro;
- deterministic critical failure produce sempre `BLOCKED`;
- stesso artifact/evidence hash produce decisione riproducibile;
- tre remediation materiali fallite producono escalation, non loop infinito;
- ogni artifact ha provenance completa.

### F5 — Eval, performance, staging e operability — effort L1: 22–30 PW

**Dipendenze:** F3 e F4.  
**Obiettivo:** misurare qualità e operabilità su workload rappresentativo.

**Deliverable:**

- golden dataset e adversarial dataset versionati;
- baseline per qualità, latenza, costo e failure recovery;
- capacity test, soak test e chaos scenarios;
- dashboard SLO e alert per burn rate;
- runbook: stuck lease, outbox lag, unknown outcome, compensation failure, tenant incident, gate outage;
- migration, backup/restore e rollback drill;
- release candidate osservata in staging.

**Gate/failure:**

- nessuna regressione sui guardrail safety/security;
- intervalli di confidenza e sample size dichiarati per metriche LLM;
- p95/p99, costo e throughput entro budget approvato;
- nessun `UNKNOWN` oltre la reconciliation SLA del workflow;
- restore e rollback completati entro RTO approvato;
- soak di almeno sette giorni e sample minimo concordato, usando il requisito più severo.

### F6 — Controlled evolution e RuFLO spike — effort L1: 16–28 PW, fuori critical path

**Dipendenze:** F4; eval framework F5 disponibile.  
**Obiettivo:** implementare proposta/esperimento, non autonomia live.

**Deliverable evolution:**

- metric collector redatto;
- proposal generator;
- risk classifier;
- offline/regression/adversarial runner;
- shadow comparison;
- approval workflow;
- canary/rollback controller disabilitato per default;
- immutable experiment report.

**Deliverable RuFLO:**

- ADR e pin esatto;
- sandbox adapter;
- contract/failure/security/load/exit test;
- decisione `ADOPT IN SHADOW | DEFER | REJECT`.

**Gate/failure:**

- qualsiasi direct write a policy/config live blocca il gate;
- candidate con guardrail regression è rifiutato anche se migliora la media;
- nessuna approvazione può essere emessa dallo stesso processo che propone;
- failure RuFLO non impatta il native harness o il runtime.

### F7 — Production candidate, canary e go-live — effort L1: 18–26 PW

**Dipendenze:** G1–G5 passati; G6 solo in modalità proposal/shadow se presente.  
**Obiettivo:** rilascio limitato, osservato e reversibile.

**Deliverable:**

- release manifest firmato;
- migration expand/migrate/contract backward-compatible;
- canary per workflow a basso impatto;
- kill switch separati per agent generation, external side effects, event publishing, evolution e RuFLO;
- on-call e escalation 24/7 secondo SLO;
- security sign-off e data retention sign-off;
- business owner approval;
- post-deploy verification e closure review.

**Gate/failure:** vedere sezioni 11 e 14. Nessun rollout prosegue automaticamente dopo un trigger rosso.

---

## 7. Maturity gate misurabili

### Formula comune

```text
PASS = tutti i blocking criteria PASS
       AND evidence bundle integra e fresca
       AND nessun rollback trigger aperto
       AND approvazioni richieste presenti

CONDITIONAL = solo non-blocking criteria con waiver valido
BLOCKED = almeno un blocking FAIL/NOT_PROVEN/ERROR
```

### Gate matrix

| Gate | Blocking evidence minima | Owner approvazione | Backtrack |
|---|---|---|---|
| **G1 Foundation** | threat model, glossary, ADR, ownership, schemas, SLO workload, 43 finding tracciati | Tech Lead + Security + Data | F0 |
| **G2 Durable Core** | concurrency, CAS, crash-window, resume, restore e reconciliation verdi | Runtime Lead + SRE | F1/F2 |
| **G3 Integration** | outbox/inbox, tenant isolation, redaction, auth, resilience e event compatibility verdi | Security + Data + Runtime | F2/F3 |
| **G4 Multi-Agent Builder** | registry/envelope/prompt hash, sandbox, budgets, deterministic blocking e provenance | AI/Eval Lead + Security | F1/F4 |
| **G5 Quality & Optimization** | golden/adversarial regression, latency/cost/capacity e soak entro target | Product + SRE + QA | F3/F4/F5 |
| **G6 Controlled Evolution** | no direct mutation, separation propose/approve, offline/shadow/rollback provati | Change Advisory + Security | F4/F6 |
| **G7 Production** | canary, backup/restore, rollback, on-call, audit, no blocker, signed manifest | Accountable Executive/Product + Tech + Security + SRE | fase responsabile o rollback |

### Waiver

Un waiver deve contenere `criterion_id`, rischio, compensating control, owner, approvatore indipendente, scadenza, scope e remediation ticket. Non è ammesso per perdita dati nota, tenant isolation, secret leak, rollback non provato, evidence integrity o side effect ad alto impatto non deduplicato/riconciliabile.

---

## 8. Test ed eval obbligatori

| Suite | Casi minimi | Fallimento bloccante |
|---|---|---|
| **Unit/property** | invarianti, config boundaries, serialization, error taxonomy | invariant breach |
| **State machine** | ogni transizione valida/vietata; status terminali/non terminali | transizione illegale accettata |
| **Concurrency** | same-key claims, CAS conflicts, lease expiry, HALF_OPEN permits | duplicate critical effect/lost update |
| **Recovery** | kill prima/dopo side effect/commit/publish/compensation | falso success o stato irrecuperabile |
| **Outbox/inbox** | duplicate, reorder, broker outage, poison event | doppia transizione o event loss locale |
| **Memory** | tenant ACL, deletion, stale source, poisoning, contradiction | cross-tenant leak o poisoned promotion |
| **Security** | JWT variants, injection, tool escalation, path/network escape, PII scan | auth bypass, exfiltration o unsandboxed execution |
| **Contract** | schema backward/forward, provider/adapter, event compatibility | breaking change non dichiarata |
| **Agent eval** | schema output, hallucinated evidence, partial, conflict, budget, cycle | invented pass/evidence o authority escalation |
| **Gate eval** | deterministic fail, tool error, stale evidence, waiver expiry | false PASS |
| **Evolution** | contamination, guardrail regression, approval separation, rollback | candidate auto-promoted o non rollbackabile |
| **Chaos/load** | DB failover, worker churn, broker outage, latency spikes, queue backlog | RTO/SLO breach senza containment |
| **RuFLO POC** | pin, malformed output, hang, crash, upgrade, export, disable | core dependency o state lock-in |

### Regola delle prove

- report senza artifact hash = invalido;
- test non eseguito = `NOT_PROVEN`;
- tool crashato = `ERROR`;
- test flaky non può essere rilanciato fino al verde senza root-cause/owner;
- evidenza scaduta va rigenerata sulla release candidate;
- lo stesso team può costruire e testare, ma l'approvazione dei gate critici richiede owner indipendente.

---

## 9. Metriche e SLO iniziali

Le soglie definitive vanno calibrate sul workload approvato in F0. Questi sono target iniziali per la release candidate, non leggi universali.

### Correctness

- `duplicate_critical_side_effects = 0` nella suite concorrente e nel canary;
- `committed_transition_data_loss = 0`;
- `illegal_state_transition = 0`;
- `cross_tenant_access = 0`;
- `false_gate_pass = 0` nel regression set critico;
- `unreconciled_UNKNOWN_older_than_domain_SLA = 0`.

### Recovery/operability

- workflow recovery p95 dopo worker kill ≤ 60 s nel benchmark iniziale;
- outbox publication lag p99 ≤ 5 s sotto carico approvato;
- lease double-ownership osservabile = 0;
- restore test rispetta RTO approvato e RPO 0 sulle transizioni committate;
- rollback applicativo completato entro il target approvato prima del canary.

### Agent/gate quality

- schema-valid agent result = 100%;
- provenance coverage degli artifact = 100%;
- critical evidence citation coverage = 100%;
- budget enforcement = 100%;
- prompt injection authority escalation = 0;
- decision reproducibility del Gate Policy Engine sullo stesso input = 100%.

### Performance/cost

- API acceptance p95 ≤ 500 ms, esclusa l'esecuzione asincrona;
- scheduler dispatch lag p95 ≤ 2 s sotto profilo di carico approvato;
- latency/cost per agent task con p50/p95/p99 e budget per classe;
- nessuna ottimizzazione promossa se migliora la media ma peggiora un guardrail o la coda oltre il budget.

### Business/fit

- tasso di workflow completati/degradati/manual intervention per tipo;
- tasso di rollback e remediation;
- gate false-block stimato su dataset etichettato;
- delta tra artifact consegnato e acceptance criteria;
- incidenti e toil operativo per 1.000 workflow.

---

## 10. Approvazioni umane e separazione dei compiti

| Decisione | Proponente | Verificatore | Approvatore |
|---|---|---|---|
| Nuovo workflow low-risk | Flow Architect | Test/Semantic Reviewer | Runtime/Product Owner |
| Side effect high-impact | Domain Owner | Security + Runtime | Accountable Business Owner |
| Schema/migrazione | Backend/Data | DBA/SRE + contract tests | Data Owner |
| Gate critical criterion | Quality/Security | Independent reviewer | Security + Tech Lead |
| Prompt/tool grant | AI/Eval | Security + adversarial eval | AI Platform Owner |
| Evolution candidate | Evolution service | Offline/shadow evaluator | Change Advisory Board |
| RuFLO update/enable | Platform | Security + POC suite | Tech Lead/SRE |
| Break-glass | Incident Commander | audit automatico | accountable on-call authority |

Nessun componente può proporre, verificare e approvare da solo la propria modifica critica.

---

## 11. Rollout, rollback e failure criteria

### Rollout

1. **Dev/local:** test deterministici e sandbox.
2. **Integration:** PostgreSQL/broker/adapters reali non produttivi.
3. **Shadow:** stessa richiesta, nessun side effect duplicato; confronto artifact/decisioni.
4. **Staging soak:** almeno sette giorni e sample minimo.
5. **Canary 1%:** solo workflow low-risk e reversibili.
6. **Canary 5% → 25% → 50%:** promozione manuale dopo finestra e sample minimi.
7. **100%:** solo dopo G7; evolution e RuFLO restano kill-switchable.

Per side effect che non possono essere shadowati, usare simulatori, record/replay redatto e canary su tenant/workflow esplicitamente autorizzati.

### Rollback design

- artifact, prompt, gate policy e workflow definition immutable/versioned;
- deployment può tornare alla versione precedente senza riscrivere history;
- migrazioni `expand → migrate → contract`; la fase contract avviene dopo la finestra di rollback;
- workflow in corso restano sulla versione originale o usano una migrazione esplicita testata;
- ogni canary ha `rollback_owner`, comando/runbook e deadline;
- rollback di policy/evolution non cancella audit ed evidence.

### Trigger di arresto immediato

- perdita/corruzione dati o side effect critico duplicato;
- auth bypass, cross-tenant access, secret/PII exfiltration;
- Gate Policy Engine produce un false PASS critico;
- workflow non recuperabile o restore fallito;
- backlog/outbox/lease fuori controllo con rischio di replay storm;
- evoluzione o RuFLO modifica una risorsa non autorizzata;
- impossibilità di attivare kill switch/rollback;
- migrazione incompatibile con la versione precedente;
- on-call o audit indisponibili durante il canary.

### Trigger di pausa e analisi

- SLO burn rate oltre budget;
- aumento di `UNKNOWN`, compensation failure o manual intervention;
- regressione quality/cost/latency oltre la soglia del gate;
- drift di schema/provider/model;
- aumento dei gate inconclusive o flaky tests.

---

## 12. Risk register

| Rischio | Severità | Controlli | Kill/rollback |
|---|---:|---|---|
| Duplicate side effect | Critica | stable key, atomic claim, downstream dedupe, reconciliation | disabilita adapter/step; stato `UNKNOWN`; manual review |
| Lost workflow state | Critica | PostgreSQL CAS, backup, recovery/restore tests | stop scheduler; restore/failover |
| False PASS del gate | Critica | deterministic engine, signed evidence, critical non-compensation | freeze promotion; revoke manifest |
| Prompt injection/tool escalation | Critica | untrusted delimiters, tool grants, sandbox, policy checks | disable agent/tool profile |
| Tenant leak/memory poisoning | Critica | ACL/RLS, provenance, quarantine, redaction | disable memory query/write; incident response |
| Event replay storm | Alta | inbox dedupe, per-key ordering, retry budget, quarantine | pause publisher/consumer partition |
| Saga compensation failure | Alta | durable compensation, idempotency, runbook | `MANUAL_INTERVENTION`; stop affected workflow type |
| Evolution drift | Critica | proposal-only, approval separation, canary/rollback | global evolution kill switch |
| RuFLO version/surface drift | Alta | exact pin, contract tests, native fallback | disable adapter |
| Observability exfiltration | Alta | allowlist/redaction/sampling/cardinality | stop exporter; local secure buffer |
| Cost/token runaway | Media/Alta | per-task budgets, cycle detection, concurrency limits | stop agent jobs; fallback deterministic/manual |
| Operational overload | Alta | SLO/burn alerts, capacity, backpressure, runbook | admission control; degrade noncritical flows |

---

## 13. Tracciabilità completa dei 43 finding

**Nota:** il design v2.1 assegna una remediation, ma i finding restano `OPEN` finché codice e prove non chiudono il gate.

### P0 — 15 bloccanti

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P0-01 Multi-agent non implementato | Registry, harness, envelope, budget, artifact/evidence pipeline | F4/G4 | OPEN |
| P0-02 asyncio non durevole | PostgreSQL source of truth, lease, resume, inbox/outbox | F2/G2 | OPEN |
| P0-03 idempotenza non atomica | stable key, unique claim/CAS, downstream key, `UNKNOWN` | F2/G2 | OPEN |
| P0-04 no resume/dedup workflow | request ID stabile e `load_or_create` atomico | F2/G2 | OPEN |
| P0-05 stato mutato/incompleto | frozen/versioned state, per-step state, CAS | F2/G2 | OPEN |
| P0-06 Saga non persistita | step serializzabili, durable action/compensation/recovery | F3/G3 | OPEN |
| P0-07 circuit HALF_OPEN errato | permit limitato, monotonic clock, fallback fuori lock | F3/G3 | OPEN |
| P0-08 retry indiscriminato | error taxonomy, transient allowlist, deadline e retry budget | F3/G3 | OPEN |
| P0-09 `critical=False` nasconde errori | discriminated result e `DEGRADED`; no generic swallow | F2–F3/G2–G3 | OPEN |
| P0-10 timeout/cancellation | monotonic deadline, persist cancel, `UNKNOWN` e reconciler | F2–F3/G2 | OPEN |
| P0-11 Pydantic non sicuro | strict/frozen/extra forbid/size limits/hidden input | F1/G1 | OPEN |
| P0-12 JWT incompleto | issuer/audience/alg pin/JWKS/claims/authz | F3/G3 | OPEN |
| P0-13 DLQ esfiltrabile | encrypted/redacted artifact ref, ACL, retention, replay audit | F3/G3 | OPEN |
| P0-14 progetto non compila | package reale, strict type/lint/import/test CI | F1/G1 | OPEN |
| P0-15 governance contraddittoria | separazione domain/process policy/orchestration/choreography | F0/G1 | OPEN |

### P1 — 18 importanti

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P1-01 resilienza obbligatoria ovunque | policy proporzionata a failure mode/SLO | F3/G3 | OPEN |
| P1-02 idempotenza assoluta | richiesta solo per side effect retryable o reconciliation | F2/G2 | OPEN |
| P1-03 adapter obbligatorio | port sui confini esterni, non astrazione rituale | F0–F1/G1 | OPEN |
| P1-04 God Master Agent | classifier/coordinator/PDP/assembler separati | F4/G4 | OPEN |
| P1-05 check deterministici come LLM | verifier tool/policy prima del semantic reviewer | F4/G4 | OPEN |
| P1-06 nessun waiver | waiver scoped, owner, expiry, audit; critical non-waivable | F4/G4 | OPEN |
| P1-07 handoff incompleto | task envelope v2.1 con versioni/budget/provenance | F1/F4/G4 | OPEN |
| P1-08 nessun budget/stop agenti | token/cost/time/handoff/cycle limits | F4/G4 | OPEN |
| P1-09 injection/codice non fidato | delimiters, sandbox, tool/network/filesystem policy | F3–F4/G3–G4 | OPEN |
| P1-10 observability incompleta | OTel resource/providers/propagation/redaction/flush | F3/G3 | OPEN |
| P1-11 correlation non propagata | adapter trace context e allowlisted baggage | F3/G3 | OPEN |
| P1-12 dati sensibili nei log | classification, allowlist e redaction processor | F3/G3 | OPEN |
| P1-13 contratto pagamento incoerente | unità esplicite e discriminated domain results | F1/G1 | OPEN |
| P1-14 alert universali | SLO/burn-rate e threshold per workflow/class | F0/F5/G5 | OPEN |
| P1-15 struttura rigida/oversized | moduli core + extras opzionali e composition root | F1/G1 | OPEN |
| P1-16 stack incoerente | dependency decision record, extras e lockfile | F1/G1 | OPEN |
| P1-17 `aioredis` obsoleto | `redis.asyncio` solo come adapter/cache opzionale | F1/F3 | OPEN |
| P1-18 stato operativo insufficiente | StepState completo con lease/result/error/compensation | F2/G2 | OPEN |

### P2 — 10 qualità/manutenibilità

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P2-01 terminologia | glossario normativo | F0/G1 | OPEN |
| P2-02 config non validate | frozen strict settings e bootstrap fail-fast | F1/G1 | OPEN |
| P2-03 clock non iniettato | Clock port monotonic + UTC | F1/F2 | OPEN |
| P2-04 error taxonomy | error code/category/retryability/safe message | F1/G1 | OPEN |
| P2-05 logging solo dichiarato | schema structlog/OTel, context binding e redaction | F3/G3 | OPEN |
| P2-06 feature flag lifecycle | owner, expiry, safe default, audit e removal ticket | F1/F7 | OPEN |
| P2-07 versionamento contratti | compatibility, deprecation, migrations e coexistence | F1–F3/G1–G3 | OPEN |
| P2-08 eccezioni custom | public error boundary e translation policy | F1/G1 | OPEN |
| P2-09 esempi non verificati | literate/import/doctest in CI | F1/G1 | OPEN |
| P2-10 ownership operativa | RACI, runbook, on-call e escalation | F0/F5/G1/G7 | OPEN |

---

## 14. Go-live criteria

Il sistema può essere dichiarato `PRODUCTION READY` solo se **tutte** le condizioni seguenti sono provate sulla release candidate:

### Architettura e backlog

- tutti i 15 P0 sono `CLOSED` con evidence refs;
- nessun P1 aperto impatta safety, security, durability, correctness o rollback;
- eventuali P1/P2 residui hanno owner, rischio accettato, scadenza e non violano un criterio non-waivable;
- Builder, NERVE-SOLVE e Runtime restano separati;
- RuFLO è disabilitato oppure ha POC/pass e non è nel critical path;
- evolution write path è disabilitato al primo go-live.

### Correttezza e sicurezza

- G1–G5 e G7 sono `PASS`; G6 è `PASS` solo per proposal/shadow oppure non attivato;
- zero false PASS critici nel regression set;
- zero duplicate critical side effect e zero cross-tenant leak nei test/canary;
- crash, resume, reconciliation, backup, restore e rollback drill passati;
- threat model e security review approvati;
- data classification, retention, deletion e audit provati.

### Operability

- SLO/SLI, capacity e error budget approvati;
- staging soak completato;
- dashboard e alert testati con synthetic incident;
- runbook esercitati, inclusa manual compensation;
- on-call, escalation e incident commander assegnati;
- kill switch e rollback provati, non soltanto documentati;
- migrazioni backward-compatible durante la finestra di rollback.

### Release

- artifact/policy/prompt/workflow/event schema con hash e firma;
- SBOM, dependency/secret/security scans verdi;
- change approvals registrate;
- canary completato senza trigger rosso;
- post-deploy verification e closure firmate dagli owner.

Se una sola condizione bloccante è rossa, non provata o in errore, il verdetto resta:

> **BLOCKED — non production-ready.**

---

## 15. Immediate next actions — primi dieci ticket

1. **OLA-001:** approvare system prompt v2.1 e AD-01…AD-12.
2. **OLA-002:** creare repository/package reale e CI strict.
3. **OLA-003:** creare schema PostgreSQL per workflow/step/lease/idempotency.
4. **OLA-004:** implementare `load_or_create`, CAS e atomic claim.
5. **OLA-005:** costruire crash-window/concurrency test harness prima degli adapter reali.
6. **OLA-006:** implementare outbox/inbox e event envelope versionato.
7. **OLA-007:** implementare strict contracts, error taxonomy, auth context e redaction.
8. **OLA-008:** creare Gate Policy Engine con criterio blocking e `NOT_PROVEN`.
9. **OLA-009:** creare Agent/Prompt Registry, envelope e Native Asyncio Harness.
10. **OLA-010:** aprire RuFLO ADR/POC separato; nessuna dipendenza core finché i contract test non passano.

L'ordine non è cosmetico: OLA-003/004/005 precedono Saga, ottimizzazione, self-evolution e qualsiasi promessa di produzione.

---

## Fonti tecniche principali

- Python `asyncio` task, timeout e cancellation: https://docs.python.org/3.11/library/asyncio-task.html
- Pydantic strict configuration: https://docs.pydantic.dev/latest/api/config/
- Redis async client: https://redis.io/docs/latest/develop/clients/redis-py/async/
- OpenTelemetry Python exporters/resources: https://opentelemetry.io/docs/languages/python/exporters/
- PyJWT claim and issuer/audience validation: https://pyjwt.readthedocs.io/en/stable/api.html
- RuFLO repository: https://github.com/ruvnet/ruflo
- RuFLO official status: https://github.com/ruvnet/ruflo/blob/main/docs/STATUS.md
- RuFLO official agent guide: https://github.com/ruvnet/ruflo/blob/main/AGENTS.md
- RuFLO releases: https://github.com/ruvnet/ruflo/releases
