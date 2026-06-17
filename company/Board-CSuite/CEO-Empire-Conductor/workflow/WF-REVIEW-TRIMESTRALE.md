---
Type: CONCEPT
Status: Active
Tags: #workflow #ceo #review #trimestrale #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-REVIEW-TRIMESTRALE — Workflow Review Trimestrale della Holding

> **Tipo:** CF-grade · **Figura:** CEO / Empire-Conductor
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CEO.md`
> **Connessioni:** [[WF-DECISIONE-STRATEGICA]] · [[WF-ARBITRATO-PRIORITA]] · [[12-DOSSIER-MAXIMILIAN]]

---

## Scopo

Produrre la diagnosi trimestrale dello stato della holding: raccogliere KPI e OKR da tutte le figure
C-Suite e dai 10 ecosistemi, valutare la performance del trimestre concluso, definire le priorità del
trimestre successivo, e emettere le direttive strategiche per il ciclo che inizia. Questo workflow è
il momento di governo più importante del ciclo trimestrale. Output: report holding trimestrale +
OKR del nuovo trimestre + direttive strategiche + ADR se necessario.

---

## Trigger

- Fine trimestre (Q1→Q2, Q2→Q3, Q3→Q4, Q4→Q1).
- Evento straordinario che richiede revisione urgente delle priorità (crisi, pivot, opportunità
  time-sensitive che cambia il piano del trimestre).

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `ceo-memoria` | 1, 9 | Load storico trimestre + write ADR/checkpoint finale |
| `ceo-conductor` | 1-9 | Orchestratore review; propone OKR nuovi; chiude direttive |
| `ceo-okr-tracker` | 2 | Raccoglie progress finale da tutti gli ecosistemi |
| `ceo-analista-strategico` | 3 | Analisi diagnosi: cosa ha funzionato, cosa no, trend |
| `ceo-advisor-rischi` | 4 | Rischi del trimestre successivo sulle priorità proposte |
| `ceo-advisor-opportunita` | 4 | Opportunità del trimestre successivo |
| `ceo-budget-allocator` | 5 | Proposta allocazione budget nuovo trimestre |
| `ceo-priorita-arbiter` | 6 | Se conflitti su priorità nuove tra ecosistemi |
| `ceo-comunicatore` | 8 | Dispatch OKR e direttive a tutti gli ecosistemi |
| `ceo-verificatore` | [setup] | Configura il monitoraggio per il nuovo trimestre |

---

## Flusso passo-passo

```
STEP 1 — CARICAMENTO STORICO TRIMESTRE
├─ ceo-memoria carica: STATO-EMPIRE + tutti i checkpoint del trimestre + ADR del periodo
├─ ceo-okr-tracker raccoglie progress FINALE da tutte le figure C-Suite e dai 10 ecosistemi
├─ Deadline raccolta: 3 giorni prima della sessione di review
├─ Ecosistemi che non rispondono: flaggati e contattati con urgenza
└─ Output: dossier KPI/OKR completo del trimestre + storico decisioni del periodo

STEP 2 — DIAGNOSI TRIMESTRE CONCLUSO
├─ ceo-analista-strategico analizza il dossier KPI/OKR:
│   - Quali OKR sono stati raggiunti, quali no, perché
│   - Pattern di successo: cosa ha funzionato sistematicamente
│   - Pattern di fallimento: cosa non ha funzionato e perché (dato, non opinione)
│   - Trend emergenti: cosa è cambiato rispetto al trimestre precedente
│   - Delta roadmap: siamo dove dovremmo essere rispetto al PIANO-MAESTRO/08-ROADMAP-FASI.md?
└─ Output: report diagnosi strutturato con finding e gap

STEP 3 — ANALISI PRIORITÀ NUOVO TRIMESTRE (parallelo)
├─ ceo-advisor-rischi: rischi delle opzioni di priorità per il trimestre successivo
├─ ceo-advisor-opportunita: opportunità e finestre temporali del trimestre successivo
├─ ceo-budget-allocator: bozza allocazione budget nuovo trimestre (in handoff col CFO)
└─ Output: profilo rischi + opportunità + proposta budget → al conductor

STEP 4 — PROPOSTA OKR E PRIORITÀ
├─ ceo-conductor formula la proposta di OKR per il nuovo trimestre:
│   - max 5-7 OKR per la holding (non per ogni ecosistema)
│   - Ogni OKR: descrizione, owner ecosistema, target misurabile (o stimato se nuovo)
│   - Ordine di priorità esplicito (non tutti uguale importanza)
├─ Allineamento con fasi roadmap corrente (PIANO-MAESTRO/08-ROADMAP-FASI.md)
└─ Output: proposta OKR + ordine priorità → Board C-Suite

STEP 5 — VOTO RAFT SUL PIANO TRIMESTRALE
├─ Board C-Suite vota la proposta OKR e le priorità
├─ Ogni figura C-Suite può proporre modifiche prima del voto
├─ Voto: favorevoli/contrari/astenuti; stallo → voto decisivo conductor
├─ Gate Mandato: il piano trimestrale non può violare Articoli LX
└─ Output: piano trimestrale approvato + esito voto

STEP 6 — REVISIONE STRUTTURALE (se necessario)
├─ Se la diagnosi rivela problemi strutturali (non solo operativi): si apre un mini-ciclo
│   WF-DECISIONE-STRATEGICA per affrontarli prima di chiudere la review
├─ Esempi: un ecosistema sistematicamente fuori OKR → decisione su ri-design o resourcing
├─ Conduzione: ceo-priorita-arbiter se conflitto; ceo-analista-strategico se analisi
└─ Output: decisioni strutturali addizionali (con ADR se architetturali)

STEP 7 — GATE MANDATO
├─ Il piano trimestrale e le direttive passano il gate LX
├─ Bloccante: nessuna direttiva parte senza pass
└─ Output: mandato_gate pass / blocked

STEP 8 — DISPATCH E CHIUSURA
├─ ceo-comunicatore: costruisce e dispatcha i pacchetti OKR + direttive a tutti gli ecosistemi
├─ Ogni ecosistema riceve: i propri OKR assegnati + priorità + budget envelope + AC
├─ ceo-verificatore: configura il piano di monitoraggio per il nuovo trimestre
├─ ceo-okr-tracker: inizializza il registro OKR del nuovo trimestre in state
├─ ceo-memoria:
│   - Scrive checkpoint "Review Trimestrale Q_-YYYY" in Memory/checkpoints/
│   - Scrive ADR se ci sono decisioni architetturali emerse dalla review
│   - Aggiorna STATO-EMPIRE: "RIPRESA DA: Q_-YYYY avviato; OKR definiti"
└─ Output finale: report trimestrale + OKR nuovo trimestre + checkpoint + direttive dispatched

STEP 9 — REVIEW MAXIMILIAN (passo 5-bis se scala)
├─ Se il piano trimestrale implica decisioni di scala o di standard (nuovo ecosistema, cambio
│   architettura, standard CF-grade applicati per la prima volta): MAXIMILIAN fa review
├─ Domanda: "Questo piano trimestrale è abbastanza ambizioso? È millimetrico?"
└─ Output: APPROVA / RIFAI + motivo
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Dossier completo | Step 1 | Bloccante | KPI/OKR ricevuti da ≥80% degli ecosistemi |
| Proposta OKR non nulla | Step 4 | Bloccante | ≥3 OKR per la holding nel piano |
| Quorum voto | Step 5 | Bloccante | Voto Board con quorum |
| Mandato gate | Step 7 | Bloccante | Piano non viola Articoli LX |
| MAXIMILIAN review | Step 9 | Condizionale | Solo se decisioni di scala |

---

## Input del workflow

```json
{
  "trimestre_concluso": "Q1-2026 | Q2-2026 | ...",
  "dossier_kpi_ecosistemi": {},
  "checkpoint_periodo": ["CP-20260101-001", "CP-20260115-002"],
  "roadmap_fase_corrente": "F2 | F3 | ...",
  "trigger": "fine_trimestre | evento_straordinario"
}
```

## Output del workflow

```json
{
  "report_diagnosi": "sintesi trimestre concluso",
  "okr_nuovo_trimestre": [
    {"id": "OKR-Q3-01", "descrizione": "string", "owner": "ecosistema", "target": "string"}
  ],
  "priorita_ordinate": ["OKR-Q3-01", "OKR-Q3-02"],
  "direttive_dispatched": ["HC-CEO-ECOSISTEMA-NNN"],
  "adr_prodotti": ["ADR-NNN | null"],
  "checkpoint_scritto": "CP-YYYYMMDD-NNN",
  "maximilian_review": "approvato | rifai | non_richiesta"
}
```

---

## State

Il workflow usa lo state `board/ceo/okr-trimestre` per il tracking degli OKR e
`board/ceo/direttive-dispatch` per le direttive trimestrali. Al termine della review,
lo state del trimestre concluso viene archiviato in `ceo-memoria` e inizializzato il nuovo.

---

## Connessioni

- [[ceo-okr-tracker]] · `agenti/ceo-okr-tracker.md`
- [[ceo-analista-strategico]] · `agenti/ceo-analista-strategico.md`
- [[WF-DECISIONE-STRATEGICA]] · `workflow/WF-DECISIONE-STRATEGICA.md`
- [[SKILLS]] · `skills/SKILLS.md` (skill okr-tracker)
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[08-ROADMAP-FASI]] · `PIANO-MAESTRO/08-ROADMAP-FASI.md`
