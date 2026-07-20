# Principles-Manager Tools (P05 Markdown+Python + Ruflo + Memory Mandate)

**Core Tools (6+ with schemas, embedded Python per P05, memory update mandate P10/P12, Ruflo integration, extracts from sources):**

1. **ReadPrinciple (P03/P12/P08):**
   - Schema: {"principle_id": "P01" | "P02" | ... "P15", "format": "full" | "summary" | "operational" (default full to enforce no-summary P03)}
   - Impl (Python embedded):
     ```python
     import os
     from pathlib import Path
     def read_principle(principle_id, format="full"):
         base = Path("references/knowledge-pack/01-principles/")
         pfile = base / f"{principle_id}-*.md"
         # glob and read full (P03 expand)
         content = pfile.read_text()
         if format == "operational":
             # extract "Come applicarlo", decision tree, examples, connections
             pass
         # Always log to memory (P10)
         run_memory_manager("--checkpoint", f"Read {principle_id} for flow", phase=4)
         return {"content": content, "trace": f"P12: from {pfile} + ANALYSIS per-P violations + our CPs (e.g. P10 in CP-013)"}
     ```
   - Ruflo: If available, memory_search("P01 iterative") via subprocess.
   - Trace: P01 full + P03/P08/P12 + our ANALYSIS (P01 application in iterative build) + CP-00X.

2. **ReadOurLessons (P10/P12/P09 from ANALYSIS/CPs):**
   - Schema: {"lesson_type": "P10_memory_fail" | "P03_stub" | "P08_shallow" | "P12_weak_trace" | "P13_not_meta" | "all", "target": "this_build" | "general"}
   - Impl: Read ANALYSIS "per-P violations" section + specific CPs/DECs (e.g. CP-013 for P10 restore as positive lesson, initial ANALYSIS for negative). Update memory with principle-state coverage.
   - Example output: "P10 violation in initial: no actual CPs/DECs files despite INDEX claims (persistence fail) → fixed in CP-013 restore + manager full + updates after every (this continuation). P03: stubs in early agents → now full expands in new (this principles-manager.md rich with extracts/tables)."

3. **CreatePrincipleFlow (P01/P06/P07/P08/PT05/PT01):**
   - Schema: {"principle_ids": ["P01", "P10", "P12"], "flow_type": "pipeline" | "team" | "single", "target": "new_architecture" | "self_improve", "use_workflow_builder": true}
   - Impl: 
     - If flow_type pipeline: handoff to workflow-builder with DAG (e.g. P01-iterative → P10-SI → P12-trace steps + memory updates).
     - If team: handoff to team-builder (principles-manager + principle-codifier + domain + qa).
     - Write flow doc in refs or assets (P06 shapes).
     - Always 7 files if creates sub-agent (PT05).
     - Memory: create CP for flow creation, update principle-state shared_state.
   - Extracts: P01 (iterative vN + changelog), P07 (three-level in flow), PT01 (conductor subagents for team), our 10-phase as example (P01 applied in build).

4. **ValidatePrincipleApplication (P09/P12/P06/PT06):**
   - Schema: {"target_path": "path/to/target", "principles": ["P01","P10"], "check_memory": true, "check_7files": true}
   - Impl (Python):
     ```python
     def validate_application(target_path, principles, check_memory=True):
         violations = []
         if check_memory:
             if not (Path(target_path)/"memory/checkpoints").exists() or len(list(...)) < 3:
                 violations.append("P10 violation: no live CPs after steps (like initial ANALYSIS)")
         # check 7 files for agents, trace headers, extracts etc.
         # run validator.py --principles
         run_memory_manager("--checkpoint", f"Validated {principles} on {target_path}", phase=4)
         if violations:
             record_decision("P violation found", ...)
         return {"violations": violations, "coverage": "85%", "trace": "P12 to P09/CS03 + our ANALYSIS P10 fail"}
     ```
   - Use qa agents + scripts/validator.py (P06/PT06/P09/P12).
   - Ruflo: memory_search for prior violations.

5. **UpdatePrincipleState (P10/P12/Research→Plan→Reset):**
   - Schema: {"principle_id": "P10", "applied": true, "cps": ["CP-013", "CP-034"], "coverage": "90%", "lessons": "from our build: enforced after every step in autonomous"}
   - Impl: Edit memory/INDEX or shared_state.json in memory/plans/ or architectures/ (two-layer: short in SES, long in INDEX + Ruflo). Append to both INDEXes. Run manager.
   - Cycle: Research (read P10 + ANALYSIS), Plan (state update), Reset (clear temp), Implement (write state + CP).
   - Trace: P10 full + Advisor two-layer + our CPs (P10 in every) + CP-013 restore.

6. **HandoffToBuilder (PT02/PT01/P07/P13):**
   - Schema: {"builder": "workflow-builder" | "team-builder" | "memory-ecosystem-builder", "spec": {...}, "meta_self_ref": true}
   - Impl: Write handoff doc (P12 trace), spawn via conductor or direct (Ruflo npx if avail), update memory (P10), meta self-ref if target self (P13: "use this principles flow to improve v2 of this skill").
   - Extracts: PT02 pipeline handoff, PT01 subagents, P07 L2 specialists, our meta-recursive-builder (PT08) + autonomous as example.

7. **MemoryManager (P10/P05/P12 - always use):**
   - Wrapper: python scripts/memory_manager.py --checkpoint "Principles flow step X for [target]" --phase=4 --target=TOP; same for EMBEDDED; --decision if needed.
   - Sync: cp recent CPs/DECs between /home/user/memory/ and skill/memory/.
   - Ruflo: if RUFLO_MEMORY=1, integrate memory_store for principle-state.
   - Two-layer: short in current SES, long in INDEX + principle-state.

**Additional (Ruflo MCP / Content-Forge scripts / Advisor):**
- Ruflo: swarm_init for principles-team (queen = principles-manager, subs = codifier + domain), memory_store("principle_state", json).
- Content-Forge: /forge --stage principles or invoke atomizer on P files.
- Advisor: Use 5Qs + Context Manifest for P15 trigger of this agent.
- Validator: python scripts/validator.py --check-principles --target=...

**Memory Mandate (P10 every tool call):** Every tool above MUST call memory_manager --checkpoint (both targets), append INDEX both, sync files. Research→Plan→Reset→Implement in complex tools. Trace all (P12). No tool without memory update.

**Failure if:** No memory update (P10 violation, log via failure-detector), no trace (P12), summary instead of extract (P03), shallow (P08), no 7 files (PT05).

**Trace (P12):** Tools designed from P05 (md+py), P10 (memory in every), P12 (trace headers), PT05 (7 files), Ruflo (memory/swarm), Content-Forge (scripts/pipeline), Advisor (cycle/two-layer), Skill-Creator (evals), our ANALYSIS (P violations as test cases), CPs (live P10), user (flussi di principi). Produced by this agent creation (autonomous + plan-builder).

*All tools enforce 10 invariants + 15P. Use via playbook. Meta: improve tool use in self v2.*