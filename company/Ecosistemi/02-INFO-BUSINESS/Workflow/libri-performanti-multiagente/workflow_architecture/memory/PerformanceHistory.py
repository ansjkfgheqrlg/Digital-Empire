
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

PerformanceHistory = MemoryComponent(
    name="PerformanceHistory",
    category="important_notes",
    read_agents=['ImprovementAnalystAgent', 'PriorityRankerAgent'],
    write_agents=['PerformanceMetricsAgent', 'MemoryWriterAgent'],
    data_schema={'history_id': 'uuid', 'phase': 'string Research Qualification Planning Production Visual', 'metrics': 'qualification_outcomes production_speed_metrics self_healing_activation_frequency plan_validity_scores memory_retrieval_patterns book_performance_signals', 'timestamp': 'ISO', 'cycle_id': 'uuid'},
    checkpoint_logic={'creation': 'after metrics calculation each cycle', 'storage': 'append historical used for pattern detection', 'retention': 'persistent for learning'},
    validation_rules=['phase required', 'metrics dict with 6 feedback signals required', 'cycle_id required'],
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackSub"
)

print(f"Memory dedicated file PerformanceHistory category {'important_notes'} eco {'AutoImprovementEcosystem'}")
