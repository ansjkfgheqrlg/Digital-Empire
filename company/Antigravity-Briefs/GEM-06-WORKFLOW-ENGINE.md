---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md + ADR-006
Esecutore: GEMINI (Antigravity) · Priorità: P1 · Created: 2026-07-22
Dipendenze: GEM-01 + GEM-02 chiusi · Consuma GEM-04 · Alimenta GEM-03/GEM-05
---

# GEM-06 — WORKFLOW ENGINE
## Far girare i workflow, invece di descriverli

> **LEGGI PRIMA:** `GEM-00`, consegne `GEM-01`/`GEM-02`. Questo è l'ultimo pacchetto: chiude il
> cerchio (definire → eseguire → misurare → migliorare).

---

## 1. IL PROBLEMA MISURATO

`WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/` contiene 9 file: `WF-MASTER.md`, `WF-S1..S6`,
`WF-PERF-LOOP.md`, **`workflows.yaml`**. Il `.yaml` è già una descrizione macchina dei flussi.
`WF-MASTER.md` definisce un loop giornaliero preciso (09:00 dashboard → 09:30 due corsie
Max/Gael → 19:00 EOD), 6 gate con deadline, regole di precedenza revenue-first, una coda swarm
(max 1 pesante), un DAG di dipendenze, e un enforcement delle decisioni con finestra di veto.

**È un buon design di orchestrazione. Nessuna riga di codice lo esegue.**
Il "loop giornaliero" oggi significa: Max o Claude leggono il file e provano a ricordarsene.

Prove concrete che l'esecuzione a memoria non regge, già nel repo:
- gate con deadline al 21/07 20:00 e 22/07 20:00 (oggi è il 22/07): **nessun file ne registra
  l'esito**;
- `ADR-006` impone un ciclo di fase a 9 passi (RECALL → SPEC → PRE-MORTEM → BUILD → GATE →
  REVIEW → TEST → COMMIT → RETRO): non esiste un modo per verificare che un passo sia stato fatto;
- CP-20260721-003 documenta un commit etichettato "Fase 1 completata" il cui **diff conteneva
  solo log**: nessun gate lo ha intercettato.

**GEM-06 costruisce il motore che esegue `workflows.yaml`, applica i gate, e non lascia
avanzare un flusso che non ha superato il passo precedente.**

---

## 2. SKILL DA USARE (verifica prima — GEM-00 §2)

| Skill | Path | Uso | Fallback |
|---|---|---|---|
| `swarm-orchestration` | `.claude/skills/swarm-orchestration/` | pattern di fan-out/merge, quando parallelizzare | esecuzione sequenziale |
| `swarm-advanced` | `.claude/skills/swarm-advanced/` | swarm con dipendenze e coda | come sopra |
| `sparc-methodology` | `.claude/skills/sparc-methodology/` | i 9 passi di ADR-006 sono una variante di SPARC: **mappali esplicitamente** | mapping in SPEC |
| `workflow-automation` | `~/.claude/skills/workflow-automation/` | pattern di automazione dei flussi | §4 |
| `verification-quality` | `.claude/skills/verification-quality/` | i gate verificano **comportamento**, non presenza di file | §4.3 |
| `hooks-automation` | `.claude/skills/hooks-automation/` | trigger dei workflow | `.bat` documentato |
| `agent-planner` | `~/.claude/skills/agent-planner/` | decomposizione con dipendenze esplicite | DAG in yaml |
| `content-forge2.0` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/` | i suoi template `workflow/` (`flow`, `state`, `triggers`, `runbook`, `observability`, `error_handling`) sono **lo schema di riferimento**: leggili prima di inventare il tuo | — |

**Da leggere prima:** `workflows.yaml` integrale, `WF-MASTER.md`, tutti i `WF-S1..S6`,
`ADR-006`, `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`,
`DIGITAL-EMPIRE/03-WORKFLOWS/` e `DIGITAL-EMPIRE/01-PLANNING/PLANNING-P7-MASTER-PLAN.md`.

---

## 3. PRINCIPIO NON NEGOZIABILE — l'engine non fa il lavoro, lo governa

Questo motore **non** esegue le attività (non scrive copy, non chiama i concessionari, non
genera video). Fa quattro cose:

1. **Tiene lo stato** di ogni workflow: dove siamo, cosa è chiuso, cosa è in attesa, cosa è in ritardo.
2. **Applica i gate**: senza gate verde, il flusso non avanza. Mai.
3. **Assegna**: dice a chi tocca (Max / Gael / Claude / Gemini / agente X) e con che priorità.
4. **Registra**: ogni transizione è un atomo di memoria (GEM-02) e una riga di telemetria (GEM-03).

I passi con `executor: human` si chiudono con conferma esplicita. **L'engine non finge mai che
un passo umano sia stato fatto.** Un passo non confermato resta aperto e va in ritardo — è
esattamente il segnale che oggi manca.

---

## 4. ARCHITETTURA RICHIESTA

```
empire/flow/
├── __init__.py
├── SPEC.md
├── spec.py         # §4.1 parser + validatore di workflows.yaml
├── dag.py          # §4.2 dipendenze, ordine topologico, rilevamento cicli
├── gate.py         # §4.3 valutazione dei gate
├── state.py        # §4.4 stato persistente per run
├── queue.py        # §4.5 coda risorse: max 1 swarm pesante, revenue-first
├── runner.py       # §4.6 esecuzione passo-passo
├── report.py       # §4.7 stato leggibile + slittamenti
├── cli.py
└── tests/
```

### 4.1 `spec.py`
Leggi **prima** `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/workflows.yaml` e adatta lo schema a quello
che c'è già (ADR-003: wrap). Estendi solo dove manca. Schema minimo per passo:

```yaml
id: WF-S1
owner: Max
priority: 1                    # revenue-first: eur_ora stimato
steps:
  - id: S1.3
    title: "Chiamare i 7 concessionari"
    executor: human            # human | script | agent | swarm
    depends_on: [S1.2]
    skill: cro-copy-architect  # opzionale, deve esistere (verificato via empire skills)
    command: null              # per executor: script
    gate:
      id: CONTATTI
      deadline: "2026-07-23T12:00:00+02:00"
      green_if: "contattati >= 7"
      on_red: "follow-up delegato + push S2 compensa"
    dod:
      - "7 su 7 contattati con esito registrato"
```

Validazione obbligatoria a load-time, con errore chiaro (file:riga):
- ogni `depends_on` punta a un `id` esistente;
- nessun ciclo nel DAG;
- ogni `skill` citata **esiste su disco** (via `empire skills`) — altrimenti `block`;
- ogni `command` referenzia un file esistente (via `empire.paths`) — altrimenti `block`;
- ogni gate ha `deadline` assoluta ISO-8601 con timezone. **Mai date relative.**

### 4.2 `dag.py`
Ordine topologico, cammino critico, e — data una data — **cosa è sbloccato adesso** e
**cosa blocca cosa**. `WF-MASTER.md` dichiara già il DAG in prosa:
`DEC-001→(landing, email) · audit→(bio S3, config S4) · DEC-002→kit S6 · case-study→outreach S6
· Fliki-test→WF-S5 · DEC-004→WF-S5`. Trasferiscilo in `workflows.yaml` **verificandolo**, non
copiandolo alla cieca.

### 4.3 `gate.py` — il cuore
Tipi di gate da supportare:
| Tipo | Verifica | Esempio reale |
|---|---|---|
| `metric` | espressione su una metrica di memoria/telemetria | `anticipi_chiusi >= 1` (gate REV) |
| `file` | esiste + non vuoto + opzionale pattern dentro | landing pubblicata |
| `command` | comando esce 0 | `python -m empire doctor` |
| `human` | conferma esplicita con nota | "7/7 contattati" |
| `conform` | `empire conform` non ha `block` | Art.8 |

Regole:
- **`green_if` è un'espressione valutata su fatti**, non un'opinione. Niente `eval()` su input
  arbitrario: implementa un mini-valutatore che accetta solo `<nome> <op> <numero>` e `and`/`or`.
- Al superamento della `deadline` senza verde → il gate diventa **🔴 automaticamente**, si applica
  `on_red`, si scrive un atomo `error` + una escalation.
- **Nessun gate "quasi verde"** (regola letterale di `WF-MASTER.md` §3). Due stati: 🟢 o 🔴.
- **Default-decision enforcement** (regola §4 di WF-MASTER): una decisione con finestra di veto
  scaduta passa ad `ATTIVA` da sola, l'engine lo registra e procede. Precedente reale: DEC-EST-001
  (prezzo Manuale €67) è ATTIVA per default scaduto.

### 4.4 `state.py`
`empire/.data/flow/<WF-id>/state.json` — append-only delle transizioni + stato corrente derivato.
Ogni transizione: `ts`, `step`, `from`, `to`, `actor`, `evidence` (path o comando+output), `note`.
Ricostruibile per intero dal log. **Idempotente**: rieseguire un passo già chiuso non lo duplica,
segnala "già chiuso il <data>".

### 4.5 `queue.py`
Regole prese letteralmente da `WF-MASTER.md`:
- **max 1 swarm pesante (Opus) alla volta**; ordine di precedenza `S1 > S2 > S6 > S5`; il resto
  degrada a esecuzione singola;
- **revenue-first**: a parità di dipendenze soddisfatte, vince il task con €/h più alto;
- **budget-guard (CLAUDE.md)**: sotto il 20% di risorse di sessione → si chiude con COMMIT, non
  si aprono build nuovi. L'engine deve poter ricevere un segnale di budget e rifiutare nuovi
  avvii pesanti.

### 4.6 `runner.py`
```
python -m empire flow status [--wf WF-S1]
python -m empire flow next                  # cosa è sbloccato ADESSO, per chi, con che priorità
python -m empire flow start --step S1.3
python -m empire flow done --step S1.3 --evidence "7/7 contattati, 2 richiami lun" --actor Max
python -m empire flow gate CONTATTI          # valuta e marca 🟢/🔴
python -m empire flow gates                  # tutti i 6 gate della settimana
python -m empire flow today                  # il loop giornaliero di WF-MASTER, eseguibile
python -m empire flow late                   # cosa è in ritardo e da quanto
python -m empire flow validate               # solo validazione dello yaml, exit 1 se rotto
```

`flow today` è il comando che sostituisce "ricordarsi del WF-MASTER": stampa il brief del
giorno — gate in scadenza oggi, passi sbloccati per corsia (Max / Gael), slittamenti, e alle
19:00 richiede il checkpoint EOD.

### 4.7 `report.py`
Stato leggibile in `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/STATO-FLUSSI.md`, consumato da GEM-05.

---

## 5. SEQUENZA

**TASK 1 — Ricognizione.** Verifica skill. Leggi `workflows.yaml`, i 9 file di
`01-FLUSSI-E-PIANI/`, ADR-006, il metodo a 9 passi, i template `workflow/` di content-forge2.0.
Output `empire/flow/SPEC.md` con: schema yaml finale, **mappatura esplicita dei 9 passi di
ADR-006 sui tipi di gate**, e l'elenco dei 6 gate estate già formalizzati.
**Gate 1**: la SPEC contiene i 6 gate con `green_if` espressi come espressioni valutabili, non
come frasi.

**TASK 2 — `spec.py` + `dag.py`.** **Gate 2**: `flow validate` sul `workflows.yaml` **reale**.
Se il file esistente è incompleto rispetto a `WF-MASTER.md`, **completalo** (è dato di
configurazione, non prosa: modificarlo è autorizzato) e mostra il diff. Il DAG deve rilevare un
ciclo se ne introduci uno di prova. Incolla entrambi gli output.

**TASK 3 — `gate.py`.** **Gate 3**: valuta i 6 gate estate sui dati **reali** di oggi
(2026-07-22). Alcuni saranno 🔴 — **va bene, è la verità**. Un gate scaduto senza esito
registrato deve risultare 🔴 con `on_red` applicato. Incolla la tabella dei 6 esiti.

**TASK 4 — `state.py` + `runner.py`.** **Gate 4**: simula un flusso completo di 5 passi con
dipendenze, di cui 2 `human`. Dimostra che: un passo con dipendenza aperta **non parte**; un
passo `human` non confermato **non si chiude da solo**; `done` due volte **non duplica**.
Incolla la traccia.

**TASK 5 — `queue.py`.** **Gate 5**: 3 richieste di swarm pesante contemporanee → 1 parte,
2 in coda nell'ordine `S1 > S2 > S6 > S5`. Incolla la traccia.

**TASK 6 — Integrazione.** Ogni transizione scrive un atomo GEM-02 + un record perf GEM-03.
**Gate 6**: chiudi un passo → verifica che compaiano **sia** l'atomo in memoria **sia** il file
in `Ispettorato/telemetry/runs/`. Incolla entrambi.

**TASK 7 — `flow today`.** **Gate 7**: esegui `flow today` il 2026-07-22 e confronta il suo
output con quanto `WF-MASTER.md` prescriverebbe a mano per oggi. Devono coincidere. Se non
coincidono, spiega quale dei due è sbagliato — **è possibile che sia il .md**, e in quel caso
è un finding da passare a Max.

**TASK 8 — Chiusura.** README, `STATO-FLUSSI.md`, checkpoint via GEM-02, consegna GEM-00 §4.

---

## 6. DEFINITION OF DONE

- [ ] DoD-1 — `flow validate` passa su `workflows.yaml` reale, o spiega esattamente cosa manca
- [ ] DoD-2 — ogni `skill` e ogni `command` citati nello yaml sono verificati esistenti
- [ ] DoD-3 — i 6 gate estate valutati sui dati reali, con esiti veri (anche 🔴)
- [ ] DoD-4 — un passo con dipendenza aperta **non può** partire (dimostrato)
- [ ] DoD-5 — un passo `human` non si auto-chiude mai (dimostrato)
- [ ] DoD-6 — gate scaduto → 🔴 automatico + `on_red` applicato + atomo `error` scritto
- [ ] DoD-7 — coda: max 1 swarm pesante, ordine di precedenza rispettato
- [ ] DoD-8 — ogni transizione produce atomo memoria + record telemetria
- [ ] DoD-9 — `flow done` idempotente: secondo run segnala "già chiuso", non duplica
- [ ] DoD-10 — `flow today` coincide con quanto prescrive `WF-MASTER.md` per la data odierna
- [ ] DoD-11 — stato interamente ricostruibile dal log delle transizioni (dimostrato cancellando lo stato derivato e rigenerandolo)
- [ ] DoD-12 — nessun `eval()` su input non fidato; pytest ≥ 25 test verdi

---

## 7. ANTI-PATTERN

| Anti-pattern | Perché rifiutato |
|---|---|
| L'engine "esegue" un passo umano marcandolo fatto | Distrugge l'unico segnale utile: il ritardo reale. |
| Gate "quasi verde" / percentuali di completamento del gate | Regola letterale di WF-MASTER: 🟢 o 🔴. |
| `eval()` sull'espressione `green_if` | Esecuzione di codice arbitrario da un file di config. Mini-valutatore. |
| Deadline relative ("entro domani") | Vietato ovunque nel monorepo. ISO-8601 con timezone. |
| Riscrivere i `WF-S1..S6` in un formato nuovo | ADR-003. Sono prosa operativa per esseri umani. Lo yaml è la parte macchina. |
| Un engine che lancia agenti LLM da solo, senza budget-guard | Brucia risorse. La coda e il budget-guard sono obbligatori. |
| Stato in memoria non persistito | Un riavvio perde la settimana. Append-only su file. |

---

## 8. HANDOFF — chiusura del cerchio

Con GEM-06 chiuso, il ciclo è completo e verificabile:

```
GEM-06 definisce ed esegue  →  GEM-02 ricorda  →  GEM-03 misura e critica
      ▲                                                      │
      └──────────  GEM-05 mostra  ←  GEM-04 censisce  ◄──────┘
                        (tutto sopra GEM-01)
```

A Max, decisione finale da prendere dopo GEM-06:
> l'engine renderà visibile **quanti passi dei workflow sono `executor: human` su Max**.
> Se il numero è alto, il collo di bottiglia dell'azienda non è la tecnologia: sei tu.
> Quella è una decisione di delega, non di codice.
</content>
