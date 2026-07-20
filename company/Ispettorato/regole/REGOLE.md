---
Type: CONCEPT
Status: Active
Tags: #ispettorato #regole #gate #bloccante
Created: 2026-07-20
Last updated: 2026-07-20
---

# Regole dell'Ispettorato Generale

Otto regole **bloccanti**. A differenza dei principi (che orientano), queste fermano il lavoro
quando violate. Ogni agente `isp-*` e ogni workflow le applica senza margine di trattativa. Chi le
vede violate ha il dovere di bloccare, non di segnalare e proseguire.

---

## R1 — Nessuna Run Senza Report

Una run non è chiusa finché non esiste il suo run-report nel formato §8, **firmato** da
`isp-conductor`. Un report parziale non è un report. (ARCHITETTURA §5 gate 1 · `WF-RUN-AUDIT`.)

## R2 — Nessun Report a Mano Quando la Telemetria Automatica Esiste

Da M2 in poi i report si **compilano dai dati** raccolti da `isp-telemetry-collector`, non si
scrivono a memoria. Un numero digitato a mano dove esiste un trace è un numero sospetto: va preso
dal trace o dichiarato mancante. Gli agenti interpretano; non riempiono i campi che gli script
misurano.

## R3 — Recidiva = Blocco Commit di Fase, Non Warning

Un match al `REGISTRO-ERRORI.md` (sulla causa radice) alza **gate ROSSO** e blocca il commit della
fase in corso, con escalation immediata a Board/MAXIMILIAN/Max via `isp-liaison-altiranghi`. Non
esiste "recidiva accettabile", "recidiva con nota" o "verde con riserva". (ARCHITETTURA §5 gate 2.)

## R4 — Un Errore Chiuso Non Si Riapre Senza `isp-verifier`

Lo stato di una voce `ERR-*` chiusa può cambiare **solo** dopo verifica indipendente che la
contromisura sia stata applicata davvero. Nessun agente che ha prodotto o assegnato la contromisura
può auto-dichiararla chiusa. (Indipendenza — PRINCIPI P5.)

## R5 — Il Registro Non Si Edita Retroattivamente (Tranne Append)

Le voci passate non si riscrivono per far quadrare il presente: si **aggiunge** una nota, uno stato,
un contatore. Vale per `REGISTRO-ERRORI.md`, `REGISTRO-REVISIONI.md`, `REGISTRO-SUCCESSI.md`.
(Append-only — PRINCIPI P3 · ARCHITETTURA §5 gate 3.)

## R6 — Zero Numeri Inventati

Un KPI senza dato si scrive "nessun dato"; una soglia si cita da `kpi/KPI-EMPIRE-WIDE.md` reale o
si marca `[DM]`. Un solo numero coniato a piacere invalida il report che lo contiene. (Mandato
Art.2 · PRINCIPI P4.)

## R7 — Nessun Verdetto Senza Evidenza Citata

Ogni scostamento, ogni anomalia, ogni match di recidiva punta a un evento concreto (step,
timestamp, ID voce). "Sembra a posto" e "sembra lento" non sono evidenze — come per il Gate QA di
A10 (`AG-A10-COORD`). Un verdetto non citato è nullo.

## R8 — L'Ispettorato Assegna e Verifica, Non Ripara

L'organo non entra nella catena di comando di chi costruisce: le azioni di miglioramento le esegue
il reparto owner (assegnate da `isp-improvement-dispatcher`), l'applicazione la conferma
`isp-verifier`. Un agente `isp-*` che modifica la delivery che audita ha violato l'indipendenza e va
fermato. (PRINCIPI P5 · ARCHITETTURA §5 gate 5.)

---

## Connessioni

- [[PRINCIPI]] · `../principi/PRINCIPI.md` — i sei principi che queste otto regole rendono bloccanti
- [[ARCHITETTURA]] · `../ARCHITETTURA.md §5` — i gate d'organo da cui discendono R1, R3, R5, R6, R8
- [[WF-RECIDIVA-GATE]] · `../workflow/WF-RECIDIVA-GATE.md` — dove R3, R4, R5 operano insieme
