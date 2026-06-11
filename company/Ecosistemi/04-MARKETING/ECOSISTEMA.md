# 📣 04 — MARKETING

> **Livello:** L1 · **Priorità:** ALTA (trasversale) · **Stato:** ATTIVO (copy-workflow live)
> Dossier completo: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md`

## Missione

Motore persuasione trasversale della holding. **Copywriting è la priorità assoluta.**
Ogni copy prodotto da DE passa da questo ecosistema. Serve tutti gli altri tramite
handoff contract sul BUS.

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Copywriting | APSOC engine: A1-A8 + S1-S3, ogni formato | `Reparti/Copywriting/` |
| L2.2 | Advertising | ads Facebook/Google/LinkedIn, creative testing | `Reparti/Advertising/` |
| L2.3 | Email Marketing | sequenze lancio/nurture/post-cancel, automazioni | `Reparti/Email-Marketing/` |
| L2.4 | Analytics&Ottimizzazione | performance loop: diagnosi → fix → misura | `Reparti/Analytics/` |

## Agenti L5 esistenti (già operativi)

**Copywriting (A1-A8 + S1-S3 — dal Copy Workflow):**
A1 Market Analyst · A2 Target Analyst · A3 Problem Amplifier ·
A4 Solution Architect · A5 Objection Handler · A6 Email Specialist ·
A7 CTA Optimizer · A8 Copy Reviewer (gate QA) ·
S1 Funnel Strategist · S2 Positioning Strategist · S3 Campaign Strategist

## Workflow principali

- `WF-COPY-REQUEST` — brief → routing formato → A1-A8 → gate A8 → consegna
- `WF-COPY-AD` — brief → 3+ varianti copy → A/B test setup → launch
- `WF-EMAIL-LANCIO` — T-30 → T+7 sequenza (APSOC per email, A6 per obiezioni)
- `WF-ANALYTICS-LOOP` — metriche → diagnosi sezione APSOC → fix → misura

## Gate qualità (invarianti)

| Gate | Soglia | Bloccante? |
|---|---|---|
| G1 — Score APSOC (A8) | ≥ 80/100 standard | sì |
| G1b — Score APSOC sales page | ≥ 85/100 | sì |
| G2 — Brand gate Mandato | checklist binaria | sì, non derogabile |
| Struttura P prima di S | −15 automatico se violata | sì |

## Come si collega al Backbone

- **BUS:** riceve brief da TUTTI gli ecosistemi; invia copy finita al richiedente
- **BRAIN:** namespace `marketing/copy/patterns/{icp}` — score storici, pattern vincenti
- **GOVERNANCE:** G1+G2 gate su ogni output
- **GUILDS:** possiede la Copy/APSOC Guild (trasversale)

## Asset esistenti (già operativi — NON toccare, ADR-003)

- `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` — orchestration layer A1-A8
- skill `cro-copy-architect`, `market-*`, `cold-email`, `ads`, `ab-testing`, etc.
- `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`

*Fonte: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` · Aggiornato: 2026-06-11*
