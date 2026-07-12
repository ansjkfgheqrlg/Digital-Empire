---
Type: PROJECT
Status: Active
Tags: #workflow #agency #qa #audit #mensile #A10
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-QUALITY-AUDIT — Audit mensile della qualità

> **Scopo.** Audit mensile della qualità complessiva delle delivery e del supporto. Non giudica la
> singola delivery (lo fa WF-QA-DELIVERY): cerca i **pattern** — i difetti che si ripetono, gli step
> che cedono sempre, i gap che non sono colpa dell'esecutore ma del motore (P6).
> Standard CF-grade. Gate BLOCCANTI (`../regole/REGOLE.md`).

---

## 1. Trigger

| Trigger | Fonte | Quando |
|---|---|---|
| Fine mese | Calendario | Ultimo giorno del mese → il workflow si apre automaticamente |
| `HC-DIR-QC-01` | AG-DIR | Audit straordinario su una pipeline o un reparto (fuori cadenza) |
| Soglia difetti sfuggiti | `agency/a10/patterns/escaped` | ≥3 difetti sfuggiti al gate nel mese → audit anticipato (A10 sta fallendo su sé stessa) |

---

## 2. Step

### S1 — Campionamento · `AG-A10-LEARN`
Campiona le delivery degli **ultimi 30 giorni** da `agency/a10/reviews/*`. Se le delivery del mese
sono ≤10, il campione è **totale** (nessun campionamento statistico su numeri piccoli: si guarda tutto).
Dichiara esplicitamente `delivery_reviewate / delivery_totali` — un audit che non dichiara il campione
non è un audit.

### S2 — Incrocio coi ticket di supporto · `AG-A10-LEARN`
Legge `agency/a4/support` (ticket dei 90gg) e li incrocia con `agency/a10/defects`.
Ogni ticket classificato come **difetto di delivery** ma **assente** dalla review corrispondente è un
**difetto sfuggito al gate** → `agency/a10/patterns/escaped`. È il KPI più severo del reparto, perché
giudica A10 stessa: se il gate lascia passare i difetti, il gate non serve a niente.

### S3 — Analisi dei pattern · `AG-A10-REVIEW`
Raggruppa i difetti per **categoria** (ambiente, brand, handover, UAT, dipendenza-DE) e per **step di
origine** nella pipeline A1→A9. Conta occorrenze e clienti distinti. Distingue:
- **Difetto di esecuzione** → l'errore è nell'esecuzione dello step (destinatario: A4, A5, A7)
- **Difetto strutturale** → il motore rende l'errore probabile o inevitabile (destinatario: 07-FORGE)

Un difetto entra tra i pattern ricorrenti solo con **≥3 occorrenze** oppure **≥2 clienti distinti**:
sotto quella soglia è un aneddoto, e gli aneddoti non cambiano i sistemi (P6).

### S4 — Report · `AG-A10-COORD`
Produce `agency/a10/patterns/monthly/{YYYY-MM}.json` + versione leggibile: campione dichiarato,
KPI del mese, difetti per categoria, pattern ricorrenti con destinatario, difetti sfuggiti al gate,
azioni proposte. Ogni numero cita la chiave di stato da cui proviene. Baseline non misurata → **[DM]**.

### S5 — Distribuzione · `AG-A10-COORD`
- `HC-QC-DIR-01` → **AG-DIR** (report completo + escalation dei FAIL ricorrenti; AG-DIR gira le
  azioni ad A4, A5, A7 — A10 non dà ordini agli altri reparti, li audita)
- `HC-QC-FG-01` → **07-FORGE** per ogni gap **strutturale** (il motore va migliorato, non l'esecutore)

**Entro 5 giorni da fine mese.** Un audit che arriva a metà del mese successivo commenta la storia.

### S6 — Chiusura del ciclo precedente · `AG-A10-LEARN`
Verifica che le azioni proposte nel report del **mese precedente** siano state prese in carico:
`aperta` / `in-corso` / `chiusa` / `ignorata`. Le azioni `ignorate` per due mesi consecutivi salgono
in escalation ad AG-DIR con `HC-QC-DIR-01`. Un audit che non verifica i propri esiti è teatro.

---

## 3. Gate

| # | Check | Owner | PASS se |
|---|---|---|---|
| Q1 | Campione dichiarato | LEARN | Il report dichiara `delivery_reviewate / delivery_totali` |
| Q2 | Zero metriche inventate | LEARN | Ogni numero cita la chiave di stato di origine; baseline assente = **[DM]** (R7) |
| Q3 | Pattern ≠ aneddoto | REVIEW | Un difetto è "ricorrente" solo con ≥3 occorrenze o ≥2 clienti distinti |
| Q4 | Difetti sfuggiti calcolati | LEARN | L'incrocio ticket-90gg ↔ review è stato eseguito (S2), anche se il risultato è 0 |
| Q5 | Destinatario esplicito | COORD | Ogni pattern ha un destinatario: A4/A5/A7 (esecuzione) o 07-FORGE (struttura) |
| Q6 | Puntualità | COORD | Report condiviso **entro 5gg** da fine mese |
| Q7 | Follow-up del mese precedente | LEARN | Stato di ogni azione del report precedente verificato (S6) |

**Blocco.** Un report che fallisce Q2 **non esce**: si torna indietro e si sostituiscono i numeri
senza fonte con `[DM]`. Un audit che inventa metriche brucia l'unica cosa che possiede: la fiducia.

---

## 4. I/O

**Input**: `agency/a10/reviews/*` · `agency/a10/defects/*` · `agency/a10/uat/*` ·
`agency/a4/support` (lettura) · report del mese precedente

**Output**:
| Artefatto | Chiave |
|---|---|
| Report mensile (JSON + leggibile) | `agency/a10/patterns/monthly/{YYYY-MM}.json` |
| Pattern ricorrenti aggiornati | `agency/a10/patterns/defects.json` |
| Difetti sfuggiti al gate | `agency/a10/patterns/escaped.json` |
| Pattern distillati a livello ecosistema | `agency/reasoning` |

Contratto JSON del report: `../skills/SKILLS.md §4`. Nessun PII, nessun segreto (R6).

---

## 5. Handoff

**In**: trigger calendario · `HC-DIR-QC-01` (AG-DIR) · soglia difetti sfuggiti
**Out**: `HC-QC-DIR-01` (AG-DIR — report + escalation) · `HC-QC-FG-01` (07-FORGE — gap strutturali)

A10 **non dà ordini** ad A4, A5 o A7: consegna il report ad AG-DIR, che possiede la linea di comando.
L'audit misura e riferisce; l'esecuzione delle azioni è di chi ha l'autorità sui reparti.

---

## 6. DONE-WHEN

Il ciclo di audit è chiuso quando:

- [ ] `monthly/{YYYY-MM}.json` esiste e dichiara il campione (`reviewate / totali`)
- [ ] Ogni KPI del mese è presente, con fonte citata **oppure** `[DM]` (mai un numero inventato — R7)
- [ ] L'incrocio ticket-90gg ↔ review è stato eseguito e `escaped.json` è aggiornato (anche se = 0)
- [ ] Ogni pattern ricorrente ha `occorrenze`, `clienti_distinti`, `step_origine`, `destinatario`
- [ ] `HC-QC-DIR-01` emesso verso AG-DIR **entro 5gg** da fine mese
- [ ] `HC-QC-FG-01` emesso per **ogni** gap classificato come strutturale
- [ ] Lo stato delle azioni del report precedente è verificato; le azioni ignorate 2 mesi consecutivi
      sono in escalation
- [ ] Nessun agente A10 ha riparato nulla durante l'audit (R1)

**Non è chiuso se**: il report contiene un numero senza fonte, se il campione non è dichiarato,
se un pattern non ha destinatario, o se arriva oltre il quinto giorno.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md §3.2` — il flusso in forma di diagramma
- [[ag-a10-learn]] · `../agenti/ag-a10-learn.md` — owner del campionamento e del report
- [[KPI]] · `../kpi/KPI.md` — i KPI che questo audit calcola
- [[WF-QA-DELIVERY]] · `WF-QA-DELIVERY.md` — la fonte dei dati che l'audit aggrega
