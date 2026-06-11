# Reparto L2.1 — SKILL-WORKS (forgia skill)

> **Ecosistema:** 07-FORGE · **Livello:** L2 · **Owner:** Chief-Forge (`frg-chief`)
> Workflow L3: `../../Workflow/WF-SKILL-NEW/` · `../../Workflow/WF-SKILL-IMPROVE/` · `../../Workflow/WF-SKILL-AUDIT/`

## Cosa fa

SKILL-WORKS è il reparto che produce e mantiene le **skill** di EMPIRE OS — il knowledge
layer separato (pattern #6: una skill, molti agenti, molti reparti). Tre linee di lavoro:

1. **WF-SKILL-NEW** — skill nuove: richiesta → spec → `skill-creator init` → draft →
   eval → package → installazione in `.claude/skills/` (o `Digital Empire/.claude/skills/`
   se di progetto).
2. **WF-SKILL-IMPROVE** — skill esistenti + nuova conoscenza (spesso da INTELLIGENCE /
   Memory Empire) → versione migliorata, con **eval prima/dopo** per provare il guadagno.
3. **WF-SKILL-AUDIT** — `skill-contradiction-analyzer` su coppie/set di skill:
   gate anti-drift, obbligatorio prima di ogni rilascio.

Ogni skill prodotta rispetta: progressive disclosure (#7 — kernel ≤500 righe, dettaglio
in `references/`), invarianti cardinali espliciti nel kernel (#8), descrizione trigger
ottimizzata (quando si attiva e quando NO).

## Come si collega

| Con | Relazione |
|---|---|
| WORKFLOW-WORKS | quando la materia prima è raw (transcript, appunti) la skill nasce dall'MKD di content-forge, poi passa qui per eval e package |
| METHOD-GUARD | ogni build skill non banale segue SPARC; variante Claude Browser → omega-create |
| INTELLIGENCE | input: materiale già ingerito da Empire Studio; output: pagina wiki `tools/` per ogni skill |
| Identity-HR / skills-map | ogni skill rilasciata viene mappata (reparto, ecosistema, stato) — zero skill orfane |
| OPERATIONS | dichiarazione costo/tier prima del rilascio (gate budget) |

Funzioni L4 del reparto: `../../Funzioni/T-spec/` · `../../Funzioni/T-draft/` ·
`../../Funzioni/T-eval-runner/` · `../../Funzioni/T-description-optimizer/`.
Agenti: `frg-skill-smith` (operatore), `frg-eval-runner`, `frg-contradiction-gate`,
`frg-spec-writer` (in prestito da METHOD-GUARD per il G-SPEC).

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** Mai spontanea: SKILL-WORKS parte SOLO da un ordine in coda approvato da
`frg-chief` (handoff `{capability_mancante, contesto, KPI, budget}`). Trigger tipici:
un ecosistema dichiara un gap ("manca una skill per X"), il dossier 07 elenca una P0
(empire-verify, context-pack, budget-guard…), o Memory Empire propone un enrichment
che supera la soglia di sicurezza (→ entra come WF-SKILL-IMPROVE).

**Ragionamento (in ordine, nessun salto):**
1. **Esiste già?** — cerca in skills-map e registro: duplicato → reuse o extend, non creare.
2. **C'è materia prima?** — interroga INTELLIGENCE (`memory_search` namespace
   `intelligence/`): se Empire Studio ha già ingerito materiale sul tema, si parte da lì.
3. **Spec prima di tutto** — G-SPEC: cosa fa, cosa NON fa, acceptance criteria misurabili.
4. **Draft con skill-creator** — kernel minimo + references; trigger description scritta
   pensando ai falsi positivi/negativi di attivazione.
5. **Eval, non opinioni** — la skill è buona se passa gli evals (≥85%), non se "sembra ok".
6. **Contradiction check** — la skill nuova non deve contraddire le 121+ esistenti.
7. **Ship = installata + registrata** — consegna solo con G-REGISTRY chiuso e pagina wiki creata.

**Anti-pattern vietati:** skill senza eval; kernel >500 righe; descrizione trigger vaga;
modificare una skill attiva senza backup + diff + eval prima/dopo (G-SAFE-ENRICH di
INTELLIGENCE vale anche qui).

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 SKILL-WORKS · Aggiornato: 2026-06-11*
