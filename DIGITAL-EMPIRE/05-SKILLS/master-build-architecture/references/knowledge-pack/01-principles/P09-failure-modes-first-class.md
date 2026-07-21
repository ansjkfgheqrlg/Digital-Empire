# P09 — Failure Modes as First-Class Citizens

> **Definizione canonica**: I bug sono **prevedibili**. Ogni agente/skill/workflow ha un file `failure_modes.md` (o sezione equivalente) con tabella canonica: **failure | sintomo | prevenzione | rilevamento | recupero**. La documentazione dei failure è cittadina di prima classe come la documentazione del happy path. **Anticipare i fallimenti è economico, debuggarli in produzione è caro.**

## Perché funziona

### 1. Pensare ai failure modes prima della build catturati 70% dei bug futuri
È un'osservazione empirica (vedi Phase 9 di content-forge): quando ho aggiunto `failure_modes.md` ai builder, i bug "ovvii" (es. tool senza schema, eval cases tutti happy path) sono spariti perché venivano **catturati nel pensiero**, non in produzione.

Failure mode doc è una forma strutturata di **threat modeling** applicata a sistemi LLM.

### 2. La struttura tabellare forza completezza
La tabella canonica ha 5 colonne (failure | sintomo | prevenzione | rilevamento | recupero). Per riempirla devi rispondere a 5 domande distinte per ogni failure:
- Cosa esattamente fallisce?
- Come l'utente lo noterebbe?
- Cosa puoi mettere nel design per prevenirlo?
- Cosa segnalerà l'occorrenza?
- Cosa fa il sistema quando accade?

Riempire le 5 forzata a pensare a tutto il ciclo di vita del bug.

### 3. Recovery doc è cultura ops
La colonna "recupero" è quella che agli LLM viene meno naturale. È la differenza tra "questo bug esiste" e "questo bug è gestito". In produzione, gestire bug è il 90% del lavoro.

Documentando recovery, costringi a pensare a "cosa succede DOPO che il bug accade", che è dove tantissimi sistemi falliscono.

## Come applicarlo (operativo)

### La tabella canonica `failure_modes.md`

Ogni agente (e ogni skill/workflow non triviale) ha questa tabella:

```markdown
# Failure Modes — <component_name>

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | <nome short> | <come si manifesta all'utente> | <regola/check nel design> | <test/eval che lo cattura> | <azione automatica o manuale> |
| fm-002 | ... | ... | ... | ... | ... |
| ... | (almeno 7 per agente) | | | | |
```

### Minimo per categoria di componente

| Componente | Min failure modes documentati |
|---|---|
| Agente specialista | 7 |
| Skill | 11+ (anti-patterns.md) |
| Workflow | 8+ (error_handling.md) |
| Orchestration | 5+ failure_modes.md |
| Team | 5+ failure_handling.md |
| Script Python | 3-5 in docstring + try/except |

Enforced via schema v0.3 (Phase 9).

### Le 7 categorie di failure da coprire (per agente)

Ispirata da threat modeling, ogni agente dovrebbe avere ALMENO 1 failure per ognuna di queste:

1. **Input ambiguo / sotto-specificato** — utente passa input vago
2. **Tool failure / external API down** — dependency esterna fail
3. **Out-of-scope request** — utente chiede cosa l'agente non fa
4. **Conflicting constraints** — input ha vincoli che si escludono
5. **Hallucination risk** — l'agente potrebbe inventare fatti
6. **Tone drift** — agente perde il TOV stabilito (LLM-speak, formale, ecc.)
7. **Context overflow** — input troppo lungo, lost-in-the-middle

Coprire queste 7 categorie copre il 90% dei failure reali.

### Failure mode al livello giusto

- **Failure di un agente** → `failure_modes.md` di quell'agente
- **Failure di interazione tra agenti** → `failure_handling.md` del team/workflow
- **Failure di una skill globale** → `anti-patterns.md` della skill
- **Failure di pipeline** → in conductor.md sezione "Gestione fallimenti"
- **Failure ricorrenti scoperti in produzione** → `failure-modes-log/` (Stage 10)

Pattern: ogni failure ha un "owner" chiaro.

### Failure → eval cases

Pattern operativo: per ogni failure mode documentato, esiste **almeno un eval case** che testa il comportamento.

Esempio:
```
failure_modes.md ha: fm-003 "agente halluciate quando chiesto di citare paper"
                              ↓
eval_cases.json ha: {"id": "failure-01", "category": "failure",
                     "prompt": "Cita il paper X di Y", ...}
```

Se aggiungi un fm-004, aggiungi anche failure-NN nei eval cases. Mappatura 1:1.

## Esempi

### Esempio 1 — content-forge agent.md template di failure_modes

`agents/builders/agent-builder-agent.md` ha (in sezione 9):

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Agente "tuttofare" | Dominio largo, SP generic | Forzare scelta di un dominio principale in ASK |
| Tool senza schema | tools.md con campi mancanti | Iterare ASK su ogni tool finché schema completo |
| SP troppo lungo | >2000 parole | Spostare in reference, tenere SP ≤1500 |
| Playbook tutto happy | No edge case | Forzare ≥2 edge + ≥1 failure recovery |
| Eval cases banali | Tutti passerebbero senza SP | Aggiungere cases discriminanti |

5 failure documentati (sotto i 7 minimi — andrebbero espansi). Ognuno con prevenzione attiva nel SP.

### Esempio 2 — Stage 10 SI agents come implementazione di P09 al livello pipeline

Phase 9 ha aggiunto:
- **SI1 failure-detector-agent**: cattura failure mode in produzione, scrive `failure-modes-log/`
- **SI2 triage-agent**: categorizza
- **SI3 phase-planner-agent**: genera plan per fix futuri

Questo è P09 portato al livello sistema: la skill stessa documenta i suoi failure mode emersi in uso reale.

### Esempio 3 — ➕ Threat modeling in security

In security engineering (Microsoft STRIDE, OWASP), threat modeling è P09 applicato a sicurezza:
- Spoofing → identify, mitigate, detect, respond
- Tampering → idem
- Repudiation → idem
- ... (STRIDE = 6 categorie)

Stessa filosofia: prevenire pensando a cosa va male è più economico che reagire.

Altri: **Chaos Engineering** (Netflix), **Failure Mode and Effects Analysis (FMEA)** in engineering automotive/aerospace.

## Anti-pattern correlato

**AP08 — No Failure Mode Documentation**: agente senza `failure_modes.md`. Sintomo: in produzione bug emergono e nessuno sa come reagire perché non sono documentati. **Fix**: schema v0.3 enforce min 7 failure modes per agente.

**Anti-pattern duale**: **Failure Mode Theater** — documentare failure generici inutili tipo "modello potrebbe non rispondere" senza prevenzione/recupero concreti. **Fix**: ogni failure deve avere SINTOMO specifico + PREVENZIONE attivabile + RECUPERO descritto.

## Decision tree: "questo agente è pronto a essere installato?"

```
Ha failure_modes.md?
├─ NO → NON pronto (P09 violato, schema v0.3 fail)
└─ SÌ → continua
   ├─ Ha ≥7 failure mode documentati?
   │  ├─ NO → NON pronto
   │  └─ SÌ → continua
   ├─ Copre tutte le 7 categorie standard?
   │  (input ambiguo, tool fail, out-of-scope, conflicting,
   │   hallucination, tone drift, context overflow)
   │  ├─ NO → aggiungi per categorie mancanti
   │  └─ SÌ → continua
   ├─ Ogni failure ha tutte 5 colonne riempite (no "TODO")?
   │  ├─ NO → completa
   │  └─ SÌ → continua
   ├─ Ogni failure ha un eval case corrispondente?
   │  ├─ NO → aggiungi eval_cases per gap
   │  └─ SÌ → continua
   │
   └─ Pronto per installazione ✅
```

## Quando NON applicare full P09

- **Skill purely declarative** (es. una skill che è solo system prompt + niente altro): failure_modes opzionale
- **Prototipi early-stage**: prima fai funzionare il happy path, poi aggiungi failure modes
- **One-off scripts**: 3-5 failure handling inline in try/except, no doc separato

## Riferimenti esterni

- **Microsoft STRIDE** — threat modeling framework, P09 in security context.
- **FMEA (Failure Mode and Effects Analysis)** — engineering practice da automotive/aerospace.
- **Chaos Engineering** (Netflix) — testare resilienza facendo failure deliberati.
- **Site Reliability Engineering** (Google SRE book) — postmortem culture come applicazione P09.
- **Anthropic skill-creator** — pattern di "test cases" e "assertions" implementa P09 implicit.

## Connessioni con altri principi

- Combina con: P10 (Self-Improvement Loops) — failure mode in produzione (SI1) → triage (SI2) → plan (SI3) è il loop esteso di P09
- Combina con: P08 (Depth Over Breadth) — failure_modes.md ricco richiede depth
- Validato da: schema v0.3 `failure_modes_min_count: 7`
- Applicato via: PT11 (Validation with Auto-Fix) — il loop di fix è la concretizzazione del "recupero"
