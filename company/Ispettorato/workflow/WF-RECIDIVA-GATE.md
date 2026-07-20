---
Type: WORKFLOW
Status: Active
Tags: #workflow #ispettorato #recidiva #gate #bloccante
Created: 2026-07-20
Last updated: 2026-07-20
---

# WF-RECIDIVA-GATE — Il Gate del "Mai Due Volte"

- **ID**: `WF-RECIDIVA-GATE`
- **Trigger**: **OGNI ERRORE trovato** (da `WF-RUN-AUDIT` o da qualsiasi audit) — dossier 15 §7.
- **Output atteso**: nuovo → voce `ERR-*` + contromisura assegnata · noto → **gate ROSSO** + escalation immediata.
- **Owner**: `isp-recidiva-sentinel` (decide), `isp-conductor` (custode del gate).

---

## Scopo

Garantire che **lo stesso errore non passi due volte**. Ogni errore individuato viene confrontato
con la memoria (`REGISTRO-ERRORI.md`): se è nuovo, si registra e si assegna una contromisura; se è
già noto, è una **recidiva** — cioè il fallimento di una contromisura promessa — e scatta un blocco,
non un avviso. È il ciclo "OGNI ERRORE" della direttiva Max.

---

## Precondizioni

- Esiste un errore candidato con almeno sintomo + causa radice candidata (da `isp-run-auditor` o
  `isp-error-registrar`).
- Il `REGISTRO-ERRORI.md` è accessibile e append-only.

---

## Step

| # | Agente | Azione | Gate |
|---|---|---|---|
| 1 | `isp-recidiva-sentinel` | Confronta l'errore con **ogni** voce del `REGISTRO-ERRORI.md`, match sulla **causa radice** (non solo sul testo del sintomo). Include i KNOWN ERRORS Empire Studio migrati. | Un match declassato a "nuovo" è il fallimento del compito: rispetta P2. |
| 2a | `isp-error-registrar` | **Ramo NUOVO** → crea voce `ERR-YYYYMMDD-NNN`: sintomo · causa radice · contromisura · owner · stato. Append-only. | Nessuna voce senza causa radice (o `causa-da-determinare`). |
| 2b | `isp-improvement-dispatcher` | **Ramo NUOVO** → assegna la contromisura al reparto owner con scadenza e criterio di verifica. | La contromisura deve avere owner + scadenza, altrimenti non è assegnata. |
| 3a | `isp-conductor` | **Ramo NOTO/RECIDIVA** → alza **gate ROSSO bloccante**: blocca il commit della fase in corso. | Nessun "verde con riserva", nessuna "recidiva accettabile". Rosso è rosso. |
| 3b | `isp-liaison-altiranghi` | **Ramo NOTO/RECIDIVA** → **escalation immediata** a Board/MAXIMILIAN/Max con l'ID della voce colpita e lo storico dei tentativi di contromisura. | L'escalation non aspetta il daily: parte subito. |
| 4 | `isp-verifier` | Chiude il loop: la contromisura (nuova o ri-assegnata) è stata applicata **davvero**? Solo lui riapre o chiude una voce del registro. | Nessuna voce chiusa senza verifica indipendente dell'applicazione reale. |

---

## Gate del workflow (bloccanti)

1. **Recidiva = gate ROSSO** (ARCHITETTURA §5 gate 2): blocca il commit di fase, non è un warning.
2. **Escalation immediata** su recidiva: percorso diretto agli alti ranghi via `isp-liaison-altiranghi`.
3. **Append-only** (gate 3): la voce nota non si riscrive; si aggiorna stato/contatore e nota,
   la riapertura passa solo da `isp-verifier`.
4. **Zero numeri inventati** (Mandato Art.2): il contatore di ricorrenze riflette il registro reale.

---

## DONE WHEN

- **Ramo NUOVO**: esiste una nuova `ERR-*` completa nel registro e la contromisura è assegnata a un
  owner con scadenza da `isp-improvement-dispatcher`.
- **Ramo NOTO**: gate ROSSO alzato (commit di fase bloccato) + escalation consegnata agli alti
  ranghi + voce esistente aggiornata (stato/contatore) senza riscrittura retroattiva.
- In entrambi i rami, `isp-verifier` sa quale contromisura dovrà verificare a chiusura.

---

## Connessioni

- [[REGISTRO-ERRORI]] · `../registro/REGISTRO-ERRORI.md` — la memoria contro cui gira il gate
- [[WF-RUN-AUDIT]] · `./WF-RUN-AUDIT.md` — il chiamante tipico (step 4) di questo workflow
- [[isp-recidiva-sentinel]] · `../agenti/isp-recidiva-sentinel.md` — l'agente che decide NUOVO vs NOTO
