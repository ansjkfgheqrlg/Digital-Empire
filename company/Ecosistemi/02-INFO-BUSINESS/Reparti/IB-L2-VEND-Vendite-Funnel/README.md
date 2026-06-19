---
Type: ENTITY
Status: Active
Tags: #reparto #info-business #vendite #funnel #evergreen #IB-L2-VEND
Created: 2026-06-18
Last updated: 2026-06-18
---

# IB-L2-VEND — VENDITE & FUNNEL

> **Livello:** L2 — Reparto di 02-INFO-BUSINESS
> **Namespace AgentDB:** `infobusiness/vendite/`
> **Coordinator:** `IB-COORD-VENDITE` (Sonnet)
> **Roster:** 8 agenti · 3 workflow CF-grade
> **Missione-in-una-riga:** costruire e ottimizzare l'infrastruttura di vendita che genera revenue
> sia durante i lanci sia nei 365 giorni tra un lancio e l'altro — il funnel evergreen come reparto,
> non come ripiego post-lancio.

---

## Missione

IB-L2-VEND è il **motore di vendita di 02-INFO-BUSINESS**. Costruisce l'infrastruttura che
trasforma traffico in lead, lead in acquirenti e acquirenti in pipeline per gli altri ecosistemi.
Il funnel evergreen — lead magnet → email nurture → sales page → checkout, con tracking eventi
su ogni step — non è un asset opzionale: è un reparto dedicato con workflow propri che gira tutti
i 365 giorni. **Un lancio valida l'offerta; il funnel evergreen la scala.**

L'**offer stack** (value stack, bonus, garanzia, order bump, upsell, naming) è progettato qui.
I **valori numerici dei prezzi** NON sono decisi in questo reparto: arrivano dal team-prezzi
(B-003, ADR-005). Questo reparto slotta l'architettura dell'offerta pronta e recepisce i numeri
approvati prima del go live.

**Il reparto NON scrive il copy di conversione da zero.** La direzione APSOC e i framework vengono
da 04-MARKETING; IB-VEND-SALESPAGE applica la skill `cro-copy-architect` per assemblare e adattare
il copy della sales page e delle email, e IB-VEND-QA verifica APSOC + "prove non promesse" (Mandato
Art.2) su ogni elemento prima del deploy. Il confine: strategia di brand e copy di reparto → MARKETING;
assemblaggio funnel + gate vendite → IB-L2-VEND.

---

## Posizione nella gerarchia

```
02-INFO-BUSINESS (L1) — ib-director
  └── IB-L2-VEND VENDITE & FUNNEL ← questo reparto
        │
        ├── coordina con: IB-L2-COMM (acquirente → onboarding studente → community)
        ├── coordina con: 04-MARKETING (copy APSOC, email nurture, direction brand)
        ├── coordina con: 06-PLATFORM (build pagina + checkout + paywall + deploy)
        ├── coordina con: team-prezzi B-003 (riceve prezzi approvati per offer stack)
        ├── coordina con: 08-INTELLIGENCE (intelligence Beggiato — Founder Authority Stack)
        └── riporta a: ib-director (L1) per ogni decisione cross-reparto + debrief lancio
```

---

## Roster agenti (8)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `IB-COORD-VENDITE` | Capo Area Vendite — L2 coordinator | Sonnet | Orchestra i 3 WF; coordina MARKETING/PLATFORM/COMM; escalation a ib-director |
| `IB-VEND-QA` | Verificatore Vendite — QA area indipendente | Sonnet | Gate copy APSOC ≥80 + gate brand "prove non promesse" su ogni elemento di sales page e funnel |
| `IB-VEND-OFFER` | Offer Architect | Sonnet | Value stack, bonus, garanzia, order bump, upsell, naming — attende prezzi da team-prezzi (B-003) |
| `IB-VEND-SALESPAGE` | Sales Page Builder | Sonnet | Sales page: copy APSOC (skill `cro-copy-architect`) + build (skill `empire-premium-style`) |
| `IB-VEND-CHECKOUT` | Checkout Technician | Haiku | Pagina pagamento, recupero carrelli abbandonati, ricevute; coordina con PLATFORM |
| `IB-VEND-CRO` | CRO Analyst | Sonnet | Test A/B su step del funnel (skill `ab-testing`, `cro`); 1 test alla volta; no rollout senza dati |
| `IB-VEND-TRACK` | Tracking Analyst | Haiku | Eventi, UTM, attribution, report conversioni per step; input per CRO e debrief lancio |
| `IB-VEND-LEAD` | Lead Magnet Specialist | Sonnet | Opt-in page, lead magnet, integrazione lista email; skill `lead-magnets` |

> **WRAPPA-ESISTENTE (ADR-003):** questo reparto wrappa `IB-R3-VENDITE-FUNNEL.md` e riusa
> l'agente esistente `IB-SALES-funnel` (Sales Funnel Manager), le cui responsabilità sono
> distribuite tra `IB-COORD-VENDITE` (orchestrazione WF) e `IB-VEND-OFFER` (offer stack).
> `IB-SALES-funnel` resta valido come alias storico; nessun asset cancellato.

---

## Workflow CF-grade (3)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-SALESPAGE` | Brief → offer stack → copy APSOC → build empire → tracking → sales page live | `workflow/WF-SALESPAGE.md` |
| `WF-FUNNEL-EVERGREEN` | Lead magnet → opt-in → nurture → sales page evergreen → checkout → loop CRO | `workflow/WF-FUNNEL-EVERGREEN.md` |
| `WF-CRO-OTTIMIZZAZIONE` | Ciclo continuo: misura → ipotesi → 1 test A/B → dati → adozione o scarto | `workflow/WF-CRO-OTTIMIZZAZIONE.md` |

---

## Skill del reparto

| Skill | Tipo | Priorità | Descrizione |
|---|---|---|---|
| `cro-copy-architect` | Ausiliaria esistente | P0 | Copy APSOC per sales page, email, CTA — usata da IB-VEND-SALESPAGE e verificata da IB-VEND-QA |
| `empire-premium-style` | Ausiliaria esistente | P0 | Build pagina premium Next.js — handoff a PLATFORM per deploy |
| `lead-magnets` | Ausiliaria esistente | P1 | Opt-in page + lead magnet — usata da IB-VEND-LEAD |
| `ab-testing` · `cro` | Ausiliaria esistente | P1 | Disegno ed esecuzione test funnel — usate da IB-VEND-CRO |
| `analytics` | Ausiliaria esistente | P1 | Tracking eventi, UTM, attribution — usata da IB-VEND-TRACK |
| `paywalls` | Ausiliaria esistente | P2 | Order bump, upsell, upgrade path — ausiliaria per IB-VEND-OFFER/CHECKOUT |
| `funnel-gate` | Propria P1 | Nuova da forgiare | Gate deterministico funnel: percorso end-to-end + eventi 100% + checkout testato |

Vedi `skills/SKILLS.md` per la specifica completa e il mapping anti-contraddizione (07-FORGE).

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Conversione evergreen | % visitatori sales page → acquisto (loop continuo) |
| Opt-in rate lead magnet | % visitatori opt-in page → lead in lista email |
| AOV | Valore medio ordine, incluso effetto order bump + upsell |
| Email open rate | % aperture sequenza nurture (per email della sequenza) |
| Revenue per lead | Revenue totale / n. lead in lista (efficienza del funnel) |
| Copertura tracking | % step funnel con evento configurato e verificato (target: 100%) |

*Baseline da stabilire al primo run reale (M1). Vedi `kpi/KPI.md`.*

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| ← team-prezzi B-003 | Pricing | Catalogo prezzi approvati per ogni prodotto (sblocca offer stack in produzione) |
| ← 04-MARKETING | Marketing | Direction APSOC, framework copy, brand_kit, email nurture base |
| → 06-PLATFORM (HC-PL-IB-01) | Platform | Build sales page (empire-premium-style) + checkout + deploy |
| → IB-L2-COMM | Community | Acquirente → WF-ONBOARDING-STUDENTE (handoff post-purchase) |
| → ib-director | Coordinatore L1 | Report conversioni, debrief lancio, escalation cross-reparto |
| ← 08-INTELLIGENCE | Intelligence | Frame Founder Authority Stack (intelligence Beggiato) per sequenza nurture |

**Regola handoff:** nessuna sales page va in produzione senza (a) prezzi da catalogo approvato
B-003, (b) gate APSOC ≥80 di IB-VEND-QA, (c) tracking eventi verde in debug mode.

---

## Escalation

- **Conversione < 1% dopo 500 visitatori sulla sales page:** IB-COORD-VENDITE flag a ib-director
  per revisione dell'OFFERTA (non solo del copy) — coinvolge IB-VEND-OFFER e team-prezzi B-003.
- **Bug checkout (pagamento non procede):** P0 — IB-VEND-CHECKOUT blocca la promozione, fix
  immediato con PLATFORM; nessun traffico verso un checkout rotto.
- **Prezzo non approvato da B-003 a ridosso del go live:** il go live slitta. Nessun agente IB
  pubblica prezzi non approvati (vincolo B-002/B-003) — neanche "provvisori".
- **Richiesta di scarcity artificiale (deadline finte sull'evergreen):** IB-VEND-QA blocca.
  Mandato Art.2 — l'evergreen non usa scarcity falsa; un bonus a scadenza deve essere reale.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-VEND
- [[IB-R3-VENDITE-FUNNEL]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R3-VENDITE-FUNNEL.md` (base wrappata)
- [[IB-SALES-funnel]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-SALES-funnel.md` (agente riusato)
- [[ARCHITETTURA]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-VEND-Vendite-Funnel/ARCHITETTURA.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — prove non promesse, no scarcity falsa)
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` (fornitore copy)
- [[06-PLATFORM]] · infrastruttura checkout, paywall, deploy
