# Memory for Workflow Deep Analyzer Agent (Empire Studio)

**Protocol:** P10 (Two-Layer Memory Ecosystem). Short-term (conversational/session) + Long-term persistent (checkpoints, decisions, knowledge-state, agent-state, projects-state).

**Mandatory Updates:** AFTER EVERY action, decision, bug, handoff, update. No exceptions. Use memory_manager.py for all logs.

**Structure (in /home/user/empire-studio/memory/ ):**
- checkpoints/ : CP-XXX-description-timestamp.md (e.g. CP-010-deep-analysis-started-for-user-report-2026-06-07T20xxxx.md )
- decisions/ : DEC-XXX-description.md (with trace, rationale, linked principles)
- sessions/ : current run state
- plans/ : analysis plans
- architectures/ : extracted from study
- strategy-applications/ : how manifests were applied
- strategy-versions/ : 
- bugs/errors/ : linked to failure-modes
- updates/ : proposals generated
- workflow-state/ , knowledge-state/ , agent-state/ , verification-logs/ , projects-state/ , repo-analysis/
- MEMORY-INDEX.md (auto-updated summary)

**P10 Rules for this Agent:**
1. Before starting analysis: read relevant prior memory (grep memory/ for similar dept=projects or input type).
2. During: after discovery → log CP "discovery-complete"
   after dimension analysis → log CP + DEC for key "perché" findings
   after atom extraction → log full atoms count + sample traces
3. After handoff: log CP "handoff-to-knowledge-extractor-complete" + update projects-state/repo-analysis/
4. Always include in headers: Timestamp, Phase, Linked Principles (from master-build), Traceability (to source + this agent's run-id)
5. Two-layer: conversational notes in session/ for immediate context; persistent CPs/DECs for Claude Code wiki feed.

**Example Checkpoint Format (exact):**
```
# CP-010-deep-analysis-started-for-report-slug-2026-06-07T201500.md

**Timestamp:** 2026-06-07T20:15:00+02:00 (Europe/Rome)
**Agent:** workflow-deep-analyzer-agent
**Dept:** projects-repos-workloads
**Phase:** Stage 1 Discovery
**Run-ID:** empire-2026-06-07-xxx
**Linked Strategy Manifest:** projects-deep-analysis-v1.0 (trace-mandatory, read-only-enforce, update-proposal-mandatory)
**Input:** /home/user/uploads/user-workflow-report.md
**Actions Taken:** 
- find + discovery.txt (47 files)
- initial cat on README + CATALOG
**Decisions:** Prioritized docs/ and agents/ subdirs because user req "tutta l'immensità della struttura d'archettatura"
**Traceability:** All reads from $INPUT only
**Next:** Proceed to dimension analysis + memory log after each subphase
**State:** In progress
```

**Example Decision:**
```
# DEC-042-chose-exhaustive-grep-for-perche-2026-06-07T201522.md

**Rationale:** User explicit "perché è stato fatto così" + "studiarlo nei minimi dettagli". Simple cat insufficient for hidden decisions in comments/docs.
**Trace:** file:report.md lines:12-30 (grep matched "perché|decision|rationale")
**Principles:** P10 memory, master-build decision logging, content-forge traceability
**Impact:** Added 8 new atoms with "perché" dimension covered.
**Linked CP:** CP-010-...
```

**Agent State Tracking:**
- Current input path
- Files discovered count
- Atoms extracted count
- Traces completeness %
- Strategy rules applied
- Read-only confirmed (yes/no)
- Handoff status

**Projects-State / Repo-Analysis Subdir:**
- Specific for 4th dept: per input slug, store analysis snapshots, atom lists, comparison results (for workload-comparator later).

**Integration:**
- memory_manager.py handles creation of CPs/DECs with correct naming (safe filenames, no bad chars).
- After every tool call or phase: call manager.
- Conductor and Memory Management Team audit this.
- For 4th dept: special category "repo-analysis/" + "projects-state/"

**Verification:** memory-auditor-agent checks for missing updates post-run. bug-error-tracker if protocol violated.

**Update Log (this file):** 
- 2026-06-07: Initialized per full 7-file requirement for projects dept agents. Added examples with exact user phrasing ("studiarlo nei minimi dettagli", "perché è stato fatto così", "non lo devi modificare", "tutta l'immensità").
- Future: After first real user report deep study, add actual CP/DEC examples from run.

**Rule:** This memory.md is updated by the agent itself during runs + by Memory Management Department.
