---
Type: CONCEPT
Status: Active
Tags: #workflow #info-business #strategia #intelligence #backlog #IB-L2-STRA
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-PRODUCT-INTELLIGENCE — Product Intelligence

> **Workflow:** WF-PRODUCT-INTELLIGENCE · **Reparto:** IB-L2-STRA Strategia & Intelligence
> **Cadenza:** mensile (+ trigger on-demand per eventi di mercato)
> **Output:** backlog aggiornato + top idea approvata per WF-VALIDAZIONE (IB-L2-PROD)
> **Gate di uscita:** IB-STRA-QA — nessuna idea passa senza fonte reale che la supporta

---

## Scopo

Alimentare continuamente il product backlog con idee **pre-validate** basate su dati di mercato, pattern
community e gap competitor. L'Area Prodotto non dovrebbe mai cercare idee: le riceve già qualificate da
questo workflow. È il motore che fa evolvere INFO-BUSINESS col mercato anziché rincorrerlo.

**Pre-validazione ≠ validazione.** Questo workflow porta un'idea con score ≥60 e fonti reali fino alla
proposta al Director. La validazione formale (test mercato, smoke test, go/no-go) è di IB-L2-PROD a valle.

---

## Trigger

- **Programmato:** ciclo mensile (es.: primo lunedì del mese).
- **On-demand:** evento di mercato rilevante — un competitor lancia un game-changer, un formato esplode,
  un picco di domanda community su un tema. Innescato da IB-STRA-INTEL o IB-STRA-COMP via alert al Coordinator.

---

## Input JSON

```json
{
  "trigger": "ciclo_mensile | evento_mercato",
  "periodo": "2026-06",
  "focus": "generale | tema_specifico",
  "fonti_disponibili": ["08-INTELLIGENCE", "community_log", "newsletter_settore", "social"],
  "segnali_community": ["domande ricorrenti, obiezioni post-vendita (da IB-L2-COMM)"],
  "backlog_corrente": "infobusiness/strategia/backlog/idee.json",
  "deadline": "YYYY-MM-DD"
}
```

---

## Pipeline (step + owner)

```
[1] IB-STRA-INTEL — scan trend                                          (owner: IB-STRA-INTEL)
  → fonti: 08-INTELLIGENCE (ricerca delegata), community, newsletter, social
  → identifica 3-5 temi emergenti nel mercato info-products AI, ognuno con fonte e forza segnale
  → output: trend_YYYYMM.md → handoff a [2] e [4]

[2] IB-STRA-COMP — audit competitor + gap analysis                      (owner: IB-STRA-COMP)
  → input: temi da [1] + lista competitor
  → audit offerta competitor: nuovi prodotti, pricing, posizionamento (ogni dato con fonte+data)
  → gap analysis: cosa non offrono che il nostro ICP chiede?
  → output: dossier_YYYYMM.md + gap_analysis → handoff a [3] e [4]

[3] IB-STRA-ICP — aggiorna profilo ICP                                  (owner: IB-STRA-ICP)
  → input: segnali community (domande, cross-sell, obiezioni post-vendita) + gap da [2]
  → aggiorna profilo ICP con dati freschi → identifica pain points non ancora coperti dai prodotti attuali
  → output: icp_infobusiness.md aggiornato + pain_scoperti → handoff a [4]

[4] IB-STRA-BACKLOG — integra + scoring                                 (owner: IB-STRA-BACKLOG)
  → input: trend [1] + gap [2] + pain ICP [3]
  → genera bozze idea prodotto con score /100 su 5 criteri (ogni punto con fonte)
  → aggiorna backlog/idee.json (idempotente: aggiorna esistenti, non duplica)
  → output: top 3 idee candidabili (≥60) → handoff a [5]

[5] IB-STRA-QA — GATE "prove non inventate"                             (owner: IB-STRA-QA)
  → verifica: ogni claim ha fonte citata? nessuna metrica inventata? score giustificato dai dati?
  → PASS → procede a [6] · FAIL → torna allo specialista responsabile del difetto

[6] IB-COORD-STRATEGIA — proposta a Director                           (owner: IB-COORD-STRATEGIA)
  → sintetizza la top idea in one-pager (cosa, perché ora, per chi, gap, lead time, ruolo)
  → presenta a ib-director → se approved: handoff HC-STRA-PROD-01 → WF-VALIDAZIONE (IB-L2-PROD)
```

---

## Gate

| Gate | Step | Chi | Criteri |
|---|---|---|---|
| **G-FONTI** (bloccante) | [5] | IB-STRA-QA | Ogni claim a supporto dell'idea ha fonte reale dichiarata (URL/screenshot/log+data) |
| **G-METRICHE** (bloccante) | [5] | IB-STRA-QA | Nessuna metrica stimata presentata come reale; stime etichettate [stima]/[DM] |
| **G-SCORE** | [5] | IB-STRA-QA | Lo score riflette i dati citati, non è gonfiato rispetto all'evidenza |
| **G-APPROVAZIONE** | [6] | ib-director | La top idea è approvata per entrare in WF-VALIDAZIONE |

**Regola del gate (dal dossier):** *nessuna idea passa senza fonte reale che la supporta.* Il gate G-FONTI
è il cuore dell'area: la differenza tra "idea pre-validata" e "opinione" è la fonte.

---

## Output JSON

```json
{
  "workflow": "WF-PRODUCT-INTELLIGENCE",
  "periodo": "2026-06",
  "backlog_aggiornato": {
    "idee_nuove": 4,
    "idee_candidabili_ge60": 3,
    "path": "infobusiness/strategia/backlog/idee.json"
  },
  "top_idea": {
    "idea_id": "IDEA-012",
    "titolo": "Mini-corso 'Claude Code per consulenti'",
    "score": 82,
    "fonti": ["trend_202606.md", "dossier_202606.md", "community_log_47richieste"],
    "qa_gate": "PASS",
    "stato": "approvata_da_director | proposta | rimandata"
  },
  "handoff": "HC-STRA-PROD-01 → IB-L2-PROD (WF-VALIDAZIONE)",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

---

## Handoff

| Contract | Da → A | Payload | Quando |
|---|---|---|---|
| `HC-INT-STRA-01` | 08-INTELLIGENCE → IB-STRA-INTEL/COMP | dataset trend/competitor + fonti | step [1]-[2] |
| `HC-COMM-STRA-01` | IB-L2-COMM → IB-STRA-ICP | segnali community (domande, obiezioni) | step [3] |
| `HC-STRA-PROD-01` | IB-COORD-STRATEGIA → IB-L2-PROD | idea pre-validata (score ≥60 + fonti + ICP fit) | step [6], se approvata |

**Payload HC-STRA-PROD-01:** `{idea_id, titolo, formato, ruolo, score_breakdown[5], fonti[], icp_target,
gap_competitor, lead_time_stimato}`. Acceptance: score ≥60, ≥1 fonte reale, QA PASS, approvazione Director.

---

## Dry-run

**Scenario:** ciclo mensile giugno 2026, nessun prodotto nuovo in catalogo dal mese scorso.

1. **[1] INTEL** delega a 08-INTEL → riceve dati su 3 lanci competitor + picco ricerche "agenti AI italiano".
   Produce `trend_202606.md`: tema forte "AI operativa no-code per micro-business" (2 fonti convergenti).
2. **[2] COMP** audita 5 competitor → 3 offrono corsi AI generici (€97-297), nessuno verticale per
   consulenti in IT. Gap analysis: "corso AI per consulenti IT" = gap ALTO. Un prezzo `[non rilevato]`.
3. **[3] ICP** integra 47 domande community → pain "automazione delivery per consulenti" confermato,
   nessun prodotto lo copre. ICP aggiornato a v1.3.
4. **[4] BACKLOG** crea IDEA-012 → scoring: domanda 18, gap 18, fit 17, fattibilità 16, revenue 13 =
   **82, priorità alta**. Ogni punto ancorato a fonte. Top 3: IDEA-012, IDEA-008, IDEA-015.
5. **[5] QA** verifica IDEA-012 → ogni claim ha fonte, nessuna metrica inventata, score giustificato → **PASS**.
   (IDEA-015 aveva un "potenziale 1500 lead" non etichettato → FAIL, tornata a BACKLOG, esclusa dalla proposta).
6. **[6] COORD** one-pager IDEA-012 a ib-director → approvata → HC-STRA-PROD-01 a IB-L2-PROD.
   Output JSON registrato. Backlog: IDEA-012 stato "in-validazione". Log in wiki.

**Esito dry-run:** 1 idea approvata, 1 bocciata al gate (correttamente), backlog cresciuto di 4 idee. Gate funzionante.

---

## Connessioni

- [[ib-coord-strategia]] · `agenti/ib-coord-strategia.md`
- [[ib-stra-intel-market-intelligence-analyst]] · `agenti/ib-stra-intel-market-intelligence-analyst.md`
- [[ib-stra-comp-competitor-analyst]] · `agenti/ib-stra-comp-competitor-analyst.md`
- [[ib-stra-icp-profiler]] · `agenti/ib-stra-icp-profiler.md`
- [[ib-stra-backlog-product-backlog-manager]] · `agenti/ib-stra-backlog-product-backlog-manager.md`
- [[ib-stra-qa-verificatore-strategia]] · `agenti/ib-stra-qa-verificatore-strategia.md`
- [[WF-ROADMAP-PRODOTTI]] · `workflow/WF-ROADMAP-PRODOTTI.md`
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-STRA
