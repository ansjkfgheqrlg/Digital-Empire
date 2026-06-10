# Tools for Workflow Deep Analyzer Agent (Empire Studio)

**Core Principle:** All tools are CLI-only, read-only for source paths. No APIs, no paid services, no modifications to user originals.

## 1. Filesystem Discovery & Read (Primary)
- `ls -laR <path>` or `find <path> -type f | head -100` (discover structure)
- `cat <file> | head -N` or `tail -N` (read sections)
- `grep -n "pattern" <file>` (find sections with line numbers for trace)
- `wc -l <file>` (size for prioritization)
- `file <path>` (type detection)

## 2. Structured Parsing (Python Scripts - to be in skills/)
- `python /home/user/empire-studio/skills/workflow-report-parser-skill/scripts/parse_report.py --input <path> --output atoms.json` (extract headers, sections, code blocks)
- `python /home/user/empire-studio/skills/repo-analyzer-skill/scripts/analyze_repo.py --root <path> --focus architecture|decisions` (build file tree, extract functions, comments, imports)
- Custom: use ast (Python), markdown parsers, simple regex for "perché" keywords in comments/docs.

## 3. Strategy & Manifest Integration
- `python /home/user/empire-studio/scripts/generate_strategy_manifest.py --input-type=projects-report --focus=deep-study --dept=projects --output /tmp/manifest.json --run-id=CP-XXX`
  - Returns: selected_strategies (e.g. "projects-deep-analysis-v1.0"), rules (trace mandatory, read-only), rationale, trace

## 4. Memory Management (Active)
- `python /home/user/empire-studio/scripts/memory_manager.py log-checkpoint --id=CP-XXX --description="deep-analysis-started-for-<slug>" --timestamp=$(date -Iseconds) --dept=projects`
- `python /home/user/empire-studio/scripts/memory_manager.py log-decision --text="Chose exhaustive read of file X because Y" --trace="file:report.md lines:1-10"`
- Read memory/ for cross-ref: `cat memory/MEMORY-INDEX.md | grep -A5 "projects"`

## 5. Traceability & Output Prep
- Always prefix analysis with exact traces.
- Build atoms list in JSON or MD with fields: id, trace, summary, expansion, implications, source_quote
- Handoff package: tar or dir of analysis.md + atoms.json + traces.log

## 6. Verification Hooks
- Self-check: count traces vs atoms (must 1:1)
- Call visual-verifier-agent if screenshots/frames from related (rare for reports)
- Failure detection via failure-modes.md rules

## 7. Content-Forge Handoff
- After analysis: `python /home/user/empire-studio/skills/content-forge-wrapper-skill/scripts/forge_wrapper.py --input analysis-package/ --target=wiki --manifest=/tmp/manifest.json --dept=projects`

**Enforcement:** All scripts must respect --read-only flag if present. Source paths never in write commands.

**Python Scripts Location:** To be expanded in skills/ (e.g. skills/workflow-report-parser-skill/ , skills/repo-deep-parser-skill/)

**Example Exact Command Sequence (from playbook):**
1. find $INPUT_PATH -type f > discovery.txt
2. for f in $(cat discovery.txt | head -20); do echo "=== TRACE: file:$f ==="; cat "$f" | head -50; done > deep_read.log
3. python parser.py --input $INPUT_PATH --traces deep_read.log
4. memory_manager.py log-...

**No modification rule:** Any command that could write (e.g. no > to source, no sed -i on source, no git commit on source). Use /tmp/ for all outputs.
