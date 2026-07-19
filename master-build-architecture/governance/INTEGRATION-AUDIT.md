# Integration Audit — 2026-07-19

## Observed repository state

This audit distinguishes files verified on disk from historical narrative claims. It does not treat a claim in `README.md`, `SKILL.md`, or `memory/MEMORY-INDEX.md` as evidence by itself.

| Check | Verified result |
|---|---:|
| Agent directories with at least seven Markdown artefacts | 15 |
| Partial agent directories | 3 |
| New operational roles in registry | 55 |
| Curated primary-reference entries | 64 |
| Workflow-first control | Present (`governance/WORKFLOW-FIRST.md`) |
| PAT-like literals in tracked documentation | None after redaction |

## Partial agents requiring completion

| Directory | Markdown files | Required action |
|---|---:|---|
| `agents/qa/coverage-verifier-agent` | 1 | Complete the canonical agent set or explicitly mark not applicable. |
| `agents/qa/failure-mode-validator-agent` | 1 | Complete the canonical agent set or explicitly mark not applicable. |
| `agents/qa/target-schema-validator-agent` | 1 | Complete the canonical agent set or explicitly mark not applicable. |

## Integration decisions

1. **Workflow first:** WF-0 is a blocking precondition for every application produced by this skill.
2. **Governance over historical prose:** the files in `governance/` supersede contradictory status or process assertions in older documents.
3. **Agent scale with control:** the 55-role registry is available, but ORCH activates the smallest sufficient group and records inactive roles as not applicable.
4. **Reference discipline:** library entries are a map, not proof of research. REF records the exact source actually used, with consultation date.
5. **Credential safety:** tokens are not stored in docs, skill packages, commits, or memory.

## Recommended next implementation tranche

1. Complete the three QA agents to the canonical seven artefacts.
2. Implement the next high-leverage roles: WFL, REF, MEM, SUP, QA and REV as repository agent specs.
3. Create and approve a sample `WF-0-core-value-flow.md`, then map it to SRS, architecture and tests.
4. Run a real validator/eval pass and store only actual outcomes in memory.
