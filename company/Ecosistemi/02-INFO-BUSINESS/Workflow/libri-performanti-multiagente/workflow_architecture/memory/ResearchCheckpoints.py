
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ResearchCheckpoints = MemoryComponent(
    name="ResearchCheckpoints",
    category="checkpoints",
    read_agents=['ResearchEcosystemController', 'SelfHealingEcosystemController', 'CheckpointManagerAgent', 'RollbackExecutorAgent'],
    write_agents=['AmazonResearchLeader', 'DataPersistenceLeader', 'CheckpointManagerAgent', 'MemoryWriterAgent'],
    data_schema={'phase': 'Research', 'state_snapshot': 'keywords books review raw refs', 'trigger': 'end batch before decision before handoff on healing'},
    checkpoint_logic={'creation_triggers': ['end each batch', 'before decision', 'before handoff', 'on healing'], 'storage': 'CheckpointManager parent ID', 'restoration': 'RollbackExecutor'},
    validation_rules={'trigger_event', 'must have timestamp', 'readable by SelfHealing', 'books_found_count'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ResearchSub"
)

print(f"Memory dedicated file ResearchCheckpoints category {'checkpoints'} eco {'ResearchEcosystem'}")
