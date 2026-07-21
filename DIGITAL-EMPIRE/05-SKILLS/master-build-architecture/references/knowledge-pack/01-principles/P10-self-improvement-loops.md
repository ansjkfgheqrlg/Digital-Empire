# P10 — Self-Improvement Loops

> **Definizione canonica**: Il sistema osserva sé stesso in produzione, cattura failure mode emergenti, fa triage automatico, genera plan per fix futuri. **Tutto autonomo, l'utente non agisce**. Loop silenzioso e condizionale che produce **memoria istituzionale** dei problemi reali. Diverso da fixare bug immediati: è continuous improvement strutturato.

## Perché funziona

### 1. I bug reali emergono solo in produzione
Phase 7 di content-forge ha fatto un test end-to-end "vero" su contenuto reale e ha trovato 2 bug che nessun unit test avrebbe scoperto. Phase 9 ne ha trovati altri 4 facendo regression.

Pattern: i bug più costosi sono quelli che emergono **mentre il sistema fa il lavoro reale**, non quelli previsti.

Per catturarli serve **osservazione continua** dell'uso reale. P10 formalizza questa osservazione.

### 2. L'overhead di "remember to log" è quello che uccide tutti i sistemi di feedback
Sistemi che richiedono all'utente di scrivere bug report manualmente, eseguire script, ricordarsi di documentare → fail nel medio termine. Ho sbagliato proprio questo in v1.1 di content-forge: avevo costruito `scripts/log_failure.py --quick "..."` da eseguire a mano. Tu giustamente hai detto: **"io non lo farò"**.

L'unico sistema di feedback che funziona è quello che **non richiede azione**.

### 3. Memoria istituzionale > memoria umana
Tra 3 mesi non ricorderai i piccoli problemi che hai notato oggi. Il sistema sì, se ha scrittura automatica. Pile di FM accumulati → quando hai tempo di fare improvement, hai dati reali su cui basarti.

## Come applicarlo (operativo)

### I 3 agenti SI (Self-Improvement) di content-forge

| Agente | Trigger | Cosa fa |
|---|---|---|
| **SI1 failure-detector-agent** | Solo se QA fail/warn O feedback utente negativo O Ox warnings | Logga FM in `failure-modes-log/logged/` |
| **SI2 triage-agent** | Solo se `count(logged/) ≥ 3` | Auto-classifica: severity/category/scope/confidence/effort |
| **SI3 phase-planner-agent** | Solo se soglie raggiunte (≥3 major, ≥1 blocker, ≥5 totali) | Genera silenziosamente `PHASE-N-CANDIDATES.md` |

Tutti spawnati dal Conductor in **Stage 10** del pipeline (l'ultimo, post-packaging). Silenzioso e condizionale = overhead zero quando nulla è successo.

### I 4 principi cardinali di SI

**1. Silenzio operativo**: nessuna notifica "ehi ho trovato un problema!". Lavoro in background, file lasciati lì per consultazione futura.

**2. Condizionalità**: agenti spawnati solo se condizione vera. Run smooth = SI non gira.

**3. Tutto JSON**: i tool che gli agenti chiamano ritornano JSON parsabile. Niente dialogo con l'utente.

**4. User pull, non system push**: l'utente chiede quando vuole ("Forge, cosa hai trovato?"), il sistema risponde leggendo i file. Mai il sistema interrompe.

### Workflow dell'utente in P10

```
Tu usi /forge normalmente
   │
   ├─ Stage 1-9 → output normale
   │
   └─ Stage 10 → silenzioso, automatico, condizionale
        │
        ├─ Se qualcosa è andato male: SI1 logga
        ├─ Se accumulo soglia: SI2 tria
        └─ Se soglie meta: SI3 genera plan

Dopo settimane/mesi, quando vuoi:

Tu: "Forge, hai trovato problemi?"
Conductor: legge failure-modes-log/INDEX.md, ti riassume.

Tu: "Forge, hai preparato un piano per la prossima phase?"
Conductor: controlla se esiste PHASE-N-CANDIDATES.md, te lo mostra.
```

### Soglie

Decise per **bilanciare segnali e rumore**:
- ≥1 blocker → hotfix immediato (non aspettare phase)
- ≥3 major in stessa categoria → cluster → priority alta
- ≥3 major totali → massa critica per phase mirata
- ≥5 FM totali → refactor generico utile

Sotto queste soglie: SI3 non genera plan (sarebbe rumore).

### Architettura file

```
failure-modes-log/
├── README.md           ← agent-managed (l'utente non tocca)
├── TEMPLATE.md         ← usato da SI1 come template
├── INDEX.md            ← rigenerato automaticamente
├── logged/             ← FM scritti da SI1 (waiting triage)
├── triaged/            ← FM analizzati da SI2 (waiting plan)
├── resolved/           ← FM fixati in phase precedenti
└── PHASE-N-CANDIDATES.md  ← generato da SI3 quando soglie OK
```

Tool: `scripts/log_failure.py` con 4 modi:
- `--quick "desc" --auto ...` (SI1)
- `--triage --auto ...` (SI2)
- `--check-thresholds` (Conductor)
- `--plan-phase N` (SI3)

## Esempi

### Esempio 1 — content-forge Phase 9→v1.2

Phase 9 (v1.1) ha fixato i 3 bug "noti" che avevo scoperto. Ma è stato pensato sapendo già che ne emergeranno altri.

v1.2 ha aggiunto Stage 10 SI agents per:
- Catturare automaticamente i nuovi bug
- Senza richiedere all'utente azione
- Accumulare in background fino a soglia
- Generare Phase 10 plan automaticamente

L'utente continua a usare la skill normalmente. Tra qualche settimana avrà dati reali su cui basare Phase 10.

### Esempio 2 — Errore che P10 risolve

Senza P10: l'utente nota problema mentre usa la skill → "ci penso dopo" → dimentica → bug resta.
3 mesi dopo: l'utente non ricorda i bug, ma ricorda di essere stato frustrato 5 volte → impressione vaga "questa skill non è perfetta", senza dati specifici per migliorarla.

Con P10: bug viene loggato automaticamente al primo segnale → triagato → accumulato. Quando l'utente vorrà migliorare, ha 10 FM concreti e specifici.

### Esempio 3 — ➕ Analogo in altri sistemi

**Sentry** (error tracking): cattura errori in produzione automaticamente, aggrega per pattern, alert su nuovi. Stessa filosofia: user pull > system push.

**Site Reliability Engineering** (Google): postmortems come pratica formalizzata di P10 a livello team. Ogni incident → doc strutturato → trend analysis → SLO refinement.

**Kaizen** (Toyota Production System): continuous improvement embedded nel workflow, non come progetto separato. Lean manufacturing.

## Anti-pattern correlato

**AP03 — User-Driven Overhead**: chiedere all'utente di scrivere bug reports, eseguire log script, fare triage manuale. **Esattamente il bug della mia v1.1**. Soluzione: agenti che fanno tutto loro.

**Anti-pattern duale**: **Notification spam** — agenti SI che notificano l'utente "ho trovato FM!" ogni volta. Distrugge il principio di silenzio operativo. **Fix**: hard rule "Conductor NEVER mentions Stage 10 unless user asks".

## Decision tree: "il mio sistema beneficia di P10?"

```
Il sistema verrà usato regolarmente (≥1 run/settimana)?
├─ NO → P10 overkill, basta logging tradizionale
└─ SÌ → continua
   ├─ I bug emergono prevedibilmente in unit test?
   │  ├─ SÌ → P10 forse non urgente
   │  └─ NO (emergono in uso reale) → P10 utile
   ├─ Hai meccanismo per fixarli (phase planning o sprint)?
   │  ├─ NO → P10 prematuro, prima costruisci il fix-side
   │  └─ SÌ → continua
   │
   └─ Implementa P10:
      1. Agente che logga (SI1 equivalent)
      2. Agente che categorizza (SI2 equivalent)
      3. Agente che pianifica (SI3 equivalent)
      4. Tool JSON per parlare tra di loro
      5. Conductor che spawna condizionalmente
```

## Quando NON applicare

- **One-shot tools**: si usano una volta, no improvement loop.
- **Sistemi senza piano di iterazione**: se non c'è next phase, perché loggare FM?
- **Sistemi LLM-free**: P10 è ottimizzato per agenti LLM (cattura giudizio semantico). Per pure software, basta error tracking tradizionale.

## Riferimenti esterni

- **Toyota Production System / Kaizen** — Continuous improvement embedded.
- **Google SRE Book** — Postmortem culture.
- **Sentry/Rollbar/Datadog** — Error tracking automatico in produzione.
- **The Lean Startup** (Eric Ries) — Build-Measure-Learn loop, analogo concettuale.

## Connessioni con altri principi

- Estende: P09 (Failure Modes First-Class) — P09 documenta i failure prevedibili, P10 cattura quelli che emergono in uso reale
- Si oppone a: AP03 (User-Driven Overhead) — P10 nasce per rimediare a AP03
- Combina con: P01 (Iterative Planning) — i PHASE-N-CANDIDATES generati da P10 alimentano PLAN-vN+1
- Implementato via: Stage 10 + agenti SI1/SI2/SI3 + scripts/log_failure.py
