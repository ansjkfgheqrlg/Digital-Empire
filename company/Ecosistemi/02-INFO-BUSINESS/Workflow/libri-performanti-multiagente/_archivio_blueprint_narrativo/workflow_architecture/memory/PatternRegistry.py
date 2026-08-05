
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

PatternRegistry = MemoryComponent(
    name="PatternRegistry",
    category="important_notes",
    read_agents=['ImprovementPlanningLeader'],
    write_agents=['PatternDetectorAgent'],
    data_schema={'pattern_id': 'uuid', 'pattern_type': 'positive negative recurring', 'description': 'string', 'frequency': 'int', 'impact': 'high medium low'},
    checkpoint_logic={'creation': 'when pattern detected by PatternDetectorAgent'},
    validation_rules=['pattern_type required', 'description required'],
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackSub"
)

print(f"Memory dedicated file PatternRegistry category {'important_notes'} eco {'AutoImprovementEcosystem'}")
