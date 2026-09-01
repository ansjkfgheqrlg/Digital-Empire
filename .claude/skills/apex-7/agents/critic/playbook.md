# CRITIC — Playbook

## Scenario 1: Prima Valutazione

1. Ricevi draft da WRITER
2. STEP C1: leggi intero output senza giudicare
3. STEP C2: rileggi marcando BLOCCANTI, MIGLIORATIVI, STILISTICI
4. STEP C3: assegna score per ognuna delle 5 dimensioni
5. STEP C4: calcola weighted_total
6. STEP C5: determina verdict
7. STEP C6: produci fix proposals specifici
8. Emetti `critique.completed` con routing

## Scenario 2: Re-Valutazione Post-Refinement

1. Ricevi draft raffinato da REFINER
2. Incrementa contatore ciclo
3. Valuta di nuovo sulle 5 dimensioni
4. Verifica che i BLOCCANTI precedenti siano risolti
5. Controlla che i punti forti siano stati preservati
6. SE dopo 3 cicli ancora REFINE → emetti `critique.restart`

## Scenario 3: PASS con Riserva

1. weighted_total ≥ 8.0
2. Ma hai identificato MIGLIORATIVI non critici
3. Verdict = PASS
4. Includi comunque i migliorativi nel report
5. REFINER li applicherà opzionalmente

## Scenario 4: RESTART

1. weighted_total < 6.0
2. L'output ha problemi strutturali, non solo di dettaglio
3. Verdict = RESTART
4. Fornisci contesto dettagliato del PERCHÉ
5. Suggerisci nuovo approccio a PLANNER
6. Emetti `critique.restart`

## Scoring Edge Cases

- Score 10/10: richiede dichiarazione esplicita e motivazione
- Due dimensioni con score < 5.0: RESTART automatico
- BLOCCANTE non risolto: REFINE anche se weighted_total ≥ 8.0
- PARTIAL su G0 (goal alignment): REFINE obbligatorio
