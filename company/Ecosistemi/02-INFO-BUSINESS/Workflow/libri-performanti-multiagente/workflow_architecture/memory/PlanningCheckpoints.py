
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

PlanningCheckpoints = MemoryComponent(
    name="PlanningCheckpoints",
    category="checkpoints",
    read_agents=['PlanningEcosystemController', 'ProductionEcosystemController'],
    write_agents=['StructurePlanningLeader', 'ProductionReadinessLeader'],
    data_schema={'phase': 'Planning', 'state_snapshot': 'video_structure_present chapters_count details_complete readiness_confirmed'},
    checkpoint_logic={'creation_triggers': ['after video_structure', 'after chapters', 'after details', 'validation', 'production_start_signal']},
    validation_rules=['video_structure_present flag required'],
    ecosystem="PlanningEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file PlanningCheckpoints category {'checkpoints'} eco {'PlanningEcosystem'}")
