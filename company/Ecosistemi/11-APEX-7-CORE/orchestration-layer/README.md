# Orchestration Layer

Production-oriented control plane for governed multi-agent workflows.

## Current implementation checkpoint

**W0 — Builder Swarm bootstrap.** This repository currently implements the specialized team that will construct the orchestration layer. It does not yet execute production workflows or grant external tool access.

## Builder Team

```bash
python -m builder_team.cli validate
python -m builder_team.cli show-team
python -m builder_team.cli bootstrap
python -m builder_team.cli create-work-item \
  --id WI-001 \
  --title "Create contracts source of truth" \
  --risk R1
```

The `.yaml` manifests use the JSON subset of YAML so the bootstrap validator runs with the Python standard library and no unpinned parser dependency.

## Plan Memory Agent

W1 adds a read-only, citation-first memory over the seven plans:

```bash
PYTHONPATH=src python -m plan_memory.cli verify
PYTHONPATH=src python -m plan_memory.cli build
PYTHONPATH=src python -m plan_memory.cli query "Qual è lo stato canonico?"
```

It uses deterministic BM25 retrieval, verifies source hashes before every query, preserves superseded plans as history, and cites file, heading, line range and SHA-256. Level 7 is the approved authority; unsupported queries return `INSUFFICIENT_EVIDENCE`.

## Deterministic Domain and Contracts

W2 adds nine strict JSON Schema 2020-12 contracts plus infrastructure-independent domain models for workflow transitions, DAG plans, budgets and side effects:

```bash
PYTHONPATH=src python -m orchestrator.contract_cli \
  workflow-command contracts/fixtures/valid/workflow-command.json

PYTHONPATH=src python -m orchestrator.contract_cli \
  plan contracts/fixtures/valid/plan.json
```

Unknown boundary fields, illegal transitions, stale versions, cyclic plans, over-budget reservations and incomplete side-effect contracts are rejected before any runtime or LLM integration.

## Durable Execution Adapter

W3 adds the PostgreSQL 16 migration and async adapters for tenant-scoped Unit of Work, optimistic workflow writes, transactional audit/outbox, task leasing, heartbeat, stale-result rejection and outbox claiming.

A real PostgreSQL server is intentionally required before production certification. Current sandbox tests verify SQL structure and adapter behavior with controlled async sessions; they do not claim to prove PostgreSQL locking, RLS or failover semantics.

## Governance and Tool Gateway

W4 adds OPA/Rego default-deny policy, fail-closed HTTP evaluation, opaque single-use capability grants, a PostgreSQL grant store and a Tool Gateway with only two initial operations: scoped repository read and immutable ADR artifact write.

```bash
OPA_BIN=/path/to/pinned/opa ./scripts/test-policy.sh
```

No shell or unrestricted network tool exists. Tokens are bound to tenant, workflow, task, execution token and audience; they are consumed before execution and cannot be replayed.

## Local R1 Vertical Slice

W5 provides a complete deterministic baseline: OPA authorization, Planner, Implementer, Critic, Gate, single-use Tool Gateway reads/writes, schema/security/correctness/evidence checks and conservative NERVE-SAVE output.

```bash
# Start pinned OPA separately, then:
PYTHONPATH=src python -m orchestrator.local_slice_cli \
  --repository tests/fixtures/repository-01 \
  --artifacts /tmp/ocp-artifacts \
  --file src/app.py --file README.md
```

The `repository-adr` skill is ACTIVE for the local R1 path. RuFlo remains disabled.

## Recovery and Chaos

W6 adds bounded retry policy, circuit breaker, cancellation, grant revocation, reconciliation, compensation catalog and a chaos harness. Unknown external outcomes are never blindly retried.

A real PostgreSQL chaos test kills a worker process with exit code 137 after durable claim; after lease expiry a replacement worker reclaims the same task at attempt 2, while stale tokens remain rejected.

## RuFlo Bridge

W7 pins and audits `ruflo@3.38.19` against source commit `3c99b1c`. Real MCP smoke and SIGKILL/restart certification pass for coordination and lifecycle tools. The TypeScript bridge validates tool schema hashes before entering `READY`.

Provider-backed `agent_execute` is not certified because no provider credential is available; therefore production routing remains disabled and LocalRuntime remains active.

```bash
cd ruflo_bridge
npm install --ignore-scripts
npm test
npm run certify:smoke
node certification/chaos.mjs
```

## Builder Swarm Sandbox Activation

W8 activates the full eight-role Builder Team in an immutable local sandbox. Testing and Security run in parallel; Gatekeeper can freeze after three failures; Release emits a sandbox-only Evidence Pack.

```bash
PYTHONPATH=src python -m builder_team.activation_cli \
  --id WI-ACT-001 \
  --title "Generate Builder Team capability report" \
  --risk R1
```

RuFlo successfully registers all eight roles in a transient bounded swarm, but generative execution remains disabled. Work items that request RuFlo execution freeze before implementation.

## Quality, Memory and Performance Baseline

W9 evaluates 30 deterministic behavior cases, 20 concurrent local workflows and 12 Plan Memory queries:

```bash
PYTHONPATH=src python -m benchmarks.cli \
  --output quality/benchmarks/w9-baseline.json
```

The LocalRuntime baseline passes all hard gates. Plan Memory reaches Recall@5 1.0 and citation-hash accuracy 1.0. RuFlo comparison remains blocked because provider-backed execution has not been certified; no result is fabricated.

## Security, Privacy and Disaster Recovery

W10 adds security scans, a signed test policy bundle, a governed deletion state machine, privacy tables with forced RLS, retention/control inventories and executable PostgreSQL backup/restore drills.

The restore drill recovers schema, workflow state, audit and outbox together. Test-only backup and signing roles are not production credentials. External penetration testing, KMS/HSM signing, managed failover and PITR remain blockers.

## Operations and Production Readiness

W11 adds structured redacted logs, Prometheus metrics, liveness/readiness, SLO/error-budget policy, severity escalation, five runbooks, service definition and an evidence-based PRR.

```bash
PYTHONPATH=src python -m orchestrator.operations.prr_cli
```

The current PRR verdict is **NO_GO** because accountable owners, on-call staffing, external penetration testing, production KMS, managed failover/PITR, PostgreSQL 16 and cloud/IdP/residency decisions are missing.

## Pilot Packaging and Rehearsal

W12 builds a reproducible `ocp-0.1.0-pilot` package, Python wheel, rootless Dockerfile, Compose rehearsal and CI definitions. Release rings advance through PILOT, production is blocked by PRR `NO_GO`, and rollback is verified.

This is a non-production CLI pilot—not the final API/worker service. No real traffic or deployment occurred.

## Readiness profiles

W11 remediation separates two truthful outcomes:

- **GO_LOCAL_PILOT**: loopback-only, Ed25519 operator identity, R0/R1, LocalRuntime, no external side effects.
- **NO_GO production**: external pentest, KMS, managed failover/PITR, PostgreSQL 16, cloud/residency and staffed ownership remain unresolved.

Anonymous token administration is intentionally rejected. A token manager must authenticate who requests and approves a grant.

## W13 API and persistent worker

The local pilot now includes an authenticated FastAPI surface, PostgreSQL workflow service, durable task worker and outbox publisher:

```bash
ocp-api       # loopback-only authenticated API
ocp-worker    # durable LocalRuntime worker
ocp-outbox    # local outbox sink
```

A real end-to-end run reached `COMPLETED` with eight ordered audit/outbox events. R2, R3 and RuFlo generative execution remain disabled.

## Safety

- Builder agents have scoped responsibilities and explicit denials.
- Authors cannot approve their own artifacts.
- Maximum WIP is 3; maximum concurrency is 4.
- Three failed gate attempts freeze a work item for human review.
- No production credentials, deployment access, or unrestricted network access are granted.
- RuFlo is not active yet; integration follows certification in W7.

## Tests

```bash
python -m unittest discover -s tests -v
```
