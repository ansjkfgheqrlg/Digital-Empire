
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

QualificationPlans = MemoryComponent(
    name="QualificationPlans",
    category="plans",
    read_agents=['PlanningEcosystemController'],
    write_agents=['QualificationReportWriterAgent', 'PlanStorageAgent'],
    data_schema={'plan_id': 'uuid', 'criteria_evaluation': 'reproducibility absurdity production_speed plan_validity business_alignment'},
    checkpoint_logic={'creation': 'when plan approved validated', 'validation': 'PlanQualityAuditor'},
    validation_rules={'evidence each', 'all 5 criteria present'},
    ecosystem="QualificationEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file QualificationPlans category {'plans'} eco {'QualificationEcosystem'}")
