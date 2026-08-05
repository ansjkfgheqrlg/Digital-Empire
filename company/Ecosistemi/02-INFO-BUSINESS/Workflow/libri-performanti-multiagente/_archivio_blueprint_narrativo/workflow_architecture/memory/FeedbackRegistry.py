
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

FeedbackRegistry = MemoryComponent(
    name="FeedbackRegistry",
    category="important_notes",
    read_agents=['ImprovementPlanningLeader', 'ResearchEcosystemController'],
    write_agents=['OutcomeCollectorAgent', 'MemoryWriterAgent'],
    data_schema={'feedback_id': 'uuid', 'source_phase': 'string', 'outcome_summary': 'GO_rate NO_GO reasons production_time self_healing_frequency plan_validity', 'timestamp': 'ISO', 'cycle_id': 'uuid production cycle'},
    checkpoint_logic={'creation': 'upon outcome collection after cycle or periodic', 'storage': 'append read by ImprovementPlanning for analysis'},
    validation_rules=['source_phase required', 'outcome_summary required', 'cycle_id required'],
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackSub"
)

print(f"Memory dedicated file FeedbackRegistry category {'important_notes'} eco {'AutoImprovementEcosystem'}")
