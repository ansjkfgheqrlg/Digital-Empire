# 🔨 06b — ECOSISTEMA FORGE V2 (Dossier EMPIRE OS)

> Dossier v2 (V2-2, ADR-007) — nasce dallo **SPLIT** del v1 `06-ECOSISTEMI-CORE.md` (che
> impacchettava insieme PLATFORM, FORGE, INTELLIGENCE, OPERATIONS) in **4 dossier V2
> indipendenti**, uno per ecosistema core (decisione registrata in `V2-INDEX.md` §"Proposta
> split 06-CORE"). Questo file amplia a scala CF-grade la sezione "07 · FORGE" del v1
> (righe 147-260). La **matrice di dipendenza tra i 4 core** — INTELLIGENCE → FORGE →
> PLATFORM, con OPERATIONS trasversale (v1 §Chiusura, righe 497-536) — resta il riferimento
> condiviso valido per tutti e 4 i dossier e NON viene riscritta qui: si cita, non si duplica.
>
> **Ecosistema L1 #07 della holding Digital Empire Group — uno dei 4 core trasversali** (gli
> altri: [[06a-ECOSISTEMA-PLATFORM-V2]], [[06c-ECOSISTEMA-INTELLIGENCE-V2]],
> [[06d-ECOSISTEMA-OPERATIONS-V2]]). FORGE è "compilatore + HR" di EMPIRE OS: crea, valuta,
> migliora e ritira skill, agenti, team, workflow e interi ecosistemi.
>
> **Nota meta (importante, unica per questo dossier):** FORGE è l'ecosistema che ha costruito
> — e continua a costruire — TUTTI gli altri dossier V2, **incluso questo che stai leggendo**.
> Il reparto L2.4 ECOSYSTEM-WORKS (§2) è, letteralmente, il motore che ha prodotto
> `06a-ECOSISTEMA-PLATFORM-V2.md` e `06b-ECOSISTEMA-FORGE-V2.md` stessi: FORGE si auto-descrive
> con lo stesso standard che impone agli altri. Questa è la prova di conformità più diretta
> possibile al proprio DONE WHEN (§0.4).
>
> Versione: 2.0 · Creato: 2026-07-19 · Fase roadmap: V2-2
> Supera il v1 `06-ECOSISTEMI-CORE.md` §FORGE per profondità e scala. Il v1 resta riferimento
> intatto, non toccato da questo dossier. Standard: CF-grade
> (§0 piano V2 `11-PIANO-V2-DIRETTIVA-SCALA.md`).

---

## 0. Missione + DONE WHEN

**MISSIONE (ereditata dal v1, invariata):** essere HR + R&D organizzativo della holding:
creare, valutare, migliorare e ritirare **skill, agenti, team, workflow e interi ecosistemi**.
La FORGE è il motivo per cui EMPIRE OS può crescere senza toccare l'architettura. I suoi due
motori reali sono **content-forge** (materia prima → artefatto, con MKD obbligatorio, 433
file) e **skill-creator** (creazione/miglioramento/eval di skill).

In v1 FORGE era 5 reparti con **10 agenti totali** — sotto lo standard minimo v2 anche per un
solo reparto. In v2, applicando §2 della direttiva di scala, FORGE diventa un **ecosistema a
5 reparti**, ognuno portato a team 6-10 agenti (con l'eccezione presidiata di METHOD-GUARD,
§2.5) + 1-5 workflow CF-grade. Nessun reparto nuovo si aggiunge: i 5 del v1 (SKILL-WORKS,
AGENT-WORKS, WORKFLOW-WORKS, ECOSYSTEM-WORKS, METHOD-GUARD) coprono già lo scope reale della
forgiatura organizzativa.

**DONE WHEN:**

| # | Criterio | Origine |
|---|---|---|
| 1 | Esiste una pipeline di forgiatura standard: richiesta → spec (agent-specification) → MKD/PRD → costruzione (content-forge o skill-creator) → eval → consegna → registro Identity-HR aggiornato | v1, confermato |
| 2 | Ogni nuovo artefatto rispetta lo schema team canonico (pattern #1) e progressive disclosure (#7: kernel ≤500 righe) | v1, confermato |
| 3 | Il registro Identity-HR (Backbone) elenca il 100% degli agenti con ruolo, costo, performance | v1, confermato |
| 4 | La FORGE ha creato almeno: 1 skill nuova con eval ≥ soglia, 1 team L4 completo, 1 reparto L2 per un ecosistema business | v1, confermato — **questo stesso dossier ne è evidenza diretta: 06a/06b sono prodotto del reparto L2.4 ECOSYSTEM-WORKS** |
| 5 | I 5 reparti L2 hanno org L3/L4 documentata, team a schede millimetriche (standard §0 piano V2), e almeno un workflow CF-grade eseguito end-to-end ciascuno | v2 NUOVO |
| 6 | Namespace memoria `forge/...` inizializzato; ogni workflow produce state ripartibile a freddo (test amnesia §6 piano V2) | v2 NUOVO |
| 7 | Skill proprie dell'ecosistema forgiate (≥3, vedi §6) — auto-forgiate da FORGE stessa (unico ecosistema che può auto-servirsi, standard §8 piano V2) | v2 NUOVO |

**OUT OF SCOPE (ora):** eseguire codice di produzione (→ 06a-PLATFORM); decidere budget/costo
di un nuovo agente in autonomia (dichiara la stima, l'approvazione passa da 06d-OPERATIONS
cost guard); ricerca di mercato/ICP per gli artefatti (→ 06c-INTELLIGENCE fornisce il contesto).

---

## 1. Posizione nella holding — FORGE è HR + R&D di tutti

```
                    👑 LX — Mandato Empire (schema team canonico, progressive disclosure)
                              |
L0  C-Suite ────── Chief-Forge ┤  (Chief-Forge = figura Board v2, workflow CF-grade — vedi 12-DOSSIER-MAXIMILIAN)
                              |
L1  06b-FORGE  ◄────── handoff contract ──────► tutti gli altri ecosistemi
        │
        ├── DIPENDE DA: 06c-INTELLIGENCE (materiale ingerito, pattern ReasoningBank — input per forgiare),
        │              06d-OPERATIONS (budget guard pre-approvazione per ogni nuovo agente)
        └── SERVE:    01-AGENCY        — team delivery, skill preventivi
                      02-INFO-BUSINESS  — team lancio, skill prodotto
                      03-CONTENT-FACTORY — team per formato/canale
                      04-MARKETING      — skill copy/ads nuove
                      05-MULTI-BUSINESS — interi rami nuovi (YT, Ecomm)
                      06a-PLATFORM      — nuovi agenti/skill engineering
                      06c-INTELLIGENCE  — (riceve artefatti creati → pagina wiki tools/)
                      06d-OPERATIONS    — (riceve dichiarazione tier/costo per ogni nuovo agente)
                      LX/Board          — mandato per nuovi ecosistemi interi (es. F9+: E-commerce)
```

### 1.1 Handoff espliciti — chi chiede cosa a FORGE

| Committente | Cosa richiede | Formato tipico | Reparto / Workflow destinazione |
|---|---|---|---|
| **QUALSIASI ecosistema** | Capability mancante (skill, agente, team, workflow) | `capability-request` | L2.1-L2.3 secondo target (skill/agente/workflow) |
| **06a PLATFORM** | Nuove skill/agenti engineering (es. nuova skill site-*) | `skill-nuova`, `agente-nuovo` | L2.1 SKILL-WORKS / L2.2 AGENT-WORKS |
| **04 MARKETING** | Skill copy/ads nuove (es. `empire-brand-gate`) | `skill-nuova` | L2.1 SKILL-WORKS |
| **01 AGENCY / 02 INFO-BUSINESS** | Team delivery/lancio completi | `team-nuovo` | L2.2 AGENT-WORKS / WF-TEAM-NEW |
| **05 MULTI-BUSINESS** | Interi rami nuovi (YT, Ecomm) | `ecosistema-nuovo` | L2.4 ECOSYSTEM-WORKS / WF-ECOSYSTEM-NEW (mandato Board richiesto) |
| **06c INTELLIGENCE** | Materiale raw ingerito + pattern ReasoningBank (in ingresso) | `materiale-forgiatura` | L2.3 WORKFLOW-WORKS (content-forge lo trasforma) |
| **LX/Board** | Mandato per ecosistemi interi o revisione standard organizzativo | `mandato-ecosistema`, `standard-review` | L2.4 ECOSYSTEM-WORKS / L2.5 METHOD-GUARD |

**Regola non negoziabile:** nessun ecosistema crea agenti, skill o team in autonomia. Ogni
capability nuova passa dalla FORGE (v1 §2: "QUALSIASI ecosistema → FORGE").

### 1.2 Contratto di richiesta capability (handoff contract standard)

```json
{
  "ecosistema": "01-AGENCY | 02-INFO | 03-CF | 04-MKT | 05-MB | 06a-PLT | 06c-INT | 06d-OPS",
  "gap": "descrizione della capability mancante",
  "target": "skill | agente | team | workflow | ecosistema",
  "kpi_attesi": "metrica di successo dell'artefatto una volta consegnato",
  "budget": "stima tier modello + costo/run — pre-approvazione 06d-OPERATIONS obbligatoria"
}
```

Risposta di FORGE: `{artefatto_consegnato, eval_report, registro_hr_aggiornato, workflow_eseguito}`.

**Regole del contratto (non negoziabili):**
- Richiesta senza `kpi_attesi` → `frg-spec-writer` la richiede prima di aprire la spec.
- La FORGE non inventa da zero quando esiste materia prima: prima chiede a 06c-INTELLIGENCE
  se Empire Studio ha già ingerito materiale sul tema; se sì, content-forge parte da quello
  (MKD intermedio obbligatorio, mai riassumere — espandere).
- Artefatto senza eval → non consegnabile (G-EVAL, §7).

---

## 2. Reparti L2 v2 — 5 reparti, uno "livello massimo"

Il v1 aveva già 5 reparti nominati ma con **10 agenti totali in tutto l'ecosistema**. In v2
nessun reparto nuovo si aggiunge (i 5 del v1 coprono già l'intero spettro della forgiatura:
skill → agenti → workflow → ecosistemi → metodo), ma ognuno viene portato a scala:

```
06b-FORGE (L1) — coordinatore: FRG-Chief (siede in C-Suite L0)
 ├── L2.1 SKILL-WORKS       ← forgia skill (motore: skill-creator)
 ├── L2.2 AGENT-WORKS       ← forgia agenti e team (motore: architect-agent)
 ├── L2.3 WORKFLOW-WORKS    ← forgia workflow/orchestrazioni (motore: content-forge, prd-architect-os)
 ├── L2.4 ECOSYSTEM-WORKS   ← forgia interi ecosistemi — IL LIVELLO MASSIMO (ha prodotto questo dossier)
 └── L2.5 METHOD-GUARD      ← custode dei pattern (motore: SPARC, omega-create)
```

---

### L2.1 — SKILL-WORKS (forgia skill)

**Missione:** creare, migliorare, valutare e ritirare skill — l'unità di capability più
piccola e più riusabile della holding. **Ingloba `skill-creator` come motore: non si
riscrive, si monta il wrapper di handoff sopra** (ADR-003).

**Dove il v1 era carente:** 0 agenti dedicati alla coordinazione di reparto; `frg-skill-smith`
(operatore skill-creator) era isolato senza lead, senza owner del ciclo di miglioramento
(WF-SKILL-IMPROVE) e senza un ritiro formalizzato. In v2 il reparto ha 7 agenti con lead, QA
di reparto e un ciclo completo nuovo→migliora→audita→ritira.

#### Team L2.1 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `frg-skill-lead` | Skill-Works Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; riceve la richiesta capability, assegna nuovo/migliora/audita, risponde dei KPI eval |
| `frg-skill-smith` | Skill Smith | worker | sonnet | (esistente) Operatore skill-creator: init, draft, package |
| `frg-skill-qa-lead` | Skill QA Lead | verifier | opus | **NUOVO v2:** supervisore del gate eval; decide fix mirato vs rifacimento totale; traccia eval score medi (mirror di COPY-QA-LEAD in 04-MKT) |
| `frg-description-optimizer` | Description Optimizer | worker | haiku | **NUOVO v2:** ottimizza la description della skill (T-description-optimizer) per triggering corretto |
| `frg-skill-improver` | Skill Improver | worker | sonnet | **NUOVO v2:** owner di WF-SKILL-IMPROVE — skill esistente + nuova conoscenza → versione migliorata, eval prima/dopo |
| `frg-contradiction-gate` | Contradiction Gate | verifier | sonnet | (esistente) skill-contradiction-analyzer su ogni rilascio (anti-drift) |
| `frg-eval-runner` | Eval Runner | worker | haiku | (esistente) Esegue eval skill, benchmark, variance analysis |

#### Workflow L3 di L2.1 (4 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SKILL-NEW** | Richiesta → spec (agent-specification) → skill-creator init → draft → eval → package | Eval ≥ soglia (§7); contradiction-analyzer verde |
| **WF-SKILL-IMPROVE** | Skill esistente + nuova conoscenza → versione migliorata (eval prima/dopo) | Eval dopo > eval prima; nessuna regressione |
| **WF-SKILL-AUDIT** | skill-contradiction-analyzer su coppie/set di skill (gate anti-drift) | Zero contraddizioni aperte oltre soglia tollerata |
| **WF-SKILL-RETIRE** | **NUOVO v2:** procedura di ritiro skill: deprecazione, archivio, aggiornamento registro | Skill deprecata segnalata a tutti gli ecosistemi committenti; nessun riferimento orfano |

#### Funzioni L4 di L2.1

`T-spec` (agent-specification) · `T-draft` · `T-eval-runner` · `T-description-optimizer` ·
`T-improve-diff` **[NUOVO v2]** · `T-retire-notice` **[NUOVO v2]**.

---

### L2.2 — AGENT-WORKS (forgia agenti e team)

**Missione:** costruire singoli agenti (7-file structure) e team completi (coordinator +
workers, I/O espliciti, acceptance criteria, escalation, shared_state — schema canonico CF).

**Dove il v1 era carente:** 2 agenti (`frg-org-designer`, `frg-hr-registrar`) senza un
operatore dedicato all'architect-agent, senza smoke test formalizzato e senza owner del
ritiro agente. In v2 il reparto ha 8 agenti con ciclo completo nuovo→registra→ritira.

#### Team L2.2 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `frg-agent-lead` | Agent-Works Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; assegna richieste agente-singolo vs team-completo |
| `frg-org-designer` | Org Designer | worker | opus | (esistente) Disegna org chart team/reparti/ecosistemi (schema canonico CF) |
| `frg-agent-architect` | Agent Architect | worker | sonnet | **NUOVO v2:** operatore `architect-agent` — costruisce la struttura 7-file per ogni agente nuovo |
| `frg-handoff-designer` | Handoff Designer | worker | sonnet | **NUOVO v2:** T-handoff-contracts — disegna i contratti I/O tra agenti di un team |
| `frg-shared-state-designer` | Shared-State Designer | worker | haiku | **NUOVO v2:** T-shared-state-schema — definisce lo schema di stato condiviso del team |
| `frg-agent-smoke-tester` | Agent Smoke Tester | verifier | haiku | **NUOVO v2:** smoke test del nuovo agente prima della registrazione HR |
| `frg-hr-registrar` | HR Registrar | worker | haiku | (esistente) Aggiorna Identity-HR: assume/ritira agenti, traccia costo/performance |
| `frg-agent-retire-op` | Agent Retire Operator | worker | haiku | **NUOVO v2:** procedura di ritiro agente (skill `agent-retire`): deprecazione, archivio, aggiornamento registro |

#### Workflow L3 di L2.2 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-AGENT-NEW** | architect-agent → 7-file structure → smoke test → registro HR | Smoke test verde; scheda millimetrica completa (standard §0 piano V2) |
| **WF-TEAM-NEW** | Team L3/L4 canonico: coordinator+workers, I/O, acceptance, escalation, shared_state | `frg-org-designer` approva la gerarchia; `frg-handoff-designer` verifica ogni contratto I/O |
| **WF-AGENT-RETIRE** | **NUOVO v2:** procedura di ritiro agente: deprecazione, archivio, aggiornamento registro HR | Nessun riferimento orfano nei workflow che lo usavano; registro HR coerente |

---

### L2.3 — WORKFLOW-WORKS (forgia workflow e orchestrazioni)

**Missione:** trasformare materia prima (raw) in artefatti target (doc/agent/team/skill/
workflow/orchestration/wiki/custom) via content-forge (433 file, motore reale #2), e produrre
PRD di qualità via prd-architect-os. È il reparto che genera le **strutture CF-grade** stesse
(script, gate, state.json) richieste dallo standard §0 della direttiva.

**Dove il v1 era carente:** 2 agenti (`frg-mkd-forger`, `frg-prd-architect`) senza lead di
reparto, senza verifica dedicata sulla soglia PRD (≥75/100 già dichiarata nel KPI ma senza
owner) e senza un router esplicito verso i target multipli di content-forge. In v2 il reparto
ha 7 agenti.

#### Team L2.3 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `frg-workflow-lead` | Workflow-Works Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; instrada tra content-forge (artefatto) e prd-architect-os (PRD) |
| `frg-mkd-forger` | MKD Forger | worker | sonnet | (esistente) Operatore content-forge: raw → MKD → artefatto target |
| `frg-prd-architect` | PRD Architect | worker | sonnet | (esistente) Operatore prd-architect-os: PRD tipo A-E con quality score |
| `frg-prd-qa` | PRD QA Verifier | verifier | haiku | **NUOVO v2:** verifica che il PRD raggiunga il quality score ≥75/100 prima di sbloccare la build (context score ≥60 già gate d'ingresso) |
| `frg-workflow-designer` | Workflow Designer | worker | sonnet | **NUOVO v2:** disegna la struttura CF-grade del workflow (gerarchia, gate, state.json) secondo standard §0 piano V2 |
| `frg-orchestration-builder` | Orchestration Builder | worker | sonnet | **NUOVO v2:** costruisce gli script eseguibili reali (.py/.ps1: orchestrazione, dispatch, QA) richiesti dallo standard §0 — "vietato consegnare un ruolo in un markdown" |
| `frg-content-forge-router` | Content-Forge Router | worker | haiku | **NUOVO v2:** classifica la richiesta e instrada al target content-forge corretto (doc/agent/team/skill/workflow/orchestration/wiki/custom) |

#### Workflow L3 di L2.3 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-FORGE-PIPELINE** | content-forge: raw → MKD → target (doc/agent/team/skill/workflow/orchestration/wiki/custom) | MKD intermedio SEMPRE presente (mai saltato); mai riassumere, sempre espandere |
| **WF-PRD** | prd-architect-os: PRD tipo A-E con quality score | Context score ≥60 in ingresso; quality score ≥75 in uscita (§7) |
| **WF-WORKFLOW-SCAFFOLD** | **NUOVO v2:** genera lo scheletro CF-grade completo (script/skill/state/gate) per un workflow nuovo, secondo lo standard §0 della direttiva | Scheletro contiene TUTTI i componenti minimi §0 (gerarchia, agenti, skill proprie, principi, script, QA a cancelli, state, memoria, dry-run) |

---

### L2.4 — ECOSYSTEM-WORKS (forgia interi ecosistemi — il livello massimo)

**Missione:** costruire, su mandato Board, l'organizzazione L2-L5 completa di un ecosistema
nuovo (o la sua evoluzione strutturale) — org chart, BACKBONE.md, namespace memoria, dossier.
**Questo è il reparto che ha prodotto — letteralmente — `06a-ECOSISTEMA-PLATFORM-V2.md` e
questo stesso file `06b-ECOSISTEMA-FORGE-V2.md`**: la nota meta in testa al dossier non è
retorica, è la prova operativa che il reparto funziona secondo il proprio standard.

**Dove il v1 era carente:** un solo workflow (WF-ECOSYSTEM-NEW) senza team dedicato — la
forgiatura di ecosistemi avveniva implicitamente tramite gli altri reparti FORGE. In v2 il
reparto ha 6 agenti con un ciclo esplicito scaffold→scrittura→mappa dipendenze→audit.

#### Team L2.4 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `frg-ecosystem-lead` | Ecosystem-Works Lead | coordinator | opus | **NUOVO v2:** riceve mandato Board → org L2-L5 completa + BACKBONE.md + namespace memoria + dossier |
| `frg-ecosystem-scaffolder` | Ecosystem Scaffolder | worker | sonnet | **NUOVO v2:** genera la struttura L2-L5 + BACKBONE.md (skill `ecosystem-scaffold`) |
| `frg-dossier-writer` | Dossier Writer | worker | sonnet | **NUOVO v2:** scrive i dossier V2 stessi (agente meta — ha scritto 06a e 06b applicando il template di 04-MARKETING-V2) |
| `frg-namespace-designer` | Namespace Designer | worker | haiku | **NUOVO v2:** definisce il namespace memoria (`{ecosistema}/...`) per l'ecosistema nuovo, coerente con lo schema esistente |
| `frg-dependency-mapper` | Dependency Mapper | worker | sonnet | **NUOVO v2:** mappa le dipendenze cross-ecosistema del nuovo/modificato ecosistema (matrice stile v1 §Chiusura) |
| `frg-ecosystem-qa` | Ecosystem QA Verifier | verifier | opus | **NUOVO v2:** verifica finale di conformità allo standard §0 piano V2 prima della consegna al mandante |

#### Workflow L3 di L2.4 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-ECOSYSTEM-NEW** | Mandato Board → org L2-L5 completa + BACKBONE.md + namespace memoria + dossier | `frg-ecosystem-qa` verifica conformità §0 piano V2; mandato Board formalmente chiuso |
| **WF-DOSSIER-SPLIT** | **NUOVO v2:** split di un dossier v1 che copre più ecosistemi in dossier V2 indipendenti — il workflow che ha prodotto QUESTO file da `06-ECOSISTEMI-CORE.md` | Ogni dossier figlio referenzia la matrice di dipendenza condivisa senza duplicarla; v1 resta intatto come riferimento |
| **WF-ECOSYSTEM-AUDIT** | **NUOVO v2:** verifica periodica di coerenza tra dossier v2 e stato reale costruito (blueprint vs costruito, cfr. `V2-INDEX.md`) | Report di scostamento; nessun dossier "mente" sullo stato di build |

---

### L2.5 — METHOD-GUARD (custode dei pattern)

**Missione:** garantire che ogni build non banale segua SPARC (Specification → Pseudocode →
Architecture → Refinement → Completion) e che i progetti Claude Browser passino da
omega-create. È il reparto che impedisce alla holding di regredire a "un ruolo in un
markdown chiamato agente" (principio Maximilian, §0 direttiva).

**Dove il v1 era carente:** un solo agente nominato (`frg-sparc-warden`) più 7 agenti SPARC
citati solo come riga di asset esistenti (§5 v1), senza un lead di reparto né un guardiano
esplicito dei pattern non negoziabili (#1, #6, #7, #8). In v2 il reparto ha 11 agenti: 4
nuovi + i 7 agenti SPARC esistenti wrappati (ADR-003) — sopra il "tipico 8-10" della
direttiva perché METHOD-GUARD è il reparto che valida OGNI altro reparto FORGE, quindi
richiede più superficie di controllo.

#### Team L2.5 (11 agenti: 4 nuovi + 7 SPARC wrappati)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `frg-method-lead` | Method-Guard Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; arbitra quando un build può saltare fasi SPARC (mai, salvo dry-run esplicito) |
| `frg-sparc-warden` | SPARC Warden | verifier | haiku | (esistente) Verifica che ogni build segua SPARC (S→P→A→R→C), blocca salti di fase |
| `frg-omega-operator` | Omega Operator | worker | sonnet | **NUOVO v2:** operatore `omega-create` per progetti Claude Browser |
| `frg-pattern-guardian` | Pattern Guardian | verifier | haiku | **NUOVO v2:** enforcement dei pattern non negoziabili (#1, #6, #7, #8 Piano Maestro) su ogni forgiatura, trasversale ai 4 reparti precedenti |
| `agent-specification` | Specification Agent | worker | sonnet | (esistente, wrappato ADR-003) SPARC fase 1: requisiti, acceptance, out-of-scope |
| `agent-planner` | Planner Agent | worker | sonnet | (esistente, wrappato) SPARC fase 2: pseudocode, piano d'implementazione |
| `agent-researcher` | Researcher Agent | worker | sonnet | (esistente, wrappato) Ricerca di supporto durante SPARC (in coordinamento con 06c-INTELLIGENCE) |
| `agent-coder` | Coder Agent | worker | sonnet | (esistente, wrappato) SPARC fase 4: implementazione (usato quando il target FORGE produce codice, in coordinamento con 06a-PLATFORM) |
| `agent-tester` | Tester Agent | worker | haiku | (esistente, wrappato) SPARC fase 4: test |
| `agent-reviewer` | Reviewer Agent | verifier | sonnet | (esistente, wrappato) SPARC fase 5: review completion |
| `agent-architecture` | Architecture Agent | worker | opus | (esistente, wrappato) SPARC fase 3: architettura |

#### Workflow L3 di L2.5 (2 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SPARC-ENFORCE** | sparc-methodology su ogni build non banale; omega-create per progetti Claude Browser | Nessuna fase SPARC saltata senza dry-run esplicito dichiarato |
| **WF-PATTERN-AUDIT** | **NUOVO v2:** verifica periodica che i pattern non negoziabili (#1, #6, #7, #8) siano rispettati in tutti gli artefatti consegnati dagli altri reparti FORGE | Report conformità; violazioni escalation a `frg-chief` |

---

## 3. Roster agenti completo (tutti i reparti)

### FRG-Chief (L1)

| ID | Agente | Tipo | Tier | Ruolo |
|---|---|---|---|---|
| `frg-chief` | Chief-Forge | coordinator | opus | Coordinatore ecosistema L1 (siede in C-Suite L0): approva forgiature, gestisce coda richieste, arbitra priorità tra committenti, escalation a Board |

### Conteggio roster v2

| Reparto | Agenti esistenti (dal v1) | Agenti nuovi v2 | Totale |
|---|---|---|---|
| L1 FRG-Chief | 1 (`frg-chief`) | 0 | 1 |
| L2.1 Skill-Works | 3 (`frg-skill-smith`, `frg-contradiction-gate`, `frg-eval-runner`) | 4 | 7 |
| L2.2 Agent-Works | 2 (`frg-org-designer`, `frg-hr-registrar`) | 6 | 8 |
| L2.3 Workflow-Works | 2 (`frg-mkd-forger`, `frg-prd-architect`) | 5 | 7 |
| L2.4 Ecosystem-Works | 0 | 6 | 6 |
| L2.5 Method-Guard | 8 (`frg-sparc-warden` + 7 agenti SPARC) | 3 | 11 |
| **TOTALE** | **16** | **24** | **40** |

*(Il v1 aveva 10 agenti nominati esplicitamente nel roster L5 §4, più 7 agenti SPARC citati
solo in §5 come asset — 16 agenti "esistenti" complessivi. In v2 se ne aggiungono 24 per
portare ogni reparto allo standard 6-10, con L2.5 a 11 per la sua funzione trasversale di
controllo su tutti gli altri reparti FORGE.)*

---

## 4. Workflow chiave CF-grade

### (a) Routing cross-ecosistema — flusso di ingresso principale

```
[Ecosistema committente]
   │  handoff contract {ecosistema, gap, target, kpi_attesi, budget}
   ▼
FRG-Chief ──► valida contratto (target riconosciuto? budget stimato dichiarato?)
   │            └─ budget mancante → richiesta stima a frg-spec-writer prima di procedere
   ▼
frg-*-lead di reparto ──► memory_search("forge/...") ← materiale/pattern già esistenti
   │            (regola operativa v1: "la FORGE non inventa da zero quando esiste materia prima")
   │            └─ chiede a 06c-INTELLIGENCE se Empire Studio ha già ingerito materiale sul tema
   ▼  ROUTING PER TARGET
   ├─ skill (nuova/migliora/audita)      → L2.1 SKILL-WORKS (WF-SKILL-NEW/IMPROVE/AUDIT/RETIRE)
   ├─ agente / team                      → L2.2 AGENT-WORKS (WF-AGENT-NEW/WF-TEAM-NEW)
   ├─ workflow / orchestrazione / PRD    → L2.3 WORKFLOW-WORKS (WF-FORGE-PIPELINE/WF-PRD/WF-WORKFLOW-SCAFFOLD)
   └─ ecosistema intero (mandato Board)  → L2.4 ECOSYSTEM-WORKS (WF-ECOSYSTEM-NEW/WF-DOSSIER-SPLIT)
   ▼
L2.5 METHOD-GUARD ──► WF-SPARC-ENFORCE (obbligatorio su ogni build non banale) + WF-PATTERN-AUDIT
   ▼
06d-OPERATIONS ──► pre-approvazione budget/costo del nuovo agente (v1 §2: "FORGE → OPERATIONS")
   ▼
frg-hr-registrar ──► Identity-HR aggiornato (assunzione/ritiro)
   ▼
Risposta handoff: {artefatto_consegnato, eval_report, registro_hr_aggiornato, workflow_eseguito}
   └─► hooks post-task: pagina wiki tools/ + log (06c-INTELLIGENCE) + evento costo (06d-OPERATIONS)
```

### (b) WF-SKILL-NEW — pipeline dettagliata

```
frg-skill-lead ── riceve richiesta capability, verifica non duplicazione (memory_search)
   ▼
agent-specification (L2.5, prestato) ── spec: requisiti, acceptance, out-of-scope
   ▼
frg-skill-smith ── skill-creator init → draft → package
   ▼
frg-description-optimizer ── ottimizza triggering della description
   ▼
frg-eval-runner ── eval score, benchmark, variance analysis
   ▼
frg-skill-qa-lead ──► score < soglia → iterazione mirata (frg-skill-improver, max 3, poi escalation)
   ▼
frg-contradiction-gate ── skill-contradiction-analyzer contro skill esistenti (gate anti-drift)
   ▼
frg-hr-registrar ── registro Identity-HR aggiornato
   └─► consegna al committente + pagina wiki tools/ (06c-INTELLIGENCE)
```

### (c) WF-ECOSYSTEM-NEW / WF-DOSSIER-SPLIT — il flusso meta

```
Mandato Board (LX/Board → FORGE) o decisione di split (es. V2-INDEX "Proposta split 06-CORE")
   ▼
frg-ecosystem-lead ── riceve il mandato, verifica scope (nuovo ecosistema vs split di esistente)
   ▼
agent-architecture + agent-planner (L2.5, prestati) ── architettura SPARC fase 2-3 del dossier
   ▼
frg-ecosystem-scaffolder ── struttura L2-L5 + BACKBONE.md (skill ecosystem-scaffold)
   ▼
frg-dossier-writer ── scrive il dossier V2 (template §0-12 come questo stesso file)
   ▼
frg-namespace-designer ── namespace memoria dedicato
   ▼
frg-dependency-mapper ── mappa dipendenze cross-ecosistema (referenzia, non duplica, la matrice condivisa)
   ▼
frg-ecosystem-qa ──► verifica conformità standard §0 piano V2 (schede millimetriche, non file piatti)
   ▼
Consegna al mandante + entry in V2-INDEX.md + wiki/log.md
```

---

## 5. Asset esistenti wrappati (ADR-003: mappatura + wrapper, MAI riscrittura)

| Path | Reparto L2 | Azione v2 |
|---|---|---|
| Skill `skill-creator` (anche in `Crea siti/skills/skill-creator`) | SKILL-WORKS | **USA** — motore reale #1, owner `frg-skill-smith` |
| `SKILL & Agenti/Content-forge/skill - FINALE/` (content-forge, 433 file) | WORKFLOW-WORKS | **USA** — motore reale #2, owner `frg-mkd-forger`; MKD obbligatorio |
| `Digital Empire/System OMEGA - Creazione proggetti e skill per Claude/` + skill `omega-create` | METHOD-GUARD | **USA** per progetti Claude Browser (owner `frg-omega-operator`); **WRAPPA** nel flusso WF-SKILL-NEW come variante target |
| Skill `prd-architect-os` | WORKFLOW-WORKS / WF-PRD | **USA** — owner `frg-prd-architect` |
| Skill `architect-agent` | AGENT-WORKS | **USA** — owner `frg-agent-architect` |
| `SKILL & Agenti/Skill Master Architecture/` | SKILL-WORKS | **USA** come reference di metodo (Three-Level Architecture) |
| Agenti SPARC: `agent-specification`, `agent-planner`, `agent-researcher`, `agent-coder`, `agent-tester`, `agent-reviewer`, `agent-architecture` | METHOD-GUARD | **USA** — pipeline SPARC standard, wrappati integralmente nel team L2.5 |
| Skill `sparc-methodology`, `swarm-orchestration` | METHOD-GUARD | **USA** |
| Skill `skill-contradiction-analyzer` | SKILL-WORKS / WF-SKILL-AUDIT | **USA** — gate obbligatorio, owner `frg-contradiction-gate` |
| `SKILL & Agenti/agent-factory/` | AGENT-WORKS | **EVOLVI** — valutare merge con WF-AGENT-NEW |

---

## 6. Skill NUOVE da forgiare (via FORGE stessa — unico ecosistema che si auto-serve, standard §8 piano V2)

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `forge-intake` | FRG-Chief | Form unico di richiesta capability: cattura `{ecosistema, gap, target, kpi_attesi, budget}` e instrada al reparto giusto | **ALTA** |
| `ecosystem-scaffold` | ECOSYSTEM-WORKS | Genera struttura completa L2-L5 + BACKBONE.md per un ecosistema nuovo (template da questo dossier) | **ALTA** |
| `team-canonical-template` | AGENT-WORKS | Genera team a schema fisso CF (coordinator, workers, I/O, acceptance, escalation, shared_state) | **ALTA** |
| `agent-retire` | AGENT-WORKS | Procedura di ritiro agente: deprecazione, archivio, aggiornamento registro HR — motore di `frg-agent-retire-op` | MEDIA |
| `forge-metrics` | FRG-Chief | Report trimestrale: skill create/migliorate, eval score medi, tempo di forgiatura | BASSA |
| `dossier-split` | ECOSYSTEM-WORKS | Formalizza il pattern WF-DOSSIER-SPLIT (split di un dossier v1 multi-ecosistema in N dossier V2 indipendenti) — motore di `frg-dossier-writer` | MEDIA |
| `workflow-scaffold` | WORKFLOW-WORKS | Genera lo scheletro CF-grade minimo (script/skill/state/gate) richiesto dallo standard §0 piano V2 — motore di `frg-workflow-designer` | **ALTA** |

**Regola anti-contraddizione:** prima di creare ogni skill nuova → `skill-contradiction-analyzer`
contro le esistenti. FORGE è l'unico ecosistema che forgia le proprie skill: massimo rischio
di auto-riferimento circolare — ogni skill nuova FORGE passa comunque dal gate G-CONTRADICTION
come qualsiasi altro artefatto (nessuna eccezione per sé stessa).

---

## 7. KPI + Quality Gates

### 7.1 Quality gates (bloccanti, in serie)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G-SPEC** | `agent-specification` (L2.5, prestato) | Spec approvata prima di costruire | Nessun build senza spec |
| **G-MKD/PRD** | `frg-mkd-forger` / `frg-prd-qa` | Documento intermedio completo — content-forge non salta MAI l'MKD; PRD bloccato se context score <60 | Rework del documento intermedio |
| **G-EVAL** | `frg-eval-runner` + `frg-skill-qa-lead` | Eval ≥ soglia (skill-creator evals) | Iterazione mirata (`frg-skill-improver`, max 3 cicli) → escalation umana |
| **G-CONTRADICTION** | `frg-contradiction-gate` | Analyzer verde vs skill/agenti esistenti | Blocco fino a fix; arbitrato da `frg-*-lead` di reparto se ambiguo |
| **G-REGISTRY** | `frg-hr-registrar` | HR aggiornato (100% agenti censiti) | Artefatto non consegnabile finché il registro non è coerente |
| **G-SPARC** | `frg-sparc-warden` + `frg-pattern-guardian` | Nessuna fase SPARC saltata; pattern non negoziabili #1/#6/#7/#8 rispettati | Blocco, rientro in fase mancante |

### 7.2 KPI

| KPI | Reparto | Target |
|---|---|---|
| Tempo richiesta → artefatto consegnato (skill semplice) | L2.1 | ≤ 2 giorni (v1) |
| Eval score nuove skill (skill-creator evals) | L2.1 | ≥ 85% pass (v1) |
| Artefatti conformi a schema canonico al primo audit | L2.2 | ≥ 90% (v1) |
| Copertura registro Identity-HR | trasversale | 100% agenti (v1) |
| PRD quality score (prd-architect-os) | L2.3 | ≥ 75/100 (v1) |
| Ecosistemi/dossier V2 prodotti conformi a standard §0 al primo audit | L2.4 | da misurare al primo ciclo WF-ECOSYSTEM-AUDIT — nessuna baseline storica (v2, niente numeri inventati) |
| Violazioni pattern non negoziabili rilevate / forgiature totali | L2.5 | tendente a 0; ogni violazione tracciata e chiusa (v2) |
| Skill ritirate senza riferimenti orfani residui | L2.1 | 100% (v2) |
| Gate bypass rate | trasversale | 0 (Art.4.1 Mandato) |

---

## 8. Integrazione Ruflo (TopologyOrchestration)

**Topologia:** `hierarchical` (default holding) — FRG-Chief coordinatore di ecosistema; lead
di reparto (`frg-skill-lead`, `frg-agent-lead`, `frg-workflow-lead`, `frg-ecosystem-lead`,
`frg-method-lead`) coordinatori L2. Fan-out `mesh` SOLO dentro batch paralleli (es. eval di
più varianti skill, smoke test di più agenti in un team nuovo). Decisioni cross-reparto (es.
un ecosistema nuovo richiede skill + team + workflow insieme) → orchestrate da `frg-chief`
come hive-mind (raft) tra i lead di reparto coinvolti.

| Funzione | Tool Ruflo | Uso in FORGE |
|---|---|---|
| Spawn pipeline spec→build→eval | `agent_spawn` sequenziale | Ogni agente riceve output del precedente (handoff interno WF-SKILL-NEW / WF-AGENT-NEW) |
| Fan-out valutazioni/smoke test | `swarm_init` + `task_orchestrate` | Eval di più skill in parallelo, smoke test di più agenti di un team nuovo |
| Pattern pre-forgiatura | `memory_search` | `frg-*-lead` interroga `forge/...` PRIMA di costruire da zero (regola operativa v1) |
| Salvataggio esiti | `memory_store` + hooks post-task | Eval report, PRD score, esiti audit dopo ogni run |
| Sicurezza input | `aidefence_scan` | Materiale raw in ingresso da 06c-INTELLIGENCE prima dell'elaborazione content-forge |
| State per workflow | state.json per esecuzione | Ogni workflow CF-grade produce record ripartibile a freddo (test amnesia §6 piano V2) |

---

## 9. Namespace memoria — `forge/...` (AgentDB/HNSW)

| Namespace | Contenuto | Owner |
|---|---|---|
| `forge/requests/queue` | Coda richieste capability in ingresso (forge-intake) | `frg-chief` scrive |
| `forge/skills/registry` | Registro skill create/migliorate/ritirate + eval score storico | `frg-skill-qa-lead` scrive |
| `forge/agents/hr` | Identity-HR: agenti con ruolo, costo, performance (registro condiviso con Backbone) | `frg-hr-registrar` scrive |
| `forge/teams/registry` | Team L4 forgiati, con gerarchia e contratti I/O | `frg-org-designer` scrive |
| `forge/ecosystems/scaffolds` | Scaffold ecosistemi creati/splittati (log WF-ECOSYSTEM-NEW/WF-DOSSIER-SPLIT) | `frg-ecosystem-lead` scrive |
| `forge/mkd/archive` | MKD intermedi (content-forge, mai riassunti, sempre integrali) | `frg-mkd-forger` scrive |
| `forge/prd/scores` | Storico PRD quality score per artefatto | `frg-prd-qa` scrive |
| `forge/patterns/anti-drift` | Output skill-contradiction-analyzer, contraddizioni risolte | `frg-contradiction-gate` scrive |
| `forge/handoffs/log` | Registro richieste/risposte cross-ecosistema | `frg-chief` scrive |

**Wiki-first (pattern #12 Piano Maestro):** ogni artefatto creato → pagina wiki `tools/` + log
(v1 §2: "FORGE → INTELLIGENCE"). In conflitto wiki ↔ AgentDB: vince la wiki, AgentDB si
reindicizza.

---

## 10. Build plan v2 (dentro V2-2, poi V2-6 per la build strutturale completa)

### Sequenza milestone (ordine non negoziabile: skill prima di agenti, agenti prima di ecosistemi)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **F1 — Pipeline skill** | WF-SKILL-NEW formalizzata su skill-creator; prima skill nuova = `empire-verify` (per 06a-PLATFORM) | Skill consegnata con eval verde |
| **F2 — Pipeline forgiatura + PRD** | WF-FORGE-PIPELINE collegato a Empire Studio (input = materiale ingerito da 06c-INTELLIGENCE); WF-PRD a regime | Un MKD→artefatto da materiale reale; un PRD ≥75/100 |
| **F3 — Identity-HR** | Registro agenti popolato (censimento da tutti gli ecosistemi, incl. i 45 agenti di 06a-PLATFORM appena definiti) | 100% censito |
| **F4 — Team reali** | WF-TEAM-NEW: forgiare un team L4 reale per un business (es. T-thumbnail per 05-MULTI-BUSINESS/YT) | Team operativo |
| **F5 — Ecosistema dry-run** | WF-ECOSYSTEM-NEW: dry-run sulla creazione ecosistema E-commerce (F9+ roadmap) | Scaffold completo validato |

---

## 11. Pre-mortem — rischi v2

| Rischio | Probabilità | Mitigazione |
|---|---|---|
| **Auto-riferimento circolare**: FORGE valuta se stessa con standard più bassi di quelli che impone agli altri | Media (rischio strutturale unico di questo ecosistema) | G-CONTRADICTION e G-SPARC si applicano SENZA eccezioni alle skill/dossier prodotti da FORGE stessa; `frg-ecosystem-qa` verifica ogni dossier V2 prodotto (incl. 06a/06b) contro lo standard §0 |
| **Riscrittura accidentale di content-forge o skill-creator** durante l'integrazione dei reparti | Alta | ADR-003 ferma: wrapper + registrazione, mai modifica ai file del motore; `Content-forge/skill - FINALE/` e `skill-creator` restano fonte di verità |
| **Collo di bottiglia**: tutti gli ecosistemi in coda su un solo reparto FORGE per capability urgenti | Media | Priorità nel contratto via `kpi_attesi`/urgenza dichiarata; fan-out swarm su eval/smoke test paralleli; escalation a Chief-Forge se due committenti confliggono |
| **Reparti L2.4/L2.5 percepiti come "meta, non urgenti"** (ECOSYSTEM-WORKS e METHOD-GUARD non hanno committenti diretti ricorrenti come L2.1) | Media | Non bloccano F1-F3; L2.4 ha già evidenza operativa diretta (questo dossier); L2.5 opera trasversalmente su OGNI altra forgiatura, quindi è sempre attivo anche senza richieste dirette |
| **Skill/agenti forgiati senza eval reale** (rischio di "consegna finta") | Alta senza presidio | G-EVAL non bypassabile; `frg-skill-qa-lead` traccia eval score medi come KPI di reparto pubblico |
| **Registro Identity-HR disallineato dal reale** (rischio già segnalato in `V2-INDEX.md`: ~248 agenti progettati, 19 censiti) | Alta, già in corso | F3 dedicata al censimento; `frg-hr-registrar` come owner esplicito; gate G-REGISTRY blocca la consegna di artefatti se il registro non è coerente |
| **Schede agenti v2 non millimetriche** ("è un file markdown? INACCETTABILE" — principio Maximilian) | Alta senza presidio | Standard §0 piano V2 obbligatorio per ogni agente nuovo; `frg-pattern-guardian` e `frg-ecosystem-qa` tracciano conformità su ogni forgiatura, incluse quelle di FORGE stessa |
| **Budget non dichiarato per nuovi agenti** (violazione vincolo globale zero spese senza ok) | Bassa (vincolo esplicito nel contratto) | Campo `budget` obbligatorio nel contratto §1.2; pre-approvazione 06d-OPERATIONS prima della registrazione HR |

---

## 12. Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern non negoziabili, roadmap
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0-2, §8 — direttiva suprema che governa questo dossier (ADR-007); §8 è il mandato diretto per L2.4/L2.5
- [[06-ECOSISTEMI-CORE]] — il v1 da cui si parte (§FORGE, righe 147-260); resta riferimento intatto
- [[06a-ECOSISTEMA-PLATFORM-V2]] — prodotto diretto di L2.4 ECOSYSTEM-WORKS (assieme a questo file); primo core nella catena di dipendenza a valle di FORGE
- [[06c-ECOSISTEMA-INTELLIGENCE-V2]] — fornitore di materiale ingerito e pattern ReasoningBank; FORGE non inventa da zero se INTELLIGENCE ha già materiale
- [[06d-ECOSISTEMA-OPERATIONS-V2]] — pre-approvazione budget per ogni nuovo agente; destinatario dell'evento costo
- [[04-ECOSISTEMA-MARKETING-V2]] — committente reale (skill `empire-brand-gate`, `copy-request-router`, `brand-strategy-gate` forgiate per lui — v1 §2)
- [[01-ECOSISTEMA-AGENCY-V2]] — committente team delivery/skill preventivi
- [[V2-INDEX.md]] — mappa di stato dei dossier V2; registra lo split 06-CORE eseguito da questo stesso reparto
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo; tutte le skill §5-§6 registrate qui
- [[12-DOSSIER-MAXIMILIAN]] — revisione 5-bis da V2-3: "Max approverebbe questo ecosistema?"
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement; schema team canonico come invariante cardinale custodito da FORGE
- ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG) · ADR-002 (memory-first)
