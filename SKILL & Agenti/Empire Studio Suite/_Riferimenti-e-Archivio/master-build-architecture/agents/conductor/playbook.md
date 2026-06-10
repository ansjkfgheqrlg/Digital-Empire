# Conductor Playbook — 10-Phase Orchestration

Detailed step-by-step execution of the 10-Phase Master Architecture Process (see SKILL.md for overview).

**Phase 0: Memory Bootstrap**
- Run memory_manager.py --init --target=[path] --vision="..."
- Create CP-000, DEC-000.
- Update MEMORY-INDEX.md with vision, sources list, principles to enforce.

**Phase 1-3: Ingestion → Analysis → MKD**
- Handoff to ingestion-agent (A1) with multi-source list.
- Parallel handoff to analysts + knowledge-graph-agent.
- Handoff to mkd-builder-agent (A5) — produce rich 40-60p narrative.

**Phase 4-5: Target + Interactive Scaffolding**
- Use target-advisor + question-designer.
- Generate PLAN-v1.
- Adaptive ASK (8-12 questions).
- Build initial topology + agent specs via swarm-builder + plan-builder.
- Critique + iterate (multiple vN).

**Phase 6: Depth Pass (O1-O5)**
- Parallel or sequenced handoff to optimizers.
- O1 on kernel, O2 on agents (expand to 7 files), O3 references, O4 humanizer, O5 validator.

**Phase 7: Self-Improvement**
- Deploy SI team (failure-detector, triage, phase-planner, silent-observer).
- Populate failure-modes-log/.
- Generate fixes or next PLAN.

**Phase 8: Validation**
- QA team + run validator.py scripts.
- Coverage, schema, real-test simulation (emit Ruflo commands).

**Phase 9: Packaging**
- packaging-expert-agent.
- Produce packaged/ + memory/ final state + .skill if possible.

**Phase 10: Continuous Improvement**
- Emit hooks/background worker instructions.
- Final memory/ with complete INDEX and traceability matrix.

**Handoff Template Example (to memory-ecosystem-builder):**
"Build the memory/ ecosystem for this architecture. Must match user screenshot exactly + extensions from P10, Ruflo, Context-Eng, Content-Forge. Include Python auto-update. Output to target/memory/. Context boundary: only [relevant principles + vision]. Log this handoff as DEC-XXX."

**Failure Recovery:** Log to failure-modes, spawn triage, restart phase or new PLAN-vN.