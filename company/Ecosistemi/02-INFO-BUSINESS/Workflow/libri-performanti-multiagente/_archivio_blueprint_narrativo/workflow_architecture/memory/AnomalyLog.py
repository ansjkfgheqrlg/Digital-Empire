
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

AnomalyLog = MemoryComponent(
    name="AnomalyLog",
    category="important_notes",
    read_agents=['DiagnosisLeader', 'RecoveryLeader', 'SelfHealingEcosystemController'],
    write_agents=['OutputMonitorAgent', 'ErrorDetectorAgent', 'AnomalyDetectorAgent', 'StallDetectorAgent', 'DetectionLeader', 'PlaywrightFailureDetectorAgent', 'MemoryFailureDetectorAgent'],
    data_schema={'anomaly_id': 'uuid', 'phase': 'string where detected', 'team': 'string', 'agent': 'string detecting', 'error_type': 'missing output incoherent output blocked process failed validation empty result from research no-go without alternative memory write failure Playwright failure', 'severity': 'critical high medium low', 'context': 'state snapshot before anomaly', 'checkpoint_before': 'checkpoint ID ref', 'timestamp': 'ISO', 'status': 'detected diagnosed recovering recovered escalated'},
    checkpoint_logic={'creation': 'on any detection trigger 8 triggers', 'storage': 'MemoryWriter append', 'checkpoint': 'SelfHealingCheckpoint before after'},
    validation_rules=['error_type must be one of 8 triggers', 'severity required', 'phase required', 'checkpoint_before required'],
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub"
)

print(f"Memory dedicated file AnomalyLog category {'important_notes'} eco {'SelfHealingEcosystem'}")
