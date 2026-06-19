---
Type: WORKFLOW
Status: Active
Tags: #workflow #ab-test #esperimento #statistica #verdetto #analytics #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-AB-TEST — Disegno ed Esecuzione Esperimento A/B

> **ID:** WF-AN-003 · **Owner:** `an3-experiment-designer` · **Reparto:** L2.4 Analytics & Ottimizzazione
> **Trigger:** diagnosi di sezione APSOC debole (da WF-OPTIMIZATION-LOOP passo 5) o richiesta
> diretta da L2.2 (test creativo) o L2.3 (test oggetto email)

---

## Scopo

Progettare, eseguire e chiudere un esperimento A/B con rigore statistico:
ipotesi falsificabile, dimensione campione calcolata prima del lancio, criterio di
verdetto predefinito e fisso, verdetto emesso solo a campione raggiunto.

Se il campione non è raggiunto entro la deadline il verdetto è "INCONCLUSIVO" —
mai forzato. L'inconclusivo è un'informazione valida: il test era troppo piccolo
per quella differenza, o la differenza attesa non si è materializzata.

**Gate d'uscita:** verdetto emesso con criterio soddisfatto O esito "INCONCLUSIVO" con
spiegazione. Esito archiviato in `marketing/ads/experiments/{test_id}`.

---

## Attori

| Step | Agente | Responsabilità |
|---|---|---|
| Richiesta | `an-lead` (da loop) o reparto richiedente (L2.2/L2.3) | Brief del test |
| Disegno esperimento | `an3-experiment-designer` | Ipotesi, varianti, campione, criterio |
| Lancio | AD3 (L2.2) per ads / EMAIL-LEAD (L2.3) per email | Esecuzione tecnica |
| Monitoraggio soglia | `an3-experiment-designer` | Verifica campione raggiunto |
| Verdetto | `an3-experiment-designer` | Emissione verdetto strutturato |
| Archivio | `an4-insight-distiller` | Distillazione se verdetto PASS |

---

## Flusso passo-passo

```
[TRIGGER]
Brief test → AN3
  {ipotesi, varianti (max 3), metrica primaria, traffico stimato, deadline}
        │
        ▼
[STEP 1] AN3 — formulazione ipotesi
  → ipotesi falsificabile: "se cambio X in Y, la metrica M aumenta di Z%"
  → metrica primaria scelta (una sola — no multitest senza correzione)
  → varianti definite (max 3; sopra 3 → sequenziare i test)
  → GATE-1: ipotesi formulata → prosegui

        │
        ▼
[STEP 2] AN3 — calcolo dimensione campione
  → input: tasso base attuale, differenza attesa, confidenza (≥90%), power (≥80%)
  → calcolo campione minimo per variante
  → stima giorni: (campione_per_variante × n_varianti) / traffico_giornaliero_stimato
  → traffico sufficiente entro deadline? → SÌ: procedi; NO: segnala 3 opzioni ad AN-LEAD
    (a) prolungare test, (b) ridurre varianti, (c) accettare power inferiore con nota)
  → GATE-2: campione fattibile entro deadline → prosegui

        │
        ▼
[STEP 3] AN3 — definizione criterio di verdetto
  → criterio fisso PRIMA del lancio (non modificabile post-lancio):
    standard veloce (CTR): p-value < 0.10 con campione raggiunto
    standard preciso (sales page, prezzi): p-value < 0.05 con campione raggiunto
  → criterio scritto nel record del test
  → GATE-3: criterio definito → prosegui

        │
        ▼
[STEP 4] Lancio
  → AN3 consegna brief a AD3 (L2.2) o EMAIL-LEAD (L2.3) per lancio tecnico
  → split 50/50 (o distribuzione definita se n varianti > 2)
  → data lancio + campione target registrati in state

        │
        ▼
[STEP 5] AN3 — monitoraggio (no peeking)
  → unica verifica a metà periodo: check tecnico (eventuali 0 conversioni = bug)
  → attende il raggiungimento del campione PRIMA di leggere i risultati finali
  → campione raggiunto? → procedi al verdetto; non raggiunto a deadline? → INCONCLUSIVO

        │
        ▼
[STEP 6] AN3 — verdetto
  → legge i risultati completi a campione raggiunto
  → calcola p-value sulla metrica primaria
  → criterio soddisfatto? → PASS: winner identificato con confidence interval
  → criterio non soddisfatto → INCONCLUSIVO: "differenza non statisticamente significativa
    con campione raggiunto" (non "X è meglio" senza evidenza)
  → GATE-4: verdetto con dati → archivio

        │
        ▼
[STEP 7] Archivio e handoff
  → record test archiviato in marketing/ads/experiments/{test_id}
  → verdetto PASS → handoff ad AN4 per distillazione pattern
  → verdetto INCONCLUSIVO → nota in state: "ipotesi non confermata con questo campione"
  → entry in wiki/log.md se il test è parte di un ciclo WF-OPTIMIZATION-LOOP
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G1 — Ipotesi formulata | Ipotesi falsificabile con metrica primaria dichiarata | AN3 | Avvio calcolo campione |
| G2 — Campione fattibile | Traffico sufficiente per campione entro deadline (o opzioni alternate accettate) | AN3 | Lancio |
| G3 — Criterio definito | Criterio di verdetto scritto nel record PRIMA del lancio | AN3 | Lancio |
| G4 — Verdetto con dati | p-value calcolato su campione raggiunto (o INCONCLUSIVO documentato) | AN3 | Distillazione pattern |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "test_id": "EXP-002",
  "contesto": "LOOP-001 — passo 5",
  "ipotesi": "hook benefit numerico ha CTR superiore a hook problema per ICP freelance-digitale-ita",
  "varianti": [
    {"id": "A", "copy_id": "CP-001", "descrizione": "hook problema (controllo)"},
    {"id": "B", "copy_id": "CP-001-revised", "descrizione": "hook benefit numerico (variante)"}
  ],
  "metrica_primaria": "CTR",
  "tasso_base_attuale": 0.009,
  "differenza_attesa": 1.5,
  "traffico_giornaliero_stimato": 600,
  "deadline": "2026-07-05"
}
```

**Output finale:**
```json
{
  "test_id": "EXP-002",
  "campione_per_variante": 980,
  "giorni_stimati": 3.3,
  "criterio_verdetto": "p-value < 0.10 su CTR, campione ≥ 980 per variante",
  "data_lancio": "2026-06-25",
  "data_verdetto": "2026-06-29",
  "risultati": {
    "A_CTR": 0.009,
    "B_CTR": 0.027,
    "p_value": 0.021,
    "campione_A": 1040,
    "campione_B": 1015
  },
  "verdetto": "PASS",
  "winner": "B",
  "confidence": "statisticamente significativo — p < 0.05 (soglia 0.10 soddisfatta con ampio margine)",
  "namespace_archiviazione": "marketing/ads/experiments/EXP-002"
}
```

---

## Gestione del risultato INCONCLUSIVO

Quando il campione è raggiunto ma il criterio non è soddisfatto:
- Si documenta il risultato osservato con confidence interval.
- Si specifica il motivo: "differenza reale inferiore a quella attesa" O "variabilità
  troppo alta per questo campione".
- Si indicano le opzioni: (a) prolungare con campione maggiore, (b) ridurre la differenza
  attesa nella prossima ipotesi, (c) abbandonare questa direzione di test.
- Mai si scrive "B è leggermente migliore quindi usiamo B": se il criterio non è soddisfatto,
  non si dichiara un winner.

---

## State

File: `marketing/ads/experiments/{test_id}/state.json`
- Campi: ipotesi, varianti, campione_target, criterio_verdetto, data_lancio,
  campione_raggiunto, data_verdetto, verdetto, winner, p_value.
- Ripartibile a freddo: AN3 può verificare lo stato del test in qualsiasi momento.

---

## Connessioni

- [[an3-experiment-designer]] · `agenti/an3-experiment-designer.md`
- [[an4-insight-distiller]] · `agenti/an4-insight-distiller.md` — riceve verdetti PASS
- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md` — passo 5
- [[L2-2-Advertising]] · AD3 esegue il lancio tecnico per test ads
- [[L2-3-Email-Lifecycle]] · EMAIL-LEAD esegue il lancio per test email
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.4`
