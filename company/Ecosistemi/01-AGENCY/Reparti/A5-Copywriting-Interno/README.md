---
Type: REPARTO
Status: Active
Tags: #reparto #agency #copywriting #apsoc #obiezioni #script #A5
Created: 2026-07-11
Last updated: 2026-07-11
---

# A5 — Copywriting Interno

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `mesh` piccolo (writer ↔ objection ↔ qa)

---

## Missione

Produrre il **copy operativo quotidiano** dell'agency con il framework **APSOC**: template
email/DM, micro-copy dei preventivi, script per le call. A5 è anche il custode della
**libreria delle obiezioni reali**, alimentata dalle conversazioni vere di A2.

A5 è il **consumatore-adattatore locale**: i pezzi grandi (sales page, sequenze lunghe, refresh
strutturali) si chiedono a 04-MARKETING via `HC-AG-MK-01`. Il **Gate Bibbia non è riscritto qui**:
è lo stesso gate di A2, riusato via cross-link (pattern 6 — una skill, molti reparti; ADR-003).

---

## Roster del reparto (6 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A5-COORD` | Coordinatore Copy | `agenti/ag-a5-coord.md` | coordinator | sonnet | Riceve il brief, orchestra il mesh writer ↔ objection ↔ qa, riporta ad AG-DIR |
| `AG-A5-WRITE` | APSOC Writer | `agenti/ag-a5-write.md` | worker | sonnet | Scrittura e variazione del copy (skill `cro-copy-architect`, `market-copy`) |
| `AG-A5-OBJ` | Objection Librarian | `agenti/ag-a5-obj.md` | worker | sonnet | Libreria obiezioni reali → risposte testate **con prove** |
| `AG-A5-SCRIPT` | Script Writer Call | `agenti/ag-a5-script.md` | worker | sonnet | Script discovery + chiusura per A8-Closing |
| `AG-A5-LEARN` | Copy Performance Analyst | `agenti/ag-a5-learn.md` | worker | sonnet | Analizza il reply rate per template → propone varianti → alimenta `agency/outreach` |
| `AG-A5-QA` | Verificatore Gate Bibbia | `agenti/ag-a5-qa.md` | verifier | sonnet | **Bloccante**: riusa il Gate Bibbia di A2 (`../A2-Acquisizione/agenti/ag-a2-qa.md`) |

---

## Workflow del reparto (2 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-COPY-REFRESH** | `workflow/WF-COPY-REFRESH.md` | Refresh data-driven dei template: analisi reply reali → 3 varianti APSOC per canale → gate → rollout graduale (batch 10% + A/B) | AG-A5-QA: Gate Bibbia PASS su ogni variante prima del test |
| **WF-SCRIPT-CALL** | `workflow/WF-SCRIPT-CALL.md` | Script discovery e chiusura per nicchia, con obiezioni attese e risposte testate | AG-A5-QA: no claim senza prova, no dependency-language, brand voice conforme |

---

## Gate del reparto — Gate Bibbia (riusato da A2)

**Presidio: AG-A5-QA. Bloccante — nessun copy esce senza gate verde.**
Il gate **non è duplicato**: A5 invoca lo stesso motore di A2 (pattern 6, ADR-003 wrap-not-rewrite).

| # | Check | FAIL se |
|---|---|---|
| 1 | **Struttura APSOC** | Manca una sezione APSOC, o la Soluzione precede il Problema |
| 2 | **CTA corretta** | CTA assente, errata o doppia |
| 3 | **No dependency-language** | Linguaggio che crea dipendenza dall'agenzia, o promesse non provabili |

**Regola obiezioni (Mandato Art.2 — prove, non promesse):** ogni risposta nella libreria deve
avere il campo `prova` popolato (riferimento a conversazione reale o esito misurato). Senza
prova → stato `non_validata`, **non rilasciabile**. Nessuna risposta inventata entra in libreria.

**Escalation:** copy bocciato per 3 cicli → AG-A5-COORD verifica se il brief è difettoso o il
target sbagliato; se serve un pezzo strutturale → `HC-AG-MK-01` a 04-MARKETING. Nessun dato
reale disponibile → A5 **non produce**: segnala il gap ad A2.

---

## KPI del reparto

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| % copy passato al Gate Bibbia al primo giro | AG-A5-QA | Output PASS al primo tentativo / tot prodotti | [DM] |
| Tempo brief→copy | AG-A5-COORD | Ore da brief a copy gated, per tipo standard (email, DM, script) | [DM] |
| Uplift reply rate post-refresh | AG-A5-LEARN | Delta reply rate variante adottata vs template precedente | [DM] |
| Risposte obiezione con prova | AG-A5-OBJ | Risposte con campo `prova` popolato / tot in libreria | Target 100% |

Dettaglio completo → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A2-Acquisizione | Dati di reply reali (reply rate, motivi) + obiezioni grezze anonimizzate |
| ← riceve da | A3-Preventivi | Pattern di loss commerciale → alimentano la libreria obiezioni |
| ← riceve da | A8-Closing | Pattern win/loss dalle call → affinamento degli script |
| ← riceve da | A6-Marketing-Interno | Case study e proof reali da usare come prove nel copy |
| ← riceve da | 08-INTELLIGENCE | `HC-AG-IN-01` — obiezioni aggregate e verificate |
| ← riceve da | 04-MARKETING | `HC-AG-MK-01` — pezzi strutturali grandi (sales page, sequenze lunghe) |
| → consegna a | A2-Acquisizione | Template aggiornati e **gated**, pronti per la run |
| → consegna a | A8-Closing | Script discovery/chiusura + libreria obiezioni per la prep call |

---

## Namespace AgentDB

**Chiave canonica: `agency/a5`** — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a5/templates` | Template attivi per canale + versione + stato gate | AG-A5-WRITE |
| `agency/a5/performance` | Reply rate per variante, esito A/B, decisione adozione/scarto | AG-A5-LEARN |
| `agency/a5/obiezioni` | Libreria obiezioni reali (anonimizzate) → risposte testate con prove | AG-A5-OBJ |
| `agency/a5/script` | Script discovery + chiusura per nicchia, stato gate, consegna ad A8 | AG-A5-SCRIPT |

In lettura: `agency/outreach` (performance per variante) e `agency/a2/reply` (obiezioni grezze).

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md` (gate riusato · prove obbligatorie)
- Stato e ripartibilità a freddo → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, flussi, confini, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A5`
- [[ag-a5-qa]] · `agenti/ag-a5-qa.md` — verificatore che riusa il Gate Bibbia
- [[ag-a2-qa]] · `../A2-Acquisizione/agenti/ag-a2-qa.md` — motore del gate (pattern 6)
- [[WF-COPY-REFRESH]] · `workflow/WF-COPY-REFRESH.md`
- [[WF-SCRIPT-CALL]] · `workflow/WF-SCRIPT-CALL.md`
- [[A8-Closing]] · destinatario degli script call gated
