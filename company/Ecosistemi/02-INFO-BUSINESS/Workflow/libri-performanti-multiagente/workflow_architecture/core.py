"""
CORE DATACLASSES - Architecture Foundation
Defines strict schemas required by ABSOLUTE RULES
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class HierarchyLevel(Enum):
    L1_SUPREME = 1
    L2_ECOSYSTEM_CONTROLLER = 2
    L3_TEAM_LEADER = 3
    L4_SENIOR = 4
    L5_OPERATIONAL = 5
    L6_SUPPORT = 6
    L7_MICRO = 7

@dataclass
class Agent:
    name: str
    role: str
    hierarchy_level: int  # 1-7 exact
    team: str
    ecosystem: str
    inputs: List[str]
    outputs: List[str]
    decision_logic: str  # exact logic
    connections: Dict[str, List[str]]  # reports_to, manages, collaborates_with
    memory_access: Dict[str, List[str]]  # read: [...], write: [...]
    self_healing_behavior: Dict[str, Any]
    playwright_usage: Optional[str] = None
    skill_usage: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "name": self.name,
            "hierarchy_level": self.hierarchy_level,
            "team": self.team,
            "ecosystem": self.ecosystem,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "decision_logic": self.decision_logic,
            "connections": self.connections,
            "memory_access": self.memory_access,
            "self_healing_behavior": self.self_healing_behavior,
            "playwright_usage": self.playwright_usage,
            "skills": self.skill_usage
        }

@dataclass
class Team:
    name: str
    ecosystem: str
    leader_agent: str
    member_agents: List[str]
    responsibilities: List[str]
    input_source: str
    output_target: str
    internal_communication_protocol: Dict[str, Any]
    external_handoff_protocol: Dict[str, Any]
    hierarchy_level: int = 3  # team leader level, team itself considered L3

@dataclass
class Skill:
    name: str
    owner_agents: List[str]
    trigger_condition: str
    execution_steps: List[str]
    success_criteria: str
    failure_handling: str
    retry_logic: Dict[str, Any]
    used_in_ecosystems: List[str]

@dataclass
class MemoryComponent:
    name: str
    category: str  # checkpoints, decisions, plans, hierarchies, important_notes
    read_agents: List[str]
    write_agents: List[str]
    data_schema: Dict[str, Any]
    checkpoint_logic: Dict[str, Any]
    validation_rules: List[str]
    ecosystem: str

@dataclass
class Flow:
    name: str
    start_condition: str
    phases: List[Dict[str, Any]]
    decision_gates: List[Dict[str, Any]]
    rollback_points: List[str]
    completion_criteria: str
    involved_ecosystems: List[str]

@dataclass
class Ecosystem:
    name: str
    controller_agent: str
    sub_ecosystems: List[str]
    agents_inside: List[str]
    teams_inside: List[str]
    flows_inside: List[str]
    memory_components_inside: List[str]
    integration_points: Dict[str, List[str]]
    hierarchy_levels_covered: List[int]
