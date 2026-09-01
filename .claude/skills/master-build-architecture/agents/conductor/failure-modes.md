# Conductor Failure Modes (P09 First-Class)

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Skipped memory bootstrap | No memory/ or stale INDEX | Mandate in every handoff + kernel invariant | validator.py + silent-observer | Immediate Phase 0 restart + DEC log |
| Context stuffing in handoffs | Sub-agents receive full KG | Tight bounded context per Context-Eng Q1-Q5 in every handoff | coverage + humanizer O4 | Re-handoff with reduced context |
| Conductor does specialist work (God-Conductor) | SKILL.md becomes monolithic, no delegation | Strict "delegate only" rule in system prompt + PT01 shape | SI failure-detector | Split to sub-teams, new PLAN-vN |
| No traceability | Outputs lack source links | KG mandatory before any build | coverage_check.py | Re-run analysis phase |
| Shallow depth | Agents have <7 files or thin content | PT05 + O2 optimizer mandatory in Phase 6 | schema_validator | Depth pass re-run |
| Ignored Ruflo principles | No swarm topology or memory integration | Explicit in every phase + ruflo_bridge | anti-pattern-hunter | Add Ruflo section, re-build swarm |
| Summary instead of expansion | MKD/PLAN shorter or thinner than sources | P03 + length_check + no_summary_lint | length_check + humanizer | Re-expand with ➕ labels |
| Feature creep | New agents added without PLAN update | Interactive scaffolding + DEC approval gate | phase-planner SI | Freeze scope, log AP06, new PLAN-vN |
| Silent failures | Sub-task "succeeds" but misses invariants | Mandatory post-handoff validation + SI observer | qa team + evals | Auto-fix or human critique loop |

Full table maintained in global failure-modes-log/.