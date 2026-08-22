# Orchestration Layer Architect v2.1 — Piano di produzione APEX-7 · Livello 5

**Data:** 12 agosto 2026  
**Ambito:** integrazione del prompt “APEX-7 Deep Refinement” nell'Orchestration Layer Architect  
**Runtime vincolante:** Python 3.11+ con `asyncio` puro; stato durevole esterno  
**Artefatto operativo associato:** [`SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md`](SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.1.md)  
**Audit di baseline:** [`AUDIT_Orchestration_Layer_Architect_v2.0.md`](AUDIT_Orchestration_Layer_Architect_v2.0.md)  
**Piano radice:** [`PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7.md`](PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7.md)  
**Piano genitore:** [`PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7_L4.md`](PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7_L4.md)  
**Livello:** **L5/7 — failure containment, safe degradation e recovery operativo**  
**Regola di versione:** questo file eredita integralmente L4 e introduce un solo miglioramento tematico addizionale.

---

## 0. Verdetto

APEX-7 contiene idee riutilizzabili, ma **non può essere incorporato letteralmente**. La versione fornita confonde design, runtime, governance, giudizio LLM e garanzie distribuite; inoltre assegna punteggi e percentuali di completamento senza evidenza eseguibile.

L'integrazione v2.1 conserva la disciplina centrale:

> **selezionare un componente, congelare la baseline, raffinarlo in profondità, provarlo localmente e contro regressione, promuoverlo solo con evidenza.**

Corregge però i punti pericolosi:

- un punteggio medio non compensa un fallimento critico;
- il Gate Agent non è l'unica autorità;
- la memoria non usa un lock globale da 100 ms come garanzia distribuita;
- il bus non promette genericamente exactly-once;
- le API RuFLO non verificate non entrano nell'architettura;
- il self-evolution non muta direttamente la produzione;
- `asyncio` resta il motore di concorrenza, PostgreSQL la fonte di verità durevole.

### Stato reale dopo questa integrazione

| Area | Stato |
|---|---|
| System prompt integrato | **DESIGN CANDIDATE** |
| Architettura target | **DEFINITA, NON IMPLEMENTATA** |
| Runtime durevole | **NON PROVATO** |
| Builder multi-agente | **NON PROVATO** |
| Quality gates eseguibili | **NON PROVATI** |
| Self-evolution controllato | **NON IMPLEMENTATO** |
| RuFLO adapter | **OPZIONALE, DA VALIDARE** |
| Production readiness | **BLOCKED** |
| Impegno su data/costo | **NON AUTORIZZATO: input critici mancanti** |
| Scope produttivo | **TPE-1 PROVVISORIO; volumi e owner non congelati** |
| Evidence execution | **NON INIZIATA: esistono specifiche, non run validi** |
| Failure containment | **DESIGN CANDIDATE; nessun drill eseguito** |

I valori “55%”, “8.5/10”, “8.7/10”, “9.0/10” e “9.2/10” del prompt APEX-7 sono **rimossi dal processo decisionale**. Non costituiscono metriche, test o prova di readiness.

### Registro del Livello 1 — unico miglioramento introdotto

**Tema:** rendere falsificabili effort, capacità, calendario e condizioni necessarie per impegnare una data.  
**Non modificato in L1:** architettura logica, contratti, gate, rollout e disposizione RuFLO del piano genitore.  
**Perché è il primo intervento:** un piano tecnicamente ricco ma sostenuto da una durata non difendibile è una promessa, non un piano.

#### 1. Baseline brutalmente sincera

Oggi esistono specifiche e audit, non un prodotto. Non esiste ancora evidenza nel workspace di:

- repository runtime compilabile;
- schema PostgreSQL migrato e testato;
- worker con lease/CAS e crash recovery;
- adapter di produzione qualificati;
- benchmark rappresentativo;
- staging, on-call o restore drill;
- team nominato e allocato;
- budget approvato;
- RuFLO clonato, pinato, ispezionato o sottoposto a POC.

Di conseguenza:

1. una data di produzione **non è impegnabile**;
2. la stima precedente di 20–24 settimane per il G7 completo è troppo ottimistica rispetto all'evidenza disponibile;
3. “molti agenti” non è un acceleratore dimostrato: aumenta coordinamento, costo, conflitti, superficie d'attacco e non-determinismo;
4. `gh repo clone ruvnet/ruflo` scarica sorgenti: non attiva né qualifica uno swarm e non prova compatibilità, sicurezza o durabilità;
5. il primo collo di bottiglia non è il numero di agenti, ma la catena state → claim → side effect → transition → recovery.

#### 2. Classificazione delle basi di stima

| Voce | Stato L1 | Conseguenza |
|---|---|---|
| 43 finding | **FATTO:** 43 `OPEN`, inclusi 15 P0 | nessuna readiness; effort minimo significativo |
| Runtime esistente | **NON PROVATO** | stima trattata come greenfield |
| Workload e side effect | **IGNOTI** | performance, idempotenza e rischio non calibrabili |
| Team e seniority | **IGNOTI** | capacità nominale non utilizzabile per commitment |
| Infrastruttura CI/CD, DB, broker, OTel | **IGNOTA** | make/buy e lead time non quantificabili |
| Vincoli compliance/data residency | **IGNOTI** | security lead time potenzialmente sottostimato |
| RuFLO | **OPZIONALE, NON QUALIFICATO** | zero credito di accelerazione nel forecast |
| F6 evolution | **FUORI CRITICAL PATH** | nessun credito per il go-live core |

Un ignoto critical non viene sostituito con un valore favorevole. Si usa un intervallo conservativo o si blocca il commitment.

#### 3. Calcolatore di realismo del forecast

Questo calcolatore stima calendario; **non** calcola production readiness e non può rendere verde un gate.

```text
C_eff = FTE_nominali × fattore_focus
T_capacity = effort_person_week / C_eff
T_forecast = max(T_capacity, critical_path_floor) + lead_time_esterno
```

Regole L1:

- `fattore_focus = 0,60–0,72`: il resto copre coordinamento, review, incidenti, ferie, hiring e supporto;
- effort core G1–G7, esclusa F6: **170 PW P50; 220 PW P80**;
- `critical_path_floor = 30 settimane`: alcuni test, soak, review e migrazioni non si comprimono aggiungendo persone;
- `lead_time_esterno = 4–8 settimane`, sovrapponibile solo in parte, per security, ambienti, procurement e approvazioni;
- se workload, team committed o piattaforma esistente restano ignoti, il forecast è una **range di pianificazione**, non una data.

| Scenario | Capacità effettiva usata | Forecast G7 | Giudizio L1 |
|---|---:|---:|---|
| 4–6 FTE nominali, media 5, focus 0,65 | 3,25 PW/settimana | **56–76 settimane** | realistico ma lento; alto rischio di dipendenze su singoli |
| 6–8 FTE nominali, media 7, focus 0,70 | 4,90 PW/settimana | **39–53 settimane** | scenario raccomandato minimo per full scope |
| 9–11 FTE esperti, piattaforma già matura | 7,2–8,0 PW/settimana | **34–38 settimane** | possibile solo dopo prova di baseline e forte leadership |
| 20–24 settimane | capacità e critical path incompatibili con gli ignoti attuali | **NON CREDIBILE per G7 completo** | ammissibile solo riducendo scope a foundation/durable-core RC, non produzione piena |

I valori non devono essere sommati meccanicamente alle durate di fase: rappresentano il forecast integrato con capacità, parallelismo limitato e attese esterne.

#### 4. Effort envelope per fase

| Fase | Effort P50–P80 | Calendario non comprimibile dominante |
|---|---:|---|
| F0 | 12–18 PW | ownership, threat model, workload e decisioni |
| F1 | 18–26 PW | bootstrap, contratti, CI, schema e migrazioni |
| F2 | 38–52 PW | correttezza concorrente, crash windows, restore |
| F3 | 34–48 PW | auth, eventing, data lifecycle, resilienza, telemetry |
| F4 | 28–40 PW | harness, registry, sandbox, gate ed eval deterministici |
| F5 | 22–30 PW | benchmark, chaos, staging soak e runbook drill |
| F7 | 18–26 PW | canary, approval, osservazione e rollback readiness |
| **Core totale** | **170–240 PW** | il planning calculator usa 170 P50 e 220 P80; 240 è coda di rischio |
| F6 opzionale | 16–28 PW separati | nessun credito sul critical path core |

#### 5. Regola anti-falsa-accelerazione dello swarm

Prima del G4, il forecast assegna a RuFLO e allo swarm **accelerazione = 0**. Dopo un POC, un beneficio può essere contabilizzato soltanto se:

- è misurato sul benchmark del progetto, non su demo;
- include costo di orchestrazione, review e rework;
- non aumenta false acceptance, incidenti di sandbox o provenance gap;
- mantiene Native Asyncio Harness come fallback;
- il limite di agenti cresce per esperimento: `2 → 4 → 8`; nessun salto a “tantissimi agenti” senza curve di throughput e qualità;
- il numero massimo deriva dal punto in cui il throughput marginale netto diventa nullo, non da una capacità dichiarata dal framework.

#### 6. Condizioni per rendere impegnabile il forecast

Il forecast può passare da range a commitment solo quando F0 produce:

- workload catalog con classi di rischio e volumi;
- inventory di repository, infrastruttura e servizi riusabili;
- team nominato con allocazione settimanale e skill coverage;
- make/buy decision per DB, broker, secrets, OTel e CI/CD;
- compliance/security lead time;
- dipendenze esterne con owner e date;
- stima bottom-up rivista per ogni epic;
- contingency esplicita e owner del rischio.

**Gate L1:** `PASS` documentale perché il piano espone calcolo, assunzioni e range; **BLOCKED per commitment** finché gli otto input sopra non esistono.

#### 7. Registro critico pubblico

| Affermazione | Obiezione più forte | Decisione L1 | Condizione che la smentisce |
|---|---|---|---|
| Più agenti accelerano | coordinamento e rework possono superare il lavoro utile | nessun credito prima di benchmark | speedup netto ripetibile con guardrail invariati |
| 20–24 settimane bastano | 15 P0 e durable recovery richiedono lavoro seriale e soak | rifiutata per G7 completo | baseline matura provata + scope ridotto o capacità eccezionale |
| RuFLO abilita la produzione | clone e swarm non sono runtime durevole né release control | adapter opzionale dopo G4 | POC dimostra contratti, isolamento, export e fallback |
| 4–6 persone sono sufficienti | forse sì, ma calendario e key-person risk crescono | 56–76 settimane come range prudente | team/prodotto esistente riducono effort misurato |

#### 8. Autocritica del Livello 1

- L'effort è ancora top-down: senza repo e workload può sbagliare anche del 30–50%.
- I fattori focus sono ipotesi, non timesheet del team reale.
- La stima non include un programma di certificazione regolatoria specifico.
- Il forecast non autorizza assunzioni, budget o release.
- Il Livello 1 migliora l'onestà del calendario, ma non riduce nessuno dei 43 finding.

**Backtrack L1:** se il repository o la piattaforma esistente mostrano evidenza sostanziale, ricalcolare effort; se emergono side effect regolati o safety-critical, ampliare la coda P80 e il lead time esterno.

### Registro del Livello 2 — unico miglioramento introdotto

**Tema:** sostituire la sequenza di macro-fasi con un grafo di dipendenze eseguibile, WIP limitato e critical path calcolato.  
**Non modificato in L2:** effort envelope L1, architettura target, contratti, gate, SLO, rollout e ruolo opzionale di RuFLO.  
**Perché serve:** L1 stimava capacità e incertezza, ma non dimostrava quali attività potessero davvero sovrapporsi. Senza dipendenze esplicite, il parallelismo viene quasi sempre sovrastimato.

#### 1. Autopsia critica del piano L1

L1 ha migliorato l'onestà della stima, ma conserva quattro debolezze:

1. il critical path `F0 → F1 → F2 → F3 → F4 → F5 → F7` è troppo grossolano;
2. F4 dichiara dipendenza da F1 e parzialmente da F2, mentre il diagramma lo colloca interamente dopo F3;
3. security, data lifecycle e sandbox sono prerequisiti trasversali, non un blocco da completare una sola volta;
4. la formula di capacità non include abbastanza costo di handoff, attese di evidence review e rework tra stream.

Conclusione: le range L1 restano utili come capacity envelope, ma sono insufficienti per il calendario. L2 le sostituisce con la previsione guidata dal grafo.

#### 2. Tipi di dipendenza vincolanti

| Tipo | Significato | Regola di avvio |
|---|---|---|
| `HARD` | contratto, schema o funzione necessaria | il predecessore deve avere exit criteria verdi |
| `EVIDENCE` | prova richiesta per non costruire su un'assunzione | evidence ref fresca e legata all'artifact hash |
| `AUTHORITY` | decisione o approvazione non delegabile | owner nominato e decision record firmato |
| `ENVIRONMENT` | ambiente, account, secret, DB, broker o capacità | smoke test dell'ambiente completato |

“Quasi finito”, branch locale, mock non rappresentativo o approvazione verbale non soddisfano una dipendenza. Un package può iniziare in discovery, ma non entrare in build/promozione senza i predecessori richiesti.

#### 3. Work-package DAG del core

Le durate sono intervalli calendario per lo scenario di riferimento **6–8 FTE nominali**, con lane riservate e WIP massimo. Non sono commitment.

| WP | Contenuto | Durata | Predecessori vincolanti | Exit evidence |
|---|---|---:|---|---|
| **W0** | workload, authority, threat model, ADR, RACI | 4–5 sett. | nessuno | catalogo workload, risk class, owner, decisioni firmate |
| **W1** | package, CI, strict contracts, schema/migration baseline | 4–6 sett. | W0 `HARD/AUTHORITY` | build riproducibile, schema compatibility, bootstrap fail-fast |
| **W2** | state machine, PostgreSQL repository, CAS e atomic claim | 6–8 sett. | W1 `HARD/ENVIRONMENT` | state/concurrency suite verde |
| **W3** | lease, idempotency, crash recovery, resume, reconciliation | 6–8 sett. | W2 `HARD/EVIDENCE` | crash-window, restore e unknown-outcome suite verdi |
| **W4** | authz, tenant/data controls, retention, secret/log policy | 5–7 sett. | W0 + W1 `HARD/AUTHORITY` | adversarial isolation e leakage suite verdi |
| **W5** | inbox/outbox, event compatibility, resilienza e OTel | 6–9 sett. | W2 + W4 `HARD` | replay, broker outage, redaction e trace propagation verdi |
| **W6** | agent/prompt registry, native harness, artifact/evidence store | 5–7 sett. | W1 `HARD` | envelope/schema/budget/provenance suite verde |
| **W7** | Gate Engine, semantic evaluator, sandbox e durable agent jobs | 6–8 sett. | W3 + W4 + W6 `HARD/EVIDENCE` | false-pass, injection, budget/cycle e recovery suite verdi |
| **W8** | hardening integrato runtime/control plane | 4–6 sett. | W5 + W7 `HARD` | end-to-end fault matrix senza blocker |
| **W9** | eval, capacity, chaos, seven-day soak e runbook drills | 7–10 sett. | W8 `HARD/ENVIRONMENT` | G5 evidence bundle e staging sign-off |
| **W10** | release candidate, restore/rollback e approval pack | 4–6 sett. | W9 `EVIDENCE/AUTHORITY` | signed manifest, rollback drill, on-call readiness |
| **W11** | canary progressivo, osservazione e closure | 4–6 sett. | W10 `HARD/AUTHORITY` | G7, post-deploy verification e closure firmata |
| **WX** | evolution/RuFLO POC | 4–7 sett. | W7; eval harness disponibile | decisione separata `ADOPT_SHADOW/DEFER/REJECT` |

`WX` è fuori dal critical path e non può sottrarre owner critici a W8–W11. Se usa le stesse persone senza capacità aggiuntiva, viene rinviato.

#### 4. Grafo e parallelismo ammesso

```text
W0 → W1 → W2 → W3 ───────────────┐
      │     │                     │
      │     └──────→ W5 ─────────┤
      ├──→ W4 ──────↑       ┌────┴→ W8 → W9 → W10 → W11
      └──→ W6 ─────────→ W7 ┘
                         └────→ WX   # opzionale, capacità separata
```

Interpretazione realistica:

- W4 e W6 possono sovrapporsi a W2/W3, ma competono per security, contracts e review;
- W5 non parte realmente prima che W2 stabilizzi transazioni e W4 definisca data/security policy;
- W7 non può dichiarare job “durevoli” prima delle prove W3;
- W8 è un merge gate tecnico, non una formalità amministrativa;
- W9 include tempo di osservazione: più agenti non comprimono un soak di sette giorni;
- W10/W11 dipendono da autorità e finestre operative esterne al team di sviluppo.

#### 5. Critical Path Method

Per il grafo L2, il percorso dominante è:

```text
W0 → W1 → W2 → W3 → W7 → W8 → W9 → W10 → W11
```

Calcolo sulla range dichiarata:

```text
lower = 4 + 4 + 6 + 6 + 6 + 4 + 7 + 4 + 4 = 45 settimane
upper = 5 + 6 + 8 + 8 + 8 + 6 + 10 + 6 + 6 = 63 settimane
```

W4 e W6 non risultano sul percorso aritmetico dominante soltanto se ricevono capacità dedicata. Se security o platform sono condivisi part-time, possono diventare il critical path reale.

#### 6. Correzione del forecast L1

Per scalare la capacità senza fingere che tutto sia parallelizzabile:

```text
T(C) = max(T_ref × (serial_fraction + parallel_fraction × C_ref / C), fast_track_floor)
serial_fraction = 0,30
parallel_fraction = 0,70
C_ref = 4,90 PW/settimana
fast_track_floor = 36 settimane
```

La frazione seriale include review, migration ordering, fault integration, soak, approval e canary. Il modello è diagnostico, non un commitment.

| Scenario | Forecast L1 | Forecast L2 | Verdetto critico |
|---|---:|---:|---|
| 4–6 FTE nominali | 56–76 sett. | **61–85 sett.** | L1 sottostimava queueing e handoff |
| 6–8 FTE nominali | 39–53 sett. | **45–63 sett.** | nuova baseline raccomandata |
| 9–11 FTE esperti + piattaforma matura | 34–38 sett. | **36–47 sett.** | rendimenti decrescenti e floor seriale |
| 20–24 settimane | non credibile | **rifiutato** | impossibile per full G7 senza eliminare scope o prove |

L2 è più lento di L1 perché espone lavoro che L1 aggregava: integration hardening, evidence queue, restore/rollback pack e canary closure.

#### 7. WIP e allocazione minima

Sono consentiti al massimo **tre stream maggiori** contemporanei e una sola promozione safety-critical per change set.

| Lane | Capacità minima nello scenario 6–8 FTE | Non può essere azzerata durante |
|---|---:|---|
| Runtime/Data | 2,0–2,5 FTE | W2–W5, W8 |
| Control Plane/Eval | 1,5–2,0 FTE | W6–W9 |
| Platform/SRE | 1,0–1,5 FTE | W1–W5, W8–W11 |
| Security/Data governance | 0,8–1,0 FTE | W0, W4, W7–W11 |
| QA/Eval | 0,8–1,0 FTE | da W2 a W11 |
| Product/Domain authority | 0,3–0,5 FTE | W0, W9–W11 |

Le allocazioni si sovrappongono per competenza, non si sommano come persone automaticamente disponibili. Se una persona copre due lane, il piano registra il conflitto e riduce il WIP.

#### 8. Regole anti-parallelismo fittizio

1. Nessun package apre più del 20% del lavoro downstream prima dell'exit evidence del predecessore.
2. Un blocker `HARD` congela build/promozione downstream; non viene nascosto come “rischio accettato”.
3. Rework superiore al 15% dell'effort settimanale per due settimane forza riduzione WIP.
4. Review queue p95 oltre tre giorni rende security/platform un collo di bottiglia esplicito.
5. Una modifica a state/event/security contract invalida le evidence downstream collegate all'hash precedente.
6. F6/RuFLO non usa capacità del critical path senza una decisione di replan approvata.
7. Non si aumenta il numero di agenti per compensare una dipendenza umana, ambientale o di autorità.

#### 9. Registro critico pubblico L2

| Affermazione ereditata | Obiezione più forte | Decisione L2 | Condizione di smentita |
|---|---|---|---|
| F3 precede interamente F4 | registry/harness possono iniziare dopo F1 | sostituita con DAG W4–W7 | dependency evidence mostra un vincolo più forte |
| 6–8 FTE: 39–53 settimane | capacity math non include abbastanza handoff/rework | corretta a 45–63 | dati di throughput reali riducono le durate WP |
| Più persone comprimono il piano | 30% del percorso è seriale o time-bound | rendimenti decrescenti espliciti | automazione provata riduce la frazione seriale |
| RuFLO può correre in parallelo | usa gli stessi owner di gate/security/eval | solo con capacità separata | staffing aggiuntivo nominato e POC isolato |

#### 10. Autocritica del Livello 2

- Le durate WP sono ancora stime top-down: il DAG è più onesto, non ancora calibrato da throughput reale.
- La frazione seriale 0,30 è un'ipotesi; può crescere con compliance o dipendenze aziendali.
- Il grafo non modella festività, hiring, procurement specifico o incidenti operativi.
- W4 security potrebbe diventare dominante; il CPM statico non cattura bene resource contention.
- L2 non chiude finding e non rende eseguibile il runtime.

**Gate L2:** struttura delle dipendenze e aritmetica CPM verificabili; **BLOCKED per commitment** finché F0 non conferma workload, persone, ambienti e owner.  
**Backtrack L2:** se una dependency review trova un predecessore mancante o una lane condivisa supera il 75% di allocazione, aggiornare DAG, CPM e forecast prima di iniziare il package interessato.

### Registro del Livello 3 — unico miglioramento introdotto

**Tema:** vincolare qualsiasi claim di readiness a uno scope hash esplicito e a un workload envelope verificato.  
**Non modificato in L3:** effort L1, DAG/CPM L2, architettura, contratti durevoli, gate, rollout e RuFLO opzionale.  
**Perché serve:** “piattaforma di orchestrazione production-ready” è una frase tecnicamente vuota se non specifica workflow, side effect, dati, tenant, regioni, volumi e SLO coperti.

#### 1. Autopsia critica del piano L2

L2 rende il calendario più credibile, ma la sua previsione di 45–63 settimane ha un denominatore implicito. Non distingue tra:

- un workflow controllato con un adapter reversibile;
- pagamenti o side effect irreversibili;
- uno o cento workflow dinamici;
- un tenant interno o una piattaforma multi-tenant pubblica;
- una regione o più residency boundary;
- dati interni o categorie regolamentate.

Senza scope contrattuale, qualsiasi successo limitato può essere venduto impropriamente come readiness generale. L3 proibisce questo salto logico.

#### 2. `ProductionScopeContract`

Ogni release candidate deve legarsi a un oggetto immutabile:

```text
ProductionScopeContract:
  scope_id, scope_version, scope_hash, owner
  workflow_definition_ids[] + hashes[]
  allowed_risk_classes[]
  tenant_ids[] | tenant_profile
  region_ids[]
  data_classes[]
  adapter_ids[] + versions[]
  allowed_tools[]
  max_steps_per_workflow
  max_payload_bytes
  max_concurrency
  arrival_rate_profile
  workflow_duration_profile
  side_effect_budget
  SLI/SLO profile hash
  exclusions[]
  evidence_bundle_hash
  approved_at, expires_at
```

Un campo non definito non significa “illimitato”: significa `NOT_PROVEN` e blocca il commitment.

#### 3. Classi di rischio operative

| Classe | Profilo | Esempi ammessi | Regola di rilascio |
|---|---|---|---|
| **C0 — no side effect** | calcolo, trasformazione o lettura controllata | validazione, enrichment non sensibile, report interno | test deterministici, isolation e audit |
| **C1 — reversibile/low impact** | effetto esterno idempotente o annullabile, blast radius limitato | ticket interno, notifica non sensibile, object write versionata | downstream key o read-back reconciliation; canary ristretto |
| **C2 — high impact compensabile** | effetto business rilevante con compensazione fallibile | provisioning, modifica account, operazione contrattuale | domain review, manual intervention, dedicated runbook, gate aggiuntivo |
| **C3 — irreversibile/regolato/safety-critical** | danno finanziario, legale, fisico o privacy elevato | pagamento, cancellazione irreversibile, decisione regolata | escluso da TPE-1; nuovo piano specialistico e authority dedicata |

La compensazione non rende automaticamente C2 equivalente a C1: una Saga può fallire anche nella compensazione.

#### 4. Primo Target Production Envelope — `TPE-1`

`TPE-1` è una proposta prudente da congelare in F0, non un claim già approvato.

| Dimensione | Envelope TPE-1 |
|---|---|
| Workflow | una definizione versionata e firmata; massimo 10 step |
| Rischio | C0 e al massimo un side effect C1 |
| Adapter esterni | uno, pinato e sottoposto a contract/failure test |
| Tenant | 1–3 tenant controllati; nessun onboarding self-service |
| Regione | una sola regione e un solo boundary di residenza |
| Dati | public/internal; niente special-category PII nei payload operativi |
| Codice/tool | niente codice arbitrario o tool grant dinamici nel runtime |
| Topologia | statica per versione; niente workflow inventato a runtime |
| Artifact | hash e firma; promozione umana obbligatoria |
| RuFLO | disabilitato nel runtime; eventuale builder sandbox solo dopo POC |
| Evolution | observe/propose soltanto; write path disabilitato |
| Volumi/SLO | `NOT_PROVEN` finché F0 non registra profilo numerico e benchmark |

La produzione iniziale non deve fingere generalità. Dimostra una slice stretta end-to-end: intake, deduplica, esecuzione, recovery, reconciliation, audit, rollback e closure.

#### 5. Scope esplicitamente escluso da TPE-1

- C2 e C3;
- pagamenti, trasferimenti di valore o decisioni regolamentate;
- side effect senza idempotency key né read-back/reconciliation affidabile;
- esecuzione di codice generato non revisionato;
- workflow o prompt forniti direttamente da tenant non fidati;
- multi-region active-active;
- cross-tenant memory o retrieval;
- onboarding pubblico/self-service;
- auto-promozione di prompt, policy, agenti o workflow;
- RuFLO come source of truth, release authority o runtime durevole;
- claim di capacità oltre il profilo di carico provato.

Un'esclusione non è debito nascosto: è un confine di sicurezza registrato nel manifest e applicato dall'admission control.

#### 6. Admission control vincolato allo scope

```text
request
→ authenticate / authorize
→ resolve ProductionScopeContract by hash
→ validate workflow + tenant + region + data + risk + adapter + budget
→ ACCEPT | REJECT_OUT_OF_SCOPE | DEFER_MANUAL_REVIEW
```

Regole:

1. nessun default permissivo;
2. `scope_hash` propagato in workflow, trace, audit, gate ed event envelope;
3. richieste C2/C3 non vengono degradate semanticamente a C1;
4. payload o concorrenza oltre envelope vengono rifiutati o ammessi da una policy di backpressure esplicita, mai accettati “best effort” in silenzio;
5. una definizione o un adapter non presenti nel contratto non possono essere caricati;
6. il Builder può proporre un nuovo scope, ma non approvarlo o attivarlo.

#### 7. Claim di readiness ammesso

La sola forma ammessa è:

```text
PRODUCTION READY FOR
scope_id=<id>
scope_hash=<sha256>
artifact_manifest_hash=<sha256>
evidence_bundle_hash=<sha256>
valid_until=<timestamp>
```

Sono vietati claim non circoscritti come “la piattaforma è production-ready”, “supporta qualsiasi workflow” o “lo swarm è pronto per la produzione”.

La scadenza del contratto o una modifica a workflow, adapter, rischio, regione, data class, SLO o policy invalida il claim finché i gate impattati non vengono rieseguiti.

#### 8. Matrice di riapertura dei gate

| Cambio di scope | Gate minimi da riaprire | Motivo |
|---|---|---|
| Nuova versione compatibile del workflow | G1, G2, G4, G5 | contratti, state path, artifact e regression |
| Nuovo adapter C1 | G2, G3, G5, G7 | idempotenza, failure modes, security e canary |
| Passaggio C1 → C2 | G1–G5, G7 | authority, compensation, operability e blast radius |
| Qualsiasi C3 | tutti + review specialistica esterna | il piano corrente non basta |
| Nuova data class sensibile | G1, G3, G5, G7 | threat, retention, redaction e incident response |
| Nuova regione/residency boundary | G1, G3, G5, G7 | storage, key, routing, restore e compliance |
| Aumento volume entro 2× | G5 e capacity sign-off | la correttezza non prova capacità |
| Aumento volume oltre 2× | G2, G3, G5, G7 | contention, queueing, lease, DB e rollout |
| Abilitazione RuFLO | G4, G5, G6; G7 solo se tocca release path | nuova superficie, costi, failure e supply chain |

#### 9. Calcolatore del delta di scope

Il forecast L2 **45–63 settimane** vale soltanto per TPE-1. Ogni espansione genera effort aggiuntivo prima di ricalcolare il DAG:

```text
E_scope = E_core
        + Σ E_adapter
        + E_risk_uplift
        + E_data_region
        + E_dynamic_surface
        + E_scale_requalification
```

| Delta | Effort diagnostico | Vincolo |
|---|---:|---|
| Adapter C1 addizionale | 8–16 PW ciascuno | contract, failure, security e operability test |
| Prima capability C2 | 20–35 PW | domain authority e compensation/manual path |
| Capability C3 | **NON STIMABILE ORA** | serve layer/review specialistica; nessun valore favorevole assunto |
| Nuova regione | 15–30 PW | residency, keys, routing, failover e restore |
| Workflow dinamici/user-authored | 25–45 PW | parser, policy, sandbox, compatibility e abuse controls |
| Profilo di carico >2× | 8–20 PW | benchmark, tuning, capacity e soak rieseguiti |

Gli effort non si sommano direttamente al calendario. Vengono inseriti come nuovi WP nel DAG L2; resource contention e predecessori determinano il nuovo critical path.

#### 10. Impatto sul forecast

| Claim | Forecast responsabile |
|---|---|
| TPE-1 con full OLA G1–G7 | **45–63 settimane**, ancora non impegnabili |
| Piattaforma generica multi-workflow/multi-adapter | **NON STIMABILE** senza scope contract |
| TPE-1 più una capability C2 | ricalcolo obbligatorio dopo domain review; L2 non è valido |
| Produzione C3 | fuori scope del piano corrente |

L3 non accorcia il piano. Riduce il rischio che 45–63 settimane vengano interpretate come costo di una piattaforma universale.

#### 11. Registro critico pubblico L3

| Affermazione ereditata | Obiezione più forte | Decisione L3 | Condizione di smentita |
|---|---|---|---|
| 45–63 settimane per “il sistema” | “il sistema” non ha workload denominator | range valida solo per TPE-1 | F0 prova un envelope diverso e il DAG viene ricalcolato |
| Una Saga rende sicuri gli effetti business | compensation può fallire o essere tardiva | C2 resta fuori da TPE-1 | domain evidence dimostra rischio C1 equivalente |
| Multi-tenant è già previsto dall'architettura | una colonna `tenant_id` non prova isolamento operativo | 1–3 tenant controllati | adversarial/capacity evidence abilita espansione |
| RuFLO/swarm aumenta lo scope supportato | builder throughput non prova runtime safety | nessun ampliamento di scope | gate e POC provano ogni nuova superficie |

#### 12. Autocritica del Livello 3

- TPE-1 è ancora una proposta: senza un caso d'uso reale potrebbe essere troppo stretto o già troppo rischioso.
- Il limite di dieci step e 1–3 tenant è prudenziale, non derivato da benchmark.
- “Public/internal data” richiede una tassonomia aziendale reale prima dell'uso.
- Gli effort di espansione sono top-down e possono variare oltre il 50%.
- L3 non sceglie il workflow business, non chiude finding e non produce implementation evidence.

**Gate L3:** il contratto e le regole di scope sono strutturalmente definiti; **TPE-1 resta `NOT_PROVEN`** finché F0 non inserisce workload, volumi, SLO, owner e data classification reali.  
**Backtrack L3:** qualsiasi richiesta fuori envelope riapre scope selection; C2/C3, nuova regione o dati sensibili obbligano a tornare a F0 e ricalcolare DAG, effort, gate e authority.

### Registro del Livello 4 — unico miglioramento introdotto

**Tema:** rendere ogni passaggio di gate e chiusura finding derivabile da evidence immutabile, riproducibile e legata alla release candidate.  
**Non modificato in L4:** forecast/effort L1, DAG L2, TPE-1 L3, architettura, rollout e ruolo opzionale di RuFLO.  
**Perché serve:** una lista di test è ancora una promessa. Senza requirement-to-evidence graph, freshness, environment equivalence e closure protocol, un report verde può riferirsi al codice sbagliato o a un ambiente irrilevante.

#### 1. Autopsia critica del piano L3

Il piano ereditato nomina test, gate ed evidence refs, ma non stabilisce ancora in modo sufficiente:

- quale test chiude quale finding;
- quale livello di ambiente è sufficiente;
- quando una prova scade o viene invalidata;
- come si trattano flaky test e rerun;
- chi può firmare una chiusura;
- come impedire che un report vecchio passi su un artifact nuovo;
- quale evidenza statistica sia realmente significativa.

Conclusione: i 43 finding hanno remediation assegnate ma **zero closure evidence eseguite**. L4 definisce il protocollo; non cambia il loro stato `OPEN`.

#### 2. Evidence graph normativo

```text
requirement/finding
→ risk statement
→ verification case versionato
→ test implementation hash
→ execution run
→ environment manifest
→ raw result/artifact refs
→ signed EvidenceRecord
→ FindingClosureRecord
→ GateRun
→ release manifest scoped TPE-1
```

Ogni arco è tipizzato. Se manca un nodo o un hash, la catena è `NOT_PROVEN`; non viene ricostruita retroattivamente con una spiegazione LLM.

#### 3. Contratti minimi di prova

```text
VerificationCase:
  case_id, version, owner
  finding_ids[], requirement_ids[], risk_class
  preconditions, input_generator, fault_schedule
  oracle_type, expected_invariants[]
  environment_level_required
  repetitions, seed_policy, timeout
  blocking, non_waivable

EvidenceRecord:
  evidence_id, case_id, case_version
  artifact_hashes[], test_implementation_hash
  command, tool_versions[], dependency_lock_hash
  environment_manifest_hash, scope_hash
  started_at, completed_at, seed_set
  status: PASS|FAIL|ERROR|FLAKY|NOT_PROVEN
  raw_result_refs[], redaction_policy_hash
  signer, signature, valid_until, invalidation_keys[]

FindingClosureRecord:
  finding_id, remediation_artifact_hashes[]
  required_evidence_ids[], independent_review_ref
  residual_risk, scope_hash
  status: OPEN|SPECIFIED|IMPLEMENTED|VERIFIED|CLOSED|REOPENED
  decided_at, decision_policy_hash, signer
```

`IMPLEMENTED` non significa `VERIFIED`; `VERIFIED` non significa automaticamente `CLOSED`; un waiver non equivale a closure.

#### 4. Livelli di evidenza

| Livello | Ambiente | Uso ammesso |
|---|---|---|
| **EL0 — assertion** | testo, diagramma o output non eseguito | nessuna chiusura; solo ipotesi |
| **EL1 — local** | esecuzione locale controllata | feedback rapido; non chiude P0/P1 |
| **EL2 — reproducible CI** | clean build con lockfile e artifact hash | può chiudere P2 e finding statici a basso rischio |
| **EL3 — integration** | PostgreSQL/broker/adapter non-prod rappresentativi | minimo P1 salvo rischio superiore |
| **EL4 — production-like fault environment** | failure injection, restore, security, capacity e config equivalenti | minimo per P0 prima del canary |
| **EL5 — scoped canary** | TPE-1 reale, traffico e blast radius limitati | conferma G7; non sostituisce EL2–EL4 |

Un test EL5 passato non sana un'assenza di unit, state-machine o recovery evidence. La piramide non è compensabile dall'alto.

#### 5. Protocollo di stato dei finding

```text
OPEN
→ SPECIFIED       # verification cases e oracle approvati
→ IMPLEMENTED     # remediation presente nell'artifact
→ VERIFIED        # evidence minima valida e indipendentemente revisionata
→ CLOSED          # closure policy soddisfatta per scope/hash
↘ REOPENED        # invalidation key, regressione, scope change o incident
```

Regole:

1. nessun salto di stato;
2. P0 richiede il livello definito nella closure matrix, approvatore indipendente e zero evidence `FLAKY/ERROR/NOT_PROVEN`; EL4 è obbligatorio per concurrency, durability, recovery, security, tenant isolation e release authority, mentre proprietà intrinsecamente statiche possono usare EL2/EL3 solo con policy esplicita e regressione integrata;
3. P1 richiede EL3, oppure EL4 se tocca security, durability, tenant isolation o rollback;
4. P2 richiede almeno EL2, salvo escalation di rischio;
5. il cambio di artifact, schema, dependency lock, environment class, scope o policy invalida le prove collegate secondo `invalidation_keys`;
6. un finding chiuso globalmente deve restare provato per ogni scope supportato; altrimenti la closure è scoped;
7. incidenti coerenti con il failure mode del finding lo portano automaticamente a `REOPENED`.

#### 6. Closure matrix iniziale dei 15 P0

Queste sono specifiche di test, non risultati.

| Finding | Verification case minimo | Oracle bloccante | Livello |
|---|---|---|---|
| **P0-01** | `V-P0-01-AGENT-BOUNDARY` | schema, budget, cycle, tool grant e provenance non bypassati | EL4 |
| **P0-02** | `V-P0-02-PROCESS-DEATH` | kill/restart riprende da stato PostgreSQL senza falso successo | EL4 |
| **P0-03** | `V-P0-03-IDEMPOTENCY-WINDOW` | same-key concurrency e crash dopo side effect non duplicano o producono `UNKNOWN` riconciliabile | EL4 |
| **P0-04** | `V-P0-04-LOAD-OR-CREATE` | request replay concorrente crea una sola workflow identity | EL4 |
| **P0-05** | `V-P0-05-STATE-CAS` | nessun lost update o transizione illegale sotto schedule concorrenti | EL4 |
| **P0-06** | `V-P0-06-SAGA-RECOVERY` | crash in action/compensation conserva ordine, stato e manual path | EL4 |
| **P0-07** | `V-P0-07-HALF-OPEN` | una sola probe autorizzata; fallback non blocca il lock | EL4 |
| **P0-08** | `V-P0-08-RETRY-TAXONOMY` | auth/validation/domain errors mai ritentati; transient entro budget/deadline | EL4 |
| **P0-09** | `V-P0-09-CRITICAL-RESULT` | failure critical non può essere serializzato o assemblato come success | EL3 |
| **P0-10** | `V-P0-10-CANCEL-DEADLINE` | cancel/timeout persiste stato e tratta side effect ambiguo come `UNKNOWN` | EL4 |
| **P0-11** | `V-P0-11-STRICT-CONTRACT` | fuzz/oversize/extra/coercion rifiutati fail-closed | EL3 |
| **P0-12** | `V-P0-12-JWT-AUTHZ` | alg/iss/aud/exp/nbf/JWKS/tenant variants non bypassano authz | EL4 |
| **P0-13** | `V-P0-13-DLQ-LEAKAGE` | secret/PII corpus assente da DLQ/log/event; replay autorizzato e auditato | EL4 |
| **P0-14** | `V-P0-14-CLEAN-BUILD` | clone pulito, lock verificato, import/type/test/build/SBOM riproducibili | EL2 |
| **P0-15** | `V-P0-15-AUTHORITY-SEPARATION` | domain/process/release authority non collassano nello stesso principal | EL4 |

La matrice non consente di chiudere P0-09/11/14 con il solo livello indicato se il loro impatto nel TPE-1 viene riclassificato come concurrency, durability, security o release-authority critical: in quel caso salgono a EL4.

#### 7. Oracle hierarchy

L'ordine di autorità è:

1. invarianti e state-transition oracle deterministici;
2. policy-as-code e schema validation;
3. proprietà/metamorphic test;
4. contract test e differential test;
5. metric window con soglia e intervallo;
6. semantic review LLM;
7. human judgment documentato.

LLM e human review sono necessari per coerenza, abuso e ambiguità, ma non sostituiscono un oracle deterministico disponibile.

#### 8. Calcolatore di forza dell'evidenza

Non si usa una media che possa compensare un rosso. Il profilo di release è una tupla:

```text
EvidenceProfile = (
  blocking_passed / blocking_total,
  minimum_required_level_met,
  stale_count,
  error_count,
  unresolved_flaky_count,
  missing_artifact_binding_count,
  independent_approval_complete
)
```

Decisione:

```text
PASS solo se blocking_passed = blocking_total
         e minimum_required_level_met = true
         e stale/error/flaky/missing_binding = 0
         e independent_approval_complete = true
altrimenti BLOCKED o ERROR
```

Un risultato 99/100 con il solo check mancante su tenant isolation è `BLOCKED`, non 99% ready.

#### 9. Realismo statistico — regola del tre

Con zero failure osservate in `n` prove indipendenti, il limite superiore approssimato al 95% del failure rate è:

```text
p_upper ≈ 3 / n
```

| Target statistico desiderato | Prove senza failure necessarie circa |
|---|---:|
| failure rate < 1% | 300 |
| failure rate < 0,1% | 3.000 |
| failure rate < 0,01% | 30.000 |
| failure rate < 0,0001% | 3.000.000 |

Conclusione brutale: cento esecuzioni verdi non dimostrano “zero duplicati” in produzione. Le proprietà critiche richiedono atomicità by design, model/state-machine test e fault injection; il campionamento misura il residuo, non crea la garanzia.

La formula vale soltanto con prove sufficientemente indipendenti e rappresentative. Schedule correlati, mock semplicistici o lo stesso seed ripetuto riducono drasticamente il valore effettivo di `n`.

#### 10. Flaky, rerun e tool error

- il primo fallimento resta nel lineage; un rerun verde non lo cancella;
- un test bloccante flaky produce `FLAKY` e blocca il gate;
- il rerun richiede motivo codificato: `INFRA_TRANSIENT`, `TEST_DEFECT`, `PRODUCT_DEFECT`, `UNKNOWN`;
- `PRODUCT_DEFECT` o `UNKNOWN` non possono essere convertiti in pass;
- quarantine test ammessa solo per non-blocking con owner e scadenza;
- tool crash, timeout o report illeggibile = `ERROR`, non failure né pass;
- tre run discordanti sullo stesso hash attivano root-cause review e congelano la promozione.

#### 11. Freshness e invalidazione

| Evidence | Validità massima iniziale | Invalidazione immediata |
|---|---|---|
| clean build/static/unit | finché artifact, lock, toolchain e policy hash non cambiano | cambio di uno degli hash |
| integration/contract | 14 giorni e stessa environment class | adapter/schema/config/dependency change |
| security/adversarial | 7 giorni sulla release candidate | auth/policy/tool grant/model/provider change |
| load/chaos/restore | 30 giorni se capacità e ambiente sono equivalenti | topology, DB/broker, volume envelope o runbook change |
| human approval | release-specific, massimo 7 giorni | artifact/evidence/scope change |
| canary | solo release e scope osservati | rollout config, artifact o scope change |

Le finestre sono default conservativi da approvare in F0. Una prova non “ringiovanisce” copiandola in un nuovo report.

#### 12. Independence e firma

| Azione | Può farla il builder? | Vincolo |
|---|---|---|
| scrivere test | sì | oracle e case versionati |
| eseguire CI | sì, tramite sistema | ambiente attestato |
| classificare un failure | sì, come proposta | audit e reviewer per critical |
| firmare closure P0 | no da solo | Runtime/Security/SRE owner indipendente secondo finding |
| emettere GateRun | policy engine | input firmati; nessuna discrezionalità nascosta |
| approvare release | no | separazione release authority |

Il Gate Evaluator LLM può produrre findings semantici; non firma da solo `FindingClosureRecord` P0 o manifest di release.

#### 13. Budget di verifica

Il forecast L2/L3 è valido soltanto se **25–35% dell'effort engineering** resta riservato a test, harness, fault injection, evidence pipeline, triage e rework. Se il piano di staffing tratta i test come fase finale, la stima 45–63 settimane è invalida.

```text
E_verification = E_test_design + E_harness + E_execution
               + E_triage + E_rework + E_evidence_operations
```

Questo budget non è overhead eliminabile: per F2/F3 può superare il 40%. Ridurlo non accelera la readiness; ritarda la scoperta dei difetti.

#### 14. Registro critico pubblico L4

| Affermazione ereditata | Obiezione più forte | Decisione L4 | Condizione di smentita |
|---|---|---|---|
| “test obbligatori” è sufficiente | non collega test, artifact, ambiente e finding | introdotto evidence graph | implementation produce una catena più forte e verificata |
| zero failure osservate prova affidabilità | con campioni piccoli il limite statistico resta alto | rule-of-three + oracle strutturali | modello probabilistico più adatto e validato |
| un rerun verde risolve il rosso | può occultare race o difetto intermittente | lineage immutabile e `FLAKY` bloccante | root cause dimostra test defect, con nuova versione |
| P0 può chiudersi quando il codice esiste | implementazione non è prova | livello closure-matrix, EL4 sui rischi critici e firma indipendente | risk review può alzare il livello; ogni livello inferiore richiede policy esplicita |

#### 15. Autocritica del Livello 4

- I verification case sono specifiche; nessun test è stato implementato o eseguito.
- I livelli EL e le freshness window sono baseline di governance, non standard universali.
- La rule-of-three non modella dipendenza tra run o eventi rari con distribuzione non stazionaria.
- EL4 richiede un ambiente realmente rappresentativo, oggi inesistente.
- Il budget 25–35% può essere insufficiente per concurrency, security e recovery greenfield.
- L4 non chiude finding e non cambia lo stato di readiness.

**Gate L4:** evidence model, P0 closure matrix e regole decisionali sono strutturalmente verificabili; **execution status = `NOT_STARTED`** e tutti i finding restano `OPEN`.  
**Backtrack L4:** un oracle ambiguo, un ambiente non equivalente, un flaky critical o un hash mismatch riporta il case a `SPECIFIED/IMPLEMENTED` e blocca gate e release.

### Registro del Livello 5 — unico miglioramento introdotto

**Tema:** trasformare il risk register in comportamento operativo deterministico quando processi, dipendenze, controlli o side effect falliscono.  
**Non modificato in L5:** effort L1, DAG L2, TPE-1 L3, evidence protocol L4, architettura logica e RuFLO opzionale.  
**Perché serve:** elencare un rischio non lo contiene. La produzione richiede una risposta definita per outage, esito ambiguo, compromissione, backlog, perdita di autorità e impossibilità di osservare.

#### 1. Autopsia critica del piano L4

Il piano ereditato include retry, circuit breaker, kill switch, rollback e runbook, ma conserva lacune operative:

- non assegna una modalità sicura a ogni dipendenza;
- non distingue fail-closed, fail-safe e degraded continuation;
- non quantifica il blast radius massimo ammesso;
- non specifica se i kill switch funzionano quando il control plane è guasto;
- non separa recovery tecnico da verifica d'integrità;
- non definisce quando fermare intake, claim, publish o side effect in modo indipendente;
- non dimostra che l'assenza di telemetry sia distinguibile dall'assenza di incidenti.

Conclusione: l'architettura può descrivere un happy path robusto e fallire comunque in modo pericoloso durante un outage combinato.

#### 2. `FailurePolicyContract`

Ogni `ProductionScopeContract` deve referenziare un contratto di failure immutabile:

```text
FailurePolicyContract:
  failure_policy_id, version, policy_hash, owner
  scope_hash, dependency_catalog_hash
  failure_modes[]
  admission_modes[]
  blast_radius_limits
  kill_switch_definitions[]
  recovery_objectives[]
  reconciliation_deadlines[]
  escalation_matrix_hash
  runbook_hashes[]
  drill_evidence_ids[]
  approved_at, expires_at
```

Se una dipendenza usata da TPE-1 non ha una failure policy, lo scope è `NOT_PROVEN`.

#### 3. Modalità operative

| Modalità | Intake | Nuovi claim | Side effect | Recovery/reconcile | Uso |
|---|---|---|---|---|---|
| **NORMAL** | ammesso entro envelope | ammessi | ammessi per scope | attivi | tutte le prove verdi |
| **DEGRADED_READ_ONLY** | solo query/status | no | no | attivi | dipendenza autorevole o KMS instabile |
| **DRAINING** | rifiuta nuovo lavoro | no nuovi claim | solo completamento sicuro già autorizzato | attivi | deploy, overload o manutenzione |
| **PAUSED** | rifiuta/deferisce | no | no | selettivi/manuali | integrità, auth o scope incerti |
| **EMERGENCY_CONTAINMENT** | chiuso | no | kill globale | solo incident command | leak, data loss, duplicate critical effect, authority compromise |

Il passaggio a una modalità meno restrittiva richiede recovery verification; il semplice ritorno della dipendenza non basta.

#### 4. Classi di dipendenza e fallback ammesso

| Classe | Dipendenze | Regola |
|---|---|---|
| **D0 — authoritative** | PostgreSQL, authz, scope/gate policy, KMS/secrets | nessun fail-open; fermare le operazioni che richiedono autorità o commit |
| **D1 — durable delivery** | broker, outbox publisher, object/evidence store | buffer durevole e backpressure; nessuna perdita silenziosa |
| **D2 — generation/coordination** | provider LLM, Native Agent Harness, RuFLO | builder degradato o manuale; runtime approvato continua indipendentemente |
| **D3 — observability/export** | OTel collector/exporter, dashboard | buffer sicuro limitato; se si perde visibilità safety-critical, ridurre o fermare lo scope |
| **D4 — external effect** | adapter TPE-1 | timeout ambiguo → `UNKNOWN` e reconciliation; niente retry cieco |

Un fallback è ammesso solo se preserva le invarianti. Redis, memoria locale, LLM o RuFLO non sostituiscono PostgreSQL, authz, KMS o Gate Policy Engine.

#### 5. Failure-mode catalog TPE-1

| Failure mode | Stato sicuro immediato | Azione vietata | Recovery evidence minima |
|---|---|---|---|
| Worker/process death | lease scade; altro worker riprende | marcare success da memoria locale | process-death EL4, no duplicate effect |
| PostgreSQL unavailable | `DEGRADED_READ_ONLY` o `PAUSED` | claim/transition locale non autorevole | failover/restore + consistency verification |
| PostgreSQL commit outcome ambiguous | stato `UNKNOWN_DB_COMMIT` | ripetere side effect | transaction/read-back reconciliation |
| Broker unavailable | outbox accumula entro budget | perdere/pushare fuori transazione | broker recovery, duplicate/reorder replay |
| Outbox backlog oltre limite | `DRAINING`; admission ridotta | crescita illimitata | drain test e lag entro SLO |
| Adapter timeout dopo invio | `UNKNOWN_EXTERNAL_EFFECT` | retry senza downstream read-back/key | reconciliation o manual intervention |
| Adapter auth failure | adapter circuit aperto; stop C1 | retry credenziali all'infinito | credential rotation + contract smoke |
| KMS/secret manager unavailable | fail-closed; no nuovo secret use | cache plaintext o log secret | recovery + key access audit |
| Authz/policy unavailable | `PAUSED` per operazioni mutate | usare ultimo allow non attestato | policy restore + authorization regression |
| Evidence store unavailable | runtime esistente continua; release freeze | promuovere senza evidence | integrity/read-back e manifest verification |
| Gate Policy Engine unavailable | release freeze | approvazione LLM/manuale sostitutiva informale | deterministic replay stesso input/hash |
| LLM provider unavailable | builder parziale/manuale | cambiare runtime artifact live | fallback/manual path con provenance |
| Memory poisoning sospetto | disabilita retrieval/write coinvolto | usare memoria per auth/gate | quarantine, tenant audit, clean rebuild |
| OTel exporter unavailable | secure bounded buffer; degrada admission | scartare telemetry critical senza allarme | export replay, loss accounting, redaction check |
| Clock skew oltre budget | stop lease claim/time-based approval | decidere expiry con clock non attendibile | NTP/clock health + monotonic invariant test |
| Disk/object quota esaurita | `DRAINING` | cancellare audit/evidence per liberare spazio | capacity restore + integrity scan |
| RuFLO hang/crash | kill adapter; Native Harness o builder pause | propagare failure al runtime | isolation/exit test; nessun authoritative state perso |
| Prompt/tool compromise | stop agent generation/tool profile | promuovere artifact prodotti durante finestra | scope audit, credential revoke, artifact re-eval |
| Tenant isolation sospetta | `EMERGENCY_CONTAINMENT` scope interessato o globale | continuare canary | forensic evidence, access regression, authority sign-off |

Le combinazioni contano: DB degradato + adapter ambiguo + telemetry assente è più pericoloso della somma di tre incidenti isolati e richiede containment globale.

#### 6. Blast-radius envelope

Non si usa un punteggio medio. Il blast radius è una tupla di massimi simultanei:

```text
BlastRadiusEnvelope = (
  tenants_exposed,
  workflows_in_flight,
  C1_effects_authorized,
  ambiguous_external_outcomes,
  data_classes_exposed,
  max_detection_time,
  max_containment_time
)
```

Per TPE-1:

- `C1_effects_per_workflow ≤ 1`;
- limiti tenant, inflight e concorrenza provengono dallo `scope_hash`;
- se anche un limite numerico non è definito, i side effect C1 restano disabilitati;
- `ambiguous_external_outcomes` ha hard cap e admission viene fermata prima di superarlo;
- canary percentage non sostituisce il cap assoluto;
- il limite globale deve considerare retry, outbox backlog e lease recovery, non soltanto richieste API.

#### 7. Calcolatore di esposizione operativa

```text
E_pending = workflows_in_flight × max_C1_effects_per_workflow
E_unknown = count(UNKNOWN_EXTERNAL_EFFECT entro reconciliation deadline)
E_backlog = outbox_unpublished + claimed_not_completed

ADMIT C1 solo se:
  E_pending < pending_cap
  AND E_unknown < unknown_cap
  AND E_backlog < backlog_cap
  AND telemetry_health = TRUSTED
  AND authority_health = TRUSTED
```

Il calcolo è un guardrail, non una misura monetaria del danno. Se `unknown_cap`, `pending_cap` o `backlog_cap` non sono approvati, la decisione è deny-by-default.

#### 8. Recovery objectives iniziali

Sono target provvisori da validare sul TPE-1, non SLO già raggiunti.

| Oggetto | RPO | Target recovery/containment | Nota |
|---|---:|---:|---|
| Workflow/step transition committata | 0 | worker recovery p95 ≤ 60 s | dipende da lease e failover provati |
| Idempotency/inbox/outbox record | 0 | nessuna perdita; backlog drain entro 15 min | sotto profilo di carico approvato |
| Audit/evidence usati per release | 0 | integrity verification ≤ 4 h | nessuna release durante outage |
| External C1 `UNKNOWN` | n/a | reconcile ≤ 15 min o manual queue | deadline domain-specific in F0 |
| PostgreSQL service | 0 sulle transizioni committate | failover/restore ≤ 30 min | obiettivo iniziale, da benchmark |
| Builder/LLM | artifact già firmati non impattati | manual/degraded path ≤ 4 h | nessun availability SLO per RuFLO |
| Telemetry critical path | accounting loss = 0 nel buffer budget | visibility restore ≤ 15 min | se buffer satura, admission ridotta |
| Kill switch | n/a | activation ≤ 60 s | canale out-of-band provato |

Se i target non sono economicamente o tecnicamente sostenibili, si riduce TPE-1; non si cambia il report a verde.

#### 9. Kill-switch architecture

| Switch | Effetto quando disattivato | Capability default | Autorità |
|---|---|---|---|
| `KS-INTAKE` | rifiuta nuovo lavoro | ON | Incident Commander/SRE |
| `KS-CLAIM` | ferma nuovi lease/claim | ON | Runtime Lead/SRE |
| `KS-SIDE-EFFECT-<adapter>` | blocca adapter C1 | OFF fino al canary autorizzato; ON solo per scope approvato | Incident Commander + Domain Owner |
| `KS-PUBLISH` | pausa outbox publisher | ON | SRE |
| `KS-AGENT-GEN` | ferma generazione agentica | OFF fino a G4 | AI Platform/Security |
| `KS-MEMORY-WRITE` | ferma write/retrieval selettivo | OFF fino a G4 | Security/Data |
| `KS-EVOLUTION` | ferma ogni evolution candidate | **OFF al primo go-live** | Change Authority |
| `KS-RUFLO` | disabilita adapter RuFLO | **OFF di default** | Platform/Security |

Nella colonna “Capability default”, `ON` significa capability abilitata e `OFF` significa deny-by-default. I comandi di spegnimento devono usare un canale out-of-band, least-privilege, auditato e indipendente dal componente da arrestare. Lo stato dei switch è parte del release manifest e della telemetry.

#### 10. Incident state machine

```text
DETECTED
→ CONTAINING
→ CONTAINED
→ DIAGNOSING
→ RECOVERING
→ VERIFYING
→ CLOSED
↘ ESCALATED / MANUAL_INTERVENTION
```

Condizioni:

- `DETECTED` senza owner entro la paging SLA scala automaticamente;
- recovery non riattiva intake/side effect;
- solo `VERIFYING` con evidence fresca può proporre ritorno a `NORMAL`;
- chi esegue recovery non approva da solo la riapertura su SEV critico;
- ogni incidente produce timeline, scope hash, artifact hash, affected identities e finding da riaprire;
- `CLOSED` richiede reconciliation di tutti gli `UNKNOWN` e accounting di event/data loss.

#### 11. Threat-to-containment matrix

| Threat | Containment immediato | Prova prima della riapertura |
|---|---|---|
| Prompt injection/tool escalation | `KS-AGENT-GEN`, revoke grants | adversarial eval + credential audit |
| Cross-tenant access | scope/global emergency containment | RLS/authz regression + forensic review |
| Memory poisoning | disable namespace/read/write | provenance rebuild + poisoned corpus test |
| Artifact/evidence tampering | release freeze, revoke manifest | signature/integrity reconstruction |
| Secret/PII exfiltration | stop exporter/adapter, revoke secret | leak scan, key rotation, access audit |
| Supply-chain compromise | freeze builds/releases | clean rebuild, SBOM/digest/provenance verify |
| Event replay storm | pause partition/publisher | inbox dedupe/replay test + backlog accounting |
| RuFLO/plugin compromise | `KS-RUFLO`, remove credentials/network | sandbox escape test + artifact revalidation |

Nessun sistema compromesso può auto-attestare da solo la propria pulizia.

#### 12. Drill matrix obbligatoria

| Drill | Frequenza iniziale | Pass bloccante |
|---|---|---|
| worker kill in ogni crash window | ogni release candidate | recovery/UNKNOWN senza falso success |
| PostgreSQL failover + restore | mensile e pre-G7 | RPO/RTO e integrity rispettati |
| broker outage + replay storm | ogni release candidate | no local event loss/double transition |
| ambiguous adapter outcome | ogni adapter/versione | cap, admission stop e reconciliation |
| KMS/authz outage | trimestrale e dopo policy change | fail-closed senza secret bypass |
| telemetry outage/buffer saturation | trimestrale | loss accounting e admission reduction |
| kill switch out-of-band | mensile e pre-canary | activation target e audit completi |
| tenant isolation incident | semestrale/tabletop + test tecnico | containment, forensic path e sign-off |
| Gate/Evidence outage | ogni release candidate | release freeze e deterministic replay |
| RuFLO failure/compromise | prima di ogni enable/update | runtime isolato, native fallback o safe pause |

Una tabletop senza esecuzione tecnica non prova RPO, idempotenza, kill switch o restore.

#### 13. Impatto sul forecast

La range TPE-1 di **45–63 settimane** resta valida solo se W8–W10 includono:

- ambiente EL4 fault-capable;
- kill-switch channel out-of-band;
- incident automation e runbook;
- almeno un ciclo di drill con remediation;
- capacità SRE/Security non condivisa oltre il limite L2.

Se ambiente EL4, failover, KMS/auth test o incident control devono essere costruiti da zero fuori dal lavoro già contato, aggiungere **6–12 settimane calendario** al DAG e ricalcolare il percorso. Nascondere questo lavoro in “operability” rende il forecast falso.

#### 14. Registro critico pubblico L5

| Affermazione ereditata | Obiezione più forte | Decisione L5 | Condizione di smentita |
|---|---|---|---|
| retry/recovery rendono resiliente | l'esito esterno può restare ambiguo | hard cap `UNKNOWN` + admission stop | adapter dimostra transazione/idempotenza più forte |
| telemetry outage è non critico | senza visibilità non si conosce il blast radius | buffer limitato e degradazione | canale alternativo prova osservabilità equivalente |
| kill switch documentato è sufficiente | può dipendere dal servizio guasto | canale out-of-band e drill | prova tecnica mostra controllo più affidabile |
| RuFLO failure usa il fallback | fallback non provato può condividere stato compromesso | kill, isolamento e revalidation | POC dimostra indipendenza completa |

#### 15. Autocritica del Livello 5

- Nessun recovery objective è stato misurato.
- I target 60 s/15 min/30 min possono essere troppo costosi o irrealistici sull'infrastruttura reale.
- I cap numerici del blast radius mancano perché TPE-1 non è congelato.
- Le failure combinate crescono combinatorialmente; la matrice non copre ogni interazione.
- Un canale out-of-band e un ambiente EL4 potrebbero richiedere procurement non conteggiato.
- L5 definisce containment, ma non esegue drill e non chiude finding.

**Gate L5:** failure policy, safe modes, kill switch e drill matrix sono definiti; **operational proof = `NOT_STARTED`**.  
**Backtrack L5:** target non sostenibile → ridurre TPE-1; drill fallito → tornare al WP proprietario; integrità/tenant/authority incerti → `EMERGENCY_CONTAINMENT`, mai ritorno automatico a `NORMAL`.

---

## 1. Integrazione dei sette componenti APEX-7

| Componente APEX-7 | Idea riusabile | Ridisegno obbligatorio | Elemento rifiutato |
|---|---|---|---|
| **1. Quality Gate System** | Gate espliciti, criteri, evidenza e remediation | Policy-as-code versionata; criteri blocking/non-blocking; `NOT_PROVEN`; waiver con owner/scadenza; artifact hash | Media ponderata che rende verde un rosso safety-critical; “dubbio=FAIL” senza distinguere prova mancante da fallimento |
| **2. Gate Agent** | Revisore dedicato e stato di valutazione | Split tra `GatePolicyEngine` deterministico e `GateEvaluatorAgent` semantico; remediation separata; timeout, budget, escalation | Autorità assoluta del solo LLM; auto-remediation con diritto di promozione; retry sullo stesso artefatto |
| **3. Memory Query Interface** | Query cross-agente, semantica, deduplica, pattern | PostgreSQL/MVCC; ACL tenant; provenance; retention/erasure; hybrid search; poisoning defense; vector index opzionale | Lock globale 100 ms come garanzia; “mai cancellare”; consistenza forte dichiarata senza protocollo |
| **4. Event Bus** | Envelope, catalogo eventi, correlation e retry | Outbox/inbox transazionali; at-least-once; consumer idempotenti; schema registry; ordering per aggregate; quarantine sicura | Exactly-once generico; payload sensibili duplicati; ordinamento globale implicito |
| **5. RuFLO Map** | Possibile meta-harness per coordinamento agenti | Adapter opzionale CLI/MCP, pin esatto, sandbox, contract test, fallback e exit strategy | `ruflo.AgentRuntime`, `WorkflowEngine`, `Router`, plugin Python e YAML APEX non verificati come API ufficiali |
| **6. Agent Prompt Templates** | Struttura identity/context/task/constraints/output/success | Prompt registry con hash/versione/owner; tool grants; input non fidato delimitato; schema output; budget; eval suite | Prompt come controllo sufficiente; output LLM trattato come trusted; un unico meta-agent onnipotente |
| **7. Self-Evolution Engine** | Osservare metriche, proporre cambiamenti, confrontare baseline | Observe → propose → offline eval → adversarial eval → shadow → approval → canary → monitor → rollback | Mutazione diretta della configurazione live; auto-approvazione; soglia “+5%” senza significatività/guardrail |

### Mappatura dei sette prompt-agente APEX

| Ruolo originale | Ruolo v2.1 | Correzione |
|---|---|---|
| Planner Agent | `PlanCoordinator` | pianifica e ordina; non approva policy o release |
| Writer Agent | `PythonBuilder` + `ADR/DocumentationWriter` | codice e documentazione hanno contratti, test e provenance distinti |
| Analyst Agent | `FlowArchitect` + `TestScenarioDesigner` | analisi architetturale separata dalla costruzione e dai test |
| Critic Agent | `SemanticReviewer` | critica semantica; non sovrascrive verifiche deterministiche |
| Refiner Agent | remediation worker versionato | modifica un componente per ciclo e produce un nuovo artifact hash |
| Gate Agent | `GateEvaluatorAgent` + `GatePolicyEngine` | giudizio LLM separato dall'autorità deterministica |
| Meta-Agent | `RequestClassifier` + `PlanCoordinator` + `PolicyDecisionPoint` + `FinalAssembler` | il God Agent viene eliminato e l'autorità distribuita |

### Decisione complessiva

- **Conservare:** disciplina di refinement, gate progressivi, registry agenti/prompt, event catalog, memoria interrogabile, esperimenti.
- **Riscrivere:** semantica dei gate, Gate Agent, consistenza della memoria, event delivery, evoluzione.
- **Isolare:** RuFLO dietro un port opzionale.
- **Rifiutare:** punteggi autoassegnati, garanzie impossibili, API inventate/non provate e modifiche autonome alla produzione.

---

## 2. Decisioni architetturali vincolanti

### AD-01 — Tre piani distinti

```text
Builder Control Plane
    usa NERVE-SOLVE per framing/design
    produce artefatti/policy/evidenza
                │
                ▼
        Release Control
                │
                ▼
Durable Workflow Runtime
    esegue solo versioni approvate
```

- **NERVE-SOLVE:** controllo cognitivo del problem solving.
- **Builder Control Plane:** genera e verifica.
- **Workflow Runtime:** esegue e recupera.

Nessun meta-agent possiede tutte e tre le autorità.

### AD-02 — `asyncio` puro, durabilità esterna

`asyncio` governa task, concorrenza e I/O nel worker. PostgreSQL governa identità, workflow, step, lease, idempotenza, inbox, outbox, audit e recovery. Redis può ottimizzare, ma non è la fonte autorevole.

### AD-03 — Garanzia realistica

```text
at-least-once execution/delivery
+ stable idempotency key
+ atomic local transition
+ downstream deduplication where available
+ reconciliation for ambiguous outcomes
```

### AD-04 — Gate deterministico sopra giudizio semantico

Il Gate Evaluator LLM produce findings; il Gate Policy Engine calcola l'esito su report firmati. Un reviewer semantico non può annullare un failure deterministico bloccante.

### AD-05 — Safety non compensabile

Perdita dati, side effect duplicati ad alto impatto, auth/tenant isolation, secret/PII leakage, recovery e rollback non possono essere mediati con criteri estetici o di costo.

### AD-06 — Memoria come dato non fidato

La similarità non prova verità. Ogni memoria ha fonte, tenant, trust, validità, retention e stato. I record possono essere quarantinati, superseded o cancellati.

### AD-07 — Eventi con outbox/inbox

Il commit dello stato e la registrazione outbox avvengono nella stessa transazione locale. I consumer deduplicano con `event_id` e/o versione aggregato.

### AD-08 — Evoluzione disaccoppiata dal go-live

Il primo rilascio può osservare e proporre, ma non deve auto-mutare. L'attivazione di canary evolutivi è una release successiva e separata.

### AD-09 — RuFLO non è nel critical path

Il sistema deve restare pienamente operativo con `NativeAsyncioAgentHarness`. RuFLO è un adapter sostituibile; nessun workflow durevole dipende dal suo stato interno.

### AD-10 — Un componente promosso per ciclo

Il lavoro può parallelizzare test e raccolta prove, ma un change set promuove un solo componente architetturale. Se il gate fallisce, si torna alla fase responsabile, non si accumulano ulteriori modifiche.

### AD-11 — Contratti e configurazioni versionati

Prompt, agent profile, workflow, evento, gate, policy, schema e migrazione hanno versione semantica, hash, owner e compatibilità dichiarata.

### AD-12 — Nessun completamento con check rosso

`FAIL`, `NOT_PROVEN` o `ERROR` su un criterio bloccante produce `BLOCKED`. Un break-glass operativo non viene rappresentato come `PASS`.

---

## 3. Architettura target

```text
┌───────────────────────────────────────────────────────────────────────┐
│ API / COMMAND INTAKE                                                  │
│ authenticate → authorize → validate → normalize → request dedupe      │
└───────────────────────────────┬───────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ BUILDER CONTROL PLANE                                                 │
│ triage → select component → plan → generate → deterministic verify    │
│ → semantic review → APEX gate → artifact manifest → release request   │
│                                                                       │
│ PromptRegistry | AgentRegistry | GatePolicy | EvidenceStore           │
│ EvolutionProposal | optional RufloMCPAdapter                          │
└───────────────────────────────┬───────────────────────────────────────┘
                                │ approved versioned artifacts
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ RELEASE CONTROL                                                       │
│ signatures | policy decision | migrations | rollout | rollback        │
└───────────────────────────────┬───────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│ DURABLE ASYNCIO WORKFLOW RUNTIME                                      │
│ scheduler | worker pool | lease heartbeat/reaper | step executor      │
│ idempotency | retry policy | circuit/bulkhead | Saga | reconciler     │
└──────────────┬─────────────────────────────┬──────────────────────────┘
               │                             │
               ▼                             ▼
┌──────────────────────────┐     ┌─────────────────────────────────────┐
│ PORTS / ADAPTERS         │     │ POSTGRESQL SOURCE OF TRUTH          │
│ HTTP, broker, object     │     │ workflow/step/lease/idempotency     │
│ store, secret manager    │     │ inbox/outbox/gate/evidence/audit    │
└──────────────────────────┘     └─────────────────────────────────────┘
```

### Struttura repository proposta

```text
src/orchestration_layer/
├── control_plane/
│   ├── intake/
│   ├── planning/
│   ├── agents/
│   ├── prompts/
│   ├── gates/
│   ├── artifacts/
│   └── evolution/
├── domain/
│   ├── workflow.py
│   ├── step.py
│   ├── events.py
│   ├── gate.py
│   └── errors.py
├── application/
│   ├── start_workflow.py
│   ├── claim_step.py
│   ├── complete_step.py
│   ├── reconcile.py
│   └── evaluate_gate.py
├── ports/
│   ├── workflow_repository.py
│   ├── artifact_store.py
│   ├── memory_store.py
│   ├── event_bus.py
│   ├── agent_harness.py
│   ├── clock.py
│   └── external_service.py
├── adapters/
│   ├── postgres/
│   ├── object_store/
│   ├── http/
│   ├── broker/
│   ├── llm/
│   └── ruflo_mcp/          # extra opzionale
├── runtime/
│   ├── scheduler.py
│   ├── worker.py
│   ├── leases.py
│   ├── executor.py
│   ├── outbox.py
│   └── reconciler.py
├── resilience/
├── security/
├── observability/
├── contracts/
└── config/

tests/
├── unit/
├── property/
├── state_machine/
├── concurrency/
├── recovery/
├── contract/
├── integration/
├── security/
├── agent_eval/
└── chaos/
```

---

## 4. Contratti minimi da implementare

### 4.1 Gate run

```text
gate_run_id, gate_id, gate_version, policy_hash,
artifact_hashes, evidence_bundle_hash, status,
criterion_results[], score_advisory, waiver_refs[],
started_at, completed_at, evaluator_provenance
```

Stati criterio: `PASS | FAIL | NOT_PROVEN | ERROR | WAIVED`.  
Stati gate: `PENDING | EVALUATING | PASS | BLOCKED | CONDITIONAL | ERROR`.

### 4.2 Workflow e step

```text
WorkflowInstance:
workflow_id, request_id, tenant_id, definition_name,
definition_version, status, version, deadline_at,
created_at, updated_at

StepState:
step_id, step_name, step_version, status, attempt,
idempotency_key, lease_owner, lease_expires_at,
started_at, deadline_at, retry_at, result_ref,
error_code, compensation_status, version
```

### 4.3 Idempotency record

```text
idempotency_key, tenant_id, operation_type,
status: CLAIMED|RUNNING|SUCCEEDED|FAILED|UNKNOWN,
owner_id, lease_expires_at, result_ref,
downstream_key, version, retention_until
```

La chiave non contiene il numero di tentativo.

### 4.4 Agent result

```text
schema_version, task_id, correlation_id, agent_profile_id,
prompt_hash, policy_hash, status, artifact_refs,
findings, evidence_refs, assumptions, risks,
retryable, confidence, usage, provenance
```

### 4.5 Evolution proposal

```text
proposal_id, component_id, baseline_hash, candidate_hash,
risk_class, hypothesis, changed_parameters,
offline_eval_ref, regression_eval_ref, shadow_eval_ref,
human_approval_ref, rollout_plan, rollback_plan,
status, owner, expires_at
```

---

## 5. RuFLO — fact-check e decisione

### 5.1 Evidenza ufficiale corrente

La documentazione ufficiale consultata descrive RuFLO come meta-harness centrato sul package npm, con superfici MCP, CLI, plugin e componenti WASM; il documento di status elenca esplicitamente tali superfici e comandi come `agent`, `swarm`, `memory`, `doctor` e `verify` ([STATUS ufficiale](https://github.com/ruvnet/ruflo/blob/main/docs/STATUS.md)).

La guida ufficiale del repository per agenti/Codex distingue coordinamento ed esecuzione: RuFLO registra e coordina, mentre l'host/agent esegue il lavoro; non è quindi sufficiente assumere che `agent spawn` equivalga a un worker Python durevole ([AGENTS.md ufficiale](https://github.com/ruvnet/ruflo/blob/main/AGENTS.md)).

Al 11 agosto 2026, la release list ufficiale indica `v3.36.0` come latest. La stessa release documenta correzioni recenti per write dichiarate riuscite ma non persistite e lost update concorrenti nella memoria ([releases ufficiali](https://github.com/ruvnet/ruflo/releases)). Questo non dimostra che RuFLO sia inutilizzabile; dimostra che l'integrazione va pinata, testata e tenuta fuori dal sistema autorevole.

Nelle fonti ufficiali consultate **non è stato trovato un contratto per le classi Python-like** `ruflo.AgentRuntime`, `WorkflowEngine`, `Router`, `MemoryPlugin`, `EventBusPlugin`, né per il file `apex7_workflow.ruflo.yaml` proposto. L'assenza dalla ricerca non prova inesistenza assoluta, ma rende queste superfici **non verificate e quindi non ammissibili** nel design di produzione.

### 5.2 Ruolo consentito

```text
AgentHarnessPort
├── NativeAsyncioAgentHarness     # riferimento e fallback
└── RufloMCPAdapter               # opzionale, sandboxed, non autorevole
```

Usi ammessi:

- coordinamento di worker generativi nel Builder Control Plane;
- discovery/routing sperimentale;
- memoria non autorevole per pattern;
- strumenti di sviluppo in sandbox.

Usi vietati:

- source of truth di workflow, gate, idempotenza o audit;
- autorità di deploy o modifica policy;
- gestione esclusiva di side effect di produzione;
- dipendenza necessaria al resume del runtime;
- installazione/upgrade con `@latest` nel critical path.

### 5.3 Proof of concept obbligatoria

| Test | Pass |
|---|---|
| Pin e riproducibilità | versione/tag/digest esatti; installazione ripetibile e SBOM generata |
| CLI/MCP contract | 100% dei comandi/tool usati rispettano schema e codici d'errore documentati |
| Failure isolation | kill/hang/malformed output non corrompono il control plane; timeout e fallback funzionano |
| Security | tool, filesystem, network e secret scope limitati; nessun accesso al DB autorevole |
| State export | artifact/result recuperabili fuori da RuFLO; nessun lock-in sul critical state |
| Load/cost | overhead entro budget approvato su benchmark rappresentativo |
| Upgrade | nuova versione testata in shadow; nessun auto-upgrade |
| Exit | disabilitazione dell'adapter non cambia la correttezza del runtime |

Se uno dei primi cinque criteri fallisce, l'esito è `DEFER/REJECT`, non “integra e correggi dopo”.

---

## 6. Piano di produzione

### Assunzione di pianificazione

La stima L2 resta valida in L3 **solo per il Target Production Envelope TPE-1**: **45–63 settimane con 6–8 FTE nominali**, **61–85 settimane con 4–6 FTE**, oppure **36–47 settimane con 9–11 FTE esperti e piattaforma matura**. Non è una stima per una piattaforma universale. Nessuna data è impegnabile prima della chiusura degli input F0, della firma del `ProductionScopeContract` e della conferma del work-package DAG. Tech lead/runtime, backend, platform/SRE, security, QA/eval e product/domain ownership devono essere coperti esplicitamente; una persona può coprire più ruoli, ma non crea capacità aggiuntiva.

### Critical path

```text
W0/F0 → W1/F1 → W2/F2 → W3/F2 ───────────────┐
          │          │                         │
          │          └→ W5/F3 ────────────────┤
          ├→ W4/F3 ─────↑              ┌──────┴→ W8 → W9/F5 → W10/F7 → W11/F7
          └→ W6/F4 ─────────────→ W7/F4┘
                                     └→ WX/F6  # opzionale, capacità separata

Critical path calcolato: W0→W1→W2→W3→W7→W8→W9→W10→W11.
F6 evolution/RuFLO non blocca il core e non riceve capacità dal critical path.
```

In caso di conflitto, il DAG W0–W11, i tipi di dipendenza e le exit evidence L2 prevalgono sulle righe riassuntive di dipendenza delle macro-fasi F0–F7.

### F0 — Freeze, separazione e threat model — effort L1: 12–18 PW

**Dipendenze:** nessuna.  
**Obiettivo:** trasformare i 43 finding in backlog verificabile e congelare le decisioni.

**Deliverable:**

- `governance.md`, `runtime_architecture.md`, `agent_registry.yaml`;
- `gate_policy.yaml`, `handoff.schema.json`, `event.schema.json`;
- glossario normativo;
- data classification e retention matrix;
- threat model: prompt injection, tenant leak, memory poisoning, side effect duplication, event replay, supply chain;
- ADR AD-01…AD-12;
- RACI e on-call ownership;
- benchmark workload e SLO target approvati;
- `ProductionScopeContract` TPE-1 con workflow, risk class, tenant, regioni, dati, adapter, volumi, SLO ed esclusioni;
- `FailurePolicyContract` con safe modes, blast caps, kill switch, recovery objective, escalation e runbook;
- backlog con ogni P0/P1/P2, owner e acceptance test.

**Gate/failure:**

- fail se un componente non ha owner;
- fail se Builder, NERVE-SOLVE e Runtime non sono separati;
- fail se un requisito critical non è tradotto in test/policy;
- fail se lo stato corrente conserva una dichiarazione “Production Ready” non qualificata o priva di evidenza; la dicitura resta ammessa solo come condizione futura nei go-live criteria.

**Human approval:** Tech Lead, Security, Data Owner e Product Owner.

### F1 — Package compilabile, contratti e CI — effort L1: 18–26 PW

**Dipendenze:** F0 completata e baseline Foundation approvata; il `PASS` finale di G1 arriva all'uscita di F1.  
**Obiettivo:** passare da snippet a progetto eseguibile.

**Deliverable:**

- package installabile con composition root;
- Pydantic strict contracts e config validate al bootstrap;
- error taxonomy e public error envelope;
- Clock port UTC/monotonic;
- schema/version registry;
- schema strict del `ProductionScopeContract` e policy di admission deny-by-default;
- migrazioni PostgreSQL iniziali;
- CI riproducibile con lockfile e SBOM;
- documentazione eseguibile/testata.

**CI minimo:**

```text
ruff check
ruff format --check
pyright --strict oppure mypy --strict
pytest unit + property
schema validation
secret scan
SAST/dependency audit
package import/build smoke test
```

**Gate/failure:** zero errori import/type; nessun extra field accettato nei contratti pubblici; configurazioni impossibili rifiutate al bootstrap.

### F2 — Durable correctness core — effort L1: 38–52 PW

**Dipendenze:** F1.  
**Obiettivo:** implementare la catena di correttezza prima dei pattern accessori.

**Deliverable:**

- request identity stabile e `load_or_create` atomico;
- workflow/step state immutabile e versionato;
- repository PostgreSQL con compare-and-swap;
- lease, heartbeat, reaper e fair claim;
- idempotency store con chiave stabile;
- resume/replay di step completati;
- stati `UNKNOWN`, `DEGRADED`, `PAUSED`, `CANCELLED`, `TIMED_OUT`, `MANUAL_INTERVENTION`;
- reconciler per esiti esterni ambigui;
- state transition event log;
- backup/restore iniziale.

**Gate/failure:**

- 100 richieste concorrenti con la stessa key producono un solo effetto osservabile nel downstream idempotente di test;
- nessun lost update con CAS;
- kill del worker in ogni crash window recupera o porta a `UNKNOWN`, mai a falso successo;
- resume da ogni stato non terminale;
- RPO zero per transizioni già committate;
- failure di restore, reconciliation o lease test blocca F3.

### F3 — Eventi, memoria, resilienza, sicurezza e observability — effort L1: 34–48 PW

**Dipendenze:** F2.  
**Obiettivo:** integrare gli altri componenti senza compromettere il durable core.

**Deliverable eventi:**

- transactional outbox/inbox;
- event schema registry e compatibilità;
- consumer idempotenti;
- ordering per aggregate/partition;
- backoff+jitter, quarantine e replay auditato.

**Deliverable memoria:**

- PostgreSQL/pgvector opzionale;
- ACL tenant/purpose, provenance e trust level;
- retention/erasure/legal hold;
- hybrid query, dedup, contradiction e poisoning checks.

**Deliverable resilienza:**

- error classifier transient/permanent/ambiguous;
- deadline end-to-end;
- retry allowlist e `Retry-After`;
- circuit breaker HALF_OPEN corretto;
- bulkhead solo dove giustificato;
- Saga serializzabile, persistita e recuperabile;
- DLQ separata dalla quarantine.

**Deliverable security/observability:**

- JWT issuer/audience/algoritmo/JWKS e authorization context;
- tool sandbox e input non fidato delimitato;
- log/trace/metric redaction;
- OTel `service.name`, propagation, bounded cardinality e flush;
- bounded secure telemetry buffer con loss accounting e admission degradation;
- failure-mode controller e kill-switch adapter out-of-band;
- audit append-only con integrità.

**Gate/failure:**

- zero cross-tenant read/write in suite avversariale;
- zero PII/secret nei sample di log, trace, metriche, memory ed eventi;
- duplicate event delivery non duplica la transition;
- crash tra DB commit e publish viene recuperato dall'outbox;
- nessun retry su auth, validation o domain rejection;
- una sola probe autorizzata in HALF_OPEN;
- compensation failure produce `MANUAL_INTERVENTION` e runbook link.

### F4 — Builder multi-agente e APEX gates — effort L1: 28–40 PW

**Dipendenze:** F1; artifact/evidence store; F2 per job durevoli.  
**Obiettivo:** rendere reali registry, routing, prompt e gate.

**Deliverable:**

- agent registry machine-readable;
- `AgentHarnessPort` e `NativeAsyncioAgentHarness`;
- task/result envelope validati;
- deadline, token/cost budget, max handoff depth e cycle detection;
- prompt registry con hash, owner, tool grants ed eval version;
- artifact/evidence store e evidence graph requirement→case→run→closure;
- `VerificationCase`, `EvidenceRecord` e `FindingClosureRecord` versionati;
- deterministic verifier pipeline;
- semantic reviewer separato;
- Gate Policy Engine e Gate Evaluator;
- waiver, expiration, audit e human escalation;
- Final Assembler senza autorità di sovrascrivere failure.

**Gate/failure:**

- output schema invalido viene rifiutato;
- prompt injection non ottiene tool grant o authority escalation;
- budget/cycle limit arresta il job con partial result sicuro;
- deterministic critical failure produce sempre `BLOCKED`;
- stesso artifact/evidence hash produce decisione riproducibile;
- tre remediation materiali fallite producono escalation, non loop infinito;
- ogni artifact ha provenance completa.

### F5 — Eval, performance, staging e operability — effort L1: 22–30 PW

**Dipendenze:** F3 e F4.  
**Obiettivo:** misurare qualità e operabilità su workload rappresentativo.

**Deliverable:**

- golden dataset e adversarial dataset versionati;
- baseline per qualità, latenza, costo e failure recovery;
- capacity test, soak test e chaos scenarios;
- dashboard SLO e alert per burn rate;
- runbook: stuck lease, outbox lag, unknown outcome, compensation failure, tenant incident, gate outage;
- drill matrix: worker/DB/broker/adapter/KMS/authz/telemetry/kill-switch/evidence failure;
- migration, backup/restore, containment e rollback drill;
- release candidate osservata in staging.

**Gate/failure:**

- nessuna regressione sui guardrail safety/security;
- intervalli di confidenza e sample size dichiarati per metriche LLM;
- p95/p99, costo e throughput entro budget approvato;
- nessun `UNKNOWN` oltre la reconciliation SLA del workflow;
- restore e rollback completati entro RTO approvato;
- soak di almeno sette giorni e sample minimo concordato, usando il requisito più severo.

### F6 — Controlled evolution e RuFLO spike — effort L1: 16–28 PW, fuori critical path

**Dipendenze:** F4; eval framework F5 disponibile.  
**Obiettivo:** implementare proposta/esperimento, non autonomia live.

**Deliverable evolution:**

- metric collector redatto;
- proposal generator;
- risk classifier;
- offline/regression/adversarial runner;
- shadow comparison;
- approval workflow;
- canary/rollback controller disabilitato per default;
- immutable experiment report.

**Deliverable RuFLO:**

- ADR e pin esatto;
- sandbox adapter;
- contract/failure/security/load/exit test;
- decisione `ADOPT IN SHADOW | DEFER | REJECT`.

**Gate/failure:**

- qualsiasi direct write a policy/config live blocca il gate;
- candidate con guardrail regression è rifiutato anche se migliora la media;
- nessuna approvazione può essere emessa dallo stesso processo che propone;
- failure RuFLO non impatta il native harness o il runtime.

### F7 — Production candidate, canary e go-live — effort L1: 18–26 PW

**Dipendenze:** G1–G5 passati; G6 solo in modalità proposal/shadow se presente.  
**Obiettivo:** rilascio limitato, osservato e reversibile.

**Deliverable:**

- release manifest firmato con `scope_id`, `scope_hash`, `failure_policy_hash`, stato kill switch ed evidence bundle;
- migration expand/migrate/contract backward-compatible;
- canary per workflow a basso impatto;
- kill switch separati per agent generation, external side effects, event publishing, evolution e RuFLO;
- on-call e escalation 24/7 secondo SLO;
- security sign-off e data retention sign-off;
- business owner approval;
- post-deploy verification e closure review.

**Gate/failure:** vedere sezioni 11 e 14. Nessun rollout prosegue automaticamente dopo un trigger rosso.

---

## 7. Maturity gate misurabili

### Formula comune

```text
PASS = tutti i blocking criteria PASS
       AND evidence graph completo, integro, fresco e legato agli artifact hash
       AND zero flaky/error/missing-binding bloccanti
       AND nessun rollback trigger aperto
       AND approvazioni indipendenti richieste presenti

CONDITIONAL = solo non-blocking criteria con waiver valido
BLOCKED = almeno un blocking FAIL/NOT_PROVEN/FLAKY,
          oppure criterion ERROR mentre il gate resta valutabile
ERROR = gate/evidence/tool/policy non valutabile complessivamente in modo integro
```

### Gate matrix

| Gate | Blocking evidence minima | Owner approvazione | Backtrack |
|---|---|---|---|
| **G1 Foundation** | threat model, glossary, ADR, ownership, schemas, SLO workload, 43 finding tracciati | Tech Lead + Security + Data | F0 |
| **G2 Durable Core** | concurrency, CAS, crash-window, resume, restore e reconciliation verdi | Runtime Lead + SRE | F1/F2 |
| **G3 Integration** | outbox/inbox, tenant isolation, redaction, auth, resilience e event compatibility verdi | Security + Data + Runtime | F2/F3 |
| **G4 Multi-Agent Builder** | registry/envelope/prompt hash, sandbox, budgets, deterministic blocking e provenance | AI/Eval Lead + Security | F1/F4 |
| **G5 Quality & Optimization** | golden/adversarial regression, latency/cost/capacity e soak entro target | Product + SRE + QA | F3/F4/F5 |
| **G6 Controlled Evolution** | no direct mutation, separation propose/approve, offline/shadow/rollback provati | Change Advisory + Security | F4/F6 |
| **G7 Production** | canary, backup/restore, rollback, on-call, audit, no blocker, signed manifest | Accountable Executive/Product + Tech + Security + SRE | fase responsabile o rollback |

### Waiver

Un waiver deve contenere `criterion_id`, rischio, compensating control, owner, approvatore indipendente, scadenza, scope e remediation ticket. Non è ammesso per perdita dati nota, tenant isolation, secret leak, rollback non provato, evidence integrity o side effect ad alto impatto non deduplicato/riconciliabile.

---

## 8. Test ed eval obbligatori

| Suite | Casi minimi | Fallimento bloccante |
|---|---|---|
| **Unit/property** | invarianti, config boundaries, serialization, error taxonomy | invariant breach |
| **State machine** | ogni transizione valida/vietata; status terminali/non terminali | transizione illegale accettata |
| **Concurrency** | same-key claims, CAS conflicts, lease expiry, HALF_OPEN permits | duplicate critical effect/lost update |
| **Recovery** | kill prima/dopo side effect/commit/publish/compensation | falso success o stato irrecuperabile |
| **Outbox/inbox** | duplicate, reorder, broker outage, poison event | doppia transizione o event loss locale |
| **Memory** | tenant ACL, deletion, stale source, poisoning, contradiction | cross-tenant leak o poisoned promotion |
| **Security** | JWT variants, injection, tool escalation, path/network escape, PII scan | auth bypass, exfiltration o unsandboxed execution |
| **Contract** | schema backward/forward, provider/adapter, event compatibility | breaking change non dichiarata |
| **Agent eval** | schema output, hallucinated evidence, partial, conflict, budget, cycle | invented pass/evidence o authority escalation |
| **Gate eval** | deterministic fail, tool error, stale evidence, waiver expiry | false PASS |
| **Evolution** | contamination, guardrail regression, approval separation, rollback | candidate auto-promoted o non rollbackabile |
| **Chaos/load** | DB failover, worker churn, broker outage, latency spikes, queue backlog | RTO/SLO breach senza containment |
| **RuFLO POC** | pin, malformed output, hang, crash, upgrade, export, disable | core dependency o state lock-in |

### Regola delle prove

- report senza artifact, scope, test implementation ed environment manifest hash = invalido;
- test non eseguito = `NOT_PROVEN`;
- tool crashato o evidence illeggibile = `ERROR`;
- test flaky bloccante = `FLAKY` e non può essere rilanciato fino al verde senza lineage, root-cause e owner;
- evidenza scaduta o invalidata va rigenerata sulla release candidate;
- un rerun non cancella il primo esito;
- lo stesso team può costruire e testare, ma l'approvazione dei gate critici richiede owner indipendente.

---

## 9. Metriche e SLO iniziali

Le soglie definitive vanno calibrate sul workload approvato in F0. Questi sono target iniziali per la release candidate, non leggi universali.

### Correctness

- `duplicate_critical_side_effects = 0` nella suite concorrente e nel canary;
- `committed_transition_data_loss = 0`;
- `illegal_state_transition = 0`;
- `cross_tenant_access = 0`;
- `false_gate_pass = 0` nel regression set critico;
- `unreconciled_UNKNOWN_older_than_domain_SLA = 0`.

### Recovery/operability

- workflow recovery p95 dopo worker kill ≤ 60 s nel benchmark iniziale;
- outbox publication lag p99 ≤ 5 s sotto carico approvato;
- lease double-ownership osservabile = 0;
- restore test rispetta RTO approvato e RPO 0 sulle transizioni committate;
- rollback applicativo completato entro il target approvato prima del canary.

### Agent/gate quality

- schema-valid agent result = 100%;
- provenance coverage degli artifact = 100%;
- critical evidence citation coverage = 100%;
- budget enforcement = 100%;
- prompt injection authority escalation = 0;
- decision reproducibility del Gate Policy Engine sullo stesso input = 100%.

### Performance/cost

- API acceptance p95 ≤ 500 ms, esclusa l'esecuzione asincrona;
- scheduler dispatch lag p95 ≤ 2 s sotto profilo di carico approvato;
- latency/cost per agent task con p50/p95/p99 e budget per classe;
- nessuna ottimizzazione promossa se migliora la media ma peggiora un guardrail o la coda oltre il budget.

### Business/fit

- tasso di workflow completati/degradati/manual intervention per tipo;
- tasso di rollback e remediation;
- gate false-block stimato su dataset etichettato;
- delta tra artifact consegnato e acceptance criteria;
- incidenti e toil operativo per 1.000 workflow.

---

## 10. Approvazioni umane e separazione dei compiti

| Decisione | Proponente | Verificatore | Approvatore |
|---|---|---|---|
| Nuovo workflow low-risk | Flow Architect | Test/Semantic Reviewer | Runtime/Product Owner |
| Side effect high-impact | Domain Owner | Security + Runtime | Accountable Business Owner |
| Schema/migrazione | Backend/Data | DBA/SRE + contract tests | Data Owner |
| Gate critical criterion | Quality/Security | Independent reviewer | Security + Tech Lead |
| Prompt/tool grant | AI/Eval | Security + adversarial eval | AI Platform Owner |
| Evolution candidate | Evolution service | Offline/shadow evaluator | Change Advisory Board |
| RuFLO update/enable | Platform | Security + POC suite | Tech Lead/SRE |
| Break-glass | Incident Commander | audit automatico | accountable on-call authority |

Nessun componente può proporre, verificare e approvare da solo la propria modifica critica.

---

## 11. Rollout, rollback e failure criteria

### Rollout

1. **Dev/local:** test deterministici e sandbox.
2. **Integration:** PostgreSQL/broker/adapters reali non produttivi.
3. **Shadow:** stessa richiesta, nessun side effect duplicato; confronto artifact/decisioni.
4. **Staging soak:** almeno sette giorni e sample minimo.
5. **Canary 1%:** solo workflow low-risk e reversibili.
6. **Canary 5% → 25% → 50%:** promozione manuale dopo finestra e sample minimi.
7. **100%:** solo dopo G7; evolution e RuFLO restano kill-switchable.

Per side effect che non possono essere shadowati, usare simulatori, record/replay redatto e canary su tenant/workflow esplicitamente autorizzati.

### Rollback design

- artifact, prompt, gate policy e workflow definition immutable/versioned;
- deployment può tornare alla versione precedente senza riscrivere history;
- migrazioni `expand → migrate → contract`; la fase contract avviene dopo la finestra di rollback;
- workflow in corso restano sulla versione originale o usano una migrazione esplicita testata;
- ogni canary ha `rollback_owner`, comando/runbook e deadline;
- rollback di policy/evolution non cancella audit ed evidence.

### Trigger di arresto immediato

- perdita/corruzione dati o side effect critico duplicato;
- auth bypass, cross-tenant access, secret/PII exfiltration;
- Gate Policy Engine produce un false PASS critico;
- workflow non recuperabile o restore fallito;
- backlog/outbox/lease fuori controllo con rischio di replay storm;
- evoluzione o RuFLO modifica una risorsa non autorizzata;
- impossibilità di attivare kill switch/rollback;
- migrazione incompatibile con la versione precedente;
- on-call o audit indisponibili durante il canary.

### Trigger di pausa e analisi

- SLO burn rate oltre budget;
- aumento di `UNKNOWN`, compensation failure o manual intervention;
- regressione quality/cost/latency oltre la soglia del gate;
- drift di schema/provider/model;
- aumento dei gate inconclusive o flaky tests.

---

## 12. Risk register

| Rischio | Severità | Controlli | Kill/rollback |
|---|---:|---|---|
| Duplicate side effect | Critica | stable key, atomic claim, downstream dedupe, reconciliation | disabilita adapter/step; stato `UNKNOWN`; manual review |
| Lost workflow state | Critica | PostgreSQL CAS, backup, recovery/restore tests | stop scheduler; restore/failover |
| False PASS del gate | Critica | deterministic engine, signed evidence, critical non-compensation | freeze promotion; revoke manifest |
| Prompt injection/tool escalation | Critica | untrusted delimiters, tool grants, sandbox, policy checks | disable agent/tool profile |
| Tenant leak/memory poisoning | Critica | ACL/RLS, provenance, quarantine, redaction | disable memory query/write; incident response |
| Event replay storm | Alta | inbox dedupe, per-key ordering, retry budget, quarantine | pause publisher/consumer partition |
| Saga compensation failure | Alta | durable compensation, idempotency, runbook | `MANUAL_INTERVENTION`; stop affected workflow type |
| Evolution drift | Critica | proposal-only, approval separation, canary/rollback | global evolution kill switch |
| RuFLO version/surface drift | Alta | exact pin, contract tests, native fallback | disable adapter |
| Observability exfiltration | Alta | allowlist/redaction/sampling/cardinality | stop exporter; local secure buffer |
| Cost/token runaway | Media/Alta | per-task budgets, cycle detection, concurrency limits | stop agent jobs; fallback deterministic/manual |
| Operational overload | Alta | SLO/burn alerts, capacity, backpressure, runbook | admission control; degrade noncritical flows |

---

## 13. Tracciabilità completa dei 43 finding

**Nota:** il design v2.1 assegna una remediation, ma i finding restano `OPEN` finché codice e prove non chiudono il gate.

### P0 — 15 bloccanti

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P0-01 Multi-agent non implementato | Registry, harness, envelope, budget, artifact/evidence pipeline | F4/G4 | OPEN |
| P0-02 asyncio non durevole | PostgreSQL source of truth, lease, resume, inbox/outbox | F2/G2 | OPEN |
| P0-03 idempotenza non atomica | stable key, unique claim/CAS, downstream key, `UNKNOWN` | F2/G2 | OPEN |
| P0-04 no resume/dedup workflow | request ID stabile e `load_or_create` atomico | F2/G2 | OPEN |
| P0-05 stato mutato/incompleto | frozen/versioned state, per-step state, CAS | F2/G2 | OPEN |
| P0-06 Saga non persistita | step serializzabili, durable action/compensation/recovery | F3/G3 | OPEN |
| P0-07 circuit HALF_OPEN errato | permit limitato, monotonic clock, fallback fuori lock | F3/G3 | OPEN |
| P0-08 retry indiscriminato | error taxonomy, transient allowlist, deadline e retry budget | F3/G3 | OPEN |
| P0-09 `critical=False` nasconde errori | discriminated result e `DEGRADED`; no generic swallow | F2–F3/G2–G3 | OPEN |
| P0-10 timeout/cancellation | monotonic deadline, persist cancel, `UNKNOWN` e reconciler | F2–F3/G2 | OPEN |
| P0-11 Pydantic non sicuro | strict/frozen/extra forbid/size limits/hidden input | F1/G1 | OPEN |
| P0-12 JWT incompleto | issuer/audience/alg pin/JWKS/claims/authz | F3/G3 | OPEN |
| P0-13 DLQ esfiltrabile | encrypted/redacted artifact ref, ACL, retention, replay audit | F3/G3 | OPEN |
| P0-14 progetto non compila | package reale, strict type/lint/import/test CI | F1/G1 | OPEN |
| P0-15 governance contraddittoria | separazione domain/process policy/orchestration/choreography | F0/G1 | OPEN |

### P1 — 18 importanti

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P1-01 resilienza obbligatoria ovunque | policy proporzionata a failure mode/SLO | F3/G3 | OPEN |
| P1-02 idempotenza assoluta | richiesta solo per side effect retryable o reconciliation | F2/G2 | OPEN |
| P1-03 adapter obbligatorio | port sui confini esterni, non astrazione rituale | F0–F1/G1 | OPEN |
| P1-04 God Master Agent | classifier/coordinator/PDP/assembler separati | F4/G4 | OPEN |
| P1-05 check deterministici come LLM | verifier tool/policy prima del semantic reviewer | F4/G4 | OPEN |
| P1-06 nessun waiver | waiver scoped, owner, expiry, audit; critical non-waivable | F4/G4 | OPEN |
| P1-07 handoff incompleto | task envelope v2.1 con versioni/budget/provenance | F1/F4/G4 | OPEN |
| P1-08 nessun budget/stop agenti | token/cost/time/handoff/cycle limits | F4/G4 | OPEN |
| P1-09 injection/codice non fidato | delimiters, sandbox, tool/network/filesystem policy | F3–F4/G3–G4 | OPEN |
| P1-10 observability incompleta | OTel resource/providers/propagation/redaction/flush | F3/G3 | OPEN |
| P1-11 correlation non propagata | adapter trace context e allowlisted baggage | F3/G3 | OPEN |
| P1-12 dati sensibili nei log | classification, allowlist e redaction processor | F3/G3 | OPEN |
| P1-13 contratto pagamento incoerente | unità esplicite e discriminated domain results | F1/G1 | OPEN |
| P1-14 alert universali | SLO/burn-rate e threshold per workflow/class | F0/F5/G5 | OPEN |
| P1-15 struttura rigida/oversized | moduli core + extras opzionali e composition root | F1/G1 | OPEN |
| P1-16 stack incoerente | dependency decision record, extras e lockfile | F1/G1 | OPEN |
| P1-17 `aioredis` obsoleto | `redis.asyncio` solo come adapter/cache opzionale | F1/F3 | OPEN |
| P1-18 stato operativo insufficiente | StepState completo con lease/result/error/compensation | F2/G2 | OPEN |

### P2 — 10 qualità/manutenibilità

| Finding | Remediation v2.1 | Fase/Gate | Stato |
|---|---|---|---|
| P2-01 terminologia | glossario normativo | F0/G1 | OPEN |
| P2-02 config non validate | frozen strict settings e bootstrap fail-fast | F1/G1 | OPEN |
| P2-03 clock non iniettato | Clock port monotonic + UTC | F1/F2 | OPEN |
| P2-04 error taxonomy | error code/category/retryability/safe message | F1/G1 | OPEN |
| P2-05 logging solo dichiarato | schema structlog/OTel, context binding e redaction | F3/G3 | OPEN |
| P2-06 feature flag lifecycle | owner, expiry, safe default, audit e removal ticket | F1/F7 | OPEN |
| P2-07 versionamento contratti | compatibility, deprecation, migrations e coexistence | F1–F3/G1–G3 | OPEN |
| P2-08 eccezioni custom | public error boundary e translation policy | F1/G1 | OPEN |
| P2-09 esempi non verificati | literate/import/doctest in CI | F1/G1 | OPEN |
| P2-10 ownership operativa | RACI, runbook, on-call e escalation | F0/F5/G1/G7 | OPEN |

---

## 14. Go-live criteria

Il sistema non può essere dichiarato genericamente `PRODUCTION READY`. È ammesso soltanto `PRODUCTION READY FOR <scope_id>@<scope_hash>` quando **tutte** le condizioni seguenti sono provate sulla release candidate e sul `ProductionScopeContract` attivo:

### Architettura e backlog

- `ProductionScopeContract` firmato, non scaduto e incluso nel manifest;
- evidence graph completo con zero blocking `FLAKY`, `ERROR`, stale o missing-binding;
- ogni P0 `CLOSED` cita il livello richiesto dalla closure matrix e firma indipendente; concurrency, durability, recovery, security, tenant isolation e release authority richiedono EL4;
- workflow, tenant, regioni, data class, adapter, tool, volumi e SLO coincidono con lo scope hash;
- admission control rifiuta o deferisce deterministicamente ogni richiesta fuori envelope;
- tutti i 15 P0 sono `CLOSED` con evidence refs;
- nessun P1 aperto impatta safety, security, durability, correctness o rollback;
- eventuali P1/P2 residui hanno owner, rischio accettato, scadenza e non violano un criterio non-waivable;
- Builder, NERVE-SOLVE e Runtime restano separati;
- RuFLO è disabilitato oppure ha POC/pass e non è nel critical path;
- evolution write path è disabilitato al primo go-live.

### Correttezza e sicurezza

- G1–G5 e G7 sono `PASS`; G6 è `PASS` solo per proposal/shadow oppure non attivato;
- zero false PASS critici nel regression set;
- zero duplicate critical side effect e zero cross-tenant leak nei test/canary;
- crash, resume, reconciliation, backup, restore e rollback drill passati;
- threat model e security review approvati;
- data classification, retention, deletion e audit provati.

### Operability

- SLO/SLI, capacity e error budget approvati;
- staging soak completato;
- dashboard e alert testati con synthetic incident;
- runbook esercitati, inclusa manual compensation;
- on-call, escalation e incident commander assegnati;
- `FailurePolicyContract` firmato e coerente con TPE-1;
- blast-radius cap numerici, `UNKNOWN` cap e admission thresholds configurati e provati;
- kill switch out-of-band, safe-mode transition e rollback provati, non soltanto documentati;
- incident drill chiuso con recovery verification indipendente;
- migrazioni backward-compatible durante la finestra di rollback.

### Release

- artifact/policy/prompt/workflow/event schema con hash e firma;
- SBOM, dependency/secret/security scans verdi;
- change approvals registrate;
- canary completato senza trigger rosso;
- post-deploy verification e closure firmate dagli owner.

Se una sola condizione bloccante è rossa, non provata o in errore, il verdetto resta:

> **BLOCKED — non production-ready per alcuno scope approvato.**

---

## 15. Immediate next actions — primi dieci ticket

1. **OLA-001:** approvare system prompt v2.1 e AD-01…AD-12.
2. **OLA-002:** creare repository/package reale e CI strict.
3. **OLA-003:** creare schema PostgreSQL per workflow/step/lease/idempotency.
4. **OLA-004:** implementare `load_or_create`, CAS e atomic claim.
5. **OLA-005:** costruire crash-window/concurrency test harness e i 15 `VerificationCase` P0 prima degli adapter reali.
6. **OLA-006:** implementare outbox/inbox e event envelope versionato.
7. **OLA-007:** implementare strict contracts, error taxonomy, auth context, redaction e `FailurePolicyContract`.
8. **OLA-008:** creare evidence graph, closure state machine e Gate Policy Engine con `NOT_PROVEN/FLAKY/ERROR`.
9. **OLA-009:** creare Agent/Prompt Registry, envelope e Native Asyncio Harness.
10. **OLA-010:** congelare `ProductionScopeContract` TPE-1 e implementare admission control deny-by-default; lo spike RuFLO resta WX dopo W7.

L'ordine non è cosmetico: OLA-003/004/005 e il contratto di scope precedono Saga, ottimizzazione, self-evolution, RuFLO e qualsiasi promessa di produzione.

---

## Fonti tecniche principali

- Python `asyncio` task, timeout e cancellation: https://docs.python.org/3.11/library/asyncio-task.html
- Pydantic strict configuration: https://docs.pydantic.dev/latest/api/config/
- Redis async client: https://redis.io/docs/latest/develop/clients/redis-py/async/
- OpenTelemetry Python exporters/resources: https://opentelemetry.io/docs/languages/python/exporters/
- PyJWT claim and issuer/audience validation: https://pyjwt.readthedocs.io/en/stable/api.html
- RuFLO repository: https://github.com/ruvnet/ruflo
- RuFLO official status: https://github.com/ruvnet/ruflo/blob/main/docs/STATUS.md
- RuFLO official agent guide: https://github.com/ruvnet/ruflo/blob/main/AGENTS.md
- RuFLO releases: https://github.com/ruvnet/ruflo/releases
