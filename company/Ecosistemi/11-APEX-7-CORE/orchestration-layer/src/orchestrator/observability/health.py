from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable


HealthProbe = Callable[[], Awaitable["ComponentHealth"]]


@dataclass(frozen=True)
class ComponentHealth:
    name: str
    status: str
    detail: str = ""
    required: bool = True


class HealthService:
    def __init__(self, probes: list[HealthProbe], timeout_seconds: float = 2.0):
        self.probes = probes
        self.timeout_seconds = timeout_seconds

    def liveness(self) -> dict:
        return {"status": "LIVE"}

    async def readiness(self) -> dict:
        async def run(probe: HealthProbe) -> ComponentHealth:
            try:
                return await asyncio.wait_for(probe(), timeout=self.timeout_seconds)
            except TimeoutError:
                return ComponentHealth("unknown", "DOWN", "probe timeout", True)
            except Exception as exc:
                return ComponentHealth("unknown", "DOWN", type(exc).__name__, True)

        components = await asyncio.gather(*(run(probe) for probe in self.probes))
        ready = all(
            component.status in {"UP", "DEGRADED"} if component.required else True
            for component in components
        )
        # Required components must be UP; DEGRADED is accepted only for optional components.
        ready = all(
            component.status == "UP" for component in components if component.required
        )
        return {
            "status": "READY" if ready else "NOT_READY",
            "components": [component.__dict__ for component in components],
        }
