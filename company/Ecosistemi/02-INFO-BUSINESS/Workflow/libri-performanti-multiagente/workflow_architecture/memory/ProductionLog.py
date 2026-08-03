
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ProductionLog = MemoryComponent(
    name="ProductionLog",
    category="important_notes",
    read_agents=['VisualEcosystemController', 'GraphicDesignLeader'],
    write_agents=['ChapterWriterAgent', 'ConsistencyCheckerAgent', 'ProductionLogWriterAgent'],
    data_schema={'log_id': 'uuid', 'book_id': 'uuid', 'decisions_made': 'list chapter decision reasoning', 'consistency_checks': 'list', 'deviations': 'list'},
    checkpoint_logic={'creation': 'during writing log decisions', 'checkpoint': 'ProductionCheckpoint per chapter'},
    validation_rules=['decisions_made required', 'book_id required'],
    ecosystem="ProductionEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file ProductionLog category {'important_notes'} eco {'ProductionEcosystem'}")
