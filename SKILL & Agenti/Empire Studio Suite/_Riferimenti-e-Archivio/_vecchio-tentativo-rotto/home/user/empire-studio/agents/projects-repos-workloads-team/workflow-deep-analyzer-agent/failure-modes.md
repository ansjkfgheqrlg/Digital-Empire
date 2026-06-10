# Failure Modes for Workflow Deep Analyzer Agent (Empire Studio)

**Format:** | Failure | Symptom | Prevention | Detection | Recovery |

**High Priority Failures (P10 + User "studiarlo nei minimi dettagli" + read-only):**

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Source file modified | Timestamp or size of input file changes after analysis | Never use write commands on $INPUT_PATH; all outputs to /tmp/ or memory/; scripts have --read-only flag enforced | Post-analysis: `stat $INPUT_PATH` vs pre; ls -l ; git status if repo (but read-only) | Immediate halt, log CP "read-only-violation-detected", rollback any temp writes, re-run analysis on fresh copy if needed, notify Conductor + Memory Management. Add to failure-modes-log/ |
| Insufficient traceability (atom without trace) | Atoms list has entries missing "file:..." or lines | Mandatory template in playbook Stage 3: every atom MUST have trace field; parser script auto-adds from grep -n output | Self-eval in Stage 4: count atoms vs traced; grep "ATOM-" /tmp/atoms* | Re-scan with more targeted grep/find for missing sections; regenerate atoms package; log DEC "added-missing-traces-for-ATOM-042"; update memory |
| Shallow analysis (not "minuti dettagli") | Only top-level files read; missing subdirs, code, "perché" sections | Use recursive find + prioritized key files (README, decisions/, agents/, memory/); python parser for structure; force min 20 atoms + 5 dimensions coverage | During Stage 2: checklist "dimensions covered?" ; atom count <15 | Deepen: additional find -name "*.py" ; cat more files with head -200; re-grep for "perché|decision|rationale"; log failure and continue |
| Strategy Manifest not applied | Analysis ignores projects-specific rules (e.g. no update-proposal) | Stage 0 mandatory: always run/generate manifest before analysis; playbook "Regola Obbligatoria" | Check /tmp/manifest.json exists and contains "projects" ; grep manifest for "update-proposal mandatory" | Halt, call generate_strategy_manifest.py --dept=projects , re-apply rules to current analysis, log DEC "manifest-applied-retroactively" |
| Memory not updated after action | No new CP/DEC after major phase | After EVERY step (discovery, analysis phase, atom extract): call memory_manager.py | Pre/post: count files in memory/checkpoints/ ; grep MEMORY-INDEX for run-id | Immediate: run memory_manager.py log-checkpoint with current state; if bug, call bug-error-tracker-agent |
| No cross-dept update proposals when relevant | Report mentions YT/video but no proposal generated | In Stage 3: explicit scan for keywords from other depts (youtube, video-watcher, tiktok, web); always produce at least "update_proposals.md" even if empty | Review output package for update_proposals.md content | Add section "Cross-Department Opportunities" with 1-3 proposals (even if "no direct link"); log as improvement |
| Python parser or CLI fails on complex repo | Parser crashes on large file or special chars | Use robust python (try/except, limit head), CLI fallbacks (pure grep/cat) | Exception in log; empty atoms | Fallback to pure CLI: more grep -r "pattern" ; manual section extraction; log failure-mode and partial results + "parser-fallback-used" |
| Input path is Empire Studio source itself | Risk of "studying" self and accidental overlap | Pre-check: if path contains "empire-studio" or "agents/" warn + require explicit --force or reject for safety | `echo $INPUT | grep -q empire-studio` | Reject with clear message to user "Cannot deep-study Empire Studio source itself to avoid self-modification risk. Provide external report/repo."; log as prevented failure |

**Low Priority / Edge:**
- Empty input or no readable files: Symptom: discovery.txt empty. Prevention: validate at least 1 file. Recovery: ask Conductor for clarification (via ask_user if interactive).
- Binary files (pdf, images): Symptom: cat shows garbage. Prevention: file cmd filter, use strings or tesseract if avail for OCR. Recovery: skip or note "binary - visual analysis needed via other skill".
- Very large repo (>1000 files): Symptom: timeout or too much output. Prevention: prioritize (top 50 files by name relevance + size), sample. Recovery: produce "summary of discovery" + "deep on top 20" + flag for iterative deeper study.

**Self-Improvement:** 
- After each run, Improver or memory-auditor reviews failure-modes encountered and proposes updates to this file + playbook.
- All failures logged to memory/failure-modes-log/ with trace.
- Update this table after real evals/runs.

**Verification Link:** See evals.md for test cases that trigger these modes intentionally. Visual-verifier if applicable (e.g. if report has diagrams).

**Trace to User:** Prevents "non ti sei dimenticato tutto" by enforcing depth, traceability, memory, read-only at failure level.
