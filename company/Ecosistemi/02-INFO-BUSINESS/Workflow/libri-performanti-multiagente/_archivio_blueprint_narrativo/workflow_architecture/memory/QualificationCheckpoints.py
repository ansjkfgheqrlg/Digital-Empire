
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

QualificationCheckpoints = MemoryComponent(
    name="QualificationCheckpoints",
    category="checkpoints",
    read_agents=['QualificationEcosystemController', 'PlanningEcosystemController'],
    write_agents=['QualificationLeader', 'CheckpointManagerAgent'],
    data_schema={'phase': 'Qualification', 'state_snapshot': 'evaluated GO NO-GO counts plan_validity'},
    checkpoint_logic={'creation_triggers': ['after evaluation', 'before GO NO-GO', 'before handoff Planning', 'on healing']},
    validation_rules=['GO NO-GO counts', 'plan_validity flag'],
    ecosystem="QualificationEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file QualificationCheckpoints category {'checkpoints'} eco {'QualificationEcosystem'}")
