# Refactoring YouTube Automation into APEX-7

Refactoring the YouTube Automation codebase from `.claude/skills/youtube-automation-factory` into the new workspace `YOUTUBE-AUTOMATION-FACTORY` following the **APEX-7** framework structure. 

The APEX-7 framework introduces a structured, event-driven, memory-connected, quality-gated multi-agent architecture.

---

## The 7-Step Architectural Evolution (Plan 1 to Plan 7)

### 📈 Plan 1: L1 - Le Fondamenta (Foundations)
- **Goal**: Set up the physical directory structure and import the core YouTube knowledge files (the Master Knowledge Document `MKD.md`, `ARCHITECTURE.md`, `SKILL.md`) into `YOUTUBE-AUTOMATION-FACTORY`. Create skeleton implementations for the APEX-7 components:
  - `memory.py` (Memory Query Interface)
  - `event_bus.py` (Publish-Subscribe Bus)
  - `quality_gate.py` (Quality Gate Definitions & Engine)
  - `gate_agent.py` (Quality Check Agent)
- **Pass Gate**: All files exist, compile, and simple unit tests verify component existence.

---

### 🔗 Plan 2: L2 - Struttura Connessa (Connected Structure)
- **Goal**: Wire the YouTube Conductor and operators (Niche Scout, Video Hunter, Script Writer, Video Producer, Metadata Optimizer, SEO Analyst) to the Event Bus and Memory.
- **Key Changes**:
  - The Conductor publishes a `task.created` event when it starts.
  - Operators communicate exclusively by publishing events (e.g., `niche.scouted`, `script.written`) instead of calling each other directly.
  - The `GateAgent` (`GATE-1`) listens to event requests and evaluates outputs against specific criteria for each phase.
- **Pass Gate**: End-to-end event chain works. Event log shows messages flowing from one agent to another via the Event Bus.

---

### 🔄 Plan 3: L3 - Loop Adattivi (Adaptive Loops)
- **Goal**: Implement feedback and error recovery loops.
- **Key Changes**:
  - If the `GateAgent` fails a step (e.g., the script written is too long or does not fit the target video), a `gate.failed` event is published.
  - A remediation flow triggers: the script writer receives the feedback, queries the Memory Decision Log, adapts its strategy, and retries.
  - If it fails 3 times, the Escalation Protocol freezes the flow and logs the anti-pattern.
- **Pass Gate**: Successfully demonstrates automatic retry and strategy change on simulated failures (e.g. forced low SEO score -> regeneration).

---

### ⚡ Plan 4: L4 - Parallelismo & Integrazione RuFLO (Concurrency & RuFLO)
- **Goal**: Introduce concurrent execution of tasks and interface with the RuFLO codebase.
- **Key Changes**:
  - Allow running multiple niche scouting tasks or script iterations in parallel.
  - Handle race conditions when writing to the central Memory DB using the Write-Lock (100ms timeout).
  - Map and integrate RuFLO API points for automation tasks.
- **Pass Gate**: Multiple concurrent agent execution runs successfully without database corruption or deadlock.

---

### 🧠 Plan 5: L5 - Intelligenza (Intelligence & Meta-Agent)
- **Goal**: Implement a supervisor agent (Meta-Agent) that has complete visibility over the swarm.
- **Key Changes**:
  - The Meta-Agent analyzes the overall workflow, detects failure patterns, and calculates dynamic quality scores.
  - It adjusts the instructions or inputs of operators based on past run history.
- **Pass Gate**: Meta-Agent successfully detects a repeating bottleneck in logs and corrects the prompt parameters.

---

### ♻️ Plan 6: L6 - Auto-Evoluzione (Self-Evolution)
- **Goal**: Allow the system to optimize its own operations within safe boundaries.
- **Key Changes**:
  - Implement memory compression (archiving low-relevance or old logs to prevent token bloat).
  - Let the system update its own rules file (`learned_rules.json`) based on performance audit results.
  - Establish strict spawning limits for agents and enforce human-override requirements for safety-critical steps.
- **Pass Gate**: System compresses its memory size and adds a new rule to its blacklist without human manual editing.

---

### 🏆 Plan 7: L7 - APEX Integration (Full Swarm & E2E Validation)
- **Goal**: Run the complete, coordinated swarm from beginning to end with self-healing capabilities.
- **Key Changes**:
  - Coordinated multi-swarm handling.
  - End-to-end execution of a real/mock YouTube video generation task (Scout -> Selection -> Script -> Video Spec -> SEO optimized title/desc -> mock upload).
  - Generation of a Consolidated Performance Dashboard.
- **Pass Gate**: 100% test coverage of all quality gates, self-healing demonstrated on multiple failure scenarios, and a clean run outputting all files.

---

## Brainstorming & Open Questions

To kick off the brainstorming session, Gael, here are a few simple questions:

1. **Il Canale e la Nicchia**: Abbiamo già delle nicchie pre-selezionate o dei canali di riferimento da usare come test iniziale per la fabbrica YouTube, oppure preferisci che il sistema inizi a cercarli da zero?
2. **Il Ruolo di Fliki**: Nella produzione dei video, useremo Fliki (tramite le sue istruzioni/spec) come strumento principale di creazione. Vuoi che la fabbrica generi solo le specifiche testuali pronte per essere incollate in Fliki, o prevedi un'integrazione più automatizzata?
3. **Controllo Umano (Gate)**: In quale fase preferisci avere il controllo manuale (es. approvare lo script prima di fare il video, o controllare il video finale prima di pubblicarlo)?
4. **Obiettivo Finale del Video**: I video avranno lo scopo di vendere i nostri info-prodotti (funnel) o punteranno a fare visualizzazioni di massa (Cash Cow classica)?

---

## Verification Plan

### Automated Tests
- Create `test_youtube_apex7.py` to test the event bus routing, memory lock timeouts, quality gate checks, and Conductor state machine.
- Run the test suite: `python -m unittest 02-AUTOMAZIONI-E-SCRIPTS/test_youtube_apex7.py`

### Manual Verification
- Execute a dry-run of the Conductor pipeline from Phase 1 to Phase 5 in headed/dry-run mode, producing final script files and metadata check reports.
