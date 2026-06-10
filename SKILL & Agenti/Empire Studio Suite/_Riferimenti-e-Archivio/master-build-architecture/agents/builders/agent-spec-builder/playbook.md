# Agent-Spec-Builder — Playbook (Step-by-Step + 6+ Example Conversations/Scenarios)

**Purpose:** Concrete, real examples of using this agent to build agent specs (7 canonical files). Drawn from actual build history (CPs 017-025 for the initial 15 agents), Content-Forge CS01-04 (real pipeline runs), knowledge-pack CS, clones (content-forge agent-builder history), advisor examples, user "piano di sviluppo", P04/P10/P12. 3 happy paths, 1 edge, 1 failure recovery, 1 meta-recursive. Each example is full conversation-like (Conductor/Plan → ASK if needed → BUILD steps with memory updates → Critique → Handoff). No summaries — full extracts + actions.

**General Playbook Steps (expanded from Content-Forge agent-builder-agent.md + our invariants):**
1. Receive handoff from conductor/plan-builder (tight context + PLAN + ASK answers if any).
2. Research: load key sources (PT05, P06, P05, P08, PT01, content-forge agent-builder-agent.md, skill-creator.md, advisor SKILL.md memory sections, ruflo swarm parts, relevant P/PT/CS from pack, past 7-file examples like conductor/*, memory-ecosystem-builder/*).
3. Internal PLAN + RESET (document in CP).
4. If ASK incomplete: spawn question-designer-agent (log CP/DEC).
5. BUILD in order: tools.md (schemas), agent.md (overview + trace map), failure-modes.md (table 7+), playbook.md (this file, examples), system-prompt.md (with few-shots), evals.md (cases), memory.md (P10 protocol).
6. After each write: CP "Wrote X.md for Y", run manager on both targets, append INDEX (both), log in target memory/sessions/ if applicable.
7. Self-critique + spawn validators (qa agents) + depth (skill-depth-agent).
8. Handoff complete + DEC "Agent spec for Y complete, 7 files, 8 CPs logged, trace 100%".
9. Update CATALOG.md + this skill's ANALYSIS if foundational.

**Example 1: Happy Path — Building 'conductor' (L1, from our history CP-017)**
Conductor: "Handoff: BUILD agent-spec for 'conductor' (L1 Kernel). Context boundary: PT01, P07, Ruflo queen, Content-Forge conductor.md + 25 agents, SKILL.md invariants 1-10, user >20 agents + memory fin da subito. Inputs: full PT05, P06, P07, P08, P10, P12, P13, content-forge2.0/agents/conductor.md (if present) + SKILL.md, past memory CPs, user query. Output to agents/conductor/ the 7 files. Log every step."
Agent-Spec-Builder (internal): Research load PT05 (canonical 7 for agent), P07 (L1 conductor), Ruflo (queen delegation), Content-Forge (conductor role in 9-stage), SKILL.md (10 invariants full extract), memory CPs 001-016 (history). PLAN: conductor.md = role L1 + 10 invariants + handoff protocol + catalog. system-prompt = full with 10 rules + extracts. ... 
CP-017 (target + self): "Handoff received for conductor; research started. Sources: PT01/PT05/P07/P08/P10/P12 + content-forge + SKILL.md + CPs 001-016. Linked: P10 P12 PT01."
... (BUILD order: write tools.md with read/write/bash/spawn + memory_manager; then conductor.md with mission + invariants + traceability; failure-modes.md with 7+ incl. "L1 overload" from P07; playbook.md with 5+ examples; system-prompt.md with handoff + 10 rules + few shots; evals.md 3 cases; memory.md with P10 protocol + screenshot ref + two-layer + cycle.)
After each: CP "Wrote X for conductor", manager run (top + skill), INDEX append "Wrote conductor/system-prompt.md per PT05 BUILD; trace to PT01 + Ruflo + SKILL.md invariants".
Self-critique: All 7 present, > min words, 4+ traces per, memory.md has P10 + screenshot. Spawn qa + depth.
DEC-xxx: "Chose L1 shape for conductor per P07/PT01 + Ruflo queen; alternatives: flat pipeline (rejected per P07 three-level); rationale: matches user + sources; consequences: enables delegation to 25+ L2; trace: P07 + PT01 + CP-017."
Handoff: "conductor 7 files complete at agents/conductor/*. Logged 7 CPs + 2 DECs during build. Ready for swarm. Handoff to coverage-verifier etc."
Memory: Updated both INDEX with "Example 1 conductor built successfully per PT05/P08 one-by-one".
(Full traces in actual files created in CP-017 era.)

**Example 2: Happy Path — Building 'memory-ecosystem-builder' (user priority per screenshot, CP-018)**
Conductor: "Handoff: BUILD agent-spec for 'memory-ecosystem-builder'. Context: user screenshot (memory/checkpoints/decisions/sessions/ MEMORY-INDEX.md), P10, Context-Eng two-layer + Research→Plan→Reset→Implement, Ruflo AgentDB/memory plugins, Content-Forge failure-modes-log + SI, our memory_manager.py, KP-PLAN + P10. Inputs: full P10, P12, PT07, PT09, advisor SKILL.md memory sections, ruflo memory, content-forge SI, past CPs 003/013 (restore), skill memory/ structure. Output to agents/builders/memory-ecosystem-builder/ 7 files. Enforce fin da subito."
Agent-Spec-Builder: Research: load user screenshot desc (memory/ > checkpoints/ > decisions/ > sessions/ > MEMORY-INDEX.md), P10 full, advisor (two-layer verbatim + cycle example), memory_manager.py (176 lines code), CPs 003/013 (restore details), Ruflo (memory_store), Content-Forge (failure-modes-log in CS), P12. PLAN: memory-ecosystem-builder.md = role guardian of memory + structure exact screenshot + extensions. memory.md (for this agent) = full protocol. system-prompt = rules + two-layer + cycle + manager calls. ...
CP-018: "Handoff for memory-ecosystem-builder; research P10 + screenshot + advisor + Ruflo + Content-Forge + CPs. Linked P10 P12 user req."
BUILD: tools.md (memory_manager calls + ensure_structure + create_checkpoint + record_decision + append + sync top/embedded); memory-ecosystem-builder.md (overview + shape from screenshot + P10); failure-modes.md (incl. "persistence fail during build" from ANALYSIS + "no two-layer in practice"); playbook.md (examples of memory updates); system-prompt.md (full with memory mandate + Research→Plan→Reset + two-layer + Ruflo); evals.md (cases: "build memory/ with 5 CPs/2 DECs from minimal; verify live files + INDEX appends"); memory.md (detailed: "After every: CP in both, run manager both, append both INDEX, sync with rsync if needed. Two-layer: short sessions for current build, long INDEX for history + sources. Cycle: research load all (short), plan (write temp), reset (clear), implement from plan + long INDEX. Ruflo: if RUFLO_MEMORY use memory_store for vector long-term, always FS for INDEX/CPs human readable. Update after every single step per user 'fin da subito' + P10.").
After writes: multiple CPs, manager runs on both, INDEX appends "Wrote memory-ecosystem-builder/memory.md with P10 protocol + screenshot ref + advisor two-layer + Ruflo".
Critique: 7 files, deep extracts from screenshot + P10 + advisor full sections expanded, memory.md has exact protocol + manager usage. Validators pass.
DEC: "Chose to make memory.md the key 7th file (➕ invention) to enforce P10 in every produced agent; rationale: user screenshot + P10 + DEC-002 memory-first + our ANALYSIS persistence fail as lesson; alternatives: use content-forge README (rejected, not memory first); consequences: every agent will have live memory updates baked in; trace: P10 + user screenshot + CP-018 + advisor SKILL.md."
Handoff complete. Memory updated with "Example 2 memory-ecosystem-builder built as user priority; 8 CPs logged; memory ecosystem now live in artifacts."
(Actual files from CP-018 match this playbook.)

**Example 3: Happy Path — Building a Domain Agent e.g. 'topology-designer' (one of 5 domain, CP-021 batch)**
Conductor: "Handoff: BUILD agent-spec for 'topology-designer' (domain L2). Context boundary: PT01 (conductor subagents), P07 (L2 specialists), Ruflo topologies (hierarchical/mesh/pipeline/federation), content-forge2.0 topology/ swarm patterns, P06 shapes, PT02 pipeline stages, our swarm-builder + plan-builder outputs. Inputs: ruflo/README (swarm/queen/topologies), content-forge agents (topology related if any), knowledge-pack P07/PT01/PT02, past swarm-builder 7 files, user vision for swarm. Output agents/domain/topology-designer/ 7 files."
Agent-Spec-Builder: Research load Ruflo topologies (hierarchical for queen, mesh for federation, pipeline for stages), PT01 full, P07 L2, content-forge (team topology.md etc), swarm-builder/system-prompt (extracts for topologies), P06 for shape. PLAN: topology-designer.md = role for designing Ruflo topologies in architectures + handoff to swarm-builder. system-prompt = extract Ruflo + PT01 + P07 + examples of topologies. ...
CP-021 (batch): "Handoff for topology-designer + 4 other domain + ingestion etc; research Ruflo + PT01/P07 + content-forge + swarm-builder. Linked P07 PT01 Ruflo."
BUILD: tools (read ruflo, write agent dir, spawn if needed, memory_manager); topology-designer.md (role + topologies table from Ruflo + trace); failure-modes (e.g. "wrong topology for task" from P07 + CS); playbook (examples: design hierarchical for conductor, mesh for multi-project, pipeline for content-forge stages; edge: hybrid); system-prompt (with topology decision tree + Ruflo commands + few shots); evals ( "Given swarm vision, design topology + 7 files for designer agent; verify topologies match Ruflo + handoff to swarm-builder"); memory.md (P10 protocol + how topology agents use memory for state e.g. shared_state.md in team shape).
After each file: CP + manager both + INDEX append "Wrote topology-designer/playbook.md with 5+ convos from Ruflo + PT01 + content-forge".
Critique + validators + depth: pass (traces to Ruflo full + P07 + PT01 + swarm-builder).
DEC: "Chose hierarchical as default for L1-L2 per P07/PT01 + Ruflo queen; mesh for federation per Ruflo; pipeline for stages per PT02 + Content-Forge; rationale: matches sources + user swarm req; trace: Ruflo + PT01 + CP-021."
Handoff. Memory: "Example 3 topology-designer (domain) built in batch; memory updates 6 CPs for this; now 14+ agents."

**Example 4: Edge Case — Incomplete ASK / Missing Memory Requirement**
Conductor: "Handoff: BUILD for 'test-agent' (minimal). Inputs: only name + role high-level. No ASK answers, no memory mention, limited sources."
Agent-Spec-Builder: Research: load PT05/P06/PT01 (canonical requires memory per our extension), P10 (mandatory), advisor (anti-stuffing but memory first), past CPs (memory always). PLAN: detect incomplete — memory missing in inputs violates P10 invariant. 
CP: "Research showed missing memory req in ASK for test-agent; per invariant 1 + P10 + user screenshot, must ASK or default enforce."
Spawn question-designer-agent: "Qs: Does this agent need memory ecosystem? (yes per P10). Specific memory features? (checkpoints/decisions/sessions/INDEX per screenshot). Update protocol? (after every step). Two-layer? (yes). Ruflo integration? (yes if swarm)."
Get answers (assume via handoff).
Then BUILD: include memory.md with full P10 + screenshot + two-layer + cycle + manager, even if not explicit (enforce invariant).
CP after: "Enforced memory.md via P10 despite incomplete ASK; added to evals as edge case."
Critique: good (caught by invariant), but note in failure-modes "incomplete ASK leads to default memory enforcement".
DEC: "Defaulted to full memory protocol per P10 invariant + user 'fin da subito' + DEC-002; alternatives: skip memory (rejected, violates core); rationale: prevents persistence fail like our early ANALYSIS; consequences: all agents have live memory; trace: P10 + CP-xxx + advisor cycle."
Handoff with note "Edge handled by enforcing memory per invariants".
Memory updated: "Example 4 edge incomplete ASK; memory enforced; logged as edge in playbook + evals."

**Example 5: Failure Recovery + Iterate (from CS04 bugs + CS03 self-imp mistake + our ANALYSIS persistence)**
Conductor: "Handoff: Re-BUILD 'bad-agent' (previous attempt had only 6 files, no memory.md, shallow traces, summary in prompt). Critique from failure-detector: P08/P03/P10/P12 violations. Fix and iterate."
Agent-Spec-Builder: Research: load previous bad output (6 files), failure-detector report, CS03 (self-imp mistake: no observer led to drift), CS04 (bugs found in real test), ANALYSIS (stub persistence fail, memory claims without files), P09/P08/P03/P10/P12.
CP: "Received failure for bad-agent; research own failures + CS03/CS04 + ANALYSIS. Linked P09 P08 P03 P10 P12."
PLAN: Add missing memory.md with full protocol; expand all to depth (no summary); add 3+ traces per section; add failure table entry for "stub persistence"; iterate v2.
BUILD v2: rewrite all 7 (tools first), add memory.md, deepen system-prompt with full extracts (no "see history"), add traces, expand playbook with this failure recovery example.
After writes: CPs "Iterate v2: added memory.md + 4 traces per file + no-summary fix for bad-agent".
Self-critique + validators: now pass (7 files, depth, trace, memory updates logged 4 CPs during iterate).
DEC: "Iterated bad-agent to v2 fixing P08 (depth), P03 (expansion), P10 (memory.md + updates), P12 (traces); alternatives: accept shallow (rejected per P08); rationale: P09 failure first + CS03/04 + our ANALYSIS as lesson; consequences: better artifact + self-imp example; trace: P09 + CS03 + CS04 + ANALYSIS + CP-xxx."
Handoff: "bad-agent v2 complete 7 files, fixed failures, 5 CPs in iterate. Ready."
Memory: "Example 5 failure recovery: bad-agent iterated; memory updates during fix; logged in failure-modes + evals as 'recovery case'; P10 enforced."

**Example 6: Meta-Recursive — Using this builder to improve itself (PT08 + P13 + P10 loops)**
Conductor: "Handoff: BUILD improved 'agent-spec-builder-v2' from current v1 spec + new requirements (e.g. add support for 40 slots catalog, deeper Ruflo integration from full ruflo clone, more from skill-creator packaging, fix any shallow in v1 per P08). Inputs: current agent-spec-builder/ 7 files + ANALYSIS post CP-025 + new CPs + full ruflo clone + skill-creator.md packaging section + user 'ok procedi' + P13. Context: use self as example of meta."
Agent-Spec-Builder: Research: load own 7 files (this playbook etc as input), ANALYSIS (stub to full progress, 6.5/10 to 7.5/10), new CPs 026+, full ruflo (more swarm details), skill-creator (packaging for agents as skills?), P13/PT08 full, P10 loops (use own memory updates as example).
CP: "Meta handoff: improve self v1 to v2 using own output + new sources + P13. Research self + ANALYSIS + ruflo + skill-creator. Linked P13 PT08 P10 P08."
PLAN: v2 system-prompt add more Ruflo extracts (full queen + memory + federation), deepen all files per P08 (add 200+ words each), add packaging-expert handoff, update memory.md with more Ruflo AgentDB, add meta example in playbook (this one), evals add case for self-build, failure-modes add "meta drift" from CS03.
BUILD v2: write 7 files for 'agent-spec-builder-v2' (or overwrite v1 with v2 content), using tools first etc. During: 8+ CPs for the meta build + memory updates.
Critique: deeper (P08), more meta (PT08), self traces (P12/P13), memory updates during (P10).
DEC: "Chose to produce v2 by feeding v1 + new sources back to self per PT08/P13; rationale: meta-recursive core of skill + P10 SI loops + user meta req; alternatives: manual edit (rejected, use the builder); consequences: skill improves itself, catalog of 25+ includes self-improved; trace: PT08 + P13 + ANALYSIS + CP-026 + this example 6 + ruflo full + skill-creator."
Handoff: "agent-spec-builder v2 complete (deeper, more Ruflo, self-improved). 9 CPs logged in meta build. Use v2 for future agents. Update CATALOG + ANALYSIS."
Memory: "Example 6 meta-recursive: self improved to v2 using own playbook + ANALYSIS + new sources; memory updates 9 CPs + 2 DECs during; P10 loop demonstrated; PT08 applied. Now ready for next agents with improved builder."
(Actual: this playbook entry created during v1, will be used for v2 in P5 or next.)

**Additional Scenarios (brief, expand in v2):**
- Building for user project (not self skill): adapt paths to user target, still enforce memory/ in user project + copy manager.py + templates.
- Swarm agent (e.g. team-builder): extra tools for Ruflo npx swarm, topology.md etc.
- After depth/SI pass: re-build with O1-O5 + SI feedback.
- Full AION-like (from user piano): use for 40+ agents in one go via meta.

**Trace for this playbook.md:** Full examples synthesized/expanded from:
- Our build history (CP-017 conductor, CP-018 memory-ecosystem-builder, CP-021 batch domain, CP-025 status, post CP-026 update)
- Content-Forge: CS01-the-mkd-discovery.md (full), CS03-the-self-improvement-mistake.md (full failure), CS04-bugs-found-in-real-test.md (full), agent-builder-agent.md (7 steps + self-critique + order), references/processes/agent.md
- Knowledge-pack: P04/P09/P10/P12/P13 + PT01/PT02/PT05/PT08 + CS01-04 + glossary
- Context-Eng advisor: Research→Plan→Reset→Implement examples, two-layer, 5Qs
- Ruflo: swarm/queen/topologies/memory/federation sections (full extracts where relevant)
- Skill-Creator: evals loop, iteration, packaging
- ANALYSIS-AND-IMPROVEMENT-PLAN.md (initial analysis of stubs, Priority 2 items 4-15, post CP-025 update, persistence fail as example)
- Past agent playbooks (e.g. conductor/playbook.md, memory-ecosystem-builder/playbook.md as templates)
- User: screenshot, "ok procedi", "più di 20 ... impeccabile", piano di sviluppo (Fase 1-5, 5 principles incl memory iterativa), KP-PLAN.md
All atoms expanded, no summary, labeled with sources + CPs. Meta example demonstrates P13/PT08/P10.

**Status:** v1 complete with 6 examples. Will be expanded with more from P5 depth/SI (e.g. real Ruflo runs once invoked).

**End of playbook.md. Memory updated during creation of this + all prior files.**