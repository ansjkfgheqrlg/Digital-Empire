
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

BookOpportunityRegistry = MemoryComponent(
    name="BookOpportunityRegistry",
    category="important_notes",
    read_agents=['QualificationLeader', 'CoverConceptAgent', 'MemoryReaderAgent'],
    write_agents=['AmazonDataExtractorAgent', 'DataFormatterAgent', 'PlaywrightSaveAgent'],
    data_schema={'book_id': 'uuid', 'title': 'string', 'amazon_url': 'url', 'keyword_match': 'string', 'metadata': 'dict', 'observed_signals': 'performance Amazon+review', 'raw_data_ref': 'Playwright ref'},
    checkpoint_logic={'creation': 'after extraction', 'validation': 'AmazonResultsValidator'},
    validation_rules={'raw_data_ref Playwright required', 'amazon_url valid', 'title not empty'},
    ecosystem="ResearchEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file BookOpportunityRegistry category {'important_notes'} eco {'ResearchEcosystem'}")
