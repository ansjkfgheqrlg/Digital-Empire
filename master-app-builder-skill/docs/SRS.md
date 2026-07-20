# Software Requirements Specification (SRS)

## Project: Master App Builder Skill

### 1. Overview
A reusable, Italian-first operational skill that guides an AI agent through the disciplined discovery, design, implementation, verification, documentation, and delivery of software applications.

### 2. Users
- Product owners who need a structured app-development workflow.
- AI agents or development assistants executing the workflow.

### 3. Functional requirements
- **RF-001:** Begin each project session by recovering its saved state and reporting the current checkpoint.
- **RF-002:** Never implement a product when material requirements are ambiguous; ask concise, decision-oriented questions.
- **RF-003:** Produce an approved SRS before architecture and implementation.
- **RF-004:** Define architecture, design system, acceptance criteria, security model, and test plan before building.
- **RF-005:** Verify implementation using appropriate tests and quality tools; report actual results without inventing metrics.
- **RF-006:** Persist a concise project state and handover at the end of every session.

### 4. Non-functional requirements
- Python-first defaults; Python 3.11+ compatibility.
- Transparent progress, explicit assumptions, no fabricated test or deployment outcomes.
- Secure-by-default handling of secrets, authentication, and user data.

### 5. Acceptance criteria
- The deliverable is a self-contained `SKILL.md` that can be pasted into an agent configuration.
- It supplies phase gates, templates, standards, and an end-of-session state format.
- It distinguishes required checks from optional checks according to the actual project stack.
