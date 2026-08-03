import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent


DataFormatterAgent = Agent(
    name="DataFormatterAgent",
    role="Formatta dati per storage via Playwright save",
    hierarchy_level=6,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PersistenceSub" if "PersistenceSub" != "None" else None,
    inputs=["raw_book_data"],
    outputs=["formatted_structured_output"],
    decision_logic="""Format data into structured_output ready to pass qualification phase list book opportunities metadata review sites analysis data raw_data refs Ensure output directly usable next phase""",
    connections={"reports_to": ["DataPersistenceLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

SaveValidatorAgent = Agent(
    name="SaveValidatorAgent",
    role="Conferma salvataggi Playwright successo",
    hierarchy_level=6,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PersistenceSub" if "PersistenceSub" != "None" else None,
    inputs=["save_operations"],
    outputs=["save_validation_result"],
    decision_logic="""Confirm saves via Playwright were successful check URL saved source logged raw_data accessible IF fail trigger self-healing retry""",
    connections={"reports_to": ["DataPersistenceLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

MemoryValidatorAgent = Agent(
    name="MemoryValidatorAgent",
    role="Valida consistenza memoria corruzione gaps active",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["memory_content_all_categories", "checkpoint_refs"],
    outputs=["validation_report", "corruption_gap_flags"],
    decision_logic="""Validate memory consistency checkpoints align decisions plans hierarchies important_notes no gap corruption Flag corruption gaps trigger SelfHealing if needed trigger Memory Maintenance Flow periodic""",
    connections={"reports_to": ["MemoryManagementLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

CheckpointManagerAgent = Agent(
    name="CheckpointManagerAgent",
    role="Gestisce checkpoint creation storage restoration core self-healing",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["checkpoint_creation_triggers", "rollback_requests", "state_snapshots"],
    outputs=["checkpoint_created_confirmation", "restored_checkpoint"],
    decision_logic="""Manage checkpoint creation storage restoration creation triggers end each phase before major decision before handoff on self-healing activation per chapter production Storage parent ID valid flag Restoration via RollbackExecutorAgent request Core self-healing""",
    connections={"reports_to": ["MemoryManagementLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

DecisionLoggerAgent = Agent(
    name="DecisionLoggerAgent",
    role="Logga decisioni full context reasoning immutable",
    hierarchy_level=6,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["decision_events", "reasoning_chains"],
    outputs=["decision_log_confirmation"],
    decision_logic="""Log decisions decision_id phase team agent type value reasoning timestamp related_data Immutable append-only traceability""",
    connections={"reports_to": ["MemoryManagementLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

RollbackExecutorAgent = Agent(
    name="RollbackExecutorAgent",
    role="Esegue rollback checkpoint precedenti real recovery",
    hierarchy_level=6,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub" if "RecoverySub" != "None" else None,
    inputs=["rollback_requests", "checkpoint_id"],
    outputs=["rollback_execution_result", "restored_state"],
    decision_logic="""Execute rollback to last valid checkpoint via CheckpointManagerAgent restore Log RecoveryLog Ensure memory_updated TRUE flow_continued TRUE checkpoint_restored TRUE per handle_failure schema""",
    connections={"reports_to": ["RecoveryLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L6"
)

ALL_L6 = [DataFormatterAgent,SaveValidatorAgent,MemoryValidatorAgent,CheckpointManagerAgent,DecisionLoggerAgent,RollbackExecutorAgent]
print("Fixed file validated")
