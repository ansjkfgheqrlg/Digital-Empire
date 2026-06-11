# Reparto L2.5 — METHOD-GUARD (custode dei pattern)

> **Ecosistema:** 07-FORGE · **Livello:** L2 · **Owner:** Chief-Forge (`frg-chief`)
> Workflow L3: `../../Workflow/WF-SPARC-ENFORCE/`

## Cosa fa

METHOD-GUARD è la coscienza metodologica della FORGE: garantisce che OGNI build non
banale segua il metodo, e che i 13 pattern architetturali non negoziabili
(`PIANO-MAESTRO/00-PIANO-MAESTRO.md` §6) restino vivi dentro ogni artefatto forgiato.
La FORGE è custode dei pattern #1 (team canonico), #6 (skill come knowledge layer),
#7 (progressive disclosure), #8 (invarianti cardinali) — questo reparto li fa rispettare.

1. **WF-SPARC-ENFORCE** — la pipeline SPARC (Specification → Pseudocode → Architecture →
   Refinement → Completion) applicata a ogni build non banale, con i 7 agenti SPARC
   installati (`agent-specification`, `agent-planner`, `agent-researcher`,
   `agent-architecture`, `agent-coder`, `agent-tester`, `agent-reviewer`).
   `frg-sparc-warden` blocca i salti di fase.
2. **Variante Claude Browser** — per progetti/skill destinati a Claude Browser, il
   motore è **omega-create** (`System OMEGA - Creazione proggetti e skill per Claude/`),
   wrappato dentro WF-SKILL-NEW come variante target.
3. **Custodia dello schema canonico** — il template CF (coordinator, agents, I/O
   espliciti, acceptance criteria, failure handling, shared_state) è la forma
   obbligatoria di ogni team; METHOD-GUARD ne mantiene il riferimento e fa audit.

## Come si collega

| Con | Relazione |
|---|---|
| TUTTI i reparti FORGE | gate trasversale: nessuna build di SKILL-WORKS / AGENT-WORKS / WORKFLOW-WORKS / ECOSYSTEM-WORKS salta SPARC se non banale |
| Drift-Sentinel (Backbone) | METHOD-GUARD è il braccio FORGE del sentinel: segnala deviazioni dallo schema canonico |
| `Skill Master Architecture/` | reference di metodo (Three-Level Architecture) per gli audit |
| skill `sparc-methodology`, `swarm-orchestration` | strumenti operativi del reparto |
| Quality Guild | condivide checklist e criteri "banale vs non banale" |

Agenti: `frg-sparc-warden` (enforcement), `frg-spec-writer` (la fase S è sua),
`frg-org-designer` (consulente per audit schema canonico).

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Always-on dentro la FORGE: ogni ordine che entra in pipeline passa da
METHOD-GUARD per la classificazione "banale / non banale". Non ha coda propria: si
aggancia alla coda di `frg-chief` come gate.

**Ragionamento:**
1. **Classifica il task** — banale (fix 1-2 righe, config, doc minore) → SPARC non
   richiesto, fast-track. Non banale (nuova skill/agente/team/feature, refactor,
   integrazione) → SPARC obbligatorio per intero.
2. **Una fase alla volta, con gate** — S completa prima di P, P prima di A, A prima di R:
   l'output di ogni fase è il cancello della successiva. Salto rilevato → build bloccata,
   non "annotata".
3. **Il metodo serve il risultato** — se SPARC sta producendo burocrazia senza valore su
   un task borderline, frg-sparc-warden lo segnala a frg-chief con proposta di
   declassamento a banale: il metodo si applica con giudizio, ma la deroga è ESPLICITA
   e loggata, mai silenziosa.
4. **Audit a campione** — sui rilasci recenti: schema canonico rispettato? kernel ≤500
   righe? invarianti scritti? Esito → `forge/evals` + segnalazione a Drift-Sentinel.
5. **I pattern si aggiornano per ADR** — se un pattern va modificato, la strada è
   proposta → Board → ADR in `company/Memory/decisions/`; mai modifica silenziosa.

**Anti-pattern vietati:** "lo facciamo veloce e poi documentiamo" (la spec viene PRIMA);
deroghe non loggate; audit fatti dagli stessi agenti che hanno costruito (separazione
costruttore/controllore).

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 METHOD-GUARD + `00-PIANO-MAESTRO.md` §6 · Aggiornato: 2026-06-11*
