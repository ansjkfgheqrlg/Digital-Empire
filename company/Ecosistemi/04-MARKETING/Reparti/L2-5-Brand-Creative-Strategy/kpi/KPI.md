---
Type: CONCEPT
Status: Active
Tags: #kpi #brand #creative-strategy #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# KPI — L2.5 Brand & Creative Strategy

> Metriche di presidio del reparto. Baseline da stabilire nel primo ciclo operativo reale (M1-M2).
> [DM] = da misurare: KPI definito, valore target da fissare dopo i primi dati reali.

---

## KPI primari (core del reparto)

| KPI | Definizione | Misurazione | Owner | Target |
|---|---|---|---|---|
| **Brand consistency score** | % output che passano G5 (BR-QA) al primo tentativo, per brand_kit | `marketing/brand/audit/g5-log/` — n. PASS primo tentativo / tot verifiche | BR-QA | [DM] — baseline da M1 |
| **Brand kit attivi** | n. brand_kit completi e approvati in `marketing/brand/kits/` | state/README.md catalogo | BRAND-LEAD | Crescita: +1/mese per ogni nuovo cliente agency onboardato |
| **Coerenza voice cross-output** | n. fail G5 per brand_kit / mese (trend: deve calare) | g5-log/ aggregato per brand_kit_id | BR-QA | [DM] — target: tendenza al ribasso mese su mese |

---

## KPI operativi (velocità e qualità del reparto)

| KPI | Definizione | Misurazione | Owner | Target |
|---|---|---|---|---|
| **Tempo medio WF-BRAND-KIT-BUILD** | Dalla richiesta al kit approvato in namespace (ore) | state/README.md — timestamp richiesta vs timestamp approvazione | BRAND-LEAD | [DM] — indicativo: < 48h per kit nuovo standard |
| **Tempo medio WF-BRAND-AUDIT** | Dalla richiesta al report approvato (giorni lavorativi) | state/README.md — timestamp richiesta vs consegna | BRAND-LEAD | [DM] — indicativo: < 5 giorni lavorativi per audit completo |
| **% kit con G5 PASS al primo tentativo** | Qualità dell'output del team prima del gate | g5-log/ per tipo output = "brand_kit" | BR-QA | [DM] — target progressivo: > 80% in M3 |
| **Richieste L2.1 bloccate per brand_kit mancante** | n. richieste copy bloccate perché brand_kit non esiste | MKT-Conductor log | BRAND-LEAD | Tendenza al ribasso (ogni blocco = kit da costruire — L2.5 deve anticipare) |

---

## KPI di qualità del sistema brand

| KPI | Definizione | Misurazione | Owner | Target |
|---|---|---|---|---|
| **Deriva voce rilevata** | n. output con pattern di deriva identificati da BR2/BR-QA nel periodo | voice_audit.md + g5-log/ tipo_warning = "voce_incoerente" | BR2 | Deve restare < 10% degli output verificati |
| **Competitor cards aggiornate** | n. brand_kit con dossier competitor aggiornato (< 60gg) / tot brand_kit attivi | state/README.md — date_ultima_analisi_competitor | BR4 | 100% dei kit attivi con dossier < 60gg |
| **ADR-bozza evolutive scalate a Max** | n. proposte evolutive brand DE per trimestre (segnale di proattività) | Memory/decisions/ ADR-DRAFT-BRAND-EVOLUTION* | BRAND-LEAD | [DM] — non zero se il mercato si muove; non alto se il brand è stabile |

---

## KPI di guardia (devono restare a 0)

| KPI | Definizione | Target |
|---|---|---|
| **Gate G5 bypassati senza log** | n. output consegnati senza verifica G5 e senza record nel log | 0 — ogni bypass senza log è un incidente critico |
| **Modifche brand DE senza approvazione Max** | n. modifiche a voice_guide.md DE senza ADR approvato | 0 — qualsiasi modifica non tracciata è una violazione Art.5.3 |
| **Brand_kit clienti con vincoli Mandato violati** | n. kit che istruiscono claim senza proof o dependency-language come regola | 0 — segnale di onboarding cliente non qualificato |

---

## Come si misurano (strumenti)

- **g5-log/:** cartella in `marketing/brand/audit/g5-log/` — un file per ogni check BR-QA.
  Ogni file: output_id, brand_kit_id, data, esito, dimensioni. Aggregazione: manuale o via
  `consistency-check.ps1` (quando costruito).
- **state/README.md:** catalogo brand_kit attivi con stato, date, versione — fonte di verità
  per KPI operativi.
- **wiki/log.md:** ogni workflow completato logga una entry — aggregazione mensile per velocità
  e volumi.

---

## Connessioni

- [[state-readme]] · `state/README.md`
- [[br-qa-brand-consistency-verifier]] · `agenti/br-qa-brand-consistency-verifier.md`
- [[brand-lead]] · `agenti/brand-lead.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §7.2 (KPI ecosistema)
