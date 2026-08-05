
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

ProductionStartSignals = MemoryComponent(
    name="ProductionStartSignals",
    category="decisions",
    read_agents=['ProductionEcosystemController', 'BookWritingLeader'],
    write_agents=['ProductionStartSignalAgent', 'DecisionLoggerAgent'],
    data_schema={'signal_id': 'uuid', 'value': 'TRUE', 'validated_by': 'ProductionReadinessLeader', 'checkpoint_ref': 'CP3'},
    checkpoint_logic={'creation': 'when production authorized marks actual start', 'checkpoint': 'CP3 Planning End Production Start gate'},
    validation_rules={'value TRUE explicit', 'checkpoint_ref CP3 required', 'validated_by required'},
    ecosystem="PlanningEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file ProductionStartSignals category {'decisions'} eco {'PlanningEcosystem'}")
