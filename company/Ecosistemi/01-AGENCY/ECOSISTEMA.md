# 🏢 01 — AGENCY

> **Livello:** L1 · **Priorità:** ALTA · **Stato:** ATTIVO (outreach 3 canali live)
> Dossier completo: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md`

## Missione

Acquisire e servire clienti delle 3 implementazioni AI di Digital Empire.
**"L'agenzia progettata per essere licenziata"** — autonomia del cliente, non dipendenza.

## Prodotti / Offerta

| Prodotto | Prezzo | Stato |
|---|---|---|
| Outreach Factory | €4.000 | ATTIVO |
| Content Factory | €3.500 | ATTIVO |
| Second Brain | €2.500 | ATTIVO |
| Engine Room (bundle) | €8.000 | ATTIVO |

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Ricerca | ICP research, lead discovery, qualifica | `Reparti/Ricerca/` |
| L2.2 | Acquisizione/Outreach | Email 500/gg + LinkedIn + Instagram DM | `Reparti/Acquisizione/` |
| L2.3 | Preventivi | Problem-first proposal, gate preventivo | `Reparti/Preventivi/` |
| L2.4 | Delivery/Operatività | Setup 7gg + UAT + handover codice | `Reparti/Delivery/` |
| L2.5 | Copywriting interno | Copy agency: outreach, landing, preventivi | `Reparti/Copy-interno/` |
| L2.6 | Marketing interno | Brand DE, case study, prova sociale | `Reparti/Marketing-interno/` |

## Workflow principali

- `WF-OUTREACH-EMAIL` — scraper → qualifica → scrittura → invio → follow-up
- `WF-OUTREACH-LINKEDIN` — commenti → connection → DM → follow-up
- `WF-OUTREACH-INSTAGRAM` — hashtag scout → qualifier → DM → follow-up
- `WF-PREVENTIVO` — brief → problem-first proposal → gate → invio
- `WF-DELIVERY` — onboarding → setup → UAT → handover → supporto 90gg

## Come si collega al Backbone

- **BUS:** riceve lead da MULTI-BUSINESS; invia brief copy a MARKETING; invia asset richiesti a CONTENT-FACTORY
- **BRAIN:** namespace `agency/*` — pipeline lead, preventivi, delivery stato
- **GOVERNANCE:** gate Preventivo + gate Delivery (checklist UAT)
- **IDENTITY-HR:** ~37 agenti L5 registrati in `registro-agenti.yaml`

## Sistemi attivi (NON toccare — ADR-003)

- `Outreach/Outreach Workflow/` — pipeline email 500/gg
- `Outreach/LinkedIn Automation/` — LinkedIn 20+20+30/gg
- `Outreach/Instagram Automation/` — Instagram 30 DM/gg
- `outreach-dashboard-premium/` — dashboard Next.js

Regola: si wrappano come team L3, non si riscrivono.

## Blocchi noti

- Token FB scaduto → rinnovare (dossier 01, fase B0)
- Dashboard KPI: evoluzione dell'`outreach-dashboard-premium` esistente

*Fonte: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` · Aggiornato: 2026-06-11*
