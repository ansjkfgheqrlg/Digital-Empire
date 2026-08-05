
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

KeywordExpansionLog = MemoryComponent(
    name="KeywordExpansionLog",
    category="important_notes",
    read_agents=['AmazonResearchLeader', 'KeywordExpansionLeader'],
    write_agents=['KeywordVariationGeneratorAgent'],
    data_schema={'keyword_original': 'string', 'variations': 'list', 'strategy': 'string'},
    checkpoint_logic={'creation': 'when empty result retry'},
    validation_rules={'strategy required'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ExpansionSub"
)

print(f"Memory dedicated file KeywordExpansionLog category {'important_notes'} eco {'ResearchEcosystem'}")
