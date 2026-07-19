---
Type: PROJECT
Status: Active
Tags: #agency #qa #audit #indipendenza #gate #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# A10 — QA-Cliente & Audit Qualità

## Overview

A10 è l'**audit qualità indipendente** di 01-AGENCY. Garantisce che ogni delivery passi una review
**esterna a chi l'ha costruita** prima che il cliente firmi l'UAT, e presidia la qualità trasversale
di tutta la pipeline A1→A9.

Nel v1 il Gate Delivery viveva dentro A4: chi consegna si auto-valutava. A10 corregge il difetto
strutturale — non sostituendo il gate di A4, ma **aggiungendone uno sopra**, indipendente e bloccante.

**Regola d'identità: A10 audita, NON costruisce.** Non scrive codice di delivery, non ripara ambienti,
non patcha workflow. Emette PASS o FAIL con lista difetti, e rimanda a chi ha costruito.

---

## Team (6 agenti)

| ID | Ruolo | Tier | File |
|---|---|---|---|
| AG-A10-COORD | QA Lead | opus | `agenti/ag-a10-coord.md` |
| AG-A10-REVIEW | Delivery Reviewer | sonnet | `agenti/ag-a10-review.md` |
| AG-A10-UAT | UAT Facilitator | sonnet | `agenti/ag-a10-uat.md` |
| AG-A10-BRAND | Brand Compliance Checker | sonnet | `agenti/ag-a10-brand.md` |
| AG-A10-HANDOVER | Handover Completeness Checker | sonnet | `agenti/ag-a10-handover.md` |
| AG-A10-LEARN | Quality Pattern Learner | sonnet | `agenti/ag-a10-learn.md` |

`AG-A10-COORD` riporta ad **AG-DIR**, non ad `AG-A4-COORD`: l'indipendenza è nella linea di riporto,
non nelle buone intenzioni.

---

## Come gira

**Per delivery (WF-QA-DELIVERY).** A4 chiude la delivery a G+7 e passa `HC-AG-QC-01`. COORD apre la
review e assegna il team: REVIEW testa il workflow sul server del cliente, BRAND verifica il `brand_kit`
in ogni output, HANDOVER verifica il pacchetto (README, codice, credenziali, licenza). Se i tre verdetti
sono verdi, UAT facilita la sessione col cliente — che deve eseguire **1 run da solo** e saperla spiegare.
COORD emette il verdetto unico: **PASS** (delivery sbloccata) o **FAIL** + lista difetti categorizzata.
LEARN distilla i pattern.

**Mensile (WF-QUALITY-AUDIT).** LEARN campiona le delivery e i ticket degli ultimi 30gg, REVIEW analizza
i pattern di difetto per categoria, COORD produce il report qualità → AG-DIR (per A4, A5, A7) e, se il
gap è strutturale, → 07-FORGE.

---

## Handoff

**In ingresso**

| Codice | Da | Contenuto |
|---|---|---|
| `HC-AG-QC-01` | A4 Delivery | Richiesta review indipendente su una delivery a G+7 |
| `HC-AG-QC-02` | A7 Account Mgmt | Segnalazione qualità post-consegna → audit mirato |
| `HC-DIR-QC-01` | AG-DIR | Audit straordinario su una pipeline o un reparto |

**In uscita**

| Codice | A | Contenuto |
|---|---|---|
| `HC-QC-AG-01` | A4 Delivery | Verdetto PASS / FAIL + lista difetti |
| `HC-QC-AG-02` | A6 Marketing Interno | "Delivery PASS verificata" → eleggibile per case study |
| `HC-QC-DIR-01` | AG-DIR | Report mensile qualità + escalation FAIL ricorrenti |
| `HC-QC-FG-01` | 07-FORGE | Gap strutturale di motore → miglioramento upstream |

---

## Gate (bloccante)

Sette check, tutti obbligatori: autonomia runtime · zero dipendenza DE · brand compliance ·
handover completo · UAT completata · run autonoma del cliente · indipendenza del verdetto.
Dettaglio in `ARCHITETTURA.md §4`. Standard di gate: `company/MAXIMILIAN/Skill/maximilian-standard-gate`.

**Nessun gate è un suggerimento.** Un FAIL ferma la chiusura della delivery.

---

## Struttura

```
A10-QA-Cliente/
├── ARCHITETTURA.md        — gerarchia, flussi, gate, namespace, confini
├── README.md              — questo file
├── agenti/                — 6 agenti (uno per riga del roster)
├── kpi/KPI.md             — KPI, owner, baseline [DM], target
├── principi/PRINCIPI.md   — P1..P6
├── regole/REGOLE.md       — R1..R8 (bloccanti)
├── scripts/README.md      — automazioni previste
├── skills/SKILLS.md       — skill del reparto, I/O JSON
├── state/README.md        — namespace agency/a10 + schema + lifecycle
└── workflow/              — WF-QA-DELIVERY.md · WF-QUALITY-AUDIT.md
```

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — architettura interna del reparto
- [[A4-Delivery]] · `../A4-Delivery/README.md` — il reparto che A10 audita
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A10`
- [[REGOLE]] · `regole/REGOLE.md` — R1..R8 bloccanti
