# 📐 Piano del Knowledge Pack — "Skill Planning & Architecture"

> Cartella di conoscenza estratta dalla creazione di `content-forge` (10 phase, 6 PLAN, 20 agenti, 80 test, 4 bug reali fixati).
> Combinata con principi di letteratura esistente su software/system architecture.
> **NON è una skill** — è materia prima da cui costruire una skill.

---

## 🎯 Cosa contiene

Conoscenza profonda su **come si pianifica e architetta una skill Anthropic** (e per estensione un sistema di agenti/workflow LLM). Pensato per chi vuole costruire skill **non scaffold ma production-ready**.

## 🧱 Struttura del pack

```
skill-planning-knowledge-pack/
├── KP-PLAN.md                    ← questo file (overview + indice)
│
├── 00-master/
│   └── master.md                 ← MKD narrativo unico (40-60 pagine) per chi vuole leggere tutto
│
├── 01-principles/                ← I PRINCIPI fondanti (10-12 file profondi)
│   ├── P01-iterative-planning.md
│   ├── P02-progressive-disclosure.md
│   ├── P03-no-summary-expansion.md
│   ├── P04-interactive-scaffolding.md
│   ├── P05-markdown-plus-python.md
│   ├── P06-shapes-and-canonical-forms.md
│   ├── P07-three-level-architecture.md (Kernel / Specialists / Tools)
│   ├── P08-depth-over-breadth.md
│   ├── P09-failure-modes-as-first-class.md
│   ├── P10-self-improvement-loops.md
│   ├── P11-anti-summary-cultural.md
│   └── P12-tracability-source-to-output.md
│
├── 02-patterns/                  ← PATTERN ricorrenti che funzionano (10-15 file)
│   ├── PT01-conductor-with-subagents.md
│   ├── PT02-pipeline-stages-with-handoff.md
│   ├── PT03-builder-then-optimizer.md
│   ├── PT04-question-designer-pattern.md
│   ├── PT05-canonical-files-per-target.md
│   ├── PT06-schema-tightening-loop.md
│   ├── PT07-silent-observer.md (Stage 10 SI agents)
│   ├── PT08-meta-recursive-skill.md (skill che produce skill)
│   ├── PT09-multi-source-with-tracability.md
│   ├── PT10-master-document-intermediate.md
│   └── PT11-validation-with-auto-fix.md
│
├── 03-anti-patterns/             ← Cosa NON fare (con esempi reali dai nostri errori)
│   ├── AP01-scaffold-as-deliverable.md
│   ├── AP02-permissive-schemas.md
│   ├── AP03-user-driven-overhead.md
│   ├── AP04-llm-speak-output.md
│   ├── AP05-monolithic-skill-md.md
│   ├── AP06-feature-creep-during-build.md
│   ├── AP07-skipping-the-plan.md
│   ├── AP08-no-failure-mode-doc.md
│   └── AP09-premature-optimization.md
│
├── 04-processes/                 ← PROCESSI step-by-step provati
│   ├── PR01-from-zero-to-plan.md         (le 5 versioni del PLAN, perché)
│   ├── PR02-from-plan-to-scaffold.md     (Phase 1)
│   ├── PR03-from-scaffold-to-content.md  (Phase 2)
│   ├── PR04-end-to-end-real-test.md      (Phase 7)
│   ├── PR05-depth-architecture-cycle.md  (Phase 9)
│   ├── PR06-continuous-improvement.md    (Phase 10)
│   └── PR07-versioning-and-packaging.md
│
├── 05-decision-trees/            ← Come decidere quando applicare cosa
│   ├── DT01-when-add-a-stage.md
│   ├── DT02-when-add-an-agent.md
│   ├── DT03-when-script-vs-agent.md
│   ├── DT04-when-tighten-schema.md
│   ├── DT05-when-restart-vs-iterate.md
│   └── DT06-when-call-it-done.md
│
├── 06-case-studies/              ← Storia reale di content-forge come esempio
│   ├── CS01-the-mkd-discovery.md         (perché aggiungemmo Stage 4 in v5)
│   ├── CS02-the-optimizer-team.md        (perché Phase 9)
│   ├── CS03-the-self-improvement-mistake.md (errore user-CLI, fix v1.2)
│   └── CS04-bugs-found-in-real-test.md   (4 bug Phase 9)
│
├── 07-templates/                 ← Template riusabili
│   ├── plan-template.md                  (struttura PLAN-vN)
│   ├── agent-spec-template.md            (7 file canonici)
│   ├── stage-doc-template.md
│   └── failure-mode-template.md
│
├── 08-glossary/
│   └── glossary.md               (termini chiave: MKD, KG, Stage, Ox, SI, ecc.)
│
├── 09-faq/
│   └── faq.md                    (steel-manning di domande comuni)
│
└── 10-references/                ← Letteratura esterna citata
    └── external-sources.md       (Brooks, Hickey, Fowler, Matuschak, Anthropic skill-creator, ecc.)
```

**Totale stimato**: ~50-70 file, 250-400 pagine totali.

---

## 📚 Cosa va in ogni macro-categoria

### `00-master/master.md` — MKD narrativo
Documento unico, 40-60 pagine, leggibile linearmente. Racconta tutto in forma narrativa: dal "perché si fa un piano" fino al "perché Phase 10 SI agents".

### `01-principles/` — 10-12 principi fondanti
Ognuno **5-10 pagine profonde** con: definizione canonica, perché funziona, esempi 3+, anti-pattern correlato, decision tree applicazione, riferimenti letteratura.

### `02-patterns/` — 10-15 pattern ricorrenti
Pattern operativi concreti riutilizzabili. Ognuno con: shape canonica, quando applicarlo, esempio nostro (content-forge), esempio generale (altro dominio), trade-off.

### `03-anti-patterns/` — 9 errori catalogati
Ognuno con: descrizione, perché si commette, esempio reale dal nostro percorso (es. AP03 era il bug della v1.1 user-CLI), come riconoscerlo, come ricoverarsi.

### `04-processes/` — 7 processi step-by-step
Sequenze esatte di passi, con tempo stimato, prerequisiti, output atteso, gates decisionali.

### `05-decision-trees/` — 6 decision tree operativi
Diagrammi di flusso per le domande ricorrenti ("ho bisogno di un nuovo stage?", "agente vs script?", ecc.).

### `06-case-studies/` — 4 storie reali dal nostro processo
Storie complete, ognuna 8-12 pagine, con: contesto, decisione, alternative considerate, scelta, conseguenze, lezione.

### `07-templates/` — 4 template
Scheletri vuoti con commenti guida per riapplicare i pattern.

### `08-glossary/` + `09-faq/` + `10-references/`
Standard.

---

## 🗺 Roadmap di creazione (con stima tempo)

| Step | Cosa produco | Tempo |
|---|---|---|
| **1** | KP-PLAN.md (questo file) | ✅ fatto |
| **2** | `08-glossary/` + `10-references/` (base concettuale) | 30 min |
| **3** | `01-principles/` (12 file profondi) | 2-3 h |
| **4** | `02-patterns/` (11 file mid-deep) | 2 h |
| **5** | `03-anti-patterns/` (9 file) | 1 h |
| **6** | `04-processes/` (7 file) | 1.5 h |
| **7** | `05-decision-trees/` (6 file con diagrammi) | 1 h |
| **8** | `06-case-studies/` (4 storie ricche) | 1.5 h |
| **9** | `07-templates/` (4 template) | 30 min |
| **10** | `09-faq/` (steel-manning) | 30 min |
| **11** | `00-master/master.md` (MKD narrativo finale) | 2 h |
| **12** | Audit + cross-reference + indice navigabile | 30 min |

**Totale stimato**: ~13-15 ore di lavoro focalizzato.
**Strategia consigliata**: incrementale, 1-2 categorie per sessione. Posso fare tutto in un colpo solo ma il risultato sarà meno raffinato.

---

## 🔑 I 12 principi cardine (preview)

Anticipo qui i titoli e 1 frase per ognuno così sai cosa aspettarti:

1. **Iterative Planning** — Mai un PLAN solo. Da PLAN-v1 a PLAN-v6 abbiamo iterato 6 volte; ogni iterazione catturava un'osservazione critica che il piano precedente mancava.

2. **Progressive Disclosure** — Il kernel resta snello (`SKILL.md` ≤500 righe), il dettaglio sta in `references/` caricati on-demand. Stesso principio di "lazy loading" applicato a documentazione.

3. **No-Summary, Always Expansion** — Il principio cardine anti-LLM. Ogni atomo informativo del sorgente diventa output **più ricco**, mai più povero. Anti-riassunto come postura culturale.

4. **Interactive Scaffolding** — Per artefatti complessi (agente, team, workflow), MAI generare in un colpo. Sempre PLAN → ASK → BUILD → CRITIQUE → ITERATE. La skill insegna il pattern applicandolo a sé stessa.

5. **Markdown + Python Embedded** — Il markdown è la spina, Python è il muscolo. I file `.md` contengono pseudocodice/regex/schemi Python quando aumentano chiarezza. Separazione "lettura LLM" vs "esecuzione macchina".

6. **Shapes & Canonical Forms** — Ogni target ha una **forma canonica**. La skill conosce le shape, mappa il knowledge graph sopra di esse, valida il risultato.

7. **Three-Level Architecture** — Kernel (Conductor) + Specialists (subagenti) + Tools (script Python). Ogni livello ha responsabilità specifiche, non si confondono.

8. **Depth Over Breadth** — Meglio 5 file profondi che 20 scaffold. Schemi stringenti che bloccano output magri. Validator come guardian.

9. **Failure Modes as First-Class Citizens** — Ogni agente ha `failure_modes.md` con tabella "failure | sintomo | prevenzione | rilevamento | recupero". I bug sono prevedibili.

10. **Self-Improvement Loops** — Il sistema osserva sé stesso (Stage 10 SI agents). Cattura failure mode in produzione, fa triage, genera plan futuri. **Senza azione manuale dell'utente.**

11. **Anti-Summary Cultural** — Più di un anti-pattern: una postura. Lint automatici, agenti dedicati (humanizer O4), regole esplicite. La skill DETESTA il riassunto.

12. **Traceability Source-to-Output** — Ogni atomo del sorgente è tracciabile fino all'output finale via Knowledge Graph + coverage check + formula validator. Niente perdite silenziose.

---

## 🎯 Come userai questo knowledge pack

Tre modi possibili:

**A — Lo leggi tu** (umano)
Apri `00-master/master.md` e leggi linearmente. Quando vuoi approfondire un punto, vai al file specifico in `01-principles/`. Tempo lettura completa: 8-12 ore distribuite.

**B — Lo dai a `content-forge` come sorgente**
`/forge skill-planning-knowledge-pack/ --target=skill --recursive`
→ `content-forge` lo trasforma in una skill operativa (probabilmente `skill-architect` o simile). Coverage altissima perché il pack è già strutturato.

**C — Lo usi come reference durante un altro lavoro**
Tieni la cartella aperta nel filesystem e consulti a colpo d'occhio quando devi prendere decisioni architetturali su altre skill. Glossario + decision tree + anti-pattern sono i file più consultati.

---

## ❓ Decisioni che mi servono prima di partire (3 brevi)

Tre micro-domande così non sbaglio scope ora che sai cosa otterresti.
