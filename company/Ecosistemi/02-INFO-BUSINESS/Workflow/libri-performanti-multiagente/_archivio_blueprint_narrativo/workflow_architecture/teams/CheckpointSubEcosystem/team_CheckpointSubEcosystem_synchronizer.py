
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony
from sync.team_synchronizer import TeamSynchronizer
from core import Team

TEAM_NAME = "CheckpointSubEcosystem"
ECOSYSTEM = "MemoryEcosystem"
SUB_ECOSYSTEM = "CheckpointSub"
LEADER = "CheckpointSubLeader"
MEMBERS = ['CheckpointSubLeader', 'CheckpointCreatorAgent', 'CheckpointValidatorAgent', 'CheckpointRestorerAgent', 'CheckpointPrunerAgent', 'CheckpointCreateMicroAgent', 'CheckpointRestoreMicroAgent']

synchronizer = TeamSynchronizer(TEAM_NAME, LEADER, MEMBERS, ECOSYSTEM)

TEAM_DEFINITION = Team(
    name=TEAM_NAME,
    ecosystem=ECOSYSTEM,
    sub_ecosystem=SUB_ECOSYSTEM,
    leader_agent=LEADER,
    member_agents=MEMBERS,
    responsibilities=["Team CheckpointSubEcosystem in MemoryEcosystem - perfetta sincronia armonia", "Gestisce flusso interno con TeamSynchronyProtocol", "Checkpoint condiviso", "Self-healing sincronizzato", "Handoff esterno 8-step"],
    input_source="Handoff package + memory MemoryEcosystem + sync signals",
    output_target="Prossimo team + memory + checkpoint condiviso + sync ack",
    internal_communication_protocol={"type": "harmonic_synchrony_perfect", "protocol": "TeamSynchronyProtocol HarmonySignal ready checkpoint handoff validation", "harmony_validation": "validate_harmony synchronized"},
    external_handoff_protocol={"protocol_name": f"{TEAM_NAME} handoff 8-step", "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True, "harmony_required": True},
    hierarchy_level=3
)

def get_synchronizer():
    return synchronizer

print(f"Team {TEAM_NAME} synchronizer initialized - {len(MEMBERS)} members perfect synchrony")
