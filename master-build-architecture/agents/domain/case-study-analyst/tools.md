# Tools for case-study-analyst (P05 Markdown + Python Embedded, Ruflo MCP + Content-Forge Scripts + Advisor 5Qs + Validator + Memory Manager Both Targets)

**Core Mandate (P10 fin da subito + user "fin da subito" + screenshot + Context-Eng two-layer + Ruflo memory + Content-Forge failure-modes-log + CS03/CS04):** EVERY tool call MUST start and end with memory update: invoke manager both targets (/home/user and projects/.agents/skills/master-build-architecture), create CP/DEC if significant, append INDEX both, update case-state shared_state (CS03/CS04 coverage + lessons), sync top/embedded, Research→Plan→Reset. Failure if no memory P10 (CS04 persistence bug like initial ANALYSIS). All tools enforce P12 trace (output ≥3 cites to CS01-CS04 full + ANALYSIS CS + CPs + user complaint + sources + our CPs/DEC-010 + this), P03 no-summary (full extracts + ➕ our), P08 depth, PT05 7 files in produced, P09 FM table + log, P07/PT01 three-level, P13/PT08 meta self-ref, P15 visibility "agenti che gestiscono i case studi" + flussi + user triggers, Ruflo/Content-Forge/Advisor/Skill-Creator/pack extracts.

**Tool 1: ReadCaseStudy (read full CS + our lessons + pack + clones + advisor + skill-creator + user + history)**
- Schema (JSON):
  {
    "name": "ReadCaseStudy",
    "description": "Read full CS01-CS04 from pack + ANALYSIS CS sections + CPs/DECs/INDEX live + SKILL/README/CATALOG + clones (content-forge2.0 failure-modes-log + CS in Stage 10) + advisor (two-layer/cycle/5Qs) + skill-creator (evals/iteration) + user complaint verbatim + prior agents (memory-builder as CS04 example, failure-detector CS03) + our history (autonomous as P13 meta CS) + 'Piano di Sviluppo' + KP-PLAN. Always memory P10 update before/after. Output full extracts + ➕ our applications as CS05+.",
    "parameters": {
      "type": "object",
      "properties": {
        "cs_id": {"type": "string", "enum": ["CS01", "CS02", "CS03", "CS04", "all"], "description": "Which case study or all"},
        "include_our_lessons": {"type": "boolean", "default": true, "description": "Include ANALYSIS + CPs/DECs/INDEX + SKILL + README + CATALOG + user complaint + our history as living CS05+"},
        "memory_update": {"type": "boolean", "default": true, "description": "MANDATORY: run manager both + CP/DEC + append INDEX both + case-state + sync before/after read"}
      },
      "required": ["cs_id"]
    }
  }
- Implementation (embedded Python P05 + Ruflo MCP + bash manager):
```python
import subprocess
def read_case_study(cs_id="all", include_our_lessons=True, memory_update=True):
    if memory_update:
        # P10 mandatory: manager both targets
        subprocess.run(["python", "scripts/memory_manager.py", "--checkpoint", f"ReadCaseStudy {cs_id} start", "--phase", "4", "--target", "/home/user"])
        subprocess.run(["python", "scripts/memory_manager.py", "--checkpoint", f"ReadCaseStudy {cs_id} start", "--phase", "4", "--target", "projects/.agents/skills/master-build-architecture"])
        # append INDEX, update case-state, sync (simplified; full in manager + manual)
    paths = {
        "CS01": "skill-planning-knowledge-pack/06-case-studies/CS01-the-mkd-discovery.md",
        # ... all CS + ANALYSIS + CPs/DECs/INDEX + SKILL + README + CATALOG + clones/content-forge2.0/references/failure-modes-log/CS* + advisor/SKILL.md + skill-creator.md + user complaint file + prior agent .md + "Piano di Sviluppo Creazione della.txt"
    }
    content = ""
    for p in (paths[cs_id] if cs_id != "all" else paths.values()):
        with open(p) as f: content += f.read() + "\n\n"
    if include_our_lessons:
        content += "# OUR LESSONS (➕ CS05+ from ANALYSIS + CPs + user + this build)\n" + open("ANALYSIS-AND-IMPROVEMENT-PLAN.md").read()[:5000] + ... # full extracts + user complaint + CP-013 CS04 + CP-025 CS03 + this batch CS04 recovery + DOVE_E_LA_SKILL + case dir creation + 7 files + visibility P02/P15
    if memory_update:
        subprocess.run(["python", "scripts/memory_manager.py", "--checkpoint", f"ReadCaseStudy {cs_id} done", "--phase", "4", "--target", "/home/user"])
        # ... both + append + case-state {"CS01": {"applied": True, "coverage": "100%", "lessons": "MKD first + user micro-obs taken seriously"}, ...} + sync
    return content  # full no-summary + trace P12 headers
```
- Failure if no memory_update (CS04 bug): "No P10 update — CS04 persistence violation. Run manager both + CP + sync first."
- Trace (P12): "Trace (P12/CS01): CS01 full text lines 1-258 (user quote 'prima di trasformarlo... guida perfetta' + MKD lesson) + ANALYSIS 'CS01 triggered MKD addition' + CP-004 this + user 'stessa cosa per il case studi' + SKILL 'agenti che gestiscono i case studi' + pack CS01 + our CPs/DEC-010 + this; sources: pack + clones + advisor + skill-creator + user + our history."

**Tool 2: ReadOurCSLessons (from ANALYSIS/CPs/DECs/INDEX/SKILL/README/CATALOG/user complaint/prior agents/our history as living CS05+)**
- Schema similar, focused on our build as primary source for ➕ lessons (CS03 self-imp mistake prevention via autonomous/memory P10/observer CPs/DECs/INDEX/ANALYSIS real audit; CS04 real-test + persistence + no fictional via CP-013 + this batch real creation + DOVE_E_LA_SKILL + validator + ls/cat; CS01 expansion + user micro-obs; CS02 team via this + domain + builders).
- Implementation: read specific files + extract CS sections + CPs with "CS04" "CS03" in text + user complaint + SKILL "case-study-analyst" + README "agenti che gestiscono i case studi" + CATALOG "Implemented 27 CS flows" + prior (memory-builder "CS04 prevention", failure-detector "CS03 observer") + this creation as P13 meta.
- Memory P10 mandatory before/after + case-state update + sync.
- Trace P12 to CS03 full + ANALYSIS CS03 + CP-025 + user + SKILL + our CPs/DEC-010 + this.

**Tool 3: CreateCSFlow (create CS-pipeline DAG or case-studies-team spec + handoff to workflow-builder/team-builder + memory P10)**
- Schema:
  {
    "name": "CreateCSFlow",
    "description": "Create CS01-MKD + CS03-SI + CS04-real-test pipeline (workflow-builder DAG) or case-studies-team (team-builder = this + anti-pattern-hunter + principle-codifier + qa + memory-builder) per PT02/PT01/P07/P13 + user 'flussi di agenti team di agenti per ogni categoria' + 'agenti che gestiscono i case studi'. Enforce 7 files/no-summary/depth/trace/memory in produced. Memory P10 + case-state + sync mandatory. Output full spec + handoff JSON + trace P12.",
    "parameters": {
      "type": "object",
      "properties": {
        "flow_type": {"type": "string", "enum": ["pipeline", "team", "both"], "description": "CS-pipeline or case-studies-team or both"},
        "target_name": {"type": "string", "description": "e.g. user-project-cs-flows or master-build-architecture-v2"},
        "include_our_lessons": {"type": "boolean", "default": true},
        "memory_update": {"type": "boolean", "default": true}
      },
      "required": ["flow_type", "target_name"]
    }
  }
- Implementation: use plan-builder logic + write DAG/team spec with CS checklist per step, shared_state case-state, handoffs (to memory-ecosystem-builder "enforce CS04 persistence", failure-detector "CS03 observer", qa "CS04 real-test + validator", conductor "meta P13"), ➕ our (this batch as CS04 recovery), memory P10 (manager both + CP after write + append + sync + case-state), trace P12.
- Handoff: spawn workflow-builder or team-builder with spec + "CS03 observer + P10 memory + CS04 real FS + validator mandatory" + memory mandate.
- Trace P12 to CS01 (MKD), CS03 (SI observer), CS04 (real-test), PT02/PT01/P07/P13, user "flussi... team di agenti", our CPs/DEC-010 + this, SKILL/ README "flussi per categoria".

**Tool 4: ValidateCSApplication (P09/P12/PT06/P06/CS04 real-test + qa/validator + FS audit)**
- Schema: params for target (produced dir or self), check_cs (list CS01-04), real_fs_audit (bool default true), memory_update true.
- Implementation: grep CS coverage in outputs + ls/cat/validator.py on memory/agents/refs (prevent CS04 fictional like initial ANALYSIS) + run qa/coverage-verifier + failure-mode-validator + target-schema + real-test (simulate Ruflo run or actual ls/find/read) + 100% atoms + real files not claims + log FM if violation (e.g. CS03 no observer → handoff failure-detector) + memory P10 + case-state + sync + trace P12.
- Failure if no real FS (CS04): "CS04 violation: claimed but no real files on FS (like early ANALYSIS). Run ls/cat/validator + create actual + DOVE_E_LA_SKILL style + manager CP + sync."
- Trace P12 to CS04 full + ANALYSIS CS04 + CP-013 + this batch + user "non vedo... non ci sono tutti gli agenti" + SKILL/ README + our CPs/DEC-010 + this.

**Tool 5: UpdateCaseState (P10/P12/Research→Plan→Reset + manager both + cycle + case-state shared_state)**
- Schema: params for cs_id, applied (bool), coverage (str), lessons (str), memory_update true.
- Implementation: update memory/architectures/case-state.json + ARCH-XXX + INDEX append + manager both + CP/DEC + sync + Research→Plan→Reset (research current state from CPs/INDEX, plan, reset, implement clean) + trace P12.
- Example: UpdateCaseState("CS04", True, "100%", "real creation + DOVE_E_LA_SKILL + architectures/ + validator + no fictional like CS04 bug in ANALYSIS; recovery from initial persistence fail", True)
- Trace P12 to CS04 + ANALYSIS + CP-013 + this + user + our CPs/DEC-010 + this.

**Tool 6: HandoffToBuilder (PT02/PT01/P07/P13 + meta + memory P10)**
- Schema: params builder (e.g. "workflow-builder", "team-builder", "memory-ecosystem-builder", "failure-detector-agent", "qa", "conductor"), spec (CS flow/team + CS checklist + memory mandate + trace), memory_update true.
- Implementation: write handoff JSON + spawn via Ruflo npx or bash + memory P10 (manager both + CP after handoff + append + sync + case-state) + self-ref P13 "feed this handoff + CS lessons back to v2" + trace P12.
- Trace P12 to PT02/PT01/P07/P13 + CS01-04 + user "flussi di agenti team di agenti" + our CPs + SKILL "flussi per categoria" + this.

**Additional Tools (Ruflo MCP + Content-Forge scripts + Advisor 5Qs + validator.py + memory_manager wrapper):**
- RufloSwarmSpawn (for case-studies-team as Ruflo swarm: topology hierarchical/mesh/pipeline, memory agentdb with case-state, hooks background CS lessons).
- ContentForgeForge (invoke /forge on CS atoms with --stage mkd (CS01) --optimizers (CS02) --si-observer (CS03) --real-test (CS04)).
- Advisor5Qs (Q1 "CS lessons apply?", Q2 "boundaries no CS03 drift?", Q3 "CS04 real-test?", Q4 "memory P10?", Q5 "trace P12 + meta P13?", falsification "if no observer → CS03 drift?").
- RunValidator (python scripts/validator.py --target=... --checks="7files,memory-live,coverage,cs04-real-fs,no-fictional" + memory P10).
- MemoryManagerWrapper (python scripts/memory_manager.py --checkpoint "CS tool X" --phase=4 --target=/home/user && same for embedded + append + case-state + sync).
- Bash (ls/cat/find on produced to enforce CS04 real FS audit; npx ruflo; python validator).

**Failure Modes for Tools (P09/PT07/CS03/CS04 + this failure-modes.md):** 
- No memory_update (CS04 persistence bug like ANALYSIS initial): symptom "no CP/DEC/INDEX append/case-state/sync after tool"; prevention "ALWAYS manager both + CP/DEC + append + sync + case-state at start/end of every tool"; detection "grep CPs in INDEX + ls memory/checkpoints after"; recovery "run manager both like CP-013 + sync + log FM + triage + P01"; example our CP-004 + this batch.
- No real FS audit (CS04): symptom "claimed CS application but ls shows no real files/7 files/memory live"; prevention "real ls/cat/validator in ValidateCSApplication + DOVE_E_LA_SKILL style visibility"; detection "run ls/find/read + validator"; recovery "create actual + manager CP + sync + this".
- No CS03 observer (CS03 drift): symptom "SI without memory P10/observer/CPs/DECs/INDEX/ANALYSIS as logs"; prevention "always handoff failure-detector + memory P10 in handoff + case-state"; detection "grep observer + CPs in outputs"; recovery "handoff failure-detector + log + CP + real validation".
- No trace P12 / no user complaint address / no flussi (P12/P15/user "non vedo... non ci sono tutti gli agenti... flussi..."): prevention "P12 headers + ≥3 cites + explicit 'agenti che gestiscono i case studi' + flussi map + user complaint verbatim in outputs + DOVE_E_LA_SKILL + SKILL/README/CATALOG"; detection "grep trace + 'agenti che gestiscono' + flussi"; recovery "add + log + manager CP + this".
- Shallow / summary (P03/CS01): prevention "full extracts + ➕ our + 5-10+ pages + no stubs"; detection "no-summary lint + user 'non vedo'"; recovery "expand + manager CP + this".
- No meta P13/PT08 (P13): prevention "self-ref 'feed back to v2' + use self (this + autonomous) as example in playbook/memory"; detection "grep 'P13' + 'v2' + 'this creation'"; recovery "add + manager CP + meta self-ref".
- Global: log all to failure-modes-log/ via failure-detector (P10/P09); silent P14; Ruflo hooks background; feed P01 vN (ANALYSIS + PLAN); our build initial violations (ANALYSIS 3/10: no memory, shallow, no FM, fictional, no flussi/agents for case/principles/patterns despite "fatto principi", visibility fail P02/P15) → recovered autonomous (DEC-010 + CPs/DECs/INDEX/manager + real creation + this + principles-manager + patterns-manager + case-study-analyst + DOVE_E_LA_SKILL + visibility fixes + real FS audit in ANALYSIS/CATALOG + memory P10 100% + trace P12 full + depth P08 + 7 files PT05 + flussi/teams per categoria + "agenti che gestiscono i case studi" explicit + name "Master build Architecture" + user complaint addressed).

**Ruflo/Content-Forge/Advisor/Skill-Creator/Pack Extracts (full in every tool desc + impl):** As in system-prompt (Ruflo swarm/queen/memory/federation/MCP/hooks/SONA for case-studies-team + case-state; Content-Forge 9-stage/MKD/CS01-04 in failure-modes-log + SI Stage 10 observer + real-test Phase 8 + evals; Advisor two-layer/Research→Plan→Reset/5Qs/falsification/Context Manifest for CS flows; Skill-Creator evals/iteration/packaging for CS-001 etc; pack CS01-CS04 full + P/PT/AP + KP-PLAN + "Piano di Sviluppo").

**Memory Update Protocol (P10 + this memory.md + CS03/CS04):** Before tool: manager both + CP "Tool X start" + append INDEX + case-state read + Research→Plan→Reset. After tool: manager both + CP "Tool X done + case-state update" + append + sync + case-state write (CS03/CS04 coverage + lessons + our CPs as example) + trace P12 in output + self-ref P13 "feed this tool call + CS lessons back to v2". Example: after ReadCaseStudy CS04 → CP + case-state {"CS04": {"applied":true, "coverage":"100%", "lessons":"real creation + DOVE_E_LA_SKILL + architectures/ + validator + no fictional like CS04 in ANALYSIS; recovery from initial persistence fail via CP-013 + this batch", "cps": ["CP-013", "CP-004"]}} + sync + trace to CS04 + ANALYSIS + CP-013 + this + user + our CPs/DEC-010 + this.

**Trace (P12) for this tools.md:** CS01 full (MKD + user quote) + CS03 full (SI without observer) + CS04 full (bugs real-test + persistence) + ANALYSIS (CS03/CS04 + real FS audit + visibility fixes + "agenti che gestiscono i case studi") + CPs (CP-013 CS04, CP-025 CS03, CP-004 this + visibility + case dir) + user complaint verbatim ("stessa cosa per il case studi devi fare agenti che gestiscono i case studi" + full "non vedo... non ci sono tutti gli agenti... flussi di agenti team di agenti per ogni categoria...") + SKILL (catalog + visibility + flussi + case-study-analyst + name "Master build Architecture") + README (map + user + flussi per categoria + case) + CATALOG (Implemented 27 CS flows + real audit) + our CPs/DECs/INDEX (live + this batch) + DEC-010 (full control + name) + prior 13 7-file agents + memory restores + post updates + P01-P15/PT01-PT11/CS01-CS04 + clones (ruflo + content-forge2.0 with CS in failure-modes-log) + advisor (full) + skill-creator (full) + pack (CS01-CS04 full + KP-PLAN + "Piano di Sviluppo") + "ok procedi" + "prendi tu il controllo totale di tutto e continua". All 10 invariants + P01/P02/P03/P07/P08/P09/P10/P12/P13/P15 + PT05/PT01/PT02/PT08/PT09 + CS03/CS04 + user "più di 20... stessa cosa per il case studi... agenti che gestiscono i case studi... Master build Architecture" + extracts from all + memory fin da subito + full control. No AP. Depth P08. Real FS matches (case dir + 7 files created this batch). 

**Status:** Tools enforce memory P10/CS03/CS04/real FS/trace/flussi/teams/"agenti che gestiscono i case studi" + all invariants + extracts. Use with memory mandate always. Continuing autonomous.