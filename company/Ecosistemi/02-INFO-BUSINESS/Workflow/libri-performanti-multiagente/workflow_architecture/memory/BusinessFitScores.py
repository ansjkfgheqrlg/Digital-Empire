
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

BusinessFitScores = MemoryComponent(
    name="BusinessFitScores",
    category="important_notes",
    read_agents=['PlanningEcosystemController'],
    write_agents=['MarketAlignmentAnalystAgent', 'BusinessFitAnalystAgent'],
    data_schema={'book_id': 'uuid', 'business_fit': 'score quantity-performance', 'evidence': 'string'},
    checkpoint_logic={'creation': 'after market alignment evaluation'},
    validation_rules={'evidence required'},
    ecosystem="QualificationEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file BusinessFitScores category {'important_notes'} eco {'QualificationEcosystem'}")
