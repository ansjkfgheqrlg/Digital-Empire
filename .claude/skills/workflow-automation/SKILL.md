---
name: workflow-automation
description: >
  Multi-step workflow automation with explicit dependencies, agent coordination, and
  reusable templates. Orchestrates complex processes that span multiple sessions or
  involve parallel agents. Defines WHAT executes WHEN and in WHAT ORDER.
trigger: "when designing or executing a multi-step automated process that will repeat"
skip: "one-off tasks, simple single-chain operations"
---

# Workflow Automation

## Core Concept
A workflow is a named, repeatable sequence of steps with explicit dependencies.
Write workflows as code, not as prose — they should be executable, not descriptive.

## Workflow Structure
```yaml
name: daily-outreach
schedule: every day at 09:00
steps:
  - name: scrape
    agent: scraper-swarm
    task: "Collect 500 leads from all sources"
    timeout: 60min
    
  - name: dedup
    depends: [scrape]
    agent: pipeline
    task: "Remove duplicates, validate emails"
    
  - name: enrich  
    depends: [dedup]
    agent: ai-enricher
    task: "Add company info, personalization data"
    
  - name: send
    depends: [enrich]
    agent: email-sender
    task: "Send emails via Bibbia sequence"
    gate: human-approval  # pause and wait for Max to review
    
  - name: log
    depends: [send]
    agent: reporter
    task: "Update dashboard, write session log"
```

## Exponium Workflow Library

### Workflow 1: Daily Lead Generation
```
scrape-google-maps → scrape-facebook → scrape-linkedin → scrape-youtube
       ↓                                                        ↓
  dedup-merge ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
       ↓
  validate-emails
       ↓
  store-leads-db
       ↓
  dashboard-refresh
```

### Workflow 2: Email Campaign Dispatch
```
get-uncontacted-leads(100)
       ↓
  bibbia-selector (which sequence for this lead?)
       ↓
  ai-personalizer (add company/name context)
       ↓
  human-review (Max approves batch)
       ↓
  smtp-sender (rate: 50/hour max)
       ↓
  log-status
```

### Workflow 3: Canva Carousel Generation (Gael's domain)
```
get-approved-topic
       ↓
  ai-copy-generator (Claude API → carousel copy)
       ↓
  canva-playwright (open template, fill text, download)
       ↓
  hitsfield-upload
       ↓
  schedule-post
```

### Workflow 4: Session Start/End (daily ritual)
```
START:
  read-giornata-md → show-daily-plan → set-today-todos

END (triggered by "finito/basta"):
  update-giornata-md → git-add-all → git-commit → git-push → confirm-user
```

## Outline-First Pattern for Structured Deliverables

When a workflow produces a structured output (presentations, reports, documents with multiple sections), always split into two steps:

1. **Step 1 — Outline:** Ask for the structure first. Validate before building.
   > "Dimmi prima la scaletta, poi la costruisci."
2. **Step 2 — Build:** Only after approval, execute the full generation.

**Why:** Correcting a bad structure at step 1 costs nothing. Correcting it at step 2 means discarding generated content. This pattern applies to any deliverable with a hierarchical structure: presentations, reports, email sequences, landing page sections, onboarding flows.

**Opus 4.8 with MEDIO/ALTO effort handles this natively** — it will propose the outline, pause, and wait for confirmation before proceeding.

---

## Implementing Workflows in Claude Code

### For daily workflows (use CLAUDE.md hooks):
Add to CLAUDE.md:
```
## WORKFLOW: DAILY-OUTREACH
Trigger: Max says "avvia scraping"
Steps:
1. Check GIORNATA.md for last scrape result
2. Run: python outreach/main.py --mode scrape
3. Report: X leads collected, Y duplicates removed
4. Push results to GitHub
```

### For code workflows (use TodoWrite):
```python
# Define the workflow as ordered todos
workflow_steps = [
    "Scrape: python scrapers/google_maps.py --limit 100",
    "Scrape: python scrapers/facebook.py --limit 100",
    "Merge: python pipeline/dedup.py",
    "Validate: python pipeline/validator.py",
    "Report: show count to Max",
]
```

## Reusable Templates

| Template | When to use |
|----------|------------|
| `scrape-pipeline` | Any data collection task |
| `sparc-dev-session` | Any development chapter |
| `session-close` | End of every session |
| `review-deploy` | After significant feature |
| `canva-generate` | Content factory batch |
