import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

DataFormatterAgent = Agent(
    name="DataFormatterAgent",
    role="Formatta dati per storage via Playwright save strutturato per qualifica L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support DataFormatterAgent in DataPersistenceTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

SaveValidatorAgent = Agent(
    name="SaveValidatorAgent",
    role="Conferma salvataggi Playwright successo URL sorgente loggata raw_data accessibile L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support SaveValidatorAgent in DataPersistenceTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ReviewScoreNormalizerAgent = Agent(
    name="ReviewScoreNormalizerAgent",
    role="Normalizza diversi scoring systems in formato unificato L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ReviewScoreNormalizerAgent in ReviewAnalysisResearchTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

AmazonResultsValidatorAgent = Agent(
    name="AmazonResultsValidatorAgent",
    role="Valida dati Amazon estratti completi coerenti titolo URL sorgente keyword L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support AmazonResultsValidatorAgent in AmazonKeywordResearchTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ReviewDataValidatorAgent = Agent(
    name="ReviewDataValidatorAgent",
    role="Valida completezza coerenza review data linkata a book opportunities L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ReviewDataValidatorAgent in ReviewAnalysisResearchTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

FinalApprovalAgent = Agent(
    name="FinalApprovalAgent",
    role="Da approvazione finale produzione manoscritto completo validato L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support FinalApprovalAgent in ProductionQualityTeam ProductionEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

VisualPlaywrightSaveAgent = Agent(
    name="VisualPlaywrightSaveAgent",
    role="Salva output visual via Playwright support operational L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support VisualPlaywrightSaveAgent in VisualPlaywrightOperationsTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

GraphicQualityReviewerAgent = Agent(
    name="GraphicQualityReviewerAgent",
    role="Revisiona qualità grafiche generate score pass fail loop revisione L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support GraphicQualityReviewerAgent in GraphicDesignTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CoverQualityReviewerAgent = Agent(
    name="CoverQualityReviewerAgent",
    role="Revisiona qualità cover critica pass fail non skippabile L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CoverQualityReviewerAgent in CoverDesignTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

HierarchyManagerAgent = Agent(
    name="HierarchyManagerAgent",
    role="Mantiene dati gerarchia 7 livelli agent_id name level team ecosystem reports_to manages L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support HierarchyManagerAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ImportantNotesAgent = Agent(
    name="ImportantNotesAgent",
    role="Memorizza recupera note critiche flags - importante L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ImportantNotesAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

PerformanceMetricsAgent = Agent(
    name="PerformanceMetricsAgent",
    role="Calcola metriche performance per fase - feedback 6 segnali L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support PerformanceMetricsAgent in FeedbackCollectionTeam AutoImprovementEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

PatternDetectorAgent = Agent(
    name="PatternDetectorAgent",
    role="Rileva pattern ricorrenti positivi negativi keyword too slow GO rate low L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support PatternDetectorAgent in FeedbackCollectionTeam AutoImprovementEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ImprovementPlanWriterAgent = Agent(
    name="ImprovementPlanWriterAgent",
    role="Scrive improvement plans prioritizzati L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementPlanningSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ImprovementPlanWriterAgent in ImprovementPlanningTeam AutoImprovementEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ThresholdUpdaterAgent = Agent(
    name="ThresholdUpdaterAgent",
    role="Aggiorna soglie decisionali basate su learning GO threshold 70 L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementExecutionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ThresholdUpdaterAgent in ImprovementExecutionTeam AutoImprovementEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

WorkflowOptimizerAgent = Agent(
    name="WorkflowOptimizerAgent",
    role="Ottimizza sequenze flow basate su dati performance L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementExecutionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support WorkflowOptimizerAgent in ImprovementExecutionTeam AutoImprovementEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

MemoryValidatorAgent = Agent(
    name="MemoryValidatorAgent",
    role="Valida consistenza memoria rileva corruzione gaps - sistema attivo L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support MemoryValidatorAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CheckpointManagerAgent = Agent(
    name="CheckpointManagerAgent",
    role="Gestisce checkpoint creation storage restoration - core self-healing L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CheckpointManagerAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

DecisionLoggerAgent = Agent(
    name="DecisionLoggerAgent",
    role="Logga decisioni con full context reasoning immutable append-only L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support DecisionLoggerAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

PlanStorageAgent = Agent(
    name="PlanStorageAgent",
    role="Memorizza recupera tutti i piani versioned not overwritten L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support PlanStorageAgent in MemoryManagementTeam MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

GraphicRevisionAgent = Agent(
    name="GraphicRevisionAgent",
    role="Revisiona grafiche fail quality review loop L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support GraphicRevisionAgent in GraphicDesignTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CoverRevisionAgent = Agent(
    name="CoverRevisionAgent",
    role="Revisiona cover se needed loop critico L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CoverRevisionAgent in CoverDesignTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

RollbackExecutorAgent = Agent(
    name="RollbackExecutorAgent",
    role="Esegue rollback a checkpoint precedenti real recovery via CheckpointManager restore L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support RollbackExecutorAgent in RecoveryTeam SelfHealingEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

RecoveryValidatorAgent = Agent(
    name="RecoveryValidatorAgent",
    role="Valida recovery successo workflow continua senza data loss L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support RecoveryValidatorAgent in RecoveryTeam SelfHealingEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CheckpointValidatorAgent = Agent(
    name="CheckpointValidatorAgent",
    role="Valida checkpoint prima storage - Memory sub-ecosystem L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CheckpointValidatorAgent in CheckpointSubEcosystem MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CheckpointRestorerAgent = Agent(
    name="CheckpointRestorerAgent",
    role="Esegue restore checkpoint su richiesta rollback - Memory sub L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CheckpointRestorerAgent in CheckpointSubEcosystem MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

CheckpointPrunerAgent = Agent(
    name="CheckpointPrunerAgent",
    role="Gestisce pruning checkpoint vecchi preservando traceability L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support CheckpointPrunerAgent in CheckpointSubEcosystem MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

DecisionLogReaderAgent = Agent(
    name="DecisionLogReaderAgent",
    role="Legge log decisioni con traceability - Memory sub L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionLogSubEcosystem",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support DecisionLogReaderAgent in DecisionLogSubEcosystem MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

DecisionTraceabilityAgent = Agent(
    name="DecisionTraceabilityAgent",
    role="Verifica traceability decisioni reasoning chain - Memory sub L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionLogSubEcosystem",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support DecisionTraceabilityAgent in DecisionLogSubEcosystem MemoryEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

VisualPlaywrightValidatorAgent = Agent(
    name="VisualPlaywrightValidatorAgent",
    role="Valida salvataggi visual Playwright L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support VisualPlaywrightValidatorAgent in VisualPlaywrightOperationsTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

FinalVisualApprovalAgent = Agent(
    name="FinalVisualApprovalAgent",
    role="Approvazione finale visual - VisualQualityTeam L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support FinalVisualApprovalAgent in VisualQualityTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

EscalationManagerAgent = Agent(
    name="EscalationManagerAgent",
    role="Gestisce escalation a controller e Supreme dopo max retry fail L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support EscalationManagerAgent in RecoveryTeam SelfHealingEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

PlaywrightFailureDetectorAgent = Agent(
    name="PlaywrightFailureDetectorAgent",
    role="Rileva fallimenti Playwright specifici timeout blocked L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support PlaywrightFailureDetectorAgent in DetectionTeam SelfHealingEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

MemoryFailureDetectorAgent = Agent(
    name="MemoryFailureDetectorAgent",
    role="Rileva fallimenti memoria write failure corruption gap L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support MemoryFailureDetectorAgent in DetectionTeam SelfHealingEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

WritingQualityCheckerAgent = Agent(
    name="WritingQualityCheckerAgent",
    role="Controlla qualità scrittura uniformità L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support WritingQualityCheckerAgent in BookWritingTeam ProductionEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ContentValidationAgent = Agent(
    name="ContentValidationAgent",
    role="Valida contenuto manoscritto vs second-level plan details L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ContentValidationAgent in ProductionQualityTeam ProductionEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

VisualQualityAuditorAgent = Agent(
    name="VisualQualityAuditorAgent",
    role="Audita qualità visual finale cross-team L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support VisualQualityAuditorAgent in VisualQualityTeam VisualEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

SearchQualityValidatorAgent = Agent(
    name="SearchQualityValidatorAgent",
    role="Valida qualità risultati search Amazon L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support SearchQualityValidatorAgent in AmazonKeywordResearchTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

NicheViabilityValidatorAgent = Agent(
    name="NicheViabilityValidatorAgent",
    role="Valida fattibilità nicchia da BookNicheDecisionSkill L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support NicheViabilityValidatorAgent in AmazonKeywordResearchTeam ResearchEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ProductionLogWriterAgent = Agent(
    name="ProductionLogWriterAgent",
    role="Scrive production log decisioni durante scrittura L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
    hierarchy_level=6,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['data_to_validate', 'memory_content_all_categories', 'checkpoint_refs', 'phase_outputs', 'save_operations', 'performance_metrics', 'historical_data', 'plan_validity', 'graphic_data', 'cover_data'],
    outputs=['validation_result', 'save_validation', 'consistency_report', 'checkpoint_created_confirmation', 'restored_checkpoint', 'read_response', 'decision_log_confirmation', 'plan_retrieval', 'quality_score', 'revision_loop_trigger', 'recovery_validation'],
    decision_logic="""Come support ProductionLogWriterAgent in BookWritingTeam ProductionEcosystem: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="support validation if involves Playwright save confirmation",
    skill_usage=['MemoryReadWriteSkill', 'CheckpointManagementSkill', 'SelfHealingSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill', 'FeedbackCollectionSkill'],
    level_name="L6_SUPPORT_AGENT"
)

ALL_L6 = [DataFormatterAgent,SaveValidatorAgent,ReviewScoreNormalizerAgent,AmazonResultsValidatorAgent,ReviewDataValidatorAgent,FinalApprovalAgent,VisualPlaywrightSaveAgent,GraphicQualityReviewerAgent,CoverQualityReviewerAgent,HierarchyManagerAgent,ImportantNotesAgent,PerformanceMetricsAgent,PatternDetectorAgent,ImprovementPlanWriterAgent,ThresholdUpdaterAgent,WorkflowOptimizerAgent,MemoryValidatorAgent,CheckpointManagerAgent,DecisionLoggerAgent,PlanStorageAgent,GraphicRevisionAgent,CoverRevisionAgent,RollbackExecutorAgent,RecoveryValidatorAgent,CheckpointValidatorAgent,CheckpointRestorerAgent,CheckpointPrunerAgent,DecisionLogReaderAgent,DecisionTraceabilityAgent,VisualPlaywrightValidatorAgent,FinalVisualApprovalAgent,EscalationManagerAgent,PlaywrightFailureDetectorAgent,MemoryFailureDetectorAgent,WritingQualityCheckerAgent,ContentValidationAgent,VisualQualityAuditorAgent,SearchQualityValidatorAgent,NicheViabilityValidatorAgent,ProductionLogWriterAgent]
