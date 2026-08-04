
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import HarmonySignal
import time

ContentDetailArchitectAgent = Agent(
    name="ContentDetailArchitectAgent",
    role="Progetta dettagli contenuti per sustainable production - operational - L5 Team ContentPlanningTeam Ecosistema PlanningEcosystem - perfetta sincronia armonia",
    hierarchy_level=5,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentSub",
    inputs=["chapters", "video_structure"],
    outputs=["production_constraints", "style_notes", "graphic_needs"],
    decision_logic="""Come agente ContentDetailArchitectAgent L5 team ContentPlanningTeam PlanningEcosystem: Progetta dettagli contenuti per sustainable production - operational - Riceve HarmonySignal ready da TeamSynchronyProtocol leader ContentPlanningLeader - Legge memoria via MemoryReaderAgent - Esegue task core con Playwright tool se necessario - Valida output con validator - Emite checkpoint condiviso broadcast ALL_TEAM - Handoff interno ack obbligatorio - Self-healing DetectionTeam se fail - Verifica harmony_status synchronized - Scrive memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent - Logga decisione via DecisionLoggerAgent - Sincronia perfetta armonia intra-team InterTeamHarmonyProtocol esterno 8-step""",
    connections={"reports_to": ["ContentPlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback checkpoint condiviso valido team ContentPlanningTeam sincronizzato - escalate leader ContentPlanningLeader poi controller PlanningEcosystemController poi Supreme", "max_retries": 3, "harmony_preserved": True},
    playwright_usage="real operational tool" if "Playwright" in "ContentDetailArchitectAgent" or "Search" in "ContentDetailArchitectAgent" or "Extractor" in "ContentDetailArchitectAgent" else None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
    level_name="L5"
)

class ContentDetailArchitectAgent_SynchronizedWrapper:
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.harmony_signals = []
        self.checkpoint_shared = None
        self.status = "initialized"
    def emit_ready(self):
        signal = HarmonySignal(signal_id=f"ContentPlanningTeam_{self.agent.name}_ready", sender_agent=self.agent.name, receiver_agent="ContentPlanningLeader", team="ContentPlanningTeam", ecosystem="PlanningEcosystem", signal_type="ready", payload={"agent": self.agent.name}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"), requires_ack=True)
        self.harmony_signals.append(signal)
        self.status = "ready"
        return signal
    def sync_checkpoint(self, checkpoint_id):
        self.checkpoint_shared = checkpoint_id
        signal = HarmonySignal(signal_id=f"ContentPlanningTeam_{self.agent.name}_checkpoint_{checkpoint_id}", sender_agent=self.agent.name, receiver_agent="ALL_TEAM", team="ContentPlanningTeam", ecosystem="PlanningEcosystem", signal_type="checkpoint", payload={"checkpoint_id": checkpoint_id}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        self.harmony_signals.append(signal)
        self.status = "checkpoint_shared"
        return signal
    def validate_harmony(self):
        return {"agent": self.agent.name, "team": "ContentPlanningTeam", "status": self.status, "harmony": "synchronized"}

ContentDetailArchitectAgent_sync = ContentDetailArchitectAgent_SynchronizedWrapper(ContentDetailArchitectAgent)
def get_agent():
    return ContentDetailArchitectAgent
def get_synchronized_wrapper():
    return ContentDetailArchitectAgent_sync
print(f"Agent dedicated ContentDetailArchitectAgent L5 Team ContentPlanningTeam - perfect synchrony harmony")
