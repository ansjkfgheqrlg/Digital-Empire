# Stage 5: Meta Review

## Obiettivo
Analisi di sistema, pattern detection ed evoluzione periodica.

## Agente Responsabile
**META AGENT** (AG-08)

## Attivazione
- Ogni 3 cicli completi (routine)
- Gate fallito 3x
- CRITIC RESTART
- REFINER non risolve dopo 3 cicli
- Agente timeout 2x
- Richiesta ORCHESTRATOR

## Processo (5 Step)

### M1 — System Health Check
Per ogni agente: qualità output, criteri successo, pattern fallimento, consistenza.
Per il workflow: efficienza, colli bottiglia, loop, gate.
Per la memoria: uso, qualità dati, consistenza.

### M2 — Pattern Detection
- Pattern di fallimento ricorrenti
- Pattern di successo
- Pattern di inefficienza
- Pattern di miglioramento

### M3 — Root Cause Analysis
Per ogni pattern negativo:
- Causa radice: prompt? workflow? threshold? contesto?

### M4 — Intervention Decision
- **Tipo A (MICRO)**: modifiche localizzate, fix immediato
- **Tipo B (MACRO)**: modifiche sistemiche, restructuring
- **Tipo C (HUMAN)**: oltre la capacità del sistema

### M5 — Evolution Opportunity
- Strategie da codificare
- Anti-pattern da registrare
- Threshold da ricalibrare
- Prompt da ottimizzare

## Output
System Analysis Report:
- System Health table (🟢🟡🔴 per agente)
- Pattern identificati (positivi e negativi)
- Root Cause Analysis
- Intervento deciso (Tipo A/B/C)
- Evolution opportunities
- Memory updates
- Next recommended action

## Post-Actions
1. Eseguire memory updates su tutti i layer
2. Applicare micro-interventions automaticamente
3. Proporre macro-interventions all'utente
4. Se ADOPT evolution: aggiornare variabile, creare Architecture Snapshot
5. Emetti `meta.analysis.completed`

## Next Stage
→ Stage 6: Final Output
