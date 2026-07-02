---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #closing #sales-call #discovery #A8
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — A8 Closing / Sales-Call

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.
> Reparto NUOVO v2 (TARGET-V2) — presidia il gap tra preventivo inviato (A3) e contratto firmato.

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A8 Closing / Sales-Call
         │
         AG-A8-COORD (coordinatore, opus)
         ├── AG-A8-PREP  Call Preparation Specialist (worker, opus)
         │     → aggrega: preventivo (A3) + dossier lead (A1) + obiezioni attese (A5) + script (A5)
         │     → produce il dossier pre-call consegnato a Max
         ├── AG-A8-OBJ  Obiezioni Anticipatore (worker, sonnet)
         │     → simula domande/obiezioni del prospect; risposte a-prova (mai claim inventati)
         │     → legge libreria obiezioni da A5 (ag-a5-obj)
         ├── AG-A8-SCRIPT  Script Coach (worker, sonnet)
         │     → personalizza lo script standard (da A5) per prospect + prodotto specifico
         ├── AG-A8-DEBRIEF  Post-Call Analyst (worker, sonnet)
         │     → dopo la call di Max: esito + obiezioni emerse + motivazione → log + pattern
         ├── AG-A8-LEARN  Closing Pattern Learner (worker, sonnet)
         │     → analizza win/loss; pattern → A5 (script) + A3 (preventivi) + 08-INTELLIGENCE
         └── AG-A8-QA  Verificatore Prep Call (verifier, sonnet)
               → gate: dossier pre-call completo ≥2h prima della call; nessun campo vuoto
               → blocca la consegna a Max se il dossier è incompleto o lo script viola Brand Voice
```

**Principio di coordinamento:** AG-A8-COORD riceve la call prenotata (da A2) e il preventivo
inviato (da A3), assegna l'aggregazione del dossier ad AG-A8-PREP e attiva OBJ + SCRIPT in
parallelo. AG-A8-QA è bloccante: nessun dossier va a Max senza gate verde. La call resta
umana (Max); il reparto la istruisce ma non la sostituisce.

---

## 2. Flussi principali (prep → call → debrief)

### 2.1 Preparazione call di chiusura (WF-CLOSING-PREP)

```
[Trigger: HC-AG-CL-01 da A2 — call prenotata + thread; preventivo inviato da A3]
         │
         ▼
AG-A8-COORD — valida trigger; recupera funnel del lead
  → preventivo disponibile? dossier A1 disponibile? data/ora call nota?
         │
         ▼
AG-A8-PREP — aggrega il dossier pre-call:
  → preventivo (A3: scope, pricing a catalogo, prove allegate)
  → dossier lead (A1: profilo, audit problema, competitor, ICP)
  → obiezioni attese (A5: libreria obiezioni per ICP/prodotto, via AG-A8-OBJ)
  → script personalizzato (A5: script standard adattato, via AG-A8-SCRIPT)
         │
         ▼   ← PARALLELO (OBJ e SCRIPT girano insieme)
AG-A8-OBJ      → top obiezioni + risposta a-prova per ciascuna (prova → da A3/A1)
AG-A8-SCRIPT   → script call adattato a prodotto + awareness level del prospect
         │
         ▼
AG-A8-QA — gate dossier pre-call:
  → tutti i campi presenti? prove allegate per ogni promessa? script conforme Brand Voice?
  → consegnato ≥2h prima della call?
  → PASS: dossier consegnato a Max · FAIL: AG-A8-COORD chiude il gap → re-gate
```

### 2.2 Debrief post-call (WF-CLOSING-DEBRIEF)

```
[Trigger: Max ha concluso la call → comunica esito ad AG-A8-COORD]
         │
         ▼
AG-A8-DEBRIEF — raccoglie esito strutturato:
  → win / loss / da-ricontattare · obiezioni realmente emerse · motivazione (SEMPRE)
         │
         ├── WIN  → AG-A8-COORD attiva HC-AG-AM-01 verso A7 + handoff A4 Delivery (contratto firmato)
         │
         └── LOSS → AG-A8-LEARN registra il pattern di perdita
                     → A3 (ag-a3-fup: follow-up commerciale) + A3 (ag-a3-learn: WF-LOSS-ANALYSIS)
                     → 08-INTELLIGENCE (pattern aggregato)
         │
         ▼
AG-A8-QA — verifica: motivo registrato (win o loss)? debrief chiuso entro 2h?
  → integrità del namespace garantita prima della chiusura
```

---

## 3. Confine con A3, A4 e Max — chi possiede cosa

| Aspetto | A8 Closing (questo reparto) | Altro reparto / umano |
|---|---|---|
| Costruzione preventivo | Lo riceve da A3; non lo riscrive | A3 Preventivi possiede pricing e proposta (beast-preventivi) |
| Esecuzione della call | Prepara il dossier; non parla col cliente | Max conduce la call (resta umana) |
| Contratto firmato (win) | Triggera l'handoff verso Delivery | A4 Delivery esegue onboarding e scope freeze |
| Follow-up dopo loss | Registra il pattern di perdita | A3 (ag-a3-fup) esegue il follow-up commerciale |
| Libreria obiezioni | La legge e la applica alla call | A5 (ag-a5-obj) la possiede e la aggiorna |
| Script di vendita | Lo personalizza per il prospect | A5 (ag-a5-script) possiede lo script standard |

**Regola d'oro:** il dossier pre-call è il documento di confine. A8 lo produce e lo firma
(gate AG-A8-QA). Max lo riceve e conduce la call. Nessun dossier va a Max senza gate verde,
nessun handoff a Delivery senza esito win registrato da AG-A8-DEBRIEF.

---

## 4. Namespace memoria — `agency/a8/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a8/prep` | Dossier pre-call: preventivo, dossier lead, obiezioni attese, script, gate QA | AG-A8-PREP |
| `agency/a8/calls` | Esiti call: win/loss, motivazione, obiezioni emerse, tempo preventivo→firma | AG-A8-DEBRIEF |
| `agency/a8/scripts` | Libreria script personalizzati per ICP/prodotto; varianti vincenti | AG-A8-SCRIPT |
| `agency/a8/patterns` | Pattern win/loss: obiezioni ricorrenti, cause di perdita, leve di chiusura | AG-A8-LEARN |

**Regola di integrità:** ogni record in `agency/a8/calls` deve avere il campo `esito` e il
campo `motivo` popolati. Una call senza motivo registrato non è una call chiusa (gate AG-A8-QA).

---

## 5. Integrazione con altri reparti e workflow

| Reparto / Sistema | Relazione |
|---|---|
| A2 Acquisizione (`ag-a2-book`) | Fornisce la call prenotata + thread conversazione (HC-AG-CL-01) |
| A1 Ricerca (`ag-a1-brief`, `ag-a1-icp`) | Fornisce dossier lead: profilo, audit problema, ICP, competitor |
| A3 Preventivi (`ag-a3-prop`) | Fornisce il preventivo inviato; A8 ne aggrega scope, pricing, prove |
| A5 Copywriting-Interno (`ag-a5-obj`, `ag-a5-script`) | Libreria obiezioni + script standard da personalizzare |
| A4 Delivery (`ag-a4-coord`, `ag-a4-hand`) | Su win: riceve contratto firmato + scope per onboarding |
| A3 Preventivi (`ag-a3-fup`, `ag-a3-learn`) | Su loss: follow-up commerciale + WF-LOSS-ANALYSIS |
| 08-INTELLIGENCE | Riceve i pattern win/loss aggregati da AG-A8-LEARN |

---

## 6. State e ripartibilità

Ogni esecuzione di WF-CLOSING-PREP produce un `state.json` in `agency/a8/prep/{call_id}/`
con i campi:
- `call_id` — identificativo univoco della call di chiusura
- `lead_id` — riferimento al lead (da A1/A2)
- `preventivo_id` — riferimento al preventivo (da A3)
- `dossier_status` — in_progress / completo
- `obiezioni_status` — assente / prodotto
- `script_status` — assente / personalizzato / conforme_brand_voice
- `qa_gate` — pending / PASS / FAIL + motivo
- `sla_2h_rispettata` — true/false (consegna ≥2h prima della call)
- `last_updated` — timestamp ultimo aggiornamento

Questo permette la **ripartibilità a freddo**: un agente può rientrare nel workflow dal punto
esatto di interruzione senza riaggregare tutto il dossier (test amnesia §6 V2).

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A8`
- [[A3-Preventivi]] · fornitore del preventivo + destinatario follow-up loss
- [[A5-Copywriting-Interno]] · fornitore libreria obiezioni e script
- [[WF-CLOSING-PREP]] · `workflow/WF-CLOSING-PREP.md`
- [[WF-CLOSING-DEBRIEF]] · `workflow/WF-CLOSING-DEBRIEF.md`
