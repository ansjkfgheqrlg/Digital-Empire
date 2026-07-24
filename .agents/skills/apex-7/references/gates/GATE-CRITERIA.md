# GATE CRITERIA — 20 Criteri su 7 Livelli

> Sistema completo di quality gating con zero tolleranza ai livelli safety e APEX.

---

## Gate Universali (G0-G4) — Applicabili a Tutti i Livelli

| ID | Criterio | Domanda di Verifica | Tipo |
|---|---|---|---|
| **G0** | Goal Alignment | L'output risponde all'obiettivo dell'utente? | Binario |
| **G1** | Completeness | L'output è completo? (nessun "[...]" o "ecc." o placeholder) | Binario |
| **G2** | Internal Coherence | L'output è coerente internamente senza contraddizioni? | Binario |
| **G3** | Usability | L'output è immediatamente usabile da un agente/umano? | Binario |
| **G4** | CRITIC Approval | Il CRITIC ha dato PASS con score ≥ 8.0? | Soglia |

---

## Gate Specifici per Livello

### Livello 1→2 — Componenti Base (Soglia: ≥ 0.80)

| ID | Criterio | Domanda |
|---|---|---|
| **GL1** | Component Definitions | Tutti i componenti base sono definiti completamente? |
| **GL2** | Single Responsibility | Ogni componente ha una e una sola responsabilità? |
| **GL3** | Interface Definitions | Le interfacce tra componenti sono definite esplicitamente? |

### Livello 2→3 — Struttura e Feedback (Soglia: ≥ 0.80)

| ID | Criterio | Domanda |
|---|---|---|
| **GL4** | Feedback Loop Documented | Il feedback loop è documentato e completo (input→process→output→feedback)? |
| **GL5** | Max Iterations Defined | Il numero massimo di iterazioni è definito per prevenire loop infiniti? |
| **GL6** | Routing Conditions | Le condizioni di routing sono specifiche e non ambigue? |

### Livello 3→4 — Parallelismo e Resilienza (Soglia: ≥ 0.83)

| ID | Criterio | Domanda |
|---|---|---|
| **GL7** | Race Condition Free | La parallelizzazione è sicura? Nessuna race condition possibile? |
| **GL8** | Checkpoints Defined | I checkpoint di salvataggio stato sono definiti? |
| **GL9** | Rollback Possible | Il rollback a uno stato precedente è possibile e documentato? |

### Livello 4→5 — Meta-Visibilità (Soglia: ≥ 0.80)

| ID | Criterio | Domanda |
|---|---|---|
| **GL10** | Meta Visibility | Il Meta Agent ha visibilità completa su tutti i componenti? |
| **GL11** | Quality Scoring Calibrated | Il quality scoring è calibrato con pesi documentati e giustificati? |
| **GL12** | Pattern Thresholds | Le soglie di pattern detection sono definite numericamente? |

### Livello 5→6 — Safety — ⚠️ ZERO TOLLERANZA (Soglia: ≥ 1.00)

| ID | Criterio | Domanda |
|---|---|---|
| **GL13** | Evolution Stability | La self-evolution non causa instabilità? Testato su 3+ run? |
| **GL14** | Human Override | Human override è sempre possibile in qualsiasi momento? |
| **GL15** | Safety Limits | I limiti di sicurezza sono definiti esplicitamente (max tokens, max runtime, max cost)? |

### Livello 6→7 — APEX — ⚠️ ZERO TOLLERANZA (Soglia: ≥ 1.00)

| ID | Criterio | Domanda |
|---|---|---|
| **GL16** | All Previous Gates | Tutti i gate L1→L6 sono stati superati con score appropriato? |
| **GL17** | End-to-End Test | Un test end-to-end è stato completato con successo? |
| **GL18** | Performance ≥ 150% | La performance è ≥ 150% rispetto alla baseline documentata? |
| **GL19** | Memory Consistency | La consistenza della memoria è stata verificata su tutti i 5 layer? |
| **GL20** | Self-Healing Demonstrated | Il self-healing è stato dimostrato con un test di fallimento reale? |

---

## Scoring Formula

```
Per ogni criterio:
  PASS    = 1.0
  PARTIAL = 0.5
  FAIL    = 0.0

gate_score = Σ(criterion_score) / total_criteria
```

### Thresholds

| Gate | Soglia PASS | Tolleranza |
|---|---|---|
| L1→L2 | ≥ 0.80 | Standard (8 criteri: G0-G3 + GL1-GL3 + G4) |
| L2→L3 | ≥ 0.80 | Standard (+ GL4-GL6) |
| L3→L4 | ≥ 0.83 | Standard (+ GL7-GL9) |
| L4→L5 | ≥ 0.80 | Standard (+ GL10-GL12) |
| L5→L6 | ≥ **1.00** | **ZERO** (+ GL13-GL15) |
| L6→L7 | ≥ **1.00** | **ZERO** (+ GL16-GL20) |

---

## Remediation Protocol

```
SE gate_score < threshold:
  1. Identifica criteri FAIL e PARTIAL
  2. Per ogni FAIL: genera fix instruction specifica
  3. Per ogni PARTIAL: suggerisci completamento
  4. Invia remediation list a REFINER (o WRITER se nessun REFINER)
  5. Incrementa tentativo
  6. SE tentativo = 3: ESCALATE a META AGENT

SE gate_score ≥ threshold:
  GATE PASSED ✓ — Avanza al livello successivo
```

---

## Safety Gate Special Rules

```
Per L5→L6 e L6→L7 (soglia 1.00):
  → Qualsiasi FAIL su GL13-GL15 o GL16-GL20 = GATE FAILED
  → Non esiste PARTIAL per i safety gates
  → Ogni criterio è binario: PASS o FAIL
  → Se FAIL su GL13 o GL14: STOP IMMEDIATO, escalation a human OBBLIGATORIA
  → Se FAIL su GL18: richiedi test di performance documentato
```
