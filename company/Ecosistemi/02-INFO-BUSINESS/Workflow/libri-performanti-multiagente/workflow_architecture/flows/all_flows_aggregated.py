import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Flow

FLOWS = []

FLOWS.append(Flow(
    name="MAIN_PRODUCTION_FLOW",
    start_condition="Nuovo ciclo SupremeOrchestratorAgent L1 crea CP0_INIT hierarchies broadcast start L2",
    phases=[
        {"phase_id":1,"name":"Research Phase Amazon + Review Sites","ecosystem":"ResearchEcosystem","teams":["AmazonKeywordResearchTeam","ReviewAnalysisResearchTeam","DataPersistenceTeam"]},
        {"phase_id":2,"name":"Qualification Phase 5 criteri","ecosystem":"QualificationEcosystem","teams":["QualificationAnalysisTeam","QualificationDecisionTeam"]},
        {"phase_id":3,"name":"Decision Gate GO NO-GO threshold 70","ecosystem":"Qualification->Planning","type":"gate"},
        {"phase_id":4,"name":"Planning Second Level CRITICAL video_structure REQUIRED verbatim","ecosystem":"PlanningEcosystem","teams":["StructurePlanningTeam","ProductionReadinessTeam","ContentPlanningTeam"]},
        {"phase_id":5,"name":"Decision Gate Plan Approval video_structure present","ecosystem":"Planning->Production","type":"gate"},
        {"phase_id":6,"name":"Production Write Book Continuity","ecosystem":"ProductionEcosystem","teams":["BookWritingTeam","ProductionQualityTeam","EditingTeam"]},
        {"phase_id":7,"name":"Visual Graphics Prompts Cover Playwright Support","ecosystem":"VisualEcosystem","teams":["GraphicDesignTeam","CoverDesignTeam","VisualPlaywrightOperationsTeam","VisualQualityTeam"]},
        {"phase_id":8,"name":"Final Assembly CP_FINAL + AutoImprovement trigger","ecosystem":"Global"}
    ],
    decision_gates=[
        {"gate_id":"DG1_GO_NO_GO","location":"after Qualification","logic":"score>=70 AND absurdity FALSE AND too_slow FALSE AND plan_validity TRUE = GO","threshold":70,"on_GO":"Planning","on_NO_GO":"Research new cycle"},
        {"gate_id":"DG2_Plan_Approval","location":"after Planning","logic":"video_structure REQUIRED verbatim present non-empty chapters non-empty details concrete production_start_signal TRUE","critical":"video_structure CP-VIDEO-01 preserve verbatim"},
        {"gate_id":"DG3_Production_Quality","location":"after Production","logic":"completeness + plan compliance + style + consistency + final approval"},
        {"gate_id":"DG4_Visual_Quality","location":"after Visual","logic":"graphics approved or skip non-critical + prompts tracciati + cover final approved critical + Playwright saves confirmed"}
    ],
    rollback_points=["CP0_INIT","CP1_RESEARCH_END","CP2_QUALIFICATION_END","CP3_PLANNING_END","CP4 per chapter + final","CP5_VISUAL_END","CP_FINAL","SelfHealingCheckpoints","any checkpoint via CheckpointManager"],
    completion_criteria="book complete validated approved + graphics approved prompts tracciati + cover final approved + all saved Playwright + checkpoints CP0-CP_FINAL + decisions logged + final assembly ready Amazon",
    involved_ecosystems=["ResearchEcosystem","QualificationEcosystem","PlanningEcosystem","ProductionEcosystem","VisualEcosystem","MemoryEcosystem","SelfHealingEcosystem","AutoImprovementEcosystem","PlaywrightOperationsSubEcosystem"],
    sub_flows=["ResearchFlow","QualificationFlow","PlanningFlow","ProductionFlow","VisualFlow"]
))

FLOWS.append(Flow(
    name="SELF_HEALING_FLOW",
    start_condition="Any anomaly detected DetectionTeam OutputMonitor ErrorDetector AnomalyDetector StallDetector PlaywrightFailureDetector MemoryFailureDetector - 8 triggers missing incoherent blocked failed validation empty result no-go without alternative memory write failure Playwright failure",
    phases=[
        {"phase_id":1,"name":"Detection OutputMonitor ErrorDetector AnomalyDetector StallDetector","team":"DetectionTeam"},
        {"phase_id":2,"name":"Diagnosis RootCause Impact Assessment Recovery Planning","team":"DiagnosisTeam"},
        {"phase_id":3,"name":"Recovery Planning mapping error_type action retry rollback escalate skip_and_log requalify","team":"DiagnosisTeam","agent":"RecoveryPlannerAgent"},
        {"phase_id":4,"name":"Recovery Execution RetryExecutor RollbackExecutor AlternativePath","team":"RecoveryTeam"},
        {"phase_id":5,"name":"Recovery Validation RecoveryValidator","team":"RecoveryTeam"},
        {"phase_id":6,"name":"Memory Update AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes flow_continued True","team":"RecoveryTeam + MemoryManagementTeam"}
    ],
    decision_gates=[
        {"gate_id":"SH_DG1_Detection_Valid","logic":"anomaly report severity location context checkpoint_before error_type one of 8 triggers","on_pass":"Diagnosis","on_fail":"re-detect"},
        {"gate_id":"SH_DG2_Recovery_Success","logic":"recovery validated without data loss workflow resume flow_continued True","on_pass":"resume affected ecosystem","on_fail":"retry count <3 retry else escalate L2 then Supreme L1"}
    ],
    rollback_points=["checkpoint_before anomaly","last valid checkpoint parent chain any CP0-CP_FINAL","SelfHealingCheckpoints","CheckpointSubEcosystem checkpoints"],
    completion_criteria="workflow resumed without data loss OR escalated L1 full diagnosis log AnomalyLog DiagnosisLog RecoveryLog memory_updated True checkpoint_restored True flow_continued True per handle_failure schema",
    involved_ecosystems=["SelfHealingEcosystem","MemoryEcosystem","All affected ecosystems"],
    sub_flows=["DetectionSubFlow","DiagnosisSubFlow","RecoverySubFlow"]
))

FLOWS.append(Flow(
    name="AUTO_IMPROVEMENT_FLOW",
    start_condition="Completion any production cycle CP_FINAL OR periodic trigger N cycles OR Supreme when GO_rate low <20% OR self-healing frequency high",
    phases=[
        {"phase_id":1,"name":"Outcome Collection OutcomeCollector PerformanceMetrics PatternDetector","team":"FeedbackCollectionTeam"},
        {"phase_id":2,"name":"Performance Analysis 6 feedback signals qualification outcomes speed metrics book performance signals self-healing frequency plan validity memory patterns","team":"FeedbackCollectionTeam","agent":"PerformanceMetricsAgent"},
        {"phase_id":3,"name":"Pattern Detection recurring positive negative","team":"FeedbackCollectionTeam","agent":"PatternDetectorAgent"},
        {"phase_id":4,"name":"Improvement Planning analyze rank write plans 5 targets future research quality future qualification decisions future plan accuracy production flow speed risk sensitivity","team":"ImprovementPlanningTeam"},
        {"phase_id":5,"name":"Improvement Execution ParameterAdjuster ThresholdUpdater WorkflowOptimizer LearningLogger generate_improvement_signal source_phase outcome_summary improvement_suggestion target memory_write True","team":"ImprovementExecutionTeam"},
        {"phase_id":6,"name":"Validation Changes at least one measurable improvement LearningLog important_notes read by Research Qualification next cycle","team":"ImprovementExecutionTeam"}
    ],
    decision_gates=[
        {"gate_id":"AI_DG1_Feedback_Complete","logic":"feedback collected outcome_summary at least one cycle"},
        {"gate_id":"AI_DG2_Improvement_Valid","logic":"improvement plan targeting one of 5 improvement_targets suggestion derived outcome"},
        {"gate_id":"AI_DG3_Improvement_Applied","logic":"at least one measurable improvement applied logged LearningLog memory_write True"}
    ],
    rollback_points=["FeedbackRegistry before","PerformanceHistory last valid","ImprovementPlans previous","LearningLog before","PatternRegistry before"],
    completion_criteria="almeno una measurable improvement applicata loggata LearningLog important_notes letta da future research cycles future qualification decisions per generate_improvement_signal schema source_phase outcome_summary improvement_suggestion target next cycle memory_write True - targets 5 improved",
    involved_ecosystems=["AutoImprovementEcosystem","MemoryEcosystem","ResearchEcosystem","QualificationEcosystem","SelfHealingEcosystem","All ecosystems parameter updates"],
    sub_flows=["FeedbackSubFlow","PlanningSubFlow","ExecutionSubFlow"]
))

FLOWS.append(Flow(
    name="MEMORY_MAINTENANCE_FLOW",
    start_condition="Periodic trigger M cycles time OR triggered MemoryValidatorAgent corruption gap detected OR SelfHealing memory write failure",
    phases=[
        {"phase_id":1,"name":"Consistency Check MemoryValidatorAgent across 35 components checkpoints align decisions plans hierarchies important_notes"},
        {"phase_id":2,"name":"Gap Detection missing checkpoint missing decision missing plan hierarchy gap important_notes gap"},
        {"phase_id":3,"name":"Corruption Detection checkpoint invalid flag decision empty reasoning plan missing required fields hierarchy corrupted"},
        {"phase_id":4,"name":"Cleanup Optimization MemoryManagementTeam CheckpointSub DecisionLogSub deduplication without loss trace cache frequently read data checkpoint storage prune old preserving traceability restore corrupted last valid"},
        {"phase_id":5,"name":"Validation Post-Cleanup MemoryValidatorAgent re-validate consistent optimized"}
    ],
    decision_gates=[
        {"gate_id":"MM_DG1_Consistency_Pass","logic":"consistency passes OR gaps corruption detected proceed cleanup"},
        {"gate_id":"MM_DG2_Cleanup_Valid","logic":"after cleanup validation passes memory consistent optimized gaps repaired flagged"}
    ],
    rollback_points=["last valid checkpoint before maintenance","Memory state snapshot before cleanup via CheckpointManager self_healing checkpoint","DecisionLog before","hierarchies before"],
    completion_criteria="memory consistent optimized per validation all gaps repaired flagged important_notes corruption restored last valid checkpoint chain valid parent IDs all categories 35 readable via MemoryReaderAgent hierarchy 7 levels valid traceability OK",
    involved_ecosystems=["MemoryEcosystem","SelfHealingEcosystem","All ecosystems memory usage"],
    sub_flows=["ConsistencySubFlow","GapSubFlow","CorruptionSubFlow","CleanupSubFlow"]
))

FLOWS.append(Flow(
    name="PLAYWRIGHT_OPERATIONS_FLOW",
    start_condition="Ogni volta ResearchEcosystem VisualEcosystem richiede operazioni Playwright real operational tool integration",
    phases=[
        {"phase_id":1,"name":"Navigation NavigatorMicroAgent AmazonPageNavigator ReviewSiteNavigator VisualNavigator real tool navigate_amazon_keyword_search navigate_review_site"},
        {"phase_id":2,"name":"Data Capture Extraction DataCaptureMicroAgent AmazonDetailExtractor ReviewDataCapture VisualCapture extract_data selectors title author ratings"},
        {"phase_id":3,"name":"Screenshot Raw Data ScreenshotMicroAgent screenshot raw_data saving"},
        {"phase_id":4,"name":"Save Results SaveAgent VisualSaveAgent SaveMicroAgent VisualSaveMicroAgent save_results visual_save results sources URLs notes graphics cover"},
        {"phase_id":5,"name":"Error Handling Self-Healing ErrorHandlerAgent handle_error retry alternative strategies timeout++ user_agent rotate max 3 escalate DetectionTeam"}
    ],
    decision_gates=[
        {"gate_id":"PW_DG1_Navigation_Success","logic":"navigation result page_loaded_flag True","on_pass":"Data Capture","on_fail":"RetryExecutor retry via ErrorHandlerAgent adjusted params"},
        {"gate_id":"PW_DG2_Save_Success","logic":"save confirmation saved_ref valid via SaveValidator","on_pass":"flow complete","on_fail":"retry save"}
    ],
    rollback_points=["checkpoint_before navigation","last valid ResearchCheckpoint","SelfHealingCheckpoint before Playwright operation"],
    completion_criteria="navigation success page loaded data captured extraction success screenshot if needed ref valid save confirmation saved_ref valid via Validator error handling retry escalate logged all saved results sources URLs notes useful material via Playwright saved confirmed",
    involved_ecosystems=["ResearchEcosystem","VisualEcosystem","MemoryEcosystem","SelfHealingEcosystem","PlaywrightOperationsSubEcosystem"],
    sub_flows=["NavigationSubFlow","ExtractionSubFlow","SaveSubFlow"]
))

print(f"FLOWS EXPANDED FIXED: {len(FLOWS)} flows")
for f in FLOWS:
    print(f"  {f.name}: {len(f.phases)} phases, {len(f.decision_gates)} gates, {len(f.rollback_points)} rollback")
