
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ResearchDecisions = MemoryComponent(
    name="ResearchDecisions",
    category="decisions",
    read_agents=['ResearchEcosystemController', 'QualificationEcosystemController'],
    write_agents=['AmazonResearchLeader', 'MemoryWriterAgent'],
    data_schema={'decision_id': 'uuid', 'type': 'keyword_selection', 'value': 'string', 'reasoning': 'why'},
    checkpoint_logic={'creation': 'every decision point', 'storage': 'DecisionLogger append-only'},
    validation_rules={'reasoning required', 'timestamp'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file ResearchDecisions category {'decisions'} eco {'ResearchEcosystem'}")
