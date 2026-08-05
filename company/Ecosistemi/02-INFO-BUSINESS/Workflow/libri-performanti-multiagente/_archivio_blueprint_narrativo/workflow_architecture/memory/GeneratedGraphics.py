
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

GeneratedGraphics = MemoryComponent(
    name="GeneratedGraphics",
    category="important_notes",
    read_agents=['GraphicQualityReviewerAgent', 'VisualPlaywrightLeader'],
    write_agents=['GraphicGeneratorAgent', 'VisualPlaywrightSaveAgent'],
    data_schema={'graphic_id': 'uuid', 'book_id': 'uuid', 'prompt_id': 'ref GraphicPrompts', 'asset_ref': 'Playwright visual_save ref', 'quality_score': 'pass fail', 'review_status': 'approved failed revised'},
    checkpoint_logic={'creation': 'after generation save via Playwright support', 'validation': 'GraphicQualityReviewer', 'revision_loop': 'failed -> RevisionAgent -> QualityReviewer'},
    validation_rules=['asset_ref via Playwright save required', 'quality_score required'],
    ecosystem="VisualEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file GeneratedGraphics category {'important_notes'} eco {'VisualEcosystem'}")
