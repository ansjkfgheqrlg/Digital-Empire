"""
APEX-7 Base Agent - Classe astratta per tutti gli agenti dello swarm
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from datetime import datetime
import uuid

class BaseAgent(ABC):
    def __init__(self, name: str, role: str, system_prompt: str):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.id = f"{name}-{str(uuid.uuid4())[:4]}"
        self.execution_count = 0
        self.memory = None

    def attach_memory(self, memory_system):
        self.memory = memory_system

    @abstractmethod
    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def log_decision(self, decision: str, why: str, alternatives: List[str], confidence: float):
        if self.memory:
            return self.memory.log_decision(decision, why, alternatives, confidence, self.name)
        return None

    def _timestamp(self):
        return datetime.now().isoformat()
