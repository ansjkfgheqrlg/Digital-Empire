"""
APEX-7 Orchestration Layer — Self-healing.

Registra ogni guasto e il tentativo di recupero. Non finge mai il successo:
`success` viene dal recovery_fn, e un recupero fallito resta a verbale come
ESCALATED perche' il gate L7 lo veda.
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass(frozen=True)
class HealingAction:
    action_id: str
    failure_type: str
    component: str
    strategy: str
    success: bool
    duration_ms: float
    detail: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "action_id": self.action_id,
            "failure_type": self.failure_type,
            "component": self.component,
            "strategy": self.strategy,
            "success": self.success,
            "duration_ms": round(self.duration_ms, 3),
            "detail": self.detail,
        }


class SelfHealingEngine:
    def __init__(self, bus: Optional[Any] = None, memory: Optional[Any] = None):
        self.bus = bus
        self.memory = memory
        self.history: List[HealingAction] = []

    def handle_failure(
        self,
        failure_type: str,
        component: str,
        recovery_fn: Callable[[], bool],
        strategy: str,
    ) -> HealingAction:
        t0 = time.perf_counter()
        self._emit("system.health.degraded", {"component": component, "failure": failure_type})

        try:
            recovered = bool(recovery_fn())
        except Exception as exc:
            recovered = False
            strategy = f"{strategy} (recovery_fn ha sollevato: {exc})"

        action = HealingAction(
            action_id=f"HEAL_{int(time.time() * 1000)}_{len(self.history)}",
            failure_type=failure_type,
            component=component,
            strategy=strategy,
            success=recovered,
            duration_ms=(time.perf_counter() - t0) * 1000.0,
            detail=f"recupero {'riuscito' if recovered else 'ESCALATED'} via {strategy}",
        )
        self.history.append(action)
        self._emit(
            "system.health.recovered" if recovered else "system.health.escalated",
            action.to_dict(),
        )
        self._remember(action)
        return action

    @property
    def unresolved(self) -> List[HealingAction]:
        return [a for a in self.history if not a.success]

    def _emit(self, event_type: str, data: Dict[str, Any]) -> None:
        if self.bus is not None and hasattr(self.bus, "publish_sync"):
            try:
                self.bus.publish_sync(event_type, data)
            except Exception:
                pass  # il bus non deve poter far cadere il self-healing

    def _remember(self, action: HealingAction) -> None:
        if self.memory is not None and hasattr(self.memory, "log_decision"):
            try:
                # posizionale: la firma di APEX7Memory usa `reason`, BaseAgent la chiama cosi'
                self.memory.log_decision(
                    f"self-healing su {action.component}",
                    action.detail,
                    ["escalation manuale"],
                    0.9 if action.success else 0.3,
                    "self_healing_engine",
                )
            except Exception:
                pass
