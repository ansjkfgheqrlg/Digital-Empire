from __future__ import annotations

import asyncio
import base64
import ipaddress
import os
from pathlib import Path

import httpx
import uvicorn
from sqlalchemy import text

from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory
from orchestrator.api.app import ApiContext, create_app
from orchestrator.application.workflow_service import WorkflowService
from orchestrator.identity import OperatorIdentityService, OperatorRegistry, SessionService
from orchestrator.observability import ComponentHealth, HealthService, OcpMetrics


def build_app():
    tenant = os.environ.get("OCP_TENANT_ID", "local-pilot")
    engine, factory = create_engine_and_factory(os.environ["OCP_DATABASE_URL"])
    registry = OperatorRegistry()
    public_key = base64.b64decode(os.environ["OCP_OPERATOR_PUBLIC_KEY_B64"], validate=True)
    registry.register_raw_public_key(
        os.environ.get("OCP_OPERATOR_ID", "local-owner"),
        public_key,
        {"LOCAL_OWNER", "TOKEN_ISSUER"},
    )

    async def postgres_probe() -> ComponentHealth:
        async with PostgresUnitOfWork(factory, tenant) as uow:
            await uow.session.execute(text("SELECT 1"))
            await uow.commit()
        return ComponentHealth("postgres", "UP", required=True)

    async def opa_probe() -> ComponentHealth:
        url = os.environ.get("OCP_OPA_URL", "http://127.0.0.1:8181").rstrip("/") + "/health"
        async with httpx.AsyncClient(timeout=1.0) as client:
            response = await client.get(url)
            response.raise_for_status()
        return ComponentHealth("opa", "UP", required=True)

    async def ruflo_probe() -> ComponentHealth:
        return ComponentHealth("ruflo", "DOWN", "disabled by profile", required=False)

    context = ApiContext(
        identity=OperatorIdentityService(registry),
        sessions=SessionService(),
        workflows=WorkflowService(lambda value: PostgresUnitOfWork(factory, value), tenant),
        health=HealthService([postgres_probe, opa_probe, ruflo_probe]),
        metrics=OcpMetrics(),
    )
    app = create_app(context)

    @app.on_event("shutdown")
    async def shutdown_engine() -> None:
        await engine.dispose()

    return app


def main() -> None:
    loopback = str(ipaddress.IPv4Address(0x7F000001))
    container_any = str(ipaddress.IPv4Address(0))
    host = os.environ.get("OCP_BIND_HOST", loopback)
    external_bind_allowed = (
        os.environ.get("OCP_CONTAINERIZED") == "true"
        or os.environ.get("OCP_PREVIEW") == "true"
    )
    if host != loopback and not (host == container_any and external_bind_allowed):
        raise RuntimeError(
            "Local pilot may bind only loopback, an explicitly containerized interface, or preview mode"
        )
    uvicorn.run(build_app(), host=host, port=int(os.environ.get("OCP_PORT", "8000")))


if __name__ == "__main__":
    main()
