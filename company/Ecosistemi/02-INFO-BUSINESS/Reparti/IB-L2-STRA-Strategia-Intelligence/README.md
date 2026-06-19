---
Type: ENTITY
Status: Active
Tags: #reparto #info-business #strategia #intelligence #product-backlog #IB-L2-STRA
Created: 2026-06-18
Last updated: 2026-06-18
---

# IB-L2-STRA — STRATEGIA & INTELLIGENCE

> **Livello:** L2 — Reparto/Area di 02-INFO-BUSINESS (azienda interna)
> **Namespace AgentDB:** `infobusiness/strategia/`
> **Coordinator:** `IB-COORD-STRATEGIA` (Opus)
> **Roster:** 7 agenti · 2 workflow CF-grade
> **Missione-in-una-riga:** alimentare INFO-BUSINESS con idee prodotto già pre-validate e una roadmap
> basata su dati — l'area che fa evolvere il business col mercato anziché rincorrerlo.

---

## Missione

IB-L2-STRA è **l'area che mancava completamente nel v1**. Gestisce il product backlog, monitora trend e
concorrenti, produce la roadmap prodotti basata su dati, e assicura che INFO-BUSINESS si evolva con il
mercato. Lavora a stretto contatto con **08-INTELLIGENCE** (a cui delega la ricerca pesante) e **alimenta
l'Area Prodotto (IB-L2-PROD)** con idee già pre-validate, prima che arrivino a WF-VALIDAZIONE.

**Il reparto NON valida i prodotti né li costruisce.** La validazione formale (test mercato, smoke test,
go/no-go) è di IB-L2-PROD via WF-VALIDAZIONE. STRA fa il lavoro a monte: identifica i temi emergenti,
mappa i gap competitor, aggiorna l'ICP, scrive le bozze idea con uno score iniziale, e propone la top
idea al Director. **Pre-validazione ≠ validazione**: STRA porta l'idea con score ≥60 e fonti reali;
PROD decide se diventa prodotto.

**Il principio che governa l'area:** *l'Area Prodotto non dovrebbe mai cercare idee — le riceve già
qualificate da questo workflow.* La ricerca dell'idea è un processo industriale, non un colpo di genio.

---

## Posizione nella gerarchia

```
02-INFO-BUSINESS (L1) — ib-director
  └── IB-L2-STRA STRATEGIA & INTELLIGENCE ← questo reparto
        │
        ├── alimenta: IB-L2-PROD (idee pre-validate → WF-VALIDAZIONE)
        ├── coordina con: 08-INTELLIGENCE (delega ricerca trend/competitor pesante)
        ├── informa: IB-L2-LANC (roadmap lanci, sequenza, buffer ≥30gg)
        ├── consuma da: IB-L2-COMM (segnali community, domande, obiezioni post-vendita)
        └── riporta a: ib-director (propone next prodotto; escalation se trend cambia)
```

---

## Roster agenti (7)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `IB-COORD-STRATEGIA` | Capo Area Strategia | Opus | Coordinator: roadmap prodotti, analisi competitiva, propone next prodotto a ib-director, escalation trend |
| `IB-STRA-QA` | Verificatore Strategia | Sonnet | Gate "prove non inventate": nessuna raccomandazione senza dati; fonti citate; nessuna metrica stimata come reale |
| `IB-STRA-INTEL` | Market Intelligence Analyst | Sonnet | Trend mercato info-products AI; cosa vendono i competitor; angoli emergenti; ingest da 08-INTELLIGENCE |
| `IB-STRA-COMP` | Competitor Analyst | Sonnet | Audit periodico offerta competitor (corsi, ebook, prezzi, posizionamento); dossier per Director |
| `IB-STRA-BACKLOG` | Product Backlog Manager | Sonnet | Coda idee con score /100, stato (idea→validato→live), priorità |
| `IB-STRA-ICP` | ICP Profiler Info-Business | Sonnet | ICP specifico prodotti info (≠ ICP AGENCY); aggiorna con dati community e lanci |
| `IB-STRA-ROADMAP` | Roadmap Builder | Sonnet | Piano prodotti 6-12 mesi: dipendenze, sequenza lanci, capacità produzione; rivisto dopo ogni lancio |

---

## Workflow CF-grade (2)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-PRODUCT-INTELLIGENCE` | Alimenta il backlog con idee pre-validate da dati mercato + community + gap competitor → top idea approvata | `workflow/WF-PRODUCT-INTELLIGENCE.md` |
| `WF-ROADMAP-PRODOTTI` | Mantiene roadmap 6-12 mesi coerente con capacità produttiva e lanci pianificati | `workflow/WF-ROADMAP-PRODOTTI.md` |

---

## Sistema di scoring idee (5 criteri /100)

Ogni idea prodotto nel backlog riceve uno **score deterministico /100** su 5 criteri (20 punti ciascuno).
È il linguaggio comune tra STRA e PROD: lo score ≥60 è la soglia di pre-validazione per proporre al Director.

| # | Criterio | Peso | Cosa misura |
|---|---|---|---|
| 1 | **Domanda di mercato** | 0-20 | Segnali reali di domanda (volume ricerche, domande community, trend) — con fonte |
| 2 | **Gap competitor** | 0-20 | Quanto è scoperto: nessuno lo offre / mal servito vs. mercato saturo |
| 3 | **Fit con ICP** | 0-20 | Quanto risponde a un pain documentato dell'ICP info-business attuale |
| 4 | **Fattibilità produzione** | 0-20 | Materiale raw già posseduto, lead time stimato, complessità |
| 5 | **Potenziale revenue/strategico** | 0-20 | Prezzo sostenibile, ruolo (lead magnet/pagamento), cross-sell verso AGENCY |

**Soglie:** `<40` scartata · `40-59` parcheggiata (serve più evidenza) · `≥60` candidabile · `≥80` priorità alta.
Vedi `principi/PRINCIPI.md` (P3) e `agenti/ib-stra-backlog-product-backlog-manager.md` per lo scoring dettagliato.

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Idee backlog con score ≥60 | n. idee candidabili in coda (alimenta PROD) |
| Lead time intelligence → idea validata → produzione | giorni dal segnale mercato all'ingresso in WF-CORSO |
| % prodotti a roadmap che arrivano a lancio nei tempi | aderenza roadmap (no slittamenti silenziosi) |
| Aggiornamenti ICP per trimestre | n. revisioni profilo ICP con dati freschi (no ICP fossile) |

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| → IB-L2-PROD | Area Prodotto | Idea pre-validata (score ≥60, fonti, ICP fit) → input a WF-VALIDAZIONE |
| ← 08-INTELLIGENCE | Intelligence holding | Trend mercato, profili competitor, dati ricerca (delega ricerca pesante) |
| → IB-L2-LANC | Area Lancio | Roadmap lanci approvata: sequenza, buffer ≥30gg, dipendenze |
| ← IB-L2-COMM | Area Community | Segnali community: domande ricorrenti, obiezioni post-vendita, cross-sell |
| → ib-director | Director INFO-BUSINESS | Top idea per approvazione; roadmap trimestrale; alert cambio trend |

**Regola handoff:** nessuna idea passa a PROD senza score ≥60 **e** almeno una fonte reale che la sostiene
(gate IB-STRA-QA). Nessuna roadmap esce senza lead time stimato per ogni prodotto e buffer ≥30gg tra lanci.

---

## Escalation

- **Trend di mercato cambia in modo dirompente** (es.: nuovo formato prodotto domina, competitor lancia
  qualcosa che ridefinisce la categoria): IB-COORD-STRATEGIA escala a ib-director con dossier e proposta
  di ri-priorizzazione roadmap. Non aspetta il ciclo mensile.
- **Idea con score alto ma fonte debole:** IB-STRA-QA blocca. L'idea torna a IB-STRA-INTEL/COMP per
  evidenza reale prima di poter essere proposta. Score senza fonte = non candidabile.
- **Roadmap in conflitto con capacità produttiva** (PROD non riesce a sostenere il ritmo): IB-STRA-ROADMAP
  ricalcola con lead time reali, IB-COORD-STRATEGIA negozia priorità con ib-director. Mai roadmap che la
  produzione non può reggere.
- **Pressione a proporre un'idea "perché piace a qualcuno"** senza dati: si applica P2 (prove non opinioni).
  IB-COORD-STRATEGIA chiede l'evidenza; se non c'è, l'idea resta parcheggiata.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-STRA
- [[ARCHITETTURA]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-STRA-Strategia-Intelligence/ARCHITETTURA.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (prove non promesse, dati reali)
- [[08-INTELLIGENCE]] · `PIANO-MAESTRO/08-ROADMAP-FASI.md` (delega ricerca)
- [[WF-PRODUCT-INTELLIGENCE]] · `workflow/WF-PRODUCT-INTELLIGENCE.md`
- [[WF-ROADMAP-PRODOTTI]] · `workflow/WF-ROADMAP-PRODOTTI.md`
