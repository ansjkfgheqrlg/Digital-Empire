---
Type: TOOL
Status: Active
Tags: #marketing #architecture #system-prompt #tool #ai-engineering
Created: 2026-04-29
Last updated: 2026-04-29
Purpose: Strategic marketing blueprint generation and architecture engine
---

## Marketing Project Architect v4.0

### Overview
Marketing Project Architect (MPA) is a strategic logic engine designed for compiling marketing variables into executable blueprints. It's a system prompt tool engineered for Claude, GPT-4o, and similar advanced LLMs.

### Tool Purpose
Transform marketing project specifications into:
- Actionable marketing architecture blueprints
- Multi-channel funnel strategies
- Content production workflows
- Executable implementation plans with metrics
- Risk mitigation and scaling frameworks

### Key Features
1. **Strategic Logic Engine** - Processes 5+ core variables through decision routing
2. **Multi-Strategy Support** - 12+ distinct strategic pathways based on:
   - Audience awareness level (5 tiers: Unaware → Most Aware)
   - Price points (Low, Mid, High, Premium)
   - Business models (Service, Product, SaaS, Info-Product, Agency, Local)
   - Growth stages (Launch, Traction, Scale, Optimization)

3. **Modular Command System**:
   - `/full` - Complete blueprint
   - `/funnel` - Funnel architecture only
   - `/hooks [n]` - Generate n conversion hooks
   - `/content` - Content system only
   - `/audit [url/text]` - Audit existing material
   - `/refine [section]` - Regenerate specific sections

4. **Quality Gates** - Built-in validation for:
   - Specificity enforcement
   - Metadata completeness
   - Actionable output verification

### Required Core Variables
| # | Variable | Format |
|---|----------|--------|
| 1 | PROJECT_TYPE | Funnel, Content System, Launch, Ads, Hybrid |
| 2 | NICHE | Industry + specific sub-sector |
| 3 | TARGET_AUDIENCE | Demographics + Psychographics + Current State |
| 4 | GOAL | Specific metric (e.g., 50 Leads/mo, $10k Revenue) |
| 5 | PLATFORM | Primary channel (LinkedIn, IG, Email, TikTok, etc.) |

**Optional Variables**: BUDGET, TIMELINE, PRICE_POINT, EXISTING_ASSETS, AWARENESS_LEVEL, TOP_COMPETITOR, BUSINESS_MODEL

### Output Structure (7 Sections)
1. **Project Overview** - Type, objective, thesis, differentiation, North Star metric
2. **Target Audience Analysis** - Psychological profile, pain/desire matrix, objections
3. **Offer Architecture** - Core offer, pricing, value equation, guarantees
4. **Funnel Architecture** - Stage-by-stage breakdown with conversion mechanics
5. **Content System** - Pillars, hooks, production workflow
6. **Execution Plan** - Sprint-based implementation timeline
7. **Optimization & Scaling** - Metrics dashboard and scaling triggers

### Technical Specifications
- **Compatibility**: Claude 3.5+, GPT-4o, Gemini 1.5 Pro
- **Language**: Italian or English (matches user)
- **Output Format**: Markdown with tables, code blocks, callouts
- **Token Optimization**: 30-40% reduction vs. v3.0 while maintaining behavioral precision

### Behavioral Rules
- NO FILLER - Direct architectural output only
- SPECIFICITY ENFORCEMENT - All metrics must be quantified
- MARKDOWN STRICTNESS - Tables for comparisons, code blocks for workflows
- LOGIC TRANSPARENCY - Reasoning shown in thinking blocks
- ERROR HANDLING - Ambiguous inputs trigger multiple strategic paths for user selection

### Modern Marketing Architectures Supported
- Short-form video funnels (TikTok/Reels → DM → Sale)
- Community-led growth (Free community → Paid tier)
- AI-assisted content workflows
- Conversational commerce (WhatsApp/DM automation)
- Signal-based outbound (intent data → personalized outreach)

### Unit Economics Mini-Section
- CAC (Customer Acquisition Cost) target
- LTV (Lifetime Value) estimate
- LTV:CAC ratio target
- Payback period

### Banned Phrases List (15+)
The tool explicitly avoids vague marketing language:
- "Engage with your audience"
- "Drive results"
- "Boost your presence"
- "Take your X to the next level"
- And 11+ others requiring specific, measurable language

### Related Tools & Concepts
[[Content System Architecture]]
[[Concept_Sales_Funnel_Design]]
[[Audience Analysis Framework]]
[[Marketing Metrics Dashboard]]
[[Tool_Market_Competitive_Intelligence]]

### Version History
- **v3.0.1** - Original system prompt (March 2026)
- **v4.0** - Complete rewrite with:
  - Expanded strategy routing (4 → 12+ paths)
  - Competitive analysis integration
  - Testing framework addition
  - Multi-audience support
  - Data completeness index
  - Modern architecture support

---
**Source**: `c:\Users\Utente\Desktop\qui tutto\Digital Empire\prove\System.md`
**Classification**: System prompt, AI Engineering Tool, Marketing Architecture
