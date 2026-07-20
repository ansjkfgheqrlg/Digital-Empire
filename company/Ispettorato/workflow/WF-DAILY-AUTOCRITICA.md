---
Type: WORKFLOW
Status: Active
Tags: #ispettorato #workflow #daily #autocritica #kpi #isp
Created: 2026-07-20
Last updated: 2026-07-20
---

# WF-DAILY-AUTOCRITICA — Ciclo Giornaliero di Autocritica

- **ID**: `WF-DAILY-AUTOCRITICA`
- **Trigger**: **ogni giorno** (direttiva Max, dossier 15 §7 — uno dei 4 cicli)
- **Owner orchestratore**: `isp-conductor`
- **Output**: daily report con KPI trend + autocritica ("cosa rifaremmo meglio") + top-3 azioni assegnate

---

## Scopo

Chiudere ogni giornata con una fotografia onesta: come sono andate le run del giorno, cosa dicono i
KPI rispetto al trend, cosa rifaremmo meglio, e — soprattutto — **tre azioni concrete** già assegnate
a un reparto owner. Non un diario: un ciclo che PRODUCE lavoro di miglioramento, non solo lo descrive.

L'autocritica non è colpa: è la domanda "sapendo com'è andata, cosa faremmo diversamente domani?"
posta sui dati, non sulle impressioni.

---

## Precondizioni

- Le run del giorno hanno scritto la loro telemetria (JSONL) via `WF-RUN-AUDIT`.
- I registri (`ERR-*`, `REV-*`, `SUC-*`) sono aggiornati alla giornata.
- Nessun numero inventato: se un KPI non ha dati sufficienti, il daily lo dichiara (Gate 4).

---

## Passi

1. **Trigger giornaliero → `isp-conductor`** apre il ciclo e nomina la data `YYYY-MM-DD`.
2. **`isp-kpi-analyst` calcola il trend**: KPI per workflow (successo run, durata, gate verdi al
   1° colpo, € API, difetti sfuggiti, `revisioni_medie_per_task`) confrontati con giorni/settimana
   precedenti. Dove manca il dato → "nessun dato", mai zero finto.
3. **`isp-run-auditor` aggrega le run del giorno**: quante run, quali VERDI/ROSSE, near-miss,
   scostamenti KPI, errori nuovi vs noti. Consolida in una sola vista giornaliera.
4. **`isp-report-forger` genera il daily** (`report/daily/<YYYY-MM-DD>.md`): impagina KPI trend +
   sezione **autocritica** ("cosa rifaremmo meglio") + blocco **top-3 azioni** prioritarie. Formato
   fisso; nessuna sezione vuota.
5. **`isp-improvement-dispatcher` assegna le top-3**: ogni azione riceve owner + scadenza + criterio
   di chiusura, in `BACKLOG.md` del reparto o come step di fase. Chiusura futura via `isp-verifier`.
6. **`isp-conductor` firma** il daily e lo passa a `isp-liaison-altiranghi` se il trend richiede
   attenzione degli alti ranghi (→ WF-REPORT-ALTIRANGHI).

---

## Gate (bloccanti)

- **G-D1** — Nessun daily senza tutte le sezioni (KPI trend, autocritica, top-3). Template integrale
  o non si emette (Gate 4 ARCHITETTURA + regola `isp-report-forger`).
- **G-D2** — Le top-3 azioni devono essere ASSEGNATE, non solo elencate: owner + scadenza obbligatori
  (Gate `isp-improvement-dispatcher`).
- **G-D3** — Un errore RECIDIVA emerso nell'aggregazione forza un'escalation (WF-RECIDIVA-GATE), non
  si scioglie in una riga del daily.
- **G-D4** — Zero numeri inventati: un KPI senza dato dice "nessun dato".

---

## DONE WHEN

- `report/daily/<YYYY-MM-DD>.md` esiste, completo di KPI trend + autocritica + top-3.
- Le tre azioni risultano assegnate a un owner con scadenza in `BACKLOG.md`/fase.
- Il trend `revisioni_medie_per_task` e gli altri KPI sono aggiornati in `ispettorato/kpi`.
- Se c'era una RECIDIVA, l'escalation è aperta e tracciata.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md` — i 4 cicli, i gate
- [[15-DOSSIER-ISPETTORATO]] · §7 (trigger "OGNI GIORNO")
- `isp-conductor` · `isp-kpi-analyst` · `isp-run-auditor` (batch gemello) — orchestrazione, KPI, aggregazione
- `isp-report-forger` · `isp-improvement-dispatcher` — daily e assegnazione azioni
- [[WF-RUN-AUDIT]] (fonte dati) · [[WF-RECIDIVA-GATE]] (escalation) · [[WF-REPORT-ALTIRANGHI]] (salita)
- `scripts/report_generator.py` · `scripts/trace_collector.py` — compilazione deterministica
