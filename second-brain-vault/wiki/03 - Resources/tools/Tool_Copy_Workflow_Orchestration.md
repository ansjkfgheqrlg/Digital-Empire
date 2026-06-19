---
Type: TOOL
Status: Active
Tags: #copywriting #apsoc #workflow #agenti #orchestration #sales-page #ads #email #funnel
Created: 2026-05-26
Last updated: 2026-05-26
---

# Copy Workflow — Orchestration Layer

## Overview
Sistema completo di copywriting derivato da "Il Manuale del Copywriting v1.1". Comprende un orchestratore master, 8 agenti specializzati in sequenza APSOC, 6 sub-skill invocabili, 4 workflow operativi e 4 template. Produce copy professionale per qualsiasi formato (ads, sales page, email, VSL) con QA automatico a 100 punti.

**Location**: `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`
**Entry point**: `copy-workflow/SKILL.md`
**Invocazione**: `/copywriting [mode]`

---

## Architettura

```
copy-workflow/
├── SKILL.md                          ← Entry point + comandi
├── orchestrators/
│   └── copy-master.md                ← Orchestratore decisionale (router)
├── agents/
│   ├── research/
│   │   ├── briefing-analyst.md       ← A1: raccoglie requisiti
│   │   └── target-analyst.md         ← A2: avatar + pain points + language map
│   ├── apsoc/
│   │   ├── attention-writer.md       ← A3: headline + hook (9 strategie)
│   │   ├── problem-writer.md         ← A4: problema amplificato (regola: no prodotto)
│   │   ├── solution-writer.md        ← A5: USP + benefits + post-acquisto
│   │   ├── objections-handler.md     ← A6: CPB framework (10 tipi obiezione)
│   │   └── cta-writer.md             ← A7: CTA profondo + urgenza
│   └── qa/
│       └── copy-reviewer.md          ← A8: score APSOC 100pt + gate qualità
├── skills/
│   ├── apsoc-builder/SKILL.md        ← Costruisce copy APSOC interattivo
│   ├── target-avatar/SKILL.md        ← Crea buyer persona completa
│   ├── headline-forge/SKILL.md       ← Genera 10 headline alternative
│   ├── objections-forge/SKILL.md     ← CPB per ogni obiezione
│   ├── funnel-designer/SKILL.md      ← Progetta funnel strategici
│   └── copy-review/SKILL.md          ← Review copy esistente
├── workflows/
│   ├── full-copy-workflow.md         ← Pipeline completo 60-120 min
│   ├── quick-ad-workflow.md          ← Ads in 15-20 min (3 varianti)
│   ├── sales-page-workflow.md        ← Sales page completa 90-120 min
│   └── email-sequence-workflow.md    ← Sequenze email (welcome/nurture/lancio)
└── templates/
    ├── briefing-template.md          ← Form raccolta dati pre-pipeline
    ├── avatar-template.md            ← Template buyer persona completo
    ├── copy-checklist.md             ← QA APSOC 100 punti compilabile
    └── cpb-template.md               ← 10 CPB pre-costruiti + matrice
```

---

## Framework Centrale: APSOC

Il DNA di tutto il sistema. Ogni copy segue questa struttura sequenziale:

| Lettera | Sezione | Regola Critica |
|---|---|---|
| **A** | Attention — headline + hook | Cattura entro 3 secondi |
| **P** | Problem — pain amplificato | Il prodotto NON compare qui |
| **S** | Solution — USP + benefits | Sempre dopo P, mai prima |
| **O** | Objections — CPB per dubbi | Claim → Proof → Benefit |
| **C** | CTA — chiusura + urgenza | CTA profondo, non superficiale |

**Violazione critica**: mostrare la soluzione prima del problema abbassa lo score di -15 punti automaticamente.

---

## Comandi Disponibili

```
/copywriting full          → Pipeline completo A1→A8 (60-120 min)
/copywriting ad            → Quick Ad Workflow 15-20 min, 3 varianti
/copywriting sales-page    → Sales page completa con anatomia dettagliata
/copywriting email         → Sequenza email (tipo da specificare)
/copywriting headline      → Solo headline-forge (10 alternative)
/copywriting objections    → Gestione obiezioni con CPB
/copywriting avatar        → Solo target-avatar (buyer persona)
/copywriting funnel        → Funnel designer strategico
/copywriting review        → Review copy esistente + score APSOC
```

---

## Agenti e Ruoli

| Agente | Codice | Ruolo | Output |
|---|---|---|---|
| Briefing Analyst | A1 | Raccoglie tutti i dati | briefing-completo.md |
| Target Analyst | A2 | Avatar + pain points + language map | avatar.md + pain-points.md |
| Attention Writer | A3 | 3 headline + hook apertura | attention-section.md |
| Problem Writer | A4 | Problema amplificato | problem-section.md |
| Solution Writer | A5 | USP + benefits + post-acquisto | solution-section.md |
| Objections Handler | A6 | CPB per 2-3 obiezioni principali | objections-section.md |
| CTA Writer | A7 | CTA profondo + urgenza | cta-section.md |
| Copy Reviewer | A8 | Score APSOC 100pt + iterazioni | copy-finale.md + qa-report.md |

---

## Score QA

| Score | Verdetto | Azione |
|---|---|---|
| ≥ 90 | Eccellente | Pubblica senza modifiche |
| 80-89 | Buono | Ritocchi minori |
| 70-79 | Accettabile | Rivedi 1-2 sezioni |
| 60-69 | Insufficiente | Revisione sostanziale |
| < 60 | Bocciato | Riscrittura da capo |

Gate standard: ≥ 80. Sales page: ≥ 85.

---

## Workflow Raccomandati per Caso d'Uso

| Obiettivo | Workflow | Durata |
|---|---|---|
| Ad Facebook/IG/TikTok | quick-ad-workflow | 15-20 min |
| Sales page low-ticket | sales-page-workflow | 60-90 min |
| Sales page high-ticket | sales-page-workflow + full | 90-120 min |
| Lancio prodotto completo | full-copy-workflow (esteso) | 2-3 ore |
| Onboarding nuovi iscritti | email-sequence-workflow (welcome) | 45-60 min |
| Recupero lista fredda | email-sequence-workflow (re-engagement) | 30-40 min |
| Review copy esistente | /copywriting review | 10-20 min |

---

## Framework CPB (Claim → Proof → Benefit)

Usato in A6 per ogni obiezione:

1. **Claim**: risposta diretta all'obiezione
2. **Proof**: prova specifica (dati, testimonianza, caso studio, garanzia...)
3. **Benefit**: "il che significa che tu..."

10 CPB pre-costruiti disponibili in `templates/cpb-template.md` per le obiezioni più comuni (prezzo, tempo, fiducia, risultati, alternative, complessità).

---

## Origine

Costruito tramite content-forge (target: orchestration) da:
- **Fonte primaria**: "Il Manuale del Copywriting v1.1" — 115 pagine, ~22.700 parole
- **Framework estratti**: APSOC, CPB, Pain Point Amplification, CTA Profondo, Funnel Architecture
- **Data build**: 2026-05-26

---

## Connessioni
- [[concepts/Framework_Cold_Outreach_APSOC]] — framework APSOC+V per outreach
- [[Map - Skill_And_Agenti]] — mappa area skill & agenti
- [[tools/Tool_Content_Forge]] — tool usato per costruire questo sistema
