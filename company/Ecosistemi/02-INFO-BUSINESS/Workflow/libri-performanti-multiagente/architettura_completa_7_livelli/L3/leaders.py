import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

AmazonResearchLeader = Agent(
    name="AmazonResearchLeader",
    role="Gestisce keyword generation, search, extraction, validation, BookNicheDecisionSkill L3 Team Leader - AmazonKeywordResearchTeam in ResearchEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOps",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader AmazonKeywordResearchTeam in ResearchEcosystem: trigger internal flow ['KeywordGeneratorAgent', 'AmazonSearchAgent', 'AmazonDataExtractorAgent', 'AmazonResultsValidatorAgent', 'KeywordQualityAnalystAgent', 'NicheCompetitionAnalystAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem PlaywrightOps se presente. Report a ResearchEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ReviewResearchLeader = Agent(
    name="ReviewResearchLeader",
    role="Gestisce review site discovery, extraction, normalization, validation L3 Team Leader - ReviewAnalysisResearchTeam in ResearchEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewSubEcosystem",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ReviewAnalysisResearchTeam in ResearchEcosystem: trigger internal flow ['ReviewSiteFinderAgent', 'ReviewDataExtractorAgent', 'ReviewScoreNormalizerAgent', 'ReviewDataValidatorAgent', 'ReviewSentimentAnalystAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem ReviewSubEcosystem se presente. Report a ResearchEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

DataPersistenceLeader = Agent(
    name="DataPersistenceLeader",
    role="Garantisce salvataggio via Playwright, formatting, validation, checkpoint CP1 L3 Team Leader - DataPersistenceTeam in ResearchEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PersistenceSubEcosystem",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader DataPersistenceTeam in ResearchEcosystem: trigger internal flow ['PlaywrightSaveAgent', 'DataFormatterAgent', 'SaveValidatorAgent', 'RawDataArchiverAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem PersistenceSubEcosystem se presente. Report a ResearchEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

KeywordExpansionLeader = Agent(
    name="KeywordExpansionLeader",
    role="Leader team espansione keyword quando empty result, genera variazioni da LearningLog L3 Team Leader - KeywordExpansionTeam in ResearchEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ExpansionSubEcosystem",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader KeywordExpansionTeam in ResearchEcosystem: trigger internal flow ['KeywordVariationGeneratorAgent', 'SemanticKeywordExpanderAgent', 'LongTailKeywordAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem ExpansionSubEcosystem se presente. Report a ResearchEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

SearchOptimizationLeader = Agent(
    name="SearchOptimizationLeader",
    role="Ottimizza strategie search Amazon, riduce blocchi Playwright L3 Team Leader - SearchOptimizationTeam in ResearchEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="SearchOptimizationTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="OptimizationSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader SearchOptimizationTeam in ResearchEcosystem: trigger internal flow ['SearchStrategyOptimizerAgent', 'PlaywrightRotationManagerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem OptimizationSub se presente. Report a ResearchEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

QualificationLeader = Agent(
    name="QualificationLeader",
    role="Gestisce 8 analyst senior, coordinate flusso valutazione 5 criteri L3 Team Leader - QualificationAnalysisTeam in QualificationEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader QualificationAnalysisTeam in QualificationEcosystem: trigger internal flow ['ReproducibilityAnalystAgent', 'AbsurdityDetectorAgent', 'ProductionSpeedAnalystAgent', 'MarketAlignmentAnalystAgent', 'PlanQualityAuditorAgent', 'CompetitionAnalystAgent', 'SustainabilityAnalystAgent', 'BusinessFitAnalystAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem AnalysisSub se presente. Report a QualificationEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

QualificationDecisionLeader = Agent(
    name="QualificationDecisionLeader",
    role="Aggrega decisioni, gestisce rischi, scrive report finale GO/NO-GO L3 Team Leader - QualificationDecisionTeam in QualificationEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="DecisionSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader QualificationDecisionTeam in QualificationEcosystem: trigger internal flow ['DecisionAggregatorAgent', 'RiskFlagManagerAgent', 'QualificationReportWriterAgent', 'DecisionQualityCheckerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem DecisionSub se presente. Report a QualificationEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

StructurePlanningLeader = Agent(
    name="StructurePlanningLeader",
    role="Gestisce video_structure REQUIRED preservato verbatim, chapters, details, coherence - CONTROL POINT CRITICO L3 Team Leader - StructurePlanningTeam in PlanningEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader StructurePlanningTeam in PlanningEcosystem: trigger internal flow ['VideoStructureArchitectAgent', 'ChapterDesignerAgent', 'DetailFillerAgent', 'PlanCoherenceValidatorAgent', 'VideoStructureValidatorAgent', 'OutlineOptimizerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem StructureSub se presente. Report a PlanningEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ProductionReadinessLeader = Agent(
    name="ProductionReadinessLeader",
    role="Verifica prerequisiti produzione, stima risorse, emette start signal L3 Team Leader - ProductionReadinessTeam in PlanningEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ReadinessSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ProductionReadinessTeam in PlanningEcosystem: trigger internal flow ['ReadinessCheckerAgent', 'ResourceEstimatorAgent', 'ProductionStartSignalAgent', 'RiskMitigationPlannerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem ReadinessSub se presente. Report a PlanningEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ContentPlanningLeader = Agent(
    name="ContentPlanningLeader",
    role="Leader pianificazione contenuti dettagliata per produzione sostenibile L3 Team Leader - ContentPlanningTeam in PlanningEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ContentPlanningTeam in PlanningEcosystem: trigger internal flow ['ContentDetailArchitectAgent', 'ContentFlowDesignerAgent', 'ResourceAllocationPlannerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem ContentSub se presente. Report a PlanningEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

BookWritingLeader = Agent(
    name="BookWritingLeader",
    role="Gestisce chapter writers paralleli, consistenza, stile, qualità L3 Team Leader - BookWritingTeam in ProductionEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader BookWritingTeam in ProductionEcosystem: trigger internal flow ['ChapterWriterAgent', 'ConsistencyCheckerAgent', 'StyleEnforcerAgent', 'ContentQualityReviewerAgent', 'ChapterDependencyManagerAgent', 'WritingProgressTrackerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem WritingSub se presente. Report a ProductionEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ProductionQualityLeader = Agent(
    name="ProductionQualityLeader",
    role="Valida manoscritto completezza, compliance piano, approvazione finale L3 Team Leader - ProductionQualityTeam in ProductionEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="QualitySub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ProductionQualityTeam in ProductionEcosystem: trigger internal flow ['ManuscriptValidatorAgent', 'PlanComplianceCheckerAgent', 'FinalApprovalAgent', 'QualityMetricsCalculatorAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem QualitySub se presente. Report a ProductionEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

EditingLeader = Agent(
    name="EditingLeader",
    role="Leader editing finale, uniformità, correzione L3 Team Leader - EditingTeam in ProductionEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader EditingTeam in ProductionEcosystem: trigger internal flow ['EditingCoordinatorAgent', 'FinalProofreaderAgent', 'CrossReferenceCheckerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem EditingSub se presente. Report a ProductionEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

GraphicDesignLeader = Agent(
    name="GraphicDesignLeader",
    role="Gestisce creazione prompt grafiche, generazione, quality review revision loop L3 Team Leader - GraphicDesignTeam in VisualEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader GraphicDesignTeam in VisualEcosystem: trigger internal flow ['GraphicPromptCreatorAgent', 'GraphicGeneratorAgent', 'GraphicQualityReviewerAgent', 'GraphicRevisionAgent', 'GraphicStyleEnforcerAgent', 'VisualConsistencyCheckerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem GraphicSub se presente. Report a VisualEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

CoverDesignLeader = Agent(
    name="CoverDesignLeader",
    role="Gestisce cover concept basato contenuto e market data, prompt, generazione, review critica L3 Team Leader - CoverDesignTeam in VisualEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader CoverDesignTeam in VisualEcosystem: trigger internal flow ['CoverConceptAgent', 'CoverPromptCreatorAgent', 'CoverGeneratorAgent', 'CoverQualityReviewerAgent', 'CoverRevisionAgent', 'CoverMarketFitAnalystAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem CoverSub se presente. Report a VisualEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

VisualPlaywrightLeader = Agent(
    name="VisualPlaywrightLeader",
    role="Gestisce navigazione Playwright e salvataggio visual tasks L3 Team Leader - VisualPlaywrightOperationsTeam in VisualEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="PlaywrightSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader VisualPlaywrightOperationsTeam in VisualEcosystem: trigger internal flow ['VisualPlaywrightNavigatorAgent', 'VisualPlaywrightSaveAgent', 'VisualPlaywrightValidatorAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem PlaywrightSub se presente. Report a VisualEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

VisualQualityLeader = Agent(
    name="VisualQualityLeader",
    role="Leader qualità visual, approva grafica e cover finali L3 Team Leader - VisualQualityTeam in VisualEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader VisualQualityTeam in VisualEcosystem: trigger internal flow ['VisualQualityAuditorAgent', 'FinalVisualApprovalAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem VisualQualitySub se presente. Report a VisualEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

MemoryManagerLeader = Agent(
    name="MemoryManagerLeader",
    role="Gestisce tutti gli agenti memoria, read/write protocols, checkpoint logic, validazione - SISTEMA ATTIVO L3 Team Leader - MemoryManagementTeam in MemoryEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader MemoryManagementTeam in MemoryEcosystem: trigger internal flow ['MemoryWriterAgent', 'MemoryReaderAgent', 'MemoryValidatorAgent', 'CheckpointManagerAgent', 'DecisionLoggerAgent', 'PlanStorageAgent', 'HierarchyManagerAgent', 'ImportantNotesAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem CoreMemorySub se presente. Report a MemoryEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

CheckpointSubLeader = Agent(
    name="CheckpointSubLeader",
    role="Leader sub-ecosistema checkpoint creation storage restoration L3 Team Leader - CheckpointSubEcosystem in MemoryEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader CheckpointSubEcosystem in MemoryEcosystem: trigger internal flow ['CheckpointCreatorAgent', 'CheckpointValidatorAgent', 'CheckpointRestorerAgent', 'CheckpointPrunerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem CheckpointSub se presente. Report a MemoryEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

DecisionLogSubLeader = Agent(
    name="DecisionLogSubLeader",
    role="Leader sub-ecosistema logging decisioni immutable L3 Team Leader - DecisionLogSubEcosystem in MemoryEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader DecisionLogSubEcosystem in MemoryEcosystem: trigger internal flow ['DecisionLogWriterAgent', 'DecisionLogReaderAgent', 'DecisionTraceabilityAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem DecisionSub se presente. Report a MemoryEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

DetectionLeader = Agent(
    name="DetectionLeader",
    role="Gestisce output monitoring, error detection, anomaly detection, stall detection L3 Team Leader - DetectionTeam in SelfHealingEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader DetectionTeam in SelfHealingEcosystem: trigger internal flow ['OutputMonitorAgent', 'ErrorDetectorAgent', 'AnomalyDetectorAgent', 'StallDetectorAgent', 'PlaywrightFailureDetectorAgent', 'MemoryFailureDetectorAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem DetectionSub se presente. Report a SelfHealingEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

DiagnosisLeader = Agent(
    name="DiagnosisLeader",
    role="Gestisce root cause analysis, impact assessment, recovery planning L3 Team Leader - DiagnosisTeam in SelfHealingEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader DiagnosisTeam in SelfHealingEcosystem: trigger internal flow ['RootCauseAnalystAgent', 'ImpactAssessorAgent', 'RecoveryPlannerAgent', 'FailurePatternAnalyzerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem DiagnosisSub se presente. Report a SelfHealingEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

RecoveryLeader = Agent(
    name="RecoveryLeader",
    role="Gestisce retry rollback alternative path validation - real recovery L3 Team Leader - RecoveryTeam in SelfHealingEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader RecoveryTeam in SelfHealingEcosystem: trigger internal flow ['RetryExecutorAgent', 'RollbackExecutorAgent', 'AlternativePathAgent', 'RecoveryValidatorAgent', 'EscalationManagerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem RecoverySub se presente. Report a SelfHealingEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

FeedbackCollectionLeader = Agent(
    name="FeedbackCollectionLeader",
    role="Gestisce outcome collection, metrics, pattern detection - real improvement L3 Team Leader - FeedbackCollectionTeam in AutoImprovementEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader FeedbackCollectionTeam in AutoImprovementEcosystem: trigger internal flow ['OutcomeCollectorAgent', 'PerformanceMetricsAgent', 'PatternDetectorAgent', 'CycleOutcomeAnalyzerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem FeedbackSub se presente. Report a AutoImprovementEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ImprovementPlanningLeader = Agent(
    name="ImprovementPlanningLeader",
    role="Analizza feedback, rank priorities, scrive improvement plans L3 Team Leader - ImprovementPlanningTeam in AutoImprovementEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ImprovementPlanningTeam in AutoImprovementEcosystem: trigger internal flow ['ImprovementAnalystAgent', 'PriorityRankerAgent', 'ImprovementPlanWriterAgent', 'OpportunityIdentifierAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem PlanningSub se presente. Report a AutoImprovementEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ImprovementExecutionLeader = Agent(
    name="ImprovementExecutionLeader",
    role="Adjust parameters, update thresholds, optimize workflows - execution reale L3 Team Leader - ImprovementExecutionTeam in AutoImprovementEcosystem - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
    hierarchy_level=3,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ExecutionSub",
    inputs=['cycle_signal', 'handoff_package_from_previous_ecosystem', 'memory_hierarchies', 'important_notes', 'team_member_status', 'checkpoint_refs'],
    outputs=['team_status', 'internal_flow_trigger', 'handoff_ready_package', 'checkpoint_creation_request', 'reports_to_L2'],
    decision_logic="""Come leader ImprovementExecutionTeam in AutoImprovementEcosystem: trigger internal flow ['ParameterAdjusterAgent', 'ThresholdUpdaterAgent', 'WorkflowOptimizerAgent', 'LearningLoggerAgent'] in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem ExecutionSub se presente. Report a AutoImprovementEcosystemController.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'BookWritingConsistencySkill'],
    level_name="L3_TEAM_LEADER"
)

ALL_L3 = [AmazonResearchLeader,ReviewResearchLeader,DataPersistenceLeader,KeywordExpansionLeader,SearchOptimizationLeader,QualificationLeader,QualificationDecisionLeader,StructurePlanningLeader,ProductionReadinessLeader,ContentPlanningLeader,BookWritingLeader,ProductionQualityLeader,EditingLeader,GraphicDesignLeader,CoverDesignLeader,VisualPlaywrightLeader,VisualQualityLeader,MemoryManagerLeader,CheckpointSubLeader,DecisionLogSubLeader,DetectionLeader,DiagnosisLeader,RecoveryLeader,FeedbackCollectionLeader,ImprovementPlanningLeader,ImprovementExecutionLeader]
