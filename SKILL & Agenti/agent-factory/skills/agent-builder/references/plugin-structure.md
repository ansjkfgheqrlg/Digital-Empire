# Plugin Structure Reference

## Complete Directory Layout

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json              ← REQUIRED: plugin manifest
├── agents/
│   ├── orchestrator.md          ← agent files
│   ├── researcher.md
│   └── writer.md
├── skills/                      ← optional
│   └── skill-name/
│       ├── SKILL.md
│       └── references/
├── commands/                    ← optional
│   └── command-name.md
└── README.md                    ← optional but recommended
```

## plugin.json Schema

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "One sentence describing what this plugin does.",
  "author": "Author Name or Organization",
  "homepage": "https://example.com",  // optional
  "license": "MIT"                    // optional
}
```

**Required fields:** `name`, `version`, `description`
**Optional fields:** `author`, `homepage`, `license`

## Agent File Schema (complete frontmatter)

```yaml
---
name: agent-identifier           # REQUIRED: lowercase, hyphens, 3-50 chars
description: |                   # REQUIRED: triggering conditions + examples
  Use this agent when [conditions]. Examples:

  <example>
  Context: [scenario]
  user: "[user message]"
  assistant: "[how assistant responds]"
  <commentary>
  [why this agent triggers here]
  </commentary>
  </example>

model: inherit                   # REQUIRED: inherit | opus | sonnet | haiku
color: blue                      # REQUIRED: blue | cyan | green | yellow | magenta | red
tools: ["Read", "Write", "Grep"] # OPTIONAL: omit for full tool access
---
```

## Auto-Discovery Rules

Claude Code automatically discovers agents when:
1. Plugin is installed (via `/plugin install` or settings)
2. Agent files are `.md` files inside `agents/` directory
3. Files have valid YAML frontmatter with required fields

**File naming:** Use the same name as the `name` field in frontmatter.
- frontmatter `name: cro-researcher` → file should be `cro-researcher.md`

## Installing a Local Plugin

**Method 1: CLI**
```bash
# In Claude Code terminal
/plugin install /absolute/path/to/plugin-folder
```

**Method 2: Settings UI**
Claude Code → Settings → Plugins → Add Local Plugin → Select folder

**Method 3: Copy to plugins directory**
```
C:\Users\[username]\.claude\plugins\[plugin-name]\
```
Then restart Claude Code.

## Namespacing

When multiple plugins are installed, agents are namespaced:
- Single plugin with agent `researcher` → accessible as `researcher`
- Multiple plugins have same agent name → accessible as `plugin-name:researcher`

## Debugging Plugin Discovery

If agents are not appearing:
1. Check `plugin.json` is valid JSON (use a JSON validator)
2. Check agent `.md` files have valid YAML frontmatter
3. Check `name` field follows naming rules (no uppercase, no underscores)
4. Restart Claude Code after installation
5. Run `/plugin list` to see installed plugins

## Example: Minimal Working Plugin

```
my-agent/
├── .claude-plugin/
│   └── plugin.json
└── agents/
    └── helper.md
```

`plugin.json`:
```json
{"name": "my-agent", "version": "1.0.0", "description": "A helper agent."}
```

`agents/helper.md`:
```markdown
---
name: helper
description: Use this agent when the user asks for help. Examples:

<example>
Context: User needs assistance.
user: "Can you help me with this?"
assistant: "I'll use the helper agent."
<commentary>Direct help request triggers this agent.</commentary>
</example>

model: inherit
color: blue
---

You are a helpful assistant...
```
