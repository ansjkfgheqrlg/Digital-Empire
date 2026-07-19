# Coverage-Verifier Agent — Failure Modes

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-CV-001 | Source atoms not enumerated | Coverage % inflated, orphans missed | Full scope scan (P12/PT09) | Manual spot-check 5 random atoms | Re-run with full scope |
| FM-CV-002 | Clone content not scanned | Coverage misses Ruflo/Content-Forge refs | Include clones in scope | Compare clone refs vs output | Add clones to scope |
| FM-CV-003 | CATALOG counted as output | Coverage inflated by metadata | Exclude CATALOG from output scan | Check output list includes only content | Filter metadata files |
| FM-CV-004 | User input not tracked | User vision atoms orphaned | Always include user inputs in sources | Check user vision in source list | Add user inputs to scope |
| FM-CV-005 | Coverage claimed without scan | Report says 100% but scan not run | Mandatory scan step in playbook | Check for scan logs in memory | Run scan, update report |
| FM-CV-006 | Memory not updated after run | No CP logged for coverage run | P10 mandate: log every run | Check memory/ for CP | Create CP retroactively |
| FM-CV-007 | Partial coverage misclassified | Atom cited 2x counted as full | Strict threshold: ≥3 = full | Re-check borderline atoms | Reclassify and update report |
| FM-CV-008 | No handoff on failure | Coverage <70% but no remediation | Mandatory handoff in playbook | Check conductor received handoff | Trigger handoff |
| FM-CV-009 | Advisor/skill-creator not scanned | External skill refs orphaned | Include advisor + skill-creator in scope | Check external refs in output | Add to scope |

## Global Rules
- All failures logged to failure-modes-log/ via SI (P09/P10/PT07)
- Silent observer default (PT07)
- Recovery always includes CP + INDEX update (P10)
- Trace to: P09 + CS04 (bugs in real test) + our ANALYSIS (coverage gaps)
