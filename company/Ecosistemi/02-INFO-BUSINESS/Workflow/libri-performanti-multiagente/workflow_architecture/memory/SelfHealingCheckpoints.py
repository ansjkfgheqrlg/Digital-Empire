
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

SelfHealingCheckpoints = MemoryComponent(
    name="SelfHealingCheckpoints",
    category="checkpoints",
    read_agents=['SelfHealingEcosystemController', 'RollbackExecutorAgent', 'RecoveryValidatorAgent'],
    write_agents=['CheckpointManagerAgent', 'MemoryWriterAgent', 'RecoveryLeader', 'DetectionLeader'],
    data_schema={'checkpoint_id': 'uuid', 'type': 'self_healing', 'phase': 'string', 'timestamp': 'ISO', 'state_before': 'snapshot before anomaly', 'state_after': 'snapshot after recovery', 'trigger_event': 'on_self_healing_activation before_recovery after_recovery', 'parent_checkpoint_id': 'uuid', 'valid': 'bool', 'related_anomaly_id': 'ref AnomalyLog'},
    checkpoint_logic={'creation': 'before and after each recovery and on self-healing activation', 'restoration': 'target for RollbackExecutor', 'validation': 'MemoryValidator'},
    validation_rules=['type self_healing', 'trigger_event required', 'parent_checkpoint_id required', 'related_anomaly_id required'],
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file SelfHealingCheckpoints category {'checkpoints'} eco {'SelfHealingEcosystem'}")
