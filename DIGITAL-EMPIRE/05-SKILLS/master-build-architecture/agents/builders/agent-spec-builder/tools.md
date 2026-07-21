# Agent-Spec-Builder — Tools (L3 Deterministic + External)

**Overview:** Tools for the Agent-Spec-Builder. Mix of L3 Python (deterministic per P05-markdown-plus-python.md), file ops, memory automation (P10), external (Ruflo npx, bash for validation, spawn for subagents). All tools enforce traceability, memory updates, canonical shapes.

**Tool 1: ReadFile (or Bash read)**
- Description: Read any file in workspace (/home/user), clones (projects/ruflo/, projects/content-forge2.0/), knowledge-pack source (/home/user/skill-planning-knowledge-pack/), installed advisor (projects/.agents/skills/context-engineering-advisor/SKILL.md), past memory/ (CPs/DECs/INDEX for examples), agents/ (existing 7 files as shape examples), references/knowledge-pack/.
- Input Schema:
```python
{
  "path": str,  # e.g. "/home/user/skill-planning-knowledge-pack/02-patterns/PT05-canonical-files-per-target.md" or "projects/content-forge2.0/agents/builders/agent-builder-agent.md"
  "max_lines": int | None,  # for large; default full or chunk
  "chunk": int | None
}
```
- Output: Full text or chunk + metadata (size, last_mod, traceability note "Read for agent-spec-builder build of [slug]; source PT05 §1")
- Errors: File not found → return error + suggest ASK for clarification; too large → chunk + CP log.
- Example:
```python
read_file(path="/home/user/projects/content-forge2.0/agents/builders/agent-builder-agent.md", max_lines=100)
# Output: frontmatter + "You are the builder for the target `agent`..." + trace link
```
- Memory Mandate: After read, if key source: CP "Read [source] for [slug] agent spec" in target + self memory/. Append INDEX with "Extracted PT05 full + agent-builder-agent.md for BUILD step 1".
- Trace: P05 (md+py for schema), PT05 (canonical), Content-Forge (load step), P12 (log source).

**Tool 2: WriteFile (exact 7 files)**
- Description: Write one of the 7 canonical files to target dir (e.g. agents/builders/[slug]/ or user target agents/[family]/[slug]/). Enforce order (tools first), min content, traceability headers.
- Input Schema:
```python
{
  "path": str,  # full target path e.g. "/home/user/projects/.agents/skills/master-build-architecture/agents/builders/agent-spec-builder/system-prompt.md"
  "content": str,  # full deep content
  "trace_header": str  # e.g. "Trace: PT05 §3 + content-forge... + CP-027 + user ASK Q2"
}
```
- Output: Success + file size + CP logged automatically.
- Errors: Path not in canonical shape → fail + suggest fix; content too short (< min per P06) → fail + iterate.
- Example: Write tools.md first with schemas, then others.
- Memory Mandate: BEFORE write: CP "About to write [file] for [slug]". AFTER write: CP "Wrote [file] [size] lines; verified canonical + trace". Run manager --checkpoint on both targets. Append INDEX "Wrote [file] per PT05 BUILD order".
- Trace: P05 (md for LLM, py embedded), PT05 (exact files), P06 (mins), P08 (depth), P10 (update after write), P12.

**Tool 3: Bash (for structure, validation, external)**
- Description: Run shell commands for mkdir -p agent dir, ls/find to verify 7 files, python memory_manager.py calls, npx ruflo (if swarm agent), python -c for quick schema checks, rsync for sync top/embedded memory.
- Input: command str, cwd optional, timeout.
- Output: stdout/stderr/exit.
- Examples:
  - "mkdir -p /home/user/projects/.agents/skills/master-build-architecture/agents/builders/new-agent"
  - "python /home/user/projects/.agents/skills/master-build-architecture/scripts/memory_manager.py --checkpoint '7 files for new-agent started' --phase=4 --target=/home/user"
  - "npx ruflo swarm init --name test --memory-first" (for swarm agents)
  - "find /home/user/projects/.agents/skills/master-build-architecture/agents/builders/agent-spec-builder -name '*.md' | wc -l"  # should be 7
- Memory Mandate: Wrap every bash with CP before/after if it changes state (e.g. mkdir, write via shell, manager run). Log command + result in CP.
- Trace: P05 (py for deterministic), Ruflo (npx), P10 (manager calls), P12.

**Tool 4: MemoryManager (Python wrapper / direct calls)**
- Description: High-level for P10 updates. Internally calls the memory_manager.py script or equivalent.
- Input Schema (for create_checkpoint):
```python
{
  "target": str,  # "/home/user" or skill root or user project
  "desc": str,
  "phase": int = 4,
  "linked_principles": str = "P10, P12, PT05, PT07, user screenshot, Ruflo memory, Content-Forge logs"
}
```
- Similar for record_decision (title, decision, rationale, alternatives, consequences, traceability).
- Also: append_to_index, ensure_structure.
- Output: file paths created.
- Example usage in playbook/memory.md: always call for both targets.
- Errors: Target not writable → fallback to print + manual note in INDEX.
- Memory Mandate: This tool itself triggers memory updates (meta). Log "MemoryManager call for [desc]" as CP.
- Trace: P10, P12, Ruflo (if AgentDB), Content-Forge (failure-logs), Context-Eng (two-layer), user screenshot.

**Tool 5: SpawnSubAgent (for ASK, critique, depth)**
- Description: Delegate to other L2/L3 per three-level (P07/PT01). E.g. question-designer-agent for ASK, failure-detector-agent for SI/critique, skill-depth-agent (O1) for depth pass, qa agents for validation, plan-builder for PLAN.
- Input: agent_name, task_context (tight boundary list of atoms), output_path, handoff_note.
- Output: sub-agent result + logged handoff DEC in memory/.
- Example: Spawn question-designer for "5Qs for agent-spec-builder role: name, inputs, constraints, success, examples"
- Memory Mandate: Before spawn: CP "Spawning [sub] for [purpose]". After: DEC "Handoff from agent-spec-builder to [sub]: [details]". Update INDEX both. Append to target sessions/ if interactive.
- Trace: PT01, P07, P04 (scaffolding), P12 (handoff log), Ruflo (queen delegation).

**Tool 6: ValidateShape (future L3, stub now; use bash/python for now)**
- Description: Check output against PT05/P06 canonical + mins (7 files, word counts, traceability count, failure table size, memory.md present with P10 protocol, no-summary lint).
- Input: agent_dir path.
- Output: pass/fail + report (missing files, shallow sections, missing traces).
- If fail: return report + trigger iterate (handoff back to self with critique).
- Memory: Log validation as CP/DEC "Shape validation for [slug]: [result]".
- Trace: PT06 (schema tightening), P06, P09 (failures), C1/C3 from content-forge, our qa agents.

**Additional Notes:**
- All tools must embed Python blocks in .md outputs per P05 (e.g. schemas above).
- For Ruflo: if RUFLO_MEMORY=1, prefer memory_store over FS for long-term, but always FS for human-readable INDEX/CPs (hybrid per Ruflo + our P10).
- External: npx skills, npx ruflo, python for our scripts.
- Deterministic: Prefer Python for validation, mkdir, manager calls (L3).
- LLM (you): For synthesis, expansion, writing prose prompts/playbooks (L2).
- Every tool call in practice: log in memory/ + INDEX.

**Trace for this tools.md:** Extracted/expanded from P05-markdown-plus-python.md (rule table + embedded py examples), PT05 (validation via schema), content-forge2.0 references/schemas/agent.schema.json (example json shape), references/processes/agent.md (tools section), Ruflo (memory + npx), memory_manager.py (full code), our scripts/ + past agent tools.md (e.g. conductor/tools.md, memory-ecosystem-builder/tools.md as examples), P12 traceability. All atoms linked to sources. No summary.

**Status:** Complete for v1. Will be expanded in depth pass (O3 reference-expander for more from clones). 

**End of tools.md. Memory updated on creation.**