---
Type: KPI
Status: Active
Tags: #kpi #CF-R4 #testo #produzione #metriche #gate-copy #derivati
Created: 2026-06-23
Last updated: 2026-06-23
---

# KPI — CF-R4 Produzione Testuale

> Tutti i valori target sono `[DM]` (da misurare) fino a baseline reale di 4 settimane.
> Nessun numero inventato (Mandato Art.2 — "prove non promesse").
> La baseline si misura a partire da CF-F5 (primo articolo + prima newsletter live con gate verdi).

---

## KPI operativi

| KPI | Owner | Definizione | Direzione | Baseline |
|---|---|---|---|---|
| Lead time brief→draft | CF-R4-COORD | Ore dalla ricezione `brief.json` validato al draft pronto per CF-R4-QA; per formato (articolo, newsletter corpo, script, caption) | ↓ | [DM] |
| Lead time brief→output finale | CF-R4-COORD | Ore dalla ricezione `brief.json` all'output con gate PASS e `pronto_per_cf_r6: true` | ↓ | [DM] |
| GATE-COPY first-pass rate | CF-R4-QA | % testi che superano GATE-COPY (CF-R4-QA) al primo giro senza rework; per formato | ↑ | [DM] |
| GATE-BRAND first-pass rate | CF-R4-QA | % testi che superano GATE-BRAND al primo giro; per brand | ↑ | [DM] |
| Pezzi prodotti / ciclo | CF-R4-COORD | N. output con gate PASS consegnati nel periodo (settimanale); per formato | ↑ | [DM] |
| Derivati per pezzo madre | CF-R4-COORD | Media di N formati derivati per ordine WF-REPURPOSING; misura ROI del repurposing | ↑ | [DM] |
| Lead time handoff MARKETING | CF-R4-COORD | Ore dall'emissione HC-MK-CF-01 alla ricezione blocco APSOC con gate_copy_guild PASS | monitora | [DM] |
| % newsletter bloccate per MARKETING indisponibile | CF-R4-COORD | N. newsletter in stato `in_attesa_marketing` > SLA / tot newsletter avviate | ↓ | [DM] |
| % draft con gap dati [DM] | CF-R4-WRITE | N. draft con ≥1 segnaposto [DM] per dati mancanti / tot draft; segnale di brief insufficienti | ↓ | [DM] |
| Rework rate per formato | CF-R4-QA | N. testi con ≥1 rework / tot testi per formato; segnale di qualità produzione | ↓ | [DM] |

---

## KPI qualità output

| KPI | Soglia tecnica | Note |
|---|---|---|
| Hook nelle prime 3 righe / [HOOK] | 100% | Automaticamente verificabile con structure-validator; deviazione = FAIL GATE-COPY |
| Parole_vietate nel testo | 0 occorrenze | Verifica CF-R4-QA su ogni pezzo |
| Word count accuracy | ±20% dal brief | Range accettato da CF-R4-QA; oltre = FAIL campo lunghezza_coerente |
| Meta description SEO | 150-160 caratteri | Range tecnico; sotto = penalizzazione SEO; verifica seo-checker |
| Oggetto email (prima variante) | ≤60 caratteri | Limite display client email standard; verifica CF-R4-CAPTION |
| Script [HOOK] (parole) | ≤25 parole | Pronunciabile in ≤3s a 130 p/min (parlato naturale italiano) |
| Derivati con FAIL bloccante per batch | < 3 per batch | ≥3 FAIL → sospensione batch; diagnosi CF-R4-COORD |

---

## KPI apprendimento (CF-R4-LEARN)

| KPI | Owner | Definizione |
|---|---|---|
| Pattern testuali validati / mese | CF-R4-LEARN | N. pattern con n ≥ 5 in `cf/patterns` per CF-R4 |
| % pezzi con dati feedback a 7gg | CF-R4-LEARN | N. testi con metriche_7gg / tot testi pubblicati |
| Aggiornamenti libreria hook da pattern | CF-R4-LEARN | N. formule hook aggiornate/aggiunte da pattern validati nel periodo |
| % FAIL gate correlati a origine brief | CF-R4-LEARN | N. FAIL con causa nel brief (identificata per ≥3 casi) / tot FAIL nel periodo |

---

## Dashboard (alimentazione)

Namespace sorgenti per dashboard CF-Director:
- `cf/text` → stato ordini testuali, lead time, gate pass/fail per ordine
- `cf/scripts` → stato script video, handoff a CF-R3
- `cf/captions` → caption prodotte per brand e canale
- `cf/patterns` → pattern hook/angle che performano per testo (da CF-R4-LEARN via CF-R7-FEEDBACK)

Dashboard aggiornata dopo ogni ordine CF-R4 chiuso (CF-R4-COORD aggiorna `cf/kpi`).

---

## Connessioni

- [[cf-r4-coord]] · `agenti/cf-r4-coord.md` — owner KPI operativi e lead time
- [[cf-r4-qa]] · `agenti/cf-r4-qa.md` — owner KPI gate qualità
- [[cf-r4-learn]] · `agenti/cf-r4-learn.md` — owner KPI apprendimento e pattern
- [[cf-r4-write]] · `agenti/cf-r4-write.md` — contribuisce a KPI word count accuracy e draft gap
