
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

GraphicPrompts = MemoryComponent(
    name="GraphicPrompts",
    category="important_notes",
    read_agents=['GraphicGeneratorAgent', 'MemoryReaderAgent'],
    write_agents=['GraphicPromptCreatorAgent', 'CoverPromptCreatorAgent'],
    data_schema={'prompt_id': 'uuid', 'book_id': 'uuid', 'chapter_ref': 'string cover', 'prompt': 'detailed prompt graphic generation', 'purpose': 'purpose'},
    checkpoint_logic={'creation': 'when prompt created per graphic requirement'},
    validation_rules={'purpose required', 'prompt detailed required'},
    ecosystem="VisualEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file GraphicPrompts category {'important_notes'} eco {'VisualEcosystem'}")
