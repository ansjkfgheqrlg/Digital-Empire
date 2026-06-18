---
Type: KPI
Status: Active
Tags: #kpi #email #lifecycle #metriche #L2-3
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.3 Email & Lifecycle

> Metriche operative del reparto. Baseline "[DM]" = da misurare dopo il primo run reale.
> Nessun numero inventato: i valori si popolano dai dati reali di AN2/AN4.

---

## KPI per sequenza (da misurare per ogni sequence_id)

| KPI | Definizione | Fonte dati | Baseline | Target |
|---|---|---|---|---|
| **Open rate** | % destinatari che aprono almeno 1 email della sequenza | AN2 / ESP del committente | [DM] | ≥35% (nurture) / ≥40% (lancio) — da validare col primo run |
| **Click-through rate (CTR)** | % destinatari che cliccano la CTA principale | AN2 / ESP | [DM] | ≥3% (nurture) / ≥5% (lancio) — da validare |
| **Reply rate** | % destinatari che rispondono direttamente all'email (dove la risposta è abilitata) | AN2 | [DM] | Dipende dal tipo di sequenza |
| **Unsubscribe rate** | % che si disiscrivono per sequenza | ESP | [DM] | <2% (segnale di lista sana) |
| **Completion rate sequenza** | % destinatari che ricevono tutte le email senza unsubscribe / bounce | AN2 | [DM] | Dipende dalla durata della sequenza |

---

## KPI per tipo di workflow

### WF-EMAIL-LAUNCH

| KPI | Definizione | Baseline | Note |
|---|---|---|---|
| Conversion rate lancio (email → acquisto) | % acquisti attribuibili alla sequenza email / lista lancio | [DM] | Misura con UTM per sequence_id |
| Open rate email di chiusura (last call) | % apertura ultima email (T-1/T+0) | [DM] | Tipicamente l'email con open rate più alto |
| Revenue per email inviata (RPE) | revenue totale lancio / n. email totali inviate | [DM] | Metrica efficienza del lancio |

### WF-EMAIL-ONBOARDING

| KPI | Definizione | Baseline | Note |
|---|---|---|---|
| Activation rate (first aha moment) | % nuovi utenti che completano il primo passo entro 7gg | [DM] | Metrica principale di E4 — richiede dato dal prodotto |
| Ritenzione 30gg (onboarded vs non) | % ritenzione a 30gg per utenti con sequenza onboarding vs senza | [DM] | Confronto da AN2; richiede dato committente |

### WF-EMAIL-WINBACK

| KPI | Definizione | Baseline | Note |
|---|---|---|---|
| Win-back rate | % churned recuperati con la sequenza | [DM] | Metrica principale di E5 |
| Exit survey completion rate | % cancellati che rispondono alla survey | [DM] | Target ≥30% per dati affidabili |
| Dunning recovery rate | % pagamenti falliti recuperati con sequenza dunning | [DM] | Solo per committenti SaaS |

---

## KPI qualità sistema (reparto)

| KPI | Definizione | Target |
|---|---|---|
| Spam score medio output | Media spam score di tutte le email gated | ≤3/10 (E2) |
| E-QA first-pass rate | % sequenze con E-QA PASS al primo tentativo | ≥80% (obiettivo reparto) |
| Incidenti PII | N. incidenti PII per periodo | 0 — ogni incidente è escalation |
| A8 score medio sequenze approvate | Media score APSOC su email nel namespace | ≥82/100 |

---

## Come si misurano

1. **AN2** (Attribution Analyst) legge i dati ESP (open, click, unsubscribe) per sequence_id.
2. **AN4** (Insight Distiller) distilla i pattern per ICP e li salva in `marketing/copy/patterns/{icp}/email/`.
3. **EMAIL-LEAD** riceve il report da AN2/AN4 e aggiorna questo file con le baseline reali.
4. **Frequenza revisione KPI:** dopo ogni sequenza completata + lancio (mensile per il reparto).

---

## Connessioni

- [[email-lead]] · `agenti/email-lead.md` — owner KPI reparto
- [[e2-deliverability-guard]] · `agenti/e2-deliverability-guard.md` — owner KPI deliverability
- [[e-qa-email-verifier]] · `agenti/e-qa-email-verifier.md` — owner KPI qualità sistema
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.3`
