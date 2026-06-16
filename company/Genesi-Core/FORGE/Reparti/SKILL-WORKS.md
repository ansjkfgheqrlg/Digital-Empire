# SKILL-WORKS — FORGE (Genesi Core)

## Missione (confine: FORGE costruisce CONTENUTO, ARCHITETTURA dà la STRUTTURA)
Forgia il **contenuto** delle skill di EMPIRE OS: dato un blueprint validato da ARCHITETTURA
(forma `skill@vN`, sezioni vuote, references previste, evals attese), SKILL-WORKS scrive il
kernel reale, i file `references/`, gli esempi, gli eval-set — e prova che funziona. Non
inventa la forma (la riceve): la **riempie**, la valuta, la pacchettizza. Tre linee di lavoro:
skill nuove, miglioramento di skill esistenti (eval prima/dopo), audit anti-drift. Motore reale: `skill-creator`.

## Team agenti (quali frg-* lavorano qui)
| id | ruolo | tier |
|---|---|---|
| `frg-skill-smith` | operatore `skill-creator`: scrive kernel + references, package | sonnet |
| `frg-eval-runner` | esegue eval-set, benchmark, variance analysis (prima/dopo) | haiku |
| `frg-contradiction-gate` | `skill-contradiction-analyzer` sulla skill nuova vs le esistenti | sonnet |
| `frg-chief` | Chief-Forge: approva l'ordine in coda, chiude la consegna | opus |

## Workflow di competenza
- **WF-SKILL-NEW** — blueprint skill da ARCHITETTURA → `skill-creator init` → draft kernel + references → eval → package → install.
- **WF-SKILL-IMPROVE** — skill esistente + nuova conoscenza (da INTELLIGENCE/Memory Empire) → versione migliorata, con **eval prima/dopo** che prova il guadagno.
- **WF-SKILL-AUDIT** — `skill-contradiction-analyzer` su coppie/set di skill: gate anti-drift, obbligatorio prima di ogni rilascio.

## Funzioni L4
1. **T-draft** — riempie il kernel dentro la forma del blueprint (≤500 righe, progressive disclosure).
2. **T-references** — scrive il dettaglio in `references/` (ciò che non sta nel kernel).
3. **T-eval-runner** — costruisce ed esegue l'eval-set; la skill è buona se passa (≥85%), non se "sembra ok".
4. **T-description-optimizer** — scrive la trigger description pensando a falsi positivi/negativi.
5. **T-package** — impacchetta e installa in `.claude/skills/` (o di progetto), pronta al registro.

## Handoff Contract
- **Riceve** da ARCHITETTURA (**HC-ARCH-FORGE**): `{request_id, blueprint_ref, schema_usato:"skill@vN", spec_ref, pattern_riusati[], validazione:"PASS"}` → entra in `WF-SKILL-NEW`.
- **Costruisce**: kernel + references + evals dentro la forma vuota (mai cambia la struttura; un buco strutturale → ritorno ad ARCHITETTURA, non patch locale).
- **Consegna** a MAXIMILIAN (è all'altezza di Max?) → poi Mandato → Identity-HR/skills-map (registro). Output: `{skill_ref, eval_score, contraddizioni:"NONE", trigger_desc}`.

## Flusso interno (passi reali)
```
blueprint skill@vN (PASS) da ARCHITETTURA
  → frg-chief: ordine in coda? c'è materia prima? (memory_search intelligence/) 
  → frg-skill-smith: skill-creator init → riempie kernel dentro la forma + references/
  → frg-eval-runner: esegue eval-set → score; <85% → itera draft (max 2 cicli, poi escala)
  → frg-contradiction-gate: skill-contradiction-analyzer vs skills-map → NONE | COLLIDE
       COLLIDE → ritorna ad ARCHITETTURA (è problema di forma) o risolve contenuto
  → frg-skill-smith: package + install
  → consegna a MAXIMILIAN → Mandato → registro (skills-map + wiki tools/)
Output: forge/builds/<request_id> + skill installata e registrata
```

## Gate
- **G-SPEC** — eredita la spec validata nel blueprint (no spec → no build; la richiede ad ARCHITETTURA).
- **G-MKD/PRD** — se la skill nasce da raw, l'MKD di WORKFLOW-WORKS è prerequisito (mai saltarlo).
- **G-EVAL** — eval ≥ 85% pass, altrimenti non si consegna.
- **G-CONTRADICTION** — `skill-contradiction-analyzer` = NONE vs le skill esistenti.
- **G-REGISTRY** — skills-map + wiki aggiornati: una skill non registrata non esiste.

## shared_state / memoria (namespace forge/...)
- `forge/queue/<request_id>` — ordine di forgiatura skill (input dal blueprint ARCHITETTURA).
- `forge/builds/<request_id>` — draft, eval report, versioni (riusabile, mai buttato).
- `forge/registry/skills` — skills-map: reparto/ecosistema/stato/eval di ogni skill.
- `patterns` (ReasoningBank) — pattern di forgiatura riusati (cosa ha alzato l'eval score).

## KPI
| KPI | Target |
|---|---|
| Eval score skill nuove (skill-creator evals) | ≥ 85% pass |
| Tempo richiesta → skill consegnata (skill semplice) | ≤ 2 giorni |
| Skill rilasciate con G-CONTRADICTION = NONE | 100% |
| Skill con kernel ≤ 500 righe (progressive disclosure) | 100% |
| Copertura skills-map (zero skill orfane) | 100% |

## Connessioni
- [[../../ARCHITETTURA/Workflow/WF-ARCH-DESIGN]] — fornisce il blueprint skill@vN (HC-ARCH-FORGE)
- [[../../ARCHITETTURA/Schemi-Canonici/Schema-Skill]] — la forma vuota che questo reparto riempie
- [[WORKFLOW-WORKS]] — quando la skill nasce da raw, l'MKD arriva da qui
- [[METHOD-GUARD]] — SPARC su ogni build skill non banale; variante Claude Browser → omega-create
- [[../../../Ecosistemi/07-FORGE/Reparti/SKILL-WORKS/README]] — stub v1 di questo reparto

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 L2 SKILL-WORKS + 14-DOSSIER-ARCHITETTURA · Standard CF-grade · 2026-06-16*
