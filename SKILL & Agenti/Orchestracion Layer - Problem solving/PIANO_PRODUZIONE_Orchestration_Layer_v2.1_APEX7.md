# Orchestration Layer Architect v2.1 — Integrazione APEX-7 e piano di produzione

**Data:** 11 agosto 2026  
**Ambito:** integrazione del prompt “APEX-7 Deep Refinement” nell'Orchestration Layer Architect  
**Runtime vincolante:** Python 3.11+ con `asyncio` puro; stato durevole esterno  
**Artefatto operativo associato:** [`SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md`](SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md)  
**Audit di baseline:** [`AUDIT_Orchestration_Layer_Architect_v2.0.md`](AUDIT_Orchestration_Layer_Architect_v2.0.md)

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

I valori “55%”, “8.5/10”, “8.7/10”, “9.0/10” e “9.2/10” del prompt APEX-7 sono **rimossi dal processo decisionale**. Non costituiscono metriche, test o prova di readiness.

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

Stima indicativa per un team cross-funzionale di **4–6 persone**: tech lead/runtime, backend, platform/SRE, security, QA/eval e product/domain ownership parziale. Durata indicativa: **20–24 settimane**, soggetta a perimetro, infrastruttura esistente e criticità dei side effect. È una stima di capacità, non una promessa.

### Critical path

```text
F0 decisioni e threat model
→ F1 contratti/package/CI
→ F2 durable core
→ F3 integrazione e sicurezza
→ F4 builder + gate
→ F5 eval/staging
→ F7 production

F6 evolution/RuFLO può iniziare dopo F4 ma non blocca il go-live core;
l'evolution write path resta disabilitato al lancio.
```

### F0 — Freeze, separazione e threat model — 1–2 settimane

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

### F1 — Package compilabile, contratti e CI — 2 settimane

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

### F2 — Durable correctness core — 4 settimane

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

### F3 — Eventi, memoria, resilienza, sicurezza e observability — 3–4 settimane

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

### F4 — Builder multi-agente e APEX gates — 3 settimane

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

### F5 — Eval, performance, staging e operability — 2–3 settimane

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

### F6 — Controlled evolution e RuFLO spike — 2–3 settimane, fuori critical path

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

### F7 — Production candidate, canary e go-live — 3–4 settimane

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
