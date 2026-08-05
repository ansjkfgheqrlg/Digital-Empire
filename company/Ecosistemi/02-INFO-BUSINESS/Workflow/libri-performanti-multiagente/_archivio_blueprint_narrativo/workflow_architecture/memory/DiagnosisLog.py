
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import MemoryComponent

DiagnosisLog = MemoryComponent(
    name="DiagnosisLog",
    category="important_notes",
    read_agents=['RecoveryLeader', 'SelfHealingEcosystemController'],
    write_agents=['RootCauseAnalystAgent', 'ImpactAssessorAgent', 'RecoveryPlannerAgent', 'FailurePatternAnalyzerAgent'],
    data_schema={'diagnosis_id': 'uuid', 'anomaly_id': 'ref AnomalyLog', 'root_cause': 'string categorization', 'cause_category': 'Playwright failure data extraction validation empty result memory stall', 'impact': 'affected phases data loss risk checkpoint availability', 'recovery_plan': 'action retry rollback escalate skip_and_log requalify adjusted_params checkpoint_id anomaly_flag'},
    checkpoint_logic={'creation': 'after diagnosis', 'storage': 'append link to AnomalyLog'},
    validation_rules=['anomaly_id ref required', 'root_cause required', 'recovery_plan action required'],
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub"
)

print(f"Memory dedicated file DiagnosisLog category {'important_notes'} eco {'SelfHealingEcosystem'}")
