- **Type**: TOOL
- **Status**: Active
- **Tags**: `#automation` `#outreach` `#sales` `#lead-generation` `#workflow`
- **Created**: 2026-04-29
- **Last updated**: 2026-04-29

## Overview

The Outreach Automation Agent System is a complete lead generation and prospecting automation platform for Digital Empire. It automates the entire client acquisition cycle: finding prospects, qualifying leads, generating personalized outreach, sending emails, and tracking engagement.

## Purpose

This system coordinates 7 active workflows (WF-A through WF-F plus WF-D2) to:
- Find businesses without websites (CRO/Copy/Funnel opportunity)
- Find businesses with poor ad funnels (CRO/Copy/Funnel opportunity)
- Find companies with manual processes suitable for AI implementation
- Qualify leads and score them by fit and readiness
- Generate personalized email outreach
- Send and track email campaigns
- Monitor prospect engagement and nurture sequences

## Service Lines

### Service 1: CRO / Copy / Funnel Strategy
For local businesses and SMEs with online presence or conversion issues:
- Website creation and high-conversion landing pages
- Persuasive copywriting for ads, email, sales pages
- Funnel strategy: complete purchase journey design
- CRO optimization on existing funnels

Target: WF-A (No Website), WF-B (Poor Ad Funnels)

### Service 2: AI Implementation & Custom Agents
For structured companies (10+ employees) with manual, repeatable processes:
- Analysis of SOPs for AI intervention opportunities
- Design and development of custom AI agents
- Process automation: back office, customer service, data entry, reporting
- AI integration into existing workflows

Target: WF-F (AI Implementation Prospects)

## Active Workflows

| ID | Name | Trigger | Script | Service | Rules |
|----|------|---------|--------|---------|-------|
| WF-A | Search No Website | Manual / Weekly | search_no_website.py | CRO/Copy/Funnel | 01_ricerca_no_sito.md |
| WF-B | Search Poor Ads Funnels | Manual / Weekly | search_ads_leads.py | CRO/Copy/Funnel | 02_ricerca_ads_funnel_scarsi.md |
| WF-C | Qualify & Score Leads | Post WF-A, WF-B, WF-F | qualify_leads.py | Both | 03_qualifica_lead.md |
| WF-D | Draft Email Outreach | Manual on qualified | draft_emails.py | Both | 04_drafta_email.md |
| WF-D2 | Send Approved Email | Manual after review | send_emails.py | Both | 04b_invia_email.md |
| WF-E | Track Outreach | Manual / Event-driven | track_outreach.py | Both | 05_traccia_outreach.md |
| WF-F | Search AI Prospects | Manual / Weekly | search_ai_prospects.py | AI Implementation | 06_ricerca_ai_prospects.md |

## Key Components

### WF-A: Business Without Website Discovery
- Searches Google Maps for local businesses in specific categories
- Filters for businesses without active websites
- Extracts contact information (phone, email)
- Calculates priority score based on Google rating, review count, category
- Output: New lead rows in Google Sheets with priority scoring

### WF-B: Poor Ad Funnel Detection
- Identifies businesses running Facebook/Google ads
- Analyzes landing page conversion efficiency
- Scores funnel health (CTA clarity, friction, social proof, trust signals)
- Prioritizes based on ad spend visibility and low conversion indicators
- Output: High-potential CRO service opportunities

### WF-C: Lead Qualification & Scoring
- Analyzes lead data for service fit
- Scores qualification criteria: company size, industry, budget indicators
- Assigns to Service 1 or Service 2 based on characteristics
- Estimates revenue potential per lead
- Weights by probability of closure
- Output: Ranked and segmented lead list

### WF-D: Email Draft Generation
- Retrieves qualified leads from scoring step
- Generates personalized email copy using Claude
- Customizes by service line (CRO vs AI Implementation)
- Creates subject lines and body copy
- Saves as drafts for human review before sending
- No automatic sending (human approval gate)

### WF-D2: Email Sending
- Sends approved emails via Gmail SMTP
- Uses app-specific password (not account password)
- Logs sent timestamps and delivery status
- Updates prospect status in tracking sheet
- Output: Sent email log with delivery confirmation

### WF-E: Outreach Tracking
- Monitors email open rates and click tracking
- Logs follow-up actions and response tracking
- Updates prospect status as pipeline progresses
- Creates engagement timeline per prospect
- Triggers follow-up sequences based on engagement
- Output: Updated tracking sheet with engagement metrics

### WF-F: AI Implementation Prospect Search
- Identifies companies with 10+ employees
- Analyzes for manual, repeatable processes
- Searches for common automation opportunities:
  - Data entry and back office
  - Customer service and support
  - Report generation and analytics
  - Repetitive communication tasks
- Estimates AI implementation revenue potential
- Output: AI Implementation qualified leads

## Technical Architecture

### Script Organization
```
agente-outreach/
├── CLAUDE.md (system specification)
├── .env (credentials - never commit)
├── requirements.txt
├── rules/ (7 workflow specifications)
├── implementation/ (7 Python scripts)
├── logs/ (automatic logging)
└── tests/ (unit tests for core functions)
```

### API Integrations
- **Apify**: Google Maps and Facebook Ad Library scraping (pay-per-use)
- **Anthropic Claude**: Personalized email generation via API (pay-per-use)
- **Gmail SMTP**: Email sending (free, app password required)
- **Google Sheets**: Optional data storage (free tier sufficient)

### Rate Limiting & Resilience
- Apify timeout: 300 seconds, retry 3x with exponential backoff (2s, 4s, 8s)
- Landing page analysis: 3-second pause between sites
- Claude API: max 20 emails per run
- All scripts include try/except error handling and detailed logging

## Qualification Criteria

### Service 1 (CRO/Copy/Funnel) - Qualification Weights
- No website or broken website: 40 points
- Running ads with poor conversion: 35 points
- Small business (1-10 employees): 10 points
- Local business category: 15 points
- Rating 3.5+ with engagement: 10 points
- Score 60+ = qualified lead

### Service 2 (AI Implementation) - Qualification Weights
- Company size 10+ employees: 30 points
- Visible manual processes: 40 points
- Multiple departments/functions: 15 points
- Tech-forward indicators (LinkedIn presence, job postings): 15 points
- Score 60+ = qualified lead

## Output Format

### Lead Data Structure
```
ID_LEAD: NS-MI-20250115143022
NOME_BUSINESS: Idraulico Rossi
CATEGORIA: Idraulico
INDIRIZZO: Via Roma 12, Milano
TELEFONO: +39 02 1234567
EMAIL: info@idraulico-rossi.it
RATING: 4.2
N_RECENSIONI: 47
SCORE_PRIORITÀ: 78
STATO_OUTREACH: nuovo | qualificato | bozza_email | email_inviata | contattato | conversione
```

### Email Draft Format
Subject line, body copy in plain text and HTML, personalization variables, tracking links

## How It Applies to Digital Empire

The Outreach Automation System is the core business development engine:
- **Automated lead generation** for both service lines
- **Qualification and prioritization** to focus sales effort
- **Personalized outreach at scale** reducing manual work
- **Pipeline tracking** for revenue forecasting
- **Continuous lead flow** maintaining consistent sales pipeline

## Related Resources

- [[Concept_Lead_Qualification_Methodology]]
- [[Concept_Email_Outreach_Strategy]]
- [[Project_Outreach_Automation_Implementation]]
- [[Tool_Market_AI_Suite]]
