
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

EditingLog = MemoryComponent(
    name="EditingLog",
    category="important_notes",
    read_agents=['ProductionQualityLeader'],
    write_agents=['EditingCoordinatorAgent', 'FinalProofreaderAgent'],
    data_schema={'editing_id': 'uuid', 'changes': 'list', 'proofread_status': 'bool'},
    checkpoint_logic={'creation': 'during editing'},
    validation_rules=['proofread_status required'],
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub"
)

print(f"Memory dedicated file EditingLog category {'important_notes'} eco {'ProductionEcosystem'}")
