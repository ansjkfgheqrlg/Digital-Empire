"""
7-LEVEL HIERARCHY - EXACTLY 7 LEVELS
Level 1 to Level 7 assignment for all agents
"""

from core import HierarchyLevel

HIERARCHY_DEFINITION = {
    1: {
        "name": "LEVEL 1 — SUPREME ORCHESTRATOR",
        "description": "Single top-level agent that controls entire workflow. Sees everything. Decides macro. Receives reports from L2. Can override any decision. Manages global state.",
        "agents": ["SupremeOrchestratorAgent"],
        "controls": [2,3,4,5,6,7],
        "reports_to": None,
        "responsibilities": ["global_state_management", "macro_decisions", "override_authority", "cycle_initiation", "final_approval"]
    },
    2: {
        "name": "LEVEL 2 — ECOSYSTEM CONTROLLERS",
        "description": "Control major ecosystems, manage teams, report to L1",
        "agents": [
            "ResearchEcosystemController",
            "QualificationEcosystemController",
            "PlanningEcosystemController",
            "ProductionEcosystemController",
            "VisualEcosystemController",
            "MemoryEcosystemController",
            "SelfHealingEcosystemController",
            "AutoImprovementEcosystemController"
        ],
        "controls": [3,4,5,6,7],
        "reports_to": [1],
        "ecosystems_controlled": [
            "ResearchEcosystem",
            "QualificationEcosystem",
            "PlanningEcosystem",
            "ProductionEcosystem",
            "VisualEcosystem",
            "MemoryEcosystem",
            "SelfHealingEcosystem",
            "AutoImprovementEcosystem"
        ]
    },
    3: {
        "name": "LEVEL 3 — TEAM LEADERS",
        "description": "Each team leader manages team members, coordinates internal work, handles intra-team communication, reports to ecosystem controller",
        "agents": [
            "AmazonResearchLeader",
            "ReviewResearchLeader",
            "DataPersistenceLeader",
            "QualificationLeader",
            "QualificationDecisionLeader",
            "StructurePlanningLeader",
            "ProductionReadinessLeader",
            "BookWritingLeader",
            "ProductionQualityLeader",
            "GraphicDesignLeader",
            "CoverDesignLeader",
            "VisualPlaywrightLeader",
            "MemoryManagerLeader",
            "DetectionLeader",
            "DiagnosisLeader",
            "RecoveryLeader",
            "FeedbackCollectionLeader",
            "ImprovementPlanningLeader",
            "ImprovementExecutionLeader"
        ],
        "controls": [4,5,6,7],
        "reports_to": [2],
        "count_teams": 19
    },
    4: {
        "name": "LEVEL 4 — SENIOR AGENTS",
        "description": "Specialized agents with decision-making authority, tactical decisions without escalating unless threshold crossed",
        "agents": [
            "ReproducibilityAnalystAgent",
            "AbsurdityDetectorAgent",
            "ProductionSpeedAnalystAgent",
            "MarketAlignmentAnalystAgent",
            "PlanQualityAuditorAgent",
            "DecisionAggregatorAgent",
            "RiskFlagManagerAgent",
            "VideoStructureArchitectAgent",
            "ChapterDesignerAgent",
            "DetailFillerAgent",
            "PlanCoherenceValidatorAgent",
            "ConsistencyCheckerAgent",
            "StyleEnforcerAgent",
            "ContentQualityReviewerAgent",
            "ManuscriptValidatorAgent",
            "PlanComplianceCheckerAgent",
            "RootCauseAnalystAgent",
            "ImpactAssessorAgent",
            "RecoveryPlannerAgent",
            "OutputMonitorAgent",
            "AnomalyDetectorAgent",
            "ImprovementAnalystAgent",
            "PriorityRankerAgent",
            "CoverConceptAgent"
        ],
        "controls": [5,6,7],
        "reports_to": [3],
        "decision_authority_threshold": "can decide without escalation if impact < team_level and no cross-team effect"
    },
    5: {
        "name": "LEVEL 5 — OPERATIONAL AGENTS",
        "description": "Execute core tasks: research, writing, evaluation, graphic creation, data collection, Playwright operations",
        "agents": [
            "KeywordGeneratorAgent",
            "AmazonSearchAgent",
            "AmazonDataExtractorAgent",
            "ReviewSiteFinderAgent",
            "ReviewDataExtractorAgent",
            "PlaywrightSaveAgent",
            "QualificationReportWriterAgent",
            "ReadinessCheckerAgent",
            "ResourceEstimatorAgent",
            "ProductionStartSignalAgent",
            "ChapterWriterAgent",
            "GraphicPromptCreatorAgent",
            "GraphicGeneratorAgent",
            "CoverPromptCreatorAgent",
            "CoverGeneratorAgent",
            "MemoryWriterAgent",
            "MemoryReaderAgent",
            "RetryExecutorAgent",
            "OutcomeCollectorAgent",
            "ParameterAdjusterAgent"
        ],
        "controls": [6,7],
        "reports_to": [4,3],
        "execution_model": "follow instructions from senior and leaders, report output"
    },
    6: {
        "name": "LEVEL 6 — SUPPORT AGENTS",
        "description": "Supporting functions: memory read/write, checkpoint management, data formatting, validation, logging, monitoring",
        "agents": [
            "DataFormatterAgent",
            "SaveValidatorAgent",
            "ReviewScoreNormalizerAgent",
            "AmazonResultsValidatorAgent",
            "ReviewDataValidatorAgent",
            "DataFormatterAgent",
            "FinalApprovalAgent",
            "VisualPlaywrightSaveAgent",
            "GraphicQualityReviewerAgent",
            "CoverQualityReviewerAgent",
            "HierarchyManagerAgent",
            "ImportantNotesAgent",
            "PerformanceMetricsAgent",
            "PatternDetectorAgent",
            "ImprovementPlanWriterAgent",
            "ThresholdUpdaterAgent",
            "WorkflowOptimizerAgent",
            "MemoryValidatorAgent",
            "CheckpointManagerAgent",
            "DecisionLoggerAgent",
            "PlanStorageAgent",
            "GraphicRevisionAgent",
            "CoverRevisionAgent",
            "RollbackExecutorAgent",
            "RecoveryValidatorAgent"
        ],
        "controls": [7],
        "reports_to": [5,4,3]
    },
    7: {
        "name": "LEVEL 7 — MICRO-AGENTS",
        "description": "Small single-purpose agents handling atomic tasks: single API call, single Playwright navigation, single data extraction, single validation check. Spawned and managed by higher levels.",
        "agents": [
            "PlaywrightNavigatorMicroAgent",
            "PlaywrightDataCaptureMicroAgent",
            "PlaywrightScreenshotMicroAgent",
            "PlaywrightErrorHandlerAgent",
            "VisualPlaywrightNavigatorAgent",
            "ErrorDetectorAgent",
            "StallDetectorAgent",
            "AlternativePathAgent"
        ],
        "controls": [],
        "reports_to": [6,5,4,3],
        "spawn_model": "spawned on demand by L3-L6, auto-terminated after atomic task"
    }
}

# Validation: exactly 7 levels
assert len(HIERARCHY_DEFINITION) == 7, "Architecture must have exactly 7 hierarchy levels"

# Count total agents
total_agents = sum(len(level["agents"]) for level in HIERARCHY_DEFINITION.values())
print(f"HIERARCHY VALIDATED: 7 levels, {total_agents} agents assigned")
