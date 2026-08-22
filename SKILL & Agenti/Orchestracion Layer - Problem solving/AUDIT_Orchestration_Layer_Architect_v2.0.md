# Audit tecnico completo — Orchestration Layer Architect v2.0

**Data:** 11 agosto 2026  
**Runtime richiesto:** Python 3.11+ / `asyncio` puro  
**Tipo di audit:** architettura, correttezza distribuita, codice Python, resilienza, sicurezza, observability, testing e sistema multi-agente

---

## 1. Verdetto esecutivo

Il documento è una **buona carta d'intenti** e contiene numerosi principi corretti, ma **non è production-ready** e non implementa ancora il sistema multi-agente che descrive.

Nella forma attuale combina quattro artefatti differenti:

1. un system prompt di governance;
2. uno standard di coding Python;
3. una bozza di runtime per workflow distribuiti;
4. un registro di “agenti” descritti come ruoli.

Questi quattro piani non sono separati da contratti e confini eseguibili. Il risultato è un sistema molto prescrittivo sul piano testuale, ma fragile sul piano operativo.

### Valutazione sintetica

| Area | Valutazione | Motivo principale |
|---|---:|---|
| Visione e principi | 7/10 | Nucleo valido, ma diversi assoluti sono tecnicamente falsi o controproducenti. |
| Compilabilità del codice | 3/10 | Import mancanti, tipi errati, componenti non definiti e test incoerenti. |
| Correttezza distribuita | 2/10 | Idempotenza race-prone, nessun recovery durevole, Saga non persistita. |
| Resilienza | 4/10 | Pattern presenti nominalmente, ma applicati sempre e con implementazioni difettose. |
| Sicurezza | 4/10 | Buone intenzioni; JWT, validazione, logging e DLQ hanno gap critici. |
| Observability | 5/10 | Tracing di base presente; mancano resource identity, metric provider, redaction e propagazione reale. |
| Sistema multi-agente reale | 2/10 | Esiste un catalogo di personas, non un runtime multi-agente. |
| Production readiness complessiva | **2/10** | Non deve essere presentato o distribuito come “Production Ready”. |

### Esito

**🔴 BLOCCATO PER LA PRODUZIONE.**

Prima della costruzione va rifattorizzato in due sistemi distinti:

```text
BUILDER CONTROL PLANE
├── policy engine
├── agent router
├── generative workers
├── deterministic verifiers
└── artifact/evaluation pipeline

WORKFLOW RUNTIME
├── durable workflow state
├── scheduler + worker leases
├── idempotent step executor
├── ports/adapters
├── retries/circuit/bulkhead
├── outbox/inbox + reconciliation
└── Saga/compensation engine
```

---

## 2. Posizionamento rispetto a NERVE-SOLVE

Questo documento **non è NERVE-SOLVE**.

- **NERVE-SOLVE** è il cognitive control layer che mappa e risolve problemi.
- **Orchestration Layer Architect** è un builder/governance control plane che dovrebbe progettare, generare e verificare software di orchestrazione.
- **Workflow Runtime** è l'infrastruttura Python che esegue workflow durevoli.

I tre elementi possono collaborare, ma non devono essere fusi:

```text
Richiesta di costruzione
        │
        ▼
Builder Control Plane ── usa NERVE-SOLVE per framing/design
        │
        ▼
Genera e verifica artefatti Python
        │
        ▼
Workflow Runtime esegue gli artefatti approvati
```

Definire tutti e tre “orchestration layer” senza qualificazione produce ambiguità strutturale.

---

## 3. Findings bloccanti — P0

### P0-01 — Il “multi-agent system” non è implementato

Il registro AGT-00…AGT-31 definisce nomi, trigger e responsabilità, ma mancano:

- classi o processi agente;
- registry machine-readable;
- router eseguibile;
- code/queue di task;
- stato condiviso;
- timeout e budget per agente;
- validazione dello handoff JSON;
- policy di accesso agli strumenti;
- isolamento del contesto non fidato;
- gestione dei fallimenti parziali;
- provenance dell'output;
- modello di consenso o arbitraggio verificabile;
- test ed eval degli agenti.

**Impatto:** il documento può al massimo simulare più ruoli dentro un singolo LLM. Non garantisce indipendenza, parallelismo o verifica reale.

**Fix:** separare agenti generativi da controlli deterministici e implementare un `AgentRuntime` con registry, typed envelope, job state, deadline, budget, artifact store e verifier pipeline.

---

### P0-02 — `asyncio` puro non fornisce workflow durevoli

`asyncio` gestisce concorrenza nel processo; non rende un workflow recuperabile dopo crash, deploy, perdita del nodo o riavvio.

Per dichiarare il runtime durevole servono almeno:

- stato persistito con versionamento;
- worker lease con scadenza;
- scheduler di step recuperabili;
- inbox/outbox transazionali;
- replay/resume;
- deduplica atomica;
- recovery dei casi `UNKNOWN`;
- heartbeat e reaper dei lease scaduti.

**Impatto:** un crash tra side effect esterno e salvataggio locale può duplicare pagamenti, prenotazioni o compensazioni.

**Fix:** mantenere `asyncio` come execution runtime, ma aggiungere PostgreSQL come fonte di verità durevole e Redis solo per ottimizzazioni/locking non autorevole.

---

### P0-03 — L'idempotenza proposta non è atomica

Il pattern:

```text
get(key) → execute side effect → set(key)
```

ha una race TOCTOU. Due worker concorrenti possono leggere “missing” ed eseguire entrambi l'effetto.

Inoltre:

- `attempt` entra nella chiave: un retry può cambiare chiave e duplicare l'effetto;
- il `workflow_id` viene rigenerato a ogni `execute()`;
- la stessa `correlation_id` non produce lo stesso workflow ID;
- il test che si aspetta una sola chiamata con la stessa correlation ID fallisce;
- un crash dopo il side effect ma prima di `store.set()` lascia esito ambiguo;
- il risultato deserializzato torna come `dict`, non necessariamente come `T`;
- il TTL fisso di 24 ore non è una garanzia di dominio.

**Fix obbligatorio:**

1. chiave stabile per operazione logica, senza numero di tentativo;
2. claim atomico con unique constraint o compare-and-set;
3. stati `CLAIMED/RUNNING/SUCCEEDED/FAILED/UNKNOWN`;
4. lease owner e versione;
5. stesso idempotency key propagato al servizio downstream;
6. codec tipizzato del risultato;
7. reconciliation quando l'esito esterno è ambiguo.

Formula consigliata:

```text
sha256(tenant_id : workflow_type : business_request_id : step_name : step_version)
```

La correlation ID serve al tracing, **non** alla deduplica.

---

### P0-04 — `BaseOrchestrator` non supporta resume e rompe il test di deduplica

Ogni chiamata genera:

```python
workflow_id = str(uuid.uuid4())
```

Non esiste `load_or_create`, non c'è business request ID, non viene ricaricato uno stato esistente e non c'è replay degli step completati.

**Impatto:** ogni retry dell'intero workflow è visto come un workflow nuovo.

**Fix:** `execute()` deve ricevere un `request_id` stabile e fare `state_repository.load_or_create(...)` in modo atomico. Un nuovo workflow ID va creato solo se la richiesta non esiste.

---

### P0-05 — Lo stato è dichiarato immutabile ma viene mutato

`WorkflowState` non è `frozen=True` e contiene liste/dizionari mutabili. `mark_step_completed()` modifica la lista in place.

Contemporaneamente `transition_to()` crea un nuovo oggetto. I due modelli — mutabile e immutabile — convivono e producono update persi o snapshot incoerenti.

Mancano inoltre:

- `version` per optimistic concurrency;
- stato per ogni step;
- attempt count;
- lease owner;
- deadline;
- result reference;
- evento di transizione;
- stati `CANCELLED`, `TIMED_OUT`, `PAUSED`, `DEGRADED`, `MANUAL_INTERVENTION`, `UNKNOWN`.

**Fix:** stato realmente immutabile, collezioni immutabili e repository CAS:

```python
async def save(self, state: WorkflowState, *, expected_version: int) -> WorkflowState: ...
```

---

### P0-06 — La Saga non persiste nulla

`SagaCoordinator` riceve `state_repository` ma non lo usa. Questo contraddice la docstring “persistere lo stato a ogni step”.

Altri problemi:

- output delle action ignorati;
- compensazioni costruite come closure in memoria;
- nessun resume dopo crash;
- nessun idempotency key per compensazione;
- nessuna transition a `COMPENSATING`;
- compensazione fallita solo loggata, non registrata nel risultato;
- nessuna DLQ effettiva;
- il passo che va in timeout può essere riuscito sul sistema remoto ma non viene compensato;
- `critical=False` può fallire e il risultato finale viene comunque impostato a `success=True`;
- `failed_step` ed `error` possono coesistere con `success=True`;
- `Callable[[], Awaitable[any]]` usa la funzione built-in `any`, non `typing.Any`.

**Impatto:** non è una Saga durevole e non garantisce una compensazione corretta.

**Fix:** persistere prima e dopo ogni action/compensation, mantenere step status e result reference, usare una strategia di reconciliation per gli esiti ambigui e rappresentare `DEGRADED`/`COMPENSATION_FAILED` esplicitamente.

Nota concettuale: una compensazione è un'azione semantica inversa, **non** un rollback ACID e non garantisce il ritorno esatto allo stato precedente.

---

### P0-07 — Il Circuit Breaker HALF_OPEN è concorrenzialmente errato

In `call()` il lock viene rilasciato prima dell'operazione. In stato `HALF_OPEN`, tutte le chiamate concorrenti possono passare. `half_open_max_calls` conta successi completati, non limita le probe in flight.

Inoltre:

- il fallback viene eseguito mentre il lock è detenuto in stato OPEN;
- un fallback che riutilizza il breaker può deadlockare;
- il fallback lento serializza tutte le richieste;
- viene usato wall clock invece del tempo monotono;
- `expected_exception=Exception` considera anche bug di programmazione e errori permanenti come failure del servizio;
- la composizione con retry non è definita;
- lo stato è process-local e diverge tra worker.

**Fix:** probe permit/semaphore dedicato, fallback fuori dal lock, clock monotono, allowlist di failure transitorie e metriche per transizione.

---

### P0-08 — Retry indiscriminato

`retryable_exceptions=(Exception,)` ritenta praticamente tutto:

- errori di autenticazione;
- input invalidi;
- errori di programmazione;
- vincoli di dominio;
- pagamenti rifiutati;
- errori permanenti.

Mancano deadline complessiva, `Retry-After`, predicate sui risultati e stop immediato su circuit open. Il commento “tutti i tentativi esauriti → DLQ” non è implementato.

**Impatto:** retry storm, latenza incontrollata e possibile duplicazione di side effect.

**Fix:** retry solo su una tassonomia esplicita di errori transient; stesso idempotency key; deadline end-to-end; budget; stop su errori permanenti; DLQ solo per task asincroni replayable.

---

### P0-09 — `critical=False` nasconde errori pericolosi

`_run_step()` cattura ogni `Exception` e restituisce `None` quando lo step non è critico.

Può quindi ignorare:

- bug;
- violazioni auth;
- contratti incompatibili;
- corruzione di dati;
- problemi di configurazione.

Il workflow viene marcato `COMPLETED` senza segnalare degradazione nell'output o nello stato.

**Fix:** graceful degradation solo per failure classificate e attese. Usare un risultato discriminato e stato `DEGRADED`; mai ingoiare eccezioni arbitrarie.

---

### P0-10 — Gestione incompleta di timeout e cancellation

La documentazione Python specifica che `asyncio.wait_for()` cancella il task e può attendere il completamento della cancellazione; il tempo totale può superare il timeout [1](https://docs.python.org/3.11/library/asyncio-task.html).

La cancellazione locale non dimostra che il servizio remoto abbia annullato il side effect. Il sistema attuale tratta il timeout come fallimento certo.

`BaseOrchestrator` non gestisce esplicitamente `asyncio.CancelledError`: un worker cancellato può lasciare lo stato `IN_PROGRESS`.

**Fix:** deadline monotona, stato `UNKNOWN` per operazioni esterne ambigue, status query/reconciliation e gestione esplicita della cancellazione con persistenza prima del re-raise.

---

### P0-11 — Validazione Pydantic non sufficientemente sicura

“Pydantic sanitizza” è un'affermazione scorretta: valida e può fare coercion, ma non sostituisce sanitizzazione contestuale o authorization.

In Pydantic v2:

- `class Config` è ancora supportato ma deprecato;
- gli extra fields vengono ignorati di default;
- gli errori possono includere il valore di input.

La documentazione raccomanda `ConfigDict`; `extra="forbid"` blocca campi inattesi e `hide_input_in_errors=True` evita l'esposizione dei valori negli errori [2](https://docs.pydantic.dev/latest/api/config/).

**Fix:** modello base con `strict=True`, `extra="forbid"`, `frozen=True`, limiti dimensionali e input nascosti negli errori. Usare `model_validate()`.

---

### P0-12 — Verifica JWT incompleta

Il codice richiede la presenza di `iss`, ma non verifica che corrisponda a un issuer fidato. Non passa `audience`, non richiede `aud`, non gestisce JWKS/key rotation e non lega il token al servizio destinatario.

PyJWT distingue tra “claim presente” e verifica del valore; `issuer=` e `audience=` sono parametri specifici di `jwt.decode()` [3](https://pyjwt.readthedocs.io/en/stable/api.html?highlight=decode).

**Fix minimo:** algoritmo pinning, issuer trusted, audience prevista, `exp/iat/nbf/sub/jti`, JWKS rotation, leeway limitata, scope normalizzato e audit delle decisioni di autorizzazione.

---

### P0-13 — DLQ con possibile esfiltrazione di dati

`DLQMessage.original_payload` conserva l'intero payload. Può includere:

- token;
- dati personali;
- dati di pagamento;
- segreti;
- documenti riservati.

Mancano cifratura, redaction, retention, ACL, schema version, message ID, tenant, checksum e policy di replay.

**Fix:** salvare un riferimento cifrato a un payload redatto, non il payload completo; separare quarantine da replay queue; autorizzare e auditare ogni replay.

---

### P0-14 — Il codice non compila come progetto completo

Esempi di simboli/import mancanti o errati:

- `Callable`, `Awaitable`, `T` in più moduli;
- `StateRepository`;
- `IdempotencyKey` nel `BaseOrchestrator`;
- `Any` nel Saga Coordinator;
- `Optional` nella Retry Policy;
- `logging` nell'observability setup;
- `DLQPublisherPort`;
- modelli request/response e numerose eccezioni;
- `PaymentAuthorizationResponse.processed_at` manca nel test;
- dipendenza `PyJWT` non presente nel `pyproject.toml`.

**Fix:** trasformare gli snippet in package reale ed eseguire obbligatoriamente `ruff`, `pyright --strict` o `mypy --strict`, import test e `pytest` in CI.

---

### P0-15 — Contraddizioni nella governance

Il documento impone:

- servizi che non si conoscono mai;
- orchestrator unico depositario del flusso;
- Pattern Advisor che può scegliere coreografia o ibrido;
- orchestrator senza business logic;
- conditional routing e compensazioni dentro l'orchestrator.

Queste regole non possono essere tutte assolute contemporaneamente.

**Fix:** distinguere:

- **domain logic:** calcoli e invarianti, fuori dall'orchestrator;
- **process policy:** ordine, branching, retry semantic e compensazioni, legittimamente nell'orchestrator;
- **orchestration:** controllo centrale quando serve;
- **choreography:** servizi/event handlers che conoscono contratti evento, non necessariamente altri servizi;
- **ibrido:** consentito per side effect e bounded context distinti.

---

## 4. Findings importanti — P1

### P1-01 — Pattern di resilienza resi obbligatori ovunque

“Timeout + retry + circuit breaker + fallback + bulkhead + DLQ + Saga sempre” è un anti-pattern di complessità.

Esempi:

- fallback non semanticamente accettabile per un pagamento;
- DLQ irrilevante in una chiamata sincrona;
- circuit breaker inutile su funzione locale;
- retry dannoso per errore permanente;
- Saga non necessaria per operazioni read-only;
- bulkhead superfluo in flussi a basso volume.

**Fix:** resilienza guidata da failure mode, SLO e semantica dell'operazione.

---

### P1-02 — “Ogni operazione deve essere idempotente” è troppo assoluto

Non tutte le operazioni sono naturalmente idempotenti. Il requisito corretto è:

> Ogni operazione con side effect che può essere ritentata deve avere una strategia di deduplica/idempotenza o una procedura esplicita di reconciliation.

---

### P1-03 — “Adapter Pattern obbligatorio” è formulato male

I `Protocol` mostrati sono **ports**. Gli adapter sono le implementazioni concrete. La dipendenza da astrazioni è corretta, ma non ogni funzione locale necessita di un adapter.

---

### P1-04 — God Master Agent

AGT-00 analizza, classifica, instrada, coordina, integra, risolve conflitti, applica governance e comunica. È un single point of failure e una versione cognitiva del God Orchestrator vietato dal documento stesso.

**Fix:** separare `RequestClassifier`, `PlanCoordinator`, `PolicyDecisionPoint` e `FinalAssembler`. AGT-00 deve coordinare, non svolgere ogni responsabilità.

---

### P1-05 — Controlli deterministici trattati come agenti LLM

Principle Guard, Anti-Pattern Detector, Security Inspector e parte del Resilience Auditor dovrebbero essere principalmente:

- regole AST;
- linter;
- type checker;
- test;
- policy-as-code;
- Semgrep/Bandit/custom checks.

Un secondo LLM non rende automaticamente la verifica indipendente.

---

### P1-06 — Nessuna policy di eccezione o waiver

“Ogni rosso blocca sempre” sembra sicuro, ma un detector probabilistico può produrre falsi positivi. Manca un processo di:

- evidenza;
- suppressione motivata;
- scadenza del waiver;
- owner;
- audit;
- rivalutazione.

---

### P1-07 — Contratti di handoff non sufficienti

Il JSON inter-agent manca di:

- `schema_version`;
- `task_id`;
- `parent_task_id`;
- `correlation_id`;
- `deadline`;
- `artifact_refs`;
- `evidence`;
- `confidence`;
- `status`;
- `retryability`;
- `policy_version`;
- firma/provenance.

---

### P1-08 — Nessun budget o stop condition per agenti

Mancano limite token/costo, tempo massimo, numero di retry, max handoff depth, cycle detection e comportamento su partial result.

---

### P1-09 — Prompt injection e codice non fidato non modellati

Il sistema analizza input e codice utente, ma non stabilisce che tali contenuti siano dati non fidati. Mancano sandbox, network policy, filesystem policy, allowlist strumenti e separazione tra istruzioni e artifact.

---

### P1-10 — Observability incompleta

`configure_observability(service_name, ...)` non usa `service_name` nella `Resource`. OpenTelemetry indica `service.name` come attributo richiesto/raccomandato per identificare correttamente il servizio [4](https://opentelemetry.io/docs/languages/python/exporters/).

Mancano inoltre:

- MeterProvider/metric exporter;
- log redaction;
- baggage policy;
- propagazione HTTP esplicita;
- instrumentation di `httpx` se usato;
- shutdown/flush del provider;
- sampling policy;
- cardinality guard per metriche.

---

### P1-11 — Correlation ID non è propagazione distribuita completa

Passare un dataclass ai metodi locali non inserisce automaticamente `traceparent`, baggage o correlation ID nelle chiamate HTTP/eventi. Gli adapter devono propagare gli header consentiti e non fidarsi ciecamente degli ID forniti dall'esterno.

---

### P1-12 — Dati sensibili nei log

Sono loggati `cached_result`, error string e validation errors. Questi campi possono contenere PII o secrets.

**Fix:** allowlist dei campi, redaction processor e classificazione dati.

---

### P1-13 — Contratto pagamento internamente incoerente

`amount: Decimal` è descritto come “importo in centesimi”. Se l'unità è il centesimo deve essere `int`; se si usa `Decimal`, il campo rappresenta l'unità monetaria e richiede precisione/quantizzazione.

`success: bool` con molti campi opzionali permette stati impossibili. Meglio una discriminated union `Authorized | Declined | Pending`.

---

### P1-14 — Alert threshold universali

`error rate > 5%`, `p99 > 5000 ms`, `DLQ > 0` non sono soglie universali. Vanno derivate da SLO, volume, criticità e finestra temporale. Una singola DLQ in un flusso best-effort non equivale sempre a incidente.

---

### P1-15 — Struttura progetto rigida e sovradimensionata

La struttura obbliga ogni progetto ad avere Saga, DLQ, security, feature flags e numerosi moduli anche se non necessari. Manca invece:

- runtime entry point;
- dependency injection/composition root;
- repository implementations;
- migrations;
- API/transport;
- inbox/outbox;
- worker scheduler;
- artifact schemas;
- policy engine.

---

### P1-16 — Stack incoerente con il codice

- `tenacity` è dipendenza ma viene scritto un retry engine custom;
- `circuitbreaker` è dichiarato nello stack, ma non nel `pyproject`;
- Temporal/Prefect sono suggeriti, ma il runtime selezionato è `asyncio` puro;
- sono incluse sia `aiohttp` sia `httpx` senza motivazione;
- Kafka, Vault e Redis sono dipendenze core anche per progetti che non li usano;
- Pact, PyJWT e strumenti citati non sono allineati alle dipendenze.

---

### P1-17 — `aioredis` è obsoleto

Redis documenta che `aioredis` è stato fuso in `redis-py`; l'API asincrona moderna è `redis.asyncio` [5](https://redis.io/faq/doc/26366kjrif/what-is-the-difference-between-aioredis-v2-0-and-redis-py-asyncio).

**Fix:** sostituire `aioredis>=2.0.1` con una versione corrente di `redis` e usare `import redis.asyncio as redis`.

---

### P1-18 — `WorkflowState` non descrive lo stato operativo reale

Un solo `completed_steps: List[str]` non basta. Ogni step deve avere almeno:

```text
status, attempt, idempotency_key, started_at, deadline,
worker_lease, result_ref, error_code, retry_at, compensation_status
```

---

## 5. Findings di qualità e manutenibilità — P2

Questi punti non bloccano da soli una proof of concept, ma vanno risolti prima di stabilizzare il prodotto.

### P2-01 — Terminologia non normalizzata

“Agent”, “service”, “module”, “component”, “layer” e “orchestrator” vengono talvolta usati come sinonimi. Serve un glossario normativo con un significato unico per ogni termine.

### P2-02 — Configurazioni non validate

Le dataclass di configurazione accettano valori impossibili, per esempio timeout non positivi, threshold minori di uno e `half_open_max_calls=0`.

**Fix:** configurazioni frozen/slots con validazione al bootstrap e failure immediata.

### P2-03 — Clock non iniettato

Circuit breaker, retry, lease e test dipendono dal tempo. L'accesso diretto al clock rende i test lenti o flaky.

**Fix:** introdurre un `Clock` port con tempo monotono per durate e UTC per timestamp persistiti.

### P2-04 — Tassonomia errori non standardizzata

Gli errori sono spesso rappresentati come stringhe. Manca un contratto condiviso con `error_code`, categoria, retryability, safe message, cause chain ed eventuale remediation.

### P2-05 — Logging strutturato solo dichiarato

`structlog` è elencato, ma gli esempi non mostrano configurazione, processor di redaction, binding del contesto o schema dei log.

### P2-06 — Feature flag senza lifecycle

I feature flag sono presenti nella struttura ma non hanno owner, scadenza, default sicuro, audit o strategia di rimozione. Possono diventare stato permanente e moltiplicare i path da testare.

### P2-07 — Versionamento dei contratti incompleto

Mancano regole per compatibilità backward/forward, deprecazione, migrazione dello stato e coesistenza di più versioni di workflow durante un deploy.

### P2-08 — Eccezioni custom senza confine pubblico

Non è definito quali eccezioni possano attraversare ports/API e quali debbano essere tradotte in risultati di dominio o error envelope. Questo lega i consumer ai dettagli interni.

### P2-09 — Esempi non verificati come documentazione eseguibile

Gli snippet sono presentati come reference production-ready, ma non risultano estratti e testati automaticamente. Vanno inclusi come file importabili oppure verificati con doctest/literate testing.

### P2-10 — Ownership operativa assente

Mancano owner per workflow/policy/adapter, runbook link, escalation path, maintenance window e responsabile delle compensazioni manuali.

---

## 6. Audit puntuale dei componenti Python

### 5.1 `IdempotentStepExecutor`

**Da correggere:**

- claim atomico;
- key stabile tra tentativi;
- owner/lease;
- result codec;
- error state;
- no logging del payload;
- retention per dominio;
- propagazione downstream;
- reconciliation.

Interfaccia minima consigliata:

```python
class IdempotencyStore(Protocol):
    async def claim(
        self,
        key: str,
        *,
        owner_id: str,
        lease_seconds: int,
    ) -> ClaimResult: ...

    async def complete(
        self,
        key: str,
        *,
        owner_id: str,
        result_ref: str,
        expected_version: int,
    ) -> None: ...

    async def mark_unknown(
        self,
        key: str,
        *,
        owner_id: str,
        reason: str,
    ) -> None: ...
```

`attempt` appartiene allo stato e alla telemetria, non alla chiave.

---

### 5.2 `BaseOrchestrator`

**Da correggere:**

- `request_id` obbligatorio;
- load/create atomico;
- resume;
- deadline workflow;
- cancellation handling;
- stato degradato;
- optimistic locking;
- audit di start/failure/cancel;
- step result discriminato;
- nessun swallow generico;
- `get_running_loop().time()` o deadline monotona;
- authorization context e tenant.

`execute()` non deve creare sempre un workflow nuovo.

---

### 5.3 Circuit Breaker

**Da correggere:**

- una sola probe o limite reale in HALF_OPEN;
- nessun `await fallback()` sotto lock;
- monotonic time;
- metriche;
- failure classifier;
- reset manuale controllato;
- test di concorrenza;
- chiarire se lo stato è locale o condiviso.

Ordine consigliato per una chiamata esterna:

```text
bulkhead → deadline budget → retry loop → circuit breaker → singolo tentativo adapter
```

Il retry deve interrompersi su `CircuitOpen` e usare sempre la stessa chiave idempotente.

---

### 5.4 Retry Policy

**Da correggere:**

- `max_attempts >= 1` validato;
- eccezioni transient allowlisted;
- deadline end-to-end;
- supporto `Retry-After`;
- full/equal jitter scelto consapevolmente;
- predicate su response;
- no DLQ implicita per chiamate sincrone;
- no logging di dati sensibili.

---

### 5.5 Saga Coordinator

**Da correggere:**

- definizione serializzabile degli step, non closure effimere;
- persistenza prima/dopo ogni azione;
- result reference;
- status `EXECUTING/SUCCEEDED/FAILED/UNKNOWN`;
- reconciliation;
- compensazione idempotente;
- retry specifico delle compensazioni;
- stato `MANUAL_INTERVENTION`;
- lista di errori, non un solo `failed_step`;
- nessun `success=True` dopo failure non critiche: usare `DEGRADED`;
- timeout delle compensazioni separato;
- recovery dopo crash.

---

### 5.6 Workflow State

Modello minimo consigliato:

```python
@dataclass(frozen=True, slots=True)
class WorkflowState:
    workflow_id: str
    request_id: str
    tenant_id: str
    workflow_name: str
    workflow_version: str
    status: WorkflowStatus
    version: int
    deadline_at: datetime | None
    steps: tuple[StepState, ...]
    created_at: datetime
    updated_at: datetime
```

Il repository deve applicare compare-and-swap sulla `version`.

---

### 5.7 Observability

**Da correggere:**

- `Resource.create({SERVICE_NAME: service_name, ...})`;
- tracing + metrics + logs lifecycle;
- redaction;
- semantic conventions;
- propagation negli adapter;
- metriche con cardinalità bounded;
- span status e exception events;
- flush allo shutdown;
- dashboard per SLO, non soglie universali.

---

### 5.8 Security

Configurazione modello Pydantic raccomandata:

```python
from pydantic import BaseModel, ConfigDict

class StrictContract(BaseModel):
    model_config = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
        hide_input_in_errors=True,
    )
```

JWT minimo:

```python
payload = jwt.decode(
    token,
    signing_key,
    algorithms=["RS256"],
    issuer=settings.trusted_issuer,
    audience=settings.expected_audience,
    leeway=settings.clock_skew_seconds,
    options={
        "require": ["exp", "iat", "nbf", "iss", "aud", "sub", "jti"],
    },
)
```

Questo esempio non sostituisce JWKS rotation, revocation policy, mTLS e authorization contestuale.

---

### 5.9 DLQ

La DLQ va usata per task asincroni replayable, non come destinazione automatica di ogni eccezione.

Record minimo:

```text
message_id, schema_version, tenant_id, workflow_id, step_id,
artifact_ref, redaction_profile, error_code, attempt_count,
created_at, retention_class, replay_policy, integrity_hash
```

Il payload completo non va loggato né duplicato senza necessità.

---

## 7. Architettura corretta per runtime `asyncio` puro

“Asyncio puro” può essere il motore di concorrenza, ma la durabilità deve vivere fuori dal processo.

```text
┌─────────────────────────────────────────────────────────────────┐
│                    COMMAND / API INTAKE                         │
│ auth → validate → authorize → normalize → request dedupe        │
└──────────────────────────┬──────────────────────────────────────┘
                           │ DB transaction
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ POSTGRESQL: WORKFLOW STORE + INBOX + OUTBOX + EVENT LOG         │
│ workflow | step_state | idempotency | leases | commands | audit │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ ASYNCIO SCHEDULER / WORKER POOL                                 │
│ claim lease → execute due step → heartbeat → persist transition │
└───────────────┬──────────────────────────────┬──────────────────┘
                │                              │
                ▼                              ▼
      ┌──────────────────┐            ┌─────────────────────┐
      │ PORTS / ADAPTERS │            │ RECONCILIATION JOBS │
      │ timeout/retry/CB │            │ resolve UNKNOWN     │
      │ stable idem key  │            │ query remote status │
      └────────┬─────────┘            └─────────────────────┘
               │
               ▼
      External services / broker
```

### Garanzia realistica

Non promettere “exactly once”. L'obiettivo realistico è:

```text
at-least-once execution
+ stable idempotency keys
+ atomic local state transitions
+ downstream deduplication
+ reconciliation of ambiguous outcomes
```

### Componenti runtime minimi

1. `WorkflowDefinition` versionata;
2. `WorkflowInstance` durevole;
3. `StepDefinition` serializzabile;
4. `StepState` durevole;
5. `PostgresWorkflowRepository` con CAS;
6. `LeaseManager`;
7. `Scheduler`;
8. `StepExecutor`;
9. `OutboxPublisher`;
10. `InboxDeduplicator`;
11. `Reconciler`;
12. `CompensationExecutor`;
13. `PolicyEngine` per retry/fallback;
14. `Telemetry` e audit redatto.

---

## 8. Architettura corretta del builder multi-agente

Non tutti i controlli devono essere agenti LLM.

```text
                         ┌────────────────────┐
User request ───────────►│ Request Classifier │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Plan Coordinator   │
                         └──────┬───────┬─────┘
                                │       │
                    ┌───────────▼─┐   ┌─▼────────────┐
                    │ Generative  │   │ Generative   │
                    │ Architect   │   │ PythonBuilder│
                    └──────┬──────┘   └──────┬───────┘
                           └────────┬─────────┘
                                    ▼
                    ┌──────────────────────────────┐
                    │ Deterministic Verification   │
                    │ schema/AST/ruff/types/tests  │
                    │ security/policy/coverage     │
                    └──────────────┬───────────────┘
                                   │ findings + evidence
                                   ▼
                         ┌────────────────────┐
                         │ Semantic Reviewer  │
                         └─────────┬──────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Final Assembler    │
                         └────────────────────┘
```

### Ruoli da mantenere come agenti generativi

- Flow Architect;
- Python Builder;
- Test Scenario Designer;
- Documentation/ADR Writer;
- Semantic Architecture Reviewer.

### Ruoli da convertire soprattutto in policy/tool deterministici

- Principle Guard;
- Anti-Pattern Detector;
- Contract Validator;
- Type Safety Validator;
- Security Scanner;
- Dependency Auditor;
- Test Runner;
- Observability schema validator.

### Envelope inter-agent v2

```json
{
  "schema_version": "2.1",
  "task_id": "uuid",
  "parent_task_id": "uuid-or-null",
  "correlation_id": "uuid",
  "agent_id": "AGT-XX",
  "status": "SUCCEEDED|FAILED|PARTIAL|BLOCKED",
  "deadline": "RFC3339",
  "policy_version": "sha256:...",
  "artifact_refs": [],
  "findings": [],
  "violations": [],
  "evidence": [],
  "recommendations": [],
  "retryable": false,
  "confidence": "LOW|MEDIUM|HIGH"
}
```

L'envelope va validato con schema, non soltanto suggerito nel prompt.

---

## 9. Correzione dei principi fondamentali

### Principio 1 — versione corretta

> L'orchestrator contiene process policy, non calcoli o invarianti del dominio. Coordina step, dipendenze, branching, timeout, retry semantici e compensazioni; delega la business capability ai servizi competenti.

### Principio 2 — versione corretta

> I bounded context dipendono da contratti, non da implementazioni. La comunicazione diretta o event-driven è ammessa quando scelta esplicitamente dal pattern; nessun servizio deve dipendere dai dettagli interni di un altro.

### Principio 3 — versione corretta

> Ogni orchestrator governa un processo coeso e versionato. I processi cross-domain usano sub-workflow e contratti di handoff, non un God Orchestrator.

### Principio 4 — versione corretta

> Ogni side effect ritentabile deve possedere idempotenza end-to-end, deduplica atomica o reconciliation esplicita. La chiave resta stabile tra i tentativi.

### Principio 5 — versione corretta

> Ogni step dichiara input, output, side effect, failure modes, deadline, retryability, idempotency strategy, compensation/reconciliation e data classification.

### Nuovo Principio 6 — Durabilità

> Nessun workflow è dichiarato durevole se lo stato necessario al resume vive solo nel processo.

### Nuovo Principio 7 — Proporzionalità

> I pattern di resilienza si applicano in base a failure mode, semantica e SLO; non per rituale.

---

## 10. Dipendenze e struttura progetto

### Correzioni immediate al `pyproject.toml`

1. rimuovere `aioredis`; usare `redis` con `redis.asyncio` [5](https://redis.io/faq/doc/26366kjrif/what-is-the-difference-between-aioredis-v2-0-and-redis-py-asyncio);
2. aggiungere `PyJWT[crypto]` se il componente verifica JWT;
3. scegliere **uno** tra `httpx` e `aiohttp`, salvo esigenza documentata;
4. rendere Kafka, Vault, Redis e uvloop extra opzionali;
5. non mantenere contemporaneamente retry custom e Tenacity senza ownership chiara;
6. aggiungere migration tool per PostgreSQL;
7. aggiungere `hypothesis` per state machine/property tests;
8. allineare mypy/pyright, Pact e scanner alle tecnologie realmente usate;
9. usare lockfile e dependency scanning;
10. fissare un support window e aggiornare periodicamente i minimum versions.

### Struttura più corretta

```text
src/orchestration_layer/
├── control_plane/          # builder multi-agent, routing, policy
├── domain/                 # workflow/step state e invarianti runtime
├── application/            # use cases: start/resume/cancel/reconcile
├── ports/                  # repository, clock, broker, services
├── adapters/               # postgres, redis, http, broker, otel
├── runtime/                # scheduler, workers, leases, execution
├── resilience/             # policy e composizione, non business logic
├── security/               # authn/authz boundary e redaction
├── observability/
├── contracts/
└── config/

tests/
├── unit/
├── property/
├── contract/
├── integration/
├── recovery/
├── concurrency/
└── chaos/
```

---

## 11. Test mancanti e acceptance gate

### Correttezza/idempotenza

- 100 chiamate concorrenti con stessa request key producono un solo side effect remoto;
- retry dello stesso step usa la stessa idempotency key;
- request differenti non collidono;
- scadenza lease consente recovery senza esecuzione simultanea;
- crash dopo side effect e prima del commit entra in `UNKNOWN` e viene riconciliato.

### State machine

- tutte le transizioni valide;
- tutte le transizioni vietate;
- optimistic locking su update concorrenti;
- resume da ogni stato non terminale;
- cancellation e timeout persistiti;
- version migration di workflow in corso.

### Circuit breaker

- una sola probe HALF_OPEN;
- nessun fallback sotto lock;
- failure concorrenti;
- success reset;
- clock monotono;
- processo multiplo e metriche coerenti.

### Retry

- nessun retry su 4xx/auth/validation/domain rejection;
- retry su timeout/503 solo se safe;
- rispetto della deadline;
- rispetto di `Retry-After`;
- jitter statisticamente presente;
- circuit open interrompe i retry.

### Saga

- ordine inverso delle compensazioni;
- compensation failure → `MANUAL_INTERVENTION`;
- crash durante compensazione e resume;
- compensazione duplicata non produce doppio effetto;
- action timed-out ma remotamente completata → reconciliation;
- noncritical failure → `DEGRADED`, non `SUCCESS` puro.

### Sicurezza

- issuer errato;
- audience errata;
- algoritmo inatteso;
- token scaduto/non ancora valido;
- scope insufficiente;
- extra field Pydantic;
- payload molto grande;
- PII assente da log, trace, metriche e DLQ;
- prompt injection nel codice/documentazione analizzata;
- tool execution sandboxed.

### Multi-agent

- schema handoff invalido;
- agent timeout;
- agent partial result;
- conflitto tra reviewer;
- verifier deterministic fail;
- policy version mismatch;
- ciclo di handoff;
- budget esaurito;
- provenance di ogni artifact.

### Gate CI minimo

```text
ruff check
ruff format --check
pyright --verifytypes / mypy --strict
pytest unit + property
pytest concurrency
pytest integration
security scan
secret scan
dependency audit
coverage threshold per moduli critici
artifact schema validation
```

---

## 12. Roadmap di correzione

### Fase 0 — Separazione degli artefatti

Creare file distinti:

- `governance.md`;
- `runtime_architecture.md`;
- `agent_registry.yaml`;
- `policy_rules.yaml`;
- `handoff.schema.json`;
- package Python;
- eval suite.

### Fase 1 — Correctness core

1. request identity stabile;
2. state model immutabile e versionato;
3. repository PostgreSQL CAS;
4. atomic idempotency claim;
5. leases;
6. resume/recovery;
7. inbox/outbox;
8. reconciliation.

### Fase 2 — Resilienza proporzionata

1. taxonomy degli errori;
2. deadline end-to-end;
3. retry policy safe;
4. circuit breaker corretto;
5. bulkhead dove necessario;
6. Saga durevole;
7. DLQ/quarantine sicura.

### Fase 3 — Sicurezza e observability

1. Pydantic strict contracts;
2. JWT issuer/audience/JWKS;
3. authorization context;
4. redaction;
5. OpenTelemetry Resource, traces e metrics;
6. audit append-only.

### Fase 4 — Builder multi-agente

1. typed registry;
2. router;
3. generative worker interfaces;
4. deterministic verification pipeline;
5. artifact store;
6. policy decision point;
7. budget/timeout/cycle detection;
8. eval e provenance.

### Fase 5 — Dichiarazione di readiness

La dicitura “Production Ready” è ammessa solo dopo:

- test di recovery/crash;
- test di concorrenza;
- threat model;
- chaos test;
- SLO definiti;
- runbook di manual intervention;
- replay sicuro;
- audit della data retention;
- release candidate osservata in staging.

---

## 13. Decisione finale

### Componenti da conservare

- ports/protocols;
- separazione orchestrator/business capability;
- contratti tipizzati;
- correlation/tracing;
- stato persistito;
- compensazioni;
- review multi-prospettiva;
- test unit/contract/integration/chaos;
- ADR e documentazione.

### Componenti da riscrivere

- idempotency executor;
- workflow identity e resume;
- workflow state;
- circuit breaker;
- retry policy;
- Saga Coordinator;
- graceful degradation;
- JWT validator;
- Pydantic base contracts;
- DLQ;
- observability bootstrap;
- registry e protocollo multi-agente.

### Conclusione

Il documento v2.0 è un **blueprint concettuale promettente**, non un'implementazione. Il rischio maggiore non è la mancanza di pattern, ma il contrario: molti pattern sono dichiarati obbligatori senza una semantica distribuita corretta.

La priorità non deve essere aggiungere altri agenti o altro codice. Deve essere costruire il nucleo di correttezza:

> **identità stabile della richiesta → stato durevole → claim atomico → side effect idempotente → transizione versionata → recovery e reconciliation.**

Senza questa catena, retry, circuit breaker, Saga, DLQ e multi-agent governance aumentano la complessità senza fornire affidabilità reale.

---

## Fonti tecniche verificate

1. Python 3.11 — comportamento di `asyncio.wait_for()` e cancellation: [1](https://docs.python.org/3.11/library/asyncio-task.html)
2. Pydantic — `ConfigDict`, `extra="forbid"`, `hide_input_in_errors`: [2](https://docs.pydantic.dev/latest/api/config/)
3. PyJWT — validazione `issuer`, `audience` e required claims: [3](https://pyjwt.readthedocs.io/en/stable/api.html?highlight=decode)
4. OpenTelemetry Python — `Resource` e `service.name`: [4](https://opentelemetry.io/docs/languages/python/exporters/)
5. Redis — fusione di `aioredis` in `redis-py` e API `redis.asyncio`: [5](https://redis.io/faq/doc/26366kjrif/what-is-the-difference-between-aioredis-v2-0-and-redis-py-asyncio)
