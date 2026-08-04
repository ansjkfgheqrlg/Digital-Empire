
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ReviewDataRegistry = MemoryComponent(
    name="ReviewDataRegistry",
    category="important_notes",
    read_agents=['QualificationLeader'],
    write_agents=['ReviewDataExtractorAgent'],
    data_schema={'review_data_id': 'uuid', 'site_url': 'url review analysis', 'linked_book_id': 'uuid'},
    checkpoint_logic={'creation': 'after ReviewDataValidator'},
    validation_rules={'site_url must be review analysis site'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file ReviewDataRegistry category {'important_notes'} eco {'ResearchEcosystem'}")
