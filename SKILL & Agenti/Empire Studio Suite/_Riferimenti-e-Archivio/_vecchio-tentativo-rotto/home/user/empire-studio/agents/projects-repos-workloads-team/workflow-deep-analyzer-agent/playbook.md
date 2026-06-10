# Playbook for Workflow Deep Analyzer Agent (Empire Studio - Projects-Repos-Workloads Dept)

**Regola Obbligatoria (from Strategy integration):** Prima di iniziare qualsiasi analisi, leggi il Strategy Manifest generato da Strategy Coordinator. Applica le selected_strategies, rules, templates per dept=projects. "Regola Obbligatoria: leggi Strategy Manifest".

**Stage 0 (Conductor triggered):**
1. Receive from Conductor: user input path (e.g. /path/to/user-report.md or /path/to/repo/), run-id, Strategy Manifest (JSON or .md with selected_strategies for projects-repos-workloads, e.g. "deep-cli-analysis-v1.0", "trace-mandatory-v1.1", "read-only-enforce", "update-proposal-cross-dept").
2. Validate: path exists, read permissions, NOT inside empire-studio source (to avoid accidental modify).
3. Memory: log checkpoint CP-XXX-deep-analysis-start-<slug>-$(date +%Y-%m-%dT%H%M%S).md
4. Call generate_strategy_manifest.py if not provided (for consistency).

**Stage 1: Discovery (Exhaustive CLI Read - "guarda il report come un video")**
- Command: `find "$INPUT" -type f \( -name "*.md" -o -name "*.txt" -o -name "*.py" -o -name "*.js" -o -name "README*" -o -name "*.json" \) | sort > /tmp/discovery.txt`
- For each key file (prioritize README, docs/, src/ architecture files, memory/, decisions/): 
  `echo "=== DEEP READ TRACE: file:$f lines:1-100 ===" >> /tmp/deep_reads.log`
  `cat "$f" | head -100 >> /tmp/deep_reads.log`
  `grep -n -E "(perché|why|decision|rationale|architecture|flow|how it works|strength|weakness|pattern)" "$f" | head -20 >> /tmp/traces.log`
- "Passaggi mostrati": For each section, describe in detail what is shown (e.g. "In lines 34-67: detailed 4-level hierarchy diagram described in text + list of 8 L3 agents. This shows the 'immensità della struttura' ").
- Use python parser for structure: extract headers, code blocks, lists.

**Stage 2: Dimension Analysis (the 5 user dimensions)**
- **Come è stato fatto:** Map file tree, main components, build process from docs/code comments.
- **Perché è stato fatto così:** Extract quotes with trace for every decision (e.g. "DEC- in memory: 'added 4th dept because user said quarto reparto' trace: memory/decisions/DEC-xxx.md").
- **Come funziona:** Reconstruct flows (numbered steps from playbooks/specs), component interactions.
- **Quanto funziona bene:** Identify explicit/implicit strengths (e.g. "full 7 files for priority agents"), weaknesses (e.g. "some agents only have .md spec"), evidence from evals/failure-modes.
- **Patterns/Anti-patterns:** Map to master-build-architecture/ (e.g. "Uses P10 memory protocol - strength"; "Long checkpoint names in old builds - anti-pattern fixed in empire-studio").

**Stage 3: Atom Extraction (Traceable)**
- For every insight: create atom entry:
  ```
  ATOM-042:
  trace: file:/path/to/report.md section:"L3 Agents" lines:45-67
  source_quote: "workflow-deep-analyzer-agent (deep study...)"
  summary: ...
  expansion: + (implications for Empire Studio 4th dept)
  ```
- Minimum 15-30 atoms per medium report. All with trace.
- Categorize: Architecture, Decisions, Effectiveness, Patterns, Cross-Department Opportunities.

**Stage 4: Memory & Verification**
- Log all CPs, DECs during process (use memory_manager.py after each major phase).
- Self-eval: "Traces complete? Atoms >=15? Read-only confirmed?"
- If gaps: log failure-mode and retry with deeper find/grep.

**Stage 5: Handoff**
- Package: /tmp/analysis-<slug>/ {deep_analysis.md, atoms.json, traces.log, update_proposals.md, strategy_manifest.json}
- Invoke: project-knowledge-extractor-agent with package.
- Then Conductor or Forge Team for content-forge2.0 (pass Manifest).
- Final memory update: CP-XXX-deep-analysis-complete-...

**Example Exact Flow (for user report):**
1. /empire /path/to/user-workflow-report.md --dept=projects
2. Conductor → Strategy Coordinator → manifest (projects strategies)
3. Conductor → workflow-deep-analyzer-agent
4. Run: find ... ; cat keyfiles with traces ; python parser
5. Log CP-010-...
6. Output package → project-knowledge-extractor → content-forge-wrapper --target=wiki
7. Memory: all updated. User gets wiki notes + update proposals + full trace.

**Rules:**
- Always use --read-only mindset.
- Trace every claim.
- Update memory after every action (no exception).
- If report mentions "Empire Studio" or similar, cross-ref to current CATALOG/agents/.
- For repos: analyze "perché" from commit messages if available (git log --oneline but read-only: git log is ok if no modify).
- Output in Italian if input Italian, with exact user phrasing preserved when quoting reqs.

**Tools Integration:** See tools.md . Always call generate_strategy_manifest.py first for projects.

This playbook is mandatory. Deviations logged as failure-modes.
