---
Type: REPARTO
Status: Active
Tags: #reparto #agency #closing #sales-call #discovery #A8
Created: 2026-06-23
Last updated: 2026-06-23
---

# A8 — Closing / Sales-Call

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A8`
> **Standard:** CF-grade (ADR-007) · **Reparto NUOVO v2 — greenfield (TARGET-V2, non esisteva nel v1)**

---

## Missione

Presidiare il momento più critico della pipeline revenue: la call tra invio del preventivo (A3)
e firma del contratto. Nel v1 questo gap non aveva struttura — da "preventivo inviato" a
"contratto firmato" era tutto su Max, senza supporto. In v2: team di 7 agenti e 2 workflow
CF-grade che preparano ogni call con il dossier completo e apprendono da ogni esito.

**La call resta umana (Max possiede la relazione).**
**A8 possiede la PREPARAZIONE e l'APPRENDIMENTO della call.**

Il confine è netto: A8 non costruisce il preventivo (viene da A3), non scrive lo script standard
(viene da A5), non possiede la libreria obiezioni (viene da A5), non conduce la call (la conduce
Max). A8 aggrega tutto in un dossier pre-call a-prova, lo gate-a, lo consegna a Max ≥2h prima,
e dopo ogni call registra l'esito per migliorare script (A5) e preventivi (A3).

---

## Roster del reparto (7 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A8-COORD` | Coordinatore Closing | `agenti/ag-a8-coord.md` | coordinator | opus | Gestisce il pipeline post-preventivo; riporta ad AG-DIR; prepara Max per ogni call |
| `AG-A8-PREP` | Call Preparation Specialist | `agenti/ag-a8-prep.md` | worker | opus | Aggrega preventivo (A3) + dossier lead (A1) + obiezioni (A5) + script (A5) |
| `AG-A8-OBJ` | Obiezioni Anticipatore | `agenti/ag-a8-obj.md` | worker | sonnet | Simula obiezioni del prospect; risposta a-prova per ciascuna (mai claim inventati) |
| `AG-A8-SCRIPT` | Script Coach | `agenti/ag-a8-script.md` | worker | sonnet | Personalizza lo script standard (A5) per prospect + prodotto specifico |
| `AG-A8-DEBRIEF` | Post-Call Analyst | `agenti/ag-a8-debrief.md` | worker | sonnet | Dopo call Max: esito + obiezioni emerse + motivazione → log + pattern learner |
| `AG-A8-LEARN` | Closing Pattern Learner | `agenti/ag-a8-learn.md` | worker | sonnet | Analizza win/loss; pattern → A5 (script) + A3 (preventivi) + 08-INTELLIGENCE |
| `AG-A8-QA` | Verificatore Prep Call | `agenti/ag-a8-qa.md` | verifier | sonnet | Gate: dossier pre-call completo ≥2h prima call; blocca consegna a Max |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-CLOSING-PREP** | `workflow/WF-CLOSING-PREP.md` | Preparare Max per ogni call di chiusura con dossier completo: preventivo + dossier lead + obiezioni attese + script personalizzato | AG-A8-QA: dossier completo, nessun campo vuoto, prove allegate, script conforme Brand Voice, consegnato ≥2h prima |
| **WF-CLOSING-DEBRIEF** | `workflow/WF-CLOSING-DEBRIEF.md` | Apprendere da ogni call (win o loss): esito + motivazione → win→A4/A7, loss→A3 follow-up + WF-LOSS-ANALYSIS | AG-A8-QA: debrief chiuso entro 2h; motivo SEMPRE registrato |

---

## Skill del reparto

| Skill | Priorità | File / Ruolo |
|---|---|---|
| `discovery-call-brief` | Esistente, mappata | Motore di AG-A8-PREP per costruire il dossier pre-call dal lead |
| `sales-enablement` | Esistente, mappata | Materiale di supporto alla call (battle card, prove) per AG-A8-PREP/SCRIPT |
| `beast-preventivi` | Esistente (A3), handoff | A8 NON la invoca; legge l'output del preventivo prodotto da A3 |
| `closing-call-prep` | P3 (da forgiare via 07-FORGE) | Formalizza la logica PREP+OBJ+SCRIPT → vedi `skills/SKILLS.md` |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| Tasso conversione preventivo→contratto | AG-A8-COORD | N. contratti firmati / N. preventivi che arrivano a call di chiusura; baseline [DM] |
| Tempo preventivo→firma | AG-A8-COORD | Giorni medi da invio preventivo (A3) a contratto firmato; [DM] |
| Pattern obiezioni ricorrenti | AG-A8-LEARN | N. obiezioni distinte catalogate con risposta a-prova; copertura libreria A5 |
| Dossier pre-call consegnati con gate PASS ≥2h | AG-A8-QA | % dossier consegnati a Max in SLA con gate verde |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A2 Acquisizione (`ag-a2-book`) | Call prenotata + thread conversazione (HC-AG-CL-01) |
| ← riceve da | A1 Ricerca (`ag-a1-brief`, `ag-a1-icp`) | Dossier lead: profilo, audit problema, ICP, competitor |
| ← riceve da | A3 Preventivi (`ag-a3-prop`) | Preventivo inviato: scope, pricing a catalogo, prove |
| ← riceve da | A5 Copywriting-Interno (`ag-a5-obj`, `ag-a5-script`) | Libreria obiezioni + script standard da personalizzare |
| → consegna a | UMANO (Max) | Dossier pre-call completo e gated, ≥2h prima della call |
| → consegna a (WIN) | A4 Delivery (`ag-a4-coord`, `ag-a4-hand`) | Contratto firmato + scope per onboarding (HC-AG-AM-01 via A7) |
| → consegna a (LOSS) | A3 Preventivi (`ag-a3-fup`, `ag-a3-learn`) | Pattern di perdita → follow-up commerciale + WF-LOSS-ANALYSIS |
| → consegna a | 08-INTELLIGENCE | Pattern win/loss aggregati (AG-A8-LEARN) |

---

## Escalation

- Dossier pre-call non completabile ≥2h prima della call (input mancante da A1/A3) → AG-A8-COORD escala ad AG-DIR; Max informato che la call è scoperta.
- Preventivo non disponibile da A3 al momento della call → AG-A8-COORD blocca la prep e segnala ad AG-DIR (la call di chiusura senza preventivo non ha base).
- Obiezione del prospect non coperta dalla libreria A5 e senza prova disponibile → AG-A8-OBJ dichiara [DM] e segnala il gap ad AG-A8-LEARN (mai inventare una risposta — Mandato Art.2).
- Debrief non comunicato da Max entro 2h → AG-A8-COORD sollecita; call senza motivo registrato resta aperta (gate AG-A8-QA).

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A8`
- [[A3-Preventivi]] · fornitore preventivo + destinatario follow-up loss
- [[A5-Copywriting-Interno]] · fornitore libreria obiezioni e script
- [[A4-Delivery]] · destinatario contratto firmato su win
- [[WF-CLOSING-PREP]] · `workflow/WF-CLOSING-PREP.md`
- [[WF-CLOSING-DEBRIEF]] · `workflow/WF-CLOSING-DEBRIEF.md`
