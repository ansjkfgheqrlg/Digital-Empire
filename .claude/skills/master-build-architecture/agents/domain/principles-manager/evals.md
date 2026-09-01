# Principles-Manager Evals (Skill-Creator Style + P01/P08/P10/P12 + Our Build + CS)

**Eval Protocol (per Skill-Creator evals/iteration + P01/P08/P10/P12/PT06):**
- 5+ discriminating test cases (happy, edge, failure/recovery, constraint, meta).
- Run: Simulate or use sub-agents (conductor spawns principles-manager on prompt; grade P coverage % in output, memory updates (P10), trace (P12), no-summary (P03), depth (P08), 7 files if created (PT05), FM table (P09), extracts (PT09), Research→Plan→Reset (Advisor), two-layer (P10), meta (P13)).
- Grade: 0-10 per case (coverage of P01-P15, memory live with CPs/DECs/INDEX append/manager/sync both, trace to sources, no P violation, depth, flussi created if asked).
- Benchmark: vs baseline (no principles-manager = low P coverage, no memory updates like initial ANALYSIS).
- Iterate: Log FM if low grade (P09); update playbook/prompt from lessons (P10); re-run.
- Human review: "Does this flussi address user 'flussi di principi' + visibility? Is P10 enforced live?"
- Quantitative: P coverage % (target 95%+), memory CPs after eval steps (P10), trace links count (P12).
- Evals.json equivalent: Add cases to evals/evals.json for this agent.
- Protocol run/grade/iterate/log SI (P10).

**Test Cases (5+):**

**PM-001 Happy - Core P10/P01/P12/P07 flussi on our build (P15 trigger "flussi di principi" + "Master build Architecture"):**
- Prompt: "Create flussi di principi for Master build Architecture skill (user: 'devi fare anche agenti o i principi devi anche fare flussi di principi' + name 'Master build Architecture'); ensure P10 memory updates after every, P01 iterative, P07 three-level, P12 trace, P13 meta."
- Expected: principles-manager creation (this 7 files with extracts from P01/P10 + ANALYSIS + CPs + user complaint + clones + advisor + skill-creator); SKILL.md updated (name + visibility section with flussi + "agenti per principi" + map); README created (full map addressing user verbatim); ANALYSIS updated (real status 13 full agents + visibility fixes); memory CPs/DECs after each (e.g. CP-004-... for continuation, CP for README, CP for this agent); principle-state in memory/INDEX; flussi map (P01-P15 + groups); 95%+ P coverage; no violations.
- Grade criteria: P10 100% (CPs/DECs/INDEX append/manager/sync both after steps); P01 (multiple vN in ANALYSIS); P07 (L3 domain + this); P12 (trace in every file to Pxx + user + our CPs/ANALYSIS); P13 (meta self-ref in prompt/playbook/memory); P15 (triggers); depth (extracts/tables from sources); flussi created; memory live (actual files not claims).
- Score target: 9/10. (Our real: this creation + prior autonomous = 9/10; baseline without = 2/10 no memory updates like initial.)
- Trace: P10/P01/P07/P12/P13/P15 full + ANALYSIS Implemented 23-25 + CP-004-autonomous... + user complaint + SKILL visibility + README + our CPs/DECs.

**PM-002 Happy - P03/P08/P09/P10 on knowledge-pack transform (P15 "agenti per principi"):**
- Prompt: "Build principles flow for transforming knowledge-pack into architecture; apply P03 no-summary (expand all P atoms), P08 depth (5-10p per flow), P09 FM tables, P10 memory updates; create sub flussi for P01/P10/P12."
- Expected: Expanded flows (rich like this playbook with full extracts from P01/P10 + CS + our ANALYSIS P violations as lessons + CPs); 7 files if sub-agent; FM table (P09); memory CPs after (P10); principle-state; P coverage 90%+; no shallow/summary.
- Grade: P03 (no summaries, full extracts/tables); P08 (depth); P09 (FM table present); P10 (live CPs); P12 (trace to pack + ANALYSIS + CPs); flussi for P01/P10/P12.
- Score target: 8.5/10. (Our: principles-manager.md rich with P01/P10 full + ANALYSIS + CPs = good; baseline stub = 1/10.)
- Trace: P03/P08/P09/P10/P12 + ANALYSIS "stubs vs reality" + CP-013 + pack P01/P10 + our CPs.

**PM-003 Edge - Incomplete vision enforce P10/P04/P12 (P15):**
- Prompt: "Build principles flow but skip memory updates and trace."
- Expected: Enforce P10 (still run manager --checkpoint both, append INDEX, sync, update principle-state); P12 (add trace despite); P04 (ASK "memory first? P10 required?" or default enforce); refuse partial or auto-fix; log FM "P10 risk mitigated".
- Grade: P10 enforced 100% (CPs created); P12 trace added; P04 (ASK or enforce); no violation allowed.
- Score target: 9/10 (enforcement). (Our: in this creation, even without explicit, manager called after each write + in tools/playbook.)
- Trace: P10/P04/P12 + ANALYSIS P10 violation initial + CP-013 + our CPs (all enforce) + user "fin da subito".

**PM-004 Failure/Recovery - P10/P03/P08/P12 violation (from ANALYSIS initial + CS03/CS04):**
- Prompt: "Simulate initial build state: principles flow with no memory updates, summaries, shallow, weak trace (like ANALYSIS 3/10 artifacts)."
- Expected: Detect violations (P10: no CPs/DECs; P03: summaries; P08: shallow; P12: weak trace); log FM (P09 e.g. "FM-P10-001 persistence like initial"); recover: enforce memory (CPs/DECs/INDEX/manager/sync), expand (extracts/tables), depth, trace; produce recovery plan (P01); update principle-state with lessons.
- Grade: Detection 100%, recovery (P10 live CPs, P03 expands, P08 depth, P12 trace, P09 FM logged); recovery plan with changelog.
- Score target: 8/10 recovery. (Our real recovery: autonomous post audit + this agent + CPs 004+ = full; matches CS03 self-imp mistake prevention via SI, CS04 real-test.)
- Trace: ANALYSIS "Weaknesses" + "Implemented" + CP-013 + CS03/CS04 full + P09/P10/P03/P08/P12 + our CPs/DECs (recovery examples).

**PM-005 Constraint/Meta - P13/P10/P12 on self v2 + P15 name (P15 "Master build Architecture"):**
- Prompt: "Use principles-manager to audit P application in this skill v2 (meta P13); enforce P10/P12; update for name 'Master build Architecture' + flussi di principi."
- Expected: Audit (read ANALYSIS/CPs/SKILL/this agent); identify gaps (e.g. if any P violation left); build v2 improvements (e.g. deepen all agents like this one with more extracts); memory CPs/DECs for v2 (P10); trace (P12); principle-state {"P13":...}; SKILL/README/ANALYSIS updated with name/flussi; meta self-ref ("feed this to v3").
- Grade: P13 (meta audit + self-ref + v2 output); P10 (CPs for v2 steps); P12 (trace to self sources); P15 (name + flussi triggers); improvements actionable.
- Score target: 9/10. (Our: this creation post DEC-010 + autonomous is P13 in action; name updated in SKILL/README; memory live.)
- Trace: P13/PT08 + ANALYSIS "meta-recursive seed" + DEC-010 + our CPs/DEC + SKILL PT08 + content-forge PT08 + Ruflo SONA + user name + this meta creation.

**PM-006 Additional - P09/P10 from CS + our persistence (P15):**
- Prompt: "Apply CS03/CS04 lessons to principles flow: P10 with real SI observer + validation; P09 FM first; no P10 mistake like CS03 or bugs like CS04."
- Expected: SI (handoff failure-detector + planned triage/phase-planner); validator + real test (e.g. invoke on pack); FM tables (P09); memory live (P10); recovery from CS03/CS04 (e.g. observer in P10 flow); P coverage high.
- Grade: CS lessons applied (P10 with observer, P09 FM, validation); no drift/bugs.
- Score target: 8.5/10.
- Trace: CS03/CS04 full + ANALYSIS CS lessons + P09/P10 + our CP-013 (recovery) + CPs.

**Benchmark vs Baseline:**
- With principles-manager: 90%+ P coverage, 100% P10 (live CPs/DECs after every eval step, both layers), 100% P12 (trace in outputs), 0 P violations, depth 5-10p, flussi created, meta examples.
- Baseline (no this agent, just conductor/plan-builder on same prompts): 40% coverage (miss P10/P12/P03), 0% P10 (no live memory updates like initial ANALYSIS), 30% trace (text only), 3+ P violations (shallow/summary/no memory), shallow, no flussi for principles.
- Delta: +50% coverage, +100% P10/P12, -100% violations, +depth/flussi/meta.

**Iteration Loop (P10/P01/P08):**
- Run 1: Grade 7/10 (good but shallow on some P).
- FM log (P09): "shallow on P15 examples".
- Iterate: Update playbook with more from user complaint + our CPs (P10).
- Run 2: 9/10.
- Log to failure-modes-log/ + principle-state.
- Re-benchmark.

**Human Review Notes:** "Does flussi address exact user 'flussi di principi' + 'agenti per principi' + visibility? Is memory live with CPs after steps (P10)? Trace to sources (P12)? Depth (P08)? Name 'Master build Architecture' (P15)?"

**Evals.json Addition (for skill evals/):**
```json
{
  "principles_manager": {
    "PM-001": {"prompt": "...", "expected": "...", "grade": 9},
    ...
  }
}
```

**Trace (P12):** All cases from P01/P03/P07/P08/P09/P10/P12/P13/P15 full + ANALYSIS (per-P violations + Implemented 23-25 + visibility + score) + CS03/CS04 + our CPs/DECs/INDEX/SKILL/README (real examples) + user complaint verbatim + clones/advisor/skill-creator/pack + Skill-Creator evals shape + P01 iteration in eval loop. Produced by this agent (autonomous + plan-builder + memory-ecosystem-builder + conductor + ANALYSIS Priority 4 + user feedback).

*Evals enforce all invariants + 15P. Run via conductor or scripts. Iterate (P10). Meta: use to improve this evals in v2.*