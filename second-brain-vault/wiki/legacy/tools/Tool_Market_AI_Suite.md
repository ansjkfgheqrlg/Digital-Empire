- **Type**: TOOL
- **Status**: Active
- **Tags**: `#automation` `#marketing` `#skill` `#multi-command` `#orchestrator`
- **Created**: 2026-04-29
- **Last updated**: 2026-04-29

## Overview

The AI Marketing Suite is a comprehensive marketing analysis and content generation system providing command-line tools for analyzing websites, generating marketing content, auditing funnels, creating proposals, and building marketing strategies.

## Purpose

The main /market command routes to specialized sub-skills for:
- **Full audits**: Parallel analysis of content, conversion, competitive, technical, and strategic dimensions
- **Quick snapshots**: 60-second marketing assessment
- **Copy generation**: Optimized copy for any page
- **Email sequences**: Personalized email campaign generation
- **Social media**: Content calendar and post generation
- **Ad creative**: Generate ad copy and creative variations
- **Funnel analysis**: Sales funnel optimization assessment
- **Competitive intelligence**: Competitor research and positioning analysis
- **Landing page CRO**: Conversion optimization analysis
- **Product launches**: Complete launch playbook generation
- **Client proposals**: Custom proposal generation
- **Reporting**: Marketing reports in Markdown and PDF formats
- **SEO audits**: Content and technical SEO analysis
- **Brand guidelines**: Brand voice analysis and guidelines

## Key Commands

| Command | Purpose | Output |
|---------|---------|--------|
| `/market audit <url>` | Full parallel marketing audit | MARKETING-AUDIT.md |
| `/market quick <url>` | 60-second snapshot | Terminal output |
| `/market copy <url>` | Copy optimization | COPY-SUGGESTIONS.md |
| `/market emails <topic>` | Email sequences | EMAIL-SEQUENCES.md |
| `/market social <topic>` | Social calendar | SOCIAL-CALENDAR.md |
| `/market ads <url>` | Ad creative | AD-CAMPAIGNS.md |
| `/market funnel <url>` | Funnel analysis | FUNNEL-ANALYSIS.md |
| `/market competitors <url>` | Competitive analysis | COMPETITOR-REPORT.md |
| `/market landing <url>` | Landing page CRO | LANDING-CRO.md |
| `/market launch <product>` | Launch playbook | LAUNCH-PLAYBOOK.md |
| `/market proposal <client>` | Client proposal | CLIENT-PROPOSAL.md |
| `/market report <url>` | Marketing report | MARKETING-REPORT.md |
| `/market seo <url>` | SEO audit | SEO-AUDIT.md |
| `/market brand <url>` | Brand analysis | BRAND-VOICE.md |

## Scoring Framework

**Marketing Score (0-100)** calculated from:
- **Content & Messaging** (25%): Copy quality, value props, clarity, persuasion
- **Conversion Optimization** (20%): CTAs, forms, friction, social proof, urgency
- **SEO & Discoverability** (20%): On-page SEO, technical SEO, content structure
- **Competitive Positioning** (15%): Differentiation, market awareness, alternatives
- **Brand & Trust** (10%): Brand consistency, trust signals, social proof
- **Growth & Strategy** (10%): Pricing, referral, retention, expansion

## Business Context Detection

Automatically detects and adapts analysis for:
- SaaS/Software (trial-to-paid conversion, onboarding, pricing)
- E-commerce (product pages, cart abandonment, reviews)
- Agency/Services (case studies, portfolio, trust signals)
- Local Business (Google Business Profile, local SEO)
- Creator/Course (lead magnets, email capture, testimonials)
- Marketplace (two-sided messaging, trust mechanisms)

## Related Resources

- [[Tool_Market_Main_Orchestrator]]
- [[Tool_Market_Competitive_Intelligence]]
- [[Tool_Market_Content_Analysis]]
- [[Tool_Market_Conversion_Optimization]]
- [[Tool_Market_Strategy_Positioning]]
- [[Tool_Market_Technical_SEO]]
