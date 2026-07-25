"""
╔══════════════════════════════════════════════════════════════╗
║          👑 TEAM CONDUCTOR — Direttore Operativo             ║
║                                                              ║
║  Coordina tutti i team. Assegna missioni con priorità.       ║
║  Monitora la salute di ogni team. Decide chi lavora su cosa. ║
║  Non esegue mai lavoro operativo direttamente.               ║
╚══════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import time
import uuid
from typing import Dict, Any, List, Optional

from event_bus import global_bus
from memory_interface import global_memory


class ConductorTeam:
    """
    👑 Team Conductor — Il Direttore Operativo del sistema.

    Responsabilità:
    - Riceve missioni dall'Orchestrator
    - Le smista ai team giusti (Quant, Forge, Execution, Meta)
    - Tiene traccia della salute di ogni team
    - Non produce output direttamente: orchestra

    Principio: Un direttore che esegue non può giudicare.
    """

    TEAM_NAMES = ["quant", "forge", "execution", "meta"]

    def __init__(self, conductor_id: str = "CONDUCTOR-1"):
        self.conductor_id = conductor_id
        self.active_missions: Dict[str, Dict[str, Any]] = {}
        self.team_health: Dict[str, float] = {t: 1.0 for t in self.TEAM_NAMES}
        self.routing_history: List[Dict[str, Any]] = []

        # Sottoscrive agli eventi di completamento per aggiornare lo stato
        global_bus.subscribe(
            "task.completed",
            self._on_task_completed,
            subscriber_id=f"{conductor_id}.task_done",
        )
        global_bus.subscribe(
            "task.failed",
            self._on_task_failed,
            subscriber_id=f"{conductor_id}.task_fail",
        )
        global_bus.subscribe(
            "agent.health.degraded",
            self._on_team_degraded,
            subscriber_id=f"{conductor_id}.health",
        )

        print(f"[{self.conductor_id}] Team Conductor inizializzato. "
              f"Team sotto gestione: {', '.join(self.TEAM_NAMES)}")

    # ------------------------------------------------------------------ #
    # Smistamento missioni
    # ------------------------------------------------------------------ #

    def dispatch(
        self,
        description: str,
        mission_type: str = "GENERIC",
        priority: str = "NORMAL",
        preferred_team: Optional[str] = None,
    ) -> str:
        """
        Smista una missione al team più adatto.

        Se preferred_team è specificato e sano, lo usa direttamente.
        Altrimenti sceglie il team con la salute più alta.
        """
        mission_id = f"MISSION-{uuid.uuid4().hex[:6].upper()}"
        target_team = self._select_team(mission_type, preferred_team)

        self.active_missions[mission_id] = {
            "description": description,
            "type": mission_type,
            "team": target_team,
            "priority": priority,
            "status": "DISPATCHED",
            "dispatched_at": time.time(),
        }

        self.routing_history.append({
            "mission_id": mission_id,
            "team": target_team,
            "reason": f"Salute team: {self.team_health[target_team]:.0%}",
        })

        print(f"[{self.conductor_id}] Missione {mission_id} → Team {target_team.upper()} "
              f"(salute: {self.team_health[target_team]:.0%}, priorità: {priority})")

        global_bus.publish("task.created", {
            "task_id": mission_id,
            "description": description,
            "priority": priority,
            "assigned_team": target_team,
            "mission_type": mission_type,
        })

        return mission_id

    def _select_team(self, mission_type: str, preferred: Optional[str]) -> str:
        """Seleziona il team ottimale in base a tipo missione e salute."""
        # Mapping tipo → team preferito di default
        type_map = {
            "ANALYSIS": "quant",
            "DATA": "forge",
            "TRADE": "execution",
            "OBSERVE": "meta",
        }

        if preferred and preferred in self.TEAM_NAMES:
            if self.team_health[preferred] >= 0.5:
                return preferred
            print(f"[{self.conductor_id}] Team {preferred} degradato, cerco alternativa.")

        # Prova il team specifico per tipo
        candidate = type_map.get(mission_type, "quant")
        if self.team_health.get(candidate, 0) >= 0.5:
            return candidate

        # Fallback: il team più sano
        return max(self.team_health.items(), key=lambda x: x[1])[0]

    # ------------------------------------------------------------------ #
    # Monitoraggio salute
    # ------------------------------------------------------------------ #

    def _on_task_completed(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        team = payload.get("assigned_team")
        if team and team in self.team_health:
            # Ogni completamento migliora leggermente la salute del team
            self.team_health[team] = min(1.0, self.team_health[team] + 0.02)

    def _on_task_failed(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        team = payload.get("assigned_team")
        if team and team in self.team_health:
            self.team_health[team] = max(0.0, self.team_health[team] - 0.10)
            print(f"[{self.conductor_id}] ⚠️ Team {team} — salute scesa a "
                  f"{self.team_health[team]:.0%}")

    def _on_team_degraded(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        agent_id = payload.get("agent_id", "")
        # Cerca il team dell'agente degradato
        for team in self.TEAM_NAMES:
            if team in agent_id.lower():
                self.team_health[team] = max(0.0, self.team_health[team] - 0.20)
                print(f"[{self.conductor_id}] 🔴 Team {team} segnalato come DEGRADATO.")
                global_memory.write("knowledge", {
                    "event": "team_degraded",
                    "team": team,
                    "agent": agent_id,
                    "health": self.team_health[team],
                }, self.conductor_id, importance=0.75)

    # ------------------------------------------------------------------ #
    # Vista stato
    # ------------------------------------------------------------------ #

    def status(self) -> Dict[str, Any]:
        return {
            "conductor": self.conductor_id,
            "active_missions": len(self.active_missions),
            "team_health": self.team_health,
            "routing_decisions": len(self.routing_history),
        }


# Istanza globale — un solo conductor per sistema
conductor = ConductorTeam()
