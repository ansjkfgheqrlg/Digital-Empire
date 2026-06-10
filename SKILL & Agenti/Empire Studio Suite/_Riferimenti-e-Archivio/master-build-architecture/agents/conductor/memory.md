# Conductor Memory Spec (Embedded)

The Conductor maintains and enforces the memory ecosystem for the entire run.

**Responsibilities:**
- Before any major action: Ensure memory/ structure exists (via memory_manager.py --init if needed).
- After every handoff/decision/critique: Create or append CP/DEC/SES entry.
- Use two-layer: Short-term conversational context in current session + long-term via INDEX + Ruflo memory_store when available.
- Enforce Research→Plan→Reset→Implement: After research-heavy phases, force synthesis to high-density PLAN, then reset before implementation.
- Maintain traceability: Every memory entry must cite sources and principles applied.

**In this very build:** We are dogfooding — see /home/user/memory/ (top) and the skill's own memory/.

**Integration:** The conductor always calls or instructs use of memory_manager.py for automation.