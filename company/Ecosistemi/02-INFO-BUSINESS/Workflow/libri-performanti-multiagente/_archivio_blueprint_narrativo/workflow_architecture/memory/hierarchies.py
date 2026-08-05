
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

hierarchies = MemoryComponent(
    name="hierarchies",
    category="hierarchies",
    read_agents=['All teams', 'All agents for routing escalation'],
    write_agents=['Orchestrator SupremeOrchestratorAgent via HierarchyManagerAgent', 'MemoryWriterAgent'],
    data_schema={'agent_id': 'uuid', 'agent_name': 'string', 'hierarchy_level': 'int 1-7', 'team': 'string', 'ecosystem': 'string', 'reports_to': 'list', 'manages': 'list', 'role': 'string', 'timestamp': 'ISO'},
    checkpoint_logic={'creation': 'at workflow initialization and on update orchestrator', 'validation': 'MemoryValidator verifies not corrupted', 'storage': 'HierarchyManagerAgent', 'update': 'only via SupremeOrchestratorAgent'},
    validation_rules=['agent_name unique required', 'hierarchy_level 1-7 required', 'reports_to required array', 'manages required', 'exactly 7 levels must exist'],
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub"
)

print(f"Memory dedicated file hierarchies category {'hierarchies'} eco {'MemoryEcosystem'}")
