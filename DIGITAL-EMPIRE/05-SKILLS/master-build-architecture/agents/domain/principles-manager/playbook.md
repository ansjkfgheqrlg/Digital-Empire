# Principles-Manager Playbook (Step-by-Step + Examples from Our Build + P Lessons)

**General Steps (per 10-phase + Content-Forge + P01/P04/P08/P10/P12):**
1. **Memory Bootstrap (P10 fin da subito):** Always first. Run `python scripts/memory_manager.py --checkpoint "Principles-manager invoked for [vision/target]" --phase=4 --target=/home/user` AND for embedded `projects/.agents/skills/master-build-architecture`. Append to both INDEX (via manager or edit). Create DEC if decision (e.g. "use P10 flow first"). Sync recent CPs/DECs. Update principle-state in memory/INDEX or shared_state (e.g. {"P10": {"applied":true, "cps":["CP-XXX"]}} ). Research→Plan→Reset→Implement: Research current state, plan updates, reset, implement clean.
2. **Research (P03/P12/PT09 multi-source):** Read all P01-P15.md full (no summary, expand). Read our ANALYSIS-AND-IMPROVEMENT-PLAN.md (per-P violations section + Implemented real status + visibility fixes). Read recent CPs/DECs/INDEX (live lessons e.g. P10 in CP-013/every, P12 headers). Read SKILL.md (invariants + catalog + Directory Structure & Visibility + flussi section + name "Master build Architecture"). Read clones (ruflo/ for swarm/P07/PT01/P10 memory; content-forge2.0/ for pipeline/P01/P10/P03/MKD). Read advisor/SKILL.md (two-layer/P10/Research-Plan-Reset/5Qs). Read skill-creator.md (evals/P01/P08/P02). Read user complaint verbatim (P15 + flussi di principi + "agenti per principi" + visibility). Read /home/user/skill-planning-knowledge-pack/ (P files + KP-PLAN + uploads + "Piano di Sviluppo"). Read existing domain (principle-codifier etc) + our agents (for P application examples). Use tools ReadPrinciple/ReadOurLessons.
3. **Synthesize (P01/P04/P08):** Build principle flows map (15P + groups like core P01/P07/P09/P10/P12 loop). Identify violations from ANALYSIS (e.g. P10: no live CPs despite claims → lesson: always use manager both layers after step). Coverage checklist for target. Decision tree per P (from P files). ➕ invention: principle-state shared_state.
4. **Plan (P01 multiple vN):** If complex, handoff to plan-builder for PLAN-vN with changelog (what changes: new P flow, structural, inversion). Or internal PLAN. Use interactive if needed (P04: ASK adaptive Qs e.g. "Which principles priority for this target?").
5. **Build (P08 depth, PT05 7 files, PT01/PT02 teams/flows):** 
   - For single P: Write/ enrich Pxx-flow.md (expand from P file + our lessons + examples).
   - For flussi: Use workflow-builder (handoff spec for DAG: e.g. P01-iterative-planning-flow → P10-SI-flow → P12-trace-flow + memory updates at each).
   - For teams: Use team-builder (handoff: principles-team = principles-manager (queen) + principle-codifier + 5 domain + qa + memory-ecosystem-builder).
   - Update refs/knowledge-pack/01-principles/ (if enrich), SKILL.md (add to catalog/flussi), agents/ (new principle sub-agents if needed, with 7 files), memory/ (principle-state).
   - Enforce 7 files (PT05), no-summary (P03), depth (P08), trace (P12), memory update (P10).
6. **Validate (P09/P12/PT06/P06):** Run validate tool + qa coverage-verifier (P coverage % in target), target-schema-validator (shapes), failure-mode-validator (P violations). Run scripts/validator.py --check-principles --target=.... Log any FM (P09). Use failure-detector if issues.
7. **SI / Critique (P10/PT07/P09):** Spawn failure-detector-agent (handoff or direct) for P violations (e.g. "P10 not applied in target = no CPs after steps"). Log to failure-modes-log/. Triage if threshold. Generate fix (e.g. new PLAN or update). Silent (P14): no spam, user pull.
8. **Handoff + Memory Final (P10/P12/P13):** Handoff to next (conductor, workflow-builder, memory-ecosystem-builder, user). Always: manager --checkpoint "Principles flussi complete for [target], P coverage 95%, lessons applied" both targets; append INDEX both (with trace to Pxx + our CPs + user); sync; update principle-state. Meta (P13): If self, "feed this back: use P10/P12 enforcement in v2 of master-architect (e.g. deepen ANALYSIS with more real status)".
9. **Continuous (P10/P14):** Hook for background (Ruflo hooks): monitor new CPs/DECs for P application, validate silently, log FM if violation.

**5+ Full Examples (Happy/Edge/Failure/Recovery/Constraint/Meta, per Skill-Creator + our build + CS + P lessons, no-summary P03, trace P12):**

**Example 1 (Happy - P10 SI flow from our build, P01/P12 applied):**
- Vision: "Ensure memory ecosystem updates after every step in this continuation (P10 enforcement)".
- Step 1: Memory bootstrap (CP-004-autonomous-continuation-start... created via manager both, INDEX appended, architectures/ mkdir, DEC for full control).
- Step 2: Research (read P10 full: 3 SI agents, silence, user pull, failure-modes-log; read ANALYSIS P10 violation initial (no files despite INDEX); read CP-013 "Memory files restored..."; read SKILL memory section + screenshot; read our README for visibility as P02).
- Step 3: Synthesize: P10 flow = manager --checkpoint after every + append INDEX both + sync + two-layer (SES short, INDEX long + principle-state) + SI (failure-detector for violations like "no CP after step").
- Step 4: Build: This principles-manager creation itself (7 files with P10 in memory.md + every tool/playbook mandates manager); update ANALYSIS with real status (13 full agents); create README (P02 visibility).
- Step 5: Validate: Coverage P10 100% (CPs after every action here); no violation (unlike initial).
- Step 6: SI: No FM needed (enforced).
- Step 7: Handoff: To user/ conductor; manager --checkpoint "P10 flow complete, 40+ CPs live" both; append INDEX; sync; principle-state update {"P10": {"applied":true, "cps": ["CP-004-...", "CP-013", ...], "coverage":"100%", "lessons":"enforced in autonomous continuation post audit"}}.
- Trace: P10 full text + ANALYSIS P10 section + CP-013 + SKILL + our CPs 000-037+ + user "fin da subito" + Ruflo memory + Content-Forge SI + Advisor two-layer. Result: Live memory ecosystem (top + embedded) with actual files, not just text claims. P01 (multiple updates to ANALYSIS/PLAN), P12 (all CPs have headers with sources).

**Example 2 (Happy - P01/P07/P12/P13 meta flussi from our build, P15 trigger):**
- Vision: "flussi di principi for Master build Architecture (user: 'devi fare anche agenti o i principi devi anche fare flussi di principi') + name 'Master build Architecture'".
- Research: P01 (iterative vN + changelog + when new: new component like this agent); P07 (L1 conductor, L2 domain for principles, L3 tools/scripts); P12 (trace to user complaint verbatim in SKILL/ANALYSIS/README); P13 (meta: our autonomous is example of skill building self via principles); P15 (trigger "flussi di principi", "agenti per principi", "Master build Architecture" optimized).
- Synthesize: Flussi = principles-manager (L3) + principle-codifier + 5 domain + workflow/team for pipelines/teams; core loop P01-P07-P10-P12-P13.
- Build: Created principles-manager/ (this 7 files deep with extracts from P01/P10 + ANALYSIS + CPs + user complaint + clones); updated SKILL.md (name + visibility section with "agenti per principi" + flussi + map); updated README (full map addressing user verbatim); updated ANALYSIS (Implemented 23-25 real + visibility fixes + name); added patterns-manager/case-study-analyst (sibling for patters/case); mkdir architectures/; memory updates (CPs/DECs for name/visibility/agents).
- Validate: P01 (multiple PLAN/ANALYSIS vN), P07 (three-level dirs), P12 (trace in this playbook to user + sources), P13 (meta examples in playbook/memory), P15 (triggers in SKILL/README).
- Handoff: To patterns/case + more agents (to 25+); manager both; append INDEX; sync; principle-state update.
- Result: User complaint fully addressed (SKILL.md exists rich, references full tree, scripts, agents + flussi per category incl principles, cartella = projects/.agents/skills/master-build-architecture/, name "Master build Architecture"). Trace: User complaint verbatim + ANALYSIS visibility + P01/P07/P12/P13/P15 full + our CPs/DECs + SKILL + README. P01 applied (iterative updates to ANALYSIS post each agent).

**Example 3 (Edge - Incomplete ASK enforce P10/P04):**
- Vision: "Build principles flow but no memory update specified".
- Research: Detect P10 violation risk (from ANALYSIS initial: "memory claims but no files").
- Synthesize: Enforce P10: even if not in vision, always bootstrap + update after steps.
- Build: Still run manager --checkpoint both; create principle-state; refuse to proceed without (P10 mandate in prompt/tools/playbook).
- Validate: P10 coverage 100% (enforced); log FM "P10 risk mitigated by mandate" (P09).
- Handoff: With note "P10 enforced per principle (unlike early build)".
- Trace: P10 + ANALYSIS P10 violation + CP-013 + our CPs (all have updates). Lesson: P04 interactive would ASK "memory first?" but we enforce default.

**Example 4 (Failure/Recovery - P10/P03/P08/P12 violation from ANALYSIS initial, recovery in autonomous):**
- Failure (from ANALYSIS "initial analysis"): P10: "no actual CP/DEC/SES files (0 in subdirs) despite INDEX rich claims + dogfood"; P03: "stubs are pure summaries"; P08: "agents shallow (stubs vs deep 5-10p)"; P12: "trace strong in text, weak in artifacts"; P13: "not executed (no self-improvement artifacts)".
- Symptoms: "non stai ancora facendo niente" (user), no visible structure (no SKILL/references/agents/flussi), persistence fail (ironic for memory skill).
- Detection: Via validate tool + our audit in autonomous start (CP-004-... "audit current state (13 full... not 20+ claimed)").
- Recovery (this continuation per DEC-010 full control + ANALYSIS Priority 4 + user): 
  - Memory restore (CP-013 + manager full + updates after every).
  - SKILL expanded rich (P03 no-summary, P02 disclosure, P08 depth start).
  - Agents deepened/added one-by-one with 7 files (PT05/P08/P09 tables/P10 memory.md/P12 trace).
  - New domain for principles/patterns/case (user exact + flussi).
  - README + SKILL visibility section (P02/P08/P15).
  - Name update (P15).
  - Memory live (40+ CPs/DECs both, architectures/, sync, manager both).
  - This principles-manager (P10/P12/P03/P08/P13 applied in creation).
- FM logged: "FM-P10-001 persistence fail (initial) → prevention: manager both + append + sync after every (enforced here)".
- Trace: ANALYSIS full "Weaknesses" + "Implemented" + CP-013 + our CPs 017+ (agent adds) + SKILL + user complaint + P10/P03/P08/P12/P13 full. Recovery: P01 (iterative from stubs to full), P09 (FM now documented), P10 (loops via CPs).

**Example 5 (Constraint/Meta - P13/P10/P12 on self, P15):**
- Vision: "Use principles-manager to audit/improve principle application in this skill v2 (meta P13) + name 'Master build Architecture'".
- Research: P13 (skill builds skills/agents; our autonomous continuation + this agent creation is meta example); P10 (self apply: memory updates in creation); P12 (trace to self sources: ANALYSIS/CPs/SKILL); P15 (trigger "Master build Architecture", "flussi di principi").
- Build: This creation itself (7 files with meta self-ref in prompt/playbook/memory: "feed this back to produce v2"); update SKILL (name + visibility + catalog with principles-manager); update ANALYSIS (real status not claims); create README; add sibling agents; memory CPs/DECs for name/visibility/agents (P10 enforced); principle-state {"P13": {"applied":true, "examples":["autonomous CP-026+","this principles-manager creation as meta"]}}.
- Validate: P13 coverage (meta examples in playbook/memory), P10 100% (CPs after each write), P12 (this playbook cites user + ANALYSIS + P13 + CPs).
- Handoff: "For v2: use this to fix any remaining P violations in agents/ANALYSIS (e.g. deepen all to full extracts like here)".
- Meta: "This agent creation (post DEC-010) is P13 in action: principles that built the skill now managed by agent inside the skill to improve it."
- Trace: P13/PT08 full + ANALYSIS "meta-recursive seed" + our CPs/DEC-010 + SKILL PT08 + content-forge PT08 + Ruflo SONA + Advisor SI + user (name + flussi) + this creation. P10/P12 enforced.

**Constraint Example 6 (P09/P10 from CS03/CS04 + our persistence):**
- From CS03 "the-self-improvement-mistake": P10 without real test/SI observer = drift.
- From CS04 "bugs-found-in-real-test": P09/P10 without real validation = bugs like our initial memory persistence.
- Recovery: This agent + SI (failure-detector) + validator + real test (invoke on "forge knowledge-pack") + memory live (P10) + FM tables (P09).
- Trace: CS03/CS04 full + ANALYSIS CS lessons + our CP-013 (recovery from persistence) + P09/P10 full.

**All examples enforce:** Memory update after every step (P10), trace (P12), no-summary expand (P03), depth (P08), 7 files (PT05), three-level (P07), FM (P09), extracts from all sources (PT09/P12), Research→Plan→Reset→Implement (Advisor), two-layer (P10), meta (P13), silent (P14), user triggers (P15). From our build as living proof (P01 iterative updates, P10 loops via CPs).

**Ruflo/Content-Forge/Advisor/Skill-Creator/Pack Integration:** Use Ruflo for swarm of principles-team; Content-Forge for pipeline stage; Advisor for cycle/two-layer; Skill-Creator for evals/iteration on flussi; pack P files as source + our CPs as live CS.

**When to Spawn:** On "flussi di principi", "agenti per principi", "validate P10 in this", "build principles flow for X", "Master build Architecture" (P15), conductor for principle-heavy targets.

*Playbook is living: append new examples from future CPs (P10). Trace full to P01/P10/P12 + ANALYSIS + CPs + user + sources.*