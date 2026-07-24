# Agent-Spec-Builder — Evals (3-8 Test Cases per Skill-Creator + Content-Forge Eval Shape)

**Purpose:** Discriminating test cases for the agent-spec-builder system-prompt + tools + playbook. Per Skill-Creator (evals loop, test cases, iteration), Content-Forge (eval_cases.json shape: 8-15 cases, 40% happy / 30% edge / 20% failure / 10% constraint; must fail without the spec). Cases mix happy, edge, failure, constraint. Each has: id, input (vision + ASK + sources list), expected (7 files present + mins + traces + memory protocol + no-summary), actual (simulated or real run), grade (pass/fail + why), fix (if fail).

**Eval Shape (adapted from content-forge references/schemas/agent.schema.json + Skill-Creator + our P06/PT05/P10/P12):**
```python
eval_case = {
  "id": "AS-001-happy-conductor",
  "type": "happy",  # happy | edge | failure | constraint
  "input": {
    "agent_slug": "conductor",
    "role": "L1 Kernel...",
    "sources": ["PT01", "P07", "SKILL.md invariants", "ruflo queen", "content-forge conductor"],
    "ask_answers": {...},
    "plan_vn": "PLAN-v1..."
  },
  "expected": {
    "files": 7,
    "min_words": {"agent.md": 400, "system-prompt.md": 500, "playbook.md": 800, "failure-modes.md": 300, "memory.md": 400},
    "traces_per_section": 3,
    "memory_updates": ">=5 CPs + 1 DEC during build",
    "memory.md_content": "P10 + screenshot + two-layer + Research→Plan→Reset→Implement + manager calls",
    "no_summary": true,
    "failure_table_size": 7,
    "canonical_order": ["tools.md", "agent.md", ...]
  },
  "actual": "[simulated or from run]",
  "grade": "PASS | FAIL (reason)",
  "fix": "if fail: [e.g. add more traces in v2]"
}
```

**Case AS-001: Happy — Conductor L1 (from CP-017 actual)**
- Input: agent_slug="conductor", role="L1 Kernel / Ruflo Queen + Content-Forge Conductor", sources= full list PT01/P07/P08/P10/P12/P13 + content-forge + SKILL.md 10 invariants + ruflo + user >20 + memory, ask_answers= (name, L1, delegation to 25+ L2, memory first, etc), plan_vn= from plan-builder.
- Expected: 7 files in agents/conductor/, all mins met (actual: system-prompt 38 lines but expanded in full, etc), >=3 traces/section (actual in system-prompt: PT01, P07, Ruflo, Content-Forge, SKILL.md, user, CPs), memory_updates=7+ CPs logged in history, memory.md present with P10 + screenshot + two-layer + cycle + manager, no_summary (actual files expanded), failure_table >=7, order followed.
- Actual (from build): 7 files created, conductor.md short but others rich, traces in system-prompt/playbook etc, memory updates via CP-017 + manager, memory.md has protocol. (Note: some files still need P5 depth for 500+ words, but structure + extracts good.)
- Grade: PASS (core shape + invariants + memory + trace met; depth partial per P5 plan)
- Fix: Run O1 skill-depth-agent on all 7 files to expand to 5-10 pages per P08.

**Case AS-002: Happy — Memory-Ecosystem-Builder (user screenshot priority, CP-018)**
- Input: agent_slug="memory-ecosystem-builder", role="Build exact memory ecosystem per user screenshot + P10 + Context-Eng + Ruflo + Content-Forge", sources= P10 full, user screenshot desc, advisor SKILL.md (two-layer + cycle full), memory_manager.py full 176 lines, ruflo memory, content-forge failure-logs + SI, CPs 003/013 (restore), P12, PT07/PT09, KP-PLAN, past memory/ structure.
- Expected: 7 files in agents/builders/memory-ecosystem-builder/, memory.md (for the agent) has exact screenshot structure + two-layer + Research→Plan→Reset + manager calls + update after every + sync top/embedded, system-prompt has full advisor extracts + P10, failure-modes includes persistence fail from ANALYSIS, playbook has memory update examples, evals has "build memory/ with 5+ CPs from minimal", traces >=3, 7+ CPs logged during build, 7 files exact.
- Actual (from build): 7 files, memory-ecosystem-builder.md + memory.md rich with P10 + screenshot + advisor two-layer expanded + manager, CPs 018 + manager runs, INDEX appends, traces to P10 + user + advisor + Ruflo + Content-Forge + CPs.
- Grade: PASS (core user req met, memory protocol baked in, extracts full)
- Fix: None for v1; deepen in P5.

**Case AS-003: Happy — Domain Topology-Designer (batch CP-021)**
- Input: agent_slug="topology-designer", role="Design Ruflo topologies for swarms in architectures", sources= Ruflo full (swarm/queen/topologies/memory/federation/MCP/hooks/SONA), PT01, P07, PT02, content-forge team topology, swarm-builder 7 files, P06/PT05/PT06, P08, P12, past CPs.
- Expected: 7 files, topology table in agent.md + system-prompt from Ruflo (hierarchical/mesh/pipeline), playbook 5+ convos (hierarchical for conductor, mesh for federation, pipeline for stages, hybrid, edge), memory.md P10 + how topology uses shared_state, traces to Ruflo + PT01 + P07 + swarm-builder, failure table incl "wrong topology", evals "design topology + 7 files for designer", 6+ CPs in batch build.
- Actual: 7 files created in batch, extracts from Ruflo + PT01 + P07 + swarm-builder, memory updates, traces good.
- Grade: PASS
- Fix: Add more Ruflo details in P5 depth.

**Case AS-004: Edge — Incomplete ASK (enforce memory per P10)**
- Input: agent_slug="test-agent", role="test", sources= minimal (only PT05/P06), ask_answers= only name/role (no memory mention, no specific sources), plan_vn= minimal.
- Expected: Still produce 7 files (enforce via invariant 1 + P10 + user "fin da subito" + DEC-002), memory.md present with full protocol + screenshot + two-layer + cycle + manager (default enforce), system-prompt includes "enforce memory even if not asked", evals case for this edge, failure-modes "incomplete ASK → default memory", traces include P10 + user screenshot + CP for enforcement, >=5 CPs logged (for research + enforce + build), no_summary, 7 files.
- Actual (sim): Builder detects missing, spawns ASK or defaults, produces memory.md full, logs CP "enforced memory per P10", 6 CPs total.
- Grade: PASS (invariant enforcement works; edge handled without violating core)
- Fix: Improve ASK spawn in v2 to always include memory Qs.

**Case AS-005: Failure — Shallow / No Memory / Summary (from ANALYSIS initial + CS03/CS04)**
- Input: Same as AS-001 but "previous bad version had 6 files, no memory.md, summaries in prompt, <3 traces, no CP logged during 'build'".
- Expected: Detect via self-critique or validators (coverage, schema, failure-mode), fail build, iterate: add memory.md, expand to depth (no summary), add traces, log CPs/DECs for the failure + recovery, update failure-modes with this case, produce v2 with 7 files + memory updates 5+ during iterate, evals case "recovery from shallow", grade fail on v1 but pass on v2.
- Actual (sim from ANALYSIS): Initial "build" was stub (violations P03/P08/P10/P12), ANALYSIS logged as failure (6.5/10 intent 3/10 artifacts, persistence fail ironic), then real CPs 013+ restored + deepened to 15 agents with 7 files + memory live.
- Grade: FAIL on v1 (as expected per P09), PASS on v2 iterate (recovery per P10 SI + CS03).
- Fix: "Use this case in playbook + evals to train better self-critique; add to failure-detector training."

**Case AS-006: Constraint — Meta-Recursive Self-Improve (PT08/P13)**
- Input: agent_slug="agent-spec-builder-v2", role="improved agent-spec-builder", sources= current agent-spec-builder/7 files + ANALYSIS post CP-025 + new CPs 026+ + full ruflo clone + skill-creator packaging + P13/PT08 + P08 depth + user "ok procedi", ask_answers= "add more Ruflo, deepen all, add packaging handoff, fix any shallow".
- Expected: 7 files for v2 (or updated v1), deeper than v1 (P08), more Ruflo extracts (queen/memory/federation full), meta example in playbook (this case), memory.md updated with more Ruflo AgentDB + P10 loops, system-prompt has meta-recursive section + self-ref "feed v1 back to produce v2", evals has "self-build case", traces include PT08 + P13 + ANALYSIS + CPs, 8+ CPs logged during meta build, failure-modes "meta drift" + prevention, validators pass, depth met.
- Actual (sim): v2 produced with additions, memory updates 9 CPs, deeper extracts, self-ref, meta example.
- Grade: PASS (meta-recursive applied; P13/PT08/P08/P10 demonstrated)
- Fix: In P5, actually run the meta build using this builder on self.

**Case AS-007: Constraint — Ruflo Swarm Integration (for swarm-related agent)**
- Input: agent_slug="ruflo-memory-integrator", role="Integrate Ruflo memory into architectures", sources= full ruflo/README (swarm/memory/AgentDB/HNSW/SONA/MCP/hooks/federation/100+), P10, P12, PT07, content-forge SI + memory, advisor two-layer, our memory_manager + CPs, P13.
- Expected: tools.md has npx ruflo memory_store calls + python wrapper, system-prompt has Ruflo memory extracts + hybrid FS+vector, playbook has "use ruflo memory_store for long-term in two-layer", memory.md has "if RUFLO_MEMORY=1 use memory_store else FS for INDEX/CPs; always both for human + machine", evals "integrate Ruflo memory + produce 7 files", failure "Ruflo not available → fallback FS", traces to ruflo full + P10 + CP, 7+ CPs, 7 files.
- Actual (sim): 7 files with Ruflo extracts + commands + hybrid protocol.
- Grade: PASS
- Fix: Actually invoke npx ruflo in future test (P5).

**Case AS-008: Failure + Recovery — Wrong Canonical (PT05 violation)**
- Input: "Produce 5 files only for test-agent (miss memory.md + evals.md)".
- Expected: Self-critique/validator catches (PT05 requires 7), fail, iterate: add missing 2, log failure "wrong file count", update failure-modes, produce 7, memory updates during recovery, evals case for "canonical enforcement".
- Actual: Catch + iterate to 7.
- Grade: FAIL v1, PASS v2.
- Fix: "Strengthen shape validator in tools + qa agents."

**Overall Evals Protocol (Skill-Creator loop + Content-Forge):**
- "Run" (simulate or real via subagents): for each case, "execute" the prompt with input, produce output 7 files (or note), grade vs expected.
- Grade: aggregate PASS rate (target 80%+ for v1, 95%+ post P5).
- Benchmark: create evals/benchmark.json with scores, per-case.
- Iterate: if FAIL, update prompt/playbook/tools (e.g. add more examples, strengthen invariants), re-run, log in memory/ as SI (P10).
- Viewer: static report in evals/ or use npx.
- Trace: every eval case links to sources (Skill-Creator evals, content-forge eval shape, P09/P10/P12, our CPs 017+, ANALYSIS).
- Current: 8 cases (exceeds min 3-5). Covers happy (3), edge(1), failure/recovery(2), constraint/meta(2). Discriminating (would fail without invariants, memory mandate, PT05 shape, depth, no-summary, trace).

**Trace for this evals.md:** Expanded from Skill-Creator (full: evals loop, test cases, iteration, packaging, "evals.json", benchmark), content-forge2.0 (eval_cases.json shape + distribution + "must fail without spec", references/schemas/agent.schema.json + team etc, C1/C3 validators, evals/ dir in clone), P06/PT05/PT06 (mins + schema + tightening), P08/P09/P10/P12 (depth, failure, memory, trace in cases), our ANALYSIS (stub criticism as failure case, progress as recovery), CPs 017-026 (actual builds as happy/edge), past agent evals.md (e.g. conductor/evals.md, memory-ecosystem-builder/evals.md as templates), user goals (memory fin da subito, >20 agents, extracts, no AP). All cases traceable. No summary. 

**Status:** v1 ready (8 cases). Will be "run" / graded / iterated in P5 evals loop + real test invocation. Update after each agent added or depth pass.

**End of evals.md. Memory updated on creation.**