---
Type: ENTITY
Status: Active
Tags: #cmo #board #marketing #brand #apsoc #c-suite
Created: 2026-06-17
Last updated: 2026-06-17
---

# CMO — Chief Marketing Officer

> **ID:** CMO-001 · **Tier:** Opus (conduzione) / Sonnet (esecuzione) / Haiku (memoria)
> **Namespace AgentDB:** `board/cmo`
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
> **Livello gerarchico:** L0 — Board C-Suite

---

## Missione

Il CMO **governa la voce e la domanda** di Digital Empire. In una frase:

> *"Ogni parola che esce da DE ha una proof dietro. Niente promesse senza dati."*

Presidia due fronti simultanei:

1. **Brand gate** — nessun output di conversione esce senza APSOC ≥80 e Brand Voice conforme (Mandato Art.2).
2. **Domanda** — campagne multi-canale, funnel cross-prodotto, lanci info-business, ICP aggiornato.

Non costruisce siti (→ CTO/Platform). Non scrive il copy finale (→ 04-MARKETING). Governa il messaggio e ne misura la resa.

---

## Team interno (10 agenti)

| Agente | Ruolo | Tier |
|---|---|---|
| `cmo-conductor` | Conduce il team, riporta al CEO | Opus |
| `cmo-brand-voice-warden` | Gate APSOC + Brand Voice su ogni output (always-on) | Sonnet |
| `cmo-marketing-liaison` | Contatto con 04-MARKETING (motore copy) | Sonnet |
| `cmo-content-liaison` | Contatto con 03-CONTENT-FACTORY (produzione) | Sonnet |
| `cmo-campaign-strategist` | Strategia campagne multi-canale | Opus |
| `cmo-funnel-architect` | Architettura funnel cross-prodotto | Sonnet |
| `cmo-audience-intel` | ICP/insight (handoff con 08-INTELLIGENCE) | Sonnet |
| `cmo-performance-analyst` | Legge performance, chiude il loop dati→copy | Sonnet |
| `cmo-launch-coordinator` | Lanci con 02-INFO-BUSINESS | Sonnet |
| `cmo-memoria` | Pattern copy vincenti per ICP, storico campagne | Haiku |

---

## Workflow CF-grade

- **WF-CAMPAGNA** — da obiettivo a lancio: strategia → brief → gate APSOC+brand → execution.
- **WF-BRAND-GATE** — ogni copy di conversione passa il gate voce/APSOC prima di uscire (always-on).
- **WF-LANCIO-COORD** — lancio info-business end-to-end con CRO incluso.

---

## Handoff

| Direzione | Ecosistema / Figura |
|---|---|
| → Esecuzione copy | **04-MARKETING** |
| → Asset produzione | **03-CONTENT-FACTORY** |
| ↔ Lanci | **02-INFO-BUSINESS** |
| ↔ Revenue lanci | **CRO** |
| ← ICP feed | **08-INTELLIGENCE** |
| → Voce | **Mandato Art.2** (Brand Voice "prove, non promesse") |
| ↑ Decisioni strategiche posizionamento | **CEO** |

---

## KPI principali

| Metrica | Target | Metodo |
|---|---|---|
| First-pass APSOC medio | ≥ 80/100 | Score audit `cmo-brand-voice-warden` |
| APSOC sales page | ≥ 85/100 | Score audit su ogni sales page |
| Output fuori brand | 0 | Gate binario `WF-BRAND-GATE` |
| CTR/CVR per campagna | [DM] | Tracking per variante attivo |
| Pattern ICP consolidati | crescita YoY | `cmo-memoria` — storico pattern |

---

## Standard APSOC attivi (Mandato Art.4)

- Gate copy standard: **≥ 80/100**
- Gate sales page + proposte commerciali: **≥ 85/100**
- P sempre prima di S — violazione = −15 automatico
- Brand Gate G2 (checklist binaria): voce ✓ · prove ✓ · APSOC ✓ · pricing ✓ · zero AI-slop ✓
- Fonte: `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`

---

## Struttura cartella

```
CMO/
├── README.md              ← questo file
├── ARCHITETTURA.md        ← architettura team e flussi
├── agenti/                ← 10 schede CF-grade (una per agente)
├── workflow/              ← 3 workflow CF-grade
├── principi/PRINCIPI.md
├── regole/REGOLE.md
├── skills/SKILLS.md
├── scripts/README.md
├── kpi/KPI.md
└── state/README.md
```

---

## Connessioni

- [[BP-CMO]] · `company/Board-CSuite/_BLUEPRINT/BP-CMO.md`
- [[cmo-conductor]] · `agenti/cmo-conductor.md`
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md`
- [[MANDATO-EMPIRE]] Art.2 (Brand Voice) + Art.4 (Gate APSOC)
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[14-DOSSIER-ARCHITETTURA]] · `PIANO-MAESTRO/14-DOSSIER-ARCHITETTURA.md`
- [[CEO-Empire-Conductor]] · `company/Board-CSuite/CEO-Empire-Conductor/README.md`
