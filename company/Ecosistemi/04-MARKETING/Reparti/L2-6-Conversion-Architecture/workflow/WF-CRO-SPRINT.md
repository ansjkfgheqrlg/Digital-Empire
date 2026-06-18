---
Type: WORKFLOW
Status: Active
Tags: #workflow #cro #sprint #ottimizzazione #ab-test #drop-rate #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-CRO-SPRINT — Sprint di Ottimizzazione Conversione

> **ID:** WF-CA-002 · **Owner:** `conv-lead` + `ca4-cro-sprint-lead`
> **Reparto:** L2.6 Conversion Architecture
> **Trigger:** segnale di drop da AN5 (L2.4) o raccomandazione CA-QA post-audit

---

## Scopo

Eseguire un ciclo completo di ottimizzazione su un funnel o landing page live:
diagnosi del collo di bottiglia (AN5) → ipotesi (CA4) → variante (L2.1 per il copy,
06-PLATFORM per la struttura) → test A/B con dimensione statistica validata (AN3)
→ verdetto → implementazione del winner. L'obiettivo è migliorare il conversion rate
su uno specifico step del funnel con un intervento chirurgico, non una redesign.

**Regola fondamentale:** nessuna implementazione senza verdetto statisticamente valido.
Un test con verdetto "inconclusivo" è comunque un'informazione: si registra il learning,
non si implementa nulla.

---

## Attori

| Step | Agente L2.6 | Agente/Reparto esterno |
|---|---|---|
| Segnale drop | — | AN5 (L2.4) |
| Diagnosi | `conv-lead` + `ca4-cro-sprint-lead` | CA3 (schema diagnosi) |
| Variante copy | `ca4-cro-sprint-lead` (brief) | L2.1: A6/A7/A3/A8 per copy variante |
| Variante strutturale | `ca4-cro-sprint-lead` (brief) | 06-PLATFORM |
| Dimensionamento test | — | AN3 (L2.4/WF-AB-TEST) |
| Esecuzione test | — | AN3 + 06-PLATFORM (implementazione variante) |
| Verdetto | — | AN3 (L2.4) |
| Implementazione winner | `ca4-cro-sprint-lead` (coordinamento) | 06-PLATFORM |
| Gate finale | `ca-qa-conversion-verifier` | — |

---

## Flusso passo-passo

```
[TRIGGER]
AN5 (L2.4) → drop report:
  {funnel_id, landing_id, drop_punto, drop_rate, sezione_APSOC_correlata}
  oppure
CA-QA → raccomandazione post-audit WF-LANDING-AUDIT
         │
         ▼
[STEP 1] CONV-LEAD + CA4 — pre-screening
  → il drop è statisticamente significativo? (sufficiente traffico per distinguere segnale da rumore)
  → GATE-1: traffico sufficiente → prosegui; insufficiente → segnala a committente "sprint prematuro,
    raccogliere più dati prima di ottimizzare"; non si avvia sprint su rumore

         │
         ▼
[STEP 2] CA4 — diagnosi collo di bottiglia
  → legge schema CA3 per identificare la coppia evento-evento con drop
  → mappa il drop su sezione APSOC:
    - drop hero → A (Attenzione) debole
    - drop proof/soluzione → S debole (o P non ha preparato bene)
    - drop CTA → O (Obiezioni) non gestite o CTA debole
    - drop checkout → attrito tecnico fuori da L2.6 (→ 06-PLATFORM)
  → formula ipotesi specifica e falsificabile
  → identifica elemento da testare (UNO per variante — regola anti-deriva)

         │
         ▼
[STEP 3] CA4 — disegno variante
  → specifica: elemento che cambia + ipotesi del perché migliora
  → se elemento = copy:
      brief a L2.1: formato, sezione APSOC, obiettivo, copy esistente da migliorare
      → L2.1 produce variante gated (G1 ≥80)
  → se elemento = struttura/posizione CTA/form:
      brief tecnico a 06-PLATFORM per implementazione variante
  → GATE-2: variante pronta (copy gated O brief tecnico approvato) → prosegui

         │
         ▼
[STEP 4] AN3 (L2.4/WF-AB-TEST) — dimensionamento e disegno test
  → riceve: controllo + variante + metrica primaria + criterio verdetto pre-definito
  → calcola: dimensione campione necessaria per p-value <0.05
  → verifica: il traffico attuale raggiunge la dimensione in un tempo ragionevole?
  → GATE-3: dimensione raggiungibile → avvia test; non raggiungibile in tempi utili →
    report a CONV-LEAD: "test non conveniente, traffico troppo basso; alternativa: audit"

         │
         ▼
[STEP 5] Test A/B in esecuzione
  → 06-PLATFORM implementa la variante (se strutturale) o aggiorna il copy
  → test live: controllo vs variante, traffico splitato 50/50
  → NESSUNA modifica durante il test (regola anti-contaminazione)
  → AN3 monitora il raggiungimento del criterio

         │
         ▼
[STEP 6] AN3 — verdetto
  → criterio raggiunto (dimensione campione + p-value <0.05)?
      WINNER IDENTIFICATO: variante o controllo
  → criterio non raggiunto dopo tempo massimo pianificato?
      INCONCLUSIVO: il test non ha abbastanza potenza per distinguere

         │
   ┌─────┴──────────┐
WINNER           INCONCLUSIVO
   │                 │
   ▼                 ▼
[STEP 7a]       [STEP 7b]
Implementazione  Learning registrato:
winner via       "elemento X non distinguibile
06-PLATFORM      con traffico Y su metrica Z"
                 Non si implementa nulla.
   │             Prossima ipotesi o wait.
   ▼
CA4 archivia sprint:
marketing/cro/sprints/{sprint_id}
con campo verdetto popolato
         │
         ▼
[STEP 8] CA-QA — verifica implementazione
  → il winner è stato implementato correttamente?
  → la struttura APSOC è ancora coerente dopo la modifica?
  → GATE-4: PASS → sprint chiuso; FAIL → CA4 coordina correzione con 06-PLATFORM
         │
         ▼
AN5 (L2.4) — misurazione post-implementazione
  → raccoglie metriche sul winner implementato
  → confronta con baseline pre-sprint
  → risultato nello state del funnel
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Traffico sufficiente | Dimensione campione raggiungibile; no sprint su rumore | CA4 + AN3 | Avvio sprint |
| G2 — Variante pronta | Copy gated G1 ≥80 O brief tecnico approvato | A8 (L2.1) / CA4 | Disegno test AN3 |
| G3 — Dimensione campione validata da AN3 | Campione sufficiente per p-value <0.05 | AN3 (L2.4) | Avvio test A/B |
| G4 — Implementazione verificata da CA-QA | Winner implementato + APSOC coerente | CA-QA | Chiusura sprint |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "sprint_trigger": "drop_report",
  "funnel_id": "FUNNEL-001",
  "landing_id": "LP-BOFU-001",
  "drop_report": {
    "fonte": "AN5",
    "drop_punto": "scroll_75 → cta_hover",
    "sezione_APSOC": "O — Obiezioni",
    "traffico_settimana": "[DM]"
  }
}
```

**Output finale (winner):**
```json
{
  "sprint_id": "SPRINT-001",
  "funnel_id": "FUNNEL-001",
  "landing_id": "LP-BOFU-001",
  "collo_di_bottiglia": "Sezione O: 2 obiezioni su 5 gestite",
  "variante": "sezione obiezioni ampliata con CPB per obiezione 'non ho tempo' e 'funziona per me?'",
  "verdetto": "winner variante",
  "metrica_migliorata": "cta_click rate",
  "delta": "[DM] — da AN5 post-implementazione",
  "implementato": true,
  "namespace": "marketing/cro/sprints/SPRINT-001"
}
```

**Output finale (inconclusivo):**
```json
{
  "sprint_id": "SPRINT-001",
  "verdetto": "inconclusivo",
  "motivo": "campione troppo basso per distinguere la differenza con p<0.05",
  "learning": "obiezione 'non ho tempo' da testare su campione maggiore in Q3",
  "implementato": false,
  "namespace": "marketing/cro/sprints/SPRINT-001"
}
```

---

## State

File: `marketing/cro/sprints/{sprint_id}.json`
- Creato all'avvio dello sprint.
- Campo `verdetto` OBBLIGATORIO alla chiusura: "winner variante" / "winner controllo" / "inconclusivo".
- Sprint senza `verdetto` = sprint non chiuso = KPI anomalia.

---

## Connessioni

- [[ca4-cro-sprint-lead]] · `agenti/ca4-cro-sprint-lead.md`
- [[ca-qa-conversion-verifier]] · `agenti/ca-qa-conversion-verifier.md`
- [[WF-FUNNEL-DESIGN]] · `workflow/WF-FUNNEL-DESIGN.md` — funnel su cui si opera
- [[WF-LANDING-AUDIT]] · `workflow/WF-LANDING-AUDIT.md` — audit che genera i trigger
- [[L2-4-Analytics]] · AN5 (drop rate) + AN3 (WF-AB-TEST) — partner analitici obbligatori
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.6 WF-CRO-SPRINT`
