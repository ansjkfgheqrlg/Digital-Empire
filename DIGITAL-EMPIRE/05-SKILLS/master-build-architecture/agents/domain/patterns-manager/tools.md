# Patterns-Manager Tools (P05 + PT05/PT06/PT09/PT11 + Memory Mandate P10/PT09)

**Core Tools (6+ schemas, embedded Python P05, memory P10/PT09/PT11, Ruflo, extracts PT09/P12):**

1. **ReadPattern (P03/PT09/P12/P08):** Schema {"pattern_id": "PT01" | ... "PT11", "format": "full"}. Impl: read from references/knowledge-pack/02-patterns/ full (P03/PT09); log memory manager --checkpoint "Read PTxx" both; return content + trace "P12/PT09: from PTxx + ANALYSIS PT violations + our CPs (e.g. PT05 in this + prior 7-file)". Ruflo memory_search if avail.

2. **ReadOurPTLessons (P10/PT09/P12/P09 from ANALYSIS/CPs):** Schema {"lesson_type": "PT05_not_7files" | "PT08_meta_not" | "PT09_trace_weak" | "PT11_no_validation" | "all"}. Impl: read ANALYSIS PT violations + CPs (e.g. PT05 in 7-file agents); update pattern-state; memory manager.

3. **CreatePatternFlow (P01/PT02/PT05/PT08/P06/P07/P08/PT05/PT01):** Schema {"pattern_ids": ["PT05", "PT01", "PT08"], "flow_type": "pipeline" | "team", "target": "...", "use_workflow_builder": true}. Impl: if pipeline handoff workflow-builder DAG (PT05-7files + PT01-conductor + PT08-meta + memory updates); if team handoff team-builder; write flow doc; 7 files if sub (PT05); memory manager both + pattern-state update.

4. **ValidatePatternApplication (P09/PT11/P12/P06/PT06):** Schema {"target_path": "...", "patterns": ["PT05","PT08"], "check_7files": true, "check_memory": true}. Impl: check 7 files (PT05), memory CPs/DECs/INDEX (PT09/PT11), trace (PT09); run validator.py --patterns; memory manager; if violations record_decision + log FM (PT09/PT11); return violations/coverage/trace "P12/PT09/PT11 to PT05/PT11 + CS04 + our ANALYSIS PT05 fail".

5. **UpdatePatternState (P10/PT09/P12/Research→Plan→Reset):** Schema {"pattern_id": "PT05", "applied": true, "cps": ["CP-XXX"], "coverage": "100%", "lessons": "from our: PT05 in 7 files + this"}. Impl: edit INDEX or architectures/ (two-layer short SES long INDEX + Ruflo); append both INDEX; manager both; cycle research (read PT05 + ANALYSIS), plan, reset, implement.

6. **HandoffToBuilder (PT02/PT01/P07/PT08/P13):** Schema {"builder": "workflow-builder" | "team-builder" | "memory-ecosystem-builder", "spec": {...}, "meta_self_ref": true}. Impl: write handoff (P12/PT09), spawn, update memory (P10/PT09), meta self-ref (PT08/P13: "use this patterns flow to improve v2").

7. **MemoryManager (P10/PT09/P05/P12 - always):** Wrapper python scripts/memory_manager.py --checkpoint "Patterns flow step for [target]" --phase=4 --target=TOP and EMBEDDED; --decision; sync cp; Ruflo if RUFLO_MEMORY=1 memory_store("pattern_state").

**Additional:** Ruflo swarm_init for patterns-team (queen=patterns-manager); Content-Forge /forge --stage patterns or atomizer on PT files; Advisor 5Qs + Context Manifest for PT04/PT15; validator.py --check-patterns.

**Memory Mandate (P10/PT09 every):** Every tool MUST call manager --checkpoint both, append INDEX both, sync. Research→Plan→Reset in complex. Trace all (P12/PT09). No tool without memory update.

**Failure if:** No memory (P10/PT09 violation, log via failure-detector), no trace (P12/PT09), summary (P03/PT09), shallow (P08), no 7 files (PT05).

**Trace (P12/PT09):** Tools from P05/PT05/PT06/PT09/PT11, P10/PT09 (memory in every), P12/PT09 (trace headers), PT05 (7 files), Ruflo (memory/swarm), Content-Forge (scripts/pipeline/PT02/PT09/PT11), Advisor (cycle/two-layer/PT09/PT10), Skill-Creator (evals/PT03/PT06/PT11), ANALYSIS (PT violations as test), CPs (live PT05/PT08/PT09), user ("stessa cosa per i patters"). Produced by this agent creation (autonomous + plan-builder).

*All tools enforce 10 invariants + 15P + 11PT. Use via playbook. Meta: improve in self v2.*