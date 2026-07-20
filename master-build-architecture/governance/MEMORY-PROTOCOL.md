# Persistent Memory Protocol

## Purpose
Conversation is temporary working context. Repository memory is the auditable source of truth.

## Canonical memory structure

```text
memory/
  MEMORY-INDEX.md
  checkpoints/     # work completed and verification evidence
  decisions/       # ADRs; never overwrite an approved decision
  sessions/        # compact handovers
  plans/           # versioned plans
  architectures/   # topology, boundaries, contracts
  risks/           # risk register and mitigations
  references/      # sources actually consulted for a decision
```

## Read → Plan → Write → Verify

1. Read `MEMORY-INDEX.md`, latest handover, open decisions, risks, and task-specific references.
2. State assumptions and intended change before implementation.
3. Create/modify the artefact and update the relevant canonical record in the same increment.
4. Record real verification evidence: command, date, result, known limitations.
5. Create a short handover at session close: status, decisions, changed files, open risks, next atomic step.

## Data discipline

Never store credentials, user personal data that is not strictly necessary, private reasoning traces, or access tokens. Store concise conclusions, decisions, evidence and provenance.

## Conflict order

User-confirmed constraints → approved ADR → approved requirements → contracts/tests → implementation notes → temporary session context.

If sources conflict, flag the conflict for ORCH/SUP. Do not silently overwrite history.
