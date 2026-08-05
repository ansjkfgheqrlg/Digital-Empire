
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ImprovementPlans = MemoryComponent(
    name="ImprovementPlans",
    category="plans",
    read_agents=['ImprovementExecutionLeader', 'ParameterAdjusterAgent'],
    write_agents=['ImprovementPlanWriterAgent', 'ImprovementPlanningLeader', 'PlanStorageAgent'],
    data_schema={'plan_id': 'uuid', 'plan_type': 'improvement', 'target': 'future research quality future qualification decisions future plan accuracy production flow speed risk detection sensitivity', 'source_feedback_id': 'ref FeedbackRegistry', 'improvement_suggestion': 'derived from outcome', 'priority': 'high medium low', 'impact_estimate': 'string', 'feasibility': 'string', 'steps': 'list steps', 'status': 'planned executing applied validated'},
    checkpoint_logic={'creation': 'after ImprovementPlanning', 'storage': 'PlanStorage', 'execution': 'ImprovementExecutionTeam'},
    validation_rules=['target must be one of 5 improvement_targets', 'improvement_suggestion required', 'priority required'],
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub"
)

print(f"Memory dedicated file ImprovementPlans category {'plans'} eco {'AutoImprovementEcosystem'}")
