---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md + dossier 15
Esecutore: GEMINI (Antigravity) · Priorità: P0 · Created: 2026-07-22
Dipendenze: GEM-01 + GEM-02 chiusi · Blocca: GEM-05
---

# GEM-03 — ISPETTORATO GENERALE: TELEMETRIA E LOOP DI PERFORMANCE
## L'organo che deve sorvegliare l'azienda e non ha mai girato

> **LEGGI PRIMA:** `GEM-00`, `GEM-01`, `GEM-02`. Questo brief usa `empire.paths` e `empire.memory`.

---

## 1. IL PROBLEMA MISURATO — questa è la risposta alla domanda di Max

Max ha chiesto: *"L'azienda stabilisce, misura, analizza le performance di questo workflow.
Ci sono agenti che lo sorvegliano, lo analizzano e lo migliorano — questo avviene o ancora no?"*

**Risposta misurata sul disco, 2026-07-22: NO. Non avviene. Zero volte.**

| Cosa dovrebbe esserci | Path | Contenuto reale |
|---|---|---|
| Report di ogni run | `company/Ispettorato/report/run/` | **VUOTA** |
| Report giornalieri | `company/Ispettorato/report/daily/` | **VUOTA** |
| Escalation | `company/Ispettorato/report/escalation/` | **VUOTA** |
| Telemetria per run | `company/Ispettorato/telemetry/runs/` | **VUOTA** |
| Telemetria giornaliera | `company/Ispettorato/telemetry/daily/` | **VUOTA** |
| Stato dell'organo | `company/Ispettorato/state/` | **VUOTA** |
| Audit di memoria | `company/Memory/audit/` | **VUOTA** |
| Script dell'Ispettorato | `company/Ispettorato/scripts/` | **1 file, nessun `.py`** |

L'Ispettorato **esiste**: 11 agenti progettati (`isp-conductor` … `isp-revision-analyst`),
5 workflow CF-grade, KPI, principi, regole, `REGISTRO-ERRORI`. È stato costruito il 2026-07-20
(CP-20260720-005). **È un organo perfettamente descritto che non ha mai emesso un solo report.**

Stessa cosa per il workflow estate: `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md` descrive
un ciclo T0→T5 preciso e sensato (capture → analyze → synthesize → dispatch → **confirm**), con
scorecard 5D e regola anti-nagging. È un buon design. **Non esiste una riga di codice che lo esegua**,
e i path che cita (`00-MEMORY/performances/`, `04-AGENTS/PERFORMANCE-CELL.md`) non esistono
nemmeno nella cartella dove il file si trova.

**GEM-03 rende eseguibile WF-PERF-LOOP e accende l'Ispettorato.**

---

## 2. SKILL DA USARE (verifica prima — GEM-00 §2)

| Skill | Path | Uso | Fallback |
|---|---|---|---|
| `verification-quality` | `.claude/skills/verification-quality/` | **la scorecard 5D deve essere comportamentale**, non estetica: misura cosa il lavoro FA, non come è scritto | criteri §4 |
| `agent-reviewer` | `~/.claude/skills/agent-reviewer/` | modello di review sistematica → base dell'analyst | §4.2 |
| `agent-tester` | `~/.claude/skills/agent-tester/` | test dei calcoli di scoring | unittest |
| `hooks-automation` | `.claude/skills/hooks-automation/` | il capture T1 è un **hook post-task**, non una chiamata volontaria | documenta il wiring |
| `content-forge2.0` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/` | i suoi agenti `self-improvement/` (`failure-detector`, `triage`, `phase-planner`) sono il modello di riferimento — **leggili** | — |
| `swarm-orchestration` | `.claude/skills/swarm-orchestration/` | collector/analyst/dispatcher sono disgiunti | sequenziale |
| `memory-empire` | `~/.claude/skills/memory-empire/` | i record perf/feedback sono atomi di memoria (GEM-02) | — |

**Documenti da leggere prima di scrivere codice (obbligatorio):**
- `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md` — **è la specifica funzionale di questo brief**
- `company/Ispettorato/` — tutti i 27 file, in particolare `agenti/`, `kpi/`, `regole/`, `principi/`
- `PIANO-MAESTRO/15-*` (dossier Ispettorato) se presente
- `company/Ispettorato/registro/` — il REGISTRO-ERRORI e il gate anti-recidiva

---

## 3. IL CICLO DA IMPLEMENTARE (da WF-PERF-LOOP, T0→T5)

```
T0  AZIONE CHIUSA
      │  (hook post-task — automatico, non volontario)
      ▼
T1  CAPTURE      perf-collector → atomo kind="perf"
      │          scrittura diretta su file, zero costo LLM
      ▼
T2  ANALYZE      perf-analyst → scorecard 5D + gate traceability
      │          ① correctness/debug  ② qualità soluzione  ③ struttura output
      │          ④ scope-fit (DoD rispettata?)  ⑤ efficiency (TTD vs benchmark ruolo)
      ▼
T3  SYNTHESIZE   segnale nuovo → pattern DRAFT in ReasoningBank
      │          segnale già visto → +1 ricorrenza
      ▼
T4  DISPATCH     TIP → all'agente · RULE-NOTE → al regolatore · MUTATION-PROP → al comandante (≥3 ricorrenze)
      │          anti-nagging: stesso TIP allo stesso agente → non ripetere entro 3 task
      ▼
T5  CONFIRM      alla PROSSIMA performance della stessa famiglia-task:
                 ✅ non ricorre → status "confirmed" → pattern UFFICIALE
                 ❌ ricorre     → status "recurred"  → escalation obbligatoria
```

**Il punto non negoziabile (parole di Max nel WF): un miglioramento ESISTE solo quando T5 lo
conferma.** Un TIP non confermato è un suggerimento, non un miglioramento. Il codice deve tenere
i conti — è tutto il senso di questo pacchetto.

---

## 4. ARCHITETTURA RICHIESTA

```
empire/inspect/
├── __init__.py
├── SPEC.md
├── record.py       # PerfRecord + FeedbackRecord → atomi kind perf/feedback (GEM-02)
├── collector.py    # T1 — capture, zero-LLM, idempotente
├── analyst.py      # T2 — scorecard 5D deterministica
├── synth.py        # T3 — pattern detection + contatore ricorrenze
├── dispatch.py     # T4 — TIP/RULE-NOTE/MUTATION-PROP + anti-nagging
├── confirm.py      # T5 — chiusura del loop, confirmed|recurred, escalation
├── benchmarks.py   # TTD attesi per famiglia-task/ruolo (tabella, tarabile)
├── report.py       # scrive company/Ispettorato/report/{run,daily,escalation}/
├── cli.py          # python -m empire inspect ...
└── tests/
```

### 4.1 `record.py`
```python
@dataclass(slots=True)
class PerfRecord:
    id: str                    # PERF-YYYYMMDD-NNN (lock ID di GEM-02)
    agent: str                 # id agente da empire.index (DEVE esistere, altrimenti warn)
    task: str
    workflow: str              # WF-S1 | WF-MASTER | GEM-03 | ...
    family: str                # famiglia-task, serve a T5: es. "build-python", "copy-landing"
    result: str                # success | partial | failed
    started: datetime; ended: datetime
    ttd_h: float               # calcolato, non dichiarato
    debug: dict                # {errori:int, retry:int, escalation:int, fix_applicati:[str]}
    output_ref: list[Path]
    verification: dict         # {verificatore, first_pass: bool, note}
    scorecard: dict            # 5 assi 1-5 + gate traceability bool
    feedback_ids: list[str]

@dataclass(slots=True)
class FeedbackRecord:
    id: str                    # FB-YYYYMMDD-NNN
    ftype: str                 # TIP | RULE-NOTE | MUTATION-PROP
    to: str                    # agente | regolatore | comandante-di-casta
    micro_input: str           # piccolo, azionabile — max 200 caratteri, enforced
    on_perf: str               # PERF-id
    status: str                # open → acked → confirmed | recurred
    opened: datetime; closed: datetime | None
```

### 4.2 `analyst.py` — la scorecard 5D **deterministica**
Non chiedere a un LLM di dare un voto. Calcolalo da fatti osservabili, così è riproducibile
e verificabile. Proposta di partenza (documenta ogni formula in `SPEC.md`, sono tarabili):

| Asse | 1-5 calcolato da |
|---|---|
| ① correctness/debug | `5 - min(4, errori + retry*0.5 + escalation*2)` |
| ② qualità soluzione | `first_pass=True` → 5; una revisione → 4; ≥2 → 3; fix post-consegna → 2; regressione → 1 |
| ③ struttura output | artefatti prodotti hanno intestazione ADR-008 + sono nei path attesi + non orfani (usa `empire.conform`) |
| ④ scope-fit | % di DoD spuntate **e verificate con comando** / DoD totali del brief |
| ⑤ efficiency | `ttd_h` vs benchmark di `benchmarks.py` per quella famiglia: ≤0.8× → 5, ≤1.2× → 4, ≤2× → 3, ≤3× → 2, oltre → 1 |
| gate traceability | esiste un atomo `checkpoint` che referenzia questo task? bool |

**Gate traceability = False è bloccante**: un lavoro senza checkpoint non è valutabile e va
segnalato come violazione ADR-002, non come voto basso.

### 4.3 `dispatch.py` — anti-nagging (regola dal WF)
Stesso `ftype` + stesso `to` + stesso tema → **non riemettere entro 3 task** dello stesso agente.
Implementa con una finestra scorrevole sugli ultimi N atomi `feedback`. Test esplicito richiesto.

### 4.4 `report.py` — riempire le cartelle vuote
- `company/Ispettorato/telemetry/runs/RUN-<id>.json` — dati grezzi, un file per run
- `company/Ispettorato/telemetry/daily/<YYYY-MM-DD>.json` — aggregato del giorno
- `company/Ispettorato/report/run/RPT-RUN-<id>.md` — leggibile: cosa è successo, voti, TIP emessi
- `company/Ispettorato/report/daily/RPT-<YYYY-MM-DD>.md` — **la daily autocritica**: cosa è
  andato male oggi, cosa ricorre, cosa è stato confermato migliorato
- `company/Ispettorato/report/escalation/ESC-<id>.md` — solo quando `recurred` ≥ 3

**Ogni report cita path:riga reali.** Un report senza riferimenti verificabili è un tema, non
un'ispezione.

### 4.5 `cli.py`
```
python -m empire inspect capture --agent <id> --task <id> --wf <WF> --family <f> --result success --started ... --ended ...
python -m empire inspect analyze [--perf PERF-...] [--all-pending]
python -m empire inspect dispatch [--dry-run]
python -m empire inspect confirm --family <f> --agent <id>
python -m empire inspect report --daily [--date 2026-07-22]
python -m empire inspect status              # loop aperti, TIP non acked, pattern in DRAFT
python -m empire inspect backfill            # §5 TASK 5 — vedi sotto
```

---

## 5. SEQUENZA — task dopo task

**TASK 1 — Ricognizione.** Verifica skill. Leggi WF-PERF-LOOP integrale, tutti i 27 file
dell'Ispettorato, gli agenti `self-improvement/` di content-forge2.0.
Output: `empire/inspect/SPEC.md` con **le 5 formule esplicite** e le loro assunzioni.
**Gate 1**: ogni formula ha un esempio numerico svolto a mano.

**TASK 2 — `record.py` + `collector.py`.** T1 funzionante, atomi scritti via GEM-02.
**Gate 2**: capture di 3 run finti → 3 atomi `perf` + 3 file in `telemetry/runs/`. Cartella
non più vuota. Incolla `ls`.

**TASK 3 — `analyst.py` + `benchmarks.py`.** T2.
**Gate 3**: stesso input → stesso punteggio, 10 esecuzioni. Determinismo dimostrato.

**TASK 4 — `synth.py` + `dispatch.py` + `confirm.py`.** T3-T4-T5, con anti-nagging.
**Gate 4**: scenario simulato — stesso problema 3 volte di fila sullo stesso agente → deve
emettere 1 TIP, poi silenzio per 3 task, poi al ricorrere una `MUTATION-PROP` + escalation.
Incolla la traccia completa dello scenario.

**TASK 5 — `backfill`: la prima ispezione VERA (il momento di verità).**
Non simulare. Usa i dati storici che il repo ha già: **~30 checkpoint reali** in
`company/Memory/checkpoints/` descrivono lavori chiusi da Max, Gael e Claude, con esiti, bug
trovati, fix. Trasformali in `PerfRecord` retroattivi (`--backfill`, marcati `estimated: true`
perché i timestamp sono parziali) e fai girare T2-T3 su di essi.

Da questo devono emergere **pattern reali**, non inventati. Esempi che il corpus contiene già:
- CP-20260719-004 e CP-20260719-007: *"NON eseguito: ambiente sessione senza Python/Node"* →
  pattern ricorrente **"build dichiarato senza runtime disponibile"**
- CP-20260720-006: bug PyInstaller `_MEIPASS` invisibile in dev → pattern **"verificato in dev,
  rotto nel frozen"**
- CP-20260719-008: collisione Max/Gael su `ui/index.html` → pattern **"due owner sullo stesso file"**
- CP-20260721-003: commit mal-etichettato, diff = solo log → pattern **"dichiarato fatto, diff vuoto"**

**Gate 5 — il gate che conta**: `report --daily` produce un report che identifica **almeno 3
pattern ricorrenti reali** con i CP-id a supporto. Se il report è generico, il synth è debole:
rifallo. Questo report è il primo output storico dell'Ispettorato — **va scritto bene.**

**TASK 6 — Automazione.** `hooks-automation`: il capture T1 deve scattare da hook post-task,
non a mano. Documenta il wiring in `consegne/GEM-03-HOOK-SETUP.md`. **Non modificare
`.claude/settings.json`** — lo approva Max.
**Gate 6**: hook eseguito a mano → atomo creato senza intervento.

**TASK 7 — Chiusura.** README, registrazione ADR-008, checkpoint via GEM-02, consegna GEM-00 §4.
**+ Riparazione**: aggiorna `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md` sostituendo i
path rotti (`00-MEMORY/performances/`, `04-AGENTS/PERFORMANCE-CELL.md`) con i comandi reali
`python -m empire inspect ...`. **Questa è l'unica modifica a un .md esistente autorizzata da
questo brief**, ed è autorizzata perché quei path non esistono: si sta correggendo un errore,
non riscrivendo un contenuto.

---

## 6. DEFINITION OF DONE

- [ ] DoD-1 — `company/Ispettorato/telemetry/runs/` **non è più vuota** (`ls` incollato)
- [ ] DoD-2 — `company/Ispettorato/telemetry/daily/` non è più vuota
- [ ] DoD-3 — `company/Ispettorato/report/daily/` contiene almeno 1 report reale, scritto dai dati
- [ ] DoD-4 — scorecard 5D deterministica: 10 run stesso input → stesso output
- [ ] DoD-5 — anti-nagging dimostrato con lo scenario del Gate 4
- [ ] DoD-6 — T5 chiude davvero il loop: `confirmed` e `recurred` entrambi raggiunti in test
- [ ] DoD-7 — escalation automatica a ≥3 ricorrenze, con file in `report/escalation/`
- [ ] DoD-8 — backfill sui ~30 checkpoint reali eseguito, ≥3 pattern reali identificati con CP-id
- [ ] DoD-9 — ogni PerfRecord è un atomo di memoria GEM-02 (nessun formato parallelo)
- [ ] DoD-10 — gate traceability marca correttamente i task senza checkpoint
- [ ] DoD-11 — `WF-PERF-LOOP.md` non contiene più path inesistenti
- [ ] DoD-12 — pytest ≥ 25 test verdi, zero crash Unicode

---

## 7. ANTI-PATTERN

| Anti-pattern | Perché rifiutato |
|---|---|
| Chiedere a un LLM di dare i voti della scorecard | Non riproducibile, non verificabile, non tarabile. La 5D è **calcolata**. |
| Emettere TIP generici ("migliora la qualità") | Il WF chiede **micro-input azionabili**. Max 200 caratteri, imperativi, specifici. |
| Loop senza T5 | Un miglioramento non confermato non esiste. È la regola centrale del WF. |
| Popolare le cartelle con dati finti per "dimostrare" | Falsifica la telemetria alla nascita. Il backfill usa **checkpoint reali**. |
| Report che non cita `path:riga` o `CP-id` | Non è un'ispezione, è un'opinione. |
| Un formato di record parallelo agli atomi GEM-02 | Ricrea la frammentazione che GEM-02 ha appena chiuso. |
| Modificare le schede dei 11 agenti dell'Ispettorato | Sono specifica. Il codice le **implementa**, non le riscrive. |

---

## 8. HANDOFF

Sblocca **GEM-05** (Dashboard): consuma `telemetry/daily/*.json`.

A Claude e Max: il primo report daily del backfill è **materiale decisionale**. Se emerge che un
pattern ricorre da settimane (es. "build dichiarato senza runtime"), quello non è un bug da
correggere: è una **regola aziendale mancante** → serve un ADR. Il brief si ferma qui e lo passa
a Max: Gemini identifica il pattern, non decide la regola.
</content>
