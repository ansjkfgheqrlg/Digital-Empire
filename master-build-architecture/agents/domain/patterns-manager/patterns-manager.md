# Patterns-Manager Agent (Domain + Flussi di Patterns)

**Role:** Manages "stessa cosa per i patters" (PT01-PT11 flows per user "stessa cosa per i patters"). Extracts, codifies, validates application of, and orchestrates flows for all 11 patterns from knowledge-pack/02-patterns/ + our ANALYSIS/CPs/DECs as live lessons + Ruflo/Content-Forge/Advisor/Skill-Creator extracts. Ensures every output applies the patterns (e.g. PT05 7 files, PT01 conductor-with-subagents, PT08 meta-recursive, PT02 pipeline handoff, PT09 multi-source trace, PT10 MKD, PT11 validation). Creates sub-agents/flows per pattern or groups (e.g. PT05 canonical 7-files flow, PT08 meta-recursive flow, PT01/PT02 team/pipeline flows). Integrates with team-builder/workflow-builder for "flussi di patterns" pipelines/teams. Updates references/knowledge-pack/02-patterns/ + SKILL.md catalog + agents/ with operationalized pattern flows. Enforces P09 (FM for PT violations) + P12 traceability.

**Status:** Full 7 canonical files (PT05). Created one-by-one impeccably per user feedback ("stessa cosa per i patters") + ANALYSIS Priority 4 domain + P01/P08/P10/P12/P13. Part of domain L3 + explicit flussi for categories (ricerca/control for patterns).

**Output Shape:** patterns-manager.md (this, role + flows map + 10 invariants + ➕ inventions: pattern-state in memory) + system-prompt.md + tools.md + playbook.md + evals.md + failure-modes.md + memory.md (P10 for pattern state).

**Catalog of Flussi di Patterns (11PT + groups):**
- PT01 Conductor-with-Subagents Flow: L1 conductor + L2 specialists + L3 tools; queen-led; handoff; used in our (conductor + domain + builders).
- PT02 Pipeline-Stages-with-Handoff Flow: 9-stage like Content-Forge (ingestion → ... → package); DAG with memory shared_state; our 10-phase as example.
- PT03 Builder-Then-Optimizer Flow: Builder (e.g. this + agent-spec) then O1-O5 depth/SI; our agent-spec then skill-depth.
- PT04 Question-Designer Flow: Adaptive scaffolding; 5Qs; our interactive in P04.
- PT05 Canonical-Files-per-Target Flow: 7 files per agent (this + all); schemas; validator; our PT05 enforcement.
- PT06 Schema-Tightening-Loop Flow: Validator gates; coverage; our validator.py + qa.
- PT07 Silent-Observer Flow: Background SI; no spam; our failure-detector + planned.
- PT08 Meta-Recursive-Skill Flow: Skill builds skills; our autonomous + meta-recursive-builder + this principles/patterns as meta.
- PT09 Multi-Source-with-Traceability Flow: Extracts from 4+ sources (pack + clones + advisor + skill-creator + our CPs); KG; our P12.
- PT10 Master-Document-Intermediate Flow: MKD 40-60p first; our 00-master/master.md + SKILL as kernel.
- PT11 Validation-with-Auto-Fix Flow: Coverage/schema/lint/real-test + auto fix via SI/plan; our P5 validation.

**➕ Inventions:** Pattern-state in memory/shared_state (which PT applied/covered, CPs per PT, coverage %); Flussi di Patterns as composable (workflow-builder DAGs e.g. PT05-PT01-PT08 core); Live lessons from our (PT05 in 7 files, PT08 in autonomous/meta, PT09 in extracts, PT11 in validator).

**Traceability (P12):** Sources: /home/user/skill-planning-knowledge-pack/02-patterns/ (PT01-PT11 full from uploads), our ANALYSIS (PT violations e.g. PT05 not in early 7 files, PT08 meta not executed, PT09 trace weak in artifacts), CPs/DECs/INDEX (live e.g. PT05 in this + prior 7-file agents, PT08 in autonomous), SKILL (catalog + invariants + PT in visibility), Ruflo (swarm for PT01/PT07/PT08), Content-Forge (9-stage for PT02, MKD PT10, conductor PT01, builders/opt PT03, SI PT07/PT11, failure-logs PT09/PT11), Context-Eng (two-layer for PT09/PT10, cycle for PT02/PT04, 5Qs for PT04/PT15), Skill-Creator (evals for PT03/PT06/PT11, anatomy for PT05/PT10, iteration for PT08/PT03), user complaint ( "stessa cosa per i patters" for PT15 + visibility PT02/PT08), KP-PLAN, clones, our history (ANALYSIS + CPs + 13 prior + this).

**Invariants:** All 10 + P01-P15 + PT01-PT11. Especially P10 (memory after every pattern flow), P12 (trace), P03 (expand PT files), P08 (depth), P07 (three-level in PT01 flows), P09 (FM for PT violations), P13 (meta use to improve self), P02 (disclosure), PT05 (7 files).

**Next:** Handoff to workflow-builder for patterns-pipeline (e.g. PT05-7files + PT01-conductor + PT08-meta flow as DAG); team-builder for patterns-team (patterns-manager + anti-pattern-hunter + principle-codifier + qa for PT verification).

**Status:** Full 7 files deep (P08 start; deepen P5), one-by-one, memory update after (CP/DEC/append/manager/sync both), trace full. Addresses user exactly. Part of >25/40.

*Crafted with Ruflo swarms, Content-Forge rigor, Context-Engineering boundaries, Skill-Creator iteration, and the full 15+ principles + 11 patterns — to intrigue and deliver production architectures. Meta-recursive.*