
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony
from sync.team_synchronizer import TeamSynchronizer
from core import Team

# Team definition - non è più un unico file per tutti i team, ma file dedicato per DiagnosisTeam
# Ogni agente ha suo file dedicato sotto questa cartella e lavora in sincronia perfetta

TEAM_NAME = "DiagnosisTeam"
ECOSYSTEM = "SelfHealingEcosystem"
SUB_ECOSYSTEM = "DiagnosisSub"
LEADER = "DiagnosisLeader"
MEMBERS = ['DiagnosisLeader', 'RootCauseAnalystAgent', 'ImpactAssessorAgent', 'RecoveryPlannerAgent', 'FailurePatternAnalyzerAgent']

# Synchronizer per garantire perfetta sincronia e armonia
synchronizer = TeamSynchronizer(TEAM_NAME, LEADER, MEMBERS, ECOSYSTEM)
global_harmony.register_team(TEAM_NAME, LEADER, MEMBERS)

TEAM_DEFINITION = Team(
    name=TEAM_NAME,
    ecosystem=ECOSYSTEM,
    sub_ecosystem=SUB_ECOSYSTEM,
    leader_agent=LEADER,
    member_agents=MEMBERS,
    responsibilities=["Responsabilita principale DiagnosisTeam in SelfHealingEcosystem", "Gestisce flusso interno con TeamSynchronyProtocol", "Valida output con validator agent", "Crea checkpoint condiviso via CheckpointManagerAgent", "Gestisce self-healing sincronizzato intra-team", "Esegue handoff esterno 8-step sincronizzato via InterTeamHarmonyProtocol"],
    input_source="Handoff package da ecosistema precedente + memory SelfHealingEcosystem + sync signals",
    output_target="Prossimo team/ecosistema + memory SelfHealingEcosystem + checkpoint condiviso + sync ack",
    internal_communication_protocol={
        "type": "harmonic_synchrony_perfect",
        "protocol": "TeamSynchronyProtocol con HarmonySignal ready checkpoint handoff validation error recovery",
        "flow": "Leader trigger members in ordine o parallelo con ready signals -> members emit checkpoint shared via CheckpointManager -> Validator valida -> se fail self-healing intra-team synchronized rollback -> se pass handoff interno con ack -> leader verifica harmony_status synchronized",
        "synchrony_mechanism": "Ogni agente invia ready signal a leader, leader coordina, checkpoint condiviso broadcast a ALL_TEAM, validazione con ack obbligatorio, harmony_status synchronized validato",
        "harmony_validation": "TeamSynchronyProtocol.validate_harmony() verifica tutti members_ready checkpoint_shared harmony_status synchronized",
        "playwright_integration": "Se team usa Playwright, PlaywrightNavigatorMicroAgent e DataCaptureMicroAgent lavorano in sincronia via TeamSynchronyProtocol con checkpoint condivisi",
        "self_healing_harmony": "Se un agente fallisce, team rimane in sincronia via rollback comune a ultimo checkpoint condiviso validato da CheckpointManagerAgent + RecoveryTeam",
        "memory_shared": "MemoryWriterAgent e MemoryReaderAgent condivisi intra-team con ImportantNotesAgent per risk flags"
    },
    external_handoff_protocol={
        "protocol_name": f"{TEAM_NAME} to next Handoff 8-step InterTeamHarmonyProtocol",
        "steps": [
            "1. DiagnosisLeader (LEADER L3) crea handoff package structured output decisions risks checkpoint ref + harmony_status synchronized",
            "2. MemoryEcosystem MemoryWriterAgent logs handoff",
            "3. Leader conferma ready scrive checkpoint condiviso via CheckpointManagerAgent broadcast ad ALL_TEAM",
            "4. Target team leader conferma receipt legge memory via MemoryReaderAgent + verifica harmony",
            "5. Target team valida completeness via Validator agent interno team",
            "6. Se validation fails -> SelfHealing DetectionTeam",
            "7. Se passes -> Target team inizia lavoro interno flow con TeamSynchronyProtocol",
            "8. Memory logs handoff completion + InterTeamHarmonyProtocol logs"
        ],
        "validation_required": True,
        "memory_logged": True,
        "checkpoint_required": True,
        "self_healing_on_failure": True,
        "harmony_required": True
    },
    hierarchy_level=3
)

def get_synchronizer():
    return synchronizer

def validate_team_harmony():
    return synchronizer.validate_team_harmony()

print(f"Team {TEAM_NAME} synchronizer initialized - leader {LEADER} members {len(MEMBERS)} - perfect synchrony harmony")
