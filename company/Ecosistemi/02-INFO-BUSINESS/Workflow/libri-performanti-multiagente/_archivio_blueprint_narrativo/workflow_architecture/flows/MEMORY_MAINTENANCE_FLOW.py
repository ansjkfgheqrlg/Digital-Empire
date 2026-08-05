
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Flow

MEMORY_MAINTENANCE_FLOW = Flow(
    name="MEMORY_MAINTENANCE_FLOW",
    start_condition="""Periodic trigger M cycles time OR triggered MemoryValidatorAgent corruption gap detected OR SelfHealing memory write failure""",
    phases=[{'phase_id': 1, 'name': 'Consistency Check MemoryValidatorAgent across 35 components checkpoints align decisions plans hierarchies important_notes'}, {'phase_id': 2, 'name': 'Gap Detection missing checkpoint missing decision missing plan hierarchy gap important_notes gap'}, {'phase_id': 3, 'name': 'Corruption Detection checkpoint invalid flag decision empty reasoning plan missing required fields hierarchy corrupted'}, {'phase_id': 4, 'name': 'Cleanup Optimization MemoryManagementTeam CheckpointSub DecisionLogSub deduplication without loss trace cache frequently read data checkpoint storage prune old preserving traceability restore corrupted last valid'}, {'phase_id': 5, 'name': 'Validation Post-Cleanup MemoryValidatorAgent re-validate consistent optimized'}],
    decision_gates=[{'gate_id': 'MM_DG1_Consistency_Pass', 'logic': 'consistency passes OR gaps corruption detected proceed cleanup'}, {'gate_id': 'MM_DG2_Cleanup_Valid', 'logic': 'after cleanup validation passes memory consistent optimized gaps repaired flagged'}],
    rollback_points=['last valid checkpoint before maintenance', 'Memory state snapshot before cleanup via CheckpointManager self_healing checkpoint', 'DecisionLog before', 'hierarchies before'],
    completion_criteria="""memory consistent optimized per validation all gaps repaired flagged important_notes corruption restored last valid checkpoint chain valid parent IDs all categories 35 readable via MemoryReaderAgent hierarchy 7 levels valid traceability OK""",
    involved_ecosystems=['MemoryEcosystem', 'SelfHealingEcosystem', 'All ecosystems memory usage'],
    sub_flows=['ConsistencySubFlow', 'GapSubFlow', 'CorruptionSubFlow', 'CleanupSubFlow']
)

print(f"Flow dedicated file MEMORY_MAINTENANCE_FLOW - phases {len(MEMORY_MAINTENANCE_FLOW.phases)} gates {len(MEMORY_MAINTENANCE_FLOW.decision_gates)}")
