import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

from core import Agent
SupremeOrchestratorAgent = Agent(
    name="SupremeOrchestratorAgent",
    role="Supreme Orchestrator L1 - unico top-level, vede tutto, decide macro, override qualsiasi decisione, gestisce stato globale, inizia cicli, valida gerarchie",
    hierarchy_level=1,
    team="SupremeOrchestratorTeam",
    ecosystem="Global",
    sub_ecosystem=None,
    inputs=["reports_from_L2_controllers", "memory_ecosystem_state", "self_healing_escalations", "auto_improvement_signals", "final_outputs_all_ecosystems", "hierarchy_validation_reports"],
    outputs=["global_state", "macro_decisions", "override_commands", "cycle_initiation_signals", "hierarchy_updates", "CP0_INIT"],
    decision_logic="""SE riceve escalation self-healing severity CRITICAL ALLORA override decisione lower + trigger rollback a ultimo checkpoint globale valido + log in hierarchies. SE GO_rate <20% ALLORA aggiusta BookNicheDecisionSkill thresholds via ThresholdUpdaterAgent + aumenta retry Research. SE nuovo ciclo ALLORA crea CP0_INIT via CheckpointManagerAgent, scrive hierarchies via HierarchyManagerAgent, broadcast start a tutti i controller L2. Sempre monitora stall via StallDetectorAgent. Authority override senza soglia.""",
    connections={"reports_to": [], "manages": ["ResearchEcosystemController","QualificationEcosystemController","PlanningEcosystemController","ProductionEcosystemController","VisualEcosystemController","MemoryEcosystemController","SelfHealingEcosystemController","AutoImprovementEcosystemController"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","AnomalyLog","PerformanceHistory","FeedbackRegistry"], "write": ["hierarchies","checkpoints","important_notes"]},
    self_healing_behavior={"on_failure": "top level non self-heala, riceve escalation, manual_override_and_global_rollback", "checkpoint_before": True},
    level_name="L1_SUPREME_ORCHESTRATOR"
)
ALL_L1 = [SupremeOrchestratorAgent]
