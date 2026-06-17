---
Type: CONCEPT
Status: Active
Tags: #workflow #ceo #arbitrato #priorita #conflitto #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-ARBITRATO-PRIORITA — Workflow Arbitrato delle Priorità

> **Tipo:** CF-grade · **Figura:** CEO / Empire-Conductor
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CEO.md`
> **Connessioni:** [[WF-DECISIONE-STRATEGICA]] · [[WF-REVIEW-TRIMESTRALE]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]]

---

## Scopo

Risolvere conflitti di priorità tra due o più ecosistemi su risorse contese (agenti, tempo, budget,
slot di attenzione del Board) quando non esiste un ADR che risponde già alla questione. Output: una
decisione tracciata con criterio canonico applicato + ri-schedulazione dell'ecosistema "perdente" +
eventuale ADR per colmare il gap di regola.

**Principio chiave:** non esiste "si troverà una via di mezzo" come decisione. Una priorità vince,
l'altra viene ri-schedulata con data, owner e acceptance criteria. Il conflitto non rimane aperto.

---

## Trigger

- Escalation da qualsiasi ecosistema L1 che lamenta conflitto di risorse con un altro.
- Alert del `ceo-verificatore` su direttive bloccate da conflitto non risolto.
- `ceo-okr-tracker` che segnala OKR at-risk per conflitto di risorse.
- Richiesta diretta del conductor durante WF-DECISIONE-STRATEGICA (sub-workflow).

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `ceo-memoria` | 1 | Load ADR esistenti; dedup check (conflitto già deciso?) |
| `ceo-conductor` | 1-7 | Orchestratore; decide se escalare o arbitrare |
| `ceo-priorita-arbiter` | 2-5 | Arbitro principale: applica criteri canonici |
| `ceo-budget-allocator` | 3 | Se il conflitto implica budget: dry-run (facoltativo) |
| `ceo-comunicatore` | 6 | Dispatch decisione di arbitrato + ri-schedulazione |
| `ceo-memoria` | 7 | Write checkpoint; proposta ADR se gap di regola |

---

## Flusso passo-passo

```
STEP 1 — RICEZIONE E PRE-SCREENING
├─ ceo-memoria: cerca ADR o checkpoint con conflitto identico o analogo
│   Trovato → applica il precedente; stop (non si riarbitra)
│   Non trovato → procede a Step 2
├─ ceo-conductor: valuta se il conflitto è reale (risorsa effettivamente limitata)
│   o se esiste una soluzione tecnica che lo elimina (es. swarm parallelo)
│   Sì, esiste soluzione tecnica → applica soluzione; mini-dispatch; stop
│   No, conflitto reale → procede a Step 2
└─ Output: go/no-go arbitrato; precedente trovato o non trovato

STEP 2 — COSTRUZIONE DOSSIER DI ARBITRATO
├─ ceo-priorita-arbiter riceve il dossier completo:
│   - Ecosistema A: risorsa richiesta + motivo + impatto se non prioritario
│   - Ecosistema B: risorsa richiesta + motivo + impatto se non prioritario
│   - Risorsa contesa: descrizione precisa (non vaga)
├─ ceo-budget-allocator: se la risorsa è budget, produce dry-run (facoltativo)
└─ Output: dossier strutturato per l'arbitro

STEP 3 — APPLICAZIONE CRITERI CANONICI (ordine fisso)
├─ Criterio 1 (Mandato Art.2): c'è una promessa fatta (pubblica o contrattuale)?
│   → La promessa vince sempre. Stop.
├─ Criterio 2 (temporale): data pubblica annunciata > data fissata > data interna stimata
│   → L'ecosistema con la scadenza più vincolante e imminente vince.
├─ Criterio 3 (revenue): impatto diretto su revenue contrattualizzata > potenziale futuro
│   → L'ecosistema con revenue certa (contratto firmato) > quello con revenue stimata.
├─ Criterio 4 (OKR): allineamento OKR del trimestre corrente
│   → L'ecosistema il cui OKR è più critico per il trimestre vince.
├─ Criterio 5 (merito): giudizio del conductor se criteri 1-4 non risolvono
│   → Il conductor propone e il Board vota.
└─ Output: criterio applicato + ecosistema prioritario

STEP 4 — DECISIONE E RI-SCHEDULAZIONE
├─ ceo-priorita-arbiter produce la decisione:
│   - Ecosistema prioritario: chi, perché (criterio canonico)
│   - Ri-schedulazione dell'altro: data, owner, modalità alternativa di esecuzione
│   - Se esiste una soluzione parziale (swarm ridotto in parallelo): la propone
├─ Gap di regola? Se nessun criterio canonico risolve il caso → proposta ADR identificata
└─ Output: decisione + ri-schedulazione + ADR draft se gap

STEP 5 — GATE MANDATO
├─ Anche una decisione di arbitrato passa il gate LX
├─ Il gate verifica che la ri-schedulazione non violi promesse esistenti verso l'ecosistema "perdente"
└─ Output: mandato_gate pass

STEP 6 — DISPATCH
├─ ceo-comunicatore costruisce:
│   - Handoff per ecosistema prioritario: conferma della priorità + acceptance criteria
│   - Handoff per ecosistema ri-schedulato: data nuova + owner + modalità alternativa
│   - Handoff per le figure C-Suite responsabili (es. CMO, COO) con istruzioni operative
├─ Dispatch sul bus corporativo
└─ Output: handoff contracts dispatched

STEP 7 — DOCUMENTAZIONE
├─ ceo-memoria: scrive checkpoint con criterio applicato e decisione
├─ Se gap di regola identificato: ceo-memoria scrive ADR draft → conductor firma
│   L'ADR diventa il precedente per conflitti analoghi futuri
└─ Output: checkpoint + ADR (se gap)
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Dedup gate | Step 1 | Bloccante | Conflitto non già risolto da ADR |
| Conflitto reale | Step 1 | Bloccante | Nessuna soluzione tecnica disponibile |
| Criterio applicato | Step 3 | Bloccante | Almeno 1 criterio canonico risolve il conflitto |
| Mandato gate | Step 5 | Bloccante | Decisione non viola promesse esistenti |
| Ri-schedulazione con data | Step 4 | Bloccante | Ecosistema perdente ha data nuova esplicita |

---

## Input del workflow

```json
{
  "ecosistemi_in_conflitto": ["01-AGENCY", "06-INFO-BUSINESS"],
  "risorsa_contesa": "descrizione precisa della risorsa",
  "dossier_A": {
    "ecosistema": "01-AGENCY",
    "motivo": "string",
    "deadline": "YYYY-MM-DD",
    "impatto_se_non_prioritario": "string"
  },
  "dossier_B": {
    "ecosistema": "06-INFO-BUSINESS",
    "motivo": "string",
    "deadline": "YYYY-MM-DD",
    "impatto_se_non_prioritario": "string"
  },
  "adr_esistenti": [],
  "okr_correnti": []
}
```

## Output del workflow

```json
{
  "ecosistema_prioritario": "06-INFO-BUSINESS",
  "criterio_applicato": "Mandato Art.2 — promessa pubblica",
  "decisione": "string",
  "ri_schedulazione": {
    "ecosistema": "01-AGENCY",
    "nuova_data": "YYYY-MM-DD",
    "owner": "CMO",
    "modalita_alternativa": "swarm ridotto in parallelo"
  },
  "mandato_gate": "pass",
  "adr_proposto": "ADR-NNN | null",
  "checkpoint_scritto": "CP-YYYYMMDD-NNN",
  "handoff_dispatched": ["HC-CEO-CMO-YYYYMMDD-001"]
}
```

---

## Casistica criteri (riferimento operativo)

| Caso | Criterio che vince | Esempio |
|---|---|---|
| Entrambi hanno deadline | Data più vincolante e imminente | Lancio annunciato > deadline interna stimata |
| Uno ha contratto firmato | Revenue certa > potenziale | Cliente AGENCY con SLA vs. lead non ancora chiuso |
| Uno è OKR del trimestre | Allineamento OKR | OKR-Q2 priorità revenue > progetto sperimentale |
| Nessun criterio risolve | Voto Board | Conductor propone; Board vota; ADR se gap |

---

## State

Lo stato del workflow è mantenuto in `board/ceo/decisioni-pendenti` durante l'esecuzione e
trasferito a checkpoint + ADR (se prodotto) al termine. Il registro dei conflitti arbitrati
è mantenuto da `ceo-memoria` come pattern per dedup futuro.

---

## Connessioni

- [[ceo-priorita-arbiter]] · `agenti/ceo-priorita-arbiter.md`
- [[ceo-conductor]] · `agenti/ceo-conductor.md`
- [[ceo-memoria]] · `agenti/ceo-memoria.md`
- [[WF-DECISIONE-STRATEGICA]] · `workflow/WF-DECISIONE-STRATEGICA.md`
- [[REGOLE]] · `regole/REGOLE.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
