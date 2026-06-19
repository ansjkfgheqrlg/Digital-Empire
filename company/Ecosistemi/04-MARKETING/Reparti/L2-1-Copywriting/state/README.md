---
Type: CONCEPT
Status: Active
Tags: #state #copywriting #namespace #L2-1 #wrap
Created: 2026-06-18
Last updated: 2026-06-18
---

# STATE — L2.1 Copywriting

> Namespace memoria del reparto. **Nota ADR-003:** lo stato di esecuzione del copy vive nel MOTORE
> esistente (Copy Workflow Orchestration Layer). Questo è il **layer di registrazione e memoria
> semantica** v2 sopra il motore, non un suo duplicato.
> Dossier: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §9.

---

## Namespace AgentDB: `marketing/copy/...` + `marketing/avatars/...`

```
marketing/
├── copy/
│   ├── patterns/{icp}/         → pattern copy vincenti per ICP (hook, angoli, CPB che hanno performato)
│   │                             — CUORE del vantaggio cumulativo. AN4 (L2.4) scrive, COPY-MASTER legge.
│   ├── antipatterns/{icp}/     → cosa NON funziona per quell'ICP (da ReasoningBank). AN4 scrive.
│   └── scores/                 → storico score APSOC per copy_id (trend qualità). A8 / COPY-QA-LEAD scrivono.
│
└── avatars/{icp}/              → avatar completi prodotti da A2 / T-AVATAR (riuso cross-ecosistema). A2 scrive.
```

---

## Owner di scrittura (chi può scrivere cosa)

| Namespace | Scrive | Legge |
|---|---|---|
| `marketing/copy/patterns/{icp}` | AN4 (L2.4) | COPY-MASTER, tutti i writer A3-A7 |
| `marketing/copy/antipatterns/{icp}` | AN4 (L2.4) | COPY-MASTER |
| `marketing/copy/scores` | A8, COPY-QA-LEAD | COPY-QA-LEAD, AN-OBSERVER (L2.4) |
| `marketing/avatars/{icp}` | A2 | tutto il reparto + cross-ecosistema |

---

## Regole di integrità state

### Lo stato del motore resta nel motore
Lo stato di esecuzione di una run del Copy Workflow (step intermedi A1→A8) è gestito dal motore
esistente. Questo namespace conserva i RISULTATI consolidati (score finali, pattern, avatar), non
lo stato intermedio della pipeline. Confine ADR-003.

### Pattern solo con evidenza
Un pattern entra in `marketing/copy/patterns/{icp}` solo dopo conferma del loop §4b (evidenza
ripetuta, non un singolo successo). Lo scrive AN4 di L2.4, non i writer: separazione tra chi produce
e chi valida l'apprendimento (anti-deriva).

### Avatar riusabile, non duplicato
Un avatar prodotto da A2 per un ICP è riusato cross-ecosistema (01-AGENCY, 02-INFO, 03-CF). Non si
ricostruisce da zero se esiste in namespace: si aggiorna. Riuso = coerenza + risparmio.

### Wiki-first sui pattern forti
I pattern consolidati con evidenza forte vengono ANCHE scritti in pagine wiki (`concepts/` o
`synthesis/`) + entry `wiki/log.md`. In conflitto wiki ↔ AgentDB vince la wiki; AgentDB si reindicizza
(Art.5.2 Mandato).

---

## Stato corrente (2026-06-18 — fase V2-2)

| Namespace | Stato | Note |
|---|---|---|
| `marketing/copy/patterns/` | DA INIZIALIZZARE | Si popola dal primo loop §4b su copy reale (M6 dossier) |
| `marketing/copy/scores/` | DA INIZIALIZZARE | Parte dal primo copy gated reale (M1-M2) |
| `marketing/avatars/` | DA INIZIALIZZARE | Primo avatar al primo handoff con `icp` (es. 01-AGENCY outreach) |

---

## Connessioni

- [[README]] · `README.md`
- [[copy-master]] · `agenti/copy-master.md`
- [[a2-target-analyst]] · `agenti/a2-target-analyst.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[kpi/KPI]] · `kpi/KPI.md`
- [[state/README]] (L2.4 Analytics, owner dei pattern) · `company/Ecosistemi/04-MARKETING/Reparti/L2-4-Analytics/state/README.md`
