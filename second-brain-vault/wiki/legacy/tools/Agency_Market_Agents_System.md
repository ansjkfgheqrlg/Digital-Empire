# Tool: Agency Market Agents System (5 Specialized Agents)

- **Type**: 🤖 Agent System / 🔧 Analysis Framework
- **Purpose**: Parallel agent architecture for comprehensive website/marketing audits
- **Status**: 🟢 Active
- **Deployment**: Python agents launched via orchestrator CLI
- **Tags**: `#agents` `#automation` `#marketing-audit` `#cro` `#competitive-analysis`

---

## 📖 System Overview

The Agency Market Agents System is a 5-agent parallel architecture for conducting comprehensive website marketing audits. Each agent specializes in analyzing one critical dimension of marketing effectiveness. Agents run in parallel for speed; results are aggregated into comprehensive audit reports.

**Core Design**: Divide-and-conquer specialization. Each agent is deep-expert in its domain; orchestrator coordinates parallel execution; outputs combine into 51/100-style overall scoring.

---

## 🔧 The 5 Specialized Agents

### 1. **Market-Competitive Agent** 
**Specialization**: Competitive positioning and market landscape analysis

**Key Responsibilities**:
- Identify 3-5 key competitors (direct + aspirational)
- Extract target website positioning statement, audience, differentiators, pricing, social proof
- Quick-scan competitors' positioning, pricing, features, content strategy
- Score target on: positioning clarity, pricing competitiveness, feature messaging, market awareness, content authority
- Identify positioning gaps, content gaps, feature gaps
- Recommend comparison pages, switching narratives, alternative landing pages

**Output Dimensions Scored**:
- Positioning Clarity (0-10): Can visitor distinguish from competitors in 10 seconds?
- Pricing Competitiveness (0-10): Is pricing transparent and competitive?
- Feature Messaging (0-10): Are differentiating features highlighted?
- Market Awareness (0-10): Do they acknowledge competitors? Any comparison pages?
- Content Authority (0-10): Are they thought leader or just product page?

**Key Deliverables**:
- Competitor comparison table (Target vs 3 competitors)
- Positioning scoring on 5 dimensions
- 3-5 actionable positioning opportunities
- Recommended new pages: "[Competitor] vs [Target]", "[Competitor] Alternative"

---

### 2. **Market-Content Agent**
**Specialization**: Copy quality, messaging effectiveness, persuasion strength

**Key Responsibilities**:
- Fetch and analyze key pages: homepage, about, pricing, 1 feature/product page, 1 blog post
- Score content on: headline clarity, value proposition strength, copy persuasion, content depth, CTA effectiveness
- Identify specific wins and critical fixes for each page
- Generate before/after copy rewrites for top 3 issues
- Assess how well copy uses benefits vs features, customer language vs jargon, emotional + logical proof

**Output Dimensions Scored**:
- Headline Clarity (0-10): Is it specific, not generic? Does visitor understand value in 5 seconds?
- Value Proposition Strength (0-10): Is it differentiated, proven, specific?
- Copy Persuasion (0-10): Benefits > features? Customer language? Addresses objections?
- Content Depth (0-10): Enough to inform purchase? Features explained with outcomes? Educational content present?
- CTA Effectiveness (0-10): Clear, specific, action-oriented? Value-driven text? Multiple placements? Primary vs secondary?

**Key Deliverables**:
- Dimension scoring on 5 content/messaging elements
- Top 3-5 specific wins with quotes
- Critical fixes with specific rewrite suggestions
- Before/after copy examples for top 3 issues
- Missing element checklist

---

### 3. **Market-Conversion Agent**
**Specialization**: Conversion optimization, friction reduction, funnel analysis

**Key Responsibilities**:
- Analyze conversion funnel: form fields, CTA buttons, payment flow, checkout friction
- Score on: form friction (field count, required fields), CTA clarity and placement, social proof strength, trust signals
- Identify abandonment points and psychological blockers
- Recommend: form simplification, CTA multiplication, guarantee/risk reversal additions, scarcity/urgency elements
- Assess pricing architecture, upsell opportunities, downsell recovery flows

**Output Dimensions Scored**:
- Form Friction (0-10): How many fields? Required vs optional? Single vs multi-step?
- CTA Design (0-10): Specific language or generic? Clear value? Multiple placements? Color contrast?
- Social Proof Quality (0-10): Testimonials with results? Customer logos? Specific numbers?
- Trust Signals (0-10): Guarantee visible? Privacy messaging? Contact info? Security badges?
- Pricing Clarity (0-10): Is pricing transparent? Money-back guarantee? Payment options?

**Key Deliverables**:
- Funnel analysis with identified friction points
- Form field audit with recommendations
- CTA placement audit with multiplication strategy
- Social proof assessment + testimonial template
- Pricing optimization recommendations
- Estimated revenue impact of quick wins (+15-25% CVR type estimates)

---

### 4. **Market-Technical Agent**
**Specialization**: Technical SEO, site speed, mobile experience, page structure

**Key Responsibilities**:
- Audit technical foundations: page speed (Lighthouse), mobile responsiveness, Core Web Vitals
- Analyze site structure: heading hierarchy, semantic HTML, schema markup, internal linking
- Check SEO health: meta tags, robot.txt, sitemap.xml, structured data implementation
- Assess accessibility: color contrast, ARIA labels, keyboard navigation, screen reader compatibility
- Identify mobile-specific issues and crawlability problems

**Output Dimensions Scored**:
- Page Speed (0-10): Lighthouse score interpretation, Core Web Vitals status
- Mobile Experience (0-10): Responsive design, touch target sizing, viewport configuration
- On-Page SEO (0-10): Meta tags, heading structure, schema implementation, internal links
- Accessibility (0-10): WCAG 2.1 AA compliance level, contrast ratios, ARIA presence
- Site Architecture (0-10): Crawlability, XML sitemap, robots.txt, structured data

**Key Deliverables**:
- Lighthouse audit results summary
- Mobile compatibility checklist
- Schema markup audit (missing Product, FAQ, Article, etc.)
- Top 5 technical quick wins
- Core Web Vitals status and optimization priorities

---

### 5. **Market-Strategy Agent**
**Specialization**: Brand & trust evaluation, growth strategy, revenue opportunity identification

**Key Responsibilities**:
- Assess brand consistency across pages (visual, messaging, voice)
- Evaluate trust architecture: about page quality, contact info, social proof, certifications
- Score authority signals: thought leadership, press mentions, awards, community presence
- Analyze pricing strategy fit: transparency, free/trial options, tiering structure
- Map acquisition channels: content marketing, SEO maturity, social presence, paid ads, partnerships
- Identify retention/expansion paths: onboarding, community, upgrade paths, help center quality
- Estimate revenue opportunities across quick wins (1-2 weeks), medium-term (1-3 months), strategic (3-6 months)

**Output Dimensions Scored**:
- Brand Consistency (0-10): Visual + messaging consistency, design quality, brand mark presence
- Trust Architecture (0-10): About page, contact info, social proof, privacy/security messaging
- Authority Signals (0-10): Thought leadership, media mentions, awards, community presence
- Pricing Strategy (0-10): Transparency, free/trial, tiering, metric alignment, upsell paths
- Acquisition Channels (0-10): Diversification and maturity across channels
- Retention & Expansion (0-10): Onboarding, community, upgrade paths, help center quality

**Key Deliverables**:
- Brand & Trust score + dimension breakdown
- Growth & Strategy score + dimension breakdown
- Revenue opportunity matrix (Quick Wins / Medium / Strategic with effort/impact estimates)
- Pricing analysis with recommendations
- Channel strategy with recommendations for next channel
- 12-month revenue projection scenarios

---

## 🔄 Execution Model: Parallel Orchestration

### Default Audit Flow (`/market audit <url>`)
```
INPUT: URL
  │
  ├─► [PARALLEL] market-competitive.md
  ├─► [PARALLEL] market-content.md
  ├─► [PARALLEL] market-conversion.md
  ├─► [PARALLEL] market-technical.md
  └─► [PARALLEL] market-strategy.md
        │
        └─► AGGREGATE → Overall Score (51/100 style)
              └─► Generate PDF report with all 5 agent outputs
```

### Output: Comprehensive Audit Report
- **Overall Score**: Weighted average of 5 agents + category breakdown
- **Executive Summary**: 3 critical gaps, 3 quick wins, revenue projection
- **Detailed Findings**: Full agent outputs with scoring tables, specific recommendations
- **Action Plan**: Prioritized checklist of recommended changes (effort/impact)
- **Revenue Impact**: Conservative estimates for each recommendation

---

## 📊 Score Aggregation Model

Each agent returns 5 dimension scores (0-10). Aggregation follows pattern used in marketing audits:

```
Content & Messaging       (Agent: market-content)      — 25% weight
Conversion Optimization   (Agent: market-conversion)   — 20% weight
SEO & Discoverability     (Agent: market-technical)    — 20% weight
Competitive Positioning   (Agent: market-competitive)  — 15% weight
Brand & Trust             (Agent: market-strategy)     — 10% weight
Growth & Strategy         (Agent: market-strategy)     — 10% weight

TOTAL = 51/100 possible (where 51 = Grade D, below average)
```

---

## 🛠️ Agent Implementation Details

### Agent Input/Output Contract

**Input to each agent**:
```json
{
  "target_url": "https://example.com",
  "fetch_pages": ["homepage", "about", "pricing", "blog_sample"],
  "search_competitors": true,
  "analysis_depth": "full"
}
```

**Output from each agent**:
```json
{
  "agent_name": "market-content",
  "overall_score": 58,
  "dimensions": {
    "headline_clarity": 7,
    "value_proposition": 6,
    "copy_persuasion": 5,
    "content_depth": 5,
    "cta_effectiveness": 4
  },
  "key_findings": [...],
  "recommendations": [
    {"priority": "high", "effort": "low", "impact": "25%", "description": "..."}
  ],
  "execution_time_seconds": 42
}
```

### Technology Stack
- **WebFetch**: Retrieve page content from target URLs
- **WebSearch**: Identify competitors, find market context
- **Python agents**: Custom analysis logic per dimension
- **PDF generation**: Combine outputs into branded audit report
- **CSV export**: Lead lists and opportunity tracking

---

## 📈 Benchmark Scores (Italian Market)

For comparison purposes, average scores in Italian market segments:

| Market Segment | Content | Conversion | SEO | Competitive | Brand | Growth | Overall |
|---|---|---|---|---|---|---|---|
| Info Products (Creator) | 58/100 | 54/100 | 38/100 | 52/100 | 42/100 | 58/100 | 51/100 |
| SaaS (B2B) | 62/100 | 68/100 | 71/100 | 58/100 | 65/100 | 72/100 | 65/100 |
| Ecommerce | 65/100 | 71/100 | 42/100 | 48/100 | 58/100 | 62/100 | 59/100 |
| Agency Service | 59/100 | 61/100 | 55/100 | 54/100 | 61/100 | 58/100 | 58/100 |

**Note**: "Info Products (Creator)" row based on Andrei Copy audit (51/100 baseline).

---

## 💼 Use Cases in Digital Empire Operations

1. **Lead Qualification**: Run `/market audit <url>` on prospects to identify high-potential CRO opportunities
2. **Competitive Research**: Use market-competitive agent output for positioning strategy
3. **Content Benchmarking**: Compare client websites against market averages on content dimension
4. **Pre-Proposal Research**: Use full audit to inform Conversion Sprint proposal and positioning
5. **Retainer Quarterly Checks**: Re-run audit quarterly to track improvement progress

---

## 🔗 Related Pages

- [[Agency_Agent_Orchestration_System]] — How agents are orchestrated
- [[Marketing_Audit_Andrei_Copy_Case_Study]] — Example of full 5-agent audit output
- [[Concept_Conversion_Rate_Optimization]] — Methodology behind conversion agent
- [[Tool_Market_Strategy_Positioning]] — Framework for competitive agent
-  — Technical implementation details

---

## 📝 Metadata

- **Created**: 2026-03-09
- **Status**: Active
- **Last Updated**: 2026-03-09
- **Maturity**: Production-ready (3+ audits completed)
- **Parallel Execution Time**: ~45-60 seconds (all 5 agents)
- **Documentation Completeness**: Complete (all 5 agent specifications defined)
