# CENSIMENTO 02 — I COLLEGAMENTI

> **Chi parla con chi oggi, e chi dovrebbe parlare con chi.**
> Rilevazione: 2026-09-06 · Autore: DOOM BOT (censimento collegamenti) · Committente: EMPERATOR
> Metodo: ogni riga viene da un file aperto o da un comando lanciato. Percorsi sempre citati.
> Stato: SEZIONI 1-4 CHIUSE · 5-6 in corso

---

## 1. IL BUS E I CONTRATTI

### 1.1 Il Bus: cosa dice di essere, cosa e'

`company/Backbone/Bus/README.md` descrive un message bus a 2 livelli (INTRA + INTER),
append-only, con handoff contract obbligatorio, 3-tier routing per priorita' e 4 KPI.
Dichiara come motori `company/orchestrator/bus.sh` e `company/orchestrator/gbus.sh`.

Verifica su disco — **l'intero Bus e' 3 file**:

| File | Cosa e' |
|---|---|
| `company/Backbone/Bus/README.md` | la descrizione dell'architettura |
| `company/Backbone/Bus/contracts/HC-template.json` | schema `empire-handoff-contract-v1` |
| `company/Backbone/Bus/handoffs/.gitkeep` | 0 byte, cartella vuota, zero handoff in tutta la vita |

Comando: `find company/Backbone/Bus -type f` → 3 risultati, nessun altro.

**Non esistono** (cercati con `find . -name`):

- `company/orchestrator/bus.sh` — NON ESISTE (la cartella `company/orchestrator/` non esiste)
- `company/orchestrator/gbus.sh` — NON ESISTE
- `validate-handoff.sh` — NON ESISTE
- `company/Backbone/Bus/contracts/registry.yaml` — NON ESISTE
- `company/Backbone/Bus/fulfilled/` e `rejected/` — NON ESISTONO (il README le disegna)
- `company/runtime/bus/` e `company/runtime/group-bus/` — NON ESISTONO
- `company/Ecosistemi/<ECO>/handoffs/{inbox,outbox,archive}/` — NON ESISTONO per nessun ecosistema

Il README stesso lo ammette in fondo: *"Stato: DA COSTRUIRE (F2, task 2.3)"*. La F2 non e' mai arrivata.

### 1.2 I contratti esistenti — scheda per scheda

Cinque file totali nel repo con schema di handoff (`find company empire -iname "*handoff*" -o -iname "HC-*"`).

#### HC-template.json — `company/Backbone/Bus/contracts/HC-template.json`

- schema: `empire-handoff-contract-v1`
- da: `01-AGENCY / outreach-executor` → a: `04-MARKETING / copy-apsoc-writer`
- carico: `lead_qualificato` (nome_azienda, settore, pain_point_emerso, budget_stimato, urgenza)
- accettazione: 3 criteri (APSOC ≥ 80, personalizzazione sul pain point, CTA Calendly)
- **istanziato: MAI** — e' il modello, e la coda che indica (`company/Backbone/Bus/handoffs/`) e' vuota.
- **Incoerenza di schema:** questo template usa `empire-handoff-contract-v1`, i 4 contratti veri
  usano `HC-v1`, e il README del Bus ne mostra un TERZO (campi `id/ts/scope/from/to/priority/type/
  payload/acceptance_criteria/status`, con `from`/`to` come stringhe-percorso invece che oggetti).
  **Tre schemi diversi, nessun validatore.**

#### HC-A1-A2-leads — `company/01-agency/A1-RICERCA/handoffs/HC-A1-A2-leads.json`

- schema `HC-v1` · creato 2026-06-11 · `"status": "template"`
- da: 01-AGENCY/A1-RICERCA/AG-A1-COORD (task WF-LEAD-SOURCING) → a: 01-AGENCY/A2-ACQUISIZIONE/AG-A2-COORD, coda `leads_ready`
- carico: `lead_batch` — lead_id, azienda, contatto, email/linkedin/instagram, nicchia, score_icp, canali, note
- accettazione: 4 criteri (score ≥ soglia ICP, ≥1 canale valido, dedup vs leads.db, nicchia identificata)
- failure_handling: on_reject → torna in A1; on_timeout → alert AG-A2-COORD
- **percorso:** 1 volta, **in DRY-RUN** (vedi §1.3)

#### HC-A2-A3-call — `company/01-agency/A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json`

- schema `HC-v1` · creato 2026-06-11 · `"status": "template"`
- da: A2-ACQUISIZIONE/AG-A2-COORD (WF-REPLY-FOLLOWUP) → a: A3-PREVENTIVI/AG-A3-COORD, coda `call_booked`
- carico: `call_booking` — cycle_id, lead_id, azienda, nicchia, call_scheduled_at, canale, thread, triage_result
- accettazione: 4 criteri (triage = interessato, call nel futuro, lead in leads.db, dossier pre-call pronto)
- `pii: true` con nota `aidefence_has_pii` prima dello store
- **percorso:** 1 volta, in DRY-RUN

#### HC-A3-A4-contratto — `company/01-agency/A3-PREVENTIVI/handoffs/HC-A3-A4-contratto.json`

- schema `HC-v1` · creato 2026-06-11 · `"status": "template"` · priorita' `critical`
- da: A3-PREVENTIVI/AG-A3-COORD (WF-PREVENTIVO) → a: A4-DELIVERY/AG-A4-COORD, coda `delivery_queue`
- carico: `contratto_firmato` — cycle_id, client_id, prodotto (4 valori a catalogo), valore_eur,
  pagamento_confermato, brief_tecnico (6 campi), brand_kit (4 campi), icp_cliente (3 campi), 2 PDF
- accettazione: 5 criteri (gate preventivo passed, pagamento confermato, ambiente server compilato, brand kit, prodotto a catalogo)
- **percorso:** 1 volta, in DRY-RUN

#### HC-A4-A6-testimonianza — `company/01-agency/A4-DELIVERY/handoffs/HC-A4-A6-testimonianza.json`

- schema `HC-v1` · creato 2026-06-11 · `"status": "template"`
- da: A4-DELIVERY/AG-A4-COORD (WF-SUPPORTO-90GG) → a: A6-MARKETING-INTERNO/AG-A6-COORD, coda `testimonianza_queue`
- carico: `delivery_completata` — cycle_id, client_id, prodotto, date, gate_delivery_passed,
  metriche_reali, supporto_90gg_ends_at, segnale_positivo
- accettazione: 5 criteri, fra cui `segnale_positivo = true`, condizione per attivare `T-upsell-mapper`
- **percorso:** 1 volta, in DRY-RUN

### 1.3 Sono mai stati percorsi? — LA CORREZIONE

EMPERATOR aveva misurato "sono definizioni, mai istanze". **La misura va corretta di un caso.**

`company/Memory/state/agency/trace.jsonl` (22 righe) contiene un ciclo end-to-end completo,
`CY-20260611-001`, del **2026-06-11 fra le 18:13:12 e le 18:14:10** (58 secondi), in cui
**tutti e 4 gli HC sono stati attraversati**: 4 eventi `handoff_sent` + 4 `handoff_received`,
piu' 3 `gate_passed`.

E `company/Memory/state/agency/state.json` lo registra nero su bianco:

```json
"handoffs": [
  { "hc": "HC-A1-A2-leads",         "sent_at": "...18:13:12Z", "accepted_at": "...18:13:12Z" },
  { "hc": "HC-A2-A3-call",          "sent_at": "...18:13:31Z", "accepted_at": "...18:13:31Z" },
  { "hc": "HC-A3-A4-contratto",     "sent_at": "...18:13:53Z", "accepted_at": "...18:13:54Z" },
  { "hc": "HC-A4-A6-testimonianza", "sent_at": "...18:14:09Z", "accepted_at": "...18:14:10Z" }
]
```

**Ma:** `"dry_run": true`, `"lead_id": "DRYRUN-001"`, `"lead_nome_azienda": "DryRun-Client-01 (TEST - non reale)"`.
Il ciclo era una simulazione per far passare il Gate F4. Nessun invio reale, nessun euro,
nessun file di handoff prodotto: `company/Backbone/Bus/handoffs/` e' rimasta vuota anche quel giorno.
**La traccia c'e', il payload no.**

Dal 2026-06-11 a oggi (2026-09-06, **87 giorni**) nessun altro ciclo: `"active": []`, `"failed": []`,
`updated_at` fermo a `2026-06-11T18:14:10Z`.

**Verdetto:** 4 contratti su 5 sono stati percorsi **una volta sola, a vuoto, in un test**.
Il quinto (HC-template, l'unico INTER-ecosistema) non e' mai stato percorso nemmeno per finta.

### 1.4 Chi scrive nel trace del ciclo

`scripts/agency-trace.ps1` (52 righe) — logger append-only. Riceve
`-CycleId -Step -Event -From -To -Hc -Agent -Summary` e appende una riga JSON in
`company/Memory/state/agency/trace.jsonl`.
E' **l'unico pezzo di codice del repo che sappia scrivere la parola `HC-` in un file di stato**,
e va invocato **a mano, un evento per volta**. Nessuno script lo chiama:
`grep -rn "agency-trace"` sui .py/.ps1 → nessun chiamante.
Il commento in testa al file lo dice: *"NON modifica state.json (quello e' manuale/Claude)"*.

### 1.5 Lo schema HC-v1 basta per instradare? — NO

HC-v1 e' un buon **descrittore di consegna**. Non e' un **indirizzo**. Cosa manca perche' un
router possa prendere un HC e sapere dove metterlo:

| Campo mancante | Perche' serve | Oggi |
|---|---|---|
| `_id` **dell'istanza** (l'`_id` attuale e' l'id del contratto, non del messaggio) | due handoff dello stesso tipo si sovrascriverebbero | non si pone: zero istanze |
| `ts` / `created_at` reale | ordinare la coda, misurare l'eta' di un pending | `metadata` ha solo `priority` e `frequenza` |
| `status` mutabile (pending→accepted→done→rejected) | dire a che punto e' | costante `"template"` in tutti e 4 |
| `queue` come **percorso** e non come nome | `"queue": "leads_ready"` non e' una cartella esistente | il destinatario non ha una casella |
| `scope` (intra / inter) | il Bus e' a 2 livelli, HC-v1 non dice a quale appartiene | l'unico contratto inter e' scritto in un dialetto diverso |
| `brand_kit` / `icp` | il README del Bus li dichiara **obbligatori** nell'inter-ecosistema (Pattern #11) | HC-v1 non li ha: 4 su 4 sarebbero invalidi per la regola del Bus |
| `note_correttive` su reject | regola del README: *"status rejected DEVE includere note_correttive"* | `failure_handling` e' prosa, non un campo compilabile |
| `retry` / `escalation_count` | regola del README: 2 reject → escalation automatica | nessun contatore |
| firma di chi ha accettato | audit: chi ha detto si' | nessuna |
| criterio di accettazione **valutabile a macchina** | oggi sono frasi italiane (`"qualifier_score >= soglia ICP attiva"`) | nessun codice puo' dire se e' passato |

L'osservazione piu' pesante: **nessun file .py o .sh del repo legge un file HC**.
`grep -rn "handoff\|HC-" --include=*.py empire scripts` → **1 sola riga**, e non e' una lettura:
`empire/core/kernel.py:3` la nomina in un docstring (*"Gestisce routing, handoff, broadcast, e memoria condivisa"*).
Il contratto non e' letto da nulla che decida.

### 1.6 L'agente router mai usato

`.claude/agents/bb-handoff-router.md` esiste ed e' registrato ("Handoff Router del Backbone.
Instrada handoff tra ecosistemi, verifica schema HC-v1"). Non compare in nessun workflow,
in nessuno script, in nessuna skill. Non avrebbe comunque nulla da instradare: la coda che
dovrebbe leggere e' vuota per costruzione.

---

## 2. I REGISTRI E CHI LI LEGGE

**La distinzione che conta: leggere per VERIFICARE (a posteriori, "e' tutto in regola?")
contro leggere per DECIDERE (a runtime, "chi chiamo adesso?").**

| Registro | Dimensione | Chi lo scrive | Chi lo legge (codice) | Perche' |
|---|---|---|---|---|
| `company/skills-map.yaml` | 3.261 righe, 650 voci `- id:` | Chief-Forge, a mano | `empire/registry/cli.py`, `empire/registry/gate.py`, `empire/registry/orphans.py`, `empire/registry/render.py`, `scripts/verify-skills.py`, `scripts/verify-empire.ps1`, `scripts/emperator_hook.py` | **VERIFICA** (7/7). E' un entry point anti-orfano in `orphans.py:ENTRY_POINTS`; `emperator_hook.py:237` lo nomina solo dentro una stringa di testo del promemoria |
| `company/REGISTRO-IMPRESA.md` | 699 righe | Chief-Forge, a mano | `empire/registry/cli.py`, `empire/registry/orphans.py`, `empire/registry/render.py`, `scripts/emperator_hook.py`, `tests/test_registry.py` | **VERIFICA** (5/5). Stesso ruolo: entry point per il calcolo degli orfani |
| `company/Backbone/Identity-HR/registro-agenti.yaml` | 653 righe, 142 voci `- id:` | Identity-HR, a mano | `scripts/verify-agents.py`, `scripts/verify-empire.ps1` | **VERIFICA** (2/2). `verify-agents.py` controlla solo il punto 5 del suo gate: *"se e' di progetto, e' censito in registro-agenti.yaml"* |
| `company/Ecosistemi/REGISTRO-NUMERI.md` | 44 righe, nato 2026-09-04 | a mano | **NESSUNO** (`grep -rln "REGISTRO-NUMERI"` su .py/.sh/.ps1 → 0) | Non e' letto da nessun codice: e' un accordo fra umani, e infatti registra due collisioni gia' avvenute (08-INTELLIGENCE vs 08-STREAM-S7-BOT; 14-LANCI vs 14-TESORERIA) |
| `company/org/inventario-asset.yaml` | — | a mano | `scripts/verify-empire.ps1` | **VERIFICA** (1/1) |
| `company/Ispettorato/registro/` (ERRORI, DECISIONI-ALTIRANGHI, REVISIONI, SUCCESSI) | 4 file | Ispettorato | nessun .py li legge | ne' verifica ne' decide: sono documenti |

**Punteggio: 16 letture di codice sui registri. 16 sono verifiche. ZERO sono decisioni di instradamento.**

### 2.1 Il dato di routing esiste gia' — e nessuno lo usa

`company/Backbone/Identity-HR/registro-agenti.yaml` **contiene i campi giusti**:

```yaml
  - id: CEO-001
    reports_to: LX-Mandato
    supervises: [tutti-gli-ecosistemi]
    input_schema: "{task, context, priority, deadline}"
    output_schema: "{result, next_steps, handoffs[], cost_estimate}"
```

Solo che li ha quasi nessuno. Conteggi su 142 voci: `input_schema` **1**, `output_schema` **1**,
`reports_to` **7**, `supervises` **7**. E l'unico lettore, `scripts/verify-agents.py`,
**non guarda nessuno di questi campi**: controlla che il file .md esista, che il frontmatter sia
parsabile, che il nome combaci col file, che la description sia ≥ 40 caratteri e che l'agente sia censito.
L'`output_schema` del CEO dichiara letteralmente `handoffs[]` — e non lo legge nessuno.

Stessa cosa per `company/skills-map.yaml`: 650 voci con `ecosistema` + `reparto` + `tipo` + `stato`,
cioe' esattamente la mappa "chi sta dove" che servirebbe a un router, e **zero campi
`consuma:` / `produce:` / `input:` / `output:`** (`grep -c` → 1 sola occorrenza, in un commento).
Il registro dice DOVE sta ogni cosa, mai COSA si passano.

---

## 3. IL MOTORE DI FLUSSO — `empire/flow/`

1.401 righe di Python su 11 moduli. E' l'unico motore di orchestrazione vero del repo.

| Modulo | Righe | Cosa fa |
|---|---|---|
| `empire/flow/spec.py` | 185 | parser + validatore di `workflows.yaml`; regole FLOW-DEPENDS-DEAD, FLOW-GATE-UNDECLARED, FLOW-NO-GATES, FLOW-GATE-NO-CRITERION, FLOW-GATE-NO-PATH |
| `empire/flow/dag.py` | 90 | ordine topologico, rilevamento cicli, `unlocked()` |
| `empire/flow/gate.py` | 212 | valutazione gate (metric / file / human / command / conform) |
| `empire/flow/decisions.py` | 162 | politica default-piu'-veto (ADR-EST-006): veto scaduto → il fatto si scrive da solo |
| `empire/flow/evidence.py` | 199 | calcolo dell'evidenza da mostrare a chi conferma un gate umano |
| `empire/flow/state.py` | 83 | log append-only per step in `empire/.data/flow/state/<step>.json`; stato DERIVATO dall'ultima transizione |
| `empire/flow/queue.py` | 48 | ammissione swarm pesanti: max 1, ordine S1>S2>S6>S5, budget-guard sotto il 20% |
| `empire/flow/runner.py` | 164 | validate, gates_table, start_step, done_step, next_unlocked, late_steps |
| `empire/flow/cli.py` | 245 | `python -m empire flow <comando>`; registra anche i plugin estate/trace/forge/avvia |

### 3.1 Cosa definisce

Sorgente unica: `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/workflows.yaml` (222 righe),
risolta via alias `wf_flussi` in `empire/empire.toml`.

- **10 workflow**: WF-MASTER, WF-S1-CONCESSIONARI, WF-S2-MANUALE, WF-S3-PAGINE, WF-S4-MENTALITA,
  WF-S5-YOUTUBE, WF-S6-REBRAND-PROMO, WF-MEM-EOD, WF-MEM-RETRO, WF-PERF-LOOP
- **24 step** con id (`s1.1` … `s6.6`), ognuno con `who` (Max | gael | claude | sistema | A1 | A2), `task`, `due`
- **6 gate**: Gate-DEC (metric), Gate-FUNNEL (file), Gate-CONTATTI (human), Gate-S4 (human), Gate-S5 (human), Gate-REV (metric)
- **3 decisioni** a default-piu'-veto: DEC-EST-001 (prezzo Manuale), DEC-EST-002 (nome Preventa), DEC-EST-004 (nicchia YT)

### 3.2 Che formato hanno i passaggi fra step

**Nessuno.** Un passaggio fra step in `empire/flow` e' esclusivamente `depends:` — una lista di id.
`spec.py` legge `wf_raw.get("depends")`, `dag.py` costruisce gli archi, `runner.start_step()`
rifiuta l'avvio se una dipendenza non e' `DONE`. **Il payload non esiste**: lo step chiuso non
consegna niente al successivo, gli dice solo "puoi partire".
La struttura `Transition` in `state.py` ha `ts, step, from_status, to_status, actor, evidence, note`:
`evidence` e' una stringa in prosa, non un carico tipizzato.
Fra `empire/flow` e i contratti HC-v1 **non c'e' un solo riferimento incrociato**:
sono due sistemi che non si sanno l'uno dell'altro.

### 3.3 Dove scrive lo stato

`empire/.data/flow/state/` (definito in `state.py:STATE_DIR`) e `empire/.data/flow/facts.json`.
Contenuto reale al 2026-09-06:

```
empire/.data/flow/facts.json                3 fatti: dec_001_attiva=1, dec_002_attiva=1, dec_004_attiva=1
empire/.data/flow/state/onred_Gate-S4.json  1 transizione, 2026-07-24T08:42:32
empire/.data/flow/state/onred_Gate-S5.json  1 transizione, 2026-07-24T08:42:32
```

### 3.4 Perche' ha 0 step chiusi

Perche' **nessuno ha mai chiamato `flow done`**. La prova sta nella cartella di stato: su 24 step
dichiarati ci sono **0 file `<step_id>.json`** e **0 file `gate_*.json`**. Gli unici due file
presenti sono `onred_*`: la registrazione di due contromosse su gate ROSSI — non chiusure di lavoro,
ma la presa d'atto che due gate non sarebbero mai diventati verdi
(S4: IG a zero follower, quindi la pubblicazione automatica non ha destinazione;
S5: `FLIKI_API_KEY` vuota, nessun video prodotto).

La causa strutturale: `runner.done_step()` e `runner.start_step()` sono richiamati da
**un solo posto**, `empire/flow/cli.py:115` e `:121`, cioe' dalla riga di comando.
`grep -rn "done_step\|start_step" --include=*.py` fuori da `empire/flow/` e dai test → **0 risultati**.
**Nessun workflow, nessuno script, nessun hook chiude uno step da solo.** Chiudere uno step e'
un atto separato e volontario, ed e' esattamente il tipo di atto che qui non si compie mai —
lo dice il docstring di `empire/trace.py`: *"scrivere la traccia era un atto separato, e gli atti
separati non si fanno"*. Stessa malattia, diagnosticata e mai curata.

Secondo motivo: la finestra e' scaduta. `workflows.yaml` dichiara
`window: {start: "2026-07-21", end: "2026-07-26"}`. Il piano che il motore orchestra e' finito da
**42 giorni** e nessuno ne ha caricato uno nuovo. Il motore gira su un piano morto.

---

## 4. LE TRACCE E L'OSSERVABILITA'

### 4.1 Cosa viene tracciato

`empire/trace.py` (219 righe) definisce **5 tipi di traccia** mappati su 5 cartelle sotto
`WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/`:

| Tipo | Cartella | Quando dovrebbe scriversi | File reali oggi |
|---|---|---|---|
| decisione | `decisions/` | quando si sceglie fra due strade | **6** |
| errore | `errors/` | quando qualcosa fallisce | **6** |
| prestazione | `performances/` | quando una fase si chiude | **7** |
| lezione | `reasoning-bank/` | quando si capisce un pattern | **4** |
| sessione | `sessions/` | apertura/chiusura finestra | **2** |
| | | **TOTALE** | **25** |

Due regole non negoziabili nel codice: `scrivi()` alza `ValueError` se `autore` e' vuoto
("una traccia anonima non e' verificabile") o se `prova` e' vuota ("senza evidenza e' solo una parola").
Idempotente: stesso tipo + titolo + giorno non duplica.

### 4.2 Chi scrive le tracce — il vero motivo del 25

`grep -rn "trace.scrivi\|from empire.trace" --include=*.py` (esclusi test e site-packages):

| Chiamante | Riga | Cosa scrive | Automatico? |
|---|---|---|---|
| `empire/avvia.py:82` (`_step_scrivi_avvio`) | 82 | **una** traccia `sessione` per ogni `python -m empire avvia-estate` | SI, ma solo se qualcuno lancia il comando |
| `empire/flow/cli.py:205` | 205 | **niente** — registra solo il sottocomando `empire trace` nella CLI | no |
| `empire/tests/test_trace.py` | 12 chiamate | scritture di test in tmpdir | no |

**Un solo scrittore automatico nell'intero Impero, e produce un solo tipo di traccia su cinque.**
Le altre quattro (decisione, errore, prestazione, lezione) si scrivono solo a mano con
`python -m empire trace scrivi <tipo> "<titolo>" --autore X --prova Y`.
Ecco perche' sono ferme a 25: sono 25 atti volontari, non 25 sottoprodotti di lavoro.
Il docstring di `trace.py` aveva previsto l'esito e prometteva il contrario
(*"qui la traccia e' un sottoprodotto, non un compito in piu'"*): la promessa non e' stata
mantenuta perche' nessun workflow chiama `scrivi()`.

### 4.3 `company/Memory/state/`

Contiene **un solo ecosistema su 14**: `company/Memory/state/agency/`, 3 file
(`README.md`, `state.json`, `trace.jsonl`).

- `state.json`: schema `agency-state-v1`, `updated_at` fermo al **2026-06-11T18:14:10Z** (87 giorni fa),
  1 ciclo completato (dry-run), 0 attivi, 0 falliti, tutti e 6 i blocchi KPI (a1…a6) a **zero**,
  con nota "baseline da misurare dal giorno 1".
- `trace.jsonl`: 22 righe, tutte del 2026-06-11, tutte dello stesso ciclo dry-run.
- Scritto da `scripts/agency-trace.ps1`, a mano, un evento per invocazione.
- Gli altri 13 ecosistemi (`company/Ecosistemi/`) **non hanno nessuna cartella di stato**.

### 4.4 `company/Backbone/Observability/`

Un solo file: `README.md`. Dichiara:

- file di stato principale `company/metrics/runs.jsonl` — **la cartella `company/metrics/` NON ESISTE**
- schema evento a 13 campi con 9 tipi (`run_done`, `gate_passed`, `gate_failed`, `handoff_rejected`,
  `swarm_done`, `lead_generated`, `content_published`, `sale_closed`, `evolution`) — **nessun emettitore nel repo**
- aggregazioni `company/metrics/cost/{by-agent,by-team,by-eco,by-brand}.json` rigenerate da
  `costs.sh` — **`costs.sh` NON ESISTE**

L'Observability e' **al 100% documentazione**: zero righe di codice, zero file di dati.

### 4.5 Cosa servirebbe perche' le tracce si scrivano da sole

Non manca la funzione: `trace.scrivi()` funziona, e' testata (`empire/tests/test_trace.py`),
rifiuta le tracce senza prova. Manca **il punto di aggancio**. Servono tre cose, tutte assenti:

1. **Una chiamata dentro `runner.done_step()`** — oggi chiudere uno step scrive una `Transition`
   in `empire/.data/flow/state/` e **non** una traccia `prestazione`. Due archivi paralleli che non
   si parlano: 2 transizioni da una parte, 25 tracce dall'altra, nessun ponte.
2. **Un hook di sessione per gli altri 4 tipi** — `empire/avvia.py` dimostra che funziona
   (scrive una `sessione` per run). Non esiste l'equivalente per decisione/errore/prestazione/lezione.
3. **Un emettitore di eventi condiviso** — lo schema di `Observability/README.md`, quello di
   `trace.py` e quello di `agency/trace.jsonl` sono **tre formati diversi per la stessa cosa**
   (13 campi / 8 campi / 10 campi). Finche' restano tre, nessuno puo' scrivere una funzione sola
   che li alimenti tutti.

---

## 5. LA MAPPA DEI COLLEGAMENTI CHE DOVREBBERO ESISTERE

*(sezione in lavorazione)*

## 6. I BUCHI

*(sezione in lavorazione)*
