
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

VideoStructureControlPoints = MemoryComponent(
    name="VideoStructureControlPoints",
    category="important_notes",
    read_agents=['StructurePlanningLeader', 'PlanCoherenceValidatorAgent', 'SelfHealingEcosystemController'],
    write_agents=['VideoStructureArchitectAgent', 'VideoStructureValidatorAgent'],
    data_schema={'original_requirement': 'video structure', 'preserved_as_is': 'bool True', 'validation_required': 'human_or_orchestrator must confirm', 'ambiguity_handling': 'preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions'},
    checkpoint_logic={'creation': 'when video_structure designed - CRITICAL CP-VIDEO-01'},
    validation_rules={'original_requirement preserved verbatim required', 'validation_required flag'},
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub"
)

print(f"Memory dedicated file VideoStructureControlPoints category {'important_notes'} eco {'PlanningEcosystem'}")
