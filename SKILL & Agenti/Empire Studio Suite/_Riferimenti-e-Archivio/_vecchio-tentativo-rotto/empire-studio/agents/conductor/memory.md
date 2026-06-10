# Conductor Memory.md (P10 Enforcement for L1)

**Mandate (P10 + Master-Build screenshot + Ruflo/Content-Forge + Context-Eng + User "fin da subito"):** Memory ecosystem from the very first step of every run and every internal step. This agent (and all spawned) ALWAYS updates memory after action.

**Two-Layer Practice (exact from master-build + Context-Eng):**
- Short-term: This SES + current context ( "current state before this handoff: 3 videos watched, 2 frames pending visual").
- Long-term: memory/INDEX + CPs/DECs (persistent, shared_state for run progress, video_state e.g. {"video-abc": {"watched": true, "frames": 12, "atoms": 45, "wiki_inserted": false}} ) + architectures/ for topology.

**Research→Plan→Reset→Implement (in every stage):**
- Research: read SKILL.md, previous CPs/DECs/INDEX, refs, clones (content-forge, master-build, playwright), user input, state.json.
- Plan: this playbook or vN, or ASK.
- Reset: clear temp, implement from clean PLAN + memory.
- Implement: spawn, write outputs, handoff.
- Then: memory update (CP/DEC if decision, manager both top+run, append INDEX both, sync).

**Update Protocol (10 Steps — Enforced):**
1. Action (e.g. handoff to processing-team).
2. Research (read relevant + previous memory).
3. Plan (update state or small PLAN).
4. Reset (clean).
5. Implement (spawn or write).
6. Manager both (top /home/user/empire-studio + phase-runs/<run>) --checkpoint "Stage X done for video Y".
7. Append INDEX both with trace.
8. Record DEC if significant (ADR).
9. Update shared_state (e.g. video_state in INDEX or architectures/run-state.md).
10. Verify (ls checkpoints/ recent, cat INDEX tail, validator if needed). Sync files if needed.

**Examples of Updates (from our build + user vision):**
- CP-000: Memory bootstrapped (this run).
- CP-001: Ingestion complete for channel.
- CP-012: Video-abc123 watched (12 frames + visual passages "mostra export JSON" extracted per user "video va visto").
- DEC-001: Use playwright for all visual (CLI only, no vision API).
- After forge: CP "Wiki notes inserted with full trace P12 to video#ts+frame".
- Meta: "This conductor memory.md creation is P13 example: L1 managing its own memory protocol for future v2."

**Shared State Example (for teams):**
In INDEX or run/architectures/:
```json
{"run_progress": {"ingestion": "done", "watched_videos": 5, "forge_done": false}, "video_state": {"abc123": {"watched":true, "visual_atoms":12, "wiki":true}}, "update_proposals_generated": 2}
```

**Ruflo Integration (if avail):** memory_store for video_state, memory_search for "previous visual analysis of design videos".

**Content-Forge:** failure-modes-log + SI loops feed P01 for this ecosystem.

**Advisor (Context-Eng):** two-layer exact, Research→Plan→Reset in CPs/INDEX, 5Qs for boundaries (e.g. "what is out of scope for this ingest?").

**Skill-Creator:** memory/ in packaged, evals/iteration on P10.

**Master-Build:** P10 screenshot exact + our CPs/ANALYSIS as live examples.

**How Updates (this agent enforces in all handoffs/playbook):**
- Invoke bootstrap at start.
- After every spawn/result: CP + manager + append + state update + verify.
- At end of run: final CP/DEC, full INDEX, architectures/run-topology.md.
- P10 loops: CPs/DECs feed next PLAN or update-proposer.

**Status this (P10 100% enforced in spec, P12 full trace, P13 meta self-ref in examples, P07 hierarchy, P08 depth visual, P09 FM, P03 no-summary, gerarchia user, CLI, content-forge wiki, video watch):**
- Top + embedded memory live (CP-000+).
- Protocol strict in playbook/system-prompt/tools.
- Trace P12: to user "memory... fin da subito" implied in complete + master-build P10 + screenshot + "aggiornare... flussi" + our CP-000 creation + this file.

**Trace (P12):** To P10 + master-build memory section + user vision (complete ecosystem with memory implied in professional structure) + content-forge + Context-Eng + our bootstrap CP + this creation as meta.

**Status:** Full P10 protocol for L1. Enforced everywhere.
