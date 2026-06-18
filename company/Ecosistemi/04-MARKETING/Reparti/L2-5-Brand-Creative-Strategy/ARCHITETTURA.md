---
Type: CONCEPT
Status: Active
Tags: #architettura #brand #creative-strategy #marketing #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.5 Brand & Creative Strategy

> Cartella-workflow CF-grade. Standard: Content Factory Exponium = 1 workflow (corpus Maximilian).
> Dossier sorgente: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §L2.5

---

## Topologia del team

```
                   ┌──────────────────────────────┐
                   │     BRAND-LEAD (Opus)          │
                   │  custode brand DE, coordinator │
                   └──────────────┬───────────────-┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
┌───────▼────────┐     ┌──────────▼───────┐     ┌──────────▼──────────┐
│ BR1            │     │ BR2              │     │ BR4                 │
│ Positioning    │     │ Brand Voice      │     │ Brand Analyst       │
│ Strategist     │     │ Architect        │     │ (Sonnet)            │
│ (Opus)         │     │ (Opus)           │     │                     │
└───────┬────────┘     └──────────┬───────┘     └──────────┬──────────┘
        │                         │                         │
        │              ┌──────────▼───────┐                 │ (input da
        │              │ BR3              │                 │ 08-INTELLIGENCE)
        │              │ Creative Director│                 │
        │              │ (Sonnet)         │                 │
        │              └──────────┬───────┘                 │
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │ brand_kit + brief visivo
                   ┌──────────────▼───────────────┐
                   │     BR-QA (Sonnet)             │
                   │  Brand Consistency Verifier    │
                   │  (gate G5 — bloccante)         │
                   └──────────────────────────────-┘
```

**Topologia:** star da `BRAND-LEAD` → specialisti in parallelo per costruzione brand_kit;
sequenziale su WF-BRAND-AUDIT (BR4 → BR1 → BR2 → BRAND-LEAD → BR-QA verifica).
BR-QA opera trasversalmente su tutti i workflow come gate G5 in uscita.

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `BRAND-LEAD` | Opus | Coordina il reparto, custodisce brand DE, approva evoluzioni |
| L1 — Strategist | `BR1` · `BR2` | Opus | Posizionamento + Brand Voice (decisioni di brand ad alto impatto) |
| L2 — Specialist | `BR3` · `BR4` | Sonnet | Creative direction e analisi competitor |
| L3 — Verifier | `BR-QA` | Sonnet | Gate G5 su ogni output in uscita dal reparto |

---

## Flussi principali

### WF-BRAND-AUDIT (audit brand positioning)
```
Trigger: richiesta audit (commissione interna o da committente)
  → BR4: analisi competitor + awareness mercato (input 08-INTELLIGENCE)
  → BR1: gap posizionamento (USP vs competitor, angolo di mercato)
  → BR2: verifica coerenza brand voice esistente con Mandato Art.2
  → BRAND-LEAD: consolida report + raccomandazioni prioritizzate
  → BR-QA: gate G5 — il report stesso è coerente con la voce DE?
Output: `marketing/brand/audit/{brand_id}_audit.md`
Gate di uscita: BR-QA PASS + BRAND-LEAD approva
```

### WF-BRAND-KIT-BUILD (costruzione brand_kit)
```
Trigger: nuovo cliente agency, nuovo canale DE, nuovo prodotto multi-brand
  → BR4: ricerca ICP + analisi competitor del cliente (8-INTELLIGENCE input)
  → BR1: posizionamento + USP + angolo di differenziazione per quel mercato
  → BR2: voice guide (tono, registro, proibizioni, esempi positivi/negativi)
  → BR3: visual brief (palette, tipografia, reference, mood, format ads)
  → BRAND-LEAD: revisione integrata brand_kit completo
  → BR-QA: gate G5 — il kit è internamente coerente e non contraddice Mandato Art.2?
Output: `marketing/brand/kits/{brand_kit_id}/` (4 file: voice-guide.md, visual-brief.md, icp.md, tone-chart.md)
Gate di uscita: BR-QA PASS + BRAND-LEAD firma il kit
```

### WF-BRAND-EVOLUTION (proposta evolutiva brand DE)
```
Trigger: segnali di deriva dal loop AN4, richiesta di Max, cambiamento mercato
  → BR4: evidenze di deriva (dati, feedback, mercato)
  → BR1: nuova ipotesi di posizionamento (cosa cambia e perché)
  → BR2: proposta di evoluzione voice guide (delta dal kit attuale)
  → BRAND-LEAD: costruisce ADR-bozza (cosa si cambia, perché, impatto su kit esistenti)
  → MKT-Conductor: escalation per revisione
  → MAX: unico autorizzato ad approvare modifiche a Art.2 (Art.5.3 Mandato)
ATTENZIONE: nessuna modifica si attua prima dell'approvazione Max.
ADR-bozza in: `company/Memory/decisions/ADR-DRAFT-BRAND-EVOLUTION-YYYYMMDD.md`
```

---

## Flussi con ecosistemi esterni

### L2.5 → L2.1 Copywriting
```
Ogni richiesta copy ricevuta da L2.1 deve portare brand_kit dichiarato.
L2.5 fornisce: brand_kit attivo (voce, tono, ICP, differenziatori, proibizioni).
Se brand_kit mancante: L2.5 blocca o avvia WF-BRAND-KIT-BUILD prima.
Namespace condiviso: marketing/brand/kits/{id} (L2.1 legge, L2.5 scrive)
```

### L2.5 → L2.2 Advertising + 03-CF
```
BR3 produce creative brief → handoff a 03-CF per visual ads.
BR3 fornisce a L2.2: direction tone ads, mood board reference, regole visuali per piattaforma.
Schema handoff: {brand_kit_id, formato_ads, platform, mood, regole_visuali, reference_url[]}
```

### L2.5 ← 08-INTELLIGENCE
```
BR4 richiede a 08-INTELLIGENCE: profilo competitor, quote mercato, ICP data aggiornata.
Schema richiesta: {brand_kit_id, competitor_list[], icp_id, profondità: "rapida|completa"}
Risposta: competitor card + positioning map + awareness mercato + differenziatori chiave
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-L25-L21-01` | L2.5 → L2.1 | brand_kit_id + voice_guide + differenziatori | brand_kit presente in namespace prima di ogni run copy |
| `HC-L25-L22-01` | L2.5 → L2.2 | creative_brief (BR3) + brand_kit_id | brief con format, mood, regole, reference |
| `HC-L25-CF-01` | L2.5 → 03-CF | visual_brief (BR3) + brand_kit_id | brief con palette, tipografia, mood, reference |
| `HC-INT-L25-01` | 08-INT → L2.5 | competitor card + positioning map | dati con fonte e data rilevazione |

---

## Namespace memoria

```
marketing/brand/
├── kits/
│   ├── DE/                  → brand_kit Digital Empire (DE — default, dal Mandato Art.2)
│   │   ├── voice-guide.md   → linee guida voce (tono, registro, proibizioni, esempi)
│   │   ├── visual-brief.md  → palette, tipografia, mood, format
│   │   ├── icp.md           → ICP principale DE (agenzie, PMI, info-producer)
│   │   └── tone-chart.md    → matrice tono per canale (email, ads, social, video)
│   └── {cliente_id}/        → brand_kit per cliente agency (struttura identica)
├── audit/
│   └── {brand_id}_audit.md  → report audit brand positioning
└── evolution/
    └── ADR-DRAFT-*.md       → bozze proposta evolutiva (in attesa approvazione Max)
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `brand-strategy-gate` (P0, nuova) | `skills/SKILLS.md` | Gate G5 deterministico: check binario voce + visual + differenziazione |
| `market-brand` (esistente) | mapping §5.2 dossier | Ausiliaria: brand identity, positioning base |
| `market-social` (esistente) | mapping §5.2 dossier | Ausiliaria: tono sui canali social |
| `market-competitors` (esistente) | mapping §5.2 dossier | Ausiliaria: competitor profiling per BR4 |

---

## Connessioni

- [[README]] · `company/Ecosistemi/04-MARKETING/Reparti/L2-5-Brand-Creative-Strategy/README.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md`
- [[WF-BRAND-AUDIT]] · `workflow/WF-BRAND-AUDIT.md`
- [[WF-BRAND-KIT-BUILD]] · `workflow/WF-BRAND-KIT-BUILD.md`
- [[WF-BRAND-EVOLUTION]] · `workflow/WF-BRAND-EVOLUTION.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 + Art.5.3)
- [[cmo-brand-voice-warden]] · `company/Board-CSuite/CMO/agenti/cmo-brand-voice-warden.md`
