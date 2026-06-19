# Tool: Outreach Automation Agent System

- **Type**: 🤖 Automation Agent / 📧 Lead Generation & Prospecting System
- **Purpose**: Automated end-to-end client acquisition pipeline for two service lines
- **Status**: 🟢 Active (7 workflows operational)
- **Language**: Italian (operations + documentation)
- **Integrations**: Apify (scraping), Anthropic API (email generation), Gmail SMTP
- **Tags**: `#automation` `#lead-generation` `#outreach` `#prospecting` `#email-automation` `#python`

---

## 📖 System Overview

The Outreach Automation Agent is a Python-based system that automates the entire client acquisition cycle for Digital Empire:

1. **Discovery**: Find prospects matching two service profiles
2. **Qualification**: Score and prioritize leads
3. **Outreach**: Generate and send personalized email campaigns
4. **Tracking**: Monitor pipeline status and engagement

**Key Design**: Human approval required for all email sending (always drafted, never auto-sent).

---

## 🎯 Service Lines (What We Sell)

### Service Line 1: CRO / Copy / Funnel Strategy
**Target**: Local businesses and SMBs with online/conversion problems

**Solutions**:
- High-conversion website and landing page design
- Persuasive copywriting (ads, email, sales pages)
- Funnel strategy: complete customer journey design
- CRO (Conversion Rate Optimization) on existing funnels

**Ideal Prospect Profile**:
- Local business without web presence
- Business running ads but with poor funnel conversion
- SaaS/online business wanting to improve sales process

### Service Line 2: AI Implementation & Custom Agents
**Target**: Structured companies (10+ employees) with manual, repetitive processes

**Solutions**:
- Analyze company SOPs to identify AI opportunities
- Design and develop custom AI agents
- Process automation: back office, customer service, data entry, reporting
- AI integration into existing workflows

**Ideal Prospect Profile**:
- 10+ employee company with revenue >€500k
- Manual, repetitive processes (high automation potential)
- Openness to AI as cost-reduction/efficiency lever

---

## 🔄 Seven Active Workflows (WF-A through WF-F)

### WF-A: "Ricerca Business Senza Sito" (No-Website Discovery)
**Purpose**: Find local businesses without web presence

**Trigger**: Manual or weekly schedule
**Script**: `search_no_website.py`
**Rule**: `rules/01_ricerca_no_sito.md`
**Service**: CRO/Copy/Funnel
**Data Sources**: Google Maps, Facebook, directory listings
**Output**: Lead list with contact info
**Qualification Target**: Medium-high (any business without site = opportunity)

### WF-B: "Ricerca Ads con Funnel Scarsi" (Poor-Funnel Ads Discovery)
**Purpose**: Find businesses running ads but with poor conversion

**Trigger**: Manual or weekly schedule
**Script**: `search_ads_leads.py`
**Rule**: `rules/02_ricerca_ads_funnel_scarsi.md`
**Service**: CRO/Copy/Funnel
**Data Sources**: Facebook Ad Library, LinkedIn Ads Library, website audit proxies
**Output**: Qualified lead list with conversion estimates
**Qualification Target**: High (poor conversion is explicit problem worth solving)

### WF-C: "Qualifica e Scoring Lead" (Lead Qualification & Scoring)
**Purpose**: Grade leads by likelihood and urgency

**Trigger**: Post WF-A, WF-B, or WF-F
**Script**: `qualify_leads.py`
**Rule**: `rules/03_qualifica_lead.md`
**Service**: Both
**Scoring Factors**:
- Budget capacity (company revenue, growth trajectory)
- Problem severity (how costly is their current problem?)
- Urgency signals (hiring growth, seasonal patterns)
- Contact accessibility (direct decision-maker vs gatekeeper)

**Output**: Scored lead list with recommended approach (warm, cool, hot)

### WF-D: "Drafta Email Outreach" (Email Generation)
**Purpose**: Create personalized outreach email for qualified leads

**Trigger**: Manual on selected qualified leads
**Script**: `draft_emails.py`
**Rule**: `rules/04_drafta_email.md`
**Service**: Both
**Process**:
- Pulls lead profile + score
- Requests Claude API to generate personalized email based on pain points
- Considers service line (CRO vs AI implementation)
- Drafts email with subject line, body, and CTA
- Saves draft to folder for human review

**Email Strategy**:
- Subject: Personalized to their specific pain point
- Hook: Reference something specific to their business
- Body: Pain agitation → solution offer → CTA (soft)
- CTA: Calendar link, demo link, or 15-min discovery call offer

**Max Rate Limit**: 20 emails generated per run (API budget protection)

### WF-D2: "Invia Email Approvata" (Approved Email Sending)
**Purpose**: Send drafted email only after human approval

**Trigger**: Manual (after human reviews WF-D draft)
**Script**: `send_emails.py`
**Rule**: `rules/04b_invia_email.md`
**Service**: Both
**Integration**: Gmail SMTP using app-specific password (not account password)
**Safety Checks**:
- Verify email approved by human
- Log send timestamp and recipient
- Store copy in logs for compliance

---

### WF-E: "Traccia Outreach" (Outreach Tracking)
**Purpose**: Monitor pipeline status and engagement

**Trigger**: Manual or event-driven
**Script**: `track_outreach.py`
**Rule**: `rules/05_traccia_outreach.md`
**Service**: Both
**Tracking Metrics**:
- Email sent (timestamp)
- Email opened (if tracking enabled)
- Link clicks (if UTM parameters used)
- Reply received (yes/no)
- Qualified meeting booked (yes/no)
- Deal stage (lead → meeting → proposal → closed)

**Output**: Pipeline dashboard (CSV or Google Sheets)

### WF-F: "Ricerca Prospect AI Implementation" (AI Implementation Targeting)
**Purpose**: Find companies with manual processes ready for AI automation

**Trigger**: Manual or weekly schedule
**Script**: `search_ai_prospects.py`
**Rule**: `rules/06_ricerca_ai_prospects.md`
**Service**: AI Implementation
**Targeting Criteria**:
- Company size: 10+ employees (complex enough for custom agents)
- Revenue: >€500k (budget for automation investment)
- Industry signals: Customer service, data entry, reporting, back office, logistics
- Growth signals: Recent hiring, expansion, new department

**Data Sources**: LinkedIn company research, industry databases, news mentions
**Output**: Prospect list with AI opportunity score

---

## 📊 Workflow Sequence & Data Flow

```
WF-A (No-website discovery)  ─┐
                             ├─→ WF-C (Qualification & scoring)
WF-B (Ads funnel discovery)  ─┤                    │
                             │                    ↓
                             │         Lead ranked by priority
                             │                    │
WF-F (AI prospects) ──────────────────────────────┘
                                                  │
                                                  ↓
                              WF-D (Draft personalized email)
                                                  │
                              [HUMAN REVIEW & APPROVAL]
                                                  │
                                                  ↓
                              WF-D2 (Send approved email)
                                                  │
                                                  ↓
                              WF-E (Track engagement & pipeline)
```

---

## 🔐 Safety & Compliance Rules

### No Auto-Sending
- Every email drafted by WF-D is **reviewed by human before sending**
- Human must explicitly approve in WF-D2 before SMTP send
- All drafts logged with approval timestamp
- GDPR-compliant (explicit opt-in opportunity in initial email)

### Error Handling (Self-Healing)
- All scripts handle errors with try/except
- API failures: retry 3x with exponential backoff (2s, 4s, 8s)
- Fatal errors: log to `logs/errors.log` and exit code 1
- Never overwrite existing data without backup

### Security
- All credentials: `.env` file (never hardcoded)
- `.env` in `.gitignore` (never committed)
- Gmail: app-specific password (not account password)
- API tokens: rotated regularly
- GDPR compliance: lead data handled according to regulations

---

## 🛠️ Technical Architecture

### Technology Stack
- **Language**: Python 3.9+
- **APIs**: Apify (scraping), Anthropic (email generation), Gmail SMTP
- **Data Storage**: Local CSV + optional Google Sheets
- **Logging**: File-based to `logs/` directory
- **Execution**: Manual CLI + optional cron schedule (weekly)

### File Structure
```
agente-outreach/
├── CLAUDE.md                   (This config file)
├── .env                        (Credentials — not committed)
├── requirements.txt            (Python dependencies)
├── rules/                      (Workflow documentation)
│   ├── 01_ricerca_no_sito.md
│   ├── 02_ricerca_ads_funnel_scarsi.md
│   ├── 03_qualifica_lead.md
│   ├── 04_drafta_email.md
│   ├── 04b_invia_email.md
│   ├── 05_traccia_outreach.md
│   └── 06_ricerca_ai_prospects.md
├── implementation/             (Python scripts)
│   ├── search_no_website.py
│   ├── search_ads_leads.py
│   ├── search_ai_prospects.py
│   ├── qualify_leads.py
│   ├── draft_emails.py
│   ├── send_emails.py
│   ├── track_outreach.py
│   └── utils/
│       ├── website_checker.py
│       ├── contact_extractor.py
│       ├── sheets_client.py
│       └── logger.py
└── logs/                       (Automatically created logs)
    ├── 2026-04-29_WF-A_discovery_milan.log
    ├── errors.log
    └── [...]
```

---

## 📈 Performance Targets

- **Discovery Rate**: 50-500 prospects per city/sector
- **Qualification Accuracy**: 70%+ of qualified leads = actual opportunities
- **Email-to-Reply Rate**: 5-15% (cold outreach standard)
- **Reply-to-Meeting Rate**: 20-40% of replies
- **Meeting-to-Proposal Rate**: 30-50%
- **Proposal-to-Close Rate**: 20-30%

---

## 🔄 Usage (Command Line)

```bash
# Activate venv
source venv/bin/activate

# Install dependencies (first time)
pip install -r requirements.txt

# Run discovery workflows
python implementation/search_no_website.py --city "Milano" --sector "ristoranti"
python implementation/search_ads_leads.py --city "Roma" --sector "dentisti"
python implementation/search_ai_prospects.py --city "Napoli"

# Qualify and score
python implementation/qualify_leads.py --input leads_raw.csv --output leads_qualified.csv

# Draft emails for hot leads
python implementation/draft_emails.py --lead-ids "NS-MI-001,AF-RM-002"

# Send approved emails (after human review)
python implementation/send_emails.py --approved-drafts drafts_approved.csv

# Track pipeline
python implementation/track_outreach.py --output pipeline_dashboard.csv
```

---

## 🔗 Related Pages

- [[Agency_Agent_Orchestration_System]] — Broader agent system
- [[Digital_Empire_Agency_Strategy]] — Core service lines
- [[Concept_Email_Outreach_Strategy]] — Email strategy methodology
- [[Funnel_Optimization_Framework]] — Scoring criteria
-  — Tracking and measurement

---

## 📝 Metadata

- **Created**: Internal automation infrastructure
- **Status**: 7/7 workflows operational
- **Languages**: Italian (operations), Italian (code comments)
- **Maintenance Owner**: Engineering team
- **Next Optimization**: Integration with CRM for real-time pipeline tracking
