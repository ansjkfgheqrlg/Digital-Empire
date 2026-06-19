# SKILL
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > agent-factory > skills > agent-builder]]

## Content

---
name: agent-builder
description: This skill should be used when the user wants to "create the agent files", "build the plugin", "turn system prompts into files", "write the agent markdown files", "create the .md files for my agents", "build my plugin structure", "make my agents ready to install", or when the agent-architect and system-prompt-forge skills have completed their work and it is time to produce actual, runnable Claude Code plugin files. Trigger this as the THIRD step in agent creation. Also trigger it whenever a user has a system prompt and wants to turn it into a proper Claude Code agent file with correct frontmatter, structure, and plugin layout.
version: 1.0.0
---

# Agent Builder

This is the third skill in the agent-factory pipeline. Its inputs are:
1. The Architecture Blueprint from `agent-architect`
2. The System Prompts Document from `system-prompt-forge`

Its output is a complete, installable Claude Code plugin with all agent `.md` files, proper frontmatter, plugin manifest, and directory structure.

## The Build Process

### Step 1: Set Up Plugin Structure

Create the plugin directory structure. Use the Architecture Blueprint to determine what components are needed.

**Standard multi-agent plugin:**
```bash
mkdir -p [plugin-name]/.claude-plugin
mkdir -p [plugin-name]/agents
mkdir -p [plugin-name]/skills     # only if adding skills
mkdir -p [plugin-name]/commands   # only if adding slash commands
```

**Create the manifest:**

File: `[plugin-name]/.claude-plugin/plugin.json`
```json
{
  "name": "[plugin-name]",
  "version": "1.0.0",
  "description": "[What this agent system does in one sentence]",
  "author": "[author]"
}
```

### Step 2: Build Each Agent File

For every agent in the Architecture Blueprint, create a `.md` file in `agents/`.

Use the Agent File Template below. Pull the system prompt from the System Prompts Document.

**Agent File Template:**

```markdown
---
name: [agent-identifier]
description: Use this agent when [specific triggering conditions]. Examples:

<example>
Context: [Scenario description]
user: "[Realistic user request that should trigger this agent]"
assistant: "[How the assistant should respond — acknowledging it will use this agent]"
<commentary>
[Why this agent is the right choice for this scenario]
</commentary>
</example>

<example>
Context: [Different scenario]
user: "[Another realistic request]"
assistant: "[Response]"
<commentary>
[Reasoning]
</commentary>
</example>

model: [inherit | sonnet | opus | haiku]
color: [blue | cyan | green | yellow | magenta | red]
tools: ["Tool1", "Tool2"]
---

[SYSTEM PROMPT FROM system-prompt-forge — paste here verbatim]
```

### Step 3: Frontmatter Field Rules

**name:**
- Lowercase only
- Hyphens for spaces (no underscores, no spaces)
- 3-50 characters
- Must start and end with alphanumeric
- Good: `cro-researcher`, `content-writer`, `master-orchestrator`
- Bad: `CROResearcher`, `my_agent`, `-helper-`

**description:**
- This is the TRIGGERING mechanism — the most critical field
- Must start with "Use this agent when..."
- Must include 2-4 `<example>` blocks
- Each example needs: Context, user, assistant, commentary
- Be specific: not "helps with copy" but "when the user needs a sales email for a cold outreach campaign"

**model:**
| Model | Use case |
|---|---|
| `inherit` | Default — same model as parent conversation |
| `opus` | Complex reasoning, judgment, strategy, orchestration |
| `sonnet` | Balanced tasks — writing, coding, research |
| `haiku` | Fast parsing, classification, formatting, routing |

**color:**
| Color | Meaning convention |
|---|---|
| `blue` | Analysis, research, thinking |
| `cyan` | Data, technical, structured output |
| `green` | Creation, generation, writing |
| `yellow` | Validation, checking, QA |
| `red` | Critical, security, blocking decisions |
| `magenta` | Strategy, orchestration, creative direction |

**tools:**
Apply least-privilege. Only include tools the agent actually needs.

```yaml
# Read-only research agent
tools: ["Read", "Grep", "Glob", "WebSearch"]

# Code generation agent
tools: ["Read", "Write", "Grep", "Bash"]

# Orchestrator (needs everything)
# Omit tools field — agent gets all tools by default
```

### Step 4: Write High-Quality Description Examples

The `<example>` blocks in the description are what make an agent trigger reliably. Write them as realistic conversations.

**Weak example:**
```
user: "help me with marketing"
assistant: "I'll use the marketing agent"
```

**Elite example:**
```
Context: User has a landing page for a high-ticket coaching program and needs to rewrite the hero section.
user: "My landing page hero section is getting low CTR. The headline is 'Transform Your Life With Coaching' — can you rewrite it to be more compelling?"
assistant: "I'll use the CRO copywriting agent to analyze your current headline against conversion principles and produce 3 alternative versions with CRO rationale for each."
<commentary>
This is a direct-response copywriting task requiring CRO expertise. The user is asking for conversion-optimized output, which is exactly this agent's specialty.
</commentary>
```

The elite version gives the triggering AI specific context, a realistic user message, and a clear reason why this agent was chosen.

### Step 5: Validate All Files

Before declaring the build complete, validate every agent file:

- [ ] `name` field: lowercase, hyphens only, 3-50 chars, starts/ends alphanumeric
- [ ] `description` field: starts with "Use this agent when...", has 2+ examples, each example has context/user/assistant/commentary
- [ ] `model` field: one of inherit/sonnet/opus/haiku
- [ ] `color` field: one of the 6 valid colors
- [ ] `tools` field: array of valid tool names (or omitted for full access)
- [ ] System prompt: present and starts with "You are..."
- [ ] System prompt: includes mission, responsibilities, process, output contract, constraints
- [ ] `plugin.json`: valid JSON, has name/version/description

### Step 6: Create Install Instructions

After building all files, produce a short install guide:

```markdown
## Install Instructions

1. Save this plugin to: `C:\Users\[name]\.claude\plugins\[plugin-name]\`
2. In Claude Code, run: `/plugin install [plugin-name]`
   OR: Open Claude Code settings → Plugins → Add local plugin → select folder
3. Restart Claude Code if needed
4. Test by triggering one of the agents with a phrase from its description examples
```

### Step 7: Hand Off to Quality Sentinel

After building, tell the user:
> "Plugin built and ready. The final step is **agent-quality-sentinel** to review and validate everything before installation. Say 'review my agents' to continue."

## Additional Resources

- **`references/plugin-structure.md`** — Complete plugin directory reference and plugin.json schema

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Outreach|Outreach Area]]
