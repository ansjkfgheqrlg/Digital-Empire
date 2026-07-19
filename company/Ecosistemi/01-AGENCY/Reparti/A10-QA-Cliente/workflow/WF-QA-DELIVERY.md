---
Type: PROJECT
Status: Active
Tags: #workflow #agency #qa #delivery #gate #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-QA-DELIVERY — Review indipendente di ogni delivery

> **Scopo.** Review indipendente di ogni delivery **prima** del Gate Delivery formale e della firma
> UAT del cliente. Il Gate Delivery interno di A4 resta (first pass, auto-verifica); questo workflow
> aggiunge sopra l'audit indipendente — quello che sblocca davvero la chiusura.
> Standard CF-grade. Gate BLOCCANTI (`../regole/REGOLE.md`).

---

## 1. Trigger

| Trigger | Fonte | Contenuto minimo |
|---|---|---|
| `HC-AG-QC-01` | A4 Delivery — delivery a G+7, Gate Delivery interno passato | `delivery_id`, `cliente_ref`, prodotto, accesso al server cliente, path pacchetto handover, esito Gate A4 |
| `HC-AG-QC-02` | A7 Account Mgmt — difetto lamentato dal cliente post-consegna | `delivery_id`, descrizione del difetto, data segnalazione |

**Handoff incompleto = non si parte.** Se manca l'accesso al server del cliente, il workflow **non**
si apre: si rimanda `HC-QC-AG-01` con motivo `handoff_incompleto`. Nessuna review su documenti:
senza esecuzione reale non c'è evidenza (R2).

---

## 2. Step

### S1 — Apertura e assegnazione · `AG-A10-COORD`
Valida l'handoff, crea `agency/a10/reviews/{delivery_id}/review.json` con `review_index = N`,
consulta `agency/a10/patterns` (i check storicamente deboli vanno guardati per primi) e assegna
il team **in parallelo**: REVIEW · BRAND · HANDOVER.

### S2a — Runtime sul server cliente · `AG-A10-REVIEW` [G1, G2]
Esegue almeno 1 run completa **sul server del cliente**, componente per componente. Poi caccia le
dipendenze residue: grep di credenziali, endpoint, path e cron di DE nel runtime.
Registra comando + output osservato + output atteso per ogni componente.

### S2b — Brand compliance · `AG-A10-BRAND` [G3]
Campiona almeno **1 output per workflow consegnato** dalla run reale. Confronta campo per campo col
`brand_kit` + `icp` del cliente. Caccia i placeholder residui, il tono di voce DE, e — priorità
assoluta — le contaminazioni da altri tenant.

### S2c — Completezza handover · `AG-A10-HANDOVER` [G4]
Apre il pacchetto e **segue il README dall'inizio**: se seguendo solo il README non si arriva a una
run, il README è rotto. Verifica codice, credenziali (intestate al cliente), licenza d'uso, runbook.

### S3 — Cancello tecnico · `AG-A10-COORD` [R5]
Raccoglie G1..G4. **Se anche un solo check è rosso: l'UAT NON si apre.** G5/G6 → `SKIP` con motivo
`R5`, verdetto FAIL, salto diretto a S5. Non si mette il cliente davanti a una delivery già rotta.

### S4 — UAT col cliente · `AG-A10-UAT` [G5, G6]
Guida il cliente nei test della checklist. Poi si toglie dalla tastiera: il cliente esegue **1 run
da solo**. Infine la verifica che il v1 non faceva: gli si chiede di **spiegare** cosa ha eseguito
e cosa si aspetta in output. Firma senza comprensione = FAIL G6.

### S5 — Verdetto · `AG-A10-COORD` [G7]
Verifica G7 (nessuna scrittura A4 in `agency/a10/*`, nessun override tentato) ed emette il verdetto
**binario** con evidenza citata per ogni check:
- **PASS** → `HC-QC-AG-01` (delivery sbloccata) + `HC-QC-AG-02` a A6 (eleggibile per case study)
- **FAIL** → `HC-QC-AG-01` con lista difetti categorizzata per severità → A4 per rework mirato

### S6 — Distillazione · `AG-A10-LEARN`
Aggiorna `agency/a10/patterns`: incrementa le occorrenze, marca lo step di origine, promuove a
pattern ricorrente ciò che supera 3 occorrenze o 2 clienti distinti. Se il pattern è **strutturale**
(motore, non esecuzione) → segnala a COORD per `HC-QC-FG-01` verso 07-FORGE.

### S7 — Re-review (solo su FAIL)
A4 fa il rework e riapre con un nuovo `HC-AG-QC-01`. Si apre una **nuova** review con
`review_index = N+1`. La review precedente resta immutabile: la storia dei FAIL non si riscrive
(è il denominatore del KPI "% PASS al primo review").

---

## 3. Gate

| # | Check | Owner | PASS se |
|---|---|---|---|
| G1 | Autonomia runtime | REVIEW | 1 run completa sul server cliente, zero intervento DE |
| G2 | Zero dipendenza DE | REVIEW | Nessuna credenziale / endpoint / path / cron DE nel runtime |
| G3 | Brand compliance | BRAND | `brand_kit` + `icp` in ogni output campionato; zero placeholder; zero cross-tenant |
| G4 | Handover completo | HANDOVER | README autosufficiente + codice + credenziali cliente + licenza |
| G5 | UAT completata | UAT | Checklist di test guidati eseguita e firmata |
| G6 | Run autonoma cliente | UAT | Il cliente esegue 1 run da solo **e** sa spiegarla |
| G7 | Indipendenza verdetto | COORD | Nessuna scrittura A4 in `agency/a10/*`; nessun override |

**Il gate blocca, non suggerisce** (R3). Un FAIL ferma la chiusura della delivery e la pubblicazione
del case study. Non esiste il PASS con riserva.

---

## 4. I/O

**Input**: `HC-AG-QC-01` (o `HC-AG-QC-02`) · accesso server cliente · pacchetto handover ·
`brand_kit` + `icp` (riferimenti) · `agency/a10/patterns` (check prioritari)

**Output**:
| Artefatto | Chiave |
|---|---|
| Verdetto + evidenze G1..G7 | `agency/a10/reviews/{delivery_id}/review.json` |
| Difetti categorizzati | `agency/a10/defects/{delivery_id}/defects.json` |
| Sessione UAT + autonomia | `agency/a10/uat/{delivery_id}/` |
| Esiti brand + handover | `agency/a10/brand/` · `agency/a10/handover/` |
| Pattern aggiornati | `agency/a10/patterns/defects.json` |

Contratti JSON: `../skills/SKILLS.md §2-3`. Nessun PII, nessun segreto (R6).

---

## 5. Handoff

**In**: `HC-AG-QC-01` (A4) · `HC-AG-QC-02` (A7)
**Out**: `HC-QC-AG-01` (A4 — verdetto) · `HC-QC-AG-02` (A6 — case study eleggibile) ·
`HC-QC-FG-01` (07-FORGE — gap strutturale, via COORD)

Canale unico verso l'esterno: **solo COORD** emette handoff. Gli altri agenti parlano a COORD.
L'audit parla con una voce sola.

---

## 6. DONE-WHEN

La review è chiusa quando **tutte** queste condizioni sono vere:

- [ ] `review.json` esiste e contiene un esito per **ognuno** dei 7 check (PASS / FAIL / SKIP-con-motivo)
- [ ] Ogni check ha un'**evidenza citata** — anche i PASS (R2)
- [ ] Il verdetto è **binario**: PASS o FAIL, nessuna terza via (R3)
- [ ] Se FAIL: ogni difetto ha `categoria`, `severita`, `step_origine` ed è in `agency/a10/defects/`
- [ ] `HC-QC-AG-01` emesso verso A4 (sempre, sia su PASS che su FAIL)
- [ ] Se PASS: `HC-QC-AG-02` emesso verso A6
- [ ] `AG-A10-LEARN` ha aggiornato `agency/a10/patterns`
- [ ] Nessun agente A10 ha modificato un artefatto di delivery (R1)
- [ ] Nessun PII e nessun segreto scritto nello state (R6)

**Non è chiusa se**: il verdetto è "PASS ma...", se un'evidenza manca, se un difetto è stato
riparato da A10 invece che rimandato, o se qualcuno di A4 ha scritto in `agency/a10/*`.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md §3.1` — il flusso in forma di diagramma
- [[REGOLE]] · `../regole/REGOLE.md` — R1..R8, i blocchi di questo workflow
- [[ag-a10-coord]] · `../agenti/ag-a10-coord.md` — owner del verdetto
- [[A4-Delivery]] · `../../A4-Delivery/ARCHITETTURA.md` — la fonte di `HC-AG-QC-01`
