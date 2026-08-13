---
Type: TOOL
Status: Active
Tags: #apex7 #orchestration #quality-gates #adr-010 #adr-003
Created: 2026-08-13
Last updated: 2026-08-13
---

# APEX-7 Orchestration Layer

Sottopacchetto di `11-APEX-7-CORE` — il motore canonico della Coordination Fabric
(ADR-010). Aggiunge attorno al `RuFLOOrchestrator` esistente una catena di stato
crittografica e sette quality gate che **bloccano davvero**.

Non sostituisce nulla e non riscrive nulla: `orchestrator/ruflo_core.py` resta
byte per byte com'era (ADR-003, wrap mai riscrittura). Tutto quello che serviva
in piu' — la DLQ del bus, la tolleranza agli errori di stampa — vive qui dentro
come strumentazione, non come patch al motore.

## Uso

```python
from orchestration import OrchestrationPipeline

esito = OrchestrationPipeline(orchestrator, memory).run_sync(
    "progetta il carosello Preventa",
    required_fields=["brand"],
    quality_threshold=7.5,
)

print(esito.ledger.render())   # scorecard L1→L7, letta dai risultati veri
if not esito.certified:
    print("bloccato a:", esito.blocked_at)
```

## I sette livelli

| Livello | Cosa verifica | Soglia |
|---|---|---|
| **L1** FOUNDATION | catena Merkle intatta, campi obbligatori, numeri finiti, niente `None` non dichiarati | 100% |
| **L2** DAG | grafo aciclico, nodi critici utilizzabili, nessun `FAILED`/`BLOCKED`, nessun NaN/Inf | 90% |
| **L3** BUS_MEMORY | DLQ vuota, nessuna consegna fallita in silenzio, contratto memoria, round-trip working memory | 85% |
| **L4** SWARM | ruoli richiesti registrati, output non vuoto, contratto di handoff, **output non tutto mock** | 85% |
| **L5** QUALITY | audit eseguiti, nessun CRITICAL, score sopra soglia, (se dichiarata) distribuzione calibrata al 100% | 90% |
| **L6** EVOLUTION | guardia interrogata davvero, invarianti intoccati, rollback sulle regressioni | 100% |
| **L7** APEX | **L1..L6 tutti eseguiti e passati**, SLA, DLQ, self-healing risolto, catena ancora intatta | 100% |

## Le tre regole di casa

1. **Nessun punto regalato.** Ogni `GateCheck` nasce da un predicato su dati reali.
   Se una condizione non si applica al run, il check **non viene emesso** — non
   viene emesso "passato". Un gate che si auto-assegna credito misura se stesso.
2. **Passare richiede zero fallimenti.** `GateResult.build` pretende soglia
   raggiunta *e* tutti i check verdi: nessun 6/7 spacciato per certificazione.
3. **La rendicontazione si legge dal registro.** `GateLedger.render()` costruisce
   la scorecard dagli esiti veri e stampa `NON CERTIFICATO` con l'elenco dei gate
   mai eseguiti. Non esiste una stringa "100% PASS" da nessuna parte.

## Origine: audit dello zip `apex7_orchestrator` (2026-08-13)

Lo zip conteneva 5.591 file: un clone di `ruvnet/claude-flow` (~5.100 file, mai
importato), tre copie dello stesso codice Python e ~1.500 righe di layer vero.
Dichiarava `100% PASS (Tolleranza Zero L1-L7)`. Fatto girare, non reggeva.

**Preso** (le idee che valevano): catena di stato Merkle, DAG con circuit
breaker, DLQ sul bus, framework dei gate a livelli, guardia di auto-evoluzione,
self-healing tracciato.

**Scartato**: il clone di claude-flow; i moduli finanziari (il layer serve a
orchestrare, non a calcolare rendimenti); i 6 "agenti swarm" che restituivano
dizionari scritti a mano con `confidence: 0.95` fisso; il generatore di report;
i path `/home/user` cablati.

**Corretto** — ogni difetto ha un test `REGRESSIONE` in `test_orchestration.py`:

| Difetto nello zip | Qui |
|---|---|
| `GateL6` importato in `pipeline.py:25` e **mai chiamato**: il run certificava con 6 gate su 7 | L6 eseguito dalla pipeline; `gate_l6_evolution([])` fallisce se la guardia non e' stata interrogata |
| `GATE_L7` controllava solo L1..L5: L6 assente non era rilevabile | `REQUIRED_GATE_IDS` copre L1..L6; C7.1 fallisce sui gate mai eseguiti |
| `checks += 1` incondizionato in L1/L3/L4/L6 (~1 punto su 5 regalato, 2 su 5 in L6) | ogni check e' un predicato; i check inapplicabili non vengono emessi |
| `"Certificazione: 100% PASS L1-L7"` era una stringa fissa nel generatore di report | `GateLedger.render()` legge dai risultati e dichiara i gate mancanti |
| Swarm simulato con dict hardcoded, e i gate lo certificavano | C4.5 fallisce se l'output e' interamente `mock: True` |
| Input assurdi certificati (rendimento 500%, capitale finale **negativo**, inflazione −50%) | L1 valida i campi dichiarati; L5 blocca su audit CRITICAL, soglia e calibrazione |
| Nodi con dipendenze fallite sparivano dai risultati, e il gate vedeva un grafo "completo" | stato `BLOCKED` esplicito; C2.5 fallisce |
| Cicli nel grafo scoperti dopo 20 iterazioni a vuoto | `topological_order` solleva `DAGCycleError` **prima** di eseguire |
| SLA documentato `<500ms`, codice che controllava `<5000ms` | `DEFAULT_SLA_MS = 500.0`, configurabile per run |

## Difetti del motore condiviso — trovati qui, NON corretti qui

Emersi facendo girare l'innesto contro `orchestrator/ruflo_core.py`. Il motore e'
condiviso da YouTube, carousel-machine, skill-forge e cold-outreach: si tocca in
un ciclo dedicato, non di straforo. Tracciati in `company/Memory/BACKLOG.md`,
fissati da `TestDifettiDelMotore` (che li dimostra senza innescarli).

1. **`execute_workflow` cade su console Windows** — `print(f"[FLOW] → {stage}")`
   solleva `UnicodeEncodeError` su stdout cp1252, nel percorso principale.
   Contenuto qui da `stdout_tollerante()`.
2. **Ricorsione infinita sotto score 4.0** — `execute_workflow` genera un
   `task_id` nuovo a ogni restart, quindi `DynamicWorkflowRouter.loop_count` non
   accumula mai e il workflow riparte per sempre. Contenuto qui: la pipeline lo
   intercetta come guasto e blocca a L4 invece di appendersi.
3. **`EventBus` inghiotte le eccezioni degli handler in un `print`** — nessuna
   traccia ispezionabile. Risolto qui da `InstrumentedEventBus`, che aggiunge
   `failed_deliveries` e `dead_letter_queue` per sottoclasse.

## File

```
orchestration/
├── contracts.py   StateSnapshot (Merkle) · GateCheck · GateResult · GateBlocked
├── dag.py         topological_order · DAGEngine · circuit breaker · NodeResult
├── bus.py         InstrumentedEventBus · instrument() — DLQ senza toccare il motore
├── gates.py       i 7 gate · QualityReport · AuditFinding · Outcome · GateLedger
├── healing.py     SelfHealingEngine · HealingAction
├── evolution.py   SelfEvolutionSafetyGuard · EvolutionExperiment
└── pipeline.py    OrchestrationPipeline · RunSpec · PipelineResult
```

## Test

```bash
cd company/Ecosistemi/11-APEX-7-CORE
python test_orchestration.py      # 46 test
python test_multi_tenant.py       # 4 test preesistenti, invariati
```

## Connessioni

- [[ADR-010-fusione-ruflo-apex7]] — perche' l'innesto sta qui e non altrove
- [[ADR-003-migrazione-wrap-non-riscrittura]] — perche' il motore non e' stato toccato
- [[ADR-005-backlog-non-blocca]] — perche' i difetti del motore sono in BACKLOG
