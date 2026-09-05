# MOTORE — il motore di orchestrazione canonico regge un flusso di lancio?

Oggetto dell'audit: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\company\Ecosistemi\11-APEX-7-CORE\orchestration-layer\`
Data verifica: 2026-09-05. Nessun file del repository è stato modificato per produrre questo report.

---

## 1. COSA E'

**Linguaggio e stack**: Python ≥3.12 dichiarato in `pyproject.toml:9` (l'ambiente disponibile ha Python 3.11.9 e un secondo interprete 3.12.6 via `py -3.12`, verificato con `python --version` e `py -3.12 --version`). Dipendenze dichiarate in `pyproject.toml:10-21`: `alembic`, `asyncpg`, `cryptography`, `fastapi`, `httpx`, `jsonschema`, `pydantic`, `prometheus-client`, `SQLAlchemy`, `uvicorn`. Ponte secondario in TypeScript/Node in `ruflo_bridge/` (con `package.json`, `tsconfig.json`).

**Struttura**: 133 file `.py` (contati con `find . -name "*.py"`, stesso numero citato in ADR-019), organizzati come control-plane a strati:
- `src/orchestrator/domain/` — modelli puri (workflow, plan, task, budget, side-effect, transizioni di stato), senza IO.
- `src/orchestrator/agents/` — 5 agenti deterministici (planner/implementer/critic/gate + skill estese: code-review, security-audit, summarizer, refiner).
- `src/orchestrator/runtime/` — `LocalAgentRuntime` (esecutore in-memory, nessuna rete).
- `src/orchestrator/adapters/postgres/` — persistenza durevole (Unit of Work, outbox, task queue) su PostgreSQL 16.
- `src/orchestrator/governance/` — policy OPA/Rego, capability grant single-use.
- `src/orchestrator/api/` — FastAPI (`app.py`).
- `src/orchestrator/worker/`, `src/tool_gateway/`, `src/plan_memory/`, `src/builder_team/` — worker durevole, gateway strumenti a permesso esplicito, memoria dei piani (BM25 + citazioni), team di builder che ha costruito il motore stesso.
- `migrations/versions/0001_core.sql`, `0002_privacy.sql` — schema Postgres reale (tipi enum, tabelle `workflows`, `tasks`, `task_runs`, RLS).
- `contracts/schemas/v1/` — 9 JSON Schema 2020-12 per i confini (workflow-command, plan, ecc.).
- `docs/adr/001..014` — 14 ADR interni al progetto (in inglese), più `docs/architecture/threat-model.md` e `docs/api/openapi.json`.
- `memory_store/checkpoints/` — un JSON di checkpoint per ogni "work item" di costruzione (W0...W13), storico di build reale.

**Punto di ingresso — non uno solo, più CLI + una API**, tutte dichiarate in `pyproject.toml:31-41` come `[project.scripts]`:
- `builder-team` / `builder-swarm` — bootstrap e attivazione del team che costruisce il motore.
- `plan-memory` — query sui piani con citazione obbligatoria.
- `ocp-contract` — validazione di un JSON contro gli schema.
- `ocp-local-slice` — l'unica pipeline end-to-end dimostrativa (Planner→Implementer→Critic→Gate) su un repository fixture, **richiede un binario OPA esterno** (`README.md:70`, "Start pinned OPA separately").
- `ocp-benchmark` — benchmark deterministico (30 casi comportamentali + 20 workflow concorrenti + 12 query di memoria).
- `ocp-api` / `ocp-worker` / `ocp-outbox` — API FastAPI loopback-only, worker durevole, publisher outbox: richiedono PostgreSQL 16 reale (non presente in questo ambiente).

**Configurazione dei flussi**: non c'è un file YAML/JSON "definisci qui il tuo flusso di lavoro" pensato per un utente finale. Un workflow si costruisce programmaticamente componendo oggetti `Workflow`/`Plan`/`TaskSpec` (vedi §3) oppure via chiamata REST `POST /v1/workflows` (`src/orchestrator/api/app.py:133`) con un body JSON conforme allo schema `contracts/schemas/v1/`. Non esiste un DSL dichiarativo tipo "step1 → step2 → step3" leggibile da un non programmatore.

**In una frase**: è una libreria/control-plane Python installabile (`pip install -e .`), consumabile via CLI multiple o via API REST, non un tool a riga di comando pensato per l'utente finale, e non un framework "no-code" di definizione flussi.

---

## 2. GIRA? (con l'output vero dei test)

**Comando eseguito, esattamente come documentato in `README.md:177-179`:**
```
cd company/Ecosistemi/11-APEX-7-CORE/orchestration-layer
PYTHONIOENCODING=utf-8 PYTHONPATH=src python -m unittest discover -s tests -v
```

**Risultato reale (Python 3.11.9, l'unico interprete con pydantic/fastapi/jsonschema già installati):**
```
Ran 114 tests in 2.891s
FAILED (errors=7, skipped=1)
```
→ **106 test passano davvero**, 7 vanno in errore, 1 viene saltato. Nessun test "finge" di passare: gli errori sono tutti `ImportError`/`ModuleNotFoundError` alla fase di caricamento del modulo, non fallimenti logici.

**I 7 errori, con causa esatta:**
- `tests/integration/test_api_worker_real.py:15` → `ModuleNotFoundError: No module named 'sqlalchemy'`
- `tests/integration/test_postgres_real.py:16` → stessa causa (`sqlalchemy` assente)
- `tests/test_api_extended.py`, `tests/test_operations.py` → falliscono importando `orchestrator.observability.metrics` che a `src/orchestrator/observability/metrics.py:3` fa `from prometheus_client import ...`, pacchetto assente
- `tests/test_api_worker.py` → stessa causa (`prometheus_client` mancante, tramite `orchestrator.api.app`)
- `tests/test_postgres_adapter.py` → `src/orchestrator/adapters/postgres/outbox.py:5` importa `sqlalchemy`, assente
- `tests/test_worker_service.py` → stessa causa a cascata

Verificato con `pip show sqlalchemy asyncpg prometheus-client cryptography`: **`asyncpg`, `sqlalchemy`, `prometheus-client` non sono installati** in nessuno dei due interpreti Python disponibili (3.11.9 e 3.12.6, controllato con `py -3.12 -m pip show ...`). Sono dipendenze dichiarate come **obbligatorie** (non opzionali) in `pyproject.toml:10-21`. Per istruzione ricevuta non le ho installate: questo è un blocco reale di ambiente, non un giudizio sul codice.

**Lo skip**: `test_policy_format_strict_check_and_tests` — richiede `OPA_BIN` (binario Open Policy Agent esterno pinnato). Cercato con `where opa` e `find ... -iname "opa.exe"`: **non presente sul sistema**.

**Test aggiuntivo eseguito con successo — il benchmark "vero" (non solo test unitari) indicato dalla skill `ocp-control-plane`:**
```
PYTHONPATH=src python -m benchmarks.cli --output .../w9-baseline.json
```
Esito reale, letto dal JSON prodotto: tutti e 6 gli hard gate `true` (`behavior_accuracy_1_0`, `quality_pass_1_0`, `evidence_pass_1_0`, `concurrent_completion_20_20`, `memory_recall_at_5_gte_0_95`, `citation_accuracy_1_0`). Latenza reale misurata: p50 18ms, p95 30ms, p99 35ms su 30 casi; 20 workflow concorrenti completati in 417ms; `cost_usd: 0.0` su tutti i casi (coerente col fatto che non c'è nessuna chiamata a modello, §4). Il campo `ruflo_comparison` riporta onestamente `"status": "BLOCKED", "reason": "provider-backed agent_execute is not certified", "fabricated_results": false` — il codice stesso dichiara di NON aver fabbricato un risultato che non poteva produrre.

**Discrepanza da segnalare**: la skill `.claude/skills/ocp-control-plane/SKILL.md:50-51` si aspetta "~148 test verdi, ~11 skip". La misura reale oggi è 114 test totali, 106 verdi, 7 errori d'import, 1 skip. La skill descrive uno stato (o un ambiente con dipendenze installate) diverso da quello effettivamente verificabile in questa sessione — non ho potuto stabilire se sia la skill ad essere disallineata o l'ambiente locale a mancare di pacchetti che altrove sono installati.

**Non eseguiti** (dichiarato, non fatto girare): `ocp-local-slice` (richiede OPA_BIN assente), test `ruflo_bridge` (richiede `npm install`, `node_modules/` assente nella cartella, non installato per non toccare il repository), qualunque test contro un vero PostgreSQL (nessun server Postgres disponibile).

---

## 3. COSA SA FARE

Letto nel codice, non nei README:

- **Definizione di flussi/step**: sì, ma vincolata. `src/orchestrator/domain/plan.py:20-21` impone `if not 1 <= len(self.tasks) <= 6: raise InvalidPlan("Plan must contain 1..6 tasks including remediation")` — **un Plan può avere al massimo 6 task**. `src/orchestrator/domain/task.py:10` fissa il vocabolario dei ruoli possibili: `ALLOWED_ROLES = {"planner", "implementer", "critic", "gate", "compensator"}`, verificato anche a runtime (`task.py:27-28`). Non esiste un ruolo generico "phase" o "step" a piacere: il motore modella UN pattern fisso (pianifica→esegui→critica→cancella), non un DAG libero di fasi nominate dal dominio applicativo.
- **DAG e parallelismo**: `Plan.topological_order()` e `Plan.parallel_groups()` (`plan.py:41-73`) calcolano ordine topologico e gruppi eseguibili in parallelo da `depends_on`; cicli vengono rifiutati. Testato in `tests/test_domain.py` (`test_cycle_is_rejected`, `test_topological_order_and_parallel_groups`, entrambi verdi).
- **Stato persistente**: sì, a due livelli. In memoria: `Workflow` è un dataclass con `version`/`sequence` e log di `DomainEvent` (`src/orchestrator/domain/workflow.py`). Su disco/DB: `migrations/versions/0001_core.sql:13-32` definisce una tabella `workflows` reale con `status`, `version` (optimistic concurrency), `budget_used`, `updated_at`; una tabella `tasks` con lease (`leased_by`, `leased_until`), tentativi limitati (`max_attempts` 1..3) e outbox transazionale. **Ma questa persistenza reale richiede PostgreSQL 16 e non è mai stata verificata contro un server reale in questo ambiente** — il README lo dichiara esso stesso (`README.md:53`: "current sandbox tests verify SQL structure ... they do not claim to prove PostgreSQL locking, RLS or failover semantics").
- **Ripresa dopo un errore / pausa umana**: il modello a stati (`src/orchestrator/domain/states.py:21-42` + `src/orchestrator/domain/transitions.py:26-115`) è sorprendentemente completo per questo caso d'uso specifico: esistono transizioni esplicite `RUNNING → PAUSED` (attore `SYSTEM`, `transitions.py:51`) e `PAUSED → RUNNING` (attore `HUMAN`, richiede il flag `resume_allowed`, `transitions.py:52-54`), oltre a `PLAN_REVIEW → AWAITING_APPROVAL` e `AWAITING_APPROVAL → AUTHORIZED` (attore `HUMAN`, richiede `approval_valid`+`plan_hash_matches`+`policy_hash_matches`, `transitions.py:39,45-47`). Esiste anche l'endpoint REST corrispondente: `POST /v1/workflows/{workflow_id}/approve` (`src/orchestrator/api/app.py:165`). Il concetto "fermati e aspetta una decisione umana" **esiste nel dominio ed è testato** (`tests/test_domain.py`, tutti verdi), ma nessun test dimostra che sopravviva per *giorni* su un processo reale: il tempo di attesa dipende dalla persistenza Postgres, non verificata (vedi sopra).
- **Gate/validazioni bloccanti**: sì, multipli livelli — `Plan.__post_init__` richiede almeno un task `"gate"` (`plan.py:38-39`); `GateAgent` (`src/orchestrator/agents/repository_adr.py:121-141`) produce verdetto `PASS`/`REMEDIATE` da issue bloccanti e gate deterministici; `QUALITY_REVIEW → COMPLETED` richiede il flag `all_blocking_gates_pass` (`transitions.py:88-89`); contratti JSON Schema 2020-12 rifiutano proprietà sconosciute, cicli, budget sforati (`tests/test_contracts.py`, tutti verdi).
- **Chiamate a modelli**: no — vedi §4.
- **Parallelismo**: sì, a livello di esecuzione simulata — il benchmark W9 ha fatto girare **20 workflow concorrenti realmente in asyncio** (417ms totali, misurato, non dichiarato), non solo teoricamente.
- **Logging**: sì, strutturato — `src/orchestrator/observability/` produce log redatti e metriche Prometheus (quest'ultime non testabili qui per `prometheus_client` mancante, §2).
- **Sicurezza per difetto**: policy OPA "default-deny" con fail-closed su errore HTTP (`tests/test_governance.py:test_http_error_fails_closed`, verde); capability grant a singolo uso, non ripetibili (`test_single_use_token`, verde); nessuno strumento di shell o rete libera esiste nel Tool Gateway (dichiarato in `README.md:63` e confermato dai soli due strumenti implementati: lettura repo scoped, scrittura ADR immutabile).

---

## 4. CHIAMA UN MODELLO?

**No.** Verifica attiva: `grep -rn "anthropic|openai|claude-3|ANTHROPIC_API_KEY|messages.create|chat.completions"` su tutto `src/` → **zero risultati**.

La prova più diretta è nel codice stesso, non in un documento: `src/orchestrator/runtime/local.py:13`, il docstring della classe che esegue i task dichiara letteralmente:
> `"""Deterministic baseline runtime. It cannot spawn agents or call tools itself."""`

Gli agenti "Planner/Implementer/Critic/Gate" (`src/orchestrator/agents/repository_adr.py:10-142`) non invocano nessuna API esterna: `ImplementerAgent.__call__` (righe 40-94) genera un ADR **con un f-string template Python** riempito da hash SHA-256 e nomi di file passati in input — zero generazione probabilistica. `CriticAgent` (righe 97-118) verifica con `if f"## {section}" not in adr` — ricerca di sottostringa, non giudizio di un modello. Coerente con l'esito del benchmark W9: `cost_usd: 0.0` su tutti i 30 casi (§2) — se avesse chiamato un modello a pagamento il costo non sarebbe zero.

Il README stesso lo conferma in più punti come limite dichiarato, non nascosto: "RuFlo remains disabled" (riga 77), "Provider-backed `agent_execute` is not certified because no provider credential is available; therefore production routing remains disabled and LocalRuntime remains active" (righe 89), "RuFlo generative execution remains disabled" (badge in `api/app.py:93`).

**Conclusione**: il motore oggi è un control-plane deterministico che governa (contratti, policy, budget, stato) ma **non genera nulla con un LLM**. Il ponte verso un motore che potrebbe farlo (`ruflo_bridge/`, pinnato a `ruflo@3.38.19`) esiste ma non è certificato in questo ambiente (nessun `npm install` mai eseguito, §2) e comunque, per stessa ammissione del README, l'esecuzione generativa resta disattivata anche quando il bridge passa i suoi test di smoke.

---

## 5. CHI LO CHIAMA OGGI

Cercato in tutto il repository (`.claude/agents/`, `.claude/skills/`, `scripts/`) chi importa o esegue davvero `orchestration-layer`.

**Risultato: un solo chiamante, ed è un comando diagnostico, non un consumatore di produzione.**

- `.claude\skills\ocp-control-plane\SKILL.md` — l'unico artefatto che invoca concretamente il motore (esegue la sua test suite e il benchmark W9). Ma il file stesso dichiara esplicitamente, al passo 4 e nel promemoria finale: **"OCP non governa ancora nessun consumatore reale (`calc/engine.py`, `arena_generator.py`, `main.py` restano fuori dal suo perimetro)"** (riga 79-80) — cioè anche il suo unico chiamante conosciuto certifica che non c'è nessun lavoro reale dietro.
- `.claude\agents\guild-quality.md` e `.claude\agents\sentinel-drift.md` — citano `orchestration-layer` solo come riferimento testuale/di governance (menzione, non `import`/`subprocess`).

Questo combacia esattamente con quanto già misurato e scritto in `company/Memory/decisions/ADR-019-motore-orchestrazione-canonico.md:35` ("Nessuno script di Digital Empire chiama nessuno dei due motori") e ribadito alla riga 79 ("OCP non governa ancora nessun consumatore reale"). **Nessun agente, skill di produzione, script di outreach, di YouTube, di formazione o di marketing lo importa o lo esegue.** L'unico "consumatore" è l'auto-verifica del motore su se stesso.

---

## 6. PUO' REGGERE UN FLUSSO DI LANCIO A 10 FASI?

Caso concreto richiesto: ~10 fasi in sequenza, ognuna produce un JSON, controlli bloccanti fra fasi, possibilità di fermarsi per giorni ad aspettare una decisione umana e riprendere, stato salvato su disco.

**Cosa il motore regge già, con prova a supporto:**
- Output per fase come artefatto verificabile: sì — il Tool Gateway scrive artefatti immutabili con hash e li rende idempotenti (`tests/test_tool_gateway.py:test_artifact_write_is_immutable_and_idempotent`, verde).
- Controllo bloccante fra una fase e l'altra: sì — pattern gate testato e obbligatorio per plan (`plan.py:38-39`, `transitions.py:88-89`).
- Pausa per attesa umana e ripresa: sì **nel modello di dominio** — `RUNNING↔PAUSED` e `AWAITING_APPROVAL→AUTHORIZED` via attore `HUMAN`, con endpoint REST `POST /v1/workflows/{id}/approve` (`api/app.py:165`). Questo è precisamente il meccanismo richiesto, e non è vaporware: è testato in `tests/test_domain.py` (verde).
- Stato su disco: progettato (schema Postgres completo con `version`, lease, outbox transazionale — `migrations/versions/0001_core.sql`), **ma mai provato contro un Postgres vero** (README.md:53, dichiarato dal progetto stesso) e non eseguibile in questo ambiente per mancanza di `sqlalchemy`/`asyncpg` (§2).

**Cosa manca, con prova a supporto — questo è il punto centrale:**
1. **Un Plan non può avere 10 fasi.** `src/orchestrator/domain/plan.py:20-21` impone un tetto rigido di **1..6 task per Plan**: `"Plan must contain 1..6 tasks including remediation"`. Un flusso a 10 fasi non entra in un singolo Plan/Workflow così come il motore è oggi.
2. **Il vocabolario dei ruoli è chiuso a 5 nomi fissi**, non a fasi di dominio: `ALLOWED_ROLES = {"planner", "implementer", "critic", "gate", "compensator"}` (`task.py:10`), verificato anche a runtime (`task.py:27-28`) e nel CHECK della tabella SQL `tasks.role` (`0001_core.sql:39`). Non esiste un modo nativo per chiamare una fase "ricerca-mercato" o "bozza-copy": ogni fase reale del business andrebbe forzata dentro "implementer" con l'oggettivo (`objective`) come testo libero, e il motore non distingue una fase dall'altra a livello di schema.
3. **Non esiste concetto di "workflow-di-workflow" o pipeline che incateni più Workflow in sequenza** — cercato nel codice (`chain_workflow`, `pipeline`, `parent_workflow`, ecc.): nessun risultato. Per arrivare a 10 fasi bisognerebbe o (a) costruire un orchestratore esterno che lancia 10 Workflow OCP separati in sequenza (uno per fase, ciascuno ≤6 task, ciascuno con il proprio gate), gestendo a mano il passaggio di stato/JSON da un Workflow al successivo, oppure (b) modificare lo schema SQL, il dominio (`ALLOWED_ROLES`, il tetto di 6 task) e i contratti JSON Schema per introdurre un concetto di "fase applicativa" che oggi non c'è.
4. **Nessuna generazione reale di contenuto**: se una qualunque delle 10 fasi richiede scrivere copy, analizzare un mercato, generare un piano — cioè richiede un modello — il motore non lo fa (§4). Andrebbe collegato un runtime diverso da `LocalAgentRuntime`, oggi non certificato (RuFlo, §4).
5. **La persistenza "per giorni" non è provata**: senza un Postgres reale in funzione, "salvato su disco e ripreso fra giorni" resta un disegno testato solo in memoria/mock.

**Stima di lavoro per adattarlo** (stima, non misurata): installare e certificare PostgreSQL 16 + le dipendenze mancanti (1-2 giorni); progettare e implementare il livello di concatenamento fra Workflow o alzare il tetto di 6 task e allargare `ALLOWED_ROLES` a un concetto di fase applicativa, con relative migrazioni SQL e schema JSON (3-6 giorni di lavoro, stima approssimativa non verificata); collegare un runtime che chiami davvero un modello per le fasi che lo richiedono (dipende dalla certificazione RuFlo, oggi bloccata per mancanza di credenziali provider — tempo indeterminato). **In sintesi: il motore regge l'ossatura concettuale del caso d'uso (stato, gate, pausa/ripresa umana) ma non la sua forma concreta a 10 fasi così com'è oggi.** Va adattato, non solo configurato.

---

## 7. IL COSTO DI ADOTTARLO

**Documentazione**: buona per uno sviluppatore, assente per un non tecnico. Il `README.md` (180 righe) racconta onestamente la storia di ogni checkpoint di build (W0...W13) con tanto di limiti dichiarati ad ogni fase — è raro trovare un progetto interno che scrive "PRR verdict NO_GO" (`README.md:137`) sul proprio stesso stato invece di nasconderlo. Esistono inoltre 14 ADR interni al progetto (`docs/adr/001..014`, in inglese) e un threat model (`docs/architecture/threat-model.md`). **Ma tutto questo presuppone di saper leggere codice Python, schema JSON, SQL e concetti come "optimistic concurrency", "capability grant", "outbox pattern"**: non c'è una guida "come lancio il mio primo flusso di lavoro" per chi non ha scritto il motore.

**Ripidità**: alta. Per capirlo davvero servono contemporaneamente: FastAPI, SQLAlchemy/asyncpg async, Alembic, OPA/Rego, JSON Schema 2020-12, pattern DDD (aggregate, eventi di dominio, optimistic concurrency), e — per la parte `ruflo_bridge` — TypeScript/Node. Non è un motore "leggi il README e parti": il README stesso rimanda a comandi che richiedono un binario OPA esterno pinnato e un server PostgreSQL 16, nessuno dei due incluso o scaricabile con un solo comando.

**Ownership**: `CODEOWNERS` (root del progetto) contiene solo placeholder — `@architecture-owner`, `@implementation-owner`, `@security-owner`, ecc. — con la nota esplicita in cima: *"Final ownership identities will replace role placeholders before PRR."* **Non c'è ancora un proprietario umano nominato per nessuna parte del codice.** Combinato con ADR-019 (che attribuisce il lavoro a Neri come autore) questo significa: oggi è sostanzialmente opera di una persona sola, senza distribuzione di conoscenza formalizzata nel repo stesso.

**Per un socio che non l'ha scritto** (Max o Gael): raccapezzarsi richiederebbe leggere in ordine il README (180 righe, denso), poi almeno `src/orchestrator/domain/` (workflow, plan, task, transitions — la parte concettualmente più riusabile) e i test corrispondenti per capire cosa è davvero garantito. Stima approssimativa e non misurata: **1-2 giornate piene** per un profilo che già conosce Python/async/DDD, di più per chi parte da zero su questi pattern.

---

## 8. VERDETTO IN TRE RIGHE

Si adotta con adattamenti — mai così com'è oggi per un flusso a 10 fasi.
La ragione principale: il motore impone un tetto rigido di 6 task per Plan e un vocabolario di ruoli chiuso a 5 nomi (planner/implementer/critic/gate/compensator), quindi non rappresenta nativamente 10 fasi di business, e non chiama nessun modello — la parte "genera contenuto" andrebbe comunque costruita altrove o certificata via RuFlo (oggi bloccato).
Il rischio della scelta: adottarlo oggi significa costruire il collante mancante (concatenamento di Workflow, Postgres reale, runtime generativo) prima di avere un solo lancio servito — cioè rifare esattamente l'errore che ADR-019 ha già misurato una volta (133 file, zero consumatori) se l'adattamento non parte da un lavoro vero e non si ferma finché non lo serve.

---

## 9. COSA NON HO POTUTO VERIFICARE

- **`ocp-local-slice`** (la pipeline dimostrativa end-to-end Planner→Implementer→Critic→Gate, l'unica cosa vicina a un "flusso completo" nel repository): richiede un binario OPA esterno pinnato (`OPA_BIN`), assente sul sistema (verificato con `where opa` e ricerca di `opa.exe` — nessun risultato). Non esiste una policy dichiarata su come procurarselo senza toccare il repository.
- **Persistenza reale su PostgreSQL 16**: nessun server Postgres disponibile in questo ambiente; i pacchetti Python `sqlalchemy` e `asyncpg` non sono installati (né nell'interprete 3.11.9 né nel 3.12.6 disponibile) e sono dipendenze obbligatorie non opzionali — non installati per istruzione ricevuta di non toccare l'ambiente/repository in modo invasivo. Di conseguenza 5 dei 7 moduli di test in errore (Postgres/API/worker) restano non verificati nel merito, solo nel fatto che non si importano.
- **Metriche Prometheus e osservabilità** (`prometheus_client` mancante): stesso discorso, 2 moduli di test coinvolti.
- **`ruflo_bridge`** (il ponte TypeScript verso RuFlo, pinnato a `ruflo@3.38.19`): `node_modules/` assente, mai eseguito `npm install` in questa cartella — non esaminato in esecuzione, solo letto a livello di file di configurazione (`package.json`, `tsconfig.json`).
- **Comportamento con OPA realmente in esecuzione** (l'unico modo per verificare il default-deny "vero" end-to-end, non solo mockato nei test unitari).
- **Se la discrepanza fra i "~148 test verdi, ~11 skip" attesi da `.claude/skills/ocp-control-plane/SKILL.md:50-51` e i 114 test/106 verdi/1 skip/7 errori osservati oggi dipenda da un ambiente diverso in cui la skill è stata scritta (con le dipendenze installate) o da un disallineamento della skill stessa**: non determinabile senza sapere in quale ambiente la skill è stata validata l'ultima volta.
- Non mi sono allargato oltre il perimetro richiesto: non ho valutato `11-APEX-7-CORE/orchestrator` o `11-APEX-7-CORE/orchestration` (gli "archivi storici" pre-ADR-019), né la qualità di RuFlo stesso, né proposto un piano di adattamento dettagliato — solo la stima di massima richiesta al punto 7 del compito.
