import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

ResearchEcosystemController = Agent(
    name="ResearchEcosystemController",
    role="Controller L2 ResearchEcosystem gestisce 5 team keyword search Amazon review sites riporta a Supreme",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem=None,
    inputs=["cycle_start_signal","memory_hierarchies","important_notes_feedback","checkpoints","team_status_reports"],
    outputs=["ecosystem_status","resource_allocation","go_signal","reports_to_L1","handoff_validation"],
    decision_logic="SE nuovo ciclo leggi important_notes LearningLog pattern successo fallimento alloca team leader L3 trigger flow interno SE team empty result anomaly trigger SelfHealing via PlaywrightErrorHandlerAgent SE output validato checkpoint marca phase complete crea checkpoint via CheckpointManagerAgent handoff prossimo ecosistema via Memory broker 8 steps SE 3 fallimenti escalate Supreme",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["AmazonResearchLeader","ReviewResearchLeader","DataPersistenceLeader","KeywordExpansionLeader","SearchOptimizationLeader"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","FeedbackRegistry","BookOpportunityRegistry"], "write": ["checkpoints","decisions","important_notes"]},
    self_healing_behavior={"detection_triggers": ["empty result from research","Playwright failure","memory write failure"], "action": "retry adjusted params rollback CP0 escalate Supreme if 3 fails", "max_retries": 3},
    playwright_usage="supervises PlaywrightOperationsSubEcosystem real tool",
    skill_usage=["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

QualificationEcosystemController = Agent(
    name="QualificationEcosystemController",
    role="Controller L2 QualificationEcosystem piano qualifica dettagliato reproducibilita assurdita velocita",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem=None,
    inputs=["research_handoff_package","checkpoints","important_notes"],
    outputs=["ecosystem_status","reports_to_L1","handoff_ready_signal"],
    decision_logic="SE research handoff validated trigger QualificationLeader teams SE analyst conflict PlanQualityAuditor escalate to self weighted scoring IF GO threshold >=70 approve handoff Planning write decisions IF NO-GO without alternative trigger auto-improvement feedback request new research cycle via ResearchController",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["QualificationLeader","QualificationDecisionLeader"], "collaborates_with": ["ResearchEcosystemController","PlanningEcosystemController"]},
    memory_access={"read": ["BookOpportunityRegistry","ReviewDataRegistry","checkpoints","decisions"], "write": ["QualificationCheckpoints","QualificationDecisions","RiskRegistry","decisions"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","no-go without alternative"], "action": "requalify anomaly flag rollback CP1"},
    skill_usage=["QualificationDecisionSkill","BookNicheDecisionSkill","SelfHealingSkill"],
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

PlanningEcosystemController = Agent(
    name="PlanningEcosystemController",
    role="Controller L2 PlanningEcosystem second-level plan video_structure REQUIRED preservato verbatim",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem=None,
    inputs=["qualification_GO_package","risk_flags"],
    outputs=["planning_status","second_level_plan_validation","production_start_authorization"],
    decision_logic="IF GO package valid trigger StructurePlanningLeader VALIDATION CRITICAL check video_structure field exists not reinterpreted if missing trigger self-healing rollback Qualification IF PlanCoherenceValidator coherent AND ReadinessChecker ready THEN authorize production_start_signal via ProductionStartSignalAgent create CP3 ELSE escalate anomaly",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["StructurePlanningLeader","ProductionReadinessLeader","ContentPlanningLeader"], "collaborates_with": ["QualificationEcosystemController","ProductionEcosystemController"]},
    memory_access={"read": ["QualificationDecisions","RiskRegistry","plans"], "write": ["PlanningCheckpoints","SecondLevelPlans","ProductionStartSignals","plans"]},
    self_healing_behavior={"detection_triggers": ["missing video_structure","incoherent output"], "action": "retry forced read original requirement rollback CP2 critical", "critical": "video_structure missing critical failure"},
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

ProductionEcosystemController = Agent(
    name="ProductionEcosystemController",
    role="Controller L2 ProductionEcosystem scrittura intero libro coerente second-level plan",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem=None,
    inputs=["second_level_plan","production_start_signal","memory_context"],
    outputs=["production_status","manuscript_ready_signal"],
    decision_logic="IF start signal TRUE validated trigger BookWritingLeader IF ContentQualityReviewer consistency fail trigger rollback last chapter checkpoint IF FinalApproval approves trigger handoff Visual",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["BookWritingLeader","ProductionQualityLeader","EditingLeader"], "collaborates_with": ["PlanningEcosystemController","VisualEcosystemController"]},
    memory_access={"read": ["SecondLevelPlans","ProductionStartSignals","decisions"], "write": ["ProductionCheckpoints","ProductionLog","CompletedManuscripts"]},
    self_healing_behavior={"detection_triggers": ["blocked process","incoherent output"], "action": "retry chapter rollback last chapter checkpoint"},
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

VisualEcosystemController = Agent(
    name="VisualEcosystemController",
    role="Controller L2 VisualEcosystem grafiche prompt cover Playwright support",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem=None,
    inputs=["completed_manuscript","second_level_plan"],
    outputs=["visual_status","final_assembly_package"],
    decision_logic="IF manuscript received trigger GraphicDesignLeader CoverDesignLeader parallel IF visual_save via Playwright fails retry 2x then skip_and_log if not cover escalate if cover missing IF all approved create CP_FINAL final assembly",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["GraphicDesignLeader","CoverDesignLeader","VisualPlaywrightLeader","VisualQualityLeader"], "collaborates_with": ["ProductionEcosystemController","MemoryEcosystemController"]},
    memory_access={"read": ["CompletedManuscripts","SecondLevelPlans"], "write": ["GraphicPrompts","GeneratedGraphics","CoverVersions","VisualProductionLog"]},
    self_healing_behavior={"detection_triggers": ["Playwright failure","missing output cover"], "action": "retry skip_and_log non-critical escalate cover"},
    playwright_usage="supervises VisualPlaywrightOperationsTeam",
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

MemoryEcosystemController = Agent(
    name="MemoryEcosystemController",
    role="Controller L2 MemoryEcosystem attivo con agenti gestione validazione checkpoint non storage passivo",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem=None,
    inputs=["read_requests","write_requests","validation_triggers","checkpoint_triggers"],
    outputs=["memory_status","read_responses","write_confirmations","validation_reports"],
    decision_logic="IF read request route MemoryReaderAgent context timestamp IF write request validate via MemoryValidatorAgent before storage IF checkpoint trigger route CheckpointManagerAgent IF gap corruption detected trigger SelfHealing flow",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["MemoryManagerLeader","CheckpointSubLeader","DecisionLogSubLeader"], "collaborates_with": ["AllEcosystemControllers"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes"], "write": ["checkpoints","decisions","plans","hierarchies","important_notes"]},
    self_healing_behavior={"detection_triggers": ["memory write failure","corruption","gap"], "action": "validate restore last valid checkpoint"},
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

SelfHealingEcosystemController = Agent(
    name="SelfHealingEcosystemController",
    role="Controller L2 SelfHealingEcosystem real active always-on healing",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem=None,
    inputs=["anomaly_reports_all_ecosystems","playwright_failures","validation_failures"],
    outputs=["healing_commands","recovery_status","escalation_to_L1","anomaly_logs"],
    decision_logic="IF anomaly report received trigger DetectionLeader DiagnosisLeader RecoveryLeader flow IF recovery fails after max retries escalate Supreme with full diagnosis log ALWAYS log AnomalyLog DiagnosisLog RecoveryLog",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["DetectionLeader","DiagnosisLeader","RecoveryLeader"], "collaborates_with": ["MemoryEcosystemController"]},
    memory_access={"read": ["checkpoints","decisions","important_notes","AnomalyLog"], "write": ["AnomalyLog","DiagnosisLog","RecoveryLog","SelfHealingCheckpoints","important_notes"]},
    self_healing_behavior={"detection": "is healer monitors self via internal validator"},
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

AutoImprovementEcosystemController = Agent(
    name="AutoImprovementEcosystemController",
    role="Controller L2 AutoImprovementEcosystem real continuous improvement impara da outcomes",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem=None,
    inputs=["cycle_outcomes","performance_metrics","self_healing_frequency","feedback_signals"],
    outputs=["improvement_plans","parameter_updates","threshold_updates","learning_logs"],
    decision_logic="IF cycle completed OR periodic trigger THEN trigger FeedbackCollectionLeader ImprovementPlanningLeader ImprovementExecutionLeader flow Update future research quality qualification decisions plan accuracy speed risk sensitivity",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["FeedbackCollectionLeader","ImprovementPlanningLeader","ImprovementExecutionLeader"], "collaborates_with": ["MemoryEcosystemController","ResearchEcosystemController"]},
    memory_access={"read": ["FeedbackRegistry","PerformanceHistory","decisions","important_notes"], "write": ["FeedbackRegistry","ImprovementPlans","PerformanceHistory","LearningLog","important_notes"]},
    self_healing_behavior={"detection_triggers": ["improvement failure"], "action": "log continue non-critical"},
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

ALL_L2 = [ResearchEcosystemController,QualificationEcosystemController,PlanningEcosystemController,ProductionEcosystemController,VisualEcosystemController,MemoryEcosystemController,SelfHealingEcosystemController,AutoImprovementEcosystemController]
print(f"L2 VALIDATED: {len(ALL_L2)} controllers")
