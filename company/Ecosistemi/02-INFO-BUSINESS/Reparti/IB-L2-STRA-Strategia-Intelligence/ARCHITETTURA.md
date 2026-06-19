---
Type: CONCEPT
Status: Active
Tags: #architettura #strategia #intelligence #info-business #IB-L2-STRA
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — IB-L2-STRA Strategia & Intelligence

> Cartella-workflow CF-grade. Standard: Content Factory Exponium = 1 workflow (corpus Maximilian).
> Dossier sorgente: `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-STRA

---

## Topologia del team

```
                    ┌──────────────────────────────────┐
                    │  IB-COORD-STRATEGIA (Opus)         │
                    │  Capo Area — roadmap, next prodotto│
                    └─────────────────┬──────────────────┘
                                      │
        ┌──────────────┬──────────────┼──────────────┬──────────────┐
        │              │              │              │              │
┌───────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
│ IB-STRA-INTEL│ │IB-STRA-COMP│ │IB-STRA-ICP │ │IB-STRA-    │ │IB-STRA-    │
│ Market Intel │ │ Competitor │ │ ICP        │ │  BACKLOG   │ │  ROADMAP   │
│ (Sonnet)     │ │ (Sonnet)   │ │ (Sonnet)   │ │ (Sonnet)   │ │ (Sonnet)   │
└───────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
        │              │              │              │              │
   (input da      (audit          (segnali      (integra +     (sequenza
    08-INTEL)      competitor)     community)    score /100)    lanci)
        │              │              │              │              │
        └──────────────┴──────────────┴──────────────┴──────────────┘
                                      │ idea con score + roadmap
                       ┌──────────────▼──────────────┐
                       │   IB-STRA-QA (Sonnet)         │
                       │  Verificatore — gate "prove   │
                       │  non inventate" (bloccante)   │
                       └──────────────────────────────┘
```

**Topologia:** star da `IB-COORD-STRATEGIA` → 5 specialisti che lavorano in pipeline (INTEL → COMP → ICP →
BACKLOG) per WF-PRODUCT-INTELLIGENCE, e ROADMAP in autonomia trimestrale per WF-ROADMAP-PRODOTTI.
`IB-STRA-QA` opera trasversalmente come gate in uscita su ogni idea e ogni roadmap (verifica prove, non merito).

---

## Livelli gerarchici interni

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `IB-COORD-STRATEGIA` | Opus | Coordina l'area, propone next prodotto, presidia roadmap, escalation trend |
| L1 — Intelligence | `IB-STRA-INTEL` · `IB-STRA-COMP` | Sonnet | Raccolta dati mercato e competitor (alimentano l'analisi) |
| L2 — Sintesi | `IB-STRA-ICP` · `IB-STRA-BACKLOG` · `IB-STRA-ROADMAP` | Sonnet | ICP, scoring backlog, roadmap (trasformano dati in decisioni) |
| L3 — Verifier | `IB-STRA-QA` | Sonnet | Gate "prove non inventate" su ogni output in uscita |

---

## Flussi principali

### WF-PRODUCT-INTELLIGENCE (alimenta il backlog)
```
Cadenza mensile (+ trigger on-demand su evento di mercato)
  → IB-STRA-INTEL: scan trend (08-INTEL, community, newsletter, social) → 3-5 temi emergenti
  → IB-STRA-COMP: audit offerta competitor (prodotti, pricing, posizionamento) → gap analysis
  → IB-STRA-ICP: aggiorna ICP con dati freschi → pain points non ancora coperti
  → IB-STRA-BACKLOG: integra → bozze idea con score /100 → top 3 a IB-COORD-STRATEGIA
  → IB-STRA-QA: verifica fonti citate, dati reali, nessun numero inventato (GATE bloccante)
  → IB-COORD-STRATEGIA: presenta top idea a ib-director → se approved → WF-VALIDAZIONE (IB-L2-PROD)
Output: backlog aggiornato + top idea approvata
Gate di uscita: IB-STRA-QA PASS (ogni idea ha fonte reale)
```

### WF-ROADMAP-PRODOTTI (roadmap 6-12 mesi)
```
Cadenza trimestrale (+ aggiornamento dopo ogni lancio)
  → IB-STRA-ROADMAP: import catalogo live + backlog validato + capacità PROD (lead time) + calendario lanci
  → IB-STRA-ROADMAP: sequenziamento → dipendenze prodotto→lancio, buffer ≥30gg, allineamento Content Factory
  → IB-STRA-ICP: check → i prodotti pianificati coprono ancora i pain ICP attuali?
  → IB-STRA-QA: verifica → ogni prodotto ha lead time stimato? buffer rispettato? (GATE)
  → IB-COORD-STRATEGIA: presenta roadmap a ib-director → approvazione → store namespace
Output: roadmap aggiornata + calendario lanci approvato → guida per tutte e 5 le aree
Gate di uscita: lead time per ogni prodotto + buffer ≥30gg tra lanci consecutivi
```

---

## Flussi con ecosistemi esterni

### IB-L2-STRA ← 08-INTELLIGENCE
```
IB-STRA-INTEL e IB-STRA-COMP delegano a 08-INTELLIGENCE la ricerca pesante (scraping, profili
competitor estesi, analisi trend di settore). STRA riceve dati grezzi + fonti, NON li raccoglie da solo.
Schema richiesta: {tipo: "trend|competitor|icp_data", scope, profondità: "rapida|completa", deadline}
Risposta: dataset + fonti dichiarate (URL, data rilevazione) → mai dato senza provenienza.
```

### IB-L2-STRA → IB-L2-PROD
```
Top idea pre-validata (score ≥60) → input a WF-VALIDAZIONE.
Handoff: {idea_id, titolo, score_breakdown[5], fonti[], icp_target, gap_competitor, lead_time_stimato}
PROD riceve l'idea già qualificata; decide se diventa prodotto (test mercato, smoke test, go/no-go).
```

### IB-L2-STRA ← IB-L2-COMM → IB-L2-LANC
```
COMM → STRA: segnali community (domande ricorrenti, obiezioni post-vendita, richieste cross-sell)
              → input per IB-STRA-ICP (aggiornamento pain) e IB-STRA-BACKLOG (nuove idee).
STRA → LANC: roadmap lanci approvata (sequenza, buffer ≥30gg, dipendenze) → guida il calendario lanci.
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-INT-STRA-01` | 08-INT → STRA | dataset trend/competitor + fonti | ogni dato ha URL + data rilevazione |
| `HC-STRA-PROD-01` | STRA → IB-L2-PROD | idea pre-validata (score ≥60 + fonti) | score ≥60, ≥1 fonte reale, ICP fit dichiarato |
| `HC-COMM-STRA-01` | IB-L2-COMM → STRA | segnali community (domande, obiezioni) | segnali con conteggio/frequenza, periodo |
| `HC-STRA-LANC-01` | STRA → IB-L2-LANC | roadmap lanci approvata | lead time per prodotto + buffer ≥30gg |

---

## Namespace memoria

```
infobusiness/strategia/
├── backlog/
│   ├── idee.json              → coda idee con score /100, stato, priorità
│   └── archivio/              → idee scartate/parcheggiate (storico decisioni)
├── intelligence/
│   ├── state.json             → stato WF-PRODUCT-INTELLIGENCE (ultimo run, temi attivi)
│   ├── trend_YYYYMM.md        → report trend mensile (IB-STRA-INTEL)
│   └── fonti.json             → registro fonti citate (provenienza ogni dato)
├── competitor/
│   └── {competitor_id}_dossier_YYYYMMDD.md  → audit offerta competitor (IB-STRA-COMP)
├── icp/
│   ├── icp_infobusiness.md    → profilo ICP corrente (≠ ICP AGENCY)
│   └── icp_changelog.md       → storico aggiornamenti ICP per trimestre
└── roadmap/
    ├── roadmap_corrente.md    → roadmap prodotti 6-12 mesi approvata
    └── roadmap_archivio/      → versioni precedenti (tracciamento deriva)
```

---

## Skill del reparto

| Skill | File | Funzione |
|---|---|---|
| `product-idea-scorer` (P0, nuova) | `skills/SKILLS.md` | Scoring deterministico idea su 5 criteri /100 — rende il gate idea ripetibile |
| `marketing-ideas` (esistente) | mapping dossier | Ausiliaria: generazione angoli/idee prodotto per IB-STRA-BACKLOG |
| `competitor-profiling` (esistente) | mapping dossier | Ausiliaria: profili competitor per IB-STRA-COMP |
| `icp-radar` (esistente) | mapping dossier | Ausiliaria: profilazione ICP per IB-STRA-ICP |
| `customer-research` (esistente) | mapping dossier | Ausiliaria: raccolta voice-of-customer per ICP e backlog |

---

## Connessioni

- [[README]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-STRA-Strategia-Intelligence/README.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-STRA
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md`
- [[WF-ROADMAP-PRODOTTI]] · `workflow/WF-ROADMAP-PRODOTTI.md`
- [[ib-stra-qa-verificatore-strategia]] · `agenti/ib-stra-qa-verificatore-strategia.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (prove non promesse)
