
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

plans = MemoryComponent(
    name="plans",
    category="plans",
    read_agents=['ProductionTeam', 'VisualTeam'],
    write_agents=['QualificationTeam', 'PlanningTeam', 'PlanStorageAgent', 'MemoryWriterAgent'],
    data_schema={'plan_id': 'uuid', 'plan_type': 'qualification second_level_operational manuscript cover improvement', 'plan_level': 'first_level second_level final', 'content': 'dict varying per type', 'status': 'draft approved validated archived', 'created_by': 'agent name', 'approved_by': 'agent name leader', 'timestamp': 'ISO', 'validity_score': 'descriptive score'},
    checkpoint_logic={'creation': 'when plan approved validated', 'validation': 'PlanQualityAuditor for qualification PlanCoherenceValidator for second-level', 'storage': 'PlanStorage versioned not overwritten', 'checkpoint': 'before after approval'},
    validation_rules=['plan_type required', 'content required', 'status required', 'created_by approved_by required'],
    ecosystem="MemoryEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file plans category {'plans'} eco {'MemoryEcosystem'}")
