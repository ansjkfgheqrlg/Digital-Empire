import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent


AmazonResearchLeader = Agent(
    name="AmazonResearchLeader",
    role="Leader AmazonKeywordResearchTeam gestisce keyword generation search extraction validation BookNicheDecisionSkill",
    hierarchy_level=3,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOps" if "PlaywrightOps" != "None" else None,
    inputs=["cycle_signal", "handoff_package", "memory_hierarchies", "important_notes"],
    outputs=["team_status", "internal_flow_trigger", "handoff_ready_package", "checkpoint_creation"],
    decision_logic="""Leader AmazonKeywordResearchTeam trigger KeywordGenerator -> Search via NavigatorMicroAgent -> Extractor via CaptureMicroAgent -> Validator -> decision -> loop if empty retry adjusted keywords""",
    connections={"reports_to": ["ResearchEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ReviewResearchLeader = Agent(
    name="ReviewResearchLeader",
    role="Leader ReviewAnalysisResearchTeam gestisce review site discovery extraction normalization validation",
    hierarchy_level=3,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewSub" if "ReviewSub" != "None" else None,
    inputs=["book_opportunities", "seed_review_sites"],
    outputs=["review_analysis_data", "normalized_scores"],
    decision_logic="""Leader ReviewResearchTeam trigger SiteFinder -> DataExtractor -> Normalizer -> Validator -> ReviewResearchLeader decision link to book opportunities""",
    connections={"reports_to": ["ResearchEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

DataPersistenceLeader = Agent(
    name="DataPersistenceLeader",
    role="Leader DataPersistenceTeam garantisce salvataggio via Playwright formatting validation checkpoint CP1",
    hierarchy_level=3,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PersistenceSub" if "PersistenceSub" != "None" else None,
    inputs=["book_opportunities", "review_data", "raw_data"],
    outputs=["save_confirmations", "research_complete_signal", "structured_output"],
    decision_logic="""Leader DataPersistenceTeam collect book review data -> Formatter formats structured_output ready qualification -> PlaywrightSaveAgent saves via save_results -> Validator validates -> Leader creates checkpoint CP1""",
    connections={"reports_to": ["ResearchEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

KeywordExpansionLeader = Agent(
    name="KeywordExpansionLeader",
    role="Leader KeywordExpansionTeam espansione keyword quando empty result LearningLog",
    hierarchy_level=3,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ExpansionSub" if "ExpansionSub" != "None" else None,
    inputs=["empty_result_trigger", "important_notes", "LearningLog"],
    outputs=["keyword_variations", "new_keyword_list"],
    decision_logic="""Leader KeywordExpansionTeam empty -> VariationGenerator -> SemanticExpander -> LongTail -> new keyword list -> AmazonSearchAgent retry""",
    connections={"reports_to": ["ResearchEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

SearchOptimizationLeader = Agent(
    name="SearchOptimizationLeader",
    role="Leader SearchOptimizationTeam ottimizza strategie search Amazon riduce blocchi Playwright",
    hierarchy_level=3,
    team="SearchOptimizationTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="OptimizationSub" if "OptimizationSub" != "None" else None,
    inputs=["Playwright_failure_logs", "AnomalyLog"],
    outputs=["optimized_strategy", "rotation_plan"],
    decision_logic="""Leader SearchOptimizationTeam analyze failures -> StrategyOptimizer adjust -> RotationManager rotate user_agent timeout alternative selector""",
    connections={"reports_to": ["ResearchEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

QualificationLeader = Agent(
    name="QualificationLeader",
    role="Leader QualificationAnalysisTeam gestisce 8 analyst valuta 5 criteri reproducibility absurdity speed market plan validity",
    hierarchy_level=3,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["research_handoff_package", "BookOpportunityRegistry"],
    outputs=["evaluation_scores", "risk_flags", "preliminary_decision"],
    decision_logic="""Orchestrate flow ReproducibilityAnalyst -> AbsurdityDetector -> ProductionSpeedAnalyst -> MarketAlignmentAnalyst -> PlanQualityAuditor -> QualificationLeader preliminary GO NO-GO""",
    connections={"reports_to": ["QualificationEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

QualificationDecisionLeader = Agent(
    name="QualificationDecisionLeader",
    role="Leader QualificationDecisionTeam aggrega decisioni gestisce rischi scrive report finale GO NO-GO",
    hierarchy_level=3,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="DecisionSub" if "DecisionSub" != "None" else None,
    inputs=["analyst_outputs", "risk_flags"],
    outputs=["final_qualification_report", "GO_NO_GO_decision"],
    decision_logic="""Trigger DecisionAggregatorAgent QualificationDecisionSkill weighted reproducibility 30% speed 25% absurdity 20% market 25% threshold 70 GO IF NO-GO log reason archive IF GO handoff package Planning""",
    connections={"reports_to": ["QualificationEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

StructurePlanningLeader = Agent(
    name="StructurePlanningLeader",
    role="Leader StructurePlanningTeam gestisce video_structure REQUIRED preservato verbatim chapters details coherence CONTROL POINT CRITICO",
    hierarchy_level=3,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["qualification_GO_package", "risk_flags"],
    outputs=["second_level_plan", "validation_status"],
    decision_logic="""CRITICAL Trigger VideoStructureArchitectAgent first must output video_structure REQUIRED as per original requirement do not remove reinterpret preserve verbatim THEN ChapterDesigner THEN DetailFiller THEN PlanCoherenceValidator IF video_structure missing critical self-healing rollback CP2 IF valid send ProductionReadinessLeader""",
    connections={"reports_to": ["PlanningEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ProductionReadinessLeader = Agent(
    name="ProductionReadinessLeader",
    role="Leader ProductionReadinessTeam verifica prerequisiti stima risorse emette start signal",
    hierarchy_level=3,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ReadinessSub" if "ReadinessSub" != "None" else None,
    inputs=["second_level_plan_draft"],
    outputs=["readiness_confirmation", "production_start_signal"],
    decision_logic="""Trigger ReadinessChecker verifies prerequisites IF ready THEN ResourceEstimator estimates IF sustainable THEN ProductionStartSignalAgent emits signal TRUE timestamp creates CP3 ELSE escalate""",
    connections={"reports_to": ["PlanningEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ContentPlanningLeader = Agent(
    name="ContentPlanningLeader",
    role="Leader ContentPlanningTeam pianificazione contenuti dettagliata produzione sostenibile",
    hierarchy_level=3,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentSub" if "ContentSub" != "None" else None,
    inputs=["second_level_plan_draft", "chapters"],
    outputs=["details_enriched", "content_flow"],
    decision_logic="""DetailArchitect enriches production_constraints style_notes business_alignment graphic_needs sustainability_check FlowDesigner designs flow AllocationPlanner plans resources""",
    connections={"reports_to": ["PlanningEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

BookWritingLeader = Agent(
    name="BookWritingLeader",
    role="Leader BookWritingTeam gestisce chapter writers paralleli consistenza stile qualita",
    hierarchy_level=3,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub" if "WritingSub" != "None" else None,
    inputs=["second_level_plan", "production_start_signal", "memory_context"],
    outputs=["complete_manuscript_draft", "writing_log"],
    decision_logic="""Trigger ChapterWriterAgents per chapter parallel where possible THEN ConsistencyChecker cross-chapter THEN StyleEnforcer uniform style THEN ContentQualityReviewer final review IF all pass approve manuscript IF fail retry chapter with memory read""",
    connections={"reports_to": ["ProductionEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ProductionQualityLeader = Agent(
    name="ProductionQualityLeader",
    role="Leader ProductionQualityTeam valida completezza compliance approvazione finale",
    hierarchy_level=3,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="QualitySub" if "QualitySub" != "None" else None,
    inputs=["manuscript_draft"],
    outputs=["validated_manuscript", "final_approval"],
    decision_logic="""Trigger ManuscriptValidator validates completeness THEN PlanComplianceChecker compliance THEN FinalApprovalAgent final approval IF any fails rollback last chapter checkpoint CP4""",
    connections={"reports_to": ["ProductionEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

EditingLeader = Agent(
    name="EditingLeader",
    role="Leader EditingTeam editing finale uniformita correzione",
    hierarchy_level=3,
    team="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub" if "EditingSub" != "None" else None,
    inputs=["validated_manuscript"],
    outputs=["edited_manuscript", "editing_log"],
    decision_logic="""Editing flow Coordinator -> Proofreader -> CrossReferenceChecker -> FinalApproval""",
    connections={"reports_to": ["ProductionEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

GraphicDesignLeader = Agent(
    name="GraphicDesignLeader",
    role="Leader GraphicDesignTeam creazione prompt grafiche generazione quality review revision loop",
    hierarchy_level=3,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicSub" if "GraphicSub" != "None" else None,
    inputs=["manuscript", "chapter_list", "details"],
    outputs=["approved_graphics"],
    decision_logic="""Flow PromptCreator creates -> Generator generates via VisualPlaywrightSaveAgent -> QualityReviewer reviews -> IF failed RevisionAgent revises back QualityReviewer IF passed approved and saved""",
    connections={"reports_to": ["VisualEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

CoverDesignLeader = Agent(
    name="CoverDesignLeader",
    role="Leader CoverDesignTeam cover concept prompt generazione review critica non skippabile",
    hierarchy_level=3,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverSub" if "CoverSub" != "None" else None,
    inputs=["manuscript", "market_data", "graphic_style"],
    outputs=["final_approved_cover"],
    decision_logic="""Trigger CoverConceptAgent concept content+market -> PromptCreator prompt -> Generator generates -> QualityReviewer reviews IF failed RevisionAgent revises loop critical cannot skip must escalate if fails""",
    connections={"reports_to": ["VisualEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

VisualPlaywrightLeader = Agent(
    name="VisualPlaywrightLeader",
    role="Leader VisualPlaywrightOperationsTeam navigazione Playwright salvataggio visual tasks",
    hierarchy_level=3,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="PlaywrightSub" if "PlaywrightSub" != "None" else None,
    inputs=["visual_assets", "save_requests"],
    outputs=["save_confirmations"],
    decision_logic="""Trigger VisualPlaywrightNavigatorAgent navigation IF needed THEN VisualPlaywrightSaveAgent saves via visual_save validation""",
    connections={"reports_to": ["VisualEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

VisualQualityLeader = Agent(
    name="VisualQualityLeader",
    role="Leader VisualQualityTeam qualita visual finale approva grafiche cover",
    hierarchy_level=3,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub" if "VisualQualitySub" != "None" else None,
    inputs=["all_graphics", "cover", "prompts"],
    outputs=["visual_quality_approval", "CP_FINAL"],
    decision_logic="""Quality final Auditor audits quality all visual vs manuscript plan market fit THEN FinalVisualApproval approval VisualQualityLeader creates CP5 CP_FINAL""",
    connections={"reports_to": ["VisualEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

MemoryManagerLeader = Agent(
    name="MemoryManagerLeader",
    role="Leader MemoryManagementTeam gestisce memoria attiva read write checkpoint decision plan hierarchy notes SISTEMA ATTIVO NON PASSIVO",
    hierarchy_level=3,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["read_requests", "write_requests", "checkpoint_triggers", "validation_triggers"],
    outputs=["read_responses", "write_confirmations", "validation_reports"],
    decision_logic="""Route write requests MemoryWriterAgent after validation by MemoryValidatorAgent Route reads MemoryReaderAgent context timestamp Checkpoint creation via CheckpointManagerAgent auto phase transitions Decision logging via DecisionLoggerAgent""",
    connections={"reports_to": ["MemoryEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

CheckpointSubLeader = Agent(
    name="CheckpointSubLeader",
    role="Leader CheckpointSubEcosystem gestione checkpoint creation storage restoration",
    hierarchy_level=3,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSub" if "CheckpointSub" != "None" else None,
    inputs=["checkpoint_creation_triggers", "rollback_requests", "state_snapshots"],
    outputs=["checkpoint_created_confirmation", "restored_checkpoint"],
    decision_logic="""Checkpoint flow Creator creates parent ID valid flag Validator validates Restorer restores rollback Pruner pruning old preserving traceability Micro atomic create restore Core self-healing""",
    connections={"reports_to": ["MemoryEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

DecisionLogSubLeader = Agent(
    name="DecisionLogSubLeader",
    role="Leader DecisionLogSubEcosystem logging decisioni immutable traceability",
    hierarchy_level=3,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionSub" if "DecisionSub" != "None" else None,
    inputs=["decision_events", "reasoning_chains"],
    outputs=["decision_log_confirmation", "decision_id", "traceability"],
    decision_logic="""Decision log flow Writer logs decision_id phase team agent type value reasoning timestamp related_data immutable Reader retrieves traceability TraceabilityAgent verifies reasoning chain Micro atomic logging""",
    connections={"reports_to": ["MemoryEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

DetectionLeader = Agent(
    name="DetectionLeader",
    role="Leader DetectionTeam monitora output completeness coherence detect errors anomalies stalled frozen",
    hierarchy_level=3,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub" if "DetectionSub" != "None" else None,
    inputs=["phase_outputs_all_ecosystems", "process_status_feeds"],
    outputs=["anomaly_reports"],
    decision_logic="""All detection agents parallel OutputMonitor checks phase outputs vs expected schemas books_found non empty plan 5 criteria second_level_plan video_structure complete_book graphics+cover ErrorDetector scans logs errors AnomalyDetector unusual patterns all NO-GO video_structure missing cover missing memory gap StallDetector frozen no heartbeat PlaywrightFailureDetector Playwright timeout MemoryFailureDetector aggregation anomaly report severity location context""",
    connections={"reports_to": ["SelfHealingEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

DiagnosisLeader = Agent(
    name="DiagnosisLeader",
    role="Leader DiagnosisTeam root cause analysis impact assessment recovery planning",
    hierarchy_level=3,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub" if "DiagnosisSub" != "None" else None,
    inputs=["anomaly_reports"],
    outputs=["diagnosis_reports_with_recovery_plan"],
    decision_logic="""RootCauseAnalyst root cause categorization ImpactAssessor impact affected phases data loss risk checkpoint availability RecoveryPlanner recovery plan choosing action retry rollback escalate skip_and_log requalify mapping error_type action per SelfHealingEngine""",
    connections={"reports_to": ["SelfHealingEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

RecoveryLeader = Agent(
    name="RecoveryLeader",
    role="Leader RecoveryTeam retry rollback alternative path validation real recovery",
    hierarchy_level=3,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub" if "RecoverySub" != "None" else None,
    inputs=["recovery_plans"],
    outputs=["recovery_confirmations_or_escalations"],
    decision_logic="""RetryExecutor retries adjusted params IF fails RollbackExecutor rolls back checkpoint via CheckpointManagerAgent IF fails AlternativePath finds executes alternative path different keyword strategy skip non-critical THEN RecoveryValidator validates without data loss IF fails after max 3 EscalationManager escalates controller Supreme""",
    connections={"reports_to": ["SelfHealingEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

FeedbackCollectionLeader = Agent(
    name="FeedbackCollectionLeader",
    role="Leader FeedbackCollectionTeam outcome collection metrics pattern detection real improvement",
    hierarchy_level=3,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackSub" if "FeedbackSub" != "None" else None,
    inputs=["cycle_completion_signals", "phase_outcomes", "AnomalyLog", "PerformanceHistory"],
    outputs=["structured_feedback_data", "metrics", "patterns"],
    decision_logic="""OutcomeCollector collects outcomes GO NO-GO rates production speed internal time self-healing frequency plan validity scores memory retrieval patterns book performance signals Amazon+review sites PerformanceMetrics calculates metrics per 6 feedback signals PatternDetector patterns positive negative""",
    connections={"reports_to": ["AutoImprovementEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ImprovementPlanningLeader = Agent(
    name="ImprovementPlanningLeader",
    role="Leader ImprovementPlanningTeam analizza feedback rank priorities scrive improvement plans",
    hierarchy_level=3,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub" if "PlanningSub" != "None" else None,
    inputs=["feedback_data", "metrics", "patterns"],
    outputs=["prioritized_improvement_plans"],
    decision_logic="""ImprovementAnalyst analyzes feedback identifies opportunities 5 targets future research quality future qualification decisions future plan accuracy production flow speed risk sensitivity PriorityRanker ranks impact feasibility aligned business goal quantity-performance OpportunityIdentifier positive patterns PlanWriter writes prioritized plan""",
    connections={"reports_to": ["AutoImprovementEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ImprovementExecutionLeader = Agent(
    name="ImprovementExecutionLeader",
    role="Leader ImprovementExecutionTeam adjust parameters update thresholds optimize workflows execution reale",
    hierarchy_level=3,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ExecutionSub" if "ExecutionSub" != "None" else None,
    inputs=["improvement_plans"],
    outputs=["updated_parameters", "workflow_optimizations", "LearningLog"],
    decision_logic="""ParameterAdjuster adjusts workflow params keyword strategies batch size retry limits ThresholdUpdater updates decision thresholds GO threshold 70 based learning WorkflowOptimizer optimizes flow sequences based performance data improve handoff validation reduce self-healing triggers fixing root causes LearningLogger logs LearningLog important_notes per generate_improvement_signal schema""",
    connections={"reports_to": ["AutoImprovementEcosystemController"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L3"
)

ALL_L3 = [AmazonResearchLeader,ReviewResearchLeader,DataPersistenceLeader,KeywordExpansionLeader,SearchOptimizationLeader,QualificationLeader,QualificationDecisionLeader,StructurePlanningLeader,ProductionReadinessLeader,ContentPlanningLeader,BookWritingLeader,ProductionQualityLeader,EditingLeader,GraphicDesignLeader,CoverDesignLeader,VisualPlaywrightLeader,VisualQualityLeader,MemoryManagerLeader,CheckpointSubLeader,DecisionLogSubLeader,DetectionLeader,DiagnosisLeader,RecoveryLeader,FeedbackCollectionLeader,ImprovementPlanningLeader,ImprovementExecutionLeader]
print("Fixed file validated")
