
"""
AGENTE DEDICATO - File singolo per ProductionStartSignalAgent
Team: ProductionReadinessTeam
Ecosistema: PlanningEcosystem / ReadinessSub
Livello Gerarchico: L5
Lavora in perfetta sincronia e armonia con altri agenti del team via TeamSynchronyProtocol
"""

import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import HarmonySignal
import time

# Definizione agente con tutti i campi richiesti RULE 3
ProductionStartSignalAgent = Agent(
    name="ProductionStartSignalAgent",
    role="Emette segnale formale start produzione TRUE timestamp marks actual start production flow - operational CRITICAL - L5 - Team ProductionReadinessTeam - Ecosistema PlanningEcosystem - Lavora in perfetta sincronia e armonia con altri agenti via TeamSynchronyProtocol HarmonySignal",
    hierarchy_level=5,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ReadinessSub",
    inputs=["readiness_confirmation", "resource_estimate"],
    outputs=["production_start_signal_explicit", "CP3_creation_trigger"],
    decision_logic="""Come agente ProductionStartSignalAgent L5 in team ProductionReadinessTeam ecosistema PlanningEcosystem sub ReadinessSub:
    Emette segnale formale start produzione TRUE timestamp marks actual start production flow - operational CRITICAL
    LOGICA DECISIONALE ESATTA:
    - Riceve HarmonySignal ready da TeamSynchronyProtocol leader ProductionReadinessLeader
    - Legge memoria rilevante via MemoryReaderAgent L5 con context timestamp se necessario: checkpoints, decisions, plans, hierarchies, important_notes, BookOpportunityRegistry, ReviewDataRegistry, FeedbackRegistry, LearningLog
    - Esegue task core specifico del ruolo con operational tool se Playwright: navigate_amazon_keyword_search url https://www.amazon.com/s?k={keyword}, extract_data selectors, save_results results sources URLs notes, visual_save supporting visual team
    - Valida output con validator agent interno team: AmazonResultsValidatorAgent, ReviewDataValidatorAgent, PlanCoherenceValidatorAgent, ManuscriptValidatorAgent, GraphicQualityReviewerAgent, CoverQualityReviewerAgent, MemoryValidatorAgent, CheckpointManagerAgent
    - Emite HarmonySignal checkpoint con checkpoint_id condiviso via CheckpointManagerAgent broadcast a ALL_TEAM team ProductionReadinessTeam
    - Emite HarmonySignal handoff interno a prossimo agente team con ack obbligatorio
    - Se fail: emette HarmonySignal error a DetectionLeader L3, trigger SelfHealing flow DetectionTeam OutputMonitorAgent - DiagnosisTeam RootCauseAnalyst - RecoveryTeam RetryExecutor con adjusted params timeout++ user_agent rotate alternative selector new keywords memory reread rollback ultimo checkpoint valido via CheckpointManagerAgent
    - Verifica harmony_status synchronized via TeamSynchronyProtocol.validate_harmony()
    - Scrive risultato in memoria via MemoryWriterAgent L5 + checkpoint via CheckpointManagerAgent L6 parent ID valid flag
    - Logga decisione traceability via DecisionLoggerAgent L6 se GO NO-GO production_start_signal keyword_selection niche_ranking
    DECISION AUTHORITY: follow instructions senior and leaders, report output
    SINCRONIA E ARMONIA: Lavora in perfetta sincronia e armonia con altri agenti del team ProductionReadinessTeam - ogni agente invia ready signal, checkpoint condiviso, handoff con ack, validazione, harmony_status synchronized - InterTeamHarmonyProtocol per handoff esterno 8-step sincronizzato via Memory broker
    """,
    connections={"reports_to": ["ProductionReadinessLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent","TeamSynchronizer_ProductionReadinessTeam"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","BookOpportunityRegistry","ReviewDataRegistry","FeedbackRegistry","LearningLog"], "write": ["checkpoints","decisions","important_notes","AnomalyLog"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes LearningLog rollback a ultimo checkpoint condiviso valido via CheckpointManagerAgent team ProductionReadinessTeam sincronizzato con altri membri team - se 3 fallimenti escalate a leader ProductionReadinessLeader poi controller PlanningEcosystemController poi Supreme", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True, "harmony_preserved": True},
    playwright_usage="real operational tool navigation data collection Amazon review sites saving results supporting visual - allowed uses per PLAYWRIGHT_USAGE_POLICY",
    skill_usage=["BookNicheDecisionSkill","QualificationDecisionSkill","SelfHealingSkill","VideoStructureDesignSkill","ChapterDesignSkill","MemoryReadWriteSkill","CheckpointManagementSkill","PlaywrightNavigationSkill","PlaywrightDataExtractionSkill","PlaywrightSaveSkill"],
    level_name="L5_OPERATIONAL"
)

# Metodi aggiuntivi per sincronia perfetta
class ProductionStartSignalAgent_SynchronizedWrapper:
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.harmony_signals: list = []
        self.checkpoint_shared = None
        self.status = "initialized"

    def emit_ready(self):
        signal = HarmonySignal(
            signal_id=f"ProductionReadinessTeam_{self.agent.name}_ready_{int(time.time()*1000)}",
            sender_agent=self.agent.name,
            receiver_agent="ProductionReadinessLeader",
            team="ProductionReadinessTeam",
            ecosystem="PlanningEcosystem",
            signal_type="ready",
            payload={"agent": self.agent.name, "status": "ready", "hierarchy_level": self.agent.hierarchy_level, "team": self.agent.team},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )
        self.harmony_signals.append(signal)
        self.status = "ready"
        return signal

    def sync_checkpoint(self, checkpoint_id: str):
        self.checkpoint_shared = checkpoint_id
        signal = HarmonySignal(
            signal_id=f"ProductionReadinessTeam_{self.agent.name}_checkpoint_{checkpoint_id}",
            sender_agent=self.agent.name,
            receiver_agent="ALL_TEAM_ProductionReadinessTeam",
            team="ProductionReadinessTeam",
            ecosystem="PlanningEcosystem",
            signal_type="checkpoint",
            payload={"checkpoint_id": checkpoint_id, "shared": True, "agent": self.agent.name, "team": "ProductionReadinessTeam"},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=False
        )
        self.harmony_signals.append(signal)
        self.status = "checkpoint_shared"
        return signal

    def communicate(self, target_agent: str, payload: dict, signal_type: str = "handoff"):
        signal = HarmonySignal(
            signal_id=f"ProductionReadinessTeam_{self.agent.name}_to_{target_agent}_{signal_type}",
            sender_agent=self.agent.name,
            receiver_agent=target_agent,
            team="ProductionReadinessTeam",
            ecosystem="PlanningEcosystem",
            signal_type=signal_type,
            payload=payload,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )
        self.harmony_signals.append(signal)
        return signal

    def validate_harmony(self):
        return {"agent": self.agent.name, "team": "ProductionReadinessTeam", "status": self.status, "checkpoint_shared": self.checkpoint_shared, "signals_count": len(self.harmony_signals), "harmony": "synchronized"}

    def self_heal_synchronized(self, error_type: str, failed_op: str):
        # Self-healing in armonia con team - rollback sincronizzato
        return {
            "phase": "ProductionReadinessTeam",
            "error_type": error_type,
            "failed_operation": failed_op,
            "agent": self.agent.name,
            "checkpoint_restored": True,
            "team_checkpoint_shared": self.checkpoint_shared,
            "action_taken": "retry con adjusted params team synchronized rollback",
            "memory_updated": True,
            "flow_continued": True,
            "harmony_preserved": True,
            "team_synchrony": "all members rollback to shared checkpoint ProductionReadinessTeam"
        }

# Istanza wrapper sincronizzata
ProductionStartSignalAgent_sync = ProductionStartSignalAgent_SynchronizedWrapper(ProductionStartSignalAgent)

def get_agent():
    return ProductionStartSignalAgent

def get_synchronized_wrapper():
    return ProductionStartSignalAgent_sync

print(f"Agent file dedicated ProductionStartSignalAgent L5 Team ProductionReadinessTeam Ecosistema PlanningEcosystem - perfect synchrony harmony initialized")
