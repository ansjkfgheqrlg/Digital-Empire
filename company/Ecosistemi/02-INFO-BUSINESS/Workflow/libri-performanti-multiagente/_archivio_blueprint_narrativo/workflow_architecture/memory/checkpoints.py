
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

checkpoints = MemoryComponent(
    name="checkpoints",
    category="checkpoints",
    read_agents=['SelfHealingEcosystemController', 'All teams on recovery', 'SupremeOrchestratorAgent', 'CheckpointManagerAgent', 'RollbackExecutorAgent'],
    write_agents=['All teams via MemoryWriterAgent', 'CheckpointManagerAgent', 'MemoryManagerLeader'],
    data_schema={'checkpoint_id': 'uuid', 'phase': 'Research Qualification Planning Production Visual SelfHealing AutoImprovement', 'team': 'string', 'timestamp': 'ISO', 'state_snapshot': 'arbitrary state', 'trigger_event': 'end phase before decision before handoff on healing periodic', 'parent_checkpoint_id': 'uuid or None', 'valid': 'bool', 'created_by': 'CheckpointManagerAgent'},
    checkpoint_logic={'creation_triggers': ['end each phase', 'before major decision GO NO-GO', 'before handoff', 'on healing', 'per chapter'], 'storage': 'CheckpointManager versioned parent ref', 'restoration': 'RollbackExecutor + CheckpointManager restore', 'validation': 'MemoryValidator checks alignment decisions plans'},
    validation_rules=['must have phase team timestamp state_snapshot trigger_event valid', 'parent_checkpoint_id required chain', 'readable by SelfHealing'],
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub"
)

print(f"Memory dedicated file checkpoints category {'checkpoints'} eco {'MemoryEcosystem'}")
