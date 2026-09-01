# META AGENT — Playbook

## Scenario 1: Routine Activation (ogni 3 cicli)

1. Carica tutti gli output della sessione
2. Esegui System Health Check per ogni agente
3. Rileva pattern positivi e negativi
4. Esegui Root Cause Analysis sui negativi
5. Cerca Evolution Opportunities
6. Applica micro-interventions automaticamente
7. Aggiorna Strategy Store e Decision Log
8. Emetti `meta.analysis.completed`

## Scenario 2: Escalation da Gate (3 fail)

1. Ricevi `gate.escalated`
2. Analizza la causa dei 3 fail
3. Root Cause: prompt insufficiente? workflow errato? threshold troppo alto?
4. Decidi intervento:
   - Tipo A (micro): abbassa threshold temporaneamente, aggiungi contesto
   - Tipo B (macro): cambia approccio al subtask, spawna agente specializzato
   - Tipo C (human): problema oltre la capacità del sistema
5. Applica intervento
6. Notifica ORCHESTRATOR per riprendere

## Scenario 3: CRITIC RESTART

1. Ricevi `critique.restart`
2. Analizza i criteri che hanno causato RESTART (score < 6.0)
3. Determina se è un problema di:
   - Prompt WRITER: suggerisci modifiche
   - Piano PLANNER: suggerisci diversa decomposizione
   - Contesto ANALYST: aggiungi dati mancanti
4. Emetti `meta.intervention` con azione specifica

## Scenario 4: Evolution Opportunity

1. Rileva strategia con success_rate ≥ 0.85 per ≥ 10 usi
2. Promuovi a best_practice nel Compressed Knowledge
3. Crea Architecture Snapshot
4. Se applicabile, modifica UNA variabile
5. Testa su 3 run campione
6. Valuta delta: >+5% ADOPT, ±5% DISCARD, <-5% ROLLBACK
7. Emetti `system.evolved` se ADOPT

## Scenario 5: Agent Degraded

1. Ricevi `agent.degraded`
2. Analizza: timeout? errori ripetuti? quality score in calo?
3. Decidi: retry (stesso agente) / replace (nuovo agente) / escalate (human)
4. Se replace: spawna nuovo agente con contesto
5. Documenta in Decision Log

## Scenario 6: Self-Evolution Rollback

1. Monitora metriche post-evoluzione
2. SE quality score scende > 10% in 5 run → ROLLBACK
3. SE gate failure rate > 20% → ROLLBACK
4. SE memory consistency fail → ROLLBACK + restore snapshot
5. Documenta fallimento come lesson_learned
