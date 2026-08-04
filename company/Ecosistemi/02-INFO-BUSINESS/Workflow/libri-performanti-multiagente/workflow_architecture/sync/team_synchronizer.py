
"""
TEAM SYNCHRONIZER - Assicura che ogni agente in team lavori in sincronia perfetta
Ogni agente ha suo file dedicato ma sincronizzato via TeamSynchronyProtocol
"""

import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony, TeamSynchronyProtocol, HarmonySignal
from core import Agent
from typing import List

class TeamSynchronizer:
    def __init__(self, team_name: str, leader_agent: str, member_agents: List[str], ecosystem: str):
        self.team_name = team_name
        self.leader_agent = leader_agent
        self.member_agents = member_agents
        self.ecosystem = ecosystem
        self.protocol = global_harmony.register_team(team_name, leader_agent, member_agents)
        self.agents_instances: dict = {}

    def register_agent_instance(self, agent: Agent):
        self.agents_instances[agent.name] = agent
        # Emit ready signal
        signal = self.protocol.emit_ready(agent.name)
        # In real system: send via message bus, wait ack from leader
        return signal

    def synchronize_checkpoint(self, agent_name: str, checkpoint_id: str):
        signal = self.protocol.emit_checkpoint(agent_name, checkpoint_id)
        # Broadcast to all team members
        # All members update shared checkpoint via CheckpointManagerAgent
        return signal

    def internal_handoff(self, from_agent: str, to_agent: str, package: dict):
        signal = self.protocol.emit_handoff_internal(from_agent, to_agent, package)
        # Wait ack from receiver
        return signal

    def validate_team_harmony(self):
        return self.protocol.validate_harmony()

    def get_harmony_status(self):
        return global_harmony.check_global_harmony()

# Example usage for a team - will be instantiated per team folder
