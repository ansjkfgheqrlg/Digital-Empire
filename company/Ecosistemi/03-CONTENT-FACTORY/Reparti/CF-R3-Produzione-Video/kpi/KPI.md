---
Type: KPI
Status: Active
Tags: #kpi #CF-R3 #video #produzione #metriche
Created: 2026-06-19
Last updated: 2026-06-19
---

# KPI — CF-R3 Produzione Video

> Tutti i valori target sono `[DM]` (da misurare) fino a baseline reale di 4 settimane.
> Nessun numero inventato (Mandato Art.2 — "prove non promesse").
> La baseline si misura a partire da CF-F6 (primo video reale con pipeline completa).

---

## KPI operativi

| KPI | Owner | Definizione | Direzione | Baseline |
|---|---|---|---|---|
| Video prodotti / ciclo | CF-R3-COORD | N. video con gate verde (CF-R6 PASS) consegnati nel periodo (settimanale) | ↑ | [DM] |
| Costo per video UGC (Higgsfield) | CF-R3-QUEUE | Crediti Higgsfield consumati / n. video UGC completi | ↓ | [DM] |
| Costo per video Avatar (HeyGen) | CF-R3-QUEUE | Crediti HeyGen consumati / n. video avatar completi | ↓ | [DM] |
| Costo per video Shortform (ffmpeg) | CF-R3-EDIT | Sempre 0 crediti engine; monitora costo tempo computazionale locale | — | 0 crediti |
| GATE-FORMATO first-pass rate | CF-R3-QA | % video che superano GATE-FORMATO al primo giro (senza rework) | ↑ | [DM] |
| GATE-BRAND pass rate | CF-R3-QA | % video con soul/palette corretti al primo giro | ↑ | [DM] |
| Delta stima/consumo crediti | CF-R3-QUEUE | (crediti_consumati - crediti_stimati) / crediti_stimati; media per engine | → 0 | [DM] |
| % batch con escalation fallimenti | CF-R3-COORD | N. batch con ≥3 job falliti / tot batch avviati | ↓ | [DM] |
| % ordini bloccati da CF-SENT-COST | CF-R3-QUEUE | N. BLOCCO budget / tot ordini video avviati | monitora | [DM] |
| Lead time brief→video pronto CF-R6 | CF-R3-COORD | Ore dalla ricezione brief.json al gate interno PASS; escluso tempo approvazione CF-SENT-COST | ↓ | [DM] |

---

## KPI qualità output

| KPI | Soglia tecnica | Note |
|---|---|---|
| Loudness video output | -14 LUFS ±2 dB | Misurato post-montaggio; deviazione = FAIL GATE-FORMATO |
| Peak audio | < -1 dBFS | Nessun clipping tollerato |
| Aspect ratio conformità | 100% | Nessun video con aspect errato supera il gate |
| Codec conformità | h264 o h265 | Verifica automatica CF-R3-QA |
| Soul-id match (video UGC) | 100% | Ogni video UGC usa il soul-id del brand_kit dichiarato |

---

## KPI apprendimento (CF-R3-LEARN)

| KPI | Owner | Definizione |
|---|---|---|
| Pattern video validati / mese | CF-R3-LEARN | N. pattern con ≥5 casi in `cf/patterns` per il reparto video |
| % video con dati feedback 7gg | CF-R3-LEARN | N. video con metriche engagement a 7gg / tot video pubblicati |
| Completion rate medio per tipo video | CF-R3-LEARN | Media completion rate per (brand, tipo_video); evoluzione mensile |

---

## Dashboard (alimentazione)

Namespace sorgenti per dashboard CF-Director:
- `cf/render-queue` → coda render attiva, stima vs consumo
- `cf/video` → stato ordini video, engine_id, crediti
- `cf/patterns` → pattern engagement per video (da CF-R3-LEARN via CF-R7-FEEDBACK)

Dashboard aggiornata dopo ogni ordine video chiuso (CF-R3-COORD aggiorna `cf/kpi`).

---

## Connessioni

- [[cf-r3-coord]] · `agenti/cf-r3-coord.md` — owner KPI operativi
- [[cf-r3-queue]] · `agenti/cf-r3-queue.md` — owner KPI budget/stima
- [[cf-r3-qa]] · `agenti/cf-r3-qa.md` — owner KPI gate qualità
- [[cf-r3-learn]] · `agenti/cf-r3-learn.md` — owner KPI apprendimento
