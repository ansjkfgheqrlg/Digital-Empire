---
Type: PROJECT
Status: Active
Tags: #clienti #exponium #outreach #content-factory #dashboard #saas
Created: 2026-05-22
Last updated: 2026-05-22
Client: EXPONIUM
Category: Client Infrastructure Delivery
---

# Exponium — Client Infrastructure Project

## Overview
Exponium è un cliente SaaS/Software company a cui Digital Empire consegna la propria infrastruttura operativa customizzata: un sistema completo di outreach automatizzato + content factory multi-formato + dashboard di gestione unificata. Consegna target: 7 giorni lavorativi dall'avvio.

## Prodotti Consegnati

### 1. Outreach Engine (clone customizzato)
- Base: `Outreach/Outreach Workflow/` (non modificato)
- Clone: `Clienti/EXPONIUM/outreach/`
- Upgrade rispetto all'originale:
  - AI client multi-provider (openai/anthropic/azure via .env — non più solo OpenRouter)
  - LinkedIn scraper (Playwright) per target B2B SaaS
  - G2 + Product Hunt scraper per lead freschi
  - Deep research agent (funding, tech stack, trigger aziendali)
  - ICP Scorer con tier A/B/C calibrato per Exponium
  - Knowledge base completamente riscritta per tono/ICP SaaS B2B
- Pipeline: 8 team agenti (da 6 dell'originale)

### 2. Content Factory (NUOVO)
- Path: `Clienti/EXPONIUM/content-factory/`
- Formati supportati: carousel Instagram, video Reels/VSL/YT Shorts, email sequence, social post
- Architettura: Brief Agent → [Carousel|Video|Email|Social] Agent → QA Agent (CRO)
- Video pipeline: Playwright → HeyGen API (avatar AI) + Runway Gen-4 (B-roll)
- Integration: 46 marketing skills (marketingskills-main di Corey Haines)
- Fondato su: `.agents/product-marketing.md` (da compilare con Exponium)

### 3. Dashboard (NUOVO)
- Path: `Clienti/EXPONIUM/dashboard/`
- Stack: Next.js 16 + Tailwind v4 + Framer Motion + shadcn/ui
- Sezioni: Overview / Outreach / Content Factory / Analytics / Settings
- Architettura modulare: può essere splittata in 2 app separate

## File Struttura
```
Clienti/EXPONIUM/
├── .agents/product-marketing.md    ← FONDAMENTALE — compilare PRIMA
├── outreach/                        ← Clone + refactor outreach
├── content-factory/                 ← NUOVO sistema contenuto
├── dashboard/                       ← Next.js management UI
└── GAEL_TASKS.md                   ← Task per team member Gael
```

## Team
- **Max** (Digital Empire): architettura, knowledge base, agenti core, review
- **Gael** (team member): scaffolding, componenti dashboard, testing, brand config

## Status Giorno 1 (2026-05-22)
- [x] Struttura cartelle creata
- [x] File workflow originali copiati
- [x] `ai_client.py` refactored → multi-provider
- [x] `.env.example` completo
- [x] `.agents/product-marketing.md` template
- [x] `knowledge/icp_profile.py` template
- [x] `content-factory/agents/brief_agent.py`
- [x] `content-factory/agents/video_script_agent.py`
- [x] `content-factory/agents/qa_agent.py`
- [x] `GAEL_TASKS.md` (13 task per Gael)
- [ ] LinkedIn scraper
- [ ] email_sequence_agent.py
- [ ] carousel_agent.py
- [ ] Dashboard API routes
- [ ] Knowledge base compilata (pending call con cliente)

## Informazioni da Raccogliere (Call con Exponium)
| Info | Usa per | Priorità |
|------|---------|---------|
| Descrizione prodotto | product-marketing.md | CRITICA |
| ICP / decision maker | icp_profile.py | CRITICA |
| 3 pain points | apsoc.py | CRITICA |
| Brand voice | brand_voice.py | CRITICA |
| API provider + key | ai_client.py .env | CRITICA |
| Gmail outreach | .env sender | CRITICA |
| Brand kit (logo, colori) | brands/exponium/config.json | ALTA |

## Connessioni
- [[Outreach_Workflow_Architecture]] — sistema base da cui è derivato il clone
- [[Content_Factory_System]] — architettura nuovo sistema contenuto
- [[marketingskills_Integration]] — 46 skill integrate nella content factory
- [[Digital_Empire_6_Phase_Process]] — processo standard deliverable clienti

## Note Strategiche
1. **product-marketing.md è il blocco critico** — senza dati Exponium, la knowledge base è vuota e tutto produce output generico
2. **LinkedIn scraper è il differenziatore chiave** per B2B SaaS (vs FB Ads Library del sistema originale)
3. **Video pipeline** (HeyGen via Playwright) è la parte più innovativa — richiede account HeyGen cliente
4. **Dashboard modulare by design** — se Exponium vuole 2 app separate, cambio minimo
