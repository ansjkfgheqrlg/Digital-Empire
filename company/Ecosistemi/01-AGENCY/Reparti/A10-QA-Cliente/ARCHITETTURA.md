---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #qa #audit #indipendenza #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# ARCHITETTURA — A10 QA-Cliente & Audit Qualità

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini, gate e namespace.
> Standard: CF-grade (ADR-007). Motori esistenti → wrap, mai rewrite (ADR-003).
> **A10 AUDITA, NON COSTRUISCE.** Separazione dei poteri: chi consegna (A4) non si auto-valuta.

---

## 1. Forma e missione

**Il difetto del v1.** Il Gate Delivery viveva *dentro* A4: `AG-A4-QA` era un verifier del reparto
che consegna, sotto lo stesso coordinatore che ha pianificato la delivery. Zero indipendenza:
il gate poteva essere piegato dalla pressione di chiudere la settimana.

**La correzione v2.** A10 è l'**audit qualità indipendente**, trasversale su tutta la pipeline
A1→A9, con QA lato cliente prima e dopo la consegna. `AG-A10-COORD` riporta ad **AG-DIR**,
non ad `AG-A4-COORD`. Il Gate Delivery di A4 **resta** (auto-verifica interna, first pass);
A10 aggiunge **sopra** l'audit indipendente, che è quello che sblocca la firma UAT del cliente.

**Confine non negoziabile:** A10 non scrive codice di delivery, non patcha workflow cliente,
non ripara ambienti. Emette **PASS** o **FAIL con lista difetti** e rimanda a chi ha costruito.
Un reparto che ripara ciò che audita smette di essere indipendente.

---

## 2. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A10 QA-Cliente & Audit Qualità        [riporta ad AG-DIR, NON ad A4]
         │
         AG-A10-COORD (coordinator, opus)  → assegna reviewer; emette PASS/FAIL
         ├── AG-A10-REVIEW   (verifier, sonnet) → testa il workflow sul server cliente
         ├── AG-A10-UAT      (worker,   sonnet) → facilita l'UAT; verifica comprensione
         ├── AG-A10-BRAND    (verifier, sonnet) → brand_kit iniettato in ogni output
         ├── AG-A10-HANDOVER (verifier, sonnet) → pacchetto handover completo
         └── AG-A10-LEARN    (worker,   sonnet) → pattern difetti → agency/reasoning
```

### Roster

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A10-COORD | QA Lead | opus | Assegna il reviewer per ogni delivery; emette il verdetto PASS/FAIL; riporta ad AG-DIR (non ad A4-Coord: indipendenza strutturale) |
| AG-A10-REVIEW | Delivery Reviewer | sonnet | Verifica che il workflow giri **sul server del cliente**; testa ogni componente; caccia le dipendenze residue da DE |
| AG-A10-UAT | UAT Facilitator | sonnet | Facilita l'UAT: guida il cliente nei test, verifica la **comprensione** (non solo la firma) |
| AG-A10-BRAND | Brand Compliance Checker | sonnet | Verifica che il `brand_kit` cliente sia iniettato correttamente in tutti gli output (pattern 11) |
| AG-A10-HANDOVER | Handover Completeness Checker | sonnet | Verifica il pacchetto handover: README, codice, credenziali, licenza d'uso |
| AG-A10-LEARN | Quality Pattern Learner | sonnet | Distilla i pattern di difetti ricorrenti → `agency/reasoning` → A4 e 07-FORGE |

**Principio di coordinamento.** `AG-A10-COORD` (opus) riceve `HC-AG-QC-01` da A4, assegna il team,
raccoglie i 4 verdetti parziali (REVIEW, BRAND, HANDOVER, UAT) e emette **un solo verdetto**.
Il verdetto è **bloccante**: nessuna delivery si chiude e nessun case study parte senza PASS A10.
`AG-A10-COORD` non riceve ordini da A4: un FAIL non è negoziabile con chi ha costruito.

---

## 3. Workflow

| Workflow | Scopo | Cadenza |
|---|---|---|
| **WF-QA-DELIVERY** | Review indipendente di ogni delivery prima del Gate Delivery formale | Per delivery (event-driven, su `HC-AG-QC-01`) |
| **WF-QUALITY-AUDIT** | Audit mensile della qualità complessiva delle delivery e del supporto | Mensile (report entro 5gg da fine mese) |

### 3.1 WF-QA-DELIVERY (flusso)

```
[A4 — delivery a G+7, Gate Delivery interno passato]
         │  HC-AG-QC-01 (richiesta di review indipendente)
         ▼
AG-A10-COORD — valida l'handoff; apre state review; assegna il team
         │
         ├──▶ AG-A10-REVIEW    — testa il workflow sul server cliente, componente per componente
         ├──▶ AG-A10-BRAND     — verifica brand_kit in ogni output prodotto
         └──▶ AG-A10-HANDOVER  — verifica README + codice + credenziali + licenza
         │
         ▼  (i 3 verdetti convergono; se uno è FAIL, l'UAT NON si apre)
AG-A10-UAT — facilita l'UAT col cliente: il cliente esegue 1 run autonoma e la spiega
         │
         ▼
AG-A10-COORD — GATE QA INDIPENDENTE (§4)
  → PASS: delivery sbloccata; segnale a A4 + A6 (case study)
  → FAIL: lista difetti categorizzata → A4 per rework mirato → re-review (mai auto-fix da A10)
         │
         ▼
AG-A10-LEARN — pattern difetti → agency/a10/patterns + agency/reasoning
```

### 3.2 WF-QUALITY-AUDIT (flusso)

```
[Fine mese]
         ▼
AG-A10-LEARN — campiona le delivery degli ultimi 30gg + i ticket supporto A4
         ▼
AG-A10-REVIEW — analizza i pattern di difetto per categoria (ambiente, brand, handover, UAT)
         ▼
AG-A10-COORD — produce il report mensile qualità
  → ad AG-DIR (per A4, A5, A7) · a 07-FORGE se il gap è strutturale (motore, non esecuzione)
```

---

## 4. Gate QA indipendente (BLOCCANTE)

| # | Check | Condizione PASS | Owner |
|---|---|---|---|
| G1 | Autonomia runtime | Il workflow gira **in autonomia sul server del cliente**, senza intervento DE | AG-A10-REVIEW |
| G2 | Zero dipendenza DE | Nessuna credenziale, nessun nodo, nessun endpoint DE nel runtime cliente | AG-A10-REVIEW |
| G3 | Brand compliance | `brand_kit` + `icp` cliente iniettati e visibili in **ogni** output campionato | AG-A10-BRAND |
| G4 | Handover completo | README + codice + credenziali (lato cliente) + licenza d'uso presenti e leggibili | AG-A10-HANDOVER |
| G5 | UAT completata | Checklist UAT firmata dal cliente dopo test guidati | AG-A10-UAT |
| G6 | Run autonoma cliente | Il cliente ha eseguito **1 run da solo** e sa spiegare cosa ha fatto | AG-A10-UAT |
| G7 | Indipendenza del verdetto | Il verdetto è emesso da A10, non da A4; nessun agente A4 ha scritto in `agency/a10/*` | AG-A10-COORD |

**Regola d'oro.** Il gate è **bloccante, mai un suggerimento**. Un FAIL non si "prende in nota":
ferma la chiusura della delivery. Standard di gate: `company/MAXIMILIAN/Skill/maximilian-standard-gate`
(criteri espliciti, verdetto binario, evidenza citata, nessun verdetto senza prova).
Skill operative: `verification-quality` (comportamento), `agent-reviewer` (qualità artefatti),
`impeccable` (completezza del pacchetto).

---

## 5. Handoff

### In ingresso

| Codice | Da | Contenuto |
|---|---|---|
| `HC-AG-QC-01` | A4 Delivery | Richiesta review indipendente: `delivery_id`, accesso server cliente, pacchetto handover, esito Gate Delivery interno |
| `HC-AG-QC-02` | A7 Account Mgmt | Segnalazione qualità post-consegna (cliente lamenta difetto) → apre audit mirato |
| `HC-DIR-QC-01` | AG-DIR | Richiesta di audit straordinario su una pipeline o un reparto |

### In uscita

| Codice | A | Contenuto |
|---|---|---|
| `HC-QC-AG-01` | A4 Delivery | Verdetto: PASS (delivery sbloccata) oppure FAIL + lista difetti categorizzata |
| `HC-QC-AG-02` | A6 Marketing Interno | Segnale "delivery PASS verificata" → materiale eleggibile per case study |
| `HC-QC-DIR-01` | AG-DIR | Report mensile qualità + escalation dei FAIL ricorrenti |
| `HC-QC-FG-01` | 07-FORGE | Gap strutturale di motore (non di esecuzione) → richiesta di miglioramento upstream |

---

## 6. Namespace memoria — `agency/a10/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a10/reviews` | Review per delivery: verdetti parziali, verdetto finale, evidenze | AG-A10-COORD |
| `agency/a10/defects` | Difetti rilevati: categoria, severità, delivery, stato rework | AG-A10-REVIEW |
| `agency/a10/uat` | Sessioni UAT: test eseguiti, run autonoma, esito comprensione | AG-A10-UAT |
| `agency/a10/brand` | Esiti brand compliance: output campionati, campi mancanti | AG-A10-BRAND |
| `agency/a10/handover` | Checklist completezza pacchetto per delivery | AG-A10-HANDOVER |
| `agency/a10/patterns` | Pattern di difetto ricorrenti + audit mensili | AG-A10-LEARN |

**Regola di integrità.** Nessun agente A4 scrive in `agency/a10/*` (sarebbe la fine
dell'indipendenza). Nessun PII cliente e nessun segreto nello state: solo riferimenti
(`cliente_ref`), i secrets restano sul server del cliente. Nessuna review può essere
`chiusa` senza `verdetto ∈ {PASS, FAIL}` e almeno un'evidenza citata per ogni check.

---

## 7. Confine A10 ↔ A4 (separazione dei poteri)

| Aspetto | A4 Delivery | A10 QA-Cliente |
|---|---|---|
| Costruisce la delivery | Sì | **Mai** |
| Ripara i difetti | Sì (rework) | **Mai** (li elenca e rimanda) |
| Gate Delivery interno | Sì (`AG-A4-QA`, first pass) | — |
| Gate QA indipendente | — | **Sì** (bloccante, sblocca la firma) |
| Riporta a | AG-A4-COORD → AG-DIR | **AG-DIR** (linea diretta) |
| Namespace scrittura | `agency/a4/*` | `agency/a10/*` |

**ADR-003 (wrap-non-riscrittura).** A10 non riscrive né i motori né gli artefatti che audita:
li osserva, li testa, li certifica. Se un motore ha un difetto strutturale, A10 apre
`HC-QC-FG-01` verso il reparto proprietario — non patcha.

---

## 8. Checklist struttura del reparto

- [x] `ARCHITETTURA.md` — questo documento
- [x] `README.md` — overview, handoff, come gira
- [x] `agenti/` — 6 file (uno per agente del roster)
- [x] `kpi/KPI.md` — KPI, owner, baseline [DM], target
- [x] `principi/PRINCIPI.md` — P1..P6
- [x] `regole/REGOLE.md` — R1..R8 BLOCCANTI
- [x] `scripts/README.md` — automazioni previste
- [x] `skills/SKILLS.md` — skill del reparto, I/O JSON
- [x] `state/README.md` — namespace `agency/a10` + schema FS + lifecycle
- [x] `workflow/` — `WF-QA-DELIVERY.md`, `WF-QUALITY-AUDIT.md`

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A10`
- [[A4-Delivery]] · `../A4-Delivery/ARCHITETTURA.md` — il reparto che A10 audita
- [[WF-QA-DELIVERY]] · `workflow/WF-QA-DELIVERY.md`
- [[WF-QUALITY-AUDIT]] · `workflow/WF-QUALITY-AUDIT.md`
