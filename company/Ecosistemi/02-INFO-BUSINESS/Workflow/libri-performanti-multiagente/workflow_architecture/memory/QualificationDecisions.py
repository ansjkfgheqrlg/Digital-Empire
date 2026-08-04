
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

QualificationDecisions = MemoryComponent(
    name="QualificationDecisions",
    category="decisions",
    read_agents=['PlanningEcosystemController', 'StructurePlanningLeader'],
    write_agents=['DecisionAggregatorAgent', 'DecisionLoggerAgent'],
    data_schema={'decision_id': 'uuid', 'type': 'GO NO-GO', 'value': 'GO NO-GO', 'reasoning': 'full reasoning weighted', 'scores': 'repro speed absurdity market'},
    checkpoint_logic={'creation': 'every go no-go', 'storage': 'DecisionLogger immutable'},
    validation_rules={'reasoning with evidence', 'all 5 criteria evaluated', 'plan_validity required', 'decision_value GO or NO-GO'},
    ecosystem="QualificationEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file QualificationDecisions category {'decisions'} eco {'QualificationEcosystem'}")
