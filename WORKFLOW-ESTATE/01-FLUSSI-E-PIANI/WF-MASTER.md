# WF-MASTER — Orchestratore della settimana (21→26/07/2026)
> Owner: chief-forge · Ricorre: continuo · Config macchina: `workflows.yaml`
> Unico compito: far eseguire il MASTER PLAN (P7) rispettando gates, coda swarm, memoria.

## Loop giornaliero
```
09:00  leggi dashboard (07-CONTROL) → gate di oggi? → brief mentale 5'
09:30  corsia Max (finestra contatti S1) · corsia Gael (build in sequenza P7)
19:00  WF-MEM-EOD: metriche → dashboard → checkpoint EOD → segnala slittamenti
```

## Regole di orchestrazione
1. **Revenue-first**: contesa risorse → vince il task con €/h più alto (P4 tabella).
2. **Coda swarm**: max 1 pesante (Opus) → ordine S1 > S2 > S6 > S5; il resto degradato a esecuzione singola.
3. **Gate discipline**: al deadline il gate si marca 🟢/🔴 e si applica il kill-criterio (P5 §2). Nessun gate "quasi verde".
4. **Default-decision enforcement**: veto scaduto → la decisione passa ad ATTIVA → si nota in dashboard e si procede.
5. **Zero-surprise memory**: qualsiasi cosa chiuda/cambi/fallisca → atomo di memoria corrispondente.

## Mappa gate (specchietto rapido)
| Gate | Deadline | 🟢 se | 🔴 → azione |
|---|---|---|---|
| DEC | 21/07 20:00 | DEC-001 ATTIVA | impossibile (auto-default) |
| FUNNEL | 22/07 20:00 | test €1 OK | fallback checkout (≤2h) |
| CONTATTI | 23/07 12:00 | 7/7 contattati | follow-up delegato + push S2 compensa |
| S4 | 24/07 20:00 | E2E auto OK | mentalita.brutale STANDBY |
| S5 | 23/07 18:00 | Fliki OK | ladder video → altrimenti slitta |
| REV | 26/07 | ≥1 anticipo incassato | RETRO causa radice → pattern correttivi |

## Dipendenze (da P3 DAG)
DEC-001→(landing, email) · audit→(bio S3, config S4) · DEC-002→kit S6 · case-study→outreach S6 · Fliki-test→WF-S5 · DEC-004→WF-S5.

## Handoff memoria
Ogni venera... no: **ogni sera h19:00** — `checkpoint --task EOD-<data> --note "gate: ... slittamenti: ..."`. Domenica 26/07 → WF-MEM-RETRO.

---
⛓️ P12: `WF-MASTER#estate-2026` · orchestra: WF-S1..S6, WF-MEM-* · fonti: PLANNING-P7, ARCHITETTURA
