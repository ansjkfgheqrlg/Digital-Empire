---
Type: CONCEPT
Status: Active
Tags: #regole #agency #closing #sales-call #gate #A8
Created: 2026-07-11
Last updated: 2026-07-11
---

# REGOLE — A8 Closing / Sales-Call

> **Tutte le regole di questo file sono BLOCCANTI.** Non sono linee guida.
> Chi le applica: **AG-A8-QA** (gate). Nessun agente del reparto — nemmeno AG-A8-COORD — può
> bypassarle. La vicinanza della call **non** abbassa la soglia: si escala, non si deroga.
> Razionale di ciascuna → `principi/PRINCIPI.md`.

---

## R1 — Nessuna prep senza preventivo, nessun handoff senza record

**Regola:** una call di tipo `closing` **non** entra in `WF-CLOSING-PREP` se manca il
`preventivo_id` di A3. Un WIN **non** viene passato ad A4 Delivery se non esiste il record
`agency/a8/calls/{call_id}.json` con `esito = win`.

**Perché blocca:** una call di chiusura senza preventivo non ha oggetto; un handoff a Delivery senza
record scritto crea un onboarding fantasma senza scope congelato.
**Cosa fare al FAIL:** AG-A8-COORD blocca la prep ed escala ad AG-DIR. Mai "prepararla lo stesso".

---

## R2 — Dossier completo o non si consegna

**Regola:** tutti e 8 i blocchi del dossier pre-call devono essere presenti e non vuoti — incluso il
blocco 7 ("cosa NON promettere") e il blocco "uscita NO" nello script. Lo script deve essere
**conforme Brand Voice** (`brand_voice_check = conforme`).

**Perché blocca:** un blocco vuoto in call diventa un'esitazione davanti al cliente; un dossier
parziale consegnato "meglio di niente" è peggio di niente, perché induce fiducia mal riposta.
**Cosa fare al FAIL:** rework del blocco mancante da parte del suo owner, poi re-gate.

---

## R3 — Nessun claim senza prova (Mandato Art.2)

**Regola:** ogni promessa nel dossier — nel preventivo aggregato, nelle risposte alle obiezioni,
nello script — deve avere una **prova citata** (case study, numero misurato, clausola contrattuale,
demo) **oppure** essere marcata `[DM]` e spostata in "cosa NON promettere".

**Perché blocca:** un claim inventato in call è un debito che esplode in delivery.
**Cosa fare al FAIL:** la frase esce dal dossier. Non si "attenua": si rimuove o si prova.
**Nessuna eccezione**, nemmeno per numeri "ovvi" o "di settore".

---

## R4 — Vietata la scarsità artificiale e ogni forma di pressione

**Regola:** vietati in ogni artefatto di A8: "solo N slot rimasti" (se non è verificabilmente vero),
"il prezzo sale domani", deadline fabbricate, urgenza indotta, leve di colpa/ansia, closing tricks.
Una scarsità **reale** e verificabile può essere dichiarata — ricade sotto R3 e va provata.

**Perché blocca:** viola il Mandato Art.2 (è un claim falso) e produce il cliente peggiore: quello
che firma per non litigare, resiste in delivery, scappa in retention.
**Cosa fare al FAIL:** rimozione immediata della leva. **Bloccante assoluta** — una sola occorrenza
manda il dossier in FAIL.

---

## R5 — Prezzi solo da catalogo, zero sconti in call

**Regola:** i prezzi citati nel dossier e nello script provengono **esclusivamente** dal catalogo
fisso (team-prezzi, **B-003**). Nessun prezzo inventato, nessun bundle improvvisato, nessuno sconto,
nessuna "condizione speciale". Richiesta sconto dal prospect → **NO automatico**.

**Perché blocca:** un prezzo negoziato in call rende sospetto tutto il preventivo e distrugge la
comparabilità dei KPI (K1, K2).
**Cosa fare al FAIL:** correzione al valore di catalogo. Deroga = **decisione Board registrata**,
mai una mossa di chi è in call. Il pattern "perdiamo per prezzo" si porta a team-prezzi con evidenze.

---

## R6 — SLA 2h, non negoziabile in nessuna direzione

**Regola:** il dossier pre-call, **gated PASS**, è nelle mani di Max **≥2h prima** della call.
Il debrief post-call è aperto e chiuso **entro 2h** dalla fine della call.

**Perché blocca:** sotto le 2h Max non ha il tempo di assimilare il dossier — e un dossier non
assimilato non esiste. Oltre le 2h dalla call, la memoria dell'esito si riscrive in una storia
coerente, e le storie coerenti sono quasi sempre false.
**Cosa fare al FAIL:** **non** si consegna un dossier in ritardo per "salvare la call". Si escala ad
AG-DIR e si informa Max che la call è **scoperta** (KPI K9 — è un incidente, non una statistica).

---

## R7 — Nessuna call chiusa senza motivo; nessun PII nello state

**Regola (a):** ogni record in `agency/a8/calls` deve avere `esito` **e** `motivo` popolati — win o
loss, sempre. `da-ricontattare` richiede una **data** nel next step, altrimenti è un `loss` mascherato.
Il motivo si registra con le **parole del prospect**, non con l'interpretazione di chi ha condotto.

**Regola (b):** negli schemi di state (`agency/a8/**`) **nessun PII**: solo `lead_id`, `call_id`,
`preventivo_id`, ICP, prodotto. Mai nomi di persone, email, telefoni, indirizzi.

**Perché blocca:** (a) il motivo è l'unico asset che una call persa produce; senza, il loss è puro
costo e il namespace è compromesso. (b) il namespace è condiviso e propagato a 08-INTELLIGENCE:
un PII qui si moltiplica ovunque.
**Cosa fare al FAIL:** la call **resta aperta** finché il motivo non arriva; il PII si rimuove prima
di qualunque scrittura.

---

## R8 — Nessun pattern sotto le 3 evidenze; nessuna riscrittura di artefatti altrui

**Regola (a):** un pattern (`agency/a8/patterns`) può essere dichiarato `consolidato: true` **solo**
con ≥3 osservazioni citate. Sotto 3 è un aneddoto, va marcato `[DM]` e non si propaga ad A5/A3/
08-INTELLIGENCE. Ogni `impatto_stimato` non misurato è `[DM]`.

**Regola (b) — ADR-003, wrap non riscrittura:** A8 **non modifica** artefatti di altri reparti.
Il preventivo (A3) si cita verbatim; la libreria obiezioni e lo script standard (A5) si wrappano e
si dichiara il `delta_vs_standard`. I miglioramenti si inviano come **proposte** al proprietario.

**Perché blocca:** (a) propagare aneddoti come verità genera superstizione commerciale e corrompe
tre reparti a valle. (b) se A8 riscrivesse il preventivo, esisterebbero due versioni della verità e
il cliente firmerebbe quella sbagliata.
**Cosa fare al FAIL:** declassare il pattern ad aneddoto `[DM]`; convertire ogni patch in proposta.

---

## Applicazione

| Regola | Gate che la applica | Momento |
|---|---|---|
| R1 | AG-A8-QA + AG-A8-COORD | Ingresso `WF-CLOSING-PREP` / handoff WIN |
| R2, R3, R4, R5, R6 | AG-A8-QA — **Gate Prep** | Uscita `WF-CLOSING-PREP`, prima della consegna a Max |
| R6, R7 | AG-A8-QA — **Gate Debrief** | Chiusura `WF-CLOSING-DEBRIEF` |
| R8 | AG-A8-QA | Pubblicazione pattern verso A5 / A3 / 08-INTELLIGENCE |

**Doppio FAIL sulla stessa call** (2 cicli consecutivi) → escalation strutturale ad AG-DIR: il
problema non è il singolo artefatto, è l'input a monte (A1/A3) o il processo.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — P1–P6, il razionale di queste regole
- [[ag-a8-qa]] · `agenti/ag-a8-qa.md` — il gate che le applica, checklist per checklist
- [[KPI]] · `kpi/KPI.md` — K3, K4, K5, K9 misurano il rispetto di queste regole
