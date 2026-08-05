
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

VisualProductionLog = MemoryComponent(
    name="VisualProductionLog",
    category="important_notes",
    read_agents=['VisualEcosystemController'],
    write_agents=['GraphicDesignLeader', 'CoverDesignLeader', 'VisualPlaywrightLeader'],
    data_schema={'log_id': 'uuid', 'book_id': 'uuid', 'graphic_decisions': 'list', 'cover_decisions': 'list', 'playwright_saves': 'list save confirmations'},
    checkpoint_logic={'creation': 'during visual production log decisions'},
    validation_rules=['book_id required'],
    ecosystem="VisualEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file VisualProductionLog category {'important_notes'} eco {'VisualEcosystem'}")
