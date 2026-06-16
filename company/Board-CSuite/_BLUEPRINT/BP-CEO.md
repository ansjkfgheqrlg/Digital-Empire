# BLUEPRINT — CEO / Empire-Conductor (figura C-level = workflow CF-grade)

> Prodotto da ARCHITETTURA (WF-ARCH-DESIGN, ARCH-BOARD-20260616). Per FORGE (build contenuto).
> Forma: **figura C-level = cartella-workflow** (peso PESANTE). NON un file, NON un reparto semplice.

## Forma scelta + perché
Una figura C-level non è un agente: è un'**organizzazione di governo**. Coordina decisioni
cross-ecosistema, regge il consenso, è l'ultimo gate verso il Mandato. Serve un team con un
decisore + analisti + arbitri + verificatori + memoria → forma cartella-workflow (≥10 agenti).

## Missione della figura
Orchestratore supremo della holding: propone le decisioni cross-ecosistema, regge il consenso
raft del Board, arbitra le priorità tra ecosistemi, ha il voto decisivo in stallo, ed è il gate
finale verso il Mandato (LX) e la review di MAXIMILIAN. NON esegue il lavoro degli ecosistemi.

## Struttura cartella (che la FORGE costruirà)
```
Board-CSuite/CEO-Empire-Conductor/
├── README.md  ARCHITETTURA.md
├── agenti/ (10)   principi/  regole/   skills/   scripts/   workflow/ (≥2)   kpi/  state/
```

## Roster agenti (10) — ruolo + tier
| Agente | Ruolo | Tier |
|---|---|---|
| ceo-conductor | decisore principale, propone e chiude il consenso | opus |
| ceo-analista-strategico | analizza scenari prima delle decisioni | opus |
| ceo-advisor-rischi | mappa i rischi di ogni opzione | sonnet |
| ceo-advisor-opportunita | mappa upside/opportunità | sonnet |
| ceo-priorita-arbiter | arbitra conflitti di priorità tra ecosistemi | opus |
| ceo-budget-allocator | alloca risorse macro (in handoff col CFO) | sonnet |
| ceo-okr-tracker | traccia OKR/obiettivi trimestrali della holding | haiku |
| ceo-comunicatore | traduce le decisioni in direttive verso gli ecosistemi | sonnet |
| ceo-verificatore | verifica che le decisioni siano eseguite davvero | sonnet |
| ceo-memoria | storico decisioni, pattern, coerenza con ADR attivi | haiku |

## Workflow CF-grade della figura (≥2)
- `WF-DECISIONE-STRATEGICA` — input cross-ecosistema → analisi (strategico+rischi+opportunità) → proposta → consenso raft → Mandato gate → ADR + dispatch.
- `WF-REVIEW-TRIMESTRALE` — raccoglie KPI/OKR da tutte le figure → diagnosi → priorità del trimestre → direttive.
- `WF-ARBITRATO-PRIORITA` — due ecosistemi in conflitto su risorse/scope → arbitro → decisione tracciata.

## Skill proprie (forgia FORGE)
`board-consensus` (regge il voto raft + quorum) · `decision-record` (ogni decisione → ADR + STATO) · `okr-tracker`.

## Handoff
- → **Mandato (LX)**: ogni decisione passa il gate di liceità prima del dispatch.
- → **MAXIMILIAN**: review 5-bis sulle decisioni di scala/standard.
- ← **tutte le 6 figure**: voti, KPI, escalation. → **tutti gli ecosistemi**: direttive eseguibili.

## KPI presidiati
Decisioni cross-eco chiuse senza stallo · tempo proposta→decisione · % direttive eseguite (verificatore) · coerenza ADR (0 contraddizioni).

## Struct-gate checklist (verifica post-build FORGE)
- [ ] ≥10 schede agente complete (I/O, logica, escalation) · [ ] ≥2 workflow CF-grade · [ ] principi/+regole/ presenti
- [ ] skill proprie ≥3 · [ ] scripts dispatch/report · [ ] kpi/+state/ · [ ] 0 file <15 righe, 0 cartelle vuote

## Note per la FORGE
Riusare il contenuto del v1 `Board-CSuite/CEO-Empire-Conductor.md` (consenso raft, voto decisivo, Mandato gate) come base di `ceo-conductor` + README. Espandere, non riassumere.

## Connessioni
- [[BP-INDEX]] · [[14-DOSSIER-ARCHITETTURA]] · [[12-DOSSIER-MAXIMILIAN]] · [[13-DOSSIER-MANDATO-ECOSISTEMA]]
