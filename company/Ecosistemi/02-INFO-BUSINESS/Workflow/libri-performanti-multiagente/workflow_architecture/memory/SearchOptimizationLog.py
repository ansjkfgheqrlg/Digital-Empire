
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

SearchOptimizationLog = MemoryComponent(
    name="SearchOptimizationLog",
    category="important_notes",
    read_agents=['SearchOptimizationLeader'],
    write_agents=['SearchStrategyOptimizerAgent'],
    data_schema={'failure_type': 'Playwright failure', 'adjusted_params': 'dict timeout user_agent selector'},
    checkpoint_logic={'creation': 'on Playwright failure'},
    validation_rules={'adjusted_params required'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="OptimizationSub"
)

print(f"Memory dedicated file SearchOptimizationLog category {'important_notes'} eco {'ResearchEcosystem'}")
