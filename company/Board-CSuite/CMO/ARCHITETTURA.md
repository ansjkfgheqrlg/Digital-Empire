---
Type: CONCEPT
Status: Active
Tags: #cmo #architettura #team #flussi #marketing #brand
Created: 2026-06-17
Last updated: 2026-06-17
---

# ARCHITETTURA — CMO (Chief Marketing Officer)

> Blueprint: `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
> Standard: CF-grade (cartella-workflow PESANTE, ≥10 agenti)

---

## 1. Posizione nella gerarchia

```
MAXIMILIAN (LX) — standard e visione
     │
  MANDATO (LX) — legge
     │
  CEO / Empire-Conductor (L0)
     │
  ┌──┴────────────────────────────┐
  │          CMO (L0)             │
  │  (governa voce + domanda)     │
  └──┬──────────────┬─────────────┘
     │              │
 04-MARKETING   03-CONTENT-FACTORY
  (copy)         (produzione)
```

Il CMO è figura C-Suite L0. Riporta al CEO. Coordina due ecosistemi L1
(04-MARKETING, 03-CONTENT-FACTORY) e dialoga in peer-review con CRO e
02-INFO-BUSINESS per i lanci.

---

## 2. Team interno — mesh degli agenti

```
cmo-conductor (Opus)
        │
        ├─ [always-on] cmo-brand-voice-warden (Sonnet)
        │       └─ gate APSOC su OGNI output
        │
        ├─ [strategy mesh]
        │   ├─ cmo-campaign-strategist (Opus)
        │   ├─ cmo-funnel-architect (Sonnet)
        │   └─ cmo-audience-intel (Sonnet) ← feed da 08-INTELLIGENCE
        │
        ├─ [liaison mesh]
        │   ├─ cmo-marketing-liaison (Sonnet) → 04-MARKETING
        │   ├─ cmo-content-liaison (Sonnet) → 03-CONTENT-FACTORY
        │   └─ cmo-launch-coordinator (Sonnet) ↔ 02-INFO-BUSINESS
        │
        ├─ [feedback loop]
        │   └─ cmo-performance-analyst (Sonnet) → chiude loop dati→copy
        │
        └─ [memoria]
            └─ cmo-memoria (Haiku) — pattern ICP + storico campagne
```

**Regola di coordinamento:** ogni workflow con spesa reale richiede dry-run
(Mandato Art.4.3, pattern #3). Nessuna campagna parte senza ok umano su budget.

---

## 3. Workflow CF-grade (3 attivi)

### WF-CAMPAGNA
Flusso principale per campagne multi-canale. Parte da un obiettivo di business
(lead, vendita, awareness) e arriva all'execution verificata.

```
OBIETTIVO DI BUSINESS
  │
  ├─ cmo-campaign-strategist → strategia (canali, audience, timing)
  ├─ cmo-audience-intel → validazione ICP + awareness level
  ├─ cmo-funnel-architect → schema funnel (entry → nurture → CTA)
  ├─ brief → cmo-marketing-liaison (04-MARKETING) + cmo-content-liaison (03-CONTENT-FACTORY)
  ├─ [GATE] cmo-brand-voice-warden → APSOC + brand check ≥80
  ├─ [dry-run] → stima spesa/crediti, ok umano
  └─ LAUNCH → cmo-performance-analyst traccia metriche
```

### WF-BRAND-GATE
Gate always-on: ogni copy di conversione della holding passa prima di uscire.

```
OUTPUT DI CONVERSIONE (qualsiasi canale)
  │
  └─ cmo-brand-voice-warden
       ├─ Checklist Brand Gate G2 (Mandato Art.4.2)
       ├─ Score APSOC (≥80 standard, ≥85 sales page)
       ├─ Anti-slop scan (zero genericità, zero icebreaker vuoti)
       ├─ CPB check (ogni claim ha proof)
       └─ [PASS → USCITA] | [FAIL → RIFAI con feedback]
```

### WF-LANCIO-COORD
Coordina un lancio info-business end-to-end con CRO.

```
INPUT: brief lancio da 02-INFO-BUSINESS
  │
  ├─ cmo-launch-coordinator → piano lancio (fasi, asset, canali)
  ├─ cmo-funnel-architect → funnel lancio dedicato
  ├─ brief → 03-CONTENT-FACTORY (asset) + 04-MARKETING (copy)
  ├─ CRO (peer) → offerta + pricing + pagina di vendita
  ├─ [GATE] cmo-brand-voice-warden → APSOC ≥85 su sales page
  ├─ [dry-run revenue] → proiezione, ok umano su spesa ads
  └─ LANCIO → cmo-performance-analyst monitoraggio real-time
```

---

## 4. Skill proprie

| Skill | Scopo |
|---|---|
| `empire-brand-gate` | Checklist voce Mandato + APSOC + anti-slop: gate bloccante |
| `campaign-orchestrator` | Orchestrazione campagna multi-canale end-to-end |
| `icp-pattern-library` | Libreria pattern ICP per nicchia: aggiornata da 08-INTELLIGENCE |

---

## 5. Flusso dati e namespace AgentDB

```
Namespace: board/cmo/

board/cmo/campagne/          — brief, strategia, risultati per campagna
board/cmo/brand-gate-log/    — log ogni APSOC check (score, esito, delta)
board/cmo/icp-patterns/      — pattern ICP consolidati per nicchia
board/cmo/lancio-history/    — storico lanci con metriche
board/cmo/performance/       — CTR/CVR per canale e variante
```

---

## 6. Regola di blocker

Il CMO NON permette mai che un output di conversione:
1. Superi il gate brand/APSOC senza score registrato.
2. Contenga claim senza proof (CPB violato = difetto bloccante, Mandato Art.2.2).
3. Abbia P dopo S (struttura APSOC invertita = −15 automatico).
4. Manchi del `brand_kit` dichiarato (multi-tenant, Mandato Art.6.1).

---

## Connessioni

- [[BP-CMO]] · `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
- [[cmo-conductor]] · `agenti/cmo-conductor.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[WF-CAMPAGNA]] · `workflow/WF-CAMPAGNA.md`
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md`
- [[WF-LANCIO-COORD]] · `workflow/WF-LANCIO-COORD.md`
- [[MANDATO-EMPIRE]] Art.2 + Art.4 + Art.6
- [[12-DOSSIER-MAXIMILIAN]] §1 — standard di qualità
