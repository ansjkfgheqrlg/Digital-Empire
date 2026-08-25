from __future__ import annotations

import json
from pathlib import Path

from orchestrator.api.app import ApiContext, create_app
from orchestrator.identity import OperatorIdentityService, OperatorRegistry, SessionService
from orchestrator.observability import ComponentHealth, HealthService, OcpMetrics


class NoopWorkflowService:
    async def create(self, *args, **kwargs): return {}
    async def get(self, *args, **kwargs): return None
    async def cancel(self, *args, **kwargs): return {}
    async def events(self, *args, **kwargs): return []


async def up(): return ComponentHealth("export", "UP")


def main() -> int:
    app = create_app(
        ApiContext(
            OperatorIdentityService(OperatorRegistry()),
            SessionService(),
            NoopWorkflowService(),
            HealthService([up]),
            OcpMetrics(),
        )
    )
    target = Path("docs/api/openapi.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(app.openapi(), indent=2) + "\n")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
