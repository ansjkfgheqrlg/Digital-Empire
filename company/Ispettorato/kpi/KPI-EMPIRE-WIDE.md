---
Type: KPI
Status: Active (M1 — misurazione manuale finché M2/M3 non automatizzano)
Tags: #ispettorato #kpi #performance
Created: 2026-07-20
Last updated: 2026-07-20
---

# KPI EMPIRE-WIDE — Ispettorato Generale

> Nessun numero inventato (Mandato Art.2). Dato non ancora misurato = `[DM]` — mai zero finto.
> Fino a M2 (telemetria automatica) questi KPI si calcolano A MANO dai registro/CP — un motivo
> in più per farli automatici presto.

| KPI | Definizione | Baseline (oggi, 2026-07-20) | Target | Fonte |
|---|---|---|---|---|
| **Tasso recidiva** | n. errori RECIDIVA (già nel registro) / n. errori totali nel periodo | **0/10** (10 voci migrate, 0 recidive finora) | 0 sempre — ogni recidiva è un fallimento del sistema, non solo dell'esecutore | REGISTRO-ERRORI |
| **Revisioni medie per task** | media di N correzioni prima dell'accettazione, sui task tracciati | `[DM]` — solo 2 voci finora (REV-001 N=1 di scala massima, REV-002 N ripetuto ma non contato) | trend in calo settimana su settimana | REGISTRO-REVISIONI |
| **% swarm morti per session-limit** | n. swarm morti prematuri / n. swarm totali lanciati | `[DM]` — non contato sistematicamente prima di oggi; noti almeno 3 episodi (18/06, 22/06 ×2, 23/07 batch-2) | tendente a 0 con la regola "un solo swarm alla volta" | ERR-20260618/22-001 + osservazione diretta |
| **% collisioni git per settimana** | n. conflitti/push falliti richiedenti intervento manuale / settimana | `[DM]` — almeno 1 collisione file (EDE-8) + N fallimenti push (ERR-20260703-001) nella sola settimana 14-20/07 | 0 collisioni su file (namespace ownership rispettato) | REGISTRO-ERRORI + REGISTRO-REVISIONI |
| **Gate verdi al 1° colpo** | % di gate struct/5-bis passati senza retry, per ciclo di fase | 01-AGENCY: gate ROSSO 1 volta (2 difetti trovati, poi verde) su 3 chiusure ecosistema (02✅ 1° colpo, 04✅ 1° colpo, 01 → 2° colpo) = **2/3 = 67%** | ≥80% | CP checkpoint chiusura ecosistemi |
| **Difetti trovati in autorevisione vs post-consegna** | n. difetti trovati PRIMA che l'utente li veda / totale difetti trovati | EmpireDesk: **3/3 = 100%** (EDE-4, EDE-5, EDE-7 tutti trovati prima del click utente) | ≥90% — la revisione interna deve intercettare quasi tutto | REGISTRO-SUCCESSI |

## Pilota PreventivoForge (dossier 15 §9 — KPI specifici, in attesa di M2)
successo run · 6/6 gate al 1° colpo · durata · foto ≥ soglia · € API = 0 · RECIDIVE = 0.
**Stato:** `[DM]` — zero telemetria automatica finché M2 non caplia `run.py`.

## Connessioni
- [[REGISTRO-ERRORI]] · [[REGISTRO-REVISIONI]] · [[REGISTRO-SUCCESSI]] · [[15-DOSSIER-ISPETTORATO]]
