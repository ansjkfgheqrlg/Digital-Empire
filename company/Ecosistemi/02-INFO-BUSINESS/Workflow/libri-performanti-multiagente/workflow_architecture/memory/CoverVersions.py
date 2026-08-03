
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

CoverVersions = MemoryComponent(
    name="CoverVersions",
    category="plans",
    read_agents=['VisualEcosystemController'],
    write_agents=['CoverConceptAgent', 'CoverGeneratorAgent', 'CoverQualityReviewerAgent', 'VisualPlaywrightSaveAgent'],
    data_schema={'cover_id': 'uuid', 'book_id': 'uuid', 'concept': 'concept rationale market signals', 'prompt': 'cover prompt detailed', 'versions': 'list version_id asset_ref quality_score review_status', 'final_approved': 'asset_ref final cover', 'status': 'draft reviewing approved critical_fail_escalated'},
    checkpoint_logic={'creation': 'from concept to final versions stored', 'validation': 'CoverQualityReviewer critical cannot skip_and_log must escalate if fails final', 'checkpoint': 'CP5 CP_FINAL'},
    validation_rules=['concept required', 'final_approved required', 'status required'],
    ecosystem="VisualEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file CoverVersions category {'plans'} eco {'VisualEcosystem'}")
