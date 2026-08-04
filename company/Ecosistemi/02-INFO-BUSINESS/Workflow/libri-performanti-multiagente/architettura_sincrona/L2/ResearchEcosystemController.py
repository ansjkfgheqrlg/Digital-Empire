
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import global_harmony

ResearchEcosystemController = Agent(
    name="ResearchEcosystemController",
    role="Controlla ResearchEcosystem 5 team keyword search Amazon review sites L2 Controller ResearchEcosystem gestisce team alloca risorse valida handoff report Supreme - perfetta sincronia armonia con Supreme L1 e L3 leaders",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem=None,
    inputs=["cycle_start_signal","memory_hierarchies","important_notes_feedback","checkpoints","team_status_reports","global_harmony_status"],
    outputs=["ecosystem_status","resource_allocation","go_signal","reports_to_L1","handoff_validation","harmony_validation"],
    decision_logic="""Controller L2 ResearchEcosystem: leggi important_notes LearningLog pattern successo fallimento alloca team leader L3 trigger flow interno team via TeamSynchronyProtocol harmony validation SE team empty result anomaly trigger SelfHealing via PlaywrightErrorHandlerAgent SE output validato checkpoint marca phase complete crea checkpoint via CheckpointManagerAgent handoff prossimo ecosistema via InterTeamHarmonyProtocol 8-step sincronizzato Memory broker SE 3 fallimenti escalate Supreme - mantiene perfect synchrony harmony intra-ecosistema e inter-ecosistemi via GlobalHarmonyOrchestrator.check_global_harmony()""",
    connections={"reports_to": ["SupremeOrchestratorAgent"], "manages": ["ResearchEcosystemLeader1","ResearchEcosystemLeader2"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController","GlobalHarmonyOrchestrator"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","FeedbackRegistry","BookOpportunityRegistry","GlobalHarmonyStatus"], "write": ["checkpoints","decisions","important_notes","GlobalHarmonyStatus"]},
    self_healing_behavior={"detection_triggers": ["empty result from research","Playwright failure","memory write failure","team desynchronized"], "action": "retry adjusted params rollback CP0 escalate Supreme if 3 fails harmony resync via GlobalHarmonyOrchestrator", "max_retries": 3},
    playwright_usage="supervises PlaywrightOperationsSubEcosystem real tool" if "ResearchEcosystem"=="ResearchEcosystem" or "ResearchEcosystem"=="VisualEcosystem" else None,
    skill_usage=["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

class ResearchEcosystemController_HarmonyWrapper:
    def __init__(self):
        self.agent = ResearchEcosystemController
        self.ecosystem = "ResearchEcosystem"
    def sync_teams(self):
        return global_harmony.check_global_harmony()
    def validate_harmony(self):
        return {"controller": "ResearchEcosystemController", "ecosystem": "ResearchEcosystem", "status": "synchronized", "teams": "ResearchEcosystem teams harmony"}

print(f"L2 Controller dedicated file ResearchEcosystemController ResearchEcosystem - perfect synchrony harmony")
