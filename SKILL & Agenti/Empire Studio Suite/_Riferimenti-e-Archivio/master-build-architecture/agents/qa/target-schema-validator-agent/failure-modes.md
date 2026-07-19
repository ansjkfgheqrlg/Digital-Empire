# Target-Schema-Validator Agent — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-TS-001 | Wrong schema loaded | Agent validated against skill schema | Match target_type to schema key | Check schema name in report | Re-run with correct schema |
| FM-TS-002 | Schema too permissive | 3 files accepted as 7 | Enforce exact file count in schema | Compare actual vs required count | Tighten schema (PT06) |
| FM-TS-003 | Schema too strict | 7 files required but 8 expected | Schema allows extras, only checks minimums | Check schema definition | Adjust min thresholds |
| FM-TS-004 | File exists but empty | File counted as present but has no content | Check file size > 0 bytes | Add size check | Flag as partial |
| FM-TS-005 | Missing required dir | Dir not created but counted | os.path.isdir check | Verify dir exists | Create dir, re-validate |
| FM-TS-006 | No schema tightening | All compliant but schema never tightens | PT06 mandate: tighten after PASS | Check schema version in CP | Tighten schema, re-validate |
| FM-TS-007 | Memory not updated | Validation run not logged as CP | P10 mandate | Check memory/ for CP | Create CP retroactively |
| FM-TS-008 | CATALOG.md counted as agent file | Metadata file inflates agent file count | Exclude CATALOG.md from agent validation | Filter known metadata files | Re-run with filter |

## Global Rules
- All failures logged to failure-modes-log/ (P09/P10/PT07)
- PT06: schema tightening is MANDATORY after every PASS
- Trace: P06 + PT05 + PT06 + P08 + our ANALYSIS
