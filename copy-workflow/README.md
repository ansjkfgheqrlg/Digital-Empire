# copy-workflow

Multi-agent copywriting system for Claude Code. Built on the APSOC framework: Attention, Problem, Solution, Objections, CTA.

Invoke with `/copywriting [mode]` inside any Claude Code session.

## Modes

| Command | Output | Time |
|---|---|---|
| `/copywriting full` | Complete copy + QA report (A1-A8) | 60-120 min |
| `/copywriting ad` | 3 ad variants (FB/IG/TikTok/Google) | 15-20 min |
| `/copywriting sales-page` | Full sales page 1000-5000 words | 90-120 min |
| `/copywriting email` | Email sequence (welcome / nurture / launch) | 45-90 min |
| `/copywriting vsl` | VSL script 8-20 min | 60-90 min |
| `/copywriting social` | 5 social posts (IG/FB/LinkedIn) | 20-30 min |
| `/copywriting headline` | 10+ headline variants | 10 min |
| `/copywriting objections` | CPB for specific objections | 10-15 min |
| `/copywriting avatar` | Buyer persona | 15-20 min |
| `/copywriting funnel` | Strategic funnel plan | 20-30 min |
| `/copywriting review` | Review + APSOC score /100 | 10-20 min |

## Structure

```
copy-workflow/
├── SKILL.md                    entry point + routing
├── orchestrators/
│   └── copy-master.md          main orchestrator
├── agents/
│   ├── research/               A1 briefing, A2 target analysis
│   ├── apsoc/                  A3-A7 writing agents
│   ├── strategy/               positioning, funnel, campaign
│   └── qa/                     A8 reviewer + score
├── skills/                     6 standalone sub-skills
├── workflows/                  6 complete pipelines
├── references/                 concepts, patterns, anti-patterns
├── templates/                  briefing, avatar, checklist, CPB
└── evals/                      8 test scenarios
```

## APSOC Rule

Problem always before Solution. Showing the solution first is the most expensive copywriting mistake. The QA agent enforces this with an automatic -15 point penalty.

## QA Gate

Score >= 80 to ship. Score >= 85 required for sales pages. Below threshold: the failing section is rewritten automatically.

## Origin

Built with content-forge from "Il Manuale del Copywriting v1.1" (115 pages, ~22,700 words). Build date: 2026-05-26.
