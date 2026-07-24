# Stage 4: Gate Check

## Obiettivo
Verificare che l'output soddisfi tutti i criteri di qualità del livello corrente.

## Agente Responsabile
**GATE AGENT** (AG-07)

## Input
- Output da verificare
- Livello corrente (1-6)
- Storico gate della sessione

## Processo (4 Step)

### G1 — LOAD
- Caricare output
- Caricare criteri per livello corrente
- Caricare storico gate

### G2 — EVALUATE
Per ogni criterio applicabile:
- Cercare evidenza nell'output
- Assegnare PASS / PARTIAL / FAIL
- Citare evidenza per ogni PASS

### G3 — SCORE
```
gate_score = (PASS*1.0 + PARTIAL*0.5) / total_criteria
```

Thresholds:
- L1→L2: ≥ 0.80
- L2→L3: ≥ 0.80
- L3→L4: ≥ 0.83
- L4→L5: ≥ 0.80
- L5→L6: ≥ 1.00 (ZERO TOLLERANZA)
- L6→L7: ≥ 1.00 (ZERO TOLLERANZA)

### G4 — DECISION
- gate_score ≥ threshold: GATE PASSED
- gate_score < threshold: GATE FAILED → remediation
- 3° fail: ESCALATE → META AGENT

## Safety Gates Special Rules

L5→L6 e L6→L7:
- Ogni criterio è binario: PASS o FAIL
- Qualsiasi FAIL = GATE FAILED
- FAIL su GL13 o GL14 = STOP IMMEDIATO, escalation HUMAN

## Output
Gate Report formattato con:
- Gate ID (L{N}→L{N+1})
- Tentativo (N di 3)
- Tabella criteri con status e evidenza
- Gate score
- Verdict (PASSED/FAILED)
- Remediation list (se FAILED)

## Post-Actions
1. Memory.WRITE in Decision Log
2. Emetti `gate.passed` o `gate.failed`
3. Se passed: notifica ORCHESTRATOR per avanzamento
4. Se failed (1a/2a): remediation a REFINER
5. Se failed (3a): `gate.escalated` a META AGENT
6. Se safety fail: STOP + HUMAN

## Next Stage
- PASSED: Stage 5 (Meta Review) o Stage 6 (Final Output)
- FAILED (1-2): REFINER → Stage 4 again
- FAILED (3): META AGENT
