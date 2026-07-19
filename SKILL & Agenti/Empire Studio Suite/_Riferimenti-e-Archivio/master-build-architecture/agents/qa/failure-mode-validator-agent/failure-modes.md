# Failure-Mode-Validator Agent — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-FMV-001 | Agent has no failure-modes.md | Scan reports MISSING | PT05 mandate: 7 files per agent | scan_agent_directory checks file exists | Handoff to agent-spec-builder |
| FM-FMV-002 | Failure table has <5 entries | Entry count low, status PARTIAL | Require ≥5 entries in template | Count table rows in parse | Add more entries from P09/AP |
| FM-FMV-003 | No SI cross-references | Missing references to failure-detector/triage | Template includes SI section | Check for SI keywords in content | Add SI cross-references |
| FM-FMV-004 | No memory integration | Missing P10/CP references | Template includes memory section | Check for memory keywords | Add memory integration |
| FM-FMV-005 | Table format invalid | Parser can't extract rows | Enforce markdown table format | Parse table, check column count | Reformat table |
| FM-FMV-006 | Validator not run after build | Compliance degrades silently | Mandatory validation after every agent build | Check for validation CP in memory | Run validation retroactively |
| FM-FMV-007 | False positive: stub file passes | File exists with minimal content | Require ≥5 entries + SI + memory refs | Check all criteria, not just existence | Tighten validation criteria |
| FM-FMV-008 | Self-validation skipped | This agent's own FM not checked | Include self in every validation run | Check self in report | Add self-check step |

## Global Rules
- All failures logged to failure-modes-log/ (P09/P10/PT07)
- CS03 lesson: SI without observer = drift → always include silent-observer in SI refs
- CS04 lesson: bugs in real test → always test validation, not just document it
- Trace: P09 + CS03/CS04 + our ANALYSIS
