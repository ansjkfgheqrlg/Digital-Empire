
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

important_notes = MemoryComponent(
    name="important_notes",
    category="important_notes",
    read_agents=['All teams', 'AutoImprovementEcosystemController', 'SelfHealingEcosystemController'],
    write_agents=['All teams', 'SelfHealingEngine', 'AutoImprovementEngine', 'ImportantNotesAgent', 'MemoryWriterAgent'],
    data_schema={'note_id': 'uuid', 'category': 'critical_notions risk_flags anomaly_logs keyword_patterns improvement_suggestions validation_uncertainties Playwright_failures', 'content': 'string critical notion', 'severity': 'critical high medium low info', 'source_agent': 'string', 'source_phase': 'string Research etc', 'timestamp': 'ISO', 'expiry': 'ISO or None persistent'},
    checkpoint_logic={'creation': 'whenever relevant signal detected any agent self-healing auto-improvement', 'storage': 'ImportantNotesAgent deduplication but without loss trace'},
    validation_rules=['content not empty', 'category required', 'source_agent required', 'timestamp required'],
    ecosystem="MemoryEcosystem",
    sub_ecosystem="None"
)

print(f"Memory dedicated file important_notes category {'important_notes'} eco {'MemoryEcosystem'}")
