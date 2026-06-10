# Evals for Workflow Deep Analyzer Agent (Empire Studio)

**Purpose:** 5+ concrete test cases to verify correct deep study behavior, traceability, read-only, memory updates, and content-forge readiness. Run manually or via verification team.

**Eval 1: Simple Workflow Report (Markdown)**
- Input: Sample report.md describing a 3-level agent system (e.g. copy from known master-build style but in /tmp/test-report.md)
- Expected:
  - Discovery: finds all sections via find/cat
  - Dimensions covered: full "come è stato fatto" (structure), "perché" (quotes from text), "come funziona" (flows), "quanto bene" (implicit strengths), patterns.
  - Atoms: >=10 with exact "file:/tmp/test-report.md section:XXX lines:NN-MM"
  - Memory: at least 2 new CPs + 1 DEC logged (check memory/checkpoints/)
  - No writes to /tmp/test-report.md (verify with ls -l timestamp unchanged)
  - Output package ready for forge (has trace log)
- Pass criteria: All 5 dimensions, 100% atoms traced, memory updated, read-only confirmed.
- Failure if: any atom without trace, or source file modified (size/timestamp change).

**Eval 2: Repo Deep Study (Directory)**
- Input: A small known repo dir e.g. /tmp/test-repo/ (copy of small empire-studio subdir or cli-printing-press example, read-only copy)
- Expected:
  - Recursive find all .md .py
  - Analysis of architecture from README + code structure (e.g. "L1 Conductor in agents/conductor/")
  - "Perché": from comments or decisions/ files if present
  - Effectiveness: note "full 7 files in conductor" as strength, "partial skills" as weakness
  - Atoms: 15+ with traces like "repo:/tmp/test-repo/agents/conductor/conductor.md lines:10-25"
  - Strategy manifest applied (projects specific rules)
- Pass: Traceable atoms, patterns mapped (e.g. "follows master-build P10"), no source mods.

**Eval 3: Cross-Department Update Proposal Generation**
- Input: Report that mentions "video watching" or "YouTube ingest"
- Expected: In update_proposals.md : specific proposal e.g. "Update video-watcher-skill to include more frame rules from this report's visual analysis section (trace: file:report.md lines:88-92)"
- Also updates Empire Studio internal if relevant (e.g. add to CATALOG.md but only in proposal, never modify original)
- Pass: At least 1 cross-dept proposal with trace.

**Eval 4: Large/Complex Workload (Stress)**
- Input: Full known dir like a copy of content-forge2.0 or master-build-architecture (read-only)
- Expected: Prioritizes key files (README, CATALOG, key agents), uses python parser for scale, produces 30+ atoms, logs multiple CPs during long run.
- Pass: Completes without timeout, all traces, memory has sequence of CPs for phases.

**Eval 5: Read-Only Enforcement + Error Recovery**
- Input: Path that is write-protected or attempt to test modify.
- Expected: Agent detects (e.g. via permission or self-check), logs failure-mode "read-only violation prevented", refuses any write command, continues with read-only analysis, still produces valid atoms + memory log.
- Pass: No actual modification occurred, failure logged correctly, analysis succeeded anyway.

**General Success Metrics:**
- Traceability: 100% atoms have source trace (file+section+lines)
- Depth: Covers all 5 user dimensions explicitly
- Memory: >=1 CP and >=1 DEC per major stage
- Strategy: Manifest rules followed (e.g. "update-proposal mandatory")
- CLI only: All commands logged and verifiable
- No summary: Full expansion in analysis

**Run Instructions:** 
Use bash to simulate: mkdir /tmp/test-xxx; echo "test report content with decisions" > /tmp/test-xxx/report.md
Then invoke agent logic manually or via Conductor simulation.
Record results in memory/evals/ or verification logs.
Update this evals.md after each real run with actual outcomes.

**Link to Failure-Modes:** See failure-modes.md for how to handle common fails (e.g. "insufficient traces" → re-grep with more patterns).
