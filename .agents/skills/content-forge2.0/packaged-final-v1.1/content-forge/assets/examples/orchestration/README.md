# Esempio end-to-end — target `orchestration`

> Output di `B6 orchestration-builder-agent`.
> Trasforma il workshop in un **orchestration layer** che decide quale tecnica/agent applicare in base alla richiesta del developer.

## Input

- Sorgente / KG / MKD: `_shared/`
- **existing_components.json** (REQUIRED): l'utente ha già 4 componenti
  - `prompt-coach` (agent, per single-task help)
  - `prompt-team` (team, per task complessi multi-stage)
  - `prompt-engineer-helper` (skill, per quick reference)
  - `prompt-review-workflow` (workflow, per CI/CD review)
- ASK answers:
  - Strategy: **hybrid** (rule-based per casi ovvi, LLM-based per ambigui)
  - Default fallback: `prompt-coach`
  - Budget: $200/mese
  - Policies: priorità a richieste high-stakes (production deployment)
  - Observability: Datadog
  - Escalation: humano se 3 fail consecutivi su stesso request

## Output

```
prompt-ops-orchestration/
├── supervisor.md                       # SP del supervisor LLM (Sonnet)
├── routing.md                          # 8 regole rule-based + supervisor prompt
├── registry.md                         # catalogo 4 componenti
├── registry.json                       # machine-readable
├── policies.md                         # budget, priority, security
├── observability.md                    # Datadog metrics + tracing spec
├── failure_modes.md                    # 9 failure
├── escalation.md                       # 4 trigger di escalation
├── eval_scenarios.json                 # 8 input → componente atteso
└── README.md
```

## Routing rules (preview)

| # | Condition | Route to | Priority | Reason |
|---|-----------|----------|----------|--------|
| 1 | input.context = "PR opened" + path matches `prompts/**` | `prompt-review-workflow` | 1 | esplicito trigger CI/CD |
| 2 | input.complexity = "high" + multi_step = true | `prompt-team` | 2 | beneficia di specializzazione 4 agenti |
| 3 | input.urgent = true + tier = "enterprise" | `prompt-team` | 1 | priority a enterprise |
| 4 | input contains "scrivi un prompt" + complexity = "low/medium" | `prompt-coach` | 3 | default per quick help |
| 5 | input contains "how does X work" / "explain" | `prompt-engineer-helper` skill | 3 | quick reference, no full pipeline |
| 6 | input.context_window_estimate > 8000 tokens | `prompt-team` | 2 | context lungo richiede decomposition |
| 7 | input.cost_sensitive = true | `prompt-engineer-helper` skill | 4 | skill è il più economico |
| 8 | default (no rule match) | LLM supervisor decides | 99 | fallback |

## Registry (preview)

```json
{
  "version": "1.0",
  "components": [
    {
      "slug": "prompt-coach",
      "type": "agent",
      "path": "/agents/prompt-coach/",
      "owner": "ml-platform-team",
      "description": "1-on-1 prompt coaching for single tasks",
      "cost_class": "low",
      "latency_class": "fast",
      "status": "stable"
    },
    {
      "slug": "prompt-team",
      "type": "team",
      "path": "/teams/prompt-team/",
      "owner": "ml-platform-team",
      "description": "4-agent team for complex multi-stage prompts",
      "cost_class": "high",
      "latency_class": "slow",
      "status": "stable"
    },
    {
      "slug": "prompt-engineer-helper",
      "type": "skill",
      "path": ".claude/skills/prompt-engineer-helper.skill",
      "owner": "ml-platform-team",
      "description": "Quick prompt reference inside Claude Code",
      "cost_class": "low",
      "latency_class": "fast",
      "status": "stable"
    },
    {
      "slug": "prompt-review-workflow",
      "type": "workflow",
      "path": "/workflows/prompt-review/",
      "owner": "devops-team",
      "description": "CI/CD review of prompts on PR",
      "cost_class": "medium",
      "latency_class": "normal",
      "status": "stable"
    }
  ]
}
```

## Supervisor SP (preview)

Used per routing decisions quando nessuna rule esplicita matcha:

```
You are the orchestrator for the Prompt Ops platform. Available components: 4.

Given an input request, decide which component to route to. Output JSON:
{
  "route_to": "<component-slug>",
  "confidence": 0.0-1.0,
  "reason": "<brief>",
  "alternatives": ["<other-slug>", ...],
  "needs_escalation": false,
  "estimated_cost_class": "low|medium|high"
}

[Registry inline]
[5 routing examples few-shot]

Routing principles:
- Prefer specialized over general when match is clear
- Prefer cheap over expensive when accuracy not critical
- Escalate to human if confidence < 0.5
```

## Policies

- **Budget**: $200/mese hard cap. Component invocations tracciate. Se 80% raggiunto → warning. 100% → blocco (escalation).
- **Priority**: tier=enterprise > pro > free. Enterprise mai sotto-prioritized.
- **Security**: `prompt-team` può scrivere su `~/Workspace/`, gli altri sono sandbox-only.
- **Versioning**: ogni componente ha `version` field; orchestrator preferisce versione stable.

## Stats

- 4 componenti registrati, 0 gap (tutti già costruiti)
- 8 routing rules + supervisor fallback
- 8 policies enforce
- 9 failure mode + 4 escalation trigger
- Eval scenarios: 8 input realistici → componente atteso (con tolerance per alternatives)

## Quando questa orchestration NON è giusta

- 1-2 componenti: overkill, basta if-else inline
- Routing puramente prevedibile: rule-based puro va bene, no LLM
- Latency-critical (<100ms): l'overhead del supervisor LLM non è accettabile
