# METHOD-GUARD — FORGE (Genesi Core)

## Missione (confine: FORGE costruisce CONTENUTO, ARCHITETTURA dà la STRUTTURA)
È la coscienza metodologica della FORGE: garantisce che il **come si costruisce il contenuto**
rispetti il metodo. ARCHITETTURA decide e valida la STRUTTURA (struct-gate); METHOD-GUARD non
duplica quel gate — presidia il **processo di costruzione** dentro la FORGE: ogni build non
banale segue SPARC (la FORGE possiede **Refinement → Completion**, ARCHITETTURA possiede
S→P→A), nessuna fase si salta, e i 13 pattern non negoziabili restano vivi in ogni artefatto
forgiato. Custodisce i pattern #1, #6, #7, #8. Motore reale: `sparc-methodology` + i 7 agenti SPARC.

## Team agenti (quali frg-* lavorano qui)
| id | ruolo | tier |
|---|---|---|
| `frg-sparc-warden` | enforcement SPARC: classifica banale/non-banale, blocca i salti di fase | haiku |
| `frg-spec-writer` | la fase S (Specification) quando la richiesta arriva senza blueprint completo | sonnet |
| `frg-eval-runner` | audit a campione sui rilasci recenti (kernel ≤500, invarianti, schema) | haiku |
| `frg-chief` | Chief-Forge: ratifica le deroghe esplicite, escala alla Board per ADR | opus |

## Workflow di competenza
- **WF-SPARC-ENFORCE** — pipeline SPARC (Specification → Pseudocode → Architecture → Refinement → Completion) su ogni build non banale, con i 7 agenti SPARC. `frg-sparc-warden` blocca i salti di fase. ARCHITETTURA copre S→P→A a monte (blueprint); METHOD-GUARD presidia R→C dentro la FORGE.
- **Variante Claude Browser** — progetti/skill per Claude Browser → motore `omega-create`, wrappato in WF-SKILL-NEW come variante target.

## Funzioni L4
1. **T-triage** — classifica ogni ordine: banale (fix 1-2 righe, config, doc minore) → fast-track; non banale → SPARC intero.
2. **T-phase-gate** — verifica che R segua A e C segua R: l'output di ogni fase è il cancello della successiva.
3. **T-pattern-audit** — audit a campione: schema canonico rispettato? kernel ≤500? invarianti scritti?
4. **T-deroga** — declassamento a banale solo ESPLICITO e loggato (mai silenzioso); ratifica `frg-chief`.
5. **T-drift-relay** — deviazioni dallo schema → segnalazione a Drift-Sentinel (Backbone) + ADR se serve.

## Handoff Contract
- **Riceve**: ogni ordine in pipeline FORGE (gate trasversale, non ha coda propria — si aggancia alla coda di `frg-chief`). Riceve anche dal blueprint ARCHITETTURA la traccia S→P→A già fatta a monte.
- **Costruisce**: non un artefatto, ma il **verdetto di metodo** — `{banale|non_banale, fase_corrente, salti_rilevati[], deroga_loggata}` — che abilita o blocca le fasi R→C dei reparti FORGE.
- **Consegna** il via libera ai reparti (SKILL/AGENT/WORKFLOW/ECOSYSTEM-WORKS) e a Drift-Sentinel l'esito audit. Un pattern da modificare → proposta → Board → ADR (mai modifica silenziosa).

## Flusso interno (passi reali)
```
ordine in coda frg-chief (+ blueprint ARCHITETTURA con S→P→A)
  → frg-sparc-warden: T-triage → banale? sì → fast-track (deroga loggata) | no → SPARC intero
  → presidio fasi R→C dentro la FORGE: R (Refinement) → C (Completion), una alla volta, con gate
       salto rilevato → BUILD BLOCCATA (non "annotata"); ritorna alla fase mancante
  → frg-eval-runner: T-pattern-audit a campione sui rilasci (kernel, invarianti, schema canonico)
       deviazione → relay a Drift-Sentinel + forge/evals
  → pattern da cambiare? → frg-chief escala a Board → ADR in company/Memory/decisions/
Output: verdetto di metodo in forge/evals/<request_id> + via libera/blocco ai reparti
```

## Gate
- **G-SPEC** — la spec viene PRIMA del codice/contenuto ("lo facciamo veloce e poi documentiamo" = vietato).
- **G-MKD/PRD** — su build documentali, l'MKD/PRD è il deliverable obbligatorio delle fasi S-P.
- **G-EVAL** — audit a campione: kernel ≤500, invarianti scritti, schema canonico rispettato.
- **G-CONTRADICTION** — separazione costruttore/controllore: l'audit non lo fa chi ha costruito.
- **G-REGISTRY** — deroghe e declassamenti loggati (mai silenziosi); modifiche pattern solo via ADR.

## shared_state / memoria (namespace forge/...)
- `forge/evals/<request_id>` — verdetti di metodo, esiti audit, salti di fase rilevati.
- `forge/method/deroghe` — log esplicito di ogni declassamento a banale (chi, perché, quando).
- `patterns` (ReasoningBank, relay) — deviazioni ricorrenti dallo schema → input a WF-SCHEMA-EVOLVE di ARCHITETTURA.
- `architettura/schemi/<forma>@<versione>` (lettura) — riferimento canonico per l'audit.

## KPI
| KPI | Target |
|---|---|
| Build non banali che seguono SPARC senza salti | 100% |
| Deroghe a "banale" loggate (mai silenziose) | 100% |
| Artefatti conformi a schema canonico all'audit a campione | ≥ 90% |
| Salti di fase rilevati e bloccati prima del Completion | 100% |
| Modifiche ai pattern fatte solo via ADR | 100% |

## Connessioni
- [[../../ARCHITETTURA/Workflow/WF-ARCH-DESIGN]] — copre S→P→A a monte; METHOD-GUARD presidia R→C
- [[../../ARCHITETTURA/Reparti/L2.4-Validazione-Strutturale]] — struct-gate strutturale (ARCHITETTURA); qui il gate è di metodo, non duplica
- [[SKILL-WORKS]] · [[AGENT-WORKS]] · [[WORKFLOW-WORKS]] · [[ECOSYSTEM-WORKS]] — gate trasversale su tutte le loro build
- [[../../ARCHITETTURA/Workflow/WF-SCHEMA-EVOLVE]] — i drift ricorrenti che rileva alimentano l'evoluzione degli schemi
- [[../../../Ecosistemi/07-FORGE/Reparti/METHOD-GUARD/README]] — stub v1 di questo reparto

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 METHOD-GUARD + 00-PIANO-MAESTRO §6 + 14-DOSSIER-ARCHITETTURA · Standard CF-grade · 2026-06-16*
