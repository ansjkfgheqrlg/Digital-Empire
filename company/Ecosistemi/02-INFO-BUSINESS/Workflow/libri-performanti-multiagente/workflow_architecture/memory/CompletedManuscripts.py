
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

CompletedManuscripts = MemoryComponent(
    name="CompletedManuscripts",
    category="plans",
    read_agents=['VisualEcosystemController', 'GraphicDesignLeader'],
    write_agents=['BookWritingLeader', 'FinalApprovalAgent', 'PlanStorageAgent'],
    data_schema={'manuscript_id': 'uuid', 'book_id': 'uuid', 'plan_id': 'ref SecondLevelPlans', 'content': 'full_book_ref chapters production_log_ref', 'status': 'validated approved final', 'validation': 'completeness plan_compliance style uniform consistency'},
    checkpoint_logic={'creation': 'when final approval given FinalApprovalAgent', 'validation': 'ManuscriptValidator + PlanComplianceChecker'},
    validation_rules=['content full_book_ref required', 'status approved required', 'plan_id ref required'],
    ecosystem="ProductionEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file CompletedManuscripts category {'plans'} eco {'ProductionEcosystem'}")
