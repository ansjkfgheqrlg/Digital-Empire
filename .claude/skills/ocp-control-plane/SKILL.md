---
name: ocp-control-plane
description: "Attiva e verifica OCP (Orchestration Control Plane), lo strato di GOVERNANCE/policy per workflow multi-agente in company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/ (ADR-012). NON è il motore che esegue gli agenti (quello resta RuFLO/orchestrator/ruflo_core.py e lo swarm APEX-7 in agents/) — OCP decide SE e COME un workflow può girare: contratti JSON Schema, budget/side-effect prima dell'esecuzione, policy OPA/Rego default-deny, grant single-use per gli strumenti, Plan Memory a citazione obbligatoria. Usa quando l'utente dice 'attiva OCP', 'verifica il control plane', '/ocp-control-plane', o chiede dello strato di governance portato da Neri da Antigravity — NON per richieste generiche su 'l'orchestration layer' senza altro contesto, in quel caso chiedi quale dei sistemi (APEX-7 swarm, RuFLO core, OCP) intende."
---

# /ocp-control-plane

Attiva ed esegue una verifica reale di **OCP** (Orchestration Control Plane),
in `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/` (ADR-012).

## Cos'è OCP e a cosa serve — perché non è "l'orchestration layer" generico

Digital Empire ha **più sistemi che orchestrano agenti**, con ruoli diversi.
Prima di eseguire qualunque azione, sappi distinguerli:

| Sistema | Cartella | Cosa fa |
|---|---|---|
| **APEX-7 swarm** | `11-APEX-7-CORE/agents/`, `orchestration/` (bus, dag, gates, healing, pipeline) | ESEGUE il workflow: planner→writer/analyst→critic→refiner→meta. È il motore attivo, agganciato oggi a `calc/engine.py`, `arena_generator.py`, `main.py`. |
| **RuFLO core** | `11-APEX-7-CORE/orchestrator/ruflo_core.py` | EventBus, PriorityQueue, DynamicWorkflowRouter — il "cuore" async su cui gira lo swarm APEX-7. |
| **OCP (questo comando)** | `11-APEX-7-CORE/orchestration-layer/` | **Non esegue niente da solo.** Decide SE un workflow è autorizzato a girare (policy OPA/Rego default-deny), valida i suoi contratti PRIMA che parta (JSON Schema su comandi/piani/budget/side-effect), emette grant single-use per gli strumenti (nessun replay), tiene una memoria dei piani con citazione obbligatoria (niente risposta senza fonte verificabile), e ha un bridge che punta a certificare RuFLO stesso (`ruflo_bridge/`, pinnato a `ruflo@3.38.19`, non ancora certificato in questo ambiente). |

**In una frase**: OCP è il cancello di governance che, quando la Fase 2 di
ADR-012 sarà fatta, si metterà DAVANTI ad APEX-7/RuFLO per autorizzarli — oggi
non è ancora collegato a nessun consumatore reale.

Se l'utente chiede genericamente di "attivare l'orchestration layer" senza
specificare, **chiedi quale dei tre** prima di agire — non assumere che
intenda OCP.

## Cosa fa questo comando, in ordine — eseguilo direttamente, non delegare a un subagent

Tutte operazioni locali, deterministiche, nessun side-effect esterno (nessun
Postgres/OPA/RuFlo reale, nessuna rete) — nessuna conferma da chiedere.

1. **Sanity check ambiente**: verifica che non ci sia un install pip editable
   orfano che collide col nome `orchestrator` (problema reale trovato in
   CP-20260826-001, non specifico di OCP ma che rompe i suoi vicini):
   ```
   pip show orchestration-layer
   ```
   Se risulta installato E il suo `Location`/`Editable project location` NON è
   `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer`, disinstallalo
   (`pip uninstall -y orchestration-layer`) prima di andare oltre.

2. **Test suite completa di OCP**:
   ```
   cd "company/Ecosistemi/11-APEX-7-CORE/orchestration-layer"
   PYTHONPATH=src python -m unittest discover -s tests
   ```
   Atteso: ~148 test verdi, ~11 skip (richiedono Postgres/OPA/RuFlo reali, non
   presenti in locale — è normale, non è un fallimento).

3. **Attivazione vera — benchmark deterministico W9** (prova che il piano di
   valutazione locale gira, non solo che i moduli si importano):
   ```
   PYTHONPATH=src python -m benchmarks.cli --output quality/benchmarks/w9-baseline.json
   ```
   Leggi il JSON di output e riporta i 6 hard gate (`behavior_accuracy_1_0`,
   `quality_pass_1_0`, `evidence_pass_1_0`, `concurrent_completion_20_20`,
   `memory_recall_at_5_gte_0_95`, `citation_accuracy_1_0`). Se anche uno è
   `false`, segnalalo chiaramente — non è un'attivazione riuscita.

4. **Verifica che APEX-7/RuFLO (i motori che OCP dovrà un giorno governare)
   non si siano rotti** — OCP e loro coesistono, non condividono ancora nulla:
   ```
   cd "company/Ecosistemi/11-APEX-7-CORE"
   python -m unittest test_orchestration test_calc test_multi_tenant
   ```
   Atteso: verdi (92 test all'ultima verifica nota).

## Come riportare il risultato

Una riga di stato per ciascuno dei 4 passi (OK/FAIL con motivo), poi un
riepilogo che nomina esplicitamente i sistemi:
- **OCP (governance)**: ATTIVO / hard gate falliti (elenco)
- **APEX-7 swarm + RuFLO core (esecuzione)**: INVARIATI / rotti (se rotti:
  **fermati, non toccare nulla altro**, ADR-003)
- Promemoria stato reale (da ADR-012): OCP non governa ancora nessun
  consumatore reale (`calc/engine.py`, `arena_generator.py`, `main.py` restano
  fuori dal suo perimetro); il bridge verso RuFLO non è certificato in questo
  ambiente (richiede `npm install` dentro `orchestration-layer/ruflo_bridge/`,
  mai eseguito).

## Cosa NON fare

- Non lanciare `local_slice_cli` (richiede un binario OPA pinnato esterno,
  `OPA_BIN`, non presente) né i test che richiedono Postgres reale — restano
  skip, per design.
- Non archiviare/spostare `orchestrator/`+`orchestration/` (APEX-7/RuFLO) in
  questo comando: quello è Fase 2 di ADR-012, decisione esplicita ancora da
  prendere con Neri/Max.
- Non installare nulla globalmente (niente `pip install` fuori dal progetto)
  oltre alla disinstallazione dell'editable orfano al passo 1.
- Non rispondere a "attiva l'orchestration layer" generico eseguendo questo
  comando in automatico — disambigua prima (vedi tabella sopra).
