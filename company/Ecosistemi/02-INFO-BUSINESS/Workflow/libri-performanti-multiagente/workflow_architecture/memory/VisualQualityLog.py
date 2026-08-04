
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

VisualQualityLog = MemoryComponent(
    name="VisualQualityLog",
    category="important_notes",
    read_agents=['VisualQualityLeader'],
    write_agents=['VisualQualityAuditorAgent', 'FinalVisualApprovalAgent'],
    data_schema={'audit_id': 'uuid', 'quality_score': 'overall visual quality', 'issues': 'list'},
    checkpoint_logic={'creation': 'after visual quality audit'},
    validation_rules=['quality_score required'],
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub"
)

print(f"Memory dedicated file VisualQualityLog category {'important_notes'} eco {'VisualEcosystem'}")
