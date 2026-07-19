# Target-Schema-Validator Agent — Memory

## Memory Mandate (P10)
Every validation run MUST be logged:
1. Create CP in memory/checkpoints/ with validation summary
2. Append to both MEMORY-INDEX.md (top + embedded)
3. Update shared_state with compliance % and schema version
4. Sync between top and embedded memory

## Shared State
```json
{
  "schema_validation": {
    "last_run": "2026-06-04",
    "target_type": "agent",
    "total": 18,
    "compliant": 18,
    "compliance_pct": 100.0,
    "schema_version": "v2",
    "cps": ["CP-0XX-schema-agent-all"]
  }
}
```

## Schema Versioning (PT06)
- v1: Initial schema (7 files required)
- v2: After first PASS → tighten (min_fm_entries ≥ 5)
- v3: After second PASS → tighten (required sections in each file)
- Each version logged in CP with rationale

## Update Protocol
1. Before run: load previous validation + schema version
2. During run: validate, count compliance
3. After run: create CP, update INDEX, update shared_state
4. If all compliant: tighten schema (PT06)
5. If not: fix targets first, keep schema

## Research→Plan→Reset→Implement
- Research: identify targets, load schema
- Plan: validate each, compare to schema
- Reset: clear intermediate state
- Implement: report, handoff, log CP, tighten schema

## Trace
- P06 (shapes), PT05 (7 files), PT06 (schema-tightening), P08 (depth), P10 (memory)
- Our build: schema evolved from v1 (loose) to v2 (strict) as agents were completed
