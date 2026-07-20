---
Type: ARCHITETTURA
Status: Active (M1)
Tags: #ispettorato #architettura #performance
Created: 2026-07-20
Last updated: 2026-07-20
---

# ARCHITETTURA — Ispettorato Generale

> Forma: reparto + backbone dati (dossier 15 §3). Non è un ecosistema: è un organo trasversale
> con diritto di audit su tutti gli altri.

## Missione
Misurazione, autocritica, miglioramento continuo — automatico, non a mano. Tre garanzie
(dossier 15 §1) + una quarta aggiunta 2026-07-20: **studiare i cicli di correzione** per ridurre
le revisioni necessarie nel tempo, e **studiare i successi**, non solo gli errori.

## Roster (11 agenti — dossier 15 §5, M3)
`isp-conductor`(opus) · `isp-telemetry-collector` · `isp-run-auditor` · `isp-error-registrar` ·
`isp-recidiva-sentinel` · `isp-kpi-analyst` · `isp-report-forger` · `isp-liaison-altiranghi` ·
`isp-improvement-dispatcher` · `isp-verifier` · `isp-revision-analyst` (nuovo, "primo colpo migliore").

## Workflow (5 — dossier 15 §7, M3)
`WF-RUN-AUDIT` (dopo ogni run) · `WF-DAILY-AUTOCRITICA` (ogni giorno) · `WF-RECIDIVA-GATE`
(ogni errore) · `WF-REPORT-ALTIRANGHI` (verso Board/MAXIMILIAN/Max) · `WF-REVISION-STUDY`
(dopo ogni ciclo di correzione — nuovo).

## Gate (bloccanti)
1. Nessuna run senza run-report (M2+, automatico).
2. **Recidiva = gate ROSSO.** Un errore già nel registro che si ripresenta blocca il commit
   della fase e apre escalation immediata — non è un warning, è un blocco.
3. Il registro è append-only: nessuna riscrittura retroattiva di una voce chiusa.
4. Zero numeri inventati (Mandato Art.2): un KPI senza dato dice "nessun dato", mai zero finto.
5. Indipendenza: l'Ispettorato non corregge da solo — assegna e verifica, non produce.

## Handoff
- **IN da** ogni reparto/ecosistema (telemetria run) + CF-R8 (pattern contenuti, wrappato non
  rifatto) + KNOWN ERRORS Empire Studio (migrato, non duplicato).
- **OUT verso** MAXIMILIAN (dati per il 5-bis) · Board C-Suite (KPI, guasti tecnici) ·
  reparto owner (azioni di miglioramento assegnate, dossier 15 agente 9).

## Namespace stato (AgentDB, ADR-008)
`ispettorato/errori` · `ispettorato/revisioni` · `ispettorato/successi` · `ispettorato/kpi` ·
`ispettorato/telemetry` — owner esclusivo: gli agenti isp-*. Lettura aperta a tutti.

## Connessioni
- [[15-DOSSIER-ISPETTORATO]] · [[ADR-006]] (ciclo 9 passi, aggancia RECALL/RETRO) ·
  [[ADR-008]] (intestazione) · [[REGISTRO-ERRORI]] · `company/MAXIMILIAN/ECOSISTEMA.md`
