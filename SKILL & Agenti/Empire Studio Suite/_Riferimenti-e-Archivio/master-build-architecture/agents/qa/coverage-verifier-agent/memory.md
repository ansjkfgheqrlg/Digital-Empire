# Coverage-Verifier Agent — Memory

## Memory Mandate (P10)
Every coverage run MUST be logged:
1. Create CP in memory/checkpoints/ with coverage report summary
2. Append to both MEMORY-INDEX.md (top + embedded)
3. Update shared_state with coverage % and orphan count
4. Sync between top and embedded memory

## Two-Layer Memory
- **Short-term:** Current session context (what scope, what outputs checked)
- **Long-term:** Historical coverage reports in memory/ (CPs), shared_state JSON

## Shared State
```json
{
  "coverage": {
    "last_run": "2026-06-04",
    "scope": "all",
    "total_atoms": 95,
    "coverage_pct": 92.6,
    "orphan_count": 0,
    "status": "PASS",
    "cps": ["CP-0XX-coverage-full", "CP-0YY-coverage-after-depth"]
  }
}
```

## Update Protocol
1. Before run: load previous coverage from shared_state
2. During run: track atoms enumerated, cites found
3. After run: create CP, update INDEX, update shared_state
4. If status changed (PASS→WARN or vice versa): create DEC

## Research→Plan→Reset→Implement
- Research: enumerate sources + outputs
- Plan: build coverage map, classify atoms
- Reset: clear intermediate state
- Implement: generate report, handoff, log CP

## Trace
- P10 (memory-first), P12 (traceability), PT07 (silent observer), PT09 (multi-source)
- Content-Forge C1 (coverage verification)
- Our build: coverage improved from 45% (early) to 92%+ (after depth pass)
