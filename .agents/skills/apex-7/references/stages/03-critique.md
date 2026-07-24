# Stage 3: Critique Loop

## Obiettivo
Valutare il draft su 5 dimensioni, determinare se PASS, REFINE o RESTART.

## Agenti Coinvolti
- **CRITIC** (AG-05) — Valutazione primaria
- **REFINER** (AG-06) — Se REFINE (condizionale)

## Max Iterazioni
**3 cicli** REFINE→CRITIC. Poi ESCALATE a META AGENT.

## Processo CRITIC

### C1 — Prima Lettura
Leggere l'intero output senza giudicare.

### C2 — Seconda Lettura (matita rossa)
Marcare BLOCCANTI, MIGLIORATIVI, STILISTICI.

### C3 — Scoring
Assegnare score 0-10 (granularità 0.5) per:
- Completezza (25%)
- Precisione (25%)
- Actionability (20%)
- Coerenza Interna (20%)
- Efficacia vs Obiettivo (10%)

### C4 — Weighted Total
Calcolare weighted_total.

### C5 — Verdict
- ≥ 8.0: PASS
- 6.0-7.9: REFINE
- < 6.0: RESTART
- BLOCCANTI presenti: REFINE (minimo)

### C6 — Fix Proposals
Per ogni problema: fix SPECIFICO (cita sezione e parametri).

## Processo REFINER (se attivato)

### R1 — Lettura Critica
Capire ogni problema in profondità.

### R2 — Priority Order
1. BLOCCANTI
2. MIGLIORATIVI ad alto impatto
3. MIGLIORATIVI a basso impatto

### R3 — Surgical Fixing
- Identificare sezione esatta
- Applicare fix minimo
- Verificare non rompa altro
- Documentare modifica

### R4 — Consistency Check
Verificare coerenza globale dopo i fix.

### R5 — Self-Critique
Rileggere come CRITIC: tutti i BLOCCANTI risolti?

## Routing

```
VERDICT = PASS
  → Stage 4 (Gate Check)

VERDICT = REFINE
  → REFINER → Torna a CRITIC (max 3 iterazioni totali)

VERDICT = RESTART
  → Stage 1 (nuovo piano con contesto fallimento)

ITERAZIONI = 3 e ancora REFINE
  → META AGENT (escalation)
```

## Output
- CRITIC: Critique Report con score table, problemi, verdict
- REFINER (se attivato): Change log, refined draft, self-assessment

## Post-Actions
1. Memory.WRITE in Decision Log
2. Emetti `critique.completed` (con sub-evento: pass/refine/restart)
3. Routing automatico in base al verdict

## Criteri di Completamento
- [x] Tutte le 5 dimensioni valutate
- [x] Weighted total calcolato
- [x] Verdict determinato
- [x] Fix proposals specifici per ogni problema
- [x] Punti forti identificati e preservati
- [x] Se REFINE: modifiche documentate con change log
