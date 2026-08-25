# LIVELLO 2/7 — Architettura logica contrattuale

**Versione:** 2.0.0  
**Sostituisce:** `level-01-general-blueprint.md`  
**Stato:** PROPOSTO — attende Gate L2 e approvazione umana  
**Baseline RuFlo verificata:** repository `ruvnet/ruflo`, commit `5234333`; root Node `>=20`, package root `claude-flow` 3.38.16; package MCP e swarm presenti ma ancora versionati alpha.  
**Principio:** L2 chiude le scelte tecniche essenziali e definisce contratti; non avvia ancora la produzione.

---

## 1. Autocritica strutturata del Livello 1

Non viene esposta una catena di pensiero privata. L’autocritica è resa verificabile tramite difetto, conseguenza e correzione.

| Difetto L1 | Perché è grave | Correzione L2 |
|---|---|---|
| Architettura troppo ampia | favorisce scaffolding vuoto | quattro deployable iniziali e un solo vertical slice |
| Stack non scelto | impossibile stimare rischi e competenze | stack di riferimento bloccato |
| RuFlo solo “dietro adapter” | boundary corretto ma non operativo | protocollo, supervisor, capability contract e fallback |
| Undici agenti mentali | rischio di confondere ruolo logico con processo LLM | quattro agenti LLM iniziali; il resto codice deterministico |
| Event bus anticipato | infrastruttura prematura | PostgreSQL queue/outbox nel vertical slice; NATS solo al trigger di scala |
| Memoria a sette layer | tassonomia elegante ma sovrapposta | quattro storage concern concreti con ACL e retention |
| Builder Swarm senza limiti | può consumare risorse senza convergere | budget, WIP, timeout, quorum e stop condition |
| Decision Protocol senza schema eseguibile | non validabile automaticamente | contratti JSON/Pydantic versionati |
| Gate qualitativi generici | PASS soggettivi | invarianti bloccanti + metriche informative separate |
| Nessun deployment target | design astratto | single-region Kubernetes, ma Docker Compose per sviluppo |
| Nessun recovery model | “compensa” era uno slogan | state machine, lease, idempotency e failure taxonomy |
| NERVE-SAVE nel core quality | può comprimere prima della correttezza | eseguito solo dopo correctness/security gate |

### Decisione critica

Il sistema iniziale **non sarà un microservizio per agente**. Sarà un modular monolith con worker separati e RuFlo bridge isolato. Spezzarlo subito in molti servizi aumenterebbe failure mode, latenza e carico operativo senza un volume dimostrato.

---

## 2. Contratto di prodotto v0.2

### 2.1 Missione

Ricevere un intento, trasformarlo in un piano autorizzabile, eseguirlo tramite capacità controllate, mantenere stato recuperabile e produrre un risultato verificato e token-efficiente.

### 2.2 Release target: `0.1 Vertical Slice`

Un workflow R1 completo:

```text
POST /workflows
→ validazione e idempotency
→ intent + risk deterministici/assistiti
→ piano massimo 5 task
→ policy gate
→ esecuzione sandbox su repository fixture
→ critic + gate
→ checkpoint persistente
→ risposta NERVE-SAVE
```

Caso campione: **analizzare un repository fixture e generare un ADR in una workspace isolata**, senza push remoto.

### 2.3 Criteri di successo release 0.1

- crash del worker durante un task: ripresa senza side effect duplicati;
- ogni transizione presente in audit log;
- task non autorizzato mai eseguito;
- output conforme allo schema e con evidenze;
- esecuzione senza RuFlo possibile tramite `LocalAgentRuntime`;
- RuFlo attivabile tramite feature flag e confrontabile A/B;
- nessun secret o PII nei log di test;
- suite end-to-end riproducibile in CI.

---

## 3. Scelte tecnologiche vincolanti

| Area | Scelta L2 | Motivo | Condizione di revisione |
|---|---|---|---|
| Control plane | Python 3.12 | compatibilità con prototipi, tipizzazione, ecosistema API/AI | throughput CPU-bound o team solo TS |
| API | FastAPI + Pydantic v2 | OpenAPI e contratti tipizzati | benchmark insufficiente |
| Persistenza canonica | PostgreSQL 16 | transazioni, JSONB, lock, outbox, pgvector opzionale | scala o tenancy incompatibili |
| ORM/migrazioni | SQLAlchemy 2 async + Alembic | controllo transazionale e migrazioni mature | nessuna |
| Work queue iniziale | PostgreSQL `FOR UPDATE SKIP LOCKED` | evita broker prematuro nel vertical slice | >50 task/s sostenuti o fan-out elevato |
| Event bus di scala | NATS JetStream | delivery persistente, consumer durevoli, operatività contenuta | introdotto solo da benchmark/necessità |
| Policy | OPA come sidecar, bundle Rego versionati | policy separata e testabile | latenza o competenze insufficienti |
| Telemetria | OpenTelemetry + Prometheus + Loki/Tempo | standard aperti e correlazione | piattaforma gestita equivalente |
| RuFlo | Node 20 sidecar/bridge, versione e commit bloccati | isolamento runtime e compatibilità MCP | SDK stabile direttamente integrabile |
| Transport RuFlo | MCP su `stdio` supervisionato nel v0.1 | nessuna porta di rete; blast radius minimo | multi-worker richiede servizio HTTP autenticato |
| Container | Docker rootless | riproducibilità e isolamento | sandbox più forte richiesta |
| Orchestrazione deploy | Kubernetes single-region | readiness, jobs, policy, scaling | team senza capacità K8s: ECS/Nomad |
| Secrets | secret manager esterno + workload identity | niente secret nei file/env persistiti | adattato al cloud scelto |
| Test | pytest, Hypothesis, Testcontainers | unit/property/integration reali | nessuna |

### 3.1 Scelte esplicitamente rimandate

- cloud provider;
- NATS in v0.1;
- pgvector e memoria semantica in v0.1;
- multi-region;
- service mesh;
- GPU/local LLM;
- federation RuFlo;
- self-evolution attiva.

---

## 4. Topologia di deployment

### 4.1 Quattro deployable iniziali

| Deployable | Responsabilità | Scala | Stato locale |
|---|---|---|---|
| `orchestrator-api` | ingress, query, command acceptance, approval endpoints | orizzontale | nessuno |
| `orchestrator-worker` | lease task, state machine, gate, recovery | orizzontale | cache effimera |
| `ruflo-bridge` | supervisione processo Node/MCP e normalizzazione capability | 1 per worker/pod | processo effimero |
| `postgres` | stato, queue, audit, outbox, memoria v0.1 | managed/HA | canonico |

OPA e OTel Collector sono sidecar/daemon di piattaforma, non servizi di dominio.

### 4.2 Confini

```text
Internet
  │ TLS/OIDC
  ▼
API Gateway ── rate limit ── orchestrator-api
                                │ command transaction
                                ▼
                            PostgreSQL
                       state │ queue │ audit │ outbox
                                ▲
                                │ lease/commit
                         orchestrator-worker
                         │       │        │
                         │       │        └── OPA sidecar
                         │       └────────── Tool Sandbox
                         └── ruflo-bridge ── MCP stdio ── pinned RuFlo

Tutti → OTel Collector → metriche/log/trace
```

### 4.3 Trust boundary

- `orchestrator-api`: input ostile;
- `worker`: trusted control plane, ma output LLM non fidato;
- `ruflo-bridge`: dipendenza esterna semi-trusted;
- `tool sandbox`: zona con side effect, capability-scoped;
- `PostgreSQL`: dati sensibili; accesso per service identity;
- output degli agenti: sempre dati, mai istruzioni privilegiate.

---

## 5. Bounded context e ownership

| Modulo | Possiede | Non possiede |
|---|---|---|
| Workflow | lifecycle, task graph, transizioni | prompt, provider, tool implementation |
| Governance | risk, policy decision, approval | esecuzione task |
| Runtime | assegnazione ed esecuzione agenti | stato canonico workflow |
| Capability | skill/tool manifest e autorizzazioni | pianificazione |
| Quality | rubriche, evidenze, gate | modifica dell’output valutato |
| Memory | record, retrieval, retention, ACL | stato workflow canonico |
| Recovery | retry decision, compensation plan | policy security |
| Observability | telemetry envelope e audit projection | logica decisionale |

**Invariante:** solo `WorkflowRepository` può mutare lo stato canonico e soltanto dentro una transazione con optimistic version check.

---

## 6. Modello di dominio minimo

### 6.1 Entità

| Entità | Chiave | Campi indispensabili |
|---|---|---|
| Workflow | `workflow_id` UUIDv7 | tenant, type, risk, status, version, budget, timestamps |
| Task | `task_id` UUIDv7 | workflow, kind, dependencies, status, lease, attempts, input/output refs |
| Decision | `decision_id` | facts, assumptions, options, selected, evidence, approvals |
| GateRun | `gate_run_id` | rubric version, criteria, score, blocking failures, verdict |
| CapabilityGrant | `grant_id` | subject, capability, scope, expiry, constraints |
| MemoryRecord | `memory_id` | namespace, type, content ref, provenance, confidence, ACL, TTL |
| AuditEvent | monotonic ID | actor, action, target, before/after hash, trace, timestamp |
| OutboxEvent | `event_id` | aggregate, type, schema version, payload, publish state |

### 6.2 Value object obbligatori

- `TenantId`, `WorkflowId`, `TaskId`;
- `RiskClass(R0..R3)`;
- `TokenBudget`, `CostBudget`, `TimeBudget`;
- `IdempotencyKey`;
- `EvidenceRef` con hash;
- `CapabilityScope`;
- `FailureCode`;
- `SchemaVersion`.

---

## 7. State machine eseguibile

```text
RECEIVED
  → VALIDATING
      → REJECTED
      → PLANNING
          → PLAN_REVIEW
              → AWAITING_APPROVAL   [R2/R3 o policy]
                  → AUTHORIZED
              → AUTHORIZED          [R0/R1]
                  → RUNNING
                      → PAUSED       [budget/human/system]
                      → RECOVERING   [errore retryable]
                          → RUNNING
                          → COMPENSATING
                      → COMPENSATING [errore non retryable con side effect]
                          → COMPENSATED
                          → MANUAL_INTERVENTION
                      → QUALITY_REVIEW
                          → REMEDIATING → RUNNING/QUALITY_REVIEW
                          → COMPLETED
                          → FAILED
```

### 7.1 Transizioni con autorità

| Da → A | Autorità | Condizione atomica |
|---|---|---|
| RECEIVED→VALIDATING | API | input e idempotency registrati |
| VALIDATING→PLANNING | Governance | schema valido e risk assegnato |
| PLAN_REVIEW→AUTHORIZED | Policy | nessun deny; approval se richiesta |
| AUTHORIZED→RUNNING | Worker | lease acquisita e budget disponibile |
| RUNNING→RECOVERING | Recovery | failure retryable e tentativi residui |
| RUNNING→COMPENSATING | Recovery | side effect confermato + failure terminale |
| QUALITY_REVIEW→COMPLETED | Gate | zero criteri bloccanti falliti |
| qualsiasi→MANUAL_INTERVENTION | Governance/Recovery | stato non automaticamente recuperabile |

### 7.2 Concorrenza

- `workflow.version` incrementale;
- update con `WHERE version = expected_version`;
- task lease con `leased_until`, `leased_by`, heartbeat;
- lease scaduta rende il task nuovamente eleggibile;
- risultato accettato solo se `execution_token` coincide;
- idempotency su `(tenant_id, idempotency_key)`.

---

## 8. Contratti applicativi

### 8.1 `CreateWorkflowCommand`

```json
{
  "schema_version": "1.0",
  "tenant_id": "tnt_...",
  "workflow_type": "repository_adr",
  "goal": "Analizza la fixture e genera un ADR",
  "input_refs": ["artifact://fixture/repo-01"],
  "constraints": {
    "max_tasks": 5,
    "deadline_seconds": 300,
    "max_tokens": 30000,
    "max_cost_usd": 2.00
  },
  "idempotency_key": "client-generated",
  "requested_by": "subject-id"
}
```

### 8.2 `TaskAssignment`

```json
{
  "schema_version": "1.0",
  "workflow_id": "uuid",
  "task_id": "uuid",
  "role": "planner|implementer|critic|gate",
  "objective": "string",
  "allowed_capabilities": ["repo.read", "artifact.write:adr/**"],
  "context_refs": ["memory://...", "artifact://..."],
  "budget": {"tokens": 6000, "seconds": 60, "cost_usd": 0.40},
  "output_schema": "schema://agent-output/1.0",
  "execution_token": "opaque-single-use"
}
```

### 8.3 `AgentResult`

```json
{
  "schema_version": "1.0",
  "task_id": "uuid",
  "execution_token": "opaque-single-use",
  "status": "SUCCEEDED|FAILED|NEEDS_INPUT",
  "output_ref": "artifact://...",
  "claims": [{"text": "string", "evidence_refs": ["artifact://..."]}],
  "usage": {"tokens_in": 0, "tokens_out": 0, "cost_usd": 0, "duration_ms": 0},
  "failure": null
}
```

### 8.4 `PolicyDecision`

```json
{
  "decision": "ALLOW|DENY|REQUIRE_APPROVAL",
  "policy_bundle": "sha256:...",
  "reasons": ["POL-R2-APPROVAL"],
  "constraints": {"capabilities": [], "expires_at": "ISO-8601"}
}
```

### 8.5 `GateReport`

```json
{
  "gate_id": "quality-output-v1",
  "rubric_version": "1.0.0",
  "verdict": "PASS|REMEDIATE|REJECT|ESCALATE",
  "blocking_failures": [],
  "criteria": [{"id": "Q1", "status": "PASS", "evidence_refs": [], "confidence": 1.0}],
  "attempt": 1,
  "artifact_hash": "sha256:..."
}
```

---

## 9. Protocollo cognitivo v2

Il “flusso di pensiero” viene implementato come stati e artefatti osservabili:

| Fase | Implementazione | Agente LLM? | Persistenza |
|---|---|---:|---|
| Frame | validatore + Intent Agent | opzionale | IntentContract |
| Risk | regole + OPA | no per verdict | RiskAssessment |
| Recall | query filtrata | no | RetrievalReceipt |
| Options | Planner | sì | PlanCandidate[] |
| Challenge | Critic indipendente | sì | ChallengeReport |
| Select | funzione di scoring + policy | verdict deterministico | DecisionRecord |
| Authorize | OPA + human approval | no | PolicyDecision |
| Execute | runtime/skill | sì o tool | TaskResult |
| Verify | schema + test + Gate Agent | misto | GateReport |
| Recover | failure matrix | no, salvo proposta | RecoveryRecord |
| Learn | curator | no promozione automatica | MemoryRecord |
| Compress | NERVE-SAVE | sì/euristico | FinalResponse |

**Divieto:** output LLM non può cambiare direttamente stato, permessi, budget o policy.

---

## 10. Runtime agenti: riduzione chirurgica

### 10.1 Quattro agenti LLM iniziali

| Agente | Scopo | Budget default | Timeout | Tool |
|---|---|---:|---:|---|
| PLANNER | produce task graph ≤5 nodi | 6k token | 60 s | memory.read, repo.read |
| IMPLEMENTER | genera artefatto nella sandbox | 10k token | 120 s | repo.read, artifact.write scoped |
| CRITIC | cerca gap e falsifica claim | 4k token | 45 s | repo.read, artifact.read |
| GATE | applica rubrica e cita prove | 3k token | 30 s | artifact.read, test.read |

INTENT resta una chiamata opzionale del PLANNER; RISK, ROUTER, RECOVERY, MEMORY-CURATOR e NERVE-SAVE sono inizialmente moduli deterministici o funzioni, non agenti autonomi.

### 10.2 Regole di spawning

- massimo 4 agenti concorrenti per workflow;
- massimo 6 task totali inclusa remediation;
- profondità spawn = 1;
- nessun agente può creare agenti direttamente;
- lo spawning passa da `RuntimePort` e budget manager;
- stop se budget residuo < costo massimo stimato del task;
- stop dopo due remediation sullo stesso artefatto;
- agente non rispondente: cancel, lease expiry, un solo retry su runtime alternativo.

---

## 11. Builder Swarm v2 operativo

### 11.1 WIP e quorum

| Regola | Valore |
|---|---:|
| Work item attivi | massimo 3 |
| Agenti concorrenti | massimo 4 |
| Durata task builder | 20 minuti |
| Retry | 1, solo failure infrastrutturale |
| Remediation | massimo 2 |
| Gate quorum | TESTER + SECURITY + GATEKEEPER per cambiamenti R2/R3 |
| Modifica architettura | ADR obbligatorio |
| Merge | test, security e gate verdi; autore escluso dall’approvazione finale |

### 11.2 Contratto comune del prompt builder

```text
IDENTITÀ: un ruolo, una responsabilità.
INPUT: work item, ADR applicabili, file consentiti, acceptance criteria.
MEMORIA: solo record citati e versionati.
VINCOLI: budget, timeout, capability, file ownership.
OUTPUT: patch/artifact + evidence manifest + rischi residui.
SUCCESS: acceptance test eseguibili, zero criterio bloccante fallito.
FAILURE: codice, causa, lavoro parziale, next safe action.
```

### 11.3 Separazione dei compiti

- ARCHITECT non approva l’ADR scritto;
- IMPLEMENTER non modifica rubriche o test bloccanti;
- TESTER non corregge implementazione durante la valutazione;
- SECURITY ha veto su finding critical/high non mitigato;
- GATEKEEPER legge artefatti per hash e non la “buona intenzione” dell’autore.

---

## 12. RuFlo Integration Contract v0.1

### 12.1 Realtà verificata

- repository e CLI attivi, ma naming storico eterogeneo (`ruflo`, `claude-flow`);
- Node richiesto `>=20`;
- pacchetti `@claude-flow/mcp` e `@claude-flow/swarm` presenti ma alpha nella baseline;
- MCP dichiara transport `stdio`, `http`, `websocket`, `in-process` nel codice;
- per v0.1 si evita l’import diretto di package alpha nel core Python.

### 12.2 Porta interna stabile

```python
class AgentRuntimePort(Protocol):
    async def health(self) -> RuntimeHealth: ...
    async def capabilities(self) -> list[RuntimeCapability]: ...
    async def execute(self, assignment: TaskAssignment) -> AgentResult: ...
    async def cancel(self, execution_token: str) -> None: ...
```

### 12.3 Responsabilità del bridge

- avviare processo RuFlo pinning versione/commit;
- handshake MCP e capability discovery;
- allowlist dei tool esposti;
- tradurre `TaskAssignment` senza perdere budget e trace context;
- validare `AgentResult` contro JSON Schema;
- applicare timeout/cancel e limite output;
- redigere log e secret;
- restituire errore normalizzato, mai stack trace grezzo;
- fallire chiuso se capability richiesta non esiste.

### 12.4 Capability matrix obbligatoria

| Capability interna | Tool/comando RuFlo reale | Versione | Smoke test | Fallback |
|---|---|---|---|---|
| runtime.health | da verificare | pinned | required | LocalRuntime health |
| agent.execute | da verificare | pinned | required | LocalRuntime execute |
| swarm.init | da verificare | pinned | optional v0.1 | sequenziale |
| memory.search | da verificare | pinned | optional v0.1 | PostgreSQL query |
| memory.store | da verificare | pinned | optional v0.1 | PostgreSQL write |

**Gate:** nessuna riga passa a “supported” senza registrazione di input, output, exit code e versione.

### 12.5 Circuit breaker bridge

- open dopo 5 failure in 60 s;
- half-open dopo 30 s;
- una probe request;
- su open: `LocalAgentRuntime` solo per R0/R1 e solo se policy consente;
- R2/R3: pausa e approvazione, mai downgrade silenzioso.

---

## 13. Memoria v2: modello ridotto e governato

### 13.1 Quattro concern, non sette database

| Concern | Tabelle/Store | Uso |
|---|---|---|
| Operational | workflows, tasks, checkpoints | stato canonico, non “memoria AI” |
| Audit/Episodic | audit_events, task_runs | cronologia immutabile e replay diagnostico |
| Knowledge | memory_records + embeddings opzionali | retrieval con provenienza |
| Plans/Decisions | plan_versions, decision_records, ADR file hash | checkpoint dei sette piani e decisioni |

### 13.2 `MemoryRecord` schema

```json
{
  "memory_id": "uuid",
  "tenant_id": "string",
  "namespace": "plan|decision|strategy|knowledge",
  "content_ref": "artifact://...",
  "content_hash": "sha256:...",
  "summary": "string",
  "source_refs": [],
  "author": "agent-or-human-id",
  "confidence": 0.0,
  "classification": "PUBLIC|INTERNAL|CONFIDENTIAL|RESTRICTED",
  "acl": {"read_roles": [], "write_roles": []},
  "valid_from": "ISO-8601",
  "valid_until": null,
  "supersedes": null,
  "status": "ACTIVE|SUPERSEDED|ARCHIVED|QUARANTINED",
  "created_at": "ISO-8601"
}
```

### 13.3 Query policy

`score = 0.45 relevance + 0.20 confidence + 0.15 freshness + 0.20 authority`

Vincoli precedenti allo scoring:

1. tenant isolation;
2. ACL;
3. classification clearance;
4. status ACTIVE;
5. temporal validity;
6. prompt-injection scan dei contenuti recuperati.

I pesi sono ipotesi iniziali; non sono quality truth e dovranno essere calibrati.

### 13.4 Plan Memory Agent

In L2 è specificato, non implementato:

- read-only sui file L1–L7 immutabili;
- indice per sezione, decisione, principio, rischio e gate;
- risposta con `file`, heading e hash;
- se due livelli divergono, prevale il livello più alto approvato e la divergenza viene mostrata;
- non interpreta un piano PROPOSTO come policy attiva;
- nessuna scrittura autonoma: nuove note entrano in inbox e richiedono curatore.

### 13.5 Retention

| Dato | Retention iniziale |
|---|---:|
| workflow operational | 90 giorni |
| audit R2/R3 | 1 anno, configurabile compliance |
| prompt/output grezzi | 30 giorni o meno se sensibili |
| metriche aggregate | 13 mesi |
| piani/ADR | durata progetto + archivio |
| secret/token | mai persistiti |

---

## 14. Skill Contract v2

### 14.1 Manifest

```yaml
apiVersion: orchestration/v1
kind: Skill
metadata:
  id: repository-adr
  version: 1.0.0
  owner: architecture-team
spec:
  riskClass: R1
  inputSchema: schemas/input.json
  outputSchema: schemas/output.json
  capabilities:
    - repo.read
    - artifact.write:adr/**
  timeoutSeconds: 120
  budgets:
    maxTokens: 10000
    maxCostUsd: 0.75
  idempotency: required
  sandbox: repository-readonly-artifact-write
  tests:
    - tests/contract.yaml
    - tests/security.yaml
```

### 14.2 Skill lifecycle

`DRAFT → VALIDATING → APPROVED → ACTIVE → DEPRECATED → REVOKED`

Attivazione richiede schema, test, owner, capability minimali, risk class, timeout e rollback/cleanup quando applicabile.

---

## 15. Failure taxonomy e recovery

| Codice | Tipo | Retry | Azione |
|---|---|---:|---|
| `VAL_*` | input/schema | no | reject |
| `POL_*` | policy/permission | no | deny o approval |
| `BUD_*` | budget | no automatico | pause/escalate |
| `RUN_TIMEOUT` | runtime timeout | 1 con backoff | alternate runtime se R0/R1 |
| `RUN_UNAVAILABLE` | RuFlo/runtime down | limitato | breaker/fallback |
| `TOOL_4XX` | richiesta tool invalida | no | fail/remediate plan |
| `TOOL_5XX` | servizio transiente | sì se idempotente | exponential backoff |
| `STATE_CONFLICT` | optimistic lock | sì immediato limitato | reload/reapply |
| `LEASE_LOST` | worker lease | no commit | discard stale result |
| `QUALITY_FAIL` | gate bloccante | max 2 remediation | reject/escalate |
| `SECURITY_*` | injection/exfiltration | no | quarantine + alert |
| `COMP_FAIL` | compensazione fallita | no loop | manual intervention + DLQ |

### 15.1 Retry formula

`delay = min(cap, base × 2^(attempt-1)) + full_jitter`

Retry consentito solo se:

- failure classificata transiente;
- deadline residua sufficiente;
- budget residuo sufficiente;
- operazione idempotente o protetta da key;
- circuit breaker non open.

---

## 16. Eventi e consistenza

### 16.1 Event envelope

```json
{
  "event_id": "uuid",
  "event_type": "workflow.authorized",
  "schema_version": "1.0",
  "occurred_at": "ISO-8601",
  "tenant_id": "string",
  "workflow_id": "uuid",
  "trace_id": "string",
  "producer": "orchestrator-worker",
  "sequence": 12,
  "payload": {},
  "payload_hash": "sha256:..."
}
```

### 16.2 Garanzia realistica

- database commit: atomico per stato + outbox;
- pubblicazione: at-least-once;
- consumer: deduplica per `event_id`;
- ordine: solo per `workflow_id` tramite `sequence`;
- duplicate: normale, non eccezione;
- gap di sequence: consumer pausa e richiede replay;
- “exactly once” non dichiarato.

Nel v0.1 l’outbox alimenta audit/projection interne. NATS viene introdotto senza cambiare il dominio quando serve fan-out esterno.

---

## 17. Quality Gate v2

### 17.1 Ordine dei gate

```text
Schema → Security → Policy → Correctness → Evidence → Operational → NERVE-SAVE
```

NERVE-SAVE non può rimuovere evidenze, warning, condizioni o istruzioni operative necessarie.

### 17.2 Criteri bloccanti vs metriche

| Tipo | Esempio | Uso |
|---|---|---|
| Invariante | schema valido, nessun secret, policy allow | blocca |
| Rubrica | completezza, actionability, coerenza | remediation/escalation |
| Metrica | TES, token count, latenza | osservazione/ottimizzazione |

TES <0.6 non forza una riscrittura se questa danneggia completezza; segnala inefficienza dopo correctness PASS.

---

## 18. API minima

| Metodo | Endpoint | Scopo |
|---|---|---|
| POST | `/v1/workflows` | crea idempotentemente |
| GET | `/v1/workflows/{id}` | stato e link artefatti |
| POST | `/v1/workflows/{id}/approve` | approvazione R2/R3 |
| POST | `/v1/workflows/{id}/cancel` | cancellazione cooperativa |
| GET | `/v1/workflows/{id}/events` | timeline paginata |
| GET | `/health/live` | processo vivo |
| GET | `/health/ready` | DB, policy, runtime secondo modalità |
| GET | `/metrics` | esposizione protetta |

### 18.1 Sicurezza API

- OIDC/OAuth2, audience e tenant claim validati;
- idempotency header obbligatorio su POST;
- body limit 1 MiB;
- rate limit per tenant;
- artifact upload separato con signed URL;
- errori RFC 9457 senza dettagli sensibili;
- approval richiede step-up authentication per R3.

---

## 19. Repository L2 ridotto e assegnato

```text
orchestration-layer/
├── README.md
├── pyproject.toml
├── uv.lock
├── package.json                      # solo bridge RuFlo
├── package-lock.json
├── Makefile
├── .env.example
│
├── docs/
│   ├── plans/level-01.md
│   ├── plans/level-02.md
│   ├── adr/
│   │   ├── 001-modular-monolith.md
│   │   ├── 002-postgres-source-of-truth.md
│   │   ├── 003-ruflo-bridge.md
│   │   ├── 004-opa-policy.md
│   │   └── 005-no-autonomous-evolution.md
│   ├── architecture/{context,containers,components,threat-model}.md
│   └── runbooks/{worker-crash,ruflo-down,compensation-failed}.md
│
├── src/orchestrator/
│   ├── bootstrap.py                  # composition root unico
│   ├── config.py                     # Settings validate-at-startup
│   ├── domain/
│   │   ├── workflow.py               # aggregate + invarianti
│   │   ├── task.py                   # task/lease/attempt
│   │   ├── decision.py               # decision record
│   │   ├── gate.py                   # gate result
│   │   ├── failure.py                # taxonomy
│   │   └── events.py                 # domain event
│   ├── application/
│   │   ├── create_workflow.py
│   │   ├── advance_workflow.py
│   │   ├── execute_task.py
│   │   ├── approve_workflow.py
│   │   ├── recover_task.py
│   │   └── complete_workflow.py
│   ├── ports/
│   │   ├── repositories.py           # workflow/task/uow
│   │   ├── agent_runtime.py
│   │   ├── policy.py
│   │   ├── capabilities.py
│   │   ├── artifacts.py
│   │   ├── memory.py
│   │   └── telemetry.py
│   ├── adapters/
│   │   ├── postgres/                 # repository, queue, outbox
│   │   ├── local_runtime/             # fallback e test baseline
│   │   ├── opa/
│   │   ├── filesystem_artifacts/      # v0.1 only
│   │   └── otel/
│   ├── governance/
│   │   ├── risk.py
│   │   ├── budget.py
│   │   └── approval.py
│   ├── quality/
│   │   ├── schema_gate.py
│   │   ├── security_gate.py
│   │   ├── evidence_gate.py
│   │   └── nerve_save.py
│   ├── memory/
│   │   ├── records.py
│   │   ├── retrieval.py
│   │   └── retention.py
│   ├── api/
│   │   ├── app.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── auth.py
│   └── worker/
│       ├── main.py
│       ├── leasing.py
│       └── supervisor.py
│
├── ruflo_bridge/
│   ├── package.json
│   ├── package-lock.json
│   ├── src/{server,supervisor,mapper,validator}.ts
│   ├── schemas/{assignment,result}.json
│   └── tests/{contract,smoke}.test.ts
│
├── policies/
│   ├── workflow.rego
│   ├── capability.rego
│   └── tests/
│
├── skills/repository-adr/
│   ├── manifest.yaml
│   ├── instructions.md
│   ├── schemas/{input,output}.json
│   └── tests/{contract,security}.yaml
│
├── builder_swarm/
│   ├── agents.yaml
│   ├── workflow.yaml                 # formato interno, non presunto RuFlo
│   ├── prompts/{lead,architect,scout,implementer,tester,security,gate}.md
│   └── gates/{architecture,implementation,release}.yaml
│
├── migrations/versions/
├── deploy/{compose,k8s,otel}/
├── scripts/{setup,smoke,benchmark,seed_fixture}.sh
├── tests/{unit,property,contract,integration,e2e,security,chaos,fixtures}/
└── .github/workflows/{ci,security,release}.yml
```

### 19.1 Ownership

- `domain/`, ADR: ARCHITECT + human reviewer;
- `application/`, adapters: IMPLEMENTER;
- `policies/`, security tests: SECURITY;
- `tests/`: TESTER, modifiche acceptance richiedono review ARCHITECT;
- `ruflo_bridge/`: RUFLO-SCOUT + IMPLEMENTER;
- `gates/`: GATEKEEPER + human owner, non IMPLEMENTER;

---

## 20. Build vs buy

| Capacità | Decisione | Motivo |
|---|---|---|
| Workflow state machine | build minimale | invarianti specifiche e controllo completo |
| Agent swarm | integrate RuFlo | non reinventare coordinamento; validare valore |
| Policy engine | buy/use OPA | linguaggio e tooling policy maturi |
| Database | managed PostgreSQL | riduce on-call e rischio dati |
| Event broker | defer NATS | non necessario al vertical slice |
| Telemetry | OpenTelemetry | standard, niente lock-in |
| Vector memory | defer; valutare RuFlo/pgvector | nessun bisogno dimostrato v0.1 |
| Secrets | cloud secret manager | non costruire crittografia operativa custom |
| Artifact store | filesystem dev, object store prod | interfaccia sostituibile |
| NERVE-SAVE | adattare package esistente | utile ma subordinato ai gate |

---

## 21. Benchmark che decide se usare lo swarm

### 21.1 Varianti

- A: singolo agente via `LocalAgentRuntime`;
- B: quattro ruoli sequenziali;
- C: RuFlo swarm minimo;
- D: RuFlo swarm adattivo, solo se C supera B.

### 21.2 Dataset

Minimo 30 fixture versionate:

- 10 repository semplici;
- 10 con ambiguità/requisiti conflittuali;
- 5 con prompt injection nei file;
- 5 con failure simulate.

### 21.3 Metriche

`utility = 0.35 correctness + 0.20 evidence + 0.15 security + 0.15 completion - 0.10 normalized_cost - 0.05 normalized_latency`

Promozione di una variante solo se:

- utility media +≥10% rispetto alla baseline;
- nessuna regressione security;
- intervallo di confidenza bootstrap 95% del delta non include zero;
- costo ≤2.5× baseline;
- p95 entro deadline del workflow.

---

## 22. Piano di costruzione L2

| Incremento | Output | Test di uscita |
|---:|---|---|
| I0 | ADR, contratti JSON, threat model | review e schema validation |
| I1 | dominio + state machine in-memory | property test transizioni |
| I2 | PostgreSQL repository, queue, outbox | crash/restart e concorrenza |
| I3 | API + auth fixture + idempotency | contract/API security test |
| I4 | LocalRuntime + skill repository-adr | e2e R1 senza RuFlo |
| I5 | OPA + capability gateway | deny/approval/bypass tests |
| I6 | RuFlo bridge pinned | capability smoke + fallback |
| I7 | quality/evidence/NERVE-SAVE | golden dataset e non-loss test |
| I8 | OTel, dashboard, runbook | trace completa e alert test |
| I9 | benchmark A/B/C | decisione documentata sullo swarm |

Ogni incremento è mergeabile, rollbackabile e produce un checkpoint.

---

## 23. Stima realistica preliminare

Assumendo 3–4 persone esperte o agenti assistiti con revisione umana:

| Blocco | Tempo indicativo |
|---|---:|
| I0–I2 | 2–3 settimane |
| I3–I5 | 2–3 settimane |
| I6 | 1–2 settimane, variabilità RuFlo elevata |
| I7–I8 | 2 settimane |
| I9 + hardening | 2 settimane |
| Totale vertical slice pre-prod | 9–12 settimane |

**Brutalmente sincero:** promettere un sistema production-grade completo in pochi giorni sarebbe falso. Gli agenti accelerano scrittura e test, non eliminano integrazione, threat modeling, benchmark, review e incident readiness.

---

## 24. Quality Gate L2 → L3

| ID | Criterio bloccante | Evidenza |
|---|---|---|
| C1 | stack e versioni approvati | ADR + lock strategy |
| C2 | state machine senza transizioni illegali | modello + property tests pianificati |
| C3 | contratti principali versionati | JSON Schema/Pydantic design |
| C4 | quattro deployable con trust boundary | container diagram |
| C5 | RuFlo isolato e fallback definito | Integration Contract |
| C6 | agenti LLM ridotti e budgettati | runtime table + spawn rules |
| C7 | memoria con tenant/ACL/provenienza | schema e query policy |
| C8 | delivery semantics realistiche | outbox/dedup/ordering contract |
| C9 | failure taxonomy e recovery | matrice completa |
| C10 | Builder Swarm con SoD e limiti | WIP/quorum/ownership |
| C11 | vertical slice e incrementi testabili | I0–I9 |
| C12 | benchmark swarm falsificabile | dataset, metriche, soglia |
| C13 | approvazione umana | via esplicito |

**Soglia:** 13/13. Un criterio mancante non viene compensato da punteggi medi.

---

## 25. Autocritica del Livello 2

### Miglioramenti rispetto a L1

- stack scelto e motivato;
- microservizi prematuri eliminati;
- state machine, contratti, concorrenza e idempotenza espliciti;
- RuFlo collegato a un bridge realistico e non a classi inventate;
- agenti LLM ridotti da undici a quattro;
- memoria trasformata da metafora a modello governato;
- delivery corretta ad at-least-once con deduplica;
- piano incrementale, benchmark e stima temporale concreti.

### Difetti residui da attaccare nel Livello 3

1. I contratti sono esempi, non JSON Schema completi.
2. Mancano diagrammi di sequenza per success, retry, approval e compensation.
3. OPA/Rego non ha ancora policy concreta.
4. Il bridge RuFlo non ha capability names verificate tramite smoke test.
5. Il protocollo MCP stdio in produzione può creare coupling di processo.
6. PostgreSQL queue non ha dimensionamento sperimentale.
7. Non esiste ancora uno schema SQL fisico né migration plan.
8. Plan Memory Agent non ha retrieval algorithm testabile né threat controls completi.
9. La formula benchmark contiene pesi iniziali arbitrari.
10. Kubernetes potrebbe essere over-engineering per un singolo team.
11. Manca SBOM, firma artefatti e supply-chain policy.
12. Compliance e data residency restano sconosciute.

### Punteggio critico

| Dimensione | L1 | L2 |
|---|---:|---:|
| Realismo | 8.8 | 9.2 |
| Specificità | 6.2 | 8.7 |
| Implementabilità | 5.5 | 8.1 |
| Sicurezza | 7.2 | 8.5 |
| Testabilità | 6.0 | 8.8 |
| Rischio di over-engineering | 6.0 | 7.6 |

**Verdetto:** L2 è abbastanza specifico per progettare una vertical slice, ma non ancora abbastanza provato per implementare la piattaforma completa. L3 dovrà trasformare i contratti in specifiche eseguibili, verificare RuFlo realmente e modellare tutti i flussi critici.