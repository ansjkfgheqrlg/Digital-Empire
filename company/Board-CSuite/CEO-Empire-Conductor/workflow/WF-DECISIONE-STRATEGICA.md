---
Type: CONCEPT
Status: Active
Tags: #workflow #ceo #decisione #strategica #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-DECISIONE-STRATEGICA — Workflow Decisione Strategica Cross-Ecosistema

> **Tipo:** CF-grade · **Figura:** CEO / Empire-Conductor
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CEO.md`
> **Connessioni:** [[WF-ARBITRATO-PRIORITA]] · [[WF-REVIEW-TRIMESTRALE]] · [[12-DOSSIER-MAXIMILIAN]]

---

## Scopo

Produrre decisioni cross-ecosistema valide, documentate e dispatchate. Ogni decisione che tocca 2+
ecosistemi, supera il budget autorizzato, richiede deroga a un gate, o ha impatto architetturale deve
passare per questo workflow. Output: decisione con rationale + voto raft + ADR/checkpoint + direttive
eseguibili con acceptance criteria.

---

## Trigger

- Escalation da qualsiasi ecosistema L1 o figura C-Suite con questione cross-ecosistema.
- Alert CFO (Cost-Sentinel) su superamento envelope.
- Alert `ceo-verificatore` su non-esecuzione di direttiva critica.
- Review periodica (da WF-REVIEW-TRIMESTRALE) che produce decisioni di priorità.
- Proposta di nuovo ecosistema o team L1 (via Chief-Forge).

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `ceo-memoria` | 1, 9 | Load contesto in apertura; write checkpoint in chiusura |
| `ceo-conductor` | 1-9 | Orchestratore; propone e chiude il voto; gate Mandato |
| `ceo-analista-strategico` | 3 | Mappa scenari e opzioni (3-5) |
| `ceo-advisor-rischi` | 4 | Mappa rischi per scenario (parallelo) |
| `ceo-advisor-opportunita` | 4 | Mappa opportunità per scenario (parallelo) |
| `ceo-budget-allocator` | 5 | Dry-run economico se impatto su spesa |
| `ceo-priorita-arbiter` | 6 | Arbitra se conflitto risorse tra ecosistemi |
| `ceo-comunicatore` | 8 | Dispatch direttive post-gate |
| `ceo-verificatore` | [async] | Monitora esecuzione direttive post-dispatch |

---

## Flusso passo-passo

```
STEP 1 — RICEZIONE E MEMORY-FIRST
├─ ceo-memoria carica: STATO-EMPIRE + ADR attivi + checkpoint recenti
├─ ceo-conductor riceve l'input strutturato
├─ dedup check: questa questione è già stata decisa? Sì → applica ADR, stop
└─ Output: brief di contesto + flag se questione nuova

STEP 2 — ISTRUTTORIA MANDATO (pre-screening)
├─ ceo-conductor verifica: la proposta contraddice un Articolo LX?
│   Sì → respinta o convertita in proposta ADR per Max (escalation)
│   No → procede a Step 3
└─ Output: go/no-go pre-analisi

STEP 3 — ANALISI SCENARI
├─ ceo-analista-strategico mappa 3-5 scenari con trade-off
├─ Identifica flag rischi e flag opportunità per i passi paralleli
└─ Output: brief scenari JSON → al conductor + ai due advisor

STEP 4 — ANALISI RISCHI E OPPORTUNITÀ (in parallelo)
├─ ceo-advisor-rischi: mappa rischi per scenario (tipo, probabilità, impatto, mitigazioni)
├─ ceo-advisor-opportunita: mappa upside per scenario (impatto, finestra, sinergie)
└─ Output: mappa-rischi + mappa-opportunità → al conductor

STEP 5 — DRY-RUN ECONOMICO (se applicabile)
├─ Se la decisione implica spesa: ceo-budget-allocator contatta CFO per envelope
├─ CFO risponde go/no-go sull'envelope
├─ Se no-go CFO: conductor non procede al voto (pending CFO go)
└─ Output: dry-run economico con stato envelope

STEP 6 — SINTESI E PROPOSTA
├─ ceo-conductor sintetizza: analisi + rischi + opportunità + budget
├─ Se conflitto risorse tra ecosistemi: ingaggia ceo-priorita-arbiter
├─ Produce la proposta di decisione con rationale esplicito
└─ Output: proposta unica + rationale → Board C-Suite

STEP 7 — VOTO RAFT
├─ ceo-conductor propone al Board (C-Suite rilevante per il dominio)
├─ Raccoglie voti: favorevoli / contrari / astenuti
├─ Verifica quorum (Council.md)
├─ Stallo → voto decisivo del conductor
└─ Output: esito voto {favorevoli, contrari, astenuti, esito}

STEP 8 — GATE MANDATO (LX)
├─ Ogni decisione passa il gate LX prima del dispatch
├─ Gate BLOCCANTE: nessuna direttiva parte senza pass
├─ Pass → procede a Step 9
│   Fail → decisione bloccata o convertita in proposta ADR per Max
└─ Output: mandato_gate: "pass | blocked | deroga_richiesta"

STEP 9 — DISPATCH E DOCUMENTAZIONE
├─ ceo-comunicatore: costruisce handoff contract per ogni destinatario
├─ Dispatch sul bus corporativo (type: directive)
├─ ceo-memoria: scrive checkpoint CP-YYYYMMDD-NNN + aggiorna STATO-EMPIRE
├─ Se decisione architetturale: ceo-memoria scrive ADR draft → conductor firma
├─ ceo-verificatore: prende in carico il monitoraggio delle direttive [async]
└─ Output finale: decisione tracciata + checkpoint + direttive dispatched
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Dedup gate | Step 1 | Bloccante | Questione non già decisa in ADR |
| Mandato pre-screen | Step 2 | Bloccante | Proposta non contraddice Articoli LX |
| CFO envelope gate | Step 5 | Bloccante (se spesa) | CFO conferma go sull'envelope |
| Quorum gate | Step 7 | Bloccante | Voto con quorum (o decisivo conductor) |
| Mandato dispatch gate | Step 8 | Bloccante | Gate LX pass prima di ogni dispatch |

---

## Input del workflow

```json
{
  "tipo": "decisione_cross | conflitto | escalation | deroga_gate | review_strategica",
  "ecosistemi_coinvolti": ["string"],
  "contesto": "string",
  "urgenza": "alta | media | bassa",
  "budget_impatto": "number | null",
  "adr_potenzialmente_toccati": ["string"]
}
```

## Output del workflow

```json
{
  "decisione": "string",
  "rationale": "string",
  "voto": {"esito": "string", "favorevoli": 0, "contrari": 0, "astenuti": 0},
  "azioni": [{"chi": "string", "cosa": "string", "acceptance_criteria": [], "deadline": "string"}],
  "mandato_gate": "pass | blocked | deroga_richiesta",
  "adr_scritto": "ADR-NNN | null",
  "checkpoint_scritto": "CP-YYYYMMDD-NNN",
  "direttive_dispatched": ["HC-CEO-CMO-YYYYMMDD-001"]
}
```

---

## State

Lo stato del workflow è mantenuto in `board/ceo/decisioni-pendenti` (durante l'esecuzione) e
trasferito a `board/ceo/direttive-dispatch` (dopo il dispatch). Ogni decisione ha un lifecycle:
`aperta → analisi → proposta → votata → dispatchata → eseguita`.

---

## Connessioni

- [[ceo-conductor]] · `agenti/ceo-conductor.md`
- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[WF-ARBITRATO-PRIORITA]] · `workflow/WF-ARBITRATO-PRIORITA.md`
- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[REGOLE]] · `regole/REGOLE.md`
