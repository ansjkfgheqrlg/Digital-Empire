# LIVELLO 6/7 — Production operating model e go-live controllato

**Versione:** 6.0.0  
**Sostituisce:** `level-05-quality-evidence-release.md`  
**Stato:** PROPOSTO — attende approvazione umana  
**Obiettivo:** definire persone, responsabilità, processi e limiti necessari per gestire l’Orchestration Layer dopo il rilascio.

---

## 1. Autocritica del Livello 5

| Limite L5 | Conseguenza | Correzione L6 |
|---|---|---|
| pipeline tecnica senza owner operativo | gate verdi ma nessuno risponde agli incidenti | service ownership e RACI |
| SLO senza servizio/supporto formalizzato | aspettative ambigue | service tier, SLI, error budget e support boundary |
| canary senza autorità decisionale | rollback ritardato | release commander e stop authority |
| runbook senza turnazione | documenti inutili durante incidenti | on-call, escalation e game day |
| tenant lifecycle assente | provisioning manuale e rischio dati residui | onboarding, quota, offboarding e deletion receipt |
| forecast costo assente | denial-of-wallet a livello portfolio | unit economics e capacity forecast |
| upgrade RuFlo non formalizzato | drift e supply-chain regression | compatibility lane, dual-run e rollback pin |
| self-evolution disabilitata senza percorso | miglioramento affidato a modifiche ad hoc | experiment/change-proposal control plane |
| PRR solo implicita | go-live soggettivo | checklist con owner, evidenza e veto |
| DR tecnico senza business continuity | recovery non prioritizzato per rischio | service restoration order |
| troppi controlli potenziali | carico operativo e rituali vuoti | automazione, exception expiry e controllo del toil |
| assenza decommission plan | sistemi e dati permanenti | lifecycle di servizio e kill criteria |

### Giudizio brutale

Un sistema non è production-ready perché supera i test. È production-ready quando esiste un team che può rilevare, contenere, spiegare e ripristinare un guasto alle 03:00 senza affidarsi all’autore originale o a conoscenza non documentata.

---

## 2. Service definition

### 2.1 Nome e tier

- **Servizio:** Orchestration Control Plane (`OCP`)
- **Release iniziale:** `0.1 PILOT`
- **Tier pilot:** Tier 2 interno, non mission-critical
- **Classi abilitate:** R0/R1; R2 solo tenant opt-in e capability allowlisted
- **R3:** disabilitato al go-live iniziale

R3 viene attivato con change separato dopo almeno 30 giorni di pilot, zero incidenti critici e PRR dedicata.

### 2.2 Dipendenze

| Dipendenza | Criticità | Owner |
|---|---|---|
| PostgreSQL managed | critica | Platform/Data |
| Object store | critica | Platform |
| OPA/policy bundle | critica | Security/Service team |
| Identity provider | alta | IAM |
| LLM provider | alta ma sostituibile R0/R1 | AI Platform |
| RuFlo bridge/runtime | opzionale nel pilot | Orchestration team |
| OTel backend | media; audit indipendente | Observability |
| Secret manager | critica per nuove esecuzioni | Platform Security |

### 2.3 Support boundary

Il servizio garantisce:

- accettazione e tracking workflow;
- policy, budget e capability enforcement;
- esecuzione entro capability dichiarate;
- audit e recovery secondo SLO;
- artifact e risultato secondo contratto.

Non garantisce:

- correttezza dei sistemi downstream fuori contratto;
- disponibilità illimitata dei provider LLM;
- rollback di azioni dichiarate irreversibili;
- risultati identici da modelli probabilistici;
- conformità legale automatica del caso d’uso del tenant;
- supporto per skill non `ACTIVE`.

---

## 3. Organizzazione e RACI

### 3.1 Ruoli umani

| Ruolo | Responsabilità |
|---|---|
| Service Owner | roadmap, rischio accettato, SLO e budget |
| Tech Lead | architettura, ADR, qualità tecnica |
| Primary On-call | triage, containment, runbook |
| Secondary On-call | escalation tecnica e recovery |
| Security Owner | policy, finding, incidenti security |
| Data/Privacy Owner | retention, deletion, data inventory |
| Release Commander | promozione, canary, rollback |
| Incident Commander | coordinamento incidenti SEV-1/2 |
| RuFlo Maintainer | compatibility e certification |
| Product/Tenant Owner | priorità e accettazione del rischio d’uso |

### 3.2 RACI sintetica

| Attività | Service | Security | Platform | Privacy | Tenant | Release Cmd |
|---|---|---|---|---|---|---|
| modifica dominio | A/R | C | C | I | I | I |
| policy capability | C | A/R | I | C | I | I |
| release | R | C | C | I | I | A |
| rollback | R | C | R | I | I | A |
| incidente SEV-1 | R | R se security | R | C | I | I |
| tenant onboarding | R | C | C | C | A | I |
| deletion request | C | I | R | A | C | I |
| RuFlo upgrade | A | C | C | I | I | R |
| R3 enablement | R | A | C | C | A | A |

`A` deve essere singolo per riga decisionale. Nessun agente LLM ricopre una responsabilità umana accountable.

---

## 4. On-call e incident management

### 4.1 Copertura pilot

- supporto iniziale: 08:00–20:00 giorni lavorativi;
- fuori orario: alert solo per data/security/cost critical;
- nessuna promessa 24/7 finché rotazione <4 persone;
- workflow R2 ammessi solo nella finestra supportata;
- R3 disabilitato.

**Motivo:** una rotazione 24/7 con meno di quattro persone è insostenibile e produce burnout o copertura fittizia.

### 4.2 Severità

| Sev | Definizione | Ack | Update | Autorità |
|---|---|---:|---:|---|
| SEV-1 | cross-tenant leak, policy bypass, duplicate critical effect, secret compromise | 5 min | 15 min | Incident Commander |
| SEV-2 | servizio indisponibile, recovery/compensation fallita, cost runaway | 15 min | 30 min | Primary + IC |
| SEV-3 | degrado parziale, RuFlo down con fallback | 1 h | 2 h | Primary |
| SEV-4 | bug senza impatto immediato | 1 giorno | backlog | Service team |

### 4.3 Protocollo

```text
Detect → Acknowledge → Classify → Contain → Preserve evidence
→ Communicate → Recover → Verify → Close → Postmortem → Track actions
```

- contenimento prima della root cause completa;
- stop R2/R3 indipendente da R0/R1;
- timeline automatica da audit/trace, verificata dall’IC;
- postmortem blameless entro 5 giorni per SEV-1/2;
- action item con owner e scadenza;
- recidiva dello stesso failure mode aumenta severità di governance.

---

## 5. SLO, error budget e policy operative

### 5.1 SLO pilot

| SLI | SLO | Esclusioni limitate |
|---|---:|---|
| API create availability | 99.5% mensile | maintenance annunciata |
| workflow R0/R1 infrastructure completion | 95% | input invalidi e downstream esplicitamente fuori SLA |
| API create latency p95 | ≤300 ms | rete client |
| task claim p95 | ≤250 ms | nessuna |
| worker crash recovery p95 | ≤45 s | region loss |
| audit completeness | 100% | nessuna |
| duplicate side effect | 0 | nessuna |
| tenant/security bypass | 0 | nessuna |
| deletion completion | entro policy, target 30 giorni | legal hold documentato |

### 5.2 Burn-rate action

| Condizione | Azione |
|---|---|
| 2% budget consumato in 1 h | page + investigate |
| 10% in 6 h | freeze release |
| 25% in 24 h | riduci traffico/capability |
| 50% in 7 giorni | stop nuove feature, reliability sprint |
| hard-zero violation | SEV-1 + freeze R2/R3 |

### 5.3 Maintenance

- finestra settimanale dichiarata, non usata per mascherare downtime ricorrente;
- migrazioni online quando possibile;
- maintenance R2/R3 richiede drain e verifica task in-flight;
- clienti/tenant informati secondo tier.

---

## 6. Tenant lifecycle

### 6.1 Onboarding

```text
REQUESTED
→ USE_CASE_REVIEW
→ DATA/RISK_CLASSIFICATION
→ QUOTA_DEFINED
→ SKILL/CAPABILITY_ALLOWLIST
→ TEST_TENANT
→ ACCEPTANCE_TEST
→ PILOT_ENABLED
→ ACTIVE
```

Checklist:

- owner umano e contatti;
- use case e classi R0–R3;
- data residency/classification;
- provider consent e subprocessor;
- quota costo/concorrenza;
- skill allowlist;
- approval group e SoD;
- retention;
- success metrics;
- kill switch testato;
- support boundary accettato.

### 6.2 Runtime isolation

- quota per tenant: concurrency, task, token, costo, storage;
- rate limit e queue fairness;
- circuit breaker per tenant e provider;
- un tenant rumoroso non consuma tutti i worker;
- weighted fair scheduling, con cap massimo;
- nessuna priorità assoluta configurabile dal tenant.

### 6.3 Offboarding

```text
NOTICE → NEW_WORK_DISABLED → DRAIN/CANCEL → GRANTS_REVOKED
→ DATA_EXPORT → ACTIVE_DELETE → BACKUP_EXPIRY_TRACKED
→ CREDENTIALS/INTEGRATIONS_REMOVED → RECEIPT → CLOSED
```

Offboarding fallito resta `PARTIAL`, non `CLOSED`.

---

## 7. Change management

### 7.1 Classi

| Classe | Esempio | Approvazione | Rollout |
|---|---|---|---|
| C0 standard | patch docs/dashboard | peer review | normale |
| C1 normal | codice R0/R1 compatibile | Tech Lead + gates | canary |
| C2 high-risk | policy, schema, auth, bridge | Security/Platform/Release | shadow + canary esteso |
| C3 emergency | contenimento incidente | IC + second approver se possibile | immediato, review successiva |

### 7.2 Change record

- motivazione e rischio;
- artifact/Evidence Pack;
- blast radius;
- migration e backward compatibility;
- metriche canary;
- rollback trigger e procedura;
- owner e finestra;
- approvazioni;
- risultato e follow-up.

### 7.3 Configuration

- config versionata e validata;
- niente modifica manuale persistente in container;
- feature flag con owner, expiry e default sicuro;
- flag stale rimosso entro 30 giorni dalla stabilizzazione;
- policy e prompt fanno parte della release unit, non “config innocua”.

---

## 8. RuFlo lifecycle management

### 8.1 Pinning

La release registra:

- repository commit;
- package/versione;
- Node version;
- lockfile hash;
- tool list e schema hash;
- provider config schema;
- certification level;
- known deviations.

`latest` è vietato in PILOT/PROD.

### 8.2 Upgrade lane

```text
New RuFlo candidate
→ source/dependency diff
→ STATIC certification
→ isolated SMOKE
→ EXECUTION eval
→ CHAOS
→ SHADOW dual-run
→ CANARY 5%
→ promote pin or reject
```

### 8.3 Compatibilità

- bridge supporta al massimo corrente e precedente pin approvato;
- schema mismatch apre breaker, non adapter coercion silenziosa;
- nuova capability non viene auto-esposta;
- memory/federation/autoscaling RuFlo restano off finché certificati separatamente;
- rollback ripristina immagine bridge + RuFlo pin + prompt/model compatibility set.

### 8.4 Frequenza

- security patch critical: lane accelerata con evidence minima non derogabile;
- minor: valutazione mensile;
- major/architecture: progetto dedicato;
- pin non aggiornato oltre 90 giorni richiede risk acceptance esplicita.

---

## 9. Provider/model lifecycle

- alias provider risolto a model ID concreto per ogni task;
- nuovo model ID passa prompt eval e cost benchmark;
- deprecazione provider genera migration plan;
- fallback cross-provider solo R0/R1 e se data policy lo consente;
- R2/R3 non cambiano provider durante un workflow senza nuova autorizzazione;
- rate limit e quota configurati per provider;
- dati inviati minimizzati e registrati per classification, non payload completo nei log;
- outage prolungato può degradare a queue/pause, non a modello non certificato.

---

## 10. Self-evolution supervisionata

### 10.1 Principio

Il runtime non modifica direttamente prompt, policy, workflow, memoria schema o agenti. Produce una **Change Proposal**.

### 10.2 Ciclo

```text
OBSERVE
→ PATTERN CANDIDATE
→ HYPOTHESIS
→ CHANGE PROPOSAL
→ RISK CLASSIFICATION
→ OFFLINE EXPERIMENT
→ HOLDOUT
→ HUMAN REVIEW
→ SHADOW
→ CANARY
→ ADOPT or REJECT
→ MONITOR/ROLLBACK
```

### 10.3 Change Proposal

```json
{
  "proposal_id": "evo-uuid",
  "target": "prompt|routing|timeout|retrieval|budget-default",
  "current_version": "...",
  "proposed_change": "artifact://...",
  "evidence": [],
  "hypothesis": "string",
  "expected_delta": {"metric": "...", "minimum": 0.05},
  "risk": "R1|R2|R3",
  "blast_radius": "shadow|5%|25%",
  "rollback": "artifact://...",
  "expires_at": "ISO-8601"
}
```

### 10.4 Autonomia consentita

| Azione | Autonoma? |
|---|---:|
| proporre cambio | sì |
| eseguire offline eval sandbox | sì entro budget |
| scartare proposta chiaramente peggiore | sì, con log |
| promuovere in shadow | solo policy R1 pre-approvata |
| canary con traffico reale | no, human approval |
| cambiare security/policy/schema | no |
| aggiungere capability/tool | no |
| modificare R2/R3 | no |

### 10.5 Guardrail

- una variabile primaria per esperimento;
- sample size minimo predefinito;
- niente accesso holdout da parte del proposer;
- adoption richiede delta significativo e nessun hard-gate regression;
- massimo due esperimenti concorrenti per dominio;
- budget mensile esperimenti;
- proposal scade;
- rollback automatico collegato alla release unit.

---

## 11. Capacity e cost forecasting

### 11.1 Driver

- tenant attivi;
- workflow/tenant/giorno;
- task/workflow;
- token e durata per ruolo;
- retry/remediation rate;
- storage artifact e retention;
- telemetry volume;
- human approval volume;
- provider rate limits;
- picco/concurrency factor.

### 11.2 Forecast

Tre scenari trimestrali:

| Scenario | Crescita | Headroom |
|---|---:|---:|
| conservative | +20% | 30% |
| expected | +50% | 40% |
| stress | +100% | 50% |

Aggiornamento mensile usando actual. Errore forecast >20% per due mesi richiede revisione modello.

### 11.3 Unit economics

Report:

- costo per workflow accettato;
- costo per workflow completato;
- costo per tenant;
- costo per skill;
- costo per runtime Local/RuFlo;
- costo remediation;
- costo umano approval/incident;
- margine di budget e anomalie.

### 11.4 Capacity review

- settimanale nel pilot, mensile dopo stabilità;
- trigger scale-up prima del 70% capacity envelope;
- scale-down non riduce redundancy minima;
- provider quota richiesta con lead time;
- DB connection budget allocato per API/worker/admin.

---

## 12. Production Readiness Review

### 12.1 Blocchi

| Area | Owner | Evidenza minima |
|---|---|---|
| scope/service tier | Service Owner | service definition |
| architecture | Tech Lead | ADR + diagrams |
| security | Security | threat model, pentest, zero high/critical |
| privacy | Privacy | inventory, retention, deletion drill |
| reliability | SRE/Service | chaos, restore, SLO dashboard |
| performance | Performance | capacity envelope |
| cost | Service Owner | forecast e hard caps |
| operations | On-call Lead | runbook/game day |
| release | Release Commander | canary/rollback rehearsal |
| RuFlo | Maintainer | certification dossier |
| tenant | Product Owner | onboarding acceptance |
| compliance | Compliance | control evidence/risk acceptance |

### 12.2 Veto

Security, Privacy, Service Owner e Release Commander hanno veto nelle rispettive aree. Un veto non viene superato con voto medio.

### 12.3 Esiti

- `GO`;
- `GO_WITH_EXCEPTIONS` solo con owner, expiry, compensating control;
- `NO_GO`;
- `REVIEW_AGAIN` dopo remediation.

Exception senza scadenza è vietata. Critical/high security e hard-zero invariant non ammettono eccezione.

---

## 13. Go-live plan

### 13.1 T-30 a T-8 giorni

- PRR documenti congelati;
- restore drill;
- penetration retest;
- capacity test;
- tenant pilot selezionati;
- on-call training;
- runbook game day;
- status/communication channel;
- support boundary firmato.

### 13.2 T-7 a T-1

- release candidate e Evidence Pack;
- change freeze non essenziale;
- credential e quota verificate;
- RuFlo pin certificato o disabilitato;
- rollback rehearsal;
- dashboard/alert test;
- backup restore point;
- go/no-go meeting.

### 13.3 T0

```text
Deploy control plane
→ smoke
→ enable R0 internal
→ observe 2 h
→ enable R1 internal
→ observe 4 h
→ tenant pilot 5%
→ observe 24 h
→ 25%
→ observe 48 h
→ pilot full eligible traffic
```

R2 non viene attivato nello stesso giorno del primo go-live.

### 13.4 T+1 a T+30

- daily operational review prima settimana;
- weekly error budget/cost/capacity;
- incident/failure pattern review;
- nessuna espansione agenti senza benchmark;
- R2 activation review dopo stabilità;
- post-launch review a 7 e 30 giorni.

---

## 14. Rollback e kill switch

### 14.1 Livelli

| Livello | Azione |
|---|---|
| K1 | disabilita nuova feature/prompt/runtime route |
| K2 | disabilita RuFlo, usa LocalRuntime R0/R1 |
| K3 | stop nuove R2/R3, drain in-flight |
| K4 | stop nuovi workflow, mantieni query/recovery |
| K5 | global containment: revoke grants, freeze writes controllato |

### 14.2 Requisiti

- accesso kill switch con MFA e SoD per K5 se tempo consente;
- esecuzione testata mensilmente;
- azione auditata;
- nessun kill indiscriminato che perda esito side effect: task incerti passano a reconciliation;
- riattivazione richiede criterio esplicito e approvazione.

---

## 15. Business continuity

### 15.1 Priorità ripristino

1. audit/state integrity;
2. revoca capability e containment;
3. query stato workflow;
4. reconciliation/compensation;
5. R0;
6. R1;
7. R2;
8. R3.

### 15.2 Modalità degradata

| Modalità | Consentito | Vietato |
|---|---|---|
| DB read-only | query e incident inspection | nuove mutation |
| RuFlo down | LocalRuntime R0/R1 certificato | R2/R3 silent fallback |
| OPA down | R0 read-only con cache stretta | nuove write/R2/R3 |
| provider down | queue/pause | modello non certificato |
| telemetry down | execution con audit DB | perdita audit |
| artifact store down | query metadata | completion task con artifact mancante |

---

## 16. Toil management

### 16.1 Misura

- interventi manuali per 100 workflow;
- remediation manuale;
- approval non necessarie;
- alert non azionabili;
- runbook non automatizzati;
- tempo on-call;
- flaky test;
- exception aperte.

### 16.2 Target

- toil <20% capacità team;
- alert actionable rate ≥90%;
- manual intervention <2% workflow R0/R1;
- runbook automation per operazioni ripetute ≥80%;
- exception scadute =0;
- false approval request <5%.

Se toil supera 20% per due sprint, freeze feature e reliability/automation work.

---

## 17. Agent ecosystem in produzione

### 17.1 Runtime iniziale

| Ruolo | Modalità | Concorrenza |
|---|---|---:|
| PLANNER | on-demand | max 1/workflow |
| IMPLEMENTER | on-demand | max 2/workflow |
| CRITIC | on-demand indipendente | max 1/artifact |
| GATE | on-demand | max 1/gate |
| Plan Memory Agent | read-only service/function | bounded query pool |
| Meta Observer | batch offline | nessun side effect |

Non esiste una popolazione permanente di “tantissimi agenti”. Lo swarm massimo cresce solo con capacity, quality delta e budget dimostrati.

### 17.2 Agent registry operativo

Per ogni agente:

- owner;
- prompt/model/version;
- capability massime;
- risk class consentite;
- SLO/timeout;
- cost cap;
- eval status;
- last certification;
- kill switch;
- deprecation date.

Agente scaduto o non certificato non viene routed.

---

## 18. Skill operations

### 18.1 Registry

| Stato | Routing |
|---|---|
| DRAFT | solo dev |
| VALIDATING | test/shadow |
| ACTIVE | production secondo risk |
| DEPRECATED | workflow esistenti, niente nuovi tenant |
| SUSPENDED | nessuna nuova esecuzione |
| REVOKED | grant revocati e incident review |

### 18.2 Ownership

Ogni skill ha:

- owner e backup owner;
- side-effect contract;
- SLO dipendenza;
- quota;
- test/evidence pack;
- runbook;
- data classification;
- deprecation e migration path.

Skill senza owner attivo viene sospesa.

---

## 19. Knowledge e memory operations

- Plan Memory Agent reindicizza solo release approvate;
- consistency scan giornaliero su hash e supersession;
- retention job con dry-run/report prima della cancellazione;
- deletion queue monitorata;
- retrieval quality settimanale nel pilot;
- poisoned/suspicious record quarantine automatica, review umana;
- index rebuild provato da source of truth;
- memoria non è backup: si può ricostruire da artifact e record approvati;
- RuFlo memory resta separata/non canonica finché non certificata.

---

## 20. Decommission e exit strategy

### 20.1 Trigger

- qualità non supera baseline dopo tre cicli;
- costo per successo non sostenibile;
- incidenti hard-zero ripetuti;
- dipendenza RuFlo/provider non mantenibile;
- owner/on-call insufficienti;
- uso tenant sotto soglia per due trimestri;
- sostituzione con servizio più semplice.

### 20.2 Piano

1. blocco nuovi tenant/workflow;
2. drain e reconcile;
3. export dati/audit;
4. revoca grant/credential;
5. offboarding tenant;
6. retention/deletion;
7. archive ADR/Evidence Pack;
8. spegnimento runtime;
9. verifica costi residui;
10. closure report.

La possibilità di dismettere il sistema impedisce lock-in operativo e architettura immortale.

---

## 21. File e artefatti L6

```text
operations/
├── service-definition.yaml
├── ownership.yaml
├── oncall-policy.md
├── severity-matrix.yaml
├── escalation-policy.yaml
├── slo.yaml
├── error-budget-policy.yaml
├── toil-dashboard.json
└── business-continuity.md

tenants/
├── onboarding-workflow.yaml
├── quota-policy.yaml
├── support-boundary.md
├── offboarding-workflow.yaml
└── templates/acceptance-test.yaml

change/
├── change-classes.yaml
├── exception-policy.yaml
├── feature-flag-policy.yaml
├── ruflo-upgrade-lane.yaml
├── model-lifecycle.yaml
└── self-evolution-proposal.schema.json

readiness/
├── prr-checklist.yaml
├── go-live-plan.md
├── rollback-matrix.yaml
├── kill-switch-runbook.md
└── post-launch-review.md

finance/
├── unit-economics.yaml
├── capacity-forecast.yaml
└── provider-quota-register.yaml
```

---

## 22. Piano incrementale L6

| Ordine | Incremento | Evidenza d’uscita |
|---:|---|---|
| O1 | service definition + RACI | owner acceptance |
| O2 | on-call/severity/escalation | tabletop incident |
| O3 | tenant onboarding/offboarding | test tenant lifecycle |
| O4 | SLO/error budget/toil | dashboard e policy simulation |
| O5 | change/config management | emergency/normal change rehearsal |
| O6 | RuFlo/model upgrade lanes | dual-run rollback test |
| O7 | self-evolution proposal flow | rejected/adopted experiment simulation |
| O8 | cost/capacity forecast | scenario review |
| O9 | PRR | evidence complete/no veto |
| O10 | go-live/kill switch | full rehearsal |
| O11 | business continuity | degraded-mode game day |
| O12 | decommission drill tabletop | exit report |

---

## 23. Quality Gate L6 → L7

| ID | Criterio bloccante | Evidenza |
|---|---|---|
| C1 | service scope e tier espliciti | service definition |
| C2 | ogni area ha un accountable umano | RACI |
| C3 | on-call sostenibile e realistico | staffing/coverage |
| C4 | incident protocol e severity testati | tabletop/game day |
| C5 | SLO guida freeze e priorità | error budget simulation |
| C6 | tenant lifecycle completo | onboarding/offboarding receipt |
| C7 | RuFlo update non usa `latest` | upgrade lane/pin register |
| C8 | model/provider drift governato | model lifecycle |
| C9 | self-evolution non auto-promuove | change proposal policy |
| C10 | capacity/costo hanno forecast | scenario report |
| C11 | PRR ha owner e veto | signed readiness review |
| C12 | go-live è progressivo | rollout plan |
| C13 | kill switch non perde side effect incerti | reconciliation rehearsal |
| C14 | business continuity ordina recovery | degraded-mode report |
| C15 | toil ha soglia e freeze | dashboard/policy |
| C16 | agenti/skill hanno owner, expiry e kill switch | registri operativi |
| C17 | decommission è possibile | exit plan |
| C18 | approvazione umana | via esplicito |

**Soglia:** 18/18.

---

## 24. Autocritica del Livello 6

### Miglioramento rispetto a L5

- assegna responsabilità umane e impedisce accountability fittizia degli agenti;
- rende on-call compatibile con la dimensione del team;
- limita il pilot a R0/R1 e R2 selezionato, lasciando R3 disattivo;
- governa tenant, quote, supporto e offboarding;
- stabilisce lifecycle RuFlo e provider;
- converte self-evolution in proposta sperimentale controllata;
- lega costi, capacity, error budget e toil alle decisioni operative;
- definisce PRR, go-live, kill switch e decommission.

### Debolezze residue da risolvere nel Livello 7

1. Cloud, region e provider concreti restano parametrici.
2. Staffing reale e nomi degli owner non sono noti.
3. SLO pilot non sono ancora supportati da dati di produzione.
4. Le procedure richiedono implementazione e rehearsal effettivi.
5. Non esiste ancora un unico blueprint finale consolidato: le decisioni sono distribuite tra sette documenti.
6. Manca una matrice finale requisito→componente→file→test→owner.
7. Manca il Definition of Done definitivo per l’intero programma.
8. Non è ancora formalizzata la sequenza esatta post-L7 per creare Builder Swarm, memoria e codice.
9. Il volume documentale può diventare esso stesso rischio di manutenzione.
10. La produzione resta condizionata dal certification harness RuFlo e dai test reali.

### Punteggio comparativo

| Dimensione | L5 | L6 |
|---|---:|---:|
| Realismo | 9.7 | 9.8 |
| Operabilità | 8.8 | 9.6 |
| Governance | 8.7 | 9.6 |
| Release safety | 9.4 | 9.6 |
| Cost/capacity control | 8.5 | 9.3 |
| Evoluzione controllata | 6.8 | 9.1 |
| Production readiness | 8.8 | 9.2 |

**Verdetto:** L6 definisce un servizio realmente gestibile, ma non è ancora il documento esecutivo definitivo. L7 dovrà consolidare tutte le decisioni in un unico blueprint production, eliminare contraddizioni, tracciare ogni requisito e stabilire l’ordine esatto di costruzione e attivazione dello swarm.