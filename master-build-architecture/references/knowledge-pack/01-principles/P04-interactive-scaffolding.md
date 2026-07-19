# P04 — Interactive Scaffolding

> **Definizione canonica**: Per artefatti complessi (agente, team, workflow, skill), MAI generare in un colpo solo. Sempre il loop **PLAN → ASK → BUILD → CRITIQUE → ITERATE**. La skill che produce sistemi complessi insegna il pattern **applicandolo a sé stessa**: meta-ricorsiva.

## Perché funziona

### 1. Gli artefatti complessi hanno dipendenze che emergono solo dialogando
Quando l'utente dice "voglio un agente per cold outreach", non sai ancora:
- Quali tool ha
- Chi è l'utente finale dell'agente
- Quali criteri di successo
- Failure mode noti

Generare l'agente "a freddo" significa indovinare 4-5 cose. Probabilità che indovini tutte = molto bassa.
Il dialogo costa 2 min, l'artefatto sbagliato costa ore di rifacimento.

### 2. La fase ASK è validazione gratuita
Le domande non sono solo per raccogliere input. Sono **occasione per il modello di pensare**. Una domanda ben posta forza l'utente a esplicitare assunzioni che teneva implicite.

Esempio: "Quale topologia del team preferisci?" → l'utente realizza che non aveva mai pensato alla topologia. Risparmiate ore di rilavoro.

### 3. La meta-ricorsività è cultura, non tecnica
Una skill che insegna "fai sempre PLAN→ASK→BUILD→CRITIQUE→ITERATE" ma che lei stessa genera output one-shot è **incoerente**. Gli utenti percepiscono incoerenza, perdono fiducia.

Quando la skill applica a sé stessa il pattern che predica, ottieni:
- Coerenza percepita
- Utenti imparano il pattern usando la skill
- Bug della skill emergono prima (la skill stessa ne soffre)

## Come applicarlo (operativo)

### Il loop standard (6 fasi)

```
PLAN     ── builder analizza KG/MKD, propone struttura
   ↓
ASK      ── question-designer genera domande adattive, Conductor le porge
   ↓
ARCH     ── builder scrive scaffold + contratti di interfaccia
   ↓
BUILD    ── builder riempie file canonici
   ↓
CRITIQUE ── self-critique interna (poi C1+C3 esterni)
   ↓
ITERATE  ── se issue, loop su BUILD (max 3 cicli)
```

### Quando applicare il loop completo

**Sempre per**:
- Agenti (B2)
- Team agenti (B3)
- Skill ufficiali (B4)
- Workflow (B5)
- Orchestration layer (B6)
- Custom (B8)

**Opzionale/leggero per**:
- Doc (B1) — solo PLAN + ASK lite + BUILD
- Wiki (B7) — PLAN + ASK + BUILD, no iterate elaborato (Obsidian è forgiving)

### Le domande dinamiche (non checklist statica)

ASK phase NON è "compila questo modulo". È un agente dedicato (`question-designer-agent` D1) che:
1. Legge il KG specifico del run
2. Identifica quali domande la KG già risponde (le omette)
3. Per domande che restano, propone **default ipotetici** quando può ("Propongo `<X>`. Confermi?")
4. Ordina per criticità
5. Raggruppa in batch (max 6 domande per batch)

Risultato: l'utente risponde a domande **intelligenti**, non a moduli. Velocità + qualità.

### Self-critique vs critique esterna

Distinzione cruciale:
- **Self-critique** = builder si rilegge cambiando lente, prima dell'handoff
- **Critique esterna** = altri agenti (C1, C3) validano indipendentemente

Entrambi necessari. Solo self = bias (l'agente è autore e giudice). Solo esterna = costoso (più round trip). Sequenza giusta: self-critique prima (cattura issue ovvi), critique esterna dopo (cattura issue da fresh eyes).

## Esempi

### Esempio 1 — Agent builder (B2) di content-forge

Quando spawnato per generare agente `prompt-coach`:

1. **PLAN interno**: legge KG, identifica "agent shape" (role chiaro, tool menzionati, failure mode noti)
2. **ASK** via D1: 9 domande adattive
   - Nome agente
   - Modello target (Sonnet/Opus/Haiku)
   - Tool disponibili (web_search? read_file? altri?)
   - Utente target (chi parla con l'agente?)
   - Criteri di successo
   - Failure mode noti
   - Esempio di output desiderato
   - Vincoli hard
   - Tono
3. **BUILD**: 7 file canonici nell'ordine: tools.md → agent.md → failure_modes.md → playbook.md → system_prompt.md v0 → eval_cases.json
4. **CRITIQUE** sul SP: ambiguità? contraddizioni? generic-ness?
5. **ITERATE**: fix issue, ripeti fino a OK

Tempo medio: 2-3 turni utente, 2-3 iterazioni interne. **Risultato: agente production-ready**.

### Esempio 2 — Errore evitato

Senza il loop, B2 avrebbe potuto produrre:
- system_prompt.md con riferimento a tool inesistenti (perché generati prima di chiedere)
- playbook con scenari incoerenti col TOV dichiarato
- eval_cases tutti happy path (no edge, no failure recovery)

Il loop forza ognuno di questi check.

### Esempio 3 — ➕ Pattern simile in Pair Programming

**XP — Extreme Programming**: pair programming è P04 applicato a coding. Il "driver" non scrive senza il "navigator" che fa domande tipo "hai considerato il caso X?". È PLAN+ASK+BUILD+CRITIQUE in tempo reale tra 2 umani.

Stesso meccanismo cognitivo: forzare verbalizzazione cattura bug prima che diventino code.

## Anti-pattern correlato

**AP06 — Feature creep during BUILD**: l'utente cambia idea a metà BUILD aggiungendo richieste. Builder accomoda silenziosamente, BUILD diventa caos. **Fix**: se cambio sostanziale, fermarsi, tornare a PLAN. Il loop esiste apposta.

**Anti-pattern duale**: **Over-asking** — D1 fa 30 domande prima di iniziare. L'utente si stanca, abbandona. **Fix**: max 6 domande per batch, e batch successivi solo dopo conferma utente.

## Decision tree: "applico il loop completo o versione leggera?"

```
Target output ha file canonici multipli (≥3 file)?
├─ NO → versione leggera (PLAN + BUILD + handoff)
└─ SÌ → continua
   ├─ L'output dipende da scelte utente non deducibili dal KG?
   │  (es. nome, tool, audience, registro)
   │  ├─ NO → PLAN + BUILD + CRITIQUE (no ASK)
   │  └─ SÌ → loop COMPLETO
   │
   └─ L'output ha dipendenze interne complesse?
      (es. system_prompt deve coerenziarsi con playbook + tools)
      ├─ NO → loop completo ma CRITIQUE leggera
      └─ SÌ → loop completo + CRITIQUE rigorosa + max 3 ITERATE
```

## Quando NON applicare

- **One-shot transformations**: rename file, formatter, code generation singolo. ASK è overhead.
- **Real-time chat**: latency-critical, il loop multi-turn è inadatto.
- **Batch processing**: 1000 documenti da classificare, no scelte interattive necessarie.

## Riferimenti esterni

- **Anthropic skill-creator** — Implementa P04 esplicitamente: capture intent → interview & research → write draft → test → iterate. Stesso schema.
- **XP — Extreme Programming**, Kent Beck — Pair programming come P04 between humans.
- **Design Thinking** (IDEO/Stanford d.school) — Empathize → Define → Ideate → Prototype → Test. Stessa filosofia.
- **OODA loop** (John Boyd) — Observe → Orient → Decide → Act. Cybernetics origin del pattern.

## Connessioni con altri principi

- Combina con: P10 (Self-Improvement) — il loop CRITIQUE+ITERATE è l'analogo interno del Stage 10 esterno
- Combina con: P09 (Failure Modes First-Class) — CRITIQUE checklist forza pensiero su failure prima che accadano
- Necessario per: PT08 (Meta-Recursive Skill) — senza P04, la meta-ricorsione non funziona
