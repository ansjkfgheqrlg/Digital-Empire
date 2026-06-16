# 📐 14 — ORGANO ARCHITETTURA (il nucleo strutturale della FORGE)

> Dossier v2 (fase Genesi Core, ADR-007 + direttiva Max 2026-06-16). Blueprint dell'organo
> da costruire come **STEP 1** del Genesi Core, PRIMA di completare la FORGE.
> Standard di struttura: CF-grade (§0 piano V2). Posizione: gerarchia altissima, nucleo della FORGE.
> Versione: 1.0 · Creato: 2026-06-16 · Stato: progettato (build STEP 1).

---

## 0. Missione + DONE WHEN

**Missione.** ARCHITETTURA è una **FORGE specializzata SOLO nella struttura**: prima che la
FORGE costruisca QUALSIASI artefatto (skill, agente, team, workflow, ecosistema, documento),
ARCHITETTURA ne **disegna la struttura al millimetro** e la valida. È il **fulcro del nucleo
di ogni operazione FORGE**: nessuna cosa viene forgiata senza un blueprint architettato e
approvato da qui. In termini SPARC: ARCHITETTURA possiede **Specification → Pseudocode →
Architecture**; la FORGE possiede **Refinement → Completion**. L'architetto disegna, la
fabbrica costruisce.

**Cosa NON è.** ARCHITETTURA **non** è l'architettura dell'infrastruttura Empire (quella è il
PIANO-MAESTRO + i dossier). È architettura **per-artefatto**: la struttura di *ogni singola cosa*
che nasce dalla FORGE. Non scrive il contenuto finale dell'artefatto (lo fa la FORGE), non
giudica se "è all'altezza di Max" (lo fa MAXIMILIAN), non decide se è lecito (Mandato).

**Parole di Max (2026-06-16):** *"L'architettura è il fulcro del nucleo di ogni singola
operazione che viene fatta dal forge. Un reparto + un intero ecosistema ben creato, ben
definito, ben preparato, fatto nel millimetro."*

**DONE WHEN (misurabili) — la build STEP 1 è completa quando:**
1. Esiste il reparto **+** ecosistema ARCHITETTURA in `company/` (non un solo file): org L2→L5,
   BACKBONE, namespace memoria, dossier — navigabile nell'Explorer (visibilità totale).
2. Esistono ≥8 agenti `arch-*` a schede millimetriche (identità, I/O JSON, logica, KPI, escalation, esempi).
3. La **Libreria degli Schemi Canonici** è operativa: per ogni FORMA prevista (skill, agente,
   team, principio, stile, workflow, documento/MKD, reparto, ecosistema) esiste lo schema-template
   al millimetro; la lista è estendibile con ingegno (WF-SCHEMA-EVOLVE), non è una gabbia.
4. Il workflow **WF-ARCH-DESIGN** gira end-to-end: una richiesta `{tipo, scopo, vincoli}`
   esce come **blueprint validato** pronto per la FORGE.
5. Il **gate strutturale** (`struct-gate`) è eseguibile: prende un artefatto e dice
   COMPLETO/INCOMPLETO con la lista esatta di cosa manca rispetto allo schema canonico.
6. Handoff ARCHITETTURA→FORGE definito e testato (un blueprint reale consegnato).
7. Test reale: dato "creami una skill X", ARCHITETTURA produce il blueprint millimetrico di X
   (struttura file, sezioni, progressive disclosure, references) SENZA scrivere il contenuto.

**OUT OF SCOPE.** Costruzione del contenuto (FORGE), giudizio di standard/visione (MAXIMILIAN),
enforcement regole (Mandato), esecuzione/runtime (Operations). Spese reali → ok esplicito (#3).

---

## 1. Le forme che ARCHITETTURA progetta — FORMA GIUSTA, non meccanica

**Principio cardine (Max 2026-06-16):** ARCHITETTURA NON applica la stessa forma a tutto.
Per OGNI cosa sceglie con **ingegno** la forma giusta: alcune cose sono grandi (un reparto +
un ecosistema, o anche di più), altre sono solo l'architettura di un **team**, altre un
**principio**, altre uno **stile**, altre un **workflow**, altre una **skill**. La domanda
prima di disegnare è sempre: *"qual è la forma minima-ma-completa che questa cosa richiede?"*
— mai gonfiare, mai banalizzare. Questa è la decisione più importante dell'organo.

Per ognuna di queste forme esiste un **schema canonico** (il template al millimetro):

| Forma | Schema canonico possiede… | Motore reale di riferimento |
|---|---|---|
| **Skill** | SKILL.md (frontmatter+kernel ≤500 righe), references/, progressive disclosure, evals | `skill-creator`, `Skill Master Architecture` |
| **Agente** | identità, missione, I/O concreto, tool, logica, escalation, KPI (7-file structure) | `architect-agent`, `agent-factory/agent-architect` |
| **Team** | coordinator + workers, handoff contract, shared_state schema, acceptance, failure handling | `T-org-design`, `T-handoff-contracts` |
| **Principio** | enunciato, perché, quando si applica, test di rispetto, esempi/anti-esempi | (nuovo schema — knowledge layer) |
| **Stile** | regole visive/voce, do/don't, token/pattern, esempi conformi e non | `empire-premium-style`, brand kit |
| **Workflow** | trigger, input, pipeline a passi, gate, output, owner, dry-run | SPARC, `agent-planner` |
| **Documento/MKD** | Master Knowledge Document: struttura, atomi informativi, cross-ref, mai riassunto | `content-forge` (MKD obbligatorio) |
| **Reparto** | missione, team L3/L4, workflow, handoff, gate, KPI | org-design |
| **Ecosistema** | org L1→L5 completa, BACKBONE, namespace memoria, dossier, handoff inter-eco | `ecosystem-scaffold` (da forgiare) |

La lista NON è una gabbia: se una cosa richiede una forma nuova o "di più", ARCHITETTURA la
progetta e `arch-schema-keeper` aggiunge lo schema (WF-SCHEMA-EVOLVE). Le forme leggere
(principio, stile, skill) NON ricevono il trattamento pesante di un ecosistema — sarebbe spreco.

**Regola madre (dallo standard CF), dove applicabile:** le forme con agenti (team, reparto,
ecosistema) seguono lo schema "team-canonico" — coordinator, I/O espliciti, acceptance,
escalation, shared_state. Le forme-conoscenza (principio, stile, documento) seguono lo schema
del loro tipo, non quello team-canonico. **L'ingegno sta nello scegliere lo schema giusto.**

---

## 2. Composizione — reparti L2 (l'ecosistema ARCHITETTURA)

```
ARCHITETTURA (organo, gerarchia alta — nucleo della FORGE)
├─ L2.1 SPEC & REQUIREMENTS      → la richiesta diventa spec precisa (cosa, perché, vincoli, fuori-scope)
├─ L2.2 BLUEPRINT & STRUTTURA    → la spec diventa struttura millimetrica dell'artefatto
├─ L2.3 SCHEMI CANONICI          → custodisce/versiona i 6 schemi-template (la "costituzione" delle strutture)
├─ L2.4 VALIDAZIONE STRUTTURALE  → gate: l'artefatto è strutturalmente completo/corretto? (pre e post FORGE)
└─ L2.5 PROGETTAZIONE ECOSISTEMI → disegna org chart interi L1→L5 (il livello più grande di design)
 ⊕  Pattern Guild (trasversale): libreria di pattern riusabili — anti-reinvenzione
```

---

## 3. Roster agenti L5 (schede millimetriche a build STEP 1)

Convenzione id: `arch-<ruolo>`.

| ID | Ruolo | Reparto | Tier | Funzione in una frase |
|---|---|---|---|---|
| `arch-director` | Direttore ARCHITETTURA | L1 | opus | Riceve la richiesta di design, instrada, sintetizza il blueprint finale |
| `arch-spec-writer` | Specification Writer | L2.1 | sonnet | Richiesta → spec precisa (acceptance, vincoli, out-of-scope) — motore `agent-specification`/`prd-architect-os` |
| `arch-blueprint` | Architetto-Struttura | L2.2 | opus | Spec → struttura millimetrica dell'artefatto (file, sezioni, I/O) — motore `architect-agent` |
| `arch-schema-keeper` | Custode Schemi Canonici | L2.3 | sonnet | Mantiene/versiona i 6 schemi-template; ogni nuovo artefatto parte da qui |
| `arch-validator` | Validatore Strutturale | L2.4 | sonnet | Gate `struct-gate`: completo/incompleto vs schema, lista esatta dei buchi |
| `arch-contradiction` | Anti-Contraddizione | L2.4 | sonnet | `skill-contradiction-analyzer`: il nuovo artefatto si sovrappone/contraddice l'esistente? |
| `arch-org-designer` | Progettista Ecosistemi | L2.5 | opus | Disegna org L1→L5 interi (reparti, team, handoff) — motore org-design |
| `arch-pattern-scout` | Pattern Scout | Guild | haiku | Cerca pattern/struttura già esistenti da riusare PRIMA di disegnare da zero |

**Gerarchia interna.** `arch-director` è il conductor: riceve `{tipo, scopo, vincoli}`, fa
girare spec-writer → (pattern-scout in parallelo) → blueprint contro lo schema di schema-keeper
→ validator + contradiction come gate → consegna alla FORGE. Per gli ecosistemi interi entra
`arch-org-designer`. Ogni scheda agente (build STEP 1) ha I/O JSON concreto + esempi reali.

---

## 4. Workflow CF-grade (≥3)

### WF-ARCH-DESIGN (il cuore: dalla richiesta al blueprint)
```
Input: { tipo: skill|agente|team|workflow|ecosistema|documento, scopo, vincoli, committente }
  │
  ├─ arch-pattern-scout: esiste già una struttura simile? (riusa, non reinventare)
  ├─ arch-spec-writer: spec precisa (acceptance, out-of-scope, dipendenze)
  ├─ arch-schema-keeper: carica lo SCHEMA CANONICO del tipo richiesto
  ├─ arch-blueprint: produce la STRUTTURA millimetrica (file/sezioni/I/O/handoff) contro lo schema
  ├─ arch-validator + arch-contradiction: GATE strutturale (completo? non collide?)
  └─ arch-director: sintetizza
Output: { blueprint: <struttura al millimetro>, schema_usato, spec, validazione: PASS }
   └─► HANDOFF a FORGE (che costruisce il CONTENUTO dentro questa struttura)
```
**Regola di blocco:** blueprint non validato → non si passa alla FORGE. Niente costruzione al buio.

### WF-STRUCT-VALIDATE (il gate riusabile, pre e post FORGE)
Prende un artefatto (blueprint o artefatto costruito) e ritorna `{COMPLETO|INCOMPLETO, buchi:[...]}`
rispetto allo schema canonico. Usato due volte: prima che la FORGE costruisca (il blueprint è
completo?) e dopo (l'artefatto costruito rispetta il blueprint?). È il gate strutturale della holding.

### WF-ECOSYSTEM-DESIGN (il livello massimo: progettare un ecosistema intero)
Dato un mandato del Board ("serve l'ecosistema E-commerce"), `arch-org-designer` produce l'org
L1→L5 completa + BACKBONE + namespace + bozza dossier → handoff alla FORGE (WF-ECOSYSTEM-NEW)
per la costruzione. È come ARCHITETTURA progetta gli organi che poi popoleranno l'azienda.

*(Aggiuntivo non bloccante: WF-SCHEMA-EVOLVE — quando un artefatto reale rivela un buco nello
schema canonico, lo schema si aggiorna con versione + diff; la "costituzione" delle strutture migliora.)*

---

## 5. Skill proprie (forgiate poi dalla FORGE in STEP 2, qui progettate)

| Skill | Scopo | Note |
|---|---|---|
| `arch-blueprint` | da spec → struttura millimetrica di un artefatto (i 6 tipi) | kernel + references/ con i 6 schemi |
| `canonical-schema` | libreria eseguibile dei 6 schemi-template (la costituzione delle strutture) | fonte di verità degli schemi §1 |
| `struct-gate` | gate strutturale deterministico: completo/incompleto + buchi esatti | bloccante, usato da FORGE pre/post |

Progettate con le skill di architettura esistenti (`skill-creator`, `prd-architect-os`, SPARC).
Nota bootstrap: queste skill le forgia la FORGE in STEP 2 — ma il loro **blueprint** lo produce
ARCHITETTURA in STEP 1 (l'organo progetta i propri strumenti prima che la FORGE li costruisca).

---

## 6. Relazione con FORGE, Maximilian, Mandato

- **FORGE (gemello, costruisce):** ARCHITETTURA disegna il blueprint → FORGE costruisce il
  contenuto dentro quel blueprint. Insieme = **Genesi Core**. Confine netto: struttura (qui) vs
  contenuto (FORGE). La FORGE NON inventa strutture: le chiede ad ARCHITETTURA.
- **MAXIMILIAN (sopra, standard):** dopo che la FORGE costruisce, MAXIMILIAN giudica "è
  all'altezza di Max?". ARCHITETTURA garantisce che sia *strutturalmente completo*; MAXIMILIAN
  che sia *all'altezza*. Due gate diversi, in serie.
- **Mandato (legge):** verifica che l'artefatto sia lecito/on-brand. ARCHITETTURA = forma corretta;
  Mandato = forma lecita.
- **Ciclo a 9 passi:** ARCHITETTURA opera dentro i passi 1 (SPEC) e 3 (BUILD, fase di design);
  il suo `struct-gate` è parte del passo 4 (GATE automatico).

**La catena del Genesi Core (handoff completo):**
```
richiesta → ARCHITETTURA (spec+blueprint+struct-gate) → FORGE (costruisce contenuto)
         → MAXIMILIAN (è all'altezza?) → Mandato (lecito?) → Identity-HR (registra) → VIVO
```

---

## 7. State + memoria

- **Namespace AgentDB:** `architettura/` — `architettura/schemi` (i 6 schemi canonici versionati),
  `architettura/blueprint` (ogni blueprint prodotto, ripartibile a freddo), `architettura/pattern`
  (libreria pattern riusabili della Guild), `architettura/validazioni` (esiti struct-gate).
- **State per esecuzione:** ogni WF-ARCH-DESIGN lascia un record `{richiesta, schema, blueprint,
  validazione}` ricostruibile (test amnesia): da `architettura/blueprint/<id>` si rifà il design.
- **ReasoningBank:** i buchi strutturali ricorrenti ("gli agenti dimenticano sempre l'escalation")
  diventano pattern → lo schema canonico si rafforza → la FORGE sbaglia meno.

---

## 8. Build plan (STEP 1 del Genesi Core, ciclo a 9 passi)

| Passo | Cosa |
|---|---|
| RECALL | questo dossier + FORGE dossier (06 §07) + motori reali esistenti (agent-factory, Skill Master Architecture, SPARC) |
| SPEC | DONE WHEN §0 (reparto+ecosistema, 8 agenti, 6 schemi canonici, WF-ARCH-DESIGN, struct-gate) |
| PRE-MORTEM | R1: diventa "documentazione morta" → contromisura: ogni schema/blueprint wireable a motore reale nativo, struct-gate eseguibile, non solo descritto. R2: swarm muore su limite → lotti idempotenti, naming Title-Case FISSO (lezione collisione 2026-06-16). R3: si sovrappone alla FORGE → confine §6 ferreo (struttura vs contenuto) |
| BUILD | reparto+ecosistema in `company/`; 8 agenti; 6 schemi canonici; 3 workflow; blueprint delle 3 skill (forgia in STEP 2) |
| GATE | reparto+ecosistema navigabile; 8 schede a schema; 6 schemi presenti; WF-ARCH-DESIGN descritto+eseguibile; struct-gate produce output reale |
| REVIEW | indipendente sul contenuto vs questo dossier |
| 5-bis | *MAXIMILIAN non ancora vivo (build STEP 3) → il conductor applica manualmente i tratti del corpus* |
| COMMIT | CP + STATO + wiki/log + push |
| RETRO | lezioni → corpus/ReasoningBank; schemi canonici aggiornati se emergono buchi |

---

## 9. Posizione nella gerarchia

```
LX  Mandato (legge) · MAXIMILIAN (standard/visione)
 │
GENESI CORE  ┌─ ARCHITETTURA (progetta la struttura di ogni creazione) ──┐
             └─ FORGE (costruisce il contenuto)  ◄── blueprint ──────────┘
 │
L0  Board C-Suite (regia, esecuzione)
 │
L1  i 10 ecosistemi (nascono DA Genesi Core, reparto-per-reparto, STEP 5)
```
ARCHITETTURA è **multi-tenant per definizione**: ogni creazione di ogni ecosistema, passando
dalla FORGE, passa prima da qui. È la costituzione strutturale dell'intera holding.

---

## 10. Connessioni

- [[06-ECOSISTEMI-CORE]] §07 FORGE — il gemello costruttore (ARCHITETTURA ne è il nucleo)
- [[12-DOSSIER-MAXIMILIAN]] — il gate di standard che segue il gate strutturale
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — il gate di liceità
- [[10-METODO-CICLO-FASE]] — passi 1 (SPEC), 3 (BUILD-design), 4 (GATE = struct-gate)
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0 standard CF-grade · §8 obbligo skill-architettura
- Motori reali: `architect-agent` · `prd-architect-os` · `agent-architecture` · `sparc-methodology` · `Skill Master Architecture` · `agent-factory/agent-architect`
