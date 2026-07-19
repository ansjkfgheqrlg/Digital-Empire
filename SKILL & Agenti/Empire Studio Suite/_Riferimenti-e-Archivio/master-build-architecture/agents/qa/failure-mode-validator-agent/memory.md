# Failure-Mode-Validator Agent — Memory

## Memory Mandate (P10)
Every validation run MUST be logged:
1. Create CP in memory/checkpoints/ with validation summary
2. Append to both MEMORY-INDEX.md (top + embedded)
3. Update shared_state with compliance %
4. Sync between top and embedded memory

## Shared State
```json
{
  "fm_validation": {
    "last_run": "2026-06-04",
    "total_agents": 18,
    "compliant": 18,
    "partial": 0,
    "missing": 0,
    "compliance_pct": 100.0,
    "cps": ["CP-0XX-fm-validation-all"]
  }
}
```

## Update Protocol
1. Before run: load previous validation from shared_state
2. During run: track per-agent status
3. After run: create CP, update INDEX, update shared_state
4. If compliance dropped: create DEC + flag regression

## Research→Plan→Reset→Implement
- Research: scan all agent directories
- Plan: validate each, aggregate results
- Reset: clear intermediate state
- Implement: generate report, handoff, log CP

## Trace
- P09 (failure-modes-first-class), P10 (memory-first), PT07 (silent observer)
- CS03 (SI with observer), CS04 (bugs in real test)
- Our build: compliance improved from 28% (early, no FM files) to 100% (after batch completion)
