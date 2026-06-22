---
Type: KPI
Status: Active
Tags: #kpi #community #retention #onboarding #infobusiness #IB-L2-COMM
Created: 2026-06-21
Last updated: 2026-06-21
---

# KPI — IB-L2-COMM Community & Retention

> Metriche del reparto. Baseline storica: [DM] — da misurare al primo lancio reale.
> Nessun numero inventato (Mandato Art.2 + principio P5 del reparto).

---

## KPI operativi

| KPI | Owner | Definizione | Baseline | Target |
|---|---|---|---|---|
| Onboarding ≤24h | IB-COMM-ONBOARDER | % acquirenti con accesso piattaforma attivo entro 24h dall'acquisto (verificato da formazione-admin) | [DM] — prima coorte | [DM] — si stabilisce dopo 1-2 coorti |
| Attivazione modulo 1 ≤7gg | IB-COMM-HEALTH | % acquirenti che completano il modulo 1 entro 7gg (progress da formazione-student) | [DM] | [DM] |
| Completamento corso per coorte | IB-COMM-HEALTH | % studenti che finiscono il corso, calcolato a fine coorte | [DM] | [DM] — soglia minima 20% (sotto = escalation IB-L2-PRODUCT) |
| Engagement community settimanale | IB-COMM-ENGAGE + IB-COMM-HEALTH | % studenti attivi per settimana (login o interazione su WhatsApp/Discord) | [DM] | [DM] — cresce con i rituali |
| Recovery abbandono precoce | IB-COMM-RETENTION | % studenti inattivi recuperati dopo sequenza win-back (mai invasiva) | [DM] | [DM] |
| Testimonianze raccolte con metrica verificata | IB-COMM-SOCIAL | N. testimonianze con metrica reale verificata da G-COMM nel periodo | [DM] | 100% testimonianze pubblicate con metrica verificata |
| Cross-sell qualificati per coorte | IB-COMM-CROSSSELL | N. lead consensuali (score ≥5 + consenso) passati ad AGENCY via HC-IB-AG-01 | [DM] | [DM] — qualità su quantità |

---

## KPI di qualità del sistema (trasversali al reparto)

| KPI | Owner | Definizione | Target |
|---|---|---|---|
| Gate G-COMM bypass rate | IB-COMM-QA | N. handoff/testimonianze pubblicate senza gate G-COMM / tot | 0 (R4 — bloccante) |
| Outreach automatico su studenti | IB-COMM-QA | N. contatti cross-sell senza segnale + consenso documentato | 0 (R2 — violazione automatica) |
| Testimonianze senza metrica reale | IB-COMM-QA | N. testimonianze pubblicate con claim non verificabile | 0 (R3 — Mandato Art.2) |
| Onboarding oltre soglia senza alert | IB-COMM-ONBOARDER | N. acquirenti oltre 24h senza alert a IB-COORD-COMMUNITY | 0 (R1) |

---

## Come si misurano

- **Onboarding ≤24h e attivazione modulo 1:** lette da formazione-admin (accesso) e
  formazione-student (progress); IB-COMM-HEALTH le scrive in `infobusiness/community/health/`.
- **Completamento corso ed engagement:** da `infobusiness/community/health/{coorte_id}_health.json`
  e dal report mensile in `infobusiness/community/engagement/{mese}_community.md`.
- **Testimonianze e cross-sell:** da `infobusiness/community/testimonials/` e
  `infobusiness/community/crosssell/state.json`; il log gate è in `crosssell/g-comm-log/`.
- **Gate KPI:** IB-COMM-QA registra ogni gate G-COMM (PASS/FAIL) nel log inviolabile.
  IB-COORD-COMMUNITY aggrega per il report mensile a IB-DIRECTOR.

---

## Cadenza di revisione

- Onboarding KPI: ad ogni coorte (al cart-close + a 7gg + a fine coorte).
- Engagement e completamento: report mensile da IB-COMM-HEALTH a IB-COORD-COMMUNITY.
- Report di sintesi a IB-DIRECTOR: mensile + escalation se completion rate < 20%.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — namespace memoria dove i KPI vengono scritti
- [[REGOLE]] · `regole/REGOLE.md` — regole non negoziabili che i KPI di qualità presidiano
- [[README]] · `README.md` — KPI presidiati e missione del reparto
- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md §IB-L2-COMM` — KPI area
