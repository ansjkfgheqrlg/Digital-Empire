---
Type: REPARTO
Status: Active
Tags: #reparto #agency #preventivi #proposta #pricing #gate #A3
Created: 2026-07-11
Last updated: 2026-07-11
---

# A3 — Preventivi

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `pipeline` lineare con gate finale bloccante

---

## Missione

Trasformare ogni discovery call in una **proposta problem-first inviata entro 48h**, con pricing
selezionato dal catalogo fisso (**mai sconti improvvisati**), che vende l'autonomia del cliente —
non la dipendenza.

Il documento apre sempre con il **problema del cliente**, mai con Digital Empire: prove
verificabili, mai promesse. A3 non decide il prezzo (lo recepisce da team-prezzi, B-003), non
conduce la call (è di A8/Max) e non consegna il progetto (è di A4): trasforma il problema in una
proposta a catalogo, gated e spedita in 48h.

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A3-COORD` | Coordinatore Preventivi | `agenti/ag-a3-coord.md` | coordinator | opus | Avvia il countdown 48h, esegue la pipeline, approva l'invio dopo il gate |
| `AG-A3-BRIEF` | Discovery Brief Builder | `agenti/ag-a3-brief.md` | worker | sonnet | Trascrizione call → brief strutturato (skill `discovery-call-brief`) |
| `AG-A3-AUDIT` | Problem Auditor | `agenti/ag-a3-audit.md` | worker | sonnet | Quantifica il problema con fonte dichiarata (`market-audit`, `cro_audit.py`) |
| `AG-A3-PROP` | Proposal Writer | `agenti/ag-a3-prop.md` | worker | opus | Scrive il preventivo problem-first (`beast-preventivi` + `market-proposal`) |
| `AG-A3-PRICE` | Pricing Configurator | `agenti/ag-a3-price.md` | worker | haiku | Seleziona prodotto/bundle dal catalogo fisso; **mai sconti** (B-003) |
| `AG-A3-QA` | Gate Preventivo | `agenti/ag-a3-qa.md` | verifier | opus | `proposal-gate` end-to-end; **BLOCCA** se non conforme, mai solo suggerisce |
| `AG-A3-FUP` | Follow-up Commerciale | `agenti/ag-a3-fup.md` | worker | sonnet | 3 touch in 10gg → esito win/loss; rispetta il "no" |
| `AG-A3-LEARN` | Pattern Learner | `agenti/ag-a3-learn.md` | worker | sonnet | Registra win/loss in `agency/reasoning`; alimenta il ReasoningBank |

Tre agenti sono **opus** (COORD, PROP, QA): ognuno porta un giudizio non delegabile —
orchestrazione, scrittura problem-first, gate del Mandato.

---

## Workflow del reparto (3 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-PREVENTIVO** | `workflow/WF-PREVENTIVO.md` | Da call a proposta inviata in ≤48h: brief → audit → scrittura → pricing → gate → invio | AG-A3-QA: Gate Preventivo PASS; nessun invio senza gate verde |
| **WF-FOLLOWUP-COMMERCIALE** | `workflow/WF-FOLLOWUP-COMMERCIALE.md` | Presidio 10gg: D+3 (valore) → D+7 (prova) → D+10 (chiusura), max 3 touch | AG-A3-QA: esito win/loss registrato; motivo obbligatorio se loss |
| **WF-LOSS-ANALYSIS** | `workflow/WF-LOSS-ANALYSIS.md` | Aggrega le loss a 30gg → pattern per categoria × nicchia → report mensile | AG-A3-QA: nessuna conclusione con n<3; significativo ≥5 |

---

## Gate del reparto — Gate Preventivo

**Presidio: AG-A3-QA (opus). Bloccante — nemmeno il countdown 48h in scadenza è una deroga.**

| Blocca se | Motivo |
|---|---|
| La proposta non apre con il problema del cliente | Violazione del principio problem-first |
| Promessa non provabile / metrica senza fonte | Mandato Art.2 — prove, non promesse ([DM] se il dato manca) |
| Prezzo fuori catalogo o sconto improvvisato | B-003 — il catalogo è vincolante, A3 recepisce e non decide |
| Clausole obbligatorie mancanti | Proprietà del codice · €0 canoni · setup ≤7gg · supporto 90gg |
| Vincoli d'ambiente non raccolti | Servono ad A4: il countdown delivery parte ad ambiente conforme |

FAIL → diagnosi per item → rework di AG-A3-PROP → re-gate. **Il countdown 48h non si ferma,
ma il gate non si bypassa.** Richiesta di sconto fuori catalogo → NO automatico; eventuale
deroga = decisione Board registrata.

---

## KPI del reparto

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| Tempo call→preventivo | AG-A3-COORD | Ore da trascrizione call a invio proposta | Target ≤48h |
| Win rate | AG-A3-LEARN | Preventivi vinti / preventivi inviati nel periodo | [DM] |
| Valore medio preventivo | AG-A3-PRICE | Valore medio delle proposte a catalogo inviate | [DM] |
| Loss con causa registrata | AG-A3-LEARN | Loss con campo `causa` popolato / tot loss | Target 100% |
| Gate bypass rate | AG-A3-QA | Proposte inviate senza gate PASS / tot inviate | Target 0 |

Dettaglio completo → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A2-Acquisizione | Call prenotata + thread di conversazione completo |
| ← riceve da | A1-Ricerca | Dossier pre-call: profilo lead, audit problema, competitor |
| ← riceve da | A8-Closing (LOSS) | Pattern di perdita post-call → follow-up commerciale + WF-LOSS-ANALYSIS |
| ← riceve da | A7-Account-Management | Upsell mappato a fine ciclo cliente (nuovo sprint / retainer) |
| ← riceve da | 08-INTELLIGENCE | Intelligence di nicchia per argomentare il problema |
| → consegna a | A8-Closing | Preventivo inviato: scope, pricing a catalogo, prove — base della call di chiusura |
| → consegna a | A4-Delivery | Scope congelato alla firma + prerequisiti d'ambiente raccolti in call |
| → consegna a | A7-Account-Management | `HC-AG-AM-01` alla firma: apertura profilo cliente + assegnazione KAM |
| → consegna a | A5-Copywriting-Interno | Pattern di loss per aggiornare la libreria obiezioni |
| → consegna a | 08-INTELLIGENCE | `HC-AG-IN-01` — loss pattern aggregati |

**Confine umano:** conduzione della call, firma e verifica del pagamento restano di Max.

---

## Namespace AgentDB

**Chiave canonica: `agency/a3`** (+ `agency/reasoning` condiviso) — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a3` | Ogni preventivo: id, lead, prodotto, esito gate, data invio, stato (inviato / in_followup / win / loss) | AG-A3-COORD |
| `agency/reasoning` | Win/loss con causa, categoria, nicchia; pattern del ReasoningBank | AG-A3-LEARN |

**Regola di integrità:** ogni loss deve avere il campo `causa` popolato. Un loss senza motivo
non è un loss chiuso.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md` (gate · pricing · prove)
- Stato e ripartibilità a freddo → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, flussi, confini, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A3`
- [[ag-a3-qa]] · `agenti/ag-a3-qa.md` — presidio del Gate Preventivo
- [[WF-PREVENTIVO]] · `workflow/WF-PREVENTIVO.md`
- [[WF-LOSS-ANALYSIS]] · `workflow/WF-LOSS-ANALYSIS.md`
- [[A8-Closing]] · conduce la call sul preventivo prodotto qui
- [[A4-Delivery]] · destinatario dello scope congelato alla firma
