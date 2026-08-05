
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Flow

MAIN_PRODUCTION_FLOW = Flow(
    name="MAIN_PRODUCTION_FLOW",
    start_condition="""Nuovo ciclo SupremeOrchestratorAgent L1 crea CP0_INIT hierarchies broadcast start L2""",
    phases=[{'phase_id': 1, 'name': 'Research Phase Amazon + Review Sites', 'ecosystem': 'ResearchEcosystem', 'teams': ['AmazonKeywordResearchTeam', 'ReviewAnalysisResearchTeam', 'DataPersistenceTeam']}, {'phase_id': 2, 'name': 'Qualification Phase 5 criteri', 'ecosystem': 'QualificationEcosystem', 'teams': ['QualificationAnalysisTeam', 'QualificationDecisionTeam']}, {'phase_id': 3, 'name': 'Decision Gate GO NO-GO threshold 70', 'ecosystem': 'Qualification->Planning', 'type': 'gate'}, {'phase_id': 4, 'name': 'Planning Second Level CRITICAL video_structure REQUIRED verbatim', 'ecosystem': 'PlanningEcosystem', 'teams': ['StructurePlanningTeam', 'ProductionReadinessTeam', 'ContentPlanningTeam']}, {'phase_id': 5, 'name': 'Decision Gate Plan Approval video_structure present', 'ecosystem': 'Planning->Production', 'type': 'gate'}, {'phase_id': 6, 'name': 'Production Write Book Continuity', 'ecosystem': 'ProductionEcosystem', 'teams': ['BookWritingTeam', 'ProductionQualityTeam', 'EditingTeam']}, {'phase_id': 7, 'name': 'Visual Graphics Prompts Cover Playwright Support', 'ecosystem': 'VisualEcosystem', 'teams': ['GraphicDesignTeam', 'CoverDesignTeam', 'VisualPlaywrightOperationsTeam', 'VisualQualityTeam']}, {'phase_id': 8, 'name': 'Final Assembly CP_FINAL + AutoImprovement trigger', 'ecosystem': 'Global'}],
    decision_gates=[{'gate_id': 'DG1_GO_NO_GO', 'location': 'after Qualification', 'logic': 'score>=70 AND absurdity FALSE AND too_slow FALSE AND plan_validity TRUE = GO', 'threshold': 70, 'on_GO': 'Planning', 'on_NO_GO': 'Research new cycle'}, {'gate_id': 'DG2_Plan_Approval', 'location': 'after Planning', 'logic': 'video_structure REQUIRED verbatim present non-empty chapters non-empty details concrete production_start_signal TRUE', 'critical': 'video_structure CP-VIDEO-01 preserve verbatim'}, {'gate_id': 'DG3_Production_Quality', 'location': 'after Production', 'logic': 'completeness + plan compliance + style + consistency + final approval'}, {'gate_id': 'DG4_Visual_Quality', 'location': 'after Visual', 'logic': 'graphics approved or skip non-critical + prompts tracciati + cover final approved critical + Playwright saves confirmed'}],
    rollback_points=['CP0_INIT', 'CP1_RESEARCH_END', 'CP2_QUALIFICATION_END', 'CP3_PLANNING_END', 'CP4 per chapter + final', 'CP5_VISUAL_END', 'CP_FINAL', 'SelfHealingCheckpoints', 'any checkpoint via CheckpointManager'],
    completion_criteria="""book complete validated approved + graphics approved prompts tracciati + cover final approved + all saved Playwright + checkpoints CP0-CP_FINAL + decisions logged + final assembly ready Amazon""",
    involved_ecosystems=['ResearchEcosystem', 'QualificationEcosystem', 'PlanningEcosystem', 'ProductionEcosystem', 'VisualEcosystem', 'MemoryEcosystem', 'SelfHealingEcosystem', 'AutoImprovementEcosystem', 'PlaywrightOperationsSubEcosystem'],
    sub_flows=['ResearchFlow', 'QualificationFlow', 'PlanningFlow', 'ProductionFlow', 'VisualFlow']
)

print(f"Flow dedicated file MAIN_PRODUCTION_FLOW - phases {len(MAIN_PRODUCTION_FLOW.phases)} gates {len(MAIN_PRODUCTION_FLOW.decision_gates)}")
