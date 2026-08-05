import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Skill
SKILLS = []

BookNicheDecisionSkill = Skill(
    name="BookNicheDecisionSkill",
    owner_agents=["BookNicheDecisionLeader","BookNicheDecisionAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando enough data collected per valutare niche viability - books_found>0 review_sites>0 structured_output ready o feedback da AutoImprovement important_notes LearningLog""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Decide quali libri e nicchie target basato su market signals",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ResearchEcosystem', 'QualificationEcosystem', 'PlanningEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(BookNicheDecisionSkill)

QualificationDecisionSkill = Skill(
    name="QualificationDecisionSkill",
    owner_agents=["QualificationDecisionLeader","QualificationDecisionAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando tutti analyst evaluations completate - reproducibility_score absurdity_flag speed_estimate market_alignment plan_validity disponibili""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Decide GO NO-GO con weighted scoring 5 criteri reproducibili",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['QualificationEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(QualificationDecisionSkill)

SelfHealingSkill = Skill(
    name="SelfHealingSkill",
    owner_agents=["SelfHealingLeader","SelfHealingAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger any anomaly error stall incoherent output - 8 triggers missing output incoherent blocked failed validation empty result no-go without alternative memory write failure Playwright failure - always active DetectionTeam""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Rileva gestisce recupera fallimenti in qualsiasi fase - tras",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['all'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(SelfHealingSkill)

VideoStructureDesignSkill = Skill(
    name="VideoStructureDesignSkill",
    owner_agents=["VideoStructureDesignLeader","VideoStructureDesignAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando qualification GO package valido + risk_flags + need second-level plan - CONTROL POINT CP-VIDEO-01 handle_ambiguity preserve_and_encapsulate""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Progetta video_structure REQUIRED preservato verbatim - CRIT",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['PlanningEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(VideoStructureDesignSkill)

ChapterDesignSkill = Skill(
    name="ChapterDesignSkill",
    owner_agents=["ChapterDesignLeader","ChapterDesignAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger dopo video_structure presente verbatim validato via VideoStructureValidatorAgent""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Definisce capitoli con descrizioni ordine scopo effort estim",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['PlanningEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(ChapterDesignSkill)

SecondLevelPlanCoherenceSkill = Skill(
    name="SecondLevelPlanCoherenceSkill",
    owner_agents=["SecondLevelPlanCoherenceLeader","SecondLevelPlanCoherenceAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando second_level_plan draft completo""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Valida coerenza completezza second-level plan con video_stru",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['PlanningEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(SecondLevelPlanCoherenceSkill)

ProductionReadinessSkill = Skill(
    name="ProductionReadinessSkill",
    owner_agents=["ProductionReadinessLeader","ProductionReadinessAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando second_level_plan draft validato PlanCoherenceValidator""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Verifica prerequisiti produzione met stima risorse emette st",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['PlanningEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(ProductionReadinessSkill)

BookWritingConsistencySkill = Skill(
    name="BookWritingConsistencySkill",
    owner_agents=["BookWritingConsistencyLeader","BookWritingConsistencyAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando second_level_plan approvato production_start_signal TRUE + memory context required""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Mantiene consistenza con decisioni precedenti vincoli e cont",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ProductionEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(BookWritingConsistencySkill)

StyleEnforcementSkill = Skill(
    name="StyleEnforcementSkill",
    owner_agents=["StyleEnforcementLeader","StyleEnforcementAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger dopo chapter writing consistency check""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Garantisce stile uniforme scrittura cross-chapters",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ProductionEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(StyleEnforcementSkill)

GraphicPromptEngineeringSkill = Skill(
    name="GraphicPromptEngineeringSkill",
    owner_agents=["GraphicPromptEngineeringLeader","GraphicPromptEngineeringAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando manuscript ready + chapter content + graphic needs from details""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Crea prompt dettagliati per generazione grafiche coerenti co",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['VisualEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(GraphicPromptEngineeringSkill)

CoverConceptDesignSkill = Skill(
    name="CoverConceptDesignSkill",
    owner_agents=["CoverConceptDesignLeader","CoverConceptDesignAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando manuscript ready + market data + performance signals Amazon + review sites""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Crea cover concept basato su contenuto libro e market data p",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['VisualEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(CoverConceptDesignSkill)

PlaywrightNavigationSkill = Skill(
    name="PlaywrightNavigationSkill",
    owner_agents=["PlaywrightNavigationLeader","PlaywrightNavigationAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando search request o visual navigation request - usa PlaywrightOperationalTool navigate methods""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Gestisce navigazione reale Playwright su Amazon e review sit",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ResearchEcosystem', 'VisualEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(PlaywrightNavigationSkill)

PlaywrightDataExtractionSkill = Skill(
    name="PlaywrightDataExtractionSkill",
    owner_agents=["PlaywrightDataExtractionLeader","PlaywrightDataExtractionAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando navigation success + extraction request selectors""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Estrae dati reali da pagine via Playwright selectors - atomi",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ResearchEcosystem', 'VisualEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(PlaywrightDataExtractionSkill)

PlaywrightSaveSkill = Skill(
    name="PlaywrightSaveSkill",
    owner_agents=["PlaywrightSaveLeader","PlaywrightSaveAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando data_to_save ready destination ref""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Salva risultati sorgenti URL note materiali via Playwright s",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['ResearchEcosystem', 'VisualEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(PlaywrightSaveSkill)

MemoryReadWriteSkill = Skill(
    name="MemoryReadWriteSkill",
    owner_agents=["MemoryReadWriteLeader","MemoryReadWriteAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger ogni read/write request da qualsiasi ecosystem via MemoryManagementTeam connector""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Gestisce lettura scrittura memoria attiva con protocolli val",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['MemoryEcosystem', 'all'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(MemoryReadWriteSkill)

CheckpointManagementSkill = Skill(
    name="CheckpointManagementSkill",
    owner_agents=["CheckpointManagementLeader","CheckpointManagementAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger end_of_each_phase before_major_decision before_handoff on_self_healing_activation per chapter in production""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Crea memorizza ripristina checkpoint - core self-healing - c",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['MemoryEcosystem', 'SelfHealingEcosystem', 'all'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(CheckpointManagementSkill)

AnomalyDetectionSkill = Skill(
    name="AnomalyDetectionSkill",
    owner_agents=["AnomalyDetectionLeader","AnomalyDetectionAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger continuous monitoring all phase outputs completeness coherence process logs exception feed heartbeat feed""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Rileva anomalie errori stalli output incoerenti - DetectionT",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['SelfHealingEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(AnomalyDetectionSkill)

RecoveryExecutionSkill = Skill(
    name="RecoveryExecutionSkill",
    owner_agents=["RecoveryExecutionLeader","RecoveryExecutionAgent","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""trigger quando diagnosis report con recovery plan available - retry adjusted params timeout++ user_agent rotate rollback to checkpoint alternative path skip_and_log""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - Esegue recovery retry rollback alternative path validation -",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"},
    used_in_ecosystems=['SelfHealingEcosystem'],
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append(RecoveryExecutionSkill)

print(f'SKILLS EXPANDED: {len(SKILLS)} skills: '+str([s.name for s in SKILLS]))
