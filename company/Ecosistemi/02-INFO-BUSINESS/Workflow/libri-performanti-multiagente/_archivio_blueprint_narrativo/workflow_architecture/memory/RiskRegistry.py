
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

RiskRegistry = MemoryComponent(
    name="RiskRegistry",
    category="important_notes",
    read_agents=['QualificationDecisionLeader', 'StructurePlanningLeader'],
    write_agents=['AbsurdityDetectorAgent', 'RiskFlagManagerAgent'],
    data_schema={'risk_id': 'uuid', 'category': 'absurdity reproducibility speed market plan_validity', 'content': 'risk description', 'severity': 'critical high medium low'},
    checkpoint_logic={'creation': 'when risk detected'},
    validation_rules={'severity required', 'category required'},
    ecosystem="QualificationEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file RiskRegistry category {'important_notes'} eco {'QualificationEcosystem'}")
