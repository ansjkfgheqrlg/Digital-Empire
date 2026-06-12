> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 METHOD-GUARD · L3 WF-SPARC-ENFORCE

# WF-SPARC-ENFORCE — Workflow L3: Enforcement Metodologia SPARC

**Ecosistema:** 07-FORGE · **Reparto:** METHOD-GUARD (L2.5) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Garantire che ogni build **non banale** della FORGE segua la pipeline SPARC
(Specification → Pseudocode → Architecture → Refinement → Completion) e che i 13
pattern architetturali non negoziabili restino vivi in ogni artefatto. Agente gate:
`frg-sparc-warden` — blocca i salti di fase, non li annota.

---

## I 7 agenti SPARC (pipeline standard)

| Agente | Fase SPARC | Responsabilità |
|---|---|---|
| `agent-specification` | S — Specification | requisiti dettagliati, acceptance criteria, edge case, out-of-scope |
| `agent-planner` | P — Pseudocode | piano ad alto livello, sequenza operazioni, punti di decisione |
| `agent-researcher` | P — Pseudocode | ricerca tecniche, pattern, precedenti; alimenta il piano |
| `agent-architecture` | A — Architecture | design sistema, interfacce, dipendenze, scelte tecniche |
| `agent-coder` | R — Refinement | implementazione (codice, contenuto, struttura) |
| `agent-tester` | R — Refinement | test, eval, verifica acceptance criteria |
| `agent-reviewer` | C — Completion | revisione finale, check schema canonico, check 13 pattern |

---

## Classificazione "banale vs non banale" (criterio di attivazione SPARC)

**Banale → fast-track (SPARC non richiesto):**
- Fix 1-2 righe in documento esistente
- Aggiornamento configurazione (nome, path, metadata)
- Documentazione minore (aggiunta entry in lista esistente)

**Non banale → SPARC obbligatorio:**
- Nuova skill, agente, team, workflow, ecosistema
- Feature nuova su sistema esistente
- Refactor che cambia interfacce o flusso
- Integrazione con sistema esterno o ecosistema diverso

In caso di dubbio: `frg-sparc-warden` classifica consultando `frg-chief`.

---

## Fasi del workflow (per build non banale)

| Fase | Gate | Chi verifica |
|---|---|---|
| **S: Specification** | spec.md completa: requisiti, acceptance, out-of-scope | `frg-sparc-warden` + `frg-chief` |
| **P: Pseudocode/Plan** | piano strutturato + ricerca completata | `frg-sparc-warden` |
| **A: Architecture** | design documentato, interfacce esplicite | `frg-sparc-warden` + `frg-org-designer` |
| **R: Refinement** | implementazione + test (almeno 1 ciclo) | `frg-eval-runner` |
| **C: Completion** | review finale schema canonico + 13 pattern | `frg-sparc-warden` + `agent-reviewer` |

**Salto di fase rilevato** → build bloccata, non "annotata". Si riparte dalla fase mancante.

---

## Variante Claude Browser (omega-create)

Per skill e progetti destinati a Claude Browser (opera nativamente in Claude.ai),
il motore è **omega-create** (`System OMEGA - Creazione proggetti e skill per Claude/`),
wrappato in WF-SKILL-NEW come variante target. Le fasi SPARC si applicano ugualmente;
cambia solo il tool nella fase R.

---

## Audit a campione (periodico)

`frg-sparc-warden` esegue audit mensile sui rilasci recenti:
- Schema canonico rispettato (coordinator + workers + I/O + acceptance + escalation)?
- Kernel ≤500 righe (progressive disclosure)?
- Invarianti cardinali scritti nel documento?

Esito → `forge/evals/sparc-audit-YYYYMMDD.md` + segnalazione a Drift-Sentinel se deviazioni.

---

## I 13 pattern verificati a completion

| # | Pattern | Verifica |
|---|---|---|
| 1 | Un team per funzionalità (coordinator+workers) | org chart presente |
| 6 | Skill come knowledge layer (agenti non inglobano conoscenza da skill) | nessun duplicato skill→agente |
| 7 | Progressive disclosure (kernel ≤500 righe) | count righe |
| 8 | Invarianti cardinali espliciti | sezione "invarianti" presente |
| 13 | Memory-first (checkpoint scritto dopo ogni task chiuso) | CP creato |

---

## KPI

| Metrica | Target |
|---|---|
| Build non banali con SPARC saltato | 0 |
| Deroghe richieste e loggate (vs deroghe silenziose) | 100% loggate |
| Audit mensile eseguito | 100% (pianificato da OPERATIONS) |
| Pass-rate schema canonico al primo audit | ≥ 90% |
