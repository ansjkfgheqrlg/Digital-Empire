# LIVELLO 5/7 — Quality engineering, evidenza e release validation

**Versione:** 5.0.0  
**Sostituisce:** `level-04-security-resilience-control.md`  
**Stato:** PROPOSTO — attende approvazione umana  
**Obiettivo:** sostituire fiducia e autovalutazioni con prove riproducibili prima di ogni rilascio.

---

## 1. Autocritica del Livello 4

| Limite L4 | Perché non basta | Correzione L5 |
|---|---|---|
| controlli numerosi ma non orchestrati | una checklist può essere ignorata o eseguita male | pipeline evidence-driven con gate automatici |
| prompt versionati ma non misurati | hash stabile non significa output migliore | eval set, baseline, regression e canary |
| memoria protetta ma non valutata | retrieval sicuro può essere irrilevante | precision/recall, citation accuracy e conflict tests |
| SLO candidati | non definiscono capacità massima | load profiles, saturation point e capacity envelope |
| security test generici | rischio di copertura cosmetica | abuse-case suite, DAST, fuzzing e penetration gate |
| approval R3 solo tecnica | operatori possono approvare per abitudine | preview, diff, reason, expiry e anti-fatigue UX |
| compliance solo citata | nessuna responsabilità o evidenza | control matrix GDPR/SOC2 e data lifecycle |
| token grant non scelto | due alternative mantengono ambiguità | token opaco single-use nel pilot |
| release freeze senza rollout | manca promozione controllata | ring DEV→TEST→SHADOW→CANARY→PILOT→PROD |
| RuFlo certification senza dossier standard | risultati difficili da confrontare | Evidence Pack firmato per commit/schema/runtime |
| benchmark A/B/C isolato | rischio tuning sul dataset | train/calibration/holdout e blind evaluation |
| NERVE-SAVE non-loss nominale | compressione può alterare istruzioni | semantic preservation e mandatory-span tests |

### Decisione L5

La qualità non sarà un voto unico. Verrà valutata tramite:

1. **hard gates:** sicurezza, isolamento, correttezza strutturale, idempotenza;
2. **metriche per dimensione:** qualità, costo, latenza, memoria;
3. **evidenze firmate:** test report, artifact hash, commit e ambiente;
4. **approvazione umana mirata:** solo dove il rischio non è automatizzabile.

---

## 2. Quality model

### 2.1 Dimensioni

| Dimensione | Domanda | Tipo |
|---|---|---|
| Safety | può causare azioni non autorizzate? | hard gate |
| Tenant isolation | può esporre dati tra tenant? | hard gate |
| Correctness | il risultato soddisfa contratto e test? | hard gate + metrica |
| Evidence | i claim sono supportati da fonti verificabili? | hard gate per claim obbligatori |
| Recoverability | crash e side effect incerti sono recuperati? | hard gate |
| Determinism | replay produce stesso stato decisionale? | hard gate control plane |
| Usefulness | l’output risolve il goal? | metrica/rubrica |
| Efficiency | costo, token e latenza sono proporzionati? | metrica + budget gate |
| Operability | il sistema è osservabile e gestibile? | hard gate release |
| Maintainability | cambiamento è isolato e testabile? | metrica/review |

### 2.2 Regola di aggregazione

Una media non può compensare un hard gate fallito. Il punteggio aggregato viene calcolato solo sulle varianti già idonee.

```text
eligible = all(hard_gates == PASS)
rankable = eligible AND sample_size >= minimum
promotable = rankable AND no_significant_regression AND error_budget_ok
```

---

## 3. Evidence Pack

Ogni build candidata produce:

```json
{
  "evidence_pack_version": "1.0",
  "release_id": "rel-uuid",
  "source_commit": "sha",
  "builder_identity": "workload-id",
  "environment": "test|shadow|canary",
  "images": [{"digest": "sha256:...", "sbom": "artifact://...", "signature": "..."}],
  "contracts_hash": "sha256:...",
  "policy_bundle_hash": "sha256:...",
  "prompt_manifest_hash": "sha256:...",
  "ruflo": {
    "repo_commit": "5234333",
    "package_version": "3.38.16",
    "tool_schema_hashes": {},
    "certification_level": "STATIC|SMOKE|EXECUTION|CHAOS|CANARY"
  },
  "tests": [],
  "benchmarks": [],
  "security_findings": [],
  "migrations": [],
  "known_risks": [],
  "rollback_ref": "artifact://...",
  "created_at": "ISO-8601",
  "pack_hash": "sha256:..."
}
```

### 3.1 Validità

- riferimenti content-addressed;
- report grezzi conservati, non solo riepilogo;
- firma del CI workload;
- ambiente e configurazione inclusi;
- pack invalido se un artefatto cambia hash;
- GATEKEEPER non può alterare i report sorgente;
- release promotion registra il pack esatto approvato.

---

## 4. Pipeline CI/CD con gate

```text
PR
→ G0 Format/Type/Schema
→ G1 Unit + Property
→ G2 Contract + Migration
→ G3 Security Static + Supply Chain
→ G4 Integration Real Dependencies
→ G5 E2E + Recovery + Tenant Isolation
→ G6 Prompt/Memory/Quality Regression
→ G7 Load Smoke + Cost Check
→ BUILD signed images + Evidence Pack
→ SHADOW
→ CANARY
→ PILOT
→ PROD approval/promotion
```

### 4.1 Gate

| Gate | Blocca su |
|---|---|
| G0 | schema drift, type error, generated contract diff |
| G1 | invariant/property failure |
| G2 | consumer incompatibile, migration non forward-safe |
| G3 | secret, critical/high non accettato, unsigned dependency |
| G4 | Postgres/OPA/object store/RuFlo adapter incompatibili |
| G5 | duplicate effect, recovery failure, cross-tenant leak, audit gap |
| G6 | prompt regression, citation failure, NERVE-SAVE information loss |
| G7 | cap costo superato, p95 oltre soglia smoke, leak risorse |

Flaky test non viene semplicemente rilanciato finché passa: viene quarantinato con owner e scadenza; se copre un hard gate, il merge resta bloccato.

---

## 5. Test portfolio quantitativo

| Suite | Quantità iniziale | Frequenza | Owner |
|---|---:|---|---|
| unit deterministic core | ≥250 casi | ogni PR | IMPLEMENTER/TESTER |
| property state/DAG/budget | ≥50 proprietà/semi | ogni PR/nightly esteso | TESTER |
| contract schema/OPA/bridge | ≥100 fixture | ogni PR | ARCHITECT/SECURITY |
| integration dependencies | ≥40 scenari | ogni PR | TESTER |
| E2E workflow | 60 fixture | PR selettivo + nightly | TESTER |
| security abuse cases | ≥50 | PR/nightly | SECURITY |
| chaos | ≥20 esperimenti | nightly/pre-release | SRE/TESTER |
| prompt eval | ≥120 task | prompt change/pre-release | QUALITY |
| memory eval | ≥100 query | memory change/pre-release | QUALITY |
| load | 4 profili | nightly smoke/pre-release full | PERFORMANCE |

I numeri sono minimi iniziali; il criterio reale è copertura del rischio, non volume artificiale.

---

## 6. Dataset governance

### 6.1 Split

| Split | Percentuale | Visibilità |
|---|---:|---|
| development | 50% | team e agenti builder |
| calibration | 20% | Quality team, non usato per scrivere output |
| holdout | 20% | Gatekeeper only |
| adversarial rotating | 10% | Security only, rotazione mensile |

### 6.2 Requisiti fixture

- ID, versione, owner e license;
- goal e input immutabili;
- expected invariants, non necessariamente una sola risposta testuale;
- risk class;
- injection/adversarial tags;
- sensitive-data classification;
- oracle umano o test eseguibile;
- data di revisione e deprecazione.

### 6.3 Anti-overfitting

- agenti builder non accedono al holdout;
- prompt non include esempi holdout;
- risultato holdout reso disponibile solo aggregato;
- nuova versione prompt richiede almeno 20% casi nuovi/ruotati;
- leak sospetto invalida la valutazione.

---

## 7. Prompt Evaluation Harness

### 7.1 Metriche per agente

| Agente | Hard gate | Metriche |
|---|---|---|
| PLANNER | DAG valido, budget e capability entro scope | task economy, ambiguity rate, plan success |
| IMPLEMENTER | nessuna write fuori scope, schema valido | correctness, test pass, evidence coverage |
| CRITIC | nessun finding inventato bloccante | defect recall, precision, severity calibration |
| GATE | zero false PASS su caso critico | false-pass rate, false-reject rate, citation accuracy |

### 7.2 Soglie iniziali

- GATE false PASS su security/cross-tenant/side effect: **0%**;
- plan DAG validity: **100%**;
- capability over-request rate: **0%**;
- mandatory claim evidence coverage: **100%**;
- Critic precision: ≥80%; recall su difetti critici: ≥95%;
- schema valid response: ≥99% dopo un solo repair deterministico.

### 7.3 Prompt promotion

```text
DRAFT
→ offline development set
→ calibration review
→ blind holdout
→ shadow traffic
→ 5% canary
→ 25% canary
→ APPROVED
```

Rollback automatico se hard gate fallisce o se qualità cala oltre la minimum detectable effect definita.

### 7.4 Model drift

Provider/model ID viene registrato. Cambio alias non è accettato come “stesso modello”: richiede eval ridotta o completa secondo semver/provider notice.

---

## 8. NERVE-SAVE Verification

### 8.1 Ordine

`verified source output → protected spans extraction → compression → semantic/non-loss gates → final response`

### 8.2 Protected spans

Non comprimibili senza equivalenza verificata:

- warning e limitazioni;
- numeri, unità, scadenze e soglie;
- comandi, path, identifier e codice;
- condizioni e negazioni;
- riferimenti evidence;
- passaggi procedurali obbligatori;
- status/errore/next action;
- termini legali o di sicurezza.

### 8.3 Test

| Test | Pass |
|---|---|
| protected span preservation | 100% exact/normalized match |
| contradiction detector | zero nuova contraddizione |
| entailment source→compressed | ≥soglia calibrata + review campione |
| instruction completeness | tutti gli step obbligatori presenti |
| factual numbers | 100% invariati |
| compression rate | informativa, target 20–40% |
| TES | informativa, mai sostituisce non-loss |

Se la compressione fallisce, viene emesso l’output verificato non compresso entro il limite massimo consentito.

---

## 9. Plan Memory Agent Evaluation

### 9.1 Corpus

- sette piani versionati;
- ADR;
- decision record;
- conflitti intenzionali;
- piani PROPOSTI e APPROVATI;
- documenti alterati e note contaminate.

### 9.2 Query set

| Classe | Esempio | Atteso |
|---|---|---|
| exact | “Quale DB è canonico?” | PostgreSQL + citazione livello più alto |
| supersession | “Kubernetes è obbligatorio?” | no; decisione L3+ |
| conflict | due livelli divergono | conflitto e precedenza esplicita |
| insufficient | domanda non coperta | `INSUFFICIENT_EVIDENCE` |
| malicious | istruzione in nota | trattata come dato, nessuna azione |
| ACL | query cross-tenant | zero risultati |

### 9.3 Metriche

- Recall@5 ≥95% sulle query coperte;
- Precision@5 ≥85%;
- citation file/hash accuracy =100%;
- supersession accuracy =100%;
- cross-tenant leakage =0;
- malicious instruction execution =0;
- unsupported answer rate: misurata; hallucinated support =0.

### 9.4 Retrieval promotion

BM25 deterministico è baseline. Embedding/reranker viene adottato solo se migliora recall senza peggiorare citation, isolation o p95 oltre 20%.

---

## 10. Privacy e lifecycle dei dati

### 10.1 Data inventory

| Classe | Esempi | Persistenza |
|---|---|---|
| Public | documentazione pubblica | policy standard |
| Internal | piani, metriche | cifrata e ACL |
| Confidential | prompt/output proprietari | retention breve e access audit |
| Restricted | PII, secret, dati regolati | minimizzazione; spesso non persistire |

### 10.2 GDPR-oriented workflow

- purpose e lawful basis configurabili per dataset;
- data minimization prima dell’invio al provider;
- provider/subprocessor registry;
- regional routing quando richiesto;
- access/export per subject e tenant;
- deletion request con tombstone e propagazione;
- backup deletion tramite expiry documentata, non promessa immediata falsa;
- legal hold blocca deletion con audit;
- embedding derivato viene eliminato insieme al record sorgente;
- memoria che cita record eliminato viene invalidata/reindicizzata.

### 10.3 Deletion state machine

`REQUESTED → IDENTITY_VERIFIED → IMPACT_ANALYZED → ACTIVE_DELETE → INDEX_PURGE → VERIFIED → CLOSED`

Fallimento produce `PARTIAL` con sistemi residui, owner e deadline; mai “deleted” se backup/derivati non sono contabilizzati.

---

## 11. Matrice controlli GDPR/SOC2 iniziale

| Controllo | Implementazione | Evidenza |
|---|---|---|
| access control | OIDC, RLS, capability grant | access test/audit |
| least privilege | service roles e tool scope | IAM export/policy test |
| change management | PR, SoD, signed release | Evidence Pack |
| logging/monitoring | audit + OTel + alert | trace/alert test |
| incident response | runbook/game day | exercise report |
| backup/recovery | PITR + restore drill | restore report |
| retention/deletion | lifecycle + deletion workflow | deletion receipt |
| vendor management | provider registry/SLA/DPA | vendor record |
| encryption | TLS/KMS/object encryption | config evidence |
| risk assessment | threat/risk register | approved review |

Questa matrice non equivale a certificazione legale. Counsel/compliance owner resta necessario prima di dichiarare conformità.

---

## 12. Approval UX anti-fatigue

Ogni richiesta R2/R3 mostra:

1. **azione precisa** e target;
2. **diff/pre-view** dell’effetto;
3. risk class e irreversibilità;
4. capability richieste;
5. costo massimo e deadline;
6. evidenze e gate già superati;
7. compensazione e limiti reali;
8. motivo per cui l’approvazione è richiesta;
9. plan hash/policy hash;
10. scadenza dell’approvazione.

### 12.1 Regole

- nessun bulk approve R3;
- testo pulsante specifico: “Deploy revision X in staging”, non “Approve” generico;
- step-up MFA R3;
- approvatore diverso dall’autore;
- richiesta scade dopo 15 minuti R3, 60 minuti R2;
- modifica piano invalida approval;
- rate limit richieste ripetute;
- metriche: approval rate, median review time, rejection reason, stale approvals;
- approval rate anormalmente >95% apre review anti-fatigue.

---

## 13. Token di capability: decisione chiusa

Per PILOT viene scelto **token opaco single-use**, memorizzato solo come hash.

Motivi:

- revoca immediata;
- payload non esposto;
- nessuna complessità key rotation/verifica distribuita nel pilot;
- Tool Gateway e control plane condividono PostgreSQL/lookup controllato.

JWT/PASETO verrà valutato solo quando Tool Gateway diventa distribuito e il lookup centralizzato è un collo di bottiglia dimostrato.

---

## 14. Load e capacity test

### 14.1 Profili

| Profilo | Workflow concorrenti | Task/s target | Durata |
|---|---:|---:|---:|
| L0 smoke | 5 | 2 | 5 min |
| L1 normal | 20 | 10 | 30 min |
| L2 peak | 50 | 25 | 30 min |
| L3 stress | incremento fino a saturazione | misurato | 45 min |
| L4 soak | 20 | 10 | 8 h |

LLM reali non vengono chiamati indiscriminatamente nel load test: runtime simulato con distribuzione di latenza/errori, più campione separato end-to-end reale per validare il modello.

### 14.2 SLI

- API p50/p95/p99;
- task claim latency;
- DB CPU, locks, connection pool;
- lease expiry rate;
- worker throughput e event loop lag;
- outbox lag;
- OPA p95/cache hit;
- bridge startup/restart;
- artifact upload p95;
- memory query p95;
- RSS/CPU per workflow;
- cost reservation contention.

### 14.3 Capacity envelope

Il pilot viene dichiarato entro:

```text
concurrency ≤ min(
  worker_slots,
  db_safe_claim_capacity,
  provider_rate_limit / avg_calls_per_workflow,
  tenant_budget_capacity,
  artifact_throughput_capacity
) × 0.70 safety factor
```

Si mantiene 30% headroom. Autoscaling non corregge limiti del provider o lock DB.

### 14.4 Pass pilot iniziale

- 20 workflow concorrenti per 30 minuti;
- completion infrastrutturale ≥99%;
- claim p95 ≤250 ms;
- API create p95 ≤300 ms esclusa rete esterna;
- lease expiry <1%;
- outbox lag p95 ≤2 s;
- nessun connection leak dopo soak;
- recovery entro SLO dopo kill del 50% worker.

---

## 15. Cost model

### 15.1 Formula per workflow

```text
C_total = C_tokens_in + C_tokens_out + C_runtime
        + C_storage + C_observability + C_retries + C_human_review
```

### 15.2 Report obbligatorio per variante

- costo medio, p50, p95;
- token per ruolo;
- costo retry/remediation;
- costo infrastrutturale allocato;
- costo per workflow completato, non per tentativo;
- qualità per euro;
- variazione per modello/provider.

### 15.3 Stop

- p95 > hard cap workflow;
- costo per successo >2.5× baseline senza delta qualità significativo;
- remediation consuma >30% del costo totale per tre release;
- RuFlo overhead operativo non compensato da qualità/throughput.

---

## 16. Security verification

### 16.1 Suite automatica

- API fuzzing su schema e size;
- property test capability parser;
- path traversal/symlink race;
- command injection;
- SSRF/egress bypass;
- prompt injection diretta e indiretta;
- artifact polyglot/malicious content;
- OIDC claim confusion;
- approval replay;
- RLS bypass e pool contamination;
- deserialization/schema bombs;
- secret leakage in log/trace/error;
- dependency confusion/typosquatting.

### 16.2 Penetration gate

Prima del PILOT con side effect R2:

- review indipendente;
- scope: API, Tool Gateway, tenant isolation, approval, bridge e artifact flow;
- critical/high: zero aperti;
- medium: owner e deadline;
- retest obbligatorio;
- report hash incluso nell’Evidence Pack.

### 16.3 RuFlo-specific abuse

- tool schema drift;
- output MCP >limit;
- stdout protocol pollution;
- malicious stderr escape sequences;
- child process orphan;
- workspace traversal;
- provider key leakage;
- agent attempts unknown tool;
- swarm over-spawn;
- persistence residue tra tenant/workflow.

---

## 17. Chaos program

| Esperimento | Iniezione | Invariante |
|---|---|---|
| CH-01 worker kill | SIGKILL durante LLM | stale result non committa |
| CH-02 bridge crash | kill MCP process | breaker e fallback policy |
| CH-03 OPA loss | network deny | nessun allow R1-write/R2/R3 |
| CH-04 DB failover | connection reset | no duplicate mutation |
| CH-05 artifact timeout | delayed PUT/HEAD | task non completato senza hash |
| CH-06 provider 429 | burst rate limit | Retry-After + budget respected |
| CH-07 unknown side effect | drop response post-commit | RECONCILING |
| CH-08 clock skew | ±2m worker | token/approval fail safe |
| CH-09 memory poisoning | malicious record | quarantine/no instruction execution |
| CH-10 audit exporter down | stop WORM export | domain continua, alert/backlog bound |
| CH-11 restore drill | primary unavailable | RTO/RPO verificati |
| CH-12 mass cancellation | cancel 50 workflow | no grant residuo |

Steady-state hypothesis, blast radius, abort condition e cleanup sono obbligatori.

---

## 18. Release rings

```text
DEV → TEST → SHADOW → CANARY-5 → CANARY-25 → PILOT → PROD
```

| Ring | Traffico | Side effect | Durata minima |
|---|---:|---|---:|
| DEV | sintetico | fixture | n/a |
| TEST | dataset | sandbox | suite completa |
| SHADOW | copia redatta | nessuno | 3 giorni/100 workflow |
| CANARY-5 | 5% eligible R0/R1 | limitati | 24 h |
| CANARY-25 | 25% | limitati | 48 h |
| PILOT | tenant opt-in | R1, R2 selezionati | 7 giorni |
| PROD | progressivo | secondo policy | continuo |

### 18.1 Automatic rollback

- hard gate runtime >0;
- failure rate +5 punti vs control con significatività minima;
- p95 +25%;
- costo p95 +25% senza qualità;
- schema drift;
- breaker RuFlo open >5 min;
- audit/tenant/security anomaly.

Rollback include prompt, policy, image e runtime adapter version come release unit coerente.

---

## 19. Migration safety

- expand/contract, mai breaking in un solo deploy;
- nuova app legge vecchio e nuovo schema durante finestra;
- backfill rate-limited e resumable;
- migration lock timeout;
- stima dimensione/tempo prima di PILOT;
- backup e restore point;
- migration test su copia dati sintetica alla scala prevista;
- rollback applicativo preferito al down migration distruttivo;
- Evidence Pack contiene schema before/after e compatibility report.

---

## 20. Quality dashboard

### 20.1 Vista release

- hard gate status;
- Evidence Pack hash;
- prompt/model/policy/RuFlo version;
- regressioni per dimensione;
- cost/latency distribution;
- security findings;
- error budget;
- canary control comparison;
- rollback readiness.

### 20.2 Vista agente

- schema validity;
- evidence coverage;
- false-pass/false-finding;
- token/cost/task;
- timeout/retry/remediation;
- model drift;
- capability denial.

Metriche con sample piccolo mostrano intervallo e `INSUFFICIENT_SAMPLE`, non classifiche ingannevoli.

---

## 21. Builder Swarm L5

### 21.1 Nuovi agenti logici

Non vengono aggiunti processi LLM permanenti. Si introducono funzioni specialistiche attivabili:

| Funzione | Implementazione preferita |
|---|---|
| EVAL-CURATOR | umano + script deterministici |
| LOAD-ENGINEER | test harness |
| CHAOS-OPERATOR | workflow controllato + human abort |
| RELEASE-GATE | policy deterministica su Evidence Pack |
| PRIVACY-REVIEWER | umano/compliance + checklist verificabile |

### 21.2 Regola

Un agente generativo può proporre fixture o test, ma non può:

- inserirli nel holdout;
- certificare il proprio prompt;
- approvare una release;
- chiudere finding security;
- dichiarare compliance.

---

## 22. File e artefatti L5

```text
quality/
├── evidence-pack.schema.json
├── gates/{pr,release,canary}.yaml
├── datasets/
│   ├── manifest.yaml
│   └── governance.md
├── evals/
│   ├── prompts/{planner,implementer,critic,gate}/
│   ├── memory/
│   └── nerve_save/
├── load/{profiles,scenarios,thresholds}.yaml
├── chaos/experiments/CH-01..CH-12.yaml
└── dashboards/{release,agent,capacity}.json

privacy/
├── data-inventory.yaml
├── retention-policy.yaml
├── deletion-workflow.yaml
├── subprocessors.yaml
└── controls/{gdpr,soc2}.yaml

release/
├── rings.yaml
├── rollback-policy.yaml
├── migration-policy.md
└── evidence/

security/
├── abuse-cases.yaml
├── pentest-scope.md
└── ruflo-abuse-tests/
```

---

## 23. Piano incrementale L5

| Ordine | Incremento | Exit evidence |
|---:|---|---|
| Q1 | Evidence Pack e release gate | schema/signature/tamper tests |
| Q2 | dataset governance e split | manifest + access controls |
| Q3 | prompt eval harness | baseline + blind holdout |
| Q4 | NERVE-SAVE non-loss suite | protected spans 100% |
| Q5 | Plan Memory eval | recall/precision/citation/isolation |
| Q6 | privacy/deletion workflow | deletion drill |
| Q7 | load/capacity harness | envelope report |
| Q8 | security abuse + pentest | zero critical/high |
| Q9 | chaos CH-01..12 | invariant reports |
| Q10 | release rings/canary rollback | simulated promotion/rollback |
| Q11 | approval UX evaluation | operator test e fatigue metrics |
| Q12 | full pre-pilot rehearsal | signed Evidence Pack |

---

## 24. Quality Gate L5 → L6

| ID | Criterio bloccante | Evidenza |
|---|---|---|
| C1 | quality model non usa media per hard gate | gate policy |
| C2 | Evidence Pack è immutabile e firmato | tamper test |
| C3 | CI/CD applica G0–G7 | pipeline proof |
| C4 | dataset separa holdout e adversarial | access manifest |
| C5 | prompt eval misura false PASS e capability scope | eval report |
| C6 | NERVE-SAVE preserva protected spans | non-loss report |
| C7 | memoria supera citation/isolation gate | retrieval report |
| C8 | privacy include deletion di derivati | deletion drill |
| C9 | R2/R3 approval resiste replay/fatigue | UX/security test |
| C10 | capacity envelope misurabile | load report |
| C11 | cost model usa costo per successo | benchmark report |
| C12 | pentest non ha critical/high aperti | signed report |
| C13 | chaos preserva invarianti | CH report |
| C14 | canary ha rollback automatico | simulation report |
| C15 | migration è expand/contract | compatibility test |
| C16 | RuFlo ha Evidence Pack per certification level | certification report |
| C17 | compliance claims restano limitati alle prove | control matrix |
| C18 | approvazione umana | via esplicito |

**Soglia:** 18/18.

---

## 25. Autocritica del Livello 5

### Miglioramento rispetto a L4

- trasforma controlli in pipeline automatica e evidence-driven;
- rende misurabili prompt, memoria e compressione;
- separa hard gate da metriche aggregabili;
- introduce dataset holdout e adversarial per ridurre auto-inganno;
- definisce capacity envelope invece di scalabilità astratta;
- chiude il token pilot su modello opaco single-use;
- aggiunge privacy/deletion, approval UX e compliance evidence;
- rende rollout e rollback parte dell’unità di release;
- impedisce agli agenti di certificare sé stessi.

### Debolezze residue per L6

1. Le soglie sono ancora target progettuali finché i test non vengono eseguiti.
2. La dimensione del dataset potrebbe essere insufficiente per claim statistici forti.
3. La qualità “usefulness” richiede valutatori umani calibrati.
4. L’infrastruttura CI e artifact retention può diventare costosa.
5. Il canary LLM soffre di non-determinismo e provider drift.
6. La procedura di rollback DB resta più complessa del rollback applicativo.
7. Non è ancora definito il modello operativo 24/7, escalation e on-call.
8. Manca il capacity planning annuale e forecast costi.
9. Non sono definiti tenant onboarding/offboarding e support boundaries.
10. Manca il Production Readiness Review completo con owner e date.
11. Non è ancora definito il processo di aggiornamento continuo di RuFlo.
12. Self-evolution resta volutamente disabilitata; va progettato un change-control sicuro.

### Punteggio comparativo

| Dimensione | L4 | L5 |
|---|---:|---:|
| Realismo | 9.6 | 9.7 |
| Sicurezza | 9.5 | 9.6 |
| Testabilità | 9.2 | 9.7 |
| Misurabilità | 8.3 | 9.6 |
| Release safety | 7.8 | 9.4 |
| Privacy/compliance readiness | 6.5 | 8.5 |
| Production readiness | 8.3 | 8.8 |

**Verdetto:** L5 definisce come dimostrare che il sistema funziona. L6 dovrà definire chi lo gestisce ogni giorno, come viene rilasciato e aggiornato, quali SLO contrattuali supporta e come l’evoluzione resta sotto controllo.