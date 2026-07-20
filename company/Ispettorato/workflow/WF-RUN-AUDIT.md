---
Type: WORKFLOW
Status: Active
Tags: #workflow #ispettorato #run-audit #gate
Created: 2026-07-20
Last updated: 2026-07-20
---

# WF-RUN-AUDIT — Audit di Ogni Run

- **ID**: `WF-RUN-AUDIT`
- **Trigger**: **DOPO OGNI UTILIZZO** (fine di ogni run di qualsiasi reparto/ecosistema) — dossier 15 §7.
- **Output atteso**: run-report completo (formato §8) + eventuali `ERR-*` registrati + eventuale RECIDIVA.
- **Owner**: `isp-conductor` (firma il report finale).

---

## Scopo

Nessuna run senza report. Ogni volta che un workflow dell'Impero termina, l'Ispettorato lo seziona
al millimetro, registra ciò che è andato storto, controlla che non sia già successo, e produce un
run-report firmato. È il ciclo "DOPO OGNI UTILIZZO" della direttiva Max, cablato in agenti.

---

## Precondizioni

- La run ha scritto un trace (`telemetry/runs/<workflow>/<run-id>.jsonl`) secondo la convenzione
  `run_id, ts, step, gate, exit, dur_ms, err` (ARCHITETTURA §6). Se manca, lo step 1 blocca.
- Le soglie KPI del workflow sono definite (o marcate `[DM]`) in `kpi/KPI-EMPIRE-WIDE.md`.

---

## Step

| # | Agente | Azione | Gate |
|---|---|---|---|
| 1 | `isp-telemetry-collector` | Raccoglie e normalizza il trace della run (exit, durate, gate, storico sidecar). | Se trace mancante/corrotto → **STOP**, segnala a `isp-conductor`. Nessun audit su telemetria assente. |
| 2 | `isp-run-auditor` | Analisi al millimetro: timeline (step→durata→esito), gate-map (1° colpo/retry), scostamenti KPI vs soglie, anomalie/near-miss. | Ogni scostamento deve citare un evento del trace. Nessun "verde con riserva". |
| 3 | `isp-error-registrar` | Per ogni errore trovato dallo step 2: prepara la voce (sintomo/causa radice/contromisura/owner/stato). Scrive **solo** se lo step 4 dice NUOVO. | Nessuna voce senza causa radice (o `causa-da-determinare`). Append-only. |
| 4 | `isp-recidiva-sentinel` | Confronta ogni errore col `REGISTRO-ERRORI.md` (match sulla causa radice). NUOVO → torna a step 3 per la scrittura. NOTO → **RECIDIVA**. | **RECIDIVA = gate ROSSO bloccante**: apre `WF-RECIDIVA-GATE`, blocca il commit della fase, escalation immediata. |
| 5 | `isp-report-forger` | Compila il **run-report** nel formato §8 (ESITO · TIMELINE · GATE · NUMERI · ERRORI) dai dati degli step 1-4. | Report incompleto = non consegnabile. Zero numeri inventati. |
| 6 | `isp-conductor` | Verifica completezza, **firma** il report, lo consegna. | Non firma se manca il report, se un KPI è uno zero finto, o se una RECIDIVA è mascherata da verde. |
| 7 | `isp-liaison-altiranghi` | Instrada il report firmato (e l'eventuale escalation RECIDIVA) verso Board/MAXIMILIAN/Max. | — |

---

## Gate del workflow (bloccanti)

1. **Nessuna run senza run-report** (ARCHITETTURA §5 gate 1). Finché il report non è firmato, la
   run non è chiusa.
2. **Recidiva = ROSSO** (gate 2). Un match al registro devia su `WF-RECIDIVA-GATE` e blocca il commit.
3. **Zero numeri inventati** (Mandato Art.2, gate 4): KPI senza dato → "nessun dato".
4. **Indipendenza** (gate 5): l'Ispettorato non ripara la run che audita; assegna via
   `isp-improvement-dispatcher` e verifica via `isp-verifier`.

---

## DONE WHEN

- Esiste `report/run/<run-id>.md` completo nel formato §8 e **firmato** da `isp-conductor`.
- Ogni errore della run è o registrato come `ERR-*` nuovo, o riconosciuto come RECIDIVA con gate ROSSO aperto.
- Il report (e l'eventuale escalation) è stato instradato da `isp-liaison-altiranghi`.
- Nessun campo del report contiene un numero inventato.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md §7-§8` — i 4 cicli + template run-report
- [[WF-RECIDIVA-GATE]] · `./WF-RECIDIVA-GATE.md` — attivato dallo step 4 su match al registro
- [[REGISTRO-ERRORI]] · `../registro/REGISTRO-ERRORI.md` — dove atterrano le voci `ERR-*`
