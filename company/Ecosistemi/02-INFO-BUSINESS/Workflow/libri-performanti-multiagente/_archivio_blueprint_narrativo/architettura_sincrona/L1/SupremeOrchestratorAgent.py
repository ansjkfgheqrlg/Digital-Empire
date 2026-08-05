
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import global_harmony

SupremeOrchestratorAgent = Agent(
    name="SupremeOrchestratorAgent",
    role="Supreme Orchestrator L1 - unico top-level vede tutto decide macro override qualsiasi decisione gestisce stato globale inizia cicli valida gerarchie 7 livelli - perfetta sincronia armonia con L2 controllers",
    hierarchy_level=1,
    team="SupremeOrchestratorTeam",
    ecosystem="Global",
    sub_ecosystem=None,
    inputs=["reports_from_L2_controllers","memory_ecosystem_state","self_healing_escalations","auto_improvement_signals","final_outputs_all_ecosystems","hierarchy_validation_reports","global_harmony_status"],
    outputs=["global_state","macro_decisions","override_commands","cycle_initiation_signals","hierarchy_updates","CP0_INIT","global_harmony_validation"],
    decision_logic="""SE escalation self-healing severity CRITICAL ALLORA override lower + rollback checkpoint globale valido + log hierarchies + broadcast global_harmony resync SE GO_rate <20% ALLORA aggiusta thresholds via ThresholdUpdaterAgent + aumenta retry Research SE nuovo ciclo ALLORA crea CP0_INIT via CheckpointManagerAgent L6 scrive hierarchies via HierarchyManagerAgent L6 leggi important_notes LearningLog FeedbackRegistry via MemoryReaderAgent L5 broadcast start tutti L2 controllers via InterTeamHarmonyProtocol 8-step + TeamSynchronyProtocol harmony validation global_harmony.check_global_harmony() Authority override senza soglia Gestisce perfect synchrony harmony globale""",
    connections={"reports_to": [], "manages": ["ResearchEcosystemController","QualificationEcosystemController","PlanningEcosystemController","ProductionEcosystemController","VisualEcosystemController","MemoryEcosystemController","SelfHealingEcosystemController","AutoImprovementEcosystemController"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController","GlobalHarmonyOrchestrator"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","AnomalyLog","PerformanceHistory","FeedbackRegistry","LearningLog"], "write": ["hierarchies","checkpoints","important_notes","GlobalHarmonyStatus"]},
    self_healing_behavior={"on_failure": "top level non self-heala riceve escalation manual_override_and_global_rollback", "checkpoint_before": True, "global_harmony_resync": True},
    level_name="L1_SUPREME_ORCHESTRATOR"
)

print("SupremeOrchestratorAgent dedicated file L1 - perfect synchrony harmony global")
