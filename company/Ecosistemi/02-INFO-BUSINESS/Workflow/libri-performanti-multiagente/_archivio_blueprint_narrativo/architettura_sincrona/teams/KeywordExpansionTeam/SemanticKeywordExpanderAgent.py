
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import HarmonySignal
import time

SemanticKeywordExpanderAgent = Agent(
    name="SemanticKeywordExpanderAgent",
    role="Espande keyword semanticamente da LearningLog patterns - operational - L5 Team KeywordExpansionTeam Ecosistema ResearchEcosystem - perfetta sincronia armonia",
    hierarchy_level=5,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ExpansionSub",
    inputs=["LearningLog", "important_notes"],
    outputs=["semantic_expansions"],
    decision_logic="""Come agente SemanticKeywordExpanderAgent L5 team KeywordExpansionTeam ResearchEcosystem: Espande keyword semanticamente da LearningLog patterns - operational - Riceve HarmonySignal ready da TeamSynchronyProtocol leader KeywordExpansionLeader - Legge memoria via MemoryReaderAgent - Esegue task core con Playwright tool se necessario - Valida output con validator - Emite checkpoint condiviso broadcast ALL_TEAM - Handoff interno ack obbligatorio - Self-healing DetectionTeam se fail - Verifica harmony_status synchronized - Scrive memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent - Logga decisione via DecisionLoggerAgent - Sincronia perfetta armonia intra-team InterTeamHarmonyProtocol esterno 8-step""",
    connections={"reports_to": ["KeywordExpansionLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback checkpoint condiviso valido team KeywordExpansionTeam sincronizzato - escalate leader KeywordExpansionLeader poi controller ResearchEcosystemController poi Supreme", "max_retries": 3, "harmony_preserved": True},
    playwright_usage="real operational tool" if "Playwright" in "SemanticKeywordExpanderAgent" or "Search" in "SemanticKeywordExpanderAgent" or "Extractor" in "SemanticKeywordExpanderAgent" else None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
    level_name="L5"
)

class SemanticKeywordExpanderAgent_SynchronizedWrapper:
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.harmony_signals = []
        self.checkpoint_shared = None
        self.status = "initialized"
    def emit_ready(self):
        signal = HarmonySignal(signal_id=f"KeywordExpansionTeam_{self.agent.name}_ready", sender_agent=self.agent.name, receiver_agent="KeywordExpansionLeader", team="KeywordExpansionTeam", ecosystem="ResearchEcosystem", signal_type="ready", payload={"agent": self.agent.name}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"), requires_ack=True)
        self.harmony_signals.append(signal)
        self.status = "ready"
        return signal
    def sync_checkpoint(self, checkpoint_id):
        self.checkpoint_shared = checkpoint_id
        signal = HarmonySignal(signal_id=f"KeywordExpansionTeam_{self.agent.name}_checkpoint_{checkpoint_id}", sender_agent=self.agent.name, receiver_agent="ALL_TEAM", team="KeywordExpansionTeam", ecosystem="ResearchEcosystem", signal_type="checkpoint", payload={"checkpoint_id": checkpoint_id}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        self.harmony_signals.append(signal)
        self.status = "checkpoint_shared"
        return signal
    def validate_harmony(self):
        return {"agent": self.agent.name, "team": "KeywordExpansionTeam", "status": self.status, "harmony": "synchronized"}

SemanticKeywordExpanderAgent_sync = SemanticKeywordExpanderAgent_SynchronizedWrapper(SemanticKeywordExpanderAgent)
def get_agent():
    return SemanticKeywordExpanderAgent
def get_synchronized_wrapper():
    return SemanticKeywordExpanderAgent_sync
print(f"Agent dedicated SemanticKeywordExpanderAgent L5 Team KeywordExpansionTeam - perfect synchrony harmony")
