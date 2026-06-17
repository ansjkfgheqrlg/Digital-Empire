---
Type: CONCEPT
Status: Active
Tags: #coo #kpi #metriche #misura #performance #operations
Created: 2026-06-17
Last updated: 2026-06-17
---

# KPI — COO (Chief Operating Officer)

> KPI presidiati dalla figura COO con logica di misura. Per ogni metrica: target (se definibile),
> metodo di misura, owner del dato, e frequenza di lettura. I KPI con `[DM]` (Da Misurare)
> richiedono una baseline che si stabilisce nelle prime 4 settimane operative.
> Fonte: `company/Board-CSuite/_BLUEPRINT/BP-COO.md` §KPI presidiati

---

## KPI 1 — Run schedulate completate senza intervento

**Descrizione:** Percentuale di run (swarm, cron, job pianificati) completate con successo
senza richiedere intervento manuale (kill/restart/re-schedule da parte del team COO).

**Target:** ≥95% (dal Blueprint BP-COO)
**Metodo di misura:** `(run completate senza INC aperto) ÷ (tot run schedulate)` × 100
**Owner dato:** `coo-runtime-marshal` (log run) + `coo-incident-handler` (log INC per run)
**Frequenza lettura:** settimanale (review settimanale) + mensile (trend)
**Fonte dati:** `board/coo/run-schedule` (run pianificate) + `board/coo/incidenti-storico` (INC per run)

**Come peggiora:** aumenta il numero di zombie, run fallite, cron mancati.
**Come migliora:** coo-process-optimizer implementa fix strutturali sui pattern ricorrenti.

---

## KPI 2 — Tempo di rilevazione incidente

**Descrizione:** Tempo in minuti tra il momento in cui l'anomalia diventa rilevabile nel
sistema e il momento in cui il coo-conductor riceve l'alert (INC aperto).

**Target:** ≤15 minuti (dal Blueprint BP-COO)
**Metodo di misura:** `timestamp_INC_aperto - timestamp_anomalia_rilevabile` (da log)
**Owner dato:** `coo-incident-handler` (timestamp INC) + monitor sorgente (timestamp anomalia)
**Frequenza lettura:** per ogni INC + mensile (percentile 90)
**Nota:** la rilevabilità dell'anomalia non sempre coincide con la sua origine. Il KPI misura
la latenza del sistema di rilevazione, non il tempo dal quale l'anomalia esiste.

**Come peggiora:** monitor non eseguiti, WF-OPS-DAILY saltato, false positive che nascondono anomalie reali.
**Come migliora:** cadenza WF-OPS-DAILY consistente, false positive registry aggiornato in coo-memoria.

---

## KPI 3 — Collisioni sync Max↔Gael

**Descrizione:** Numero di collisioni Git (conflitti non previsti che richiedono risoluzione
manuale) tra le sessioni di Max e Gael nel monorepo.

**Target:** 0 collisioni (dal Blueprint BP-COO)
**Metodo di misura:** n. conflitti Git che richiedono risoluzione manuale (da log git + coo-sync-keeper)
**Owner dato:** `coo-sync-keeper`
**Frequenza lettura:** ogni sync check + settimanale
**Nota:** un conflitto Git automaticamente risolto da Git stesso (fast-forward) non conta.
Solo i conflitti che richiedono intervento umano per la risoluzione.

**Come peggiora:** flag COORDINAMENTO non rispettati, sync automatico ADR-004 non funzionante.
**Come migliora:** rispetto rigoroso del flag COORDINAMENTO + sync regolare + script sync-guard.

---

## KPI 4 — HC rotti aperti

**Descrizione:** Numero di contratti Handoff Contract classificati come "rotti" o "degradati"
nel registry che non hanno ancora un fix applicato.

**Target:** 0 HC rotti senza owner + deadline (dal Blueprint BP-COO)
**Metodo di misura:** count di HC con stato "rotto | degradato" e `owner = null OR deadline = null`
**Owner dato:** `coo-handoff-auditor` (via `board/coo/hc-audit-log`)
**Frequenza lettura:** ogni audit WF-HANDOFF-AUDIT + mensile
**Nota:** un HC rotto che ha owner + deadline non viola il KPI: è un HC in fix. Il KPI
misura i problemi abbandonati, non quelli in lavorazione.

---

## KPI 5 — MTTR (Mean Time to Recovery) [DM]

**Descrizione:** Tempo medio in minuti dalla rilevazione di un incidente alla sua risoluzione
(sistema tornato allo stato verde per il componente impattato).

**Target:** [DM] — baseline da stabilire nelle prime 4 settimane operative
**Metodo di misura:** `media(timestamp_INC_chiuso - timestamp_INC_aperto)` per tutti gli INC del periodo
**Owner dato:** `coo-incident-handler` + `coo-memoria`
**Frequenza lettura:** mensile
**Separazione per severità:** MTTR critico / alto / medio / basso (per rilevare dove il sistema è lento)

---

## KPI 6 — Cadenza operativa [DM]

**Descrizione:** Percentuale di eventi cadenza (standup, review settimanale, review mensile)
completati nel periodo rispetto a quelli previsti.

**Target:** ≥90% per standup · 100% per review settimanale e mensile [DM]
**Metodo di misura:** `eventi cadenza completati ÷ eventi cadenza previsti` × 100
**Owner dato:** `coo-cadence-keeper` (via cadence log)
**Frequenza lettura:** mensile

---

## KPI 7 — Incidenti ricorrenti (stesso pattern in 30gg) [DM]

**Descrizione:** Percentuale di incidenti aperti che hanno un pattern_bank_entry già esistente
nel pattern bank di coo-memoria (= incidente già visto, non ancora risolto strutturalmente).

**Target:** trend decrescente nel tempo — obiettivo a regime: <20% degli INC sono ricorrenti [DM]
**Metodo di misura:** `INC con pattern_bank_entry già esistente ÷ tot INC` × 100
**Owner dato:** `coo-memoria` + `coo-process-optimizer`
**Frequenza lettura:** mensile

**Come migliora:** coo-process-optimizer implementa fix strutturali (ottimizzazioni) sui pattern
che producono INC ricorrenti. Il KPI misura l'efficacia del sistema di apprendimento.

---

## KPI 8 — % sessioni con report CEO inviato [DM]

**Descrizione:** Percentuale di sessioni operative in cui il coo-conductor ha inviato
il report stato al CEO (HC-COO-CEO-01) entro 5 minuti dall'apertura sessione.

**Target:** 100% [DM] — ogni sessione deve iniziare con visibilità per il CEO
**Metodo di misura:** log HC-COO-CEO-01 (timestamp invio) vs. timestamp apertura sessione
**Owner dato:** `coo-conductor`
**Frequenza lettura:** settimanale

---

## Dashboard aggregata — lettura rapida

| KPI | Target | Owner | Frequenza |
|---|---|---|---|
| Run completate senza intervento | ≥95% | coo-runtime-marshal | settimanale |
| Tempo rilevazione incidente | ≤15min | coo-incident-handler | per-INC + mensile |
| Collisioni sync | 0 | coo-sync-keeper | ogni check |
| HC rotti senza owner+deadline | 0 | coo-handoff-auditor | ogni audit |
| MTTR | [DM] | coo-incident-handler | mensile |
| Cadenza operativa | ≥90%/100% | coo-cadence-keeper | mensile |
| Incidenti ricorrenti | trend decrescente | coo-memoria | mensile |
| Report CEO per sessione | 100% | coo-conductor | settimanale |

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[REGOLE]] · `regole/REGOLE.md`
- [[state/README]] · `state/README.md`
- [[BP-COO]] · `company/Board-CSuite/_BLUEPRINT/BP-COO.md`
- [[CEO-Empire-Conductor/kpi/KPI]] · `../CEO-Empire-Conductor/kpi/KPI.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
