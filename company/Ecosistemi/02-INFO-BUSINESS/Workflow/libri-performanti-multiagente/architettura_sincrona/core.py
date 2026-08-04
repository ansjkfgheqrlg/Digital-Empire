"""
CORE 7-LEVEL ARCHITECTURE - Dataclasses per validazione rigorosa
Ogni agente deve avere: name, role, hierarchy_level, team, inputs, outputs, decision_logic, connections, memory_access, self_healing_behavior
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class Agent:
    name: str
    role: str
    hierarchy_level: int
    team: str
    ecosystem: str
    sub_ecosystem: Optional[str]
    inputs: List[str]
    outputs: List[str]
    decision_logic: str
    connections: Dict[str, List[str]]
    memory_access: Dict[str, List[str]]
    self_healing_behavior: Dict[str, Any]
    playwright_usage: Optional[str] = None
    skill_usage: List[str] = field(default_factory=list)
    level_name: str = ""

@dataclass
class Team:
    name: str
    ecosystem: str
    sub_ecosystem: Optional[str]
    leader_agent: str
    member_agents: List[str]
    responsibilities: List[str]
    input_source: str
    output_target: str
    internal_communication_protocol: Dict[str, Any]
    external_handoff_protocol: Dict[str, Any]
    hierarchy_level: int = 3

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
    hierarchy_levels: List[int]

@dataclass
class MemoryComponent:
    name: str
    category: str
    read_agents: List[str]
    write_agents: List[str]
    data_schema: Dict[str, Any]
    checkpoint_logic: Dict[str, Any]
    validation_rules: List[str]
    ecosystem: str
    sub_ecosystem: Optional[str]

@dataclass
class Flow:
    name: str
    start_condition: str
    phases: List[Dict[str, Any]]
    decision_gates: List[Dict[str, Any]]
    rollback_points: List[str]
    completion_criteria: str
    involved_ecosystems: List[str]
    sub_flows: List[str] = field(default_factory=list)

@dataclass
class Ecosystem:
    name: str
    controller_agent: str
    sub_ecosystems: List[Dict[str, Any]]
    agents_inside: List[str]
    teams_inside: List[str]
    flows_inside: List[str]
    memory_components_inside: List[str]
    skills_inside: List[str]
    integration_points: Dict[str, List[str]]
    hierarchy_levels_covered: List[int]
    description: str = ""
