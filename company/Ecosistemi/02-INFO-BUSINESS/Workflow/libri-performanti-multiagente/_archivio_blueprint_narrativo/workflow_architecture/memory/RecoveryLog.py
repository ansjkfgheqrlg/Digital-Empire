
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

RecoveryLog = MemoryComponent(
    name="RecoveryLog",
    category="important_notes",
    read_agents=['SelfHealingEcosystemController', 'SupremeOrchestratorAgent'],
    write_agents=['RetryExecutorAgent', 'RollbackExecutorAgent', 'AlternativePathAgent', 'RecoveryValidatorAgent', 'EscalationManagerAgent'],
    data_schema={'recovery_id': 'uuid', 'anomaly_id': 'ref', 'diagnosis_id': 'ref', 'action_taken': 'retry rollback escalate skip_and_log requalify', 'execution_result': 'success fail', 'checkpoint_restored': 'bool', 'memory_updated': 'bool', 'flow_continued': 'bool', 'retry_count': 'int', 'timestamp': 'ISO', 'validation_result': 'recovered without data loss or escalated'},
    checkpoint_logic={'creation': 'after each recovery execution', 'storage': 'append handle_failure schema must include phase error_type checkpoint_restored action_taken memory_updated flow_continued'},
    validation_rules=['action_taken required one of 5', 'checkpoint_restored bool required', 'memory_updated bool required', 'flow_continued bool required per handle_failure'],
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub"
)

print(f"Memory dedicated file RecoveryLog category {'important_notes'} eco {'SelfHealingEcosystem'}")
