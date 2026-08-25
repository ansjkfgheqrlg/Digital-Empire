# ADR-009 — Publish deterministic baseline; block fabricated RuFlo comparison

- **Status:** Accepted for W9
- **Date:** 2026-08-23

## Decision

Quality, memory and performance are measured before any RuFlo promotion. The LocalRuntime baseline uses 30 behavior cases, including adversarial and invalid inputs, plus 20 concurrent local workflows. Plan Memory is evaluated on a versioned query set with approved-only retrieval, citation hashes and explicit insufficient-evidence behavior.

RuFlo comparison remains `BLOCKED` because provider-backed `agent_execute` is not certified. No synthetic or guessed RuFlo quality/cost result is accepted.

## Consequences

- Local deterministic latency and zero model cost are reference measurements only; they are not comparable to an LLM until the same dataset is executed through a certified provider.
- BM25 query expansion and heading-path scoring are versioned as index 1.1.
- Recall@5 and citation integrity pass; MRR remains visible rather than hidden by a single aggregate score.
- Load results use tiny temporary fixtures and do not establish production capacity.
