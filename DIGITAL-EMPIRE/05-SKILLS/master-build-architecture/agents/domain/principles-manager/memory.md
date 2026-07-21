# Principles-Manager Memory (P10 Self-Improvement + Screenshot Exact + Two-Layer + Research→Plan→Reset→Implement + Ruflo/Content-Forge/Advisor/Skill-Creator + Our Build Lessons)

**P10 Mandate (fin da subito, user screenshot + P10 + Context-Eng two-layer + Ruflo memory + Content-Forge failure-logs + our CP-013 + every autonomous step):** This agent **ALWAYS** updates the memory ecosystem after *every* single step (tool call, research, plan, build, validate, handoff, write). No exception. Two-layer: Short-term (session conversational in SES-*.md + current context) + Long-term (persistent INDEX + vector/Ruflo AgentDB + principle-state shared_state + our CPs/DECs as live examples). Research→Plan→Reset→Implement cycle (per Advisor): Research (all sources + our CPs/ANALYSIS), synthesize to high-density PLAN for flussi, **RESET context**, implement clean from PLAN only. Update both top (/home/user/memory/) and embedded (projects/.agents/skills/master-build-architecture/memory/) . Run memory_manager.py --checkpoint/--decision --target on both; append both INDEX.md (with trace P12); sync files (cp recent CPs/DECs/INDEX updates); update principle-state (shared_state for which P applied/covered in target, CPs per P, coverage %). Architectures/ for principle-state docs. This is core to "fin da subito" + P10 loops + SI (P10/PT07) + our recovery from initial persistence fail (CP-013 + manager full + updates after every in this continuation).

**Exact Structure (user screenshot + extensions from P10 + Ruflo + Content-Forge + Context-Eng + our build):**
```
memory/
├── checkpoints/
│   ├── CP-004-autonomous-continuation-start-....md (this creation)
│   ├── CP-004-created-readme.md-for-visibility-....md
│   ├── CP-013-priority-1-memory-restore-....md (P10 recovery from initial fail)
│   ├── ... (40+ live, updated after every step in autonomous + prior)
│   └── CP-XXX-principles-manager-....md (this + every sub-step)
├── decisions/
│   ├── DEC-take-full-autonomous-control-....md (DEC-010)
│   ├── DEC-add-readme.md-+-explicit-visibility-....md
│   ├── ... (8+ ADR-style with context/decision/alts/rationale/consequences/trace P12)
│   └── DEC-XXX-principles-manager-....md (for flussi decisions)
├── sessions/
│   ├── SES-001-initial-setup-....md (full log)
│   └── SES-XXX- (short-term conversational for this session)
├── plans/
│   ├── PLAN-v1-master-architect-creation.md
│   ├── ANALYSIS-AND-IMPROVEMENT-PLAN.md (living, with per-P violations + Implemented real + visibility fixes + this update)
│   └── PLAN-vN- (for flussi if complex, per P01)
├── architectures/
│   ├── ARCH-001-memory-architecture-....md (two-layer FS + vector + principle-state)
│   └── ARCH-XXX-principle-state-....md (shared_state for P coverage)
└── MEMORY-INDEX.md   ← Living source of truth. Updated after *every* step (append via manager or edit; rules, indexes, principles list, update protocol, our CPs/DECs as P10 examples)
```

**Rules Enforced (non-negotiable, from P10 + user screenshot + Advisor + Ruflo + Content-Forge + our ANALYSIS/CPs/INDEX):**
- Update after EVERY step (tool call, decision, handoff, artifact, write, validate, research, plan). This creation: CP/DEC after dir, after each .md write, after batch.
- Two-layer: Short-term (SES + current in context/this memory.md) + Long-term (INDEX + principle-state in architectures/ or plans/ + Ruflo AgentDB if avail + our CPs/DECs/ANALYSIS as persistent lessons e.g. P10 enforcement in CP-013 + autonomous CPs).
- Research→Plan→Reset→Implement: Research (P files + ANALYSIS per-P + CPs + SKILL + clones + advisor + skill-creator + user + pack), synthesize PLAN for flussi (high-density), RESET (clear temp context), implement clean (write flows + updates from PLAN only). Documented in CPs/INDEX.
- Trace every entry (P12): Headers in CPs/DECs (Timestamp/Phase/Linked Principles/Traceability with sources P10/P12/PT07/user screenshot/Ruflo/Content-Forge/Advisor + our CPs/ANALYSIS); INDEX appends with trace; all outputs cite >=3 sources + our history.
- Failure modes logged (P09): To failure-modes-log/ (via SI); this agent's FM table (P09); SI (failure-detector + planned) for P violations (e.g. P10 slip).
- Python auto-update (P05): This script memory_manager.py (full, tested on both targets); validator.py (memory live check); run after every.
- Principle-state (➕ invention, P10/P13 meta): shared_state (JSON or section in INDEX/architectures/): e.g. {"P01": {"applied": true, "cps": ["CP-001", "CP-004-..."], "coverage": "95%", "lessons": "from our build: multiple vN in ANALYSIS"}, "P10": {"applied": true, "cps": ["CP-013", "every autonomous CP-004-..."], "coverage": "100%", "lessons": "enforced after every step via manager both + append + sync; recovery from initial fail"}, ... "P13": {"applied": true, "examples": ["autonomous continuation post DEC-010", "this principles-manager creation as meta"], ...}}. Updated in every step. Two-layer: short in SES, long in INDEX + Ruflo.
- Silent/conditional (P14/PT07): Background SI; user pull ("show principle state", "P10 coverage in this build"); no spam.
- Ruflo memory (P10): If RUFLO_MEMORY=1, use memory_store("principle_state", json); memory_search for prior P lessons; hooks for background principle validation/SI.
- Content-Forge analogy (P10/P09): failure-modes-log/ like their Stage 10; SI agents like their failure-detector/triage/phase-planner; P10 loops feed P01 next vN.
- Context-Eng (P10): Two-layer exact (short conversational + long persistent); Research→Plan→Reset→Implement cycle; 5Qs for P15 trigger of this; Context Manifest for principle boundaries.
- Skill-Creator (P10/P01/P08): Evals/iteration on flussi (P10 loops); packaging includes memory/; progressive disclosure (P02: lean here, full in P files + this + playbook examples from our CPs).
- Our build lessons (P10/P12/P13 from ANALYSIS/CPs/INDEX): Initial violation (P10: "no actual files despite INDEX claims" → CP-013 restore + manager full + updates after every in autonomous/this = recovery); P12 (headers + trace in all CPs/DECs/INDEX/outputs); P13 (autonomous + this meta creation = executed); P09 (FM tables now in all new agents, logged); live in top + embedded synced.

**Update Protocol (10 steps, P10/P12, after every action - this creation followed exactly):**
1. Action (e.g. write this memory.md).
2. Research (if needed: read P10 + ANALYSIS P10 section + CP-013 + SKILL memory + our CPs).
3. Plan (mental or via plan-builder: "update principle-state for P10/P13, create CP/DEC").
4. RESET (clear temp).
5. Implement: Run manager --checkpoint "Principles-manager: [step desc e.g. memory.md written with P10 mandate]" --phase=4 --target=/home/user ; same --target=projects/.agents/skills/master-build-architecture .
6. Append to both INDEX.md (via manager or edit: "- [CP-004-XXX] ... trace to P10/P12 + ANALYSIS + user + sources").
7. If decision: record_decision both (ADR with trace).
8. Update principle-state (edit INDEX or architectures/ARCH-XXX or plans/ : add to shared_state {"P10":..., "P13":...}; append trace).
9. Sync: cp/rsync recent CPs/DECs/INDEX updates between top and embedded (e.g. find CP-004-* | xargs cp ...).
10. Verify: ls both memory/checkpoints/ | wc -l (increase); cat both INDEX | tail -5 (appended); principle-state visible; log in SES if interactive. Run validator.py --check-memory.

**Examples from Our Build (P10/P12/P13 live, P01 iterative, P09 FM):**
- CP-013 + DEC-009: "Priority 1: Memory sub-files fully restored... persistence violation fixed" (P10 recovery from initial "no files despite claims"; two-layer; manager run; sync; trace to P10/P12/PT07/user screenshot/Ruflo/Content-Forge/Advisor + ANALYSIS).
- Every autonomous CP-004-... (this continuation): After dir mkdir, after README write, after each .md for this agent, after batch. E.g. "CP-004-autonomous-continuation-start: audit current state (13 full 7-file agents... proceeding to add principles-manager...)" ; "CP-004-created-readme..."; DEC for full control + visibility.
- principle-state update (this): {"P10": {"applied":true, "cps":["CP-004-...", "CP-013", "prior 40+"], "coverage":"100%", "lessons":"enforced after every (manager both + append + sync); from ANALYSIS initial fail recovered"}, "P13": {"applied":true, "examples":["DEC-010 full control autonomous", "this principles-manager creation (meta: principles that built skill now manage principles in skill)"], "coverage":"90%"}, "P12": {"applied":true, "examples":["all CPs/DECs headers + this memory.md trace section + SKILL/ANALYSIS/README"], ...}, ...}.
- INDEX appends (both): After every, with trace (e.g. "- [CP-004-XXX] 2026-06-04: ... Trace: P10/P12 + ANALYSIS + user complaint + P files + clones + advisor + skill-creator + our CPs").
- Sync: After manager, cp recent between layers (e.g. our sync for CPs/DECs).
- SES: Short-term log of this session (P10 two-layer).
- ARCH: For principle-state (e.g. ARCH-XXX-principle-state.md with shared_state + rationale from P10 + our lessons).
- P01: Multiple updates to ANALYSIS (Implemented sections post each agent/batch); PLAN-v1 + ANALYSIS as vN.
- P09: FM for P10 violation (initial) logged in ANALYSIS + this failure-modes.md; SI (failure-detector) planned in P10 flow.
- P13 meta: This memory.md + creation uses our CPs/ANALYSIS as input (self); "feed this back to v2: use P10 enforcement + principle-state in all future".
- P12: Every CP/DEC/INDEX/this file has "Trace: P10/P12 + ... + our CPs/ANALYSIS/DEC-010 + user + sources".

**Ruflo/Content-Forge/Advisor/Skill-Creator/Pack Integration (P10/P12):**
- Ruflo: memory_store("principle_state", json from shared_state); memory_search("P10 lessons from our CPs"); swarm for principles-team (queen=this, subs= codifier+domain+qa+memory-builder); hooks for background P10 validation/SI.
- Content-Forge: failure-modes-log/ + SI agents (like their Stage 10); P10 loops feed their P01 iterative + MKD/PLAN; scripts/ like their Python for auto.
- Advisor: Two-layer exact; Research→Plan→Reset→Implement (documented in CPs/INDEX); 5Qs for P15 of this agent; Context Manifest for principle boundaries in memory.
- Skill-Creator: Memory/ in packaged/ (P05/P06); evals/iteration on P10 (P01/P08/P10); this memory.md as example of bundled resource.
- Pack: P10/P12/PT07/PT09/CS03/04/glossary as source + our CPs/ANALYSIS/DECs as live "CS" for P10 (e.g. persistence recovery as positive CS03-like); KP-PLAN for tree.

**How This Agent Updates (P10/P12/P13 meta, step-by-step with our examples):**
- On invoke: Bootstrap (manager both, CP/DEC, principle-state init, INDEX append).
- On research: CP "Researched P10 + ANALYSIS P10 + CP-013 + SKILL memory", update principle-state coverage.
- On plan: CP "Planned flussi for P01/P10/P12/P13", DEC if decision.
- On build (write 7 files): CP after each (e.g. "principles-manager.md written with P10 mandate + extracts"), principle-state {"P10":... "P13":...}, INDEX append.
- On validate: CP "Validated P10 100% on target (live CPs both layers)", log FM if violation.
- On SI: Handoff failure-detector, CP "SI for P10 violation", update failure-modes-log.
- On handoff: CP "Handoff complete, P coverage 95%", manager both, append, sync, principle-state final.
- On meta self: "This update (P10 in memory.md + creation) is P13: principles managing principles in the skill that uses them to build architectures".
- Example from this: After README write → CP-004-created-readme... (both); after principles-manager.md → CP for it; etc. All in INDEX/CPs/DECs.

**Two-Layer in Practice (P10 + Advisor + Ruflo + our CPs):**
- Short-term: This SES + current context (e.g. "current principle-state before this write: P10 95%").
- Long-term: INDEX (appended with trace), principle-state in architectures/ARCH-XXX or plans/ANALYSIS section, our CPs/DECs/ANALYSIS (persistent lessons e.g. P10 in CP-013 + autonomous), Ruflo AgentDB if avail (vector for "P10 enforcement examples").
- Research→Plan→Reset→Implement: In CP-013 (research initial fail, plan restore, reset, implement manager + files); in this creation (research ANALYSIS/CPs, plan additions, reset, implement rich with P10 mandate).

**Status (this creation, P10 100% enforced, P12 full trace, P13 meta applied, P01 iterative, P09 FM, P07 three-level, P08 depth start):**
- Top + embedded: 40+ CPs (incl new for this + README + autonomous), 8+ DECs (incl for control/visibility), SES, plans (PLAN-v1 + ANALYSIS updated), architectures/ (now with principle-state), both INDEX appended live.
- principle-state: Updated with P10/P13/P12/P01/P07/P08/P09/P15 etc from this + prior.
- Sync: Performed (cp for recent).
- Validator: Will run post (P06/PT06/P09/P12).
- Trace full (P12): P10/P12 + ANALYSIS (P10 section + CP-013 + Implemented 23-25 + visibility) + our CPs/DECs/INDEX (live) + SKILL (memory section + screenshot + name + flussi) + README (map + user complaint) + user complaint verbatim + P10 full + Ruflo/Content-Forge/Advisor/Skill-Creator + pack P10/P12/CS + clones + DEC-010 + this creation.

**P10 Loops (P10/P01/P13/P09):** CPs/DECs feed P01 next vN (e.g. ANALYSIS updates post this); SI (failure-detector) for violations (P09); meta (P13) self-ref ("use this P10 enforcement in v2"); principle-state accumulates coverage/lessons for future (P10 memory institutional).

*This memory.md is the P10 kernel for this agent. Enforce in all (prompt/tools/playbook/evals/failure-modes). Meta: this P10 in creation improves self. Living: append from future CPs (P10 SI). All 10 invariants + 15P + P10 fin da subito + screenshot exact + two-layer + cycle + extracts + our lessons.*