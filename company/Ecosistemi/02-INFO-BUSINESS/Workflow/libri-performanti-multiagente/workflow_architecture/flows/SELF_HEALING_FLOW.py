
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Flow

SELF_HEALING_FLOW = Flow(
    name="SELF_HEALING_FLOW",
    start_condition="""Any anomaly detected DetectionTeam OutputMonitor ErrorDetector AnomalyDetector StallDetector PlaywrightFailureDetector MemoryFailureDetector - 8 triggers missing incoherent blocked failed validation empty result no-go without alternative memory write failure Playwright failure""",
    phases=[{'phase_id': 1, 'name': 'Detection OutputMonitor ErrorDetector AnomalyDetector StallDetector', 'team': 'DetectionTeam'}, {'phase_id': 2, 'name': 'Diagnosis RootCause Impact Assessment Recovery Planning', 'team': 'DiagnosisTeam'}, {'phase_id': 3, 'name': 'Recovery Planning mapping error_type action retry rollback escalate skip_and_log requalify', 'team': 'DiagnosisTeam', 'agent': 'RecoveryPlannerAgent'}, {'phase_id': 4, 'name': 'Recovery Execution RetryExecutor RollbackExecutor AlternativePath', 'team': 'RecoveryTeam'}, {'phase_id': 5, 'name': 'Recovery Validation RecoveryValidator', 'team': 'RecoveryTeam'}, {'phase_id': 6, 'name': 'Memory Update AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes flow_continued True', 'team': 'RecoveryTeam + MemoryManagementTeam'}],
    decision_gates=[{'gate_id': 'SH_DG1_Detection_Valid', 'logic': 'anomaly report severity location context checkpoint_before error_type one of 8 triggers', 'on_pass': 'Diagnosis', 'on_fail': 're-detect'}, {'gate_id': 'SH_DG2_Recovery_Success', 'logic': 'recovery validated without data loss workflow resume flow_continued True', 'on_pass': 'resume affected ecosystem', 'on_fail': 'retry count <3 retry else escalate L2 then Supreme L1'}],
    rollback_points=['checkpoint_before anomaly', 'last valid checkpoint parent chain any CP0-CP_FINAL', 'SelfHealingCheckpoints', 'CheckpointSubEcosystem checkpoints'],
    completion_criteria="""workflow resumed without data loss OR escalated L1 full diagnosis log AnomalyLog DiagnosisLog RecoveryLog memory_updated True checkpoint_restored True flow_continued True per handle_failure schema""",
    involved_ecosystems=['SelfHealingEcosystem', 'MemoryEcosystem', 'All affected ecosystems'],
    sub_flows=['DetectionSubFlow', 'DiagnosisSubFlow', 'RecoverySubFlow']
)

print(f"Flow dedicated file SELF_HEALING_FLOW - phases {len(SELF_HEALING_FLOW.phases)} gates {len(SELF_HEALING_FLOW.decision_gates)}")
