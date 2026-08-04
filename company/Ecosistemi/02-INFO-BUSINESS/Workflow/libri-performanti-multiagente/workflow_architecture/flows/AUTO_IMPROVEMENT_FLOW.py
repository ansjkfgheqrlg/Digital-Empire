
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Flow

AUTO_IMPROVEMENT_FLOW = Flow(
    name="AUTO_IMPROVEMENT_FLOW",
    start_condition="""Completion any production cycle CP_FINAL OR periodic trigger N cycles OR Supreme when GO_rate low <20% OR self-healing frequency high""",
    phases=[{'phase_id': 1, 'name': 'Outcome Collection OutcomeCollector PerformanceMetrics PatternDetector', 'team': 'FeedbackCollectionTeam'}, {'phase_id': 2, 'name': 'Performance Analysis 6 feedback signals qualification outcomes speed metrics book performance signals self-healing frequency plan validity memory patterns', 'team': 'FeedbackCollectionTeam', 'agent': 'PerformanceMetricsAgent'}, {'phase_id': 3, 'name': 'Pattern Detection recurring positive negative', 'team': 'FeedbackCollectionTeam', 'agent': 'PatternDetectorAgent'}, {'phase_id': 4, 'name': 'Improvement Planning analyze rank write plans 5 targets future research quality future qualification decisions future plan accuracy production flow speed risk sensitivity', 'team': 'ImprovementPlanningTeam'}, {'phase_id': 5, 'name': 'Improvement Execution ParameterAdjuster ThresholdUpdater WorkflowOptimizer LearningLogger generate_improvement_signal source_phase outcome_summary improvement_suggestion target memory_write True', 'team': 'ImprovementExecutionTeam'}, {'phase_id': 6, 'name': 'Validation Changes at least one measurable improvement LearningLog important_notes read by Research Qualification next cycle', 'team': 'ImprovementExecutionTeam'}],
    decision_gates=[{'gate_id': 'AI_DG1_Feedback_Complete', 'logic': 'feedback collected outcome_summary at least one cycle'}, {'gate_id': 'AI_DG2_Improvement_Valid', 'logic': 'improvement plan targeting one of 5 improvement_targets suggestion derived outcome'}, {'gate_id': 'AI_DG3_Improvement_Applied', 'logic': 'at least one measurable improvement applied logged LearningLog memory_write True'}],
    rollback_points=['FeedbackRegistry before', 'PerformanceHistory last valid', 'ImprovementPlans previous', 'LearningLog before', 'PatternRegistry before'],
    completion_criteria="""almeno una measurable improvement applicata loggata LearningLog important_notes letta da future research cycles future qualification decisions per generate_improvement_signal schema source_phase outcome_summary improvement_suggestion target next cycle memory_write True - targets 5 improved""",
    involved_ecosystems=['AutoImprovementEcosystem', 'MemoryEcosystem', 'ResearchEcosystem', 'QualificationEcosystem', 'SelfHealingEcosystem', 'All ecosystems parameter updates'],
    sub_flows=['FeedbackSubFlow', 'PlanningSubFlow', 'ExecutionSubFlow']
)

print(f"Flow dedicated file AUTO_IMPROVEMENT_FLOW - phases {len(AUTO_IMPROVEMENT_FLOW.phases)} gates {len(AUTO_IMPROVEMENT_FLOW.decision_gates)}")
