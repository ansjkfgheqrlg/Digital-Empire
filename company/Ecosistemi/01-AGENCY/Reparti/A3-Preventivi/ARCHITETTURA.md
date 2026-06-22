---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #preventivi #pipeline #gate #A3
Created: 2026-06-22
Last updated: 2026-06-22
---

# ARCHITETTURA — A3 Preventivi

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A3 Preventivi
         │
         AG-A3-COORD (coordinatore, opus)
         ├── AG-A3-BRIEF Discovery Brief Builder (worker, sonnet)
         │     → trascrizione call → brief strutturato (skill discovery-call-brief)
         ├── AG-A3-AUDIT Problem Auditor (worker, sonnet)
         │     → quantifica il problema (market-audit + cro_audit.py [WRAPPA])
         ├── AG-A3-PROP Proposal Writer (worker, opus)
         │     → preventivo problem-first (beast-preventivi + market-proposal)
         ├── AG-A3-PRICE Pricing Configurator (worker, haiku)
         │     → seleziona prodotto/bundle dal catalogo fisso; mai sconti (B-003)
         ├── AG-A3-QA Gate Preventivo (verifier, opus)
         │     → proposal-gate end-to-end; BLOCCA se non conforme (mai solo suggerisce)
         ├── AG-A3-FUP Follow-up Commerciale (worker, sonnet)
         │     → 3 touch in 10gg → esito win/loss
         └── AG-A3-LEARN Pattern Learner (worker, sonnet)
               → registra win/loss in agency/reasoning; alimenta ReasoningBank
```

**Principio di coordinamento:** AG-A3-COORD esegue la pipeline lineare con gate finale bloccante.
AG-A3-QA è bloccante su ogni proposta prima dell'invio. Nessun preventivo esce senza gate verde,
nemmeno con il countdown 48h in scadenza. Tre agenti sono opus (COORD, PROP, QA) perché ognuno
porta un giudizio non delegabile: orchestrazione, scrittura problem-first, gate del Mandato.

---

## 2. Flussi principali

### 2.1 WF-PREVENTIVO — da call a proposta inviata (≤48h)

```
[A2: call avvenuta + trascrizione] · [A1: dossier pre-call]
         │
         ▼
AG-A3-COORD — avvia countdown 48h; RECALL agency/03-preventivi + agency/reasoning
         │
         ▼
AG-A3-BRIEF — brief (problema, awareness, stack, vincoli ambiente)
   → vincoli ambiente mancanti? richiesta a Max PRIMA di scrivere (servono ad A4)
         │
         ▼
AG-A3-AUDIT — quantifica il problema (fonte dichiarata; [DM] se manca il dato)
         │
         ▼
AG-A3-PROP — preventivo problem-first (apre col problema, prove non promesse)
         │
         ▼
AG-A3-PRICE — prodotto/bundle dal CATALOGO FISSO (mai sconti, B-003)
         │
         ▼
AG-A3-QA — Gate Preventivo (proposal-gate) — BLOCCA se non conforme
   → PASS: AG-A3-COORD approva → invio ≤48h
   → FAIL: diagnosi per item → rework AG-A3-PROP → re-gate (countdown resta)
         │
         ▼
record in agency/03-preventivi → AG-A3-FUP (WF-FOLLOWUP-COMMERCIALE)
```

### 2.2 WF-FOLLOWUP-COMMERCIALE — presidio 10gg

```
Proposta inviata → AG-A3-FUP
  D+3 (valore) → D+7 (prova) → D+10 (chiusura) · max 3 touch · rispetto del "no"
         │
         ├── WIN  → HC-AG-AM-01 ad A7 + scope congelato ad A4 (firma/pagamento = Max)
         └── LOSS → AG-A3-LEARN registra MOTIVO (sempre) in agency/reasoning
```

### 2.3 WF-LOSS-ANALYSIS — apprendimento dalla perdita

```
AG-A3-LEARN aggrega loss ultimi 30gg
  → pattern per categoria × nicchia (prezzo/scope/competitor/tempistica)
  → soglia: significativo ≥5 · nessuna conclusione n < 3
  → report mensile → A5 (libreria obiezioni) + 08-INTELLIGENCE (HC-AG-IN-01)
  → ReasoningBank aggiornato → recall per AG-A3-PROP nei preventivi futuri
```

---

## 3. Confini del reparto — cosa A3 NON fa

| Aspetto | A3 Preventivi | Chi lo possiede |
|---|---|---|
| Decisione di prezzo | Seleziona dal catalogo fisso; mai sconti né prezzi inventati | team-prezzi (B-003) |
| Conduzione della call | Prepara il dossier pre-call e la proposta | UMANO (Max) — la call resta umana |
| Firma + verifica pagamento | Attiva l'handoff alla firma | UMANO (Max) |
| Delivery del prodotto | Passa lo scope congelato | A4 Delivery (countdown 7gg ad ambiente conforme) |
| Relazione post-firma | Apre il profilo cliente via HC-AG-AM-01 | A7 Account Management |
| Intelligence di nicchia | Consuma e segnala loss pattern | 08-INTELLIGENCE (HC-AG-IN-01) |

**Regola d'oro:** A3 trasforma il problema del cliente in una proposta a catalogo, problem-first,
gated e inviata in 48h. Tutto ciò che è prezzo, firma, delivery e relazione vive fuori dal reparto.

---

## 4. Namespace memoria — `agency/03-preventivi` + `agency/reasoning`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/03-preventivi/` | Ogni preventivo: id, lead, prodotto, esito gate, data invio, stato (inviato/in_followup/win/loss) | AG-A3-COORD |
| `agency/reasoning` | Win/loss con causa, categoria, nicchia; pattern del ReasoningBank | AG-A3-LEARN |

**Regola di integrità:** ogni loss in `agency/reasoning` deve avere il campo `causa` popolato.
Un loss senza motivo non è un loss chiuso (alimenta WF-LOSS-ANALYSIS con dati incompleti).

---

## 5. Integrazione con altri reparti e sistemi

| Reparto / Sistema | Relazione |
|---|---|
| A2 Acquisizione | Fornisce la call prenotata + thread conversazione completo |
| A1 Ricerca | Fornisce il dossier pre-call (profilo, audit problema, competitor) |
| A4 Delivery | Riceve lo scope congelato alla firma (prerequisiti ambiente raccolti in call) |
| A5 Copywriting Interno | Riceve i pattern di loss per aggiornare la libreria obiezioni |
| A7 Account Management | Riceve `HC-AG-AM-01` alla firma (apertura profilo cliente + KAM) |
| 08-INTELLIGENCE | Riceve `HC-AG-IN-01` (loss pattern); fornisce intelligence di nicchia |
| team-prezzi (B-003) | Fonte vincolante del catalogo prezzi; A3 recepisce, non decide |

---

## 6. State e ripartibilità

Ogni esecuzione di `WF-PREVENTIVO` produce `agency/03-preventivi/{id}/state.json` con i campi:
- `preventivo_id` · `lead` · `prodotto` · `esito_gate` · `data_invio` · `stato`
- `last_updated` — timestamp ultimo aggiornamento

Questo permette la **ripartibilità a freddo**: un agente può rientrare nel workflow dal punto esatto
di interruzione (es. attesa integrazione vincoli ambiente da Max) senza riestrarre tutto il contesto.

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[REGOLE]] · `regole/REGOLE.md` — vincoli non negoziabili (gate, pricing, prove)
- [[WF-PREVENTIVO]] · `workflow/WF-PREVENTIVO.md` — pipeline principale
- [[state/README]] · `state/README.md` — definizione dei namespace memoria
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3`
