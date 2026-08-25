# LIVELLO 7/7 — Blueprint definitivo di pre-produzione

**Versione:** 7.0.0  
**Sostituisce:** `level-06-production-operating-model.md`  
**Stato:** CANDIDATO FINALE — attende approvazione umana prima dell’implementazione  
**Scopo:** unica fonte progettuale per costruire, verificare e attivare l’Orchestration Layer.  
**Baseline RuFlo candidata:** `ruvnet/ruflo@5234333`, root 3.38.16, Node ≥20; nessun uso production finché la certification non passa.

> “Definitivo” significa consolidato e implementabile, non infallibile. Cloud, identità degli owner e soglie finali devono essere confermati con misure reali. Ogni assunzione non provata resta un gate, non viene trasformata in promessa.

---

## 1. Autocritica finale del Livello 6

| Limite L6 | Correzione L7 |
|---|---|
| decisioni distribuite in sei piani | un solo blueprint normativo, i precedenti diventano storia |
| nessuna matrice completa di tracciabilità | requisito→componente→file→test→owner |
| albero repository ancora variabile | struttura definitiva per vertical slice e produzione |
| sequenza post-L7 non formalizzata | programma di costruzione W0–W12 con gate |
| Plan Memory Agent solo specificato | work package iniziale read-only con test e manifest |
| Builder Swarm non bootstrapato | manifest, ruoli, workflow, budget e attivazione definiti |
| RuFlo clone/integration non inseriti nel build flow | lane source-audit→certification→bridge→canary |
| Definition of Done frammentata | DoD globale e per incremento |
| GO/NO-GO distribuito | dossier PRR finale con veto e stop condition |
| rischio documentazione obsoleta | source-of-truth map, owner e drift test |

### Decisione finale

Il prodotto sarà un **control plane deterministico Python**, con execution plane sostituibile. RuFlo fornisce capacità swarm solo se certificato e se supera la baseline. PostgreSQL resta stato canonico. Gli LLM producono proposte e artefatti; non concedono permessi, non mutano policy e non decidono transizioni privilegiate.

---

## 2. Missione, scope e risultato

### 2.1 Missione

Trasformare un intento in un workflow autorizzato, eseguibile, recuperabile, auditabile e token-efficiente tramite agenti e skill controllati.

### 2.2 Release iniziale

`OCP 0.1 PILOT`:

- R0 e R1 abilitati;
- R2 limitato a tenant e skill allowlisted;
- R3 disabilitato;
- un vertical slice: analisi di repository fixture e generazione di ADR in workspace isolata;
- LocalRuntime obbligatorio come baseline/fallback;
- RuFlo opzionale dietro feature flag;
- nessuna self-evolution diretta.

### 2.3 Non-scope

- microservizio per agente;
- swarm illimitato;
- exactly-once distribuito;
- multi-region iniziale;
- agent federation;
- memoria RuFlo canonica;
- policy o security modificabili autonomamente;
- conformità legale dichiarata senza audit competente.

---

## 3. Principi costituzionali finali

1. Control plane deterministico; cognition probabilistica ai bordi.
2. Default deny e least privilege.
3. PostgreSQL è l’unica autorità di stato workflow.
4. RuFlo è executor sostituibile, mai source of truth.
5. Output LLM è sempre non fidato.
6. Idempotenza o reconciliation prima del retry.
7. Esito incerto è `RECONCILING`, non successo presunto.
8. Stato, audit e outbox sono atomici.
9. Nessun PASS senza evidenza verificabile.
10. Hard gate non compensabile da medie.
11. NERVE-SAVE opera solo dopo correctness/security PASS.
12. Memoria richiede provenienza, ACL, validità e lifecycle.
13. Minimo swarm efficace; più agenti solo su benchmark.
14. Human sovereignty su R2/R3, security, policy e release.
15. Ogni dipendenza ha fallback, pause o fail-closed esplicito.
16. Ogni release è un’unità coerente di codice, schema, policy, prompt e runtime pin.
17. Backup vale solo dopo restore drill.
18. Ogni componente ha owner, expiry/deprecation e kill switch.

---

## 4. Architettura definitiva

```text
                               ┌──────────────────────┐
Client / Approval UI ─OIDC/TLS→│ API Gateway / WAF    │
                               └──────────┬───────────┘
                                          ▼
┌────────────────────────── ORCHESTRATION CONTROL PLANE ──────────────────────────┐
│ orchestrator-api                                                               │
│  ├ request schema / idempotency / tenant                                      │
│  ├ workflow commands & queries                                                │
│  └ approval/cancel endpoints                                                  │
│                                                                                │
│ orchestrator-worker                                                            │
│  ├ Workflow Aggregate + Transition Registry                                   │
│  ├ Planner/Dispatcher                                                         │
│  ├ Risk/Budget/Capability                                                     │
│  ├ OPA Policy Adapter                                                         │
│  ├ Recovery/Reconciliation/Compensation                                       │
│  ├ Quality Gates → NERVE-SAVE                                                 │
│  └ Memory/Artifact adapters                                                   │
│                                                                                │
│ PostgreSQL: state | tasks/leases | approvals | budget | audit | outbox | memory│
└──────────────┬───────────────────────────────┬──────────────────────────────────┘
               │ TaskAssignment               │ grants
               ▼                              ▼
┌──────────────────── EXECUTION PLANE ─────────────────┐  ┌─────────────────────┐
│ AgentRuntimePort                                      │  │ Tool Gateway/Sandbox│
│  ├ LocalRuntime                                      │  │ capability enforce  │
│  └ RuFloBridge → MCP stdio → pinned RuFlo → provider│  │ side-effect contract│
└───────────────────────┬───────────────────────────────┘  └──────────┬──────────┘
                        │ AgentResult/evidence                        │
                        └────────────────────┬────────────────────────┘
                                             ▼
                                  Object Store S3-compatible

All components → OTel Collector → metrics/logs/traces
Control transactions → audit DB → WORM export/hash chain
```

### 4.1 Deployable

| Deployable | Responsabilità | Stato locale |
|---|---|---|
| `orchestrator-api` | command/query/auth/approval | nessuno |
| `orchestrator-worker` | state machine, execution supervision, quality/recovery | cache effimera |
| `ruflo-bridge` | MCP supervision e mapping | workspace effimera |
| `tool-gateway` | capability e sandbox | nonce/cache effimera |
| PostgreSQL managed | stato canonico | durevole |
| Object store managed | artifact/evidence | durevole/versionato |
| OPA sidecar | policy evaluation | bundle cache firmata |
| OTel Collector | telemetry | buffer limitato |

API e worker possono iniziare nello stesso repository e immagine base, ma come processi/deployment separati. Nessun altro microservizio viene creato senza trigger di scala o sicurezza.

### 4.2 Deployment profile

- DEV: Docker Compose;
- PILOT: managed containers single-region, 2 API e 2 worker;
- SCALE/Kubernetes: solo con trigger misurati (>20 concorrenti sostenuti, isolation o scaling indipendente).

---

## 5. Stack definitivo del pilot

| Area | Tecnologia |
|---|---|
| Language control plane | Python 3.12 |
| API/contracts | FastAPI, Pydantic v2, JSON Schema 2020-12 |
| Persistence | PostgreSQL 16, SQLAlchemy 2 async, Alembic |
| Queue pilot | PostgreSQL `SKIP LOCKED` + lease |
| Broker futuro | NATS JetStream solo ai trigger definiti |
| Policy | OPA/Rego |
| RuFlo bridge | TypeScript/Node 20, MCP stdio supervisionato |
| Artifact | MinIO DEV, S3-compatible managed PILOT |
| Telemetry | OpenTelemetry, Prometheus, Loki/Tempo o equivalenti gestiti |
| Test | pytest, Hypothesis, Testcontainers; Vitest per bridge |
| Packaging | `uv.lock` + npm lockfile, container rootless |
| Supply chain | SBOM CycloneDX, Cosign, provenance, scans |

---

## 6. Ecosistemi interni

| Ecosistema | Moduli | Autorità |
|---|---|---|
| Governance | risk, OPA, approval, capability, budget | deterministica |
| Cognition | Planner, Implementer, Critic, Gate | propone/valuta, non autorizza |
| Workflow | aggregate, task graph, transition registry | canonica |
| Execution | runtime port, bridge, tool gateway | esecuzione controllata |
| Recovery | retry, reconciliation, compensation | deterministica per catalogo |
| Memory | plan index, knowledge record, retention | governata |
| Quality | schema, security, evidence, correctness, NERVE-SAVE | hard gate + metriche |
| Observability | audit, logs, metrics, trace | audit canonico separato |
| Evolution | eval, experiment, change proposal | shadow/human-promoted |
| Operations | SLO, on-call, tenant, release, DR | responsabilità umana |

---

## 7. Flusso di mentalità finale

Il sistema applica sempre questo orientamento:

```text
Prudenza → separa fatti e assunzioni
Proporzionalità → controlli commisurati al rischio
Reversibilità → preferisci azioni annullabili
Evidenza → nessuna promozione senza prova
Least privilege → capacità minime e temporanee
Economia → minimo agente/token/tool efficace
Esplicitazione → unknown, failure e limiti sono stati reali
Apprendimento controllato → proposta, esperimento, human promotion
```

---

## 8. Protocollo decisionale osservabile

Non viene memorizzato un monologo interno. Ogni ragionamento operativo produce artefatti:

1. **FRAME:** goal, vincoli, dati mancanti.
2. **RISK:** R0–R3 con motivi.
3. **RECALL:** record ammessi con citazione/hash.
4. **OPTIONS:** massimo tre strategie.
5. **PLAN:** DAG, budget, capability, side effect.
6. **CHALLENGE:** failure mode e assunti contestati.
7. **SELECT:** decision record deterministico/policy-aware.
8. **AUTHORIZE:** OPA e human approval quando richiesta.
9. **EXECUTE:** lease, grant e sandbox.
10. **VERIFY:** schema→security→correctness→evidence→operational.
11. **RECOVER:** retry/reconcile/compensate/escalate.
12. **LEARN:** memoria quarantinata o approvata.
13. **COMPRESS:** NERVE-SAVE con protected spans.
14. **REPORT:** risultato, limiti, usage, trace/audit refs.

---

## 9. State machine finale

```text
RECEIVED → VALIDATING → PLANNING → PLAN_REVIEW
  ├ REJECTED
  ├ AWAITING_APPROVAL → AUTHORIZED
  └ AUTHORIZED
       → RUNNING
          ├ PAUSED
          ├ RECOVERING → RUNNING
          ├ RECONCILING → RUNNING | COMPENSATING | MANUAL_INTERVENTION
          ├ COMPENSATING → COMPENSATED | MANUAL_INTERVENTION
          ├ QUALITY_REVIEW → REMEDIATING → RUNNING
          │                  ├ COMPLETED
          │                  └ FAILED
          └ CANCEL_REQUESTED → CANCELLING
                               ├ CANCELLED
                               ├ RECONCILING
                               └ COMPENSATING
```

### 9.1 Terminali

`COMPLETED`, `FAILED`, `REJECTED`, `CANCELLED`, `COMPENSATED`, `MANUAL_INTERVENTION`.

### 9.2 Invarianti

- Transition Registry unico;
- optimistic version;
- lease + execution token;
- stale result scartato;
- budget monotono;
- stato/audit/outbox stessa transazione;
- side effect senza idempotency/reconcile non retryable;
- approval legata a plan/policy hash e scadenza.

---

## 10. Agenti runtime definitivi del pilot

| Agente | Istanze | Autorità | Budget default |
|---|---:|---|---:|
| PLANNER | max 1/workflow | produce Plan, nessun tool write | 6k token/60 s/$0.40 |
| IMPLEMENTER | max 2/workflow | artifact write scoped | 10k/120 s/$0.75 |
| CRITIC | max 1/artifact | read-only challenge | 4k/45 s/$0.30 |
| GATE | max 1/gate | verdict rubric, nessuna modifica | 3k/30 s/$0.20 |
| Plan Memory Agent | bounded service/function | read-only piani approvati | 6k context/query |
| Meta Observer | batch offline | Change Proposal only | budget mensile |

RISK, ROUTER, BUDGET, RECOVERY, CAPABILITY e MEMORY CURATION restano moduli deterministici.

### 10.1 Spawn policy

- massimo 4 agenti concorrenti/workflow;
- profondità spawn 1;
- agenti non spawnano agenti;
- massimo 6 task incluse remediation;
- massimo due remediation;
- ogni istanza ha prompt/model/hash/capability/expiry;
- agente non certificato o scaduto non viene routed.

---

## 11. Skill architecture

Ogni skill contiene:

```text
skills/<skill-id>/
├── manifest.yaml
├── instructions.md
├── schemas/input.json
├── schemas/output.json
├── policies/
├── side-effects.yaml
├── prompts/
├── tests/contract/
├── tests/security/
├── tests/recovery/
├── runbook.md
└── changelog.md
```

### 11.1 Lifecycle

`DRAFT → VALIDATING → ACTIVE → DEPRECATED → SUSPENDED/REVOKED`.

### 11.2 Activation gate

- owner e backup;
- risk/data classification;
- schema;
- capability minime;
- budget/timeout;
- side-effect/reconciliation/compensation;
- test ed Evidence Pack;
- runbook;
- kill switch;
- deprecation path.

Prima skill: `repository-adr`, R1, repository read-only e artifact write scoped.

---

## 12. Memory ecosystem definitivo

### 12.1 Concern

| Concern | Store | Uso |
|---|---|---|
| Operational | PostgreSQL | workflow/task/checkpoint |
| Audit/Episodic | PostgreSQL + WORM export | eventi e task run |
| Plans/Decisions | file immutabili + manifest DB | L1–L7, ADR, decision record |
| Knowledge | `memory_records` + index ricostruibile | retrieval governato |
| Experimental | namespace separato/quarantine | output non approvati |

### 12.2 Plan Memory Agent

- legge `plans/level-*.md` e solo release approvate;
- SHA-256, heading tree, line range, supersession;
- BM25 baseline; semantic retrieval solo se supera benchmark;
- restituisce file, heading, linee, hash e status;
- livello approvato più alto prevale;
- conflitti mostrati, non fusi;
- `INSUFFICIENT_EVIDENCE` quando necessario;
- nessuna capability e nessuna scrittura;
- note/output agenti restano QUARANTINED finché curate.

### 12.3 Target

- Recall@5 ≥95%;
- Precision@5 ≥85%;
- citation/hash e supersession 100%;
- cross-tenant leak e instruction execution 0.

---

## 13. RuFlo integration definitiva

### 13.1 Source acquisition post-approvazione

```bash
gh repo clone ruvnet/ruflo vendor/ruflo-source
cd vendor/ruflo-source
git checkout <approved-pin>
git verify-commit <approved-pin> || record provenance exception
```

Il clone serve per audit e certification. Non diventa automaticamente dipendenza production e non viene modificato dal Builder Swarm.

### 13.2 Tool candidate

- `system_health`;
- `swarm_init`, `swarm_status`, `swarm_shutdown`;
- `agent_spawn`, `agent_execute`, `agent_status`, `agent_terminate`.

Memory tool, federation e autoscaling restano disabilitati nel pilot.

### 13.3 Certification

`STATIC → SMOKE → EXECUTION → CHAOS → CANARY`.

Per ogni tool: commit, schema hash, input/output golden, timeout, restart, persistence semantics, provider usage, cleanup e failure mapping.

### 13.4 Swarm pilot

```json
{
  "topology": "hierarchical",
  "maxAgents": 4,
  "config": {
    "communicationProtocol": "message-bus",
    "consensusMechanism": "majority",
    "failureHandling": "retry",
    "loadBalancing": false,
    "autoScaling": false
  },
  "metadata": {"non_canonical": true}
}
```

### 13.5 Promotion

RuFlo viene usato se:

- nessun hard gate fallisce;
- correctness/evidence migliora ≥10% rispetto a LocalRuntime;
- CI bootstrap 95% del delta >0;
- costo ≤2.5×;
- incident rate non peggiora oltre 5 punti;
- bridge passa chaos e canary.

Se non passa, LocalRuntime resta production path. RuFlo non è un requisito ideologico.

---

## 14. Security architecture finale

- OIDC/MFA/step-up;
- tenant RLS forzata;
- token capability opaco, single-use, task-bound, TTL ≤5 min;
- OPA default deny;
- tool sandbox rootless, filesystem readonly e egress allowlist;
- object store KMS/versioning/hash/write-once key;
- secret manager/workload identity;
- prompt/artifact come untrusted data;
- supply-chain pin, SBOM, signature, provenance;
- audit transazionale e WORM export;
- kill switch K1–K5;
- critical/high finding aperto blocca PILOT/PROD.

R3 resta disabilitato finché PRR dedicata non prova approval, irreversible action preview, DR e on-call 24/7 adeguato.

---

## 15. Reliability architecture finale

| Failure | Comportamento |
|---|---|
| worker crash | lease expiry, stale token rejection, safe resume |
| RuFlo crash | breaker; LocalRuntime solo R0/R1 policy-permitted |
| OPA down | fail closed; cache allow solo R0 read-only ≤10 s |
| DB down | stop mutation/claim, API 503, restore/failover |
| artifact down | nessuna completion senza hash verificato |
| provider 429 | Retry-After entro budget/deadline |
| provider auth | no retry, incident |
| unknown side effect | RECONCILING |
| compensation fail | MANUAL_INTERVENTION + critical alert |
| telemetry down | audit continua; telemetry backlog bounded |

RPO ≤5 min; RTO control plane ≤60 min; worker recovery p95 ≤45 s nel pilot.

---

## 16. Quality e release

### 16.1 Gate order

`Schema → Security → Policy → Correctness → Evidence → Recovery/Operational → NERVE-SAVE`.

### 16.2 Pipeline

`G0 Format/Type → G1 Unit/Property → G2 Contract/Migration → G3 Security/Supply chain → G4 Integration → G5 E2E/Recovery/Tenant → G6 Prompt/Memory/NERVE-SAVE → G7 Load/Cost`.

### 16.3 Release rings

`DEV → TEST → SHADOW → CANARY-5 → CANARY-25 → PILOT → PROD`.

### 16.4 Evidence Pack

Commit, image digest, SBOM, schema, policy, prompt, model, RuFlo pin/schema, test, security, benchmark, migration, risk e rollback firmati come unità coerente.

---

## 17. NERVE-SAVE nel sistema finale

NERVE-SAVE è Layer 3 di espressione, non gate di verità.

```text
Verified output
→ extract protected spans
→ eliminate filler/format/densify
→ non-loss and contradiction checks
→ emit compressed output or fallback verified source
```

Protected spans: warning, numeri, soglie, negazioni, comandi, path, evidenze, step obbligatori, errori, next action e termini security/legal.

TES resta metrica informativa; non può approvare un output incompleto o scorretto.

---

## 18. Builder Swarm definitivo

### 18.1 Team

| ID | Ruolo | Produce | Non approva |
|---|---|---|---|
| BUILD-LEAD | backlog/dipendenze | work item e checkpoint | codice/gate proprio |
| ARCHITECT | contratti/ADR | design e traceability | propria ADR finale |
| RUFLO-SCOUT | audit/certification | capability dossier | RuFlo promotion |
| IMPLEMENTER | codice/migrazioni | patch e artifact manifest | test/gate modificati |
| TESTER | test/failure injection | report grezzi | production code dello stesso item |
| SECURITY | policy/threat/abuse | finding e sign-off | finding proprio chiuso senza retest |
| GATEKEEPER | criteri/evidenza | PASS/FAIL/ESCALATE | artifact valutato |
| RELEASE | packaging/canary | Evidence Pack e rollout | deroga hard gate |

### 18.2 Limiti

- WIP 3;
- concorrenza 4;
- task 20 minuti;
- retry 1 solo infrastrutturale;
- remediation 2;
- branch/worktree isolato;
- rete off di default;
- nessun secret production;
- autore escluso dall’approvazione finale;
- tre fail: freeze e human review.

### 18.3 Workflow

```text
Work item
→ scope/acceptance/file ownership
→ ADR/contract
→ RuFlo capability proof se coinvolta
→ implementation in worktree
→ test + security paralleli
→ immutable Artifact Manifest
→ Gatekeeper
→ merge candidate
→ CI G0–G7
→ Evidence Pack
→ release ring
```

---

## 19. Repository definitivo

```text
orchestration-layer/
├── README.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── uv.lock
├── package.json
├── package-lock.json
├── .env.example
├── CODEOWNERS
│
├── plans/
│   ├── README.md
│   ├── level-01-general-blueprint.md
│   ├── level-02-contractual-architecture.md
│   ├── level-03-executable-nervous-system.md
│   ├── level-04-security-resilience-control.md
│   ├── level-05-quality-evidence-release.md
│   ├── level-06-production-operating-model.md
│   └── level-07-final-production-blueprint.md
│
├── docs/
│   ├── architecture/{context,containers,components,data-flow,threat-model}.md
│   ├── adr/001-*.md
│   ├── api/openapi.yaml
│   ├── runbooks/RB-01..RB-10.md
│   └── operations/{service-definition,oncall,prr,go-live}.md
│
├── contracts/
│   ├── schemas/v1/
│   │   ├── workflow-command.json
│   │   ├── plan.json
│   │   ├── task-assignment.json
│   │   ├── agent-result.json
│   │   ├── gate-report.json
│   │   ├── policy-decision.json
│   │   ├── capability-grant.json
│   │   ├── side-effect-contract.json
│   │   └── event-envelope.json
│   └── fixtures/{valid,invalid}/
│
├── src/orchestrator/
│   ├── bootstrap.py
│   ├── config.py
│   ├── domain/
│   │   ├── workflow.py
│   │   ├── transitions.py
│   │   ├── task.py
│   │   ├── decision.py
│   │   ├── budget.py
│   │   ├── capability.py
│   │   ├── side_effect.py
│   │   ├── cancellation.py
│   │   ├── gate.py
│   │   ├── failure.py
│   │   └── events.py
│   ├── application/
│   │   ├── create_workflow.py
│   │   ├── plan_workflow.py
│   │   ├── approve_workflow.py
│   │   ├── execute_task.py
│   │   ├── request_cancel.py
│   │   ├── reconcile_task.py
│   │   ├── compensate_workflow.py
│   │   └── complete_workflow.py
│   ├── ports/
│   │   ├── unit_of_work.py
│   │   ├── repositories.py
│   │   ├── agent_runtime.py
│   │   ├── policy.py
│   │   ├── artifacts.py
│   │   ├── tools.py
│   │   ├── memory.py
│   │   └── telemetry.py
│   ├── adapters/
│   │   ├── postgres/{uow,repositories,queue,outbox}.py
│   │   ├── local_runtime/
│   │   ├── opa/
│   │   ├── object_store/
│   │   └── otel/
│   ├── governance/{risk,budget,approval,grants}.py
│   ├── recovery/{retry,reconciliation,compensation_catalog}.py
│   ├── quality/{schema,security,correctness,evidence,nerve_save}.py
│   ├── memory/{records,plan_ingest,retrieval,retention}.py
│   ├── api/{app,routes,schemas,auth,errors}.py
│   └── worker/{main,leasing,supervisor}.py
│
├── ruflo_bridge/
│   ├── package.json
│   ├── package-lock.json
│   ├── src/{server,supervisor,mcp_client,mapper,validator,sandbox}.ts
│   ├── certification/{static,smoke,execution,chaos}.ts
│   ├── manifests/tool-schema-hashes.json
│   └── tests/
│
├── tool_gateway/
│   ├── app.py
│   ├── grants.py
│   ├── nonce.py
│   ├── sandbox.py
│   └── tests/
│
├── policies/{authorization,tenant,approval,capability}.rego
├── prompts/{planner,implementer,critic,gate}/
├── skills/repository-adr/
├── builder_swarm/{agents,workflow,prompts,gates}/
├── migrations/versions/
├── quality/{datasets,evals,load,chaos,dashboards}/
├── operations/{ownership,slo,escalation,tenants,change,finance}/
├── privacy/{inventory,retention,deletion,controls}/
├── deploy/{compose,pilot,otel,backup,security}/
├── scripts/{setup,smoke,seed,benchmark,restore-drill}.sh
├── tests/{unit,property,contract,integration,e2e,security,chaos,fixtures}/
└── .github/workflows/{ci,security,release}.yml
```

**Regola:** i file vengono creati solo dal work package che li usa; l’albero è target, non autorizzazione a generare stub vuoti.

---

## 20. Matrice di tracciabilità essenziale

| Requisito | Componente | File principali | Test | Owner |
|---|---|---|---|---|
| stato canonico | Workflow/Postgres | `domain/workflow.py`, `postgres/uow.py` | property/integration | ARCHITECT |
| transizioni legali | Transition Registry | `domain/transitions.py` | property | TESTER |
| idempotenza | API/UoW/Tool | `create_workflow.py`, `tools.py` | duplicate E2E | IMPLEMENTER |
| tenant isolation | RLS/Auth | `auth.py`, migrations | security | SECURITY |
| policy default deny | OPA | `policies/*.rego` | contract/abuse | SECURITY |
| capability | Grants/Tool Gateway | `grants.py` | replay/expiry | SECURITY |
| budget | Cost ledger | `domain/budget.py` | concurrency/property | SERVICE |
| RuFlo isolation | Bridge | `ruflo_bridge/src/*` | certification/chaos | RUFLO-SCOUT |
| fallback | LocalRuntime | `adapters/local_runtime` | E2E/chaos | IMPLEMENTER |
| unknown outcome | Reconciliation | `reconcile_task.py` | chaos | TESTER |
| compensation | Catalog | `compensation_catalog.py` | recovery | SKILL OWNER |
| evidence | Quality/Object store | `quality/evidence.py` | tamper | GATEKEEPER |
| compression safe | NERVE-SAVE | `quality/nerve_save.py` | non-loss | QUALITY |
| plan memory | Memory | `plan_ingest.py`, `retrieval.py` | citation/ACL | MEMORY OWNER |
| audit | UoW/outbox/WORM | `postgres/outbox.py` | gap/hash | SRE |
| release safety | Evidence Pack/CI | `quality/`, workflows | promotion simulation | RELEASE |
| privacy delete | Data lifecycle | `privacy/deletion` | deletion drill | PRIVACY |
| recovery | backup/runbook | `deploy/backup`, runbook | restore drill | PLATFORM |

La matrice completa verrà materializzata in `docs/traceability.csv` durante W1 e deve raggiungere copertura 100% dei requisiti P0/P1.

---

## 21. Programma di implementazione post-approvazione

### W0 — Freeze e bootstrap

- approva L7 e calcola hash dei sette piani;
- crea repository e branch protection;
- registra ADR iniziali;
- acquisisce RuFlo via `gh repo clone` e blocca candidate pin;
- crea Builder Swarm manifest senza attivare tool production.

**Gate:** source/provenance/owner definiti.

### W1 — Plan Memory Agent minimo

- manifest piani;
- parser heading/line/hash;
- BM25 read-only;
- precedence/status/conflict;
- CLI/API query locale;
- citation e contamination test.

**Gate:** citation/supersession 100%, zero write/capability.

### W2 — Contratti e deterministic domain

- JSON Schema source of truth;
- Workflow Aggregate/Transition Registry;
- DAG, budget, side-effect value object;
- property test.

**Gate:** nessuna sequenza generata viola invarianti.

### W3 — Durable execution

- PostgreSQL schema/RLS;
- UoW, queue, lease, audit, outbox;
- crash/concurrency test.

**Gate:** zero duplicate mutation e stale result commit.

### W4 — Governance

- OPA;
- risk/approval;
- token opaco capability;
- cost reservation;
- Tool Gateway skeleton/sandbox.

**Gate:** abuse suite zero bypass.

### W5 — Local vertical slice

- LocalRuntime;
- quattro prompt;
- skill `repository-adr`;
- artifact store;
- quality chain e NERVE-SAVE.

**Gate:** 60 fixture E2E e non-loss.

### W6 — Recovery

- cancel/reconcile/compensation;
- dependency breaker;
- runbook e chaos CH-01..12.

**Gate:** invarianti preservate e manual intervention corretta.

### W7 — RuFlo certification

- STATIC/SMOKE;
- provider test isolato;
- tool schema manifest;
- EXECUTION/CHAOS;
- bridge mapping.

**Gate:** tool necessari `SUPPORTED`; altrimenti RuFlo disabilitato.

### W8 — Builder Swarm activation

- esegue work item solo in sandbox;
- confronta output con team/manual baseline;
- attiva massimo quattro agenti;
- Evidence Pack per ogni merge.

**Gate:** nessuna violazione SoD/capability e quality delta positivo.

### W9 — Quality/Memory/Performance

- eval/holdout;
- Plan Memory metrics;
- load/soak;
- benchmark Local vs RuFlo;
- cost model.

**Gate:** hard constraints e capacity envelope.

### W10 — Security/Privacy/DR

- penetration test;
- deletion drill;
- restore drill;
- supply-chain/signature;
- audit WORM.

**Gate:** zero critical/high e RPO/RTO provati.

### W11 — Operations/PRR

- owner/on-call;
- tenant pilot;
- alerts/game day;
- PRR e exceptions.

**Gate:** GO/NO-GO firmato.

### W12 — Go-live

- R0 internal→R1→5%→25%→pilot;
- daily review;
- R2 separato;
- R3 disabilitato.

**Gate:** 30-day review prima dell’espansione.

---

## 22. Stima e critical path

| Blocco | Stima |
|---|---:|
| W0–W2 | 1–2 settimane |
| W3–W4 | 2–3 settimane |
| W5–W6 | 2–3 settimane |
| W7–W9 | 2–3 settimane |
| W10–W11 | 2 settimane |
| W12 pilot | 1 settimana + 30 giorni osservazione |

Vertical slice pre-pilot: **9–12 settimane** con 3–4 persone esperte e agenti assistivi. Calendario aumenta se mancano SRE, Security o Privacy owner. Nessuna stima presume che lo swarm elimini review, test o incident readiness.

Critical path:

`contracts → domain → durable execution → governance → local slice → recovery → RuFlo/quality → security/DR → PRR`.

Plan Memory Agent può essere costruito in parallelo dopo W0, ma non blocca il deterministic core oltre W2.

---

## 23. Definition of Done globale

### Architecture

- ADR approvate;
- traceability P0/P1 100%;
- zero dipendenza RuFlo nel dominio;
- diagrammi e state machine allineati al codice.

### Code/contracts

- schema source of truth;
- type/static checks;
- migration expand/contract;
- nessuno stub non usato nel path production.

### Security/privacy

- RLS, OPA, capability e sandbox testati;
- zero critical/high;
- deletion e restore drill;
- secret/log scan;
- data inventory e retention.

### Reliability

- crash/retry/reconcile/compensate provati;
- RPO/RTO raggiunti;
- hard-zero invariant mai violata;
- runbook e kill switch rehearsed.

### Agents/memory

- prompt/model/hash certificati;
- agent registry con owner/expiry;
- Plan Memory Agent citation/supersession 100%;
- nessuna auto-promozione della memoria.

### RuFlo

- pin esatto;
- Evidence Pack;
- tool schema hash;
- certification almeno CHAOS per R1;
- fallback LocalRuntime;
- benchmark promozione superato oppure RuFlo disabilitato.

### Quality/release

- G0–G7 verdi;
- holdout non contaminato;
- NERVE-SAVE non-loss;
- capacity/cost envelope;
- signed Evidence Pack;
- rollback canary provato.

### Operations

- Service Owner e on-call;
- SLO/error budget;
- tenant acceptance;
- PRR GO;
- support boundary;
- monitoring/alerts;
- decommission plan.

---

## 24. GO/NO-GO finale

### GO solo se

- DoD completo;
- hard gate tutti PASS;
- zero critical/high security aperti;
- restore, reconciliation e kill switch provati;
- audit completo;
- capacity 30% headroom;
- costo entro cap;
- owner/on-call presenti;
- tenant pilot accetta limiti;
- RuFlo certificato o disabilitato;
- Evidence Pack firmato.

### NO-GO immediato se

- cross-tenant leak;
- policy/capability bypass;
- duplicate side effect;
- audit gap;
- unknown outcome trasformato in successo senza reconciliation;
- backup non ripristinabile;
- approval replay;
- schema RuFlo drift non gestito;
- critical/high finding;
- assenza owner/on-call;
- costo senza hard cap.

---

## 25. Rischi residui accettabili e non accettabili

### Accettabili nel pilot, con monitoraggio

- variabilità output LLM;
- RuFlo disabilitato se non supera benchmark;
- supporto non 24/7;
- single-region;
- BM25 senza embeddings;
- PostgreSQL queue entro envelope;
- R2 limitato e R3 off.

### Non accettabili

- permessi decisi dall’LLM;
- stato canonico in RuFlo/file locali;
- agenti illimitati;
- retry non idempotente;
- memoria senza tenant/provenienza;
- self-evolution diretta;
- release con `latest`;
- conformità dichiarata senza evidenza;
- eccezioni permanenti senza owner/scadenza.

---

## 26. Autocritica finale L7

### Punti di forza

- consolida architettura, sicurezza, qualità, operazioni e produzione;
- separa chiaramente determinismo e probabilità;
- integra RuFlo senza consegnargli autorità impropria;
- rende agenti, memoria e skill misurabili e revocabili;
- definisce un ordine di costruzione con gate e DoD;
- ammette esplicitamente che RuFlo può non essere promosso;
- evita microservizi e swarm prematuri;
- rende possibile decommission e rollback.

### Limiti reali

1. Non sostituisce l’implementazione e i test reali.
2. Il candidate pin RuFlo può diventare obsoleto prima di W7.
3. Cloud, region, IdP e nomi degli owner devono essere scelti.
4. Le soglie saranno ricalibrate sui dati del pilot.
5. Penetration, restore e chaos report non esistono ancora.
6. La stima 9–12 settimane dipende da competenze disponibili.
7. Il sistema è complesso: se il caso d’uso reale non giustifica questa complessità, va ridotto.

### Punteggio

| Dimensione | L6 | L7 |
|---|---:|---:|
| Realismo | 9.8 | 9.8 |
| Specificità | 9.3 | 9.7 |
| Implementabilità | 9.2 | 9.6 |
| Sicurezza | 9.6 | 9.7 |
| Operabilità | 9.6 | 9.7 |
| Tracciabilità | 7.5 | 9.5 |
| Production readiness progettuale | 9.2 | 9.6 |
| Production readiness reale | 0 finché non implementato/testato | 0 finché non implementato/testato |

**Verdetto finale:** blueprint approvabile per iniziare la costruzione. Non è autorizzazione a dichiarare il sistema production-ready. La readiness reale esisterà solo dopo W0–W12, Evidence Pack e PRR GO.