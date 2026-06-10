# Agent Factory

A pipeline of 4 skills that collaborate to design, write, build, and validate professional Claude Code agents.

## The Pipeline

```
[1] agent-architect      → Design the blueprint
        ↓
[2] system-prompt-forge  → Write elite system prompts
        ↓
[3] agent-builder        → Build plugin files
        ↓
[4] agent-quality-sentinel → Audit, score, and fix
```

## Skills

### 1. agent-architect
Design the complete architecture before writing a single line. Defines agent map, data flow, model assignments, tool matrix, and failure modes.

### 2. system-prompt-forge
Transform the architecture blueprint into elite, production-grade system prompts using proven frameworks (CoT, ReAct, ToT, Critic-in-the-Loop).

### 3. agent-builder
Build the actual `.md` files, plugin manifest, and directory structure. Validates frontmatter, writes description examples, and produces install instructions.

### 4. agent-quality-sentinel
Multi-dimensional audit: structural validity, triggering quality score, system prompt depth score, architecture coherence. Provides specific fixes and issues final installation clearance.

## Install

Copy this folder to `C:\Users\[username]\.claude\plugins\agent-factory\`
Then in Claude Code: `/plugin install agent-factory`

## Usage

1. Say: "I want to build an agent that [describes goal]"
2. `agent-architect` triggers → produces Architecture Blueprint
3. Say: "write the system prompts"
4. `system-prompt-forge` triggers → produces System Prompts Document
5. Say: "build the agents"
6. `agent-builder` triggers → produces plugin files
7. Say: "review my agents"
8. `agent-quality-sentinel` triggers → audits and clears for install
