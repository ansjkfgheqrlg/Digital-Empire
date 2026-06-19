# Project: Agency Agent Orchestration System

- **Type**: 🤖 Agent System / 🔧 Infrastructure
- **Status**: 🟡 Active Development
- **Owner**: Digital Empire
- **Created**: 2026-03-09
- **Purpose**: Automated agent system for running 3 concurrent CRO/growth pipelines targeting businesses without web presence, funnel optimization needs, and AI implementation opportunities
- **Tags**: `#agents` `#automation` `#cro` `#outreach` `#orchestration` `#python`

## 📖 Project Overview

Agency Agent Orchestration System is an internal automation framework that combines 3 proprietary sub-agents into a unified pipeline orchestrator. The system is built around **CLI-driven execution** and supports both single-pipeline and full-sequence execution modes.

The system's core philosophy: **One orchestrator handles decision logic and CLI routing; three specialized sub-agents execute in parallel; templates standardize outreach communication**.

## 🏗️ Architecture & Components

### Core Folder Structure
```
Agency/
├── orchestrator/              ← ENTRY POINT
│   ├── AGENT.md               (Decision logic documentation)
│   └── run.py                 (CLI: python run.py --pipeline [type])
│
├── sub-agents/                ← 3 SPECIALIZED AGENTS
│   ├── no-website/            Targets: Businesses without web presence
│   │   ├── AGENT.md
│   │   ├── pipeline.py        Main execution flow
│   │   ├── scraper.py         Lead discovery via directory/listings
│   │   ├── qualifier.py       Filters prospects by viability
│   │   ├── contact_finder.py  Extracts email/phone/SMS contact
│   │   └── message_generator.py Creates personalized outreach
│   │
│   ├── cro-funnel/            Targets: Businesses with conversion optimization needs
│   │   ├── AGENT.md
│   │   ├── pipeline.py        Main execution flow
│   │   ├── scraper.py         Website content analysis
│   │   ├── site_analyzer.py   Full funnel audit
│   │   ├── market_runner.py   Competitive benchmarking
│   │   ├── pdf_generator.py   Report PDF creation
│   │   └── email_composer.py  Audit report delivery
│   │
│   └── ai-implementation/     Targets: Businesses with AI needs
│       ├── AGENT.md
│       ├── pipeline.py        Main execution flow
│       ├── scraper.py         Company research
│       ├── ai_scorer.py       Scores AI opportunity fit
│       └── proposal_generator.py Creates AI implementation proposal
│
├── outreach/                  ← Legacy agent (imported)
├── agents/                    ← 5 pre-built market agents
├── skills/                    ← 15 market-specific skills
├── templates/                 ← Email/content templates (standardized)
├── requirements.txt           ← Python dependencies
└── .env.example              ← Environment config template
```

## 🚀 Execution Modes

### Single Pipeline Execution
Run individual pipeline targeting a specific business profile:

```bash
# No-Website Pipeline
python Agency/orchestrator/run.py --pipeline no-website --citta "Milano" --settore "ristoranti"

# CRO-Funnel Pipeline
python Agency/orchestrator/run.py --pipeline cro-funnel --citta "Roma" --settore "dentisti"

# AI-Implementation Pipeline
python Agency/orchestrator/run.py --pipeline ai-implementation --citta "Napoli" --settore "avvocati"
```

### Full Sequence Execution
Runs all 3 pipelines in sequence for comprehensive outreach:

```bash
python Agency/orchestrator/run.py --pipeline full --citta "Torino" --settore "commercialisti"
```

## 📊 Sub-Agent Definitions

### 1. **no-website/** Agent
**Problem Solved**: Businesses with audience but zero web presence can't capture leads online

**Pipeline Flow**:
- scraper.py: Search business directories, Google Maps, LinkedIn for prospects matching città/settore
- qualifier.py: Filter by business size, revenue signals, online absence confirmation
- contact_finder.py: Extract email, phone, SMS contact (multi-channel extraction)
- message_generator.py: Create personalized outreach highlighting "you have traffic but no way to capture it"

**Output**: Email sequences targeting no-website businesses

### 2. **cro-funnel/** Agent
**Problem Solved**: Businesses with traffic but low conversions are leaving money on table

**Pipeline Flow**:
- scraper.py: Fetch website content, meta tags, page structure, analytics signals (proxy)
- site_analyzer.py: Full CRO audit across messaging, trust signals, UX friction, CTA clarity
- market_runner.py: Competitive benchmarking (scrape competitor sites, compare conversion elements)
- pdf_generator.py: Create professional audit PDF (branded, visual, actionable recommendations)
- email_composer.py: Draft email with audit PDF attachment + CTA for "Conversion Sprint" project

**Output**: Audit PDFs + email sequences with audit attached

### 3. **ai-implementation/** Agent
**Problem Solved**: Businesses don't know where/how AI can improve operations

**Pipeline Flow**:
- scraper.py: Research company website, product/service, current processes
- ai_scorer.py: Score business model against AI implementation opportunities (customer service, content generation, lead qualification, forecasting, etc.)
- proposal_generator.py: Generate AI implementation proposal with specific use cases, ROI estimation, 3-month implementation plan

**Output**: Custom AI implementation proposals

## 💻 /market Command Suite (18 Total Commands)

These are implemented as aliases/shortcuts that map to the agent orchestrator:

| Command | Type | Purpose | Output |
|---------|------|---------|--------|
| `/market audit <url>` | Full Audit | Complete marketing audit with 5 parallel agents | Markdown report |
| `/market quick <url>` | Snapshot | 60-second marketing snapshot (fast version) | Quick summary |
| `/market copy <url>` | Copy Analysis | Extract and optimize site copy | Before/after copy comparison |
| `/market emails <topic>` | Content Generation | Generate complete email sequences | Email templates |
| `/market social <topic>` | Content Calendar | 30-day social media content calendar | Posting schedule |
| `/market ads <url>` | Ad Creatives | Ad copy and creative for all platforms | Ad variations |
| `/market funnel <url>` | Funnel Analysis | Sales funnel analysis and optimization | Funnel diagram + recommendations |
| `/market competitors <url>` | Competitive Intel | Competitive intelligence report | Competitor comparison |
| `/market landing <url>` | CRO Analysis | Landing page CRO analysis | Optimization checklist |
| `/market launch <product>` | Playbook | Product launch playbook | Timeline + checklist |
| `/market proposal <client>` | Proposal Gen | Client proposal generator | Proposal document |
| `/market report <url>` | Markdown Report | Full marketing report (Markdown) | Complete markdown report |
| `/market report-pdf <url>` | PDF Report | Professional marketing report (PDF) | Branded PDF report |
| `/market seo <url>` | SEO Audit | SEO content audit | SEO recommendations |
| `/market brand <url>` | Brand Analysis | Brand voice analysis and guidelines | Brand voice guide |

## 🔄 Pipeline Dependencies & Sequencing

When running `--pipeline full`, the orchestrator executes in this order:
1. **no-website pipeline** (fastest, discovery stage)
2. **cro-funnel pipeline** (medium, analysis stage)
3. **ai-implementation pipeline** (longest, proposal generation)

Cross-pipeline data sharing:
- Prospect list from `no-website` feeds into `cro-funnel` (filter: if business has website, schedule for CRO audit)
- Prospect list from `cro-funnel` feeds into `ai-implementation` (augment prospect profile with conversion data)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- .env file with API keys (OpenAI, Stripe, Google Search, etc.)

### Installation Steps
```bash
# Install dependencies
pip install -r Agency/requirements.txt

# Setup environment
cp Agency/.env.example Agency/.env
# Edit .env with your API keys

# Test installation
python Agency/orchestrator/run.py --help
```

## 📈 Metrics & Success Criteria

- **Prospect Discovery Rate**: X prospects found per città/settore (target: 50-500 per execution)
- **Outreach Quality**: % of generated emails/proposals that result in response (target: 10%+ response rate)
- **Pipeline Execution Time**: Full sequence completes in under 2 hours (target: <120 min)
- **Report Quality**: % of audit PDFs resulting in client interest (target: 15%+ conversion to consultation)

## 🔗 Related Pages

- [[Digital_Empire_Agency_Strategy]] — Core agency positioning and service offerings
- [[Concept_Conversion_Rate_Optimization]] — Methodology behind cro-funnel agent
- [[Funnel_Optimization_Framework]] — Detailed funnel analysis framework
-  — AI opportunities and positioning
-  — Technical stack for agent development
- [[Outreach_Automation_Agent_System]] — Legacy outreach components
-  — Comparison of automated vs manual approaches

## 📝 Metadata

- **Date Created**: 2026-03-09
- **Last Updated**: 2026-03-09
- **Status**: Development phase, documented architecture
- **Complexity**: High (3 agents, 18 commands, multi-modal outreach)
- **Maintenance Owner**: Development team
- **Next Checkpoint**: Agent test execution and command validation
