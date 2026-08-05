
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

LearningLog = MemoryComponent(
    name="LearningLog",
    category="important_notes",
    read_agents=['SupremeOrchestratorAgent', 'All EcosystemControllers', 'ResearchEcosystemController'],
    write_agents=['ParameterAdjusterAgent', 'ThresholdUpdaterAgent', 'WorkflowOptimizerAgent', 'LearningLoggerAgent'],
    data_schema={'log_id': 'uuid', 'improvement_plan_id': 'ref ImprovementPlans', 'what_learned': 'string what system learned', 'what_changed': 'parameter adjusted threshold updated flow optimized', 'target': 'next cycle or next similar phase', 'before': 'state before', 'after': 'state after', 'validation': 'measurable improvement boolean', 'timestamp': 'ISO', 'memory_write': 'True per generate_improvement_signal schema'},
    checkpoint_logic={'creation': 'after improvement execution per generate_improvement_signal schema source_phase outcome_summary improvement_suggestion target memory_write True', 'use': 'read by Research Qualification before new cycle to adapt'},
    validation_rules=['what_learned required', 'what_changed required', 'target required', 'improvement_plan_id ref required'],
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ExecutionSub"
)

print(f"Memory dedicated file LearningLog category {'important_notes'} eco {'AutoImprovementEcosystem'}")
