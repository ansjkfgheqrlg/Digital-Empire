---
Type: ENTITY
Status: Active
Tags: #reparto #marketing #brand #creative #strategy #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.5 — BRAND & CREATIVE STRATEGY

> **Livello:** L2.5 — Reparto di 04-MARKETING
> **Namespace AgentDB:** `marketing/brand/`
> **Coordinator:** `brand-lead` (Opus)
> **Roster:** 6 agenti · 3 workflow CF-grade
> **Missione-in-una-riga:** custodire, formalizzare e difendere l'identità di brand di Digital Empire
> e dei clienti multi-tenant — il reparto che traduce il Mandato Art.2 in sistemi operativi concreti.

---

## Missione

L2.5 Brand & Creative Strategy è il **custode operativo del Mandato Art.2 (Brand Voice)**
all'interno dell'ecosistema 04-MARKETING. Definisce, formalizza e protegge l'identità di
brand — posizionamento, voce, differenziazione competitor, direction creativa — per Digital
Empire e per ogni cliente multi-tenant che lavora con l'agenzia.

**Il reparto NON scrive copy di conversione.** Quello è L2.1-COPYWRITING. Il brand governa
il copy: fornisce la brand_voice guide, il brand_kit, il tono, la differenziazione — e poi
**BR-QA verifica che ogni output prodotto da L2.1/L2.2/L2.3 sia coerente** con quanto
formalizzato. Il confine è netto: strategia di brand → L2.5; execution copy → L2.1.

**Connessione con il Mandato:** Brand-Voice Sentinel riporta a LX (sempre-on su tutti gli
output), ma L2.5 è il fornitore della conoscenza di brand che la Sentinel usa come riferimento.
Nessuna evoluzione del brand DE si attua senza approvazione esplicita di Max (Art.5.3 Mandato).

---

## Posizione nella gerarchia

```
04-MARKETING (L1) — MKT-Conductor
  └── L2.5 BRAND & CREATIVE STRATEGY ← questo reparto
        │
        ├── coordina con: L2.1 (fornisce brand_kit per ogni richiesta copy)
        ├── coordina con: L2.2 (direction creative per ads → BR3 → 03-CF)
        ├── coordina con: 03-CONTENT-FACTORY (brief visivo per asset creativi)
        ├── coordina con: 08-INTELLIGENCE (dati competitor per BR4)
        └── riporta a: MKT-Conductor (L1) per ogni decisione cross-reparto
```

---

## Roster agenti (6)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `BRAND-LEAD` | Brand Strategy Lead | Opus | Coordinator: custodisce brand positioning DE, approva evoluzioni voce, coordina il team |
| `BR1` | Positioning Strategist | Opus | Posizionamento, USP, angolo di mercato, differenziazione competitor |
| `BR2` | Brand Voice Architect | Opus | Formalizza e aggiorna brand voice Art.2 per ogni brand_kit |
| `BR3` | Creative Director | Sonnet | Brief visivo/creativo per 03-CF, direction creative per ads |
| `BR4` | Brand Analyst | Sonnet | Analisi competitor, differenziazione, awareness mercato (coord 08-INTELLIGENCE) |
| `BR-QA` | Brand Consistency Verifier | Sonnet | Verifica ogni output vs brand_kit dichiarato + Mandato Art.2 (gate G5) |

---

## Workflow CF-grade (3)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-BRAND-AUDIT` | Audit brand positioning: competitor + voice + differenziazione + gap → report | `workflow/WF-BRAND-AUDIT.md` |
| `WF-BRAND-KIT-BUILD` | Costruzione brand_kit per nuovo cliente/canale: voice guide + visual brief + ICP + tone chart | `workflow/WF-BRAND-KIT-BUILD.md` |
| `WF-BRAND-EVOLUTION` | Proposta evolutiva brand DE → ADR-bozza (solo Max approva Art.5.3) | `workflow/WF-BRAND-EVOLUTION.md` |

---

## Skill del reparto

| Skill | Tipo | Priorità | Descrizione |
|---|---|---|---|
| `brand-strategy-gate` | Propria P0 | Nuova da forgiare | Verifica coerenza brand_kit di un output (voce, visual language, differenziazione vs competitor) |
| `market-brand` | Ausiliaria esistente | P1 | Mappata a questo reparto dal dossier §5.2 |
| `market-social` | Ausiliaria esistente | P2 | Social presence, tono sui canali — ausiliaria per BR2/BR3 |
| `market-competitors` | Ausiliaria esistente | P2 | Competitor profiling — ausiliaria per BR4 |

Skill `brand-strategy-gate` (P0): da forgiare via 07-FORGE con PRD + architettura prima della
build M1. È la skill che rende il gate G5 eseguibile deterministicamente (check binario voce
+ visual language + differenziazione). Vedi `skills/SKILLS.md` per la specifica completa.

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Brand consistency score | % output che passano G5 (BR-QA) al primo tentativo per cliente/brand_kit |
| Brand kit attivi | n. brand_kit in `marketing/brand/kits/` (crescita = il sistema scala) |
| Coerenza voice cross-output | n. fail G5 per brand_kit / mese (trend: deve calare) |
| Tempo medio brand audit | [DM] — dalla richiesta al report approvato da BRAND-LEAD |
| Brand kit aggiornamenti | n. evoluzioni brand_kit approvate nel mese (tracciamento deriva) |

*[DM] = da misurare, baseline da stabilire al primo run reale.*

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| → L2.1 | Copywriting | brand_kit attivo (voce, tono, ICP, differenziatori) come input obbligatorio per ogni richiesta copy |
| → L2.2 | Advertising | creative brief visivo (BR3) per direction ads, tono per copy ads |
| → 03-CONTENT-FACTORY | Content Factory | brief visivo e direction creativa per asset editoriali e ads |
| ← 08-INTELLIGENCE | Intelligence | Dati competitor, trend mercato, awareness ICP (input per BR4 e BR1) |
| → MKT-Conductor | Coordinatore L1 | Escalation evoluzioni brand, approvazione ADR-bozza |
| → LX/MAXIMILIAN | Mandato/Max | Proposta ADR per modifica Art.2 (solo Max approva) |

**Regola handoff:** nessun committente riceve copy da L2.1 senza `brand_kit` dichiarato.
Se il kit non esiste → L2.5 lo costruisce prima (WF-BRAND-KIT-BUILD) o blocca la richiesta.

---

## Escalation

- **G5 fail persistente (stesso brand_kit, 2+ volte consecutive):** BRAND-LEAD riesamina il
  brief originale del committente. Se il problema è nel brief → richiede brief corretto.
  Se è nel brand_kit → avvia WF-BRAND-EVOLUTION.
- **Richiesta di modifica Art.2 (brand voice DE):** non si attua. Apre WF-BRAND-EVOLUTION
  → BRAND-LEAD prepara ADR-bozza → scala a MKT-Conductor → solo Max approva (Art.5.3).
- **Collisione brand_kit vs brand voice DE:** vince il Mandato Art.2 sempre; il brand_kit
  del cliente può derogare alla voce DE per i suoi asset specifici, ma non può violare i
  vincoli di integrità (zero claim senza proof, zero dependency-language, Art.2.2).

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §L2.5
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` Art.2 + Art.5.3
- [[ARCHITETTURA]] · `company/Ecosistemi/04-MARKETING/Reparti/L2-5-Brand-Creative-Strategy/ARCHITETTURA.md`
- [[cmo-brand-voice-warden]] · `company/Board-CSuite/CMO/agenti/cmo-brand-voice-warden.md`
- [[03-CONTENT-FACTORY]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md`
- [[08-INTELLIGENCE]] · `PIANO-MAESTRO/08-ROADMAP-FASI.md`
