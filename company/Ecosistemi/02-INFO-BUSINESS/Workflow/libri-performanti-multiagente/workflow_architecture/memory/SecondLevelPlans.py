
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

SecondLevelPlans = MemoryComponent(
    name="SecondLevelPlans",
    category="plans",
    read_agents=['ProductionEcosystemController', 'BookWritingLeader', 'VisualEcosystemController'],
    write_agents=['VideoStructureArchitectAgent', 'ChapterDesignerAgent', 'DetailFillerAgent', 'PlanStorageAgent'],
    data_schema={'plan_id': 'uuid', 'content': 'video_structure REQUIRED preserved verbatim + chapters list + details concrete + production_start_signal TRUE'},
    checkpoint_logic={'creation': 'when plan approved validated StructurePlanningLeader', 'validation': 'PlanCoherenceValidator checks video_structure present verbatim'},
    validation_rules={'details concrete not vague', 'chapters non-empty', 'production_start_signal TRUE required', 'video_structure REQUIRED must exist non-empty non-reinterpreted'},
    ecosystem="PlanningEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file SecondLevelPlans category {'plans'} eco {'PlanningEcosystem'}")
