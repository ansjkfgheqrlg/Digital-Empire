---
Type: CONCEPT
Status: Active
Tags: #kpi #copywriting #apsoc #L2-1
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.1 Copywriting

> I KPI del reparto cuore. Fonte: dossier §7.2.
> **Convenzione [DM]:** KPI operativo attivo; il target si fissa dopo i primi run reali (M1-M2 dossier).
> "Prove non promesse": nessun numero inventato.

---

## KPI-COPY-001 — First-pass rate G1
**Metrica:** % di copy che passa A8 ≥80 (≥85 sales page) alla PRIMA iterazione.
**Formula:** `copy PASS al primo giro / copy totali sottomessi al gate`.
**Fonte:** log COPY-QA-LEAD + `marketing/copy/scores`.
**Responsabile:** COPY-QA-LEAD.
**Target:** [DM] — baseline dai primi run; più alto = brief migliori + writer più calibrati.
**Cadenza:** continua; report settimanale.

---

## KPI-COPY-002 — Time-to-copy per formato
**Metrica:** tempo dalla richiesta valida alla consegna gated, per formato.
**Fonte:** timestamp ingresso contratto → timestamp output gated.
**Responsabile:** COPY-MASTER.
**Target (indicativi dal motore esistente):** ad ~15-20 min · sales page ~90-120 min. Da confermare
sui dati reali, non promesse.
**Cadenza:** per run; medie mensili per formato.

---

## KPI-COPY-003 — Score APSOC medio per formato
**Metrica:** media degli score A8 dei copy consegnati, per formato.
**Fonte:** `marketing/copy/scores`.
**Responsabile:** A8 + COPY-QA-LEAD.
**Target:** ≥80 standard, ≥85 sales page (per definizione del gate); trend in salita = sistema che impara.
**Cadenza:** settimanale.

---

## KPI-COPY-004 — Pattern ICP consolidati
**Metrica:** numero di pattern validati con evidenza in `marketing/copy/patterns/{icp}`.
**Fonte:** namespace `marketing/copy/patterns/*`.
**Responsabile:** AN4 (L2.4) scrive, COPY-MASTER consuma.
**Target:** [DM] — crescita nel tempo = vantaggio cumulativo (il sistema scrive sempre meglio per gli ICP noti).
**Cadenza:** mensile.

---

## KPI-COPY-005 — Iterazioni medie al gate
**Metrica:** numero medio di cicli A8 prima del PASS (1 = first-pass, 3 = limite prima dell'escalation).
**Fonte:** log COPY-QA-LEAD.
**Responsabile:** COPY-QA-LEAD.
**Target:** tendere a 1; ≥3 ricorrente su una sezione = problema di brief o di pattern, non di esecuzione.
**Cadenza:** settimanale.

---

## KPI-COPY-006 — Gate bypass rate
**Metrica:** numero di copy consegnati senza gate completo.
**Fonte:** audit `marketing/copy/scores` vs consegne.
**Responsabile:** COPY-QA-LEAD + Brand-Voice Sentinel.
**Target:** **0** — KPI di qualità del Backbone (Art.4.1). Ogni bypass è un incidente.
**Cadenza:** continua.

---

## Connessioni

- [[copy-qa-lead]] · `agenti/copy-qa-lead.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-master]] · `agenti/copy-master.md`
- [[state/README]] · `state/README.md`
- [[KPI]] (L2.4 Analytics) · `company/Ecosistemi/04-MARKETING/Reparti/L2-4-Analytics/kpi/KPI.md`
