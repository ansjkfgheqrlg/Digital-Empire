
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Skill

PlaywrightNavigationSkill = Skill(
    name="PlaywrightNavigationSkill",
    owner_agents=['PlaywrightNavigationLeader', 'PlaywrightNavigationAgent', 'SupremeOrchestratorAgent', 'MemoryManagerLeader', 'SelfHealingEcosystemController'],
    trigger_condition="""trigger quando search request o visual navigation request - usa PlaywrightOperationalTool navigate methods""",
    execution_steps=['1. Riceve trigger condition valida con input necessari disponibili', '2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Gestisce navigazione reale Playwright su Amazon e review sit', '3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error', '4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)', '5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag', '6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking', '7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes'],
    success_criteria="""Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills""",
    failure_handling="""Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido""",
    retry_logic={'max_retries': 3, 'retry_strategy': ['retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread', 'rollback a ultimo checkpoint valido via CheckpointManagerAgent', 'escalate flag anomaly pause branch log important_notes', 'skip_and_log broken step log continua dove possibile solo non-critical', 'requalify rimanda a qualification con anomaly flag'], 'checkpoint': 'SelfHealingCheckpoint before after each retry', 'memory_integration': 'reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes'},
    used_in_ecosystems=['ResearchEcosystem', 'VisualEcosystem'],
    hierarchy_levels=[1, 2, 3, 4, 5, 6, 7]
)

print(f"Skill dedicated file PlaywrightNavigationSkill - owners {len(PlaywrightNavigationSkill.owner_agents)} - trigger {'PlaywrightNavigationSkill'}")
