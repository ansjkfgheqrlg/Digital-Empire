# Agent-Spec-Builder — Memory.md (P10 Self-Improvement + User Screenshot + Two-Layer + Research→Plan→Reset→Implement + Ruflo + Content-Forge + Context-Eng)

**Purpose (➕ Extension per P10/P12/PT05):** This is the 7th canonical file for every agent produced by Master-Architect (beyond content-forge's 7, to enforce "memory ecosystem fin da subito" + P10 "update after every single step" + user screenshot + "ecosistema di memoria che si aggiorna dopo il singolo step" + DEC-002 memory-first + CP-013 restore + our ANALYSIS persistence fix). Every agent spec MUST include this exact memory.md (or adapted for role) with full protocol. This file for agent-spec-builder itself documents how *this* agent uses and updates the ecosystem.

**The Memory Ecosystem (exact from user screenshot + extensions per P10 + Context-Eng + Ruflo + Content-Forge + this skill):**
```
memory/
├── checkpoints/
│   ├── CP-000-....md (bootstrap)
│   ├── CP-XXX-*.md (after every step: "handoff received", "research done", "file X written", "critique received", "iterate vN", "handoff complete")
│   └── (live updates, timestamped, phase, linked principles, actions, rationale, evidence, next, traceability)
├── decisions/
│   ├── DEC-000-....md (ADR format)
│   ├── DEC-XXX-*.md (title, date, context, decision, rationale, alternatives considered, consequences, traceability/sources/principles)
│   └── (e.g. "Use hierarchical topology", "Enforce memory.md in 7 files", "Default to two-layer")
├── sessions/
│   ├── SES-000-....md (initial)
│   ├── SES-XXX-*.md (conversational logs if interactive, ASK answers, human feedback, full dialogue)
│   └── (short-term layer)
├── plans/
│   ├── PLAN-v1-....md (initial)
│   ├── PLAN-vN-....md (iterates per P01)
│   ├── ANALYSIS-AND-IMPROVEMENT-PLAN.md (living audit + ultra-specific plan with ✅ marks)
│   └── (high-density synthesis)
├── architectures/
│   ├── ARCH-001-....md (initial structure)
│   ├── ARCH-XXX-*.md (topology diagrams, component maps, three-level, swarm diagrams)
│   └── (for complex)
└── MEMORY-INDEX.md (living source)
    - Rules (non-negotiable: update after EVERY, two-layer, Research→Plan→Reset→Implement, trace every, failure logged, Python auto)
    - Index of Checkpoints/Decisions/Sessions/Plans/Architectures (appended live)
    - Principles Enforced (P10, P12, PT07, PT09, Ruflo memory, Content-Forge logs, Context-Eng two-layer, user screenshot)
    - Current Status (updated)
    - Update Protocol (after action: run manager or append + re-index)
```

**Two-Layer Memory (exact from Context-Engineering-Advisor/SKILL.md + P10 + Ruflo + Content-Forge + our CP-013):**
- **Short-term layer (sessions/ + current context + short CPs for active build):** Conversational, high-density for current handoff/ASK/research/PLAN/BUILD step. Cleared on RESET (per advisor). Used during chaotic Research phase. E.g. "Current handoff: BUILD agent-spec for topology-designer. ASK answers: [list]. Recent CP-021 batch."
- **Long-term layer (MEMORY-INDEX.md + architectures/ + plans/ + vector/Ruflo AgentDB/HNSW if RUFLO_MEMORY=1 + full past CPs/DECs/SES as reference):** Persistent, traceable, for history + sources + past examples (e.g. "load conductor/system-prompt.md as example of L1 shape", "CP-013 restore details for persistence lesson", "P10 full text", "ruflo README memory sections"). Survives resets. INDEX is the living source of truth for status + all history.
- Hybrid: Always FS for human-readable (INDEX, CPs, DECs, plans) + optional Ruflo memory_store for vector search / fast recall in swarm (per Ruflo + P10). Python manager bridges both.
- Research→Plan→Reset→Implement (Context-Eng full cycle from advisor SKILL.md):
  1. **Research (chaotic, load all, short-term):** Load PT05, P06, P05, P08, PT01, content-forge agent-builder-agent.md full, skill-creator.md, advisor SKILL.md (memory + cycle sections), ruflo full relevant, knowledge-pack P/PT/CS relevant, past CPs/agents/ as examples, user vision + ASK + PLAN-vN. Use short-term for active, long-term INDEX for history. No synthesis yet. Log CP "Research started for [slug]: loaded X sources".
  2. **Plan (synthesize high-density, still short + long):** Synthesize internal PLAN for the 7 files (shape, extracts, examples, failures, memory protocol). Write temp plan if complex. Use plan-builder if needed. Log CP "PLAN synthesized for [slug] 7 files".
  3. **Reset (clear context, per advisor anti-stuffing + two-layer):** Clear short-term (sessions/ active, recent CPs if temp), focus on long-term INDEX + synthesized PLAN only. "RESET performed — now implement clean from PLAN + long-term sources only." Log CP "RESET for [slug] build; context cleared".
  4. **Implement (clean, from PLAN only):** Write the 7 files using only the PLAN + long-term (e.g. exact extracts from INDEX refs, not re-loading all). Strict, no re-research. After each file: CP "Wrote [file]", run manager, append INDEX. Log full.
- Document the cycle in every CP/DEC for this build + in the produced agent's memory.md.

**Python Automation (memory_manager.py + P05 + Ruflo + our scripts/):**
- Full manager at scripts/memory_manager.py (176 lines: ensure_memory_structure, get_timestamp, create_checkpoint (writes CP-XXX-*.md + append INDEX), record_decision (ADR + append), append_to_index, main with argparse --init/--target/--vision/--checkpoint/--phase/--decision/--rationale).
- Usage (always on BOTH targets: the user project being architected + self skill root /home/user/projects/.agents/skills/master-build-architecture for embedded dogfood):
  ```bash
  python /home/user/projects/.agents/skills/master-build-architecture/scripts/memory_manager.py --checkpoint "Handoff received for agent-spec-builder building [slug]" --phase=4 --target=/home/user
  python ... --target=/home/user/projects/.agents/skills/master-build-architecture
  # Same for --decision "Chose X per PT05" --rationale "..." --target=...
  ```
- In code (if Python tool): from scripts.memory_manager import create_checkpoint, record_decision; create_checkpoint(target, desc, phase, linked)
- Ruflo integration: if RUFLO_MEMORY=1 or env, use subprocess "npx ruflo memory store --key=cp-xxx --value=... --target=..." or memory_search; but always FS for INDEX/CPs (human + machine readable per P05/P10/Ruflo hybrid).
- Other: ensure on init, sync with rsync/cp between top /home/user/memory/ and embedded skill/memory/ after batches (as in CP-013/026).
- Manager calls: after EVERY action (handoff, research chunk, file write, critique, iterate, handoff complete). Min 5-7 CPs + 1-2 DECs per agent spec build (as in our CP-017-025 history).
- Auto in tools: WriteFile / Bash / MemoryManager tool always trigger CP before/after.

**Update Protocol (non-negotiable, from P10 + user + INDEX + manager + our CP-013/026):**
1. After any action (even internal): run manager --checkpoint or --decision on BOTH targets (or manual append if tool fail).
2. Append detailed entry to BOTH MEMORY-INDEX.md (top + embedded) with full trace (sources, principles, CPs, what changed).
3. Sync if divergence (cp -r or rsync memory/ between /home/user/ and skill root; as done in restores).
4. For interactive: log to sessions/ + SES-XXX.
5. For decisions: full ADR in DEC-XXX + INDEX.
6. For plans: update PLAN-vN or ANALYSIS with status.
7. At end of build: verify >=5 CPs/1 DEC for this agent, INDEX has entries, memory.md in produced agent documents the protocol, CATALOG/ANALYSIS updated if needed.
8. Silent observer (PT07) + failure-detector monitor for missed updates.
9. Two-layer: short for current action, long for history + sources + this protocol itself.
10. Research→Plan→Reset→Implement: always document in CPs/DECs for the build.

**Research→Plan→Reset→Implement Cycle in Practice (for this agent, from advisor + P10 + our builds):**
- Research: load sources to short-term (read_file multiple, bash find), log CP "Research loaded PT05 + content-forge agent-builder + advisor memory sections + past CPs 017+ + ANALYSIS + ruflo + pack P/PT/CS + user".
- Plan: synthesize (internal or write temp PLAN-agent-spec-xxx.md in plans/), log CP "PLAN: 7 files shape from PT05/P06, extracts from X, memory protocol from P10 + screenshot + advisor, examples from history + CS, failure table from P09 + ANALYSIS + CS03/04".
- Reset: clear short (focus), log CP "RESET: now implement from PLAN + long-term INDEX only (no re-load all sources)".
- Implement: write 7 files (tools first etc), after each: CP "Implemented [file] v1", manager run both, INDEX append "Wrote [file] per BUILD order + trace to PT05 + content-forge + P06 + P10 + CP-xxx + ANALYSIS", sync if needed.
- Repeat for critique/iterate: Research new feedback (short), Plan fixes, Reset, Implement v2.
- End: CP "Build complete for [slug], 8 CPs + 2 DECs logged, cycle followed, memory live in target + self".
- Document in produced memory.md + this one.

**Ruflo Swarm Memory Integration (from ruflo clone + P10 + PT07 + our memory-ecosystem-builder):**
- If building swarm-related agent (e.g. topology, swarm-builder, team): extract full from projects/ruflo/README.md (swarm, queen, memory, federation, MCP, hooks, SONA, agentdb, HNSW, 100+ agents), docs/USERGUIDE, plugins/ruflo-swarm, agentdb.rvf etc.
- Include in tools/playbook/system-prompt: npx ruflo swarm init --name [ ] --memory-first, npx ruflo memory store/search, Ruflo AgentDB for long-term vector in two-layer, federation for multi-skill, hooks for background SI (silent-observer), queen for delegation (handoffs).
- Hybrid: FS for INDEX/CPs/DECs (human readable, P05 md+py), Ruflo memory_store for vector recall in swarm (fast, scalable per Ruflo).
- In memory.md of produced swarm agents: "Use Ruflo memory for shared_state in team topology, hooks for continuous-improver, SONA for self-org. Always FS + INDEX for traceability (P12)."
- Example from our: memory-ecosystem-builder used Ruflo memory notes + our manager.

**Content-Forge Memory Analogy (from clone + CS + our):**
- Content-Forge has failure-modes-log/ (populated by SI), PLAN-v*.md, CS*.md, evals/, references/ (stages/patterns), agents/ with memory in prompts.
- We expand: every agent has memory.md + live memory/ in target + self (dogfood), failure-modes.md + log, CPs/DECs/INDEX as "failure-modes-log + plans".
- In produced agents: "Log to memory/failure-modes-log/ like Content-Forge; use SI agents (failure-detector etc) like Content-Forge Stage 10; MKD + PLAN-vN like their stages."
- Our CP-021 batch + 025 autonomous like their pipeline runs.

**Traceability in Memory (P12 + PT09 + P10 + every entry):**
- Every CP/DEC/INDEX entry / memory.md section: "Trace: P10 + user screenshot 2026-05-30 + Ruflo memory (README + plugins) + Context-Eng advisor two-layer + cycle (SKILL.md) + Content-Forge failure-modes-log + CS03 + our ANALYSIS (persistence fail + restore CP-013) + memory_manager.py (code) + CP-017-026 (history) + PT05/PT07/PT09/P12 + this agent-spec-builder build + [specific source file]."
- KG: links to Pxx.md, PTxx.md, clones paths, advisor/SKILL.md, skill-creator.md, user vision, knowledge-pack/, past CPs/agents.
- Coverage: qa coverage-verifier checks memory atoms too.
- No orphan: every memory action traceable.

**Self-Improvement on Memory (P10 + PT07 + P13 + our loops):**
- This protocol itself improves: feed this memory.md + new CPs (e.g. from P5 SI pass) + new Ruflo details + new user req back to agent-spec-builder (meta) or continuous-improver (once added) to produce v2 memory.md with more (e.g. full Ruflo AgentDB code, more cycle examples, actual vector integration).
- Silent-observer (PT07) + failure-detector + phase-planner + triage watch for missed updates, drift, persistence issues.
- Log SI actions as CPs/DECs (e.g. "SI: added Ruflo vector example to memory.md per P10 loop").
- Dogfood: this skill's own memory/ (top + embedded) is updated by this agent during its builds (as we did for CP-026 etc).
- Meta: the memory ecosystem produced can include this builder's memory.md as template for other memory agents.

**Example Memory Updates During a Build (from our CP-017-026 + playbook examples):**
- CP-017: "Handoff received for conductor; research started. Sources: PT01/PT05/P07... Linked: P10 P12 PT01."
- After tools.md write: CP-017b "Wrote tools.md for conductor [size]; verified canonical + trace to P05 + Ruflo npx. Manager run both targets. INDEX appended."
- DEC-xxx: "Chose to include memory.md as 7th (➕) per P10 + user screenshot + DEC-002; rationale... Trace: P10 + CP-018..."
- After all 7 + critique: CP-017z "conductor 7 files complete; 7 CPs + 2 DECs logged; cycle followed (research load all, plan shape, reset, implement clean); memory live in agents/conductor/memory.md + target memory/ + self. Handoff to qa + depth."
- INDEX append: "- [CP-017] ... Conductor deepened... See CP-017 and ANALYSIS."
- Sync: rsync or cp between top and embedded after batch.
- For meta (Example 6): 9 CPs during self v2 build, DEC "PT08 applied", memory.md v2 updated with more.

**Invariants Enforced in Memory (all 10 + P10 core):**
- 1. Memory from 0: yes, this file + protocol.
- 2. MKD first: mini-MKD in agent.md + plans/ for build.
- 3. No-summary: full expansion in CPs/INDEX/memory.md (no "see history").
- 4. Interactive: ASK/PLAN/ITERATE logged in sessions/CPs/DECs.
- 5. Three-level: L3 Python manager + L2 this agent + L1 conductor delegation.
- 6. Depth + shapes: memory.md is canonical shape, deep protocol.
- 7. Failure first: failures logged in CPs/DECs + failure-modes + global log.
- 8. Trace: every memory entry has trace header.
- 9. Research→Plan→Reset→Implement: documented + used in every build.
- 10. Meta-recursive: this memory.md + protocol can be fed back to improve (P13/PT08).

**Ruflo + Content-Forge + Advisor + Skill-Creator + Pack Extracts (full, no summary, in memory context):**
- Ruflo (from clone README + docs): "Ruflo swarm memory: AgentDB for persistent, HNSW for similarity, SONA for self-org, MCP for multi, hooks for background learning, federation zero-trust. Queen for delegation (handoffs like our). Use memory_store for long-term in two-layer. npx ruflo ... --memory-first. 100+ agents inspiration for our 25+."
- Content-Forge (from clone SKILL.md + agents + CS + PLAN-v* + failure-modes-log/ + evals/): "9-stage pipeline with memory in stages (PLAN-v*, master.md, failure-modes-log populated by SI agents, evals/ for loop). Conductor spawns builders with handoffs logged. Self-improvement Stage 10 with failure-detector. MKD first (PT10). No-summary. Builder-then-optimizer (O1 skill-depth our). Our memory/ extends their logs + plans + CS with CPs/DECs/INDEX + two-layer + P10 mandatory in every agent via this .md."
- Context-Eng Advisor (full SKILL.md): "Two-layer memory: short-term conversational + long-term (vector or FS). Research→Plan→Reset→Implement: allow chaos, synthesize PLAN, clear context, implement clean. 5Qs for ASK, Context Manifest, falsification test, anti-stuffing (use RESET + two-layer). Our protocol bakes this into every agent."
- Skill-Creator (from clone refs/external/skill-creator.md): "Evals loop, iteration, packaging. Anatomy for SKILL.md adapted to agent 7 files (frontmatter in SP, progressive disclosure in agent.md vs details in subs, evals.json shape in evals.md, iteration in playbook). Our memory.md + updates enforce packaging with live memory from day 0."
- Knowledge-pack (P10 full, P12, PT07/PT09, CS03/04, glossary "memory ecosystem", "two-layer", "Research Plan Reset Implement", "canonical files", "shape", "traceability", "meta-recursive", "failure modes", "self-improvement loops"): "P10: memory iterativa, update after every, self-imp. User screenshot + 'fin da subito'. P12: trace source to output. PT07 silent observer. PT09 multi-source. CS03 self-imp mistake (no observer). CS04 bugs (real test). Our protocol + CPs/DECs/INDEX + this .md + manager + sync + cycle = full implementation + expansion of all."
- Our build (ANALYSIS + CPs 000-026 + 15 agents 7 files + SKILL.md + CATALOG + memory/ in top + embedded): "ANALYSIS initial: memory only text, no files (persistence fail, 3/10 artifacts). CP-013: restore from INDEX text to actual files + manager + sync + both layers + DEC-009 fix. CP-017-025: agents deepened with memory updates. CP-026: docs update + start P4. INDEX 25+ appends. Embedded sync. memory.md in all 15 agents. This demonstrates P10/P12 in action. Future: P5 SI on self memory/ for more."

**How This Agent Updates Memory (specific to agent-spec-builder):**
- On handoff receive: CP "Handoff received for agent-spec-builder building [slug]. Context boundary: [list]. Linked P10 P12 PT05 etc."
- During research: CP per major source load or chunk "Loaded PT05 full + content-forge agent-builder-agent.md + advisor memory sections + ANALYSIS + past CPs 017+ + ruflo + pack P10/P12/PT05 etc."
- On PLAN synthesize: CP "PLAN synthesized: 7 files per PT05/P06, extracts from X, memory protocol Y, examples from history + CS, failure table from P09 + ANALYSIS."
- On RESET: CP "RESET performed for [slug]; short-term cleared; implement from PLAN + long-term only."
- After each file write (tools first): CP "Wrote [file].md [lines] for [slug]; verified shape + trace + memory protocol. Manager run on /home/user and skill root. INDEX appended both. Sync checked."
- On critique/validator handoff: DEC "Handoff from agent-spec-builder to coverage-verifier-agent etc: [details]. Rationale: PT06 + P12 + P09. Trace: ..."
- On iterate: CP "Iterate vN for [slug]: [fixes e.g. added memory.md, more traces, depth]. Logged as failure FM-AS-002 + recovery."
- On complete: CP "agent-spec-builder build for [slug] complete. 8 CPs + 2 DECs logged during. Cycle followed. 7 files + memory.md with P10 protocol. Memory live in target + self (embedded). Handoff to qa + depth + conductor. Update CATALOG + ANALYSIS + this memory.md if meta."
- Always: append detailed to both INDEX (with full trace + "See CP-XXX"), run manager both, sync if needed, log in target sessions/ if interactive.
- For meta builds: extra CPs for self-ref, v2 improvements to this memory.md.

**Status:** This memory.md is the living protocol for agent-spec-builder. It was created/updated during its own build (CPs 026+). Every produced agent will have an adapted version. P10 enforced. Will be deepened in P5 (more Ruflo code, actual vector examples, P5 SI feedback, real runs).

**End of memory.md for agent-spec-builder. All atoms traceable to sources listed. Memory updated on creation (see CPs/INDEX). Protocol active.**

**Trace for this memory.md:** Full expansion from user screenshot (verbatim structure), P10-self-improvement-loops.md (full), DEC-002 (memory first), CP-013 (restore full), CP-017-026 (actual updates), ANALYSIS-AND-IMPROVEMENT-PLAN.md (memory criticism + restore + post CP-025), memory_manager.py (full code + usage), Context-Engineering-Advisor/SKILL.md (two-layer full + Research→Plan→Reset→Implement full + 5Qs + anti-stuffing + Context Manifest + examples), Ruflo clone (README full swarm/memory/AgentDB/HNSW/SONA/MCP/hooks/federation/queen + docs + plugins), content-forge2.0 (SKILL.md pipeline + failure-modes-log/ + CS03/CS04 full + PLAN-v* + evals/ + agents with memory in prompts + references), skill-creator.md (packaging + iteration + evals with memory), knowledge-pack P10/P12/PT07/PT09 + CS03/CS04 + glossary (memory terms) + KP-PLAN (P10 section), our SKILL.md (memory section + 10 invariants), CATALOG (memory in status), past agent memory.md (conductor/memory.md, memory-ecosystem-builder/memory.md, etc as templates + their protocols), CPs/DECs/INDEX in top + embedded (live examples). All expanded, no summary, with inline quotes/traces + CPs. P10/P12 first-class. Matches screenshot + extensions exactly. 

**This completes the 7 canonical files for agent-spec-builder. One-by-one impeccable per user + plan + all sources + invariants. Memory updated live during creation (CPs 026+, INDEX appends, manager runs both, sync). Ready for use in swarm. Next: update CATALOG/ANALYSIS, create CP/DEC for this addition, then next agent or batch.**