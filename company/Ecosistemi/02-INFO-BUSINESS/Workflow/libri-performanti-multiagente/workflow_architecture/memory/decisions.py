
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

decisions = MemoryComponent(
    name="decisions",
    category="decisions",
    read_agents=['ProductionTeam', 'VisualTeam', 'AutoImprovementEcosystemController', 'All teams'],
    write_agents=['QualificationTeam', 'PlanningTeam', 'DecisionLoggerAgent', 'MemoryWriterAgent'],
    data_schema={'decision_id': 'uuid', 'phase': 'string', 'team': 'string', 'agent': 'string decision maker', 'decision_type': 'GO NO-GO production_start keyword_selection niche_ranking', 'decision_value': 'string value', 'reasoning': 'full reasoning chain', 'timestamp': 'ISO', 'related_data': 'dict book_id scores risk_flags plan_id'},
    checkpoint_logic={'creation': 'at every decision point all ecosystems', 'storage': 'append-only DecisionLogger immutable full context', 'checkpoint': 'checkpoint created before major decision'},
    validation_rules=['decision_type required', 'decision_value required', 'reasoning required traceable', 'timestamp required', 'agent required'],
    ecosystem="MemoryEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file decisions category {'decisions'} eco {'MemoryEcosystem'}")
