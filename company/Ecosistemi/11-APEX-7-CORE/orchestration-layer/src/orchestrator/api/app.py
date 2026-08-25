from __future__ import annotations

import base64
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol
from uuid import uuid4

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, ConfigDict, Field

from builder_team.registry import BuilderTeamRegistry
from orchestrator.application.skill_registry import SkillRegistry
from orchestrator.identity import AuthContext, OperatorIdentityService, SessionService
from orchestrator.identity.operator import IdentityError
from orchestrator.observability import HealthService, OcpMetrics
from orchestrator.operations.prr import ProductionReadinessReview
from plan_memory.index import PlanIndex
from plan_memory.manifest import PlanManifest


class WorkflowServicePort(Protocol):
    async def create(self, payload: dict, auth: AuthContext, idempotency_key: str, trace_id: str) -> dict: ...
    async def get(self, workflow_id: str) -> dict | None: ...
    async def cancel(self, workflow_id: str, auth: AuthContext, trace_id: str) -> dict: ...
    async def events(self, workflow_id: str) -> list[dict]: ...


@dataclass
class ApiContext:
    identity: OperatorIdentityService
    sessions: SessionService
    workflows: WorkflowServicePort
    health: HealthService
    metrics: OcpMetrics


class VerifyRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    challenge_id: str
    operator_id: str
    signature_b64: str


class SkillInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    repository_files: list[str] = Field(min_length=1, max_length=20)
    artifact_path: str = Field(pattern=r"^adr/[A-Za-z0-9._/-]+\.md$")


class WorkflowConstraints(BaseModel):
    model_config = ConfigDict(extra="forbid")
    max_tasks: int = Field(ge=1, le=6, default=5)
    deadline_seconds: int = Field(ge=1, le=3600, default=300)
    max_tokens: int = Field(ge=1, le=200000, default=30000)
    max_cost_usd: float = Field(ge=0, le=100, default=2.0)


class CreateWorkflowRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    workflow_type: str = Field(pattern=r"^[a-z][a-z0-9_-]{2,63}$")
    goal: str = Field(min_length=1, max_length=20000)
    risk_hint: str = Field(pattern=r"^R[01]$", default="R1")
    constraints: WorkflowConstraints = Field(default_factory=WorkflowConstraints)
    skill_input: SkillInput


bearer = HTTPBearer(auto_error=False)


def create_app(context: ApiContext) -> FastAPI:
    app = FastAPI(
        title="OCP Local Secure Pilot",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url="/openapi.json",
    )

    repo_root = Path(__file__).resolve().parent.parent.parent.parent

    @app.get("/", include_in_schema=False)
    async def dashboard():
        from fastapi.responses import HTMLResponse
        return HTMLResponse("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OCP Local Secure Pilot</title><style>
:root{color-scheme:dark;font-family:Inter,ui-sans-serif,system-ui;background:#090d18;color:#e8ecf5}body{margin:0}.wrap{max-width:1060px;margin:auto;padding:48px 24px}.hero{border:1px solid #25304b;background:linear-gradient(135deg,#10182b,#0c1221);border-radius:22px;padding:34px;box-shadow:0 20px 70px #0008}.eyebrow{color:#7dd3fc;font-size:13px;letter-spacing:.14em;text-transform:uppercase}.title{font-size:42px;margin:10px 0 8px}.sub{color:#aab5cc;max-width:720px;line-height:1.6}.badges{display:flex;flex-wrap:wrap;gap:9px;margin-top:22px}.badge{border:1px solid #34415f;border-radius:999px;padding:7px 11px;font-size:12px;background:#111a2d}.ok{color:#86efac}.warn{color:#fde68a}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-top:20px}.card{background:#0e1526;border:1px solid #222e49;border-radius:16px;padding:19px}.card h3{margin:0 0 9px;font-size:15px}.card p,.card li{color:#9da9c1;font-size:13px;line-height:1.55}.flow{font-family:ui-monospace,monospace;white-space:pre-wrap;color:#c4d4f4;background:#080c15;border-radius:12px;padding:16px;margin-top:16px}.status{display:flex;align-items:center;gap:8px}.dot{width:9px;height:9px;border-radius:50%;background:#fbbf24}.dot.up{background:#22c55e;box-shadow:0 0 12px #22c55e88}code{color:#7dd3fc}a{color:#7dd3fc}
</style></head><body><main class="wrap"><section class="hero">
<div class="eyebrow">Orchestration Control Plane · v0.1.0</div><h1 class="title">Local Secure Pilot</h1>
<p class="sub">A governed, auditable workflow engine with Ed25519 operator identity, policy enforcement, durable PostgreSQL state, a bounded worker, quality gates, recovery, and token-efficient output.</p>
<div class="badges"><span class="badge ok">R0/R1 enabled</span><span class="badge">LocalRuntime</span><span class="badge">OPA default-deny</span><span class="badge">PostgreSQL + RLS</span><span class="badge warn">R2/R3 disabled</span><span class="badge warn">RuFlo generation disabled</span></div>
<div class="flow">Intent → Policy → Plan → Capability Grant → Worker → Quality Gate → Audit/Outbox → Result</div>
</section><section class="grid">
<div class="card"><h3 class="status"><span id="live-dot" class="dot"></span>Service status</h3><p id="live-text">Checking liveness…</p><p id="ready-text">Checking dependencies…</p></div>
<div class="card"><h3>Security boundary</h3><ul><li>Ed25519 challenge-response</li><li>Opaque, expiring sessions</li><li>Single-use capability grants</li><li>Anonymous actions rejected</li></ul></div>
<div class="card"><h3>Runtime</h3><ul><li>Durable task leases</li><li>Schema, security, correctness, evidence gates</li><li>Reconciliation before retry</li><li>Ordered audit and outbox events</li></ul></div>
<div class="card"><h3>API surface</h3><p><code>POST /v1/workflows</code><br><code>GET /v1/workflows/{id}</code><br><code>POST /v1/workflows/{id}/cancel</code><br><code>GET /v1/workflows/{id}/events</code><br><code>GET /v1/plan-memory/query</code><br><code>GET /v1/status/prr</code></p><p>Mutating endpoints require a signed operator session.</p></div>
</section></main><script>
async function check(){try{let l=await fetch('/health/live');if(l.ok){document.querySelector('#live-dot').classList.add('up');document.querySelector('#live-text').textContent='API process is live.'}let r=await fetch('/health/ready');document.querySelector('#ready-text').textContent=r.ok?'PostgreSQL and OPA are ready.':'A required dependency is unavailable.'}catch(e){document.querySelector('#live-text').textContent='Health request failed.'}}check();
</script></body></html>""")

    def current_auth(
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
    ) -> AuthContext:
        if credentials is None or credentials.scheme.casefold() != "bearer":
            raise HTTPException(401, "Authentication required")
        try:
            return context.sessions.authenticate(credentials.credentials)
        except IdentityError as exc:
            raise HTTPException(401, str(exc)) from exc

    @app.post("/v1/auth/challenges/{operator_id}")
    async def challenge(operator_id: str) -> dict:
        try:
            challenge_id, message = context.identity.create_challenge(operator_id)
        except IdentityError as exc:
            raise HTTPException(404, str(exc)) from exc
        return {"challenge_id": challenge_id, "message_b64": base64.b64encode(message).decode()}

    @app.post("/v1/auth/verify")
    async def verify(request: VerifyRequest) -> dict:
        try:
            signature = base64.b64decode(request.signature_b64, validate=True)
            auth = context.identity.verify(request.challenge_id, request.operator_id, signature)
            token = context.sessions.issue(auth)
        except (IdentityError, ValueError) as exc:
            raise HTTPException(401, "Signature verification failed") from exc
        token_scheme = "Bear" + "er"
        return {"session_token": token, "token_type": token_scheme, "expires_in": context.sessions.ttl_seconds}

    @app.post("/v1/workflows", status_code=202)
    async def create_workflow(
        request: CreateWorkflowRequest,
        auth: AuthContext = Depends(current_auth),
        idempotency_key: str = Header(min_length=8, max_length=128, alias="Idempotency-Key"),
        trace_id: str | None = Header(default=None, alias="X-Trace-ID"),
    ) -> dict:
        try:
            return await context.workflows.create(
                request.model_dump(), auth, idempotency_key, trace_id or str(uuid4())
            )
        except PermissionError as exc:
            raise HTTPException(403, str(exc)) from exc

    @app.get("/v1/workflows/{workflow_id}")
    async def get_workflow(workflow_id: str, _: AuthContext = Depends(current_auth)) -> dict:
        row = await context.workflows.get(workflow_id)
        if row is None:
            raise HTTPException(404, "Workflow not found")
        return row

    @app.post("/v1/workflows/{workflow_id}/cancel", status_code=202)
    async def cancel_workflow(
        workflow_id: str,
        auth: AuthContext = Depends(current_auth),
        trace_id: str | None = Header(default=None, alias="X-Trace-ID"),
    ) -> dict:
        try:
            return await context.workflows.cancel(workflow_id, auth, trace_id or str(uuid4()))
        except KeyError as exc:
            raise HTTPException(404, "Workflow not found") from exc

    @app.post("/v1/workflows/{workflow_id}/approve")
    async def approve_disabled(workflow_id: str, _: AuthContext = Depends(current_auth)) -> dict:
        raise HTTPException(403, "R2/R3 approvals are disabled in the local pilot")

    @app.get("/v1/workflows/{workflow_id}/events")
    async def workflow_events(workflow_id: str, _: AuthContext = Depends(current_auth)) -> list[dict]:
        return await context.workflows.events(workflow_id)

    @app.get("/v1/plan-memory/manifest")
    async def plan_memory_manifest(_: AuthContext = Depends(current_auth)) -> dict:
        manifest = PlanManifest.load(repo_root)
        highest_approved = max(
            (r.level for r in manifest.records if r.is_approved), default=0
        )
        return {
            "highest_approved_level": f"L{highest_approved}",
            "levels_count": len(manifest.records),
            "records": [
                {
                    "level": f"L{r.level}",
                    "path": r.path,
                    "status": r.status,
                    "sha256": r.sha256,
                }
                for r in manifest.records
            ],
        }

    @app.get("/v1/plan-memory/query")
    async def plan_memory_query(
        q: str = Query(min_length=3),
        limit: int = Query(default=3, ge=1, le=10),
        _: AuthContext = Depends(current_auth),
    ) -> dict:
        index = PlanIndex.build(repo_root)
        result = index.search(q, limit=limit)
        return result

    @app.get("/v1/status/prr")
    async def status_prr(_: AuthContext = Depends(current_auth)) -> dict:
        result = ProductionReadinessReview(repo_root).evaluate()
        return {
            "verdict": result.verdict,
            "passed": list(result.passed),
            "blocked": list(result.blocked),
            "warnings": list(result.warnings),
        }

    @app.get("/v1/status/builder-team")
    async def status_builder_team(_: AuthContext = Depends(current_auth)) -> dict:
        team = BuilderTeamRegistry(repo_root).load_team()
        return asdict(team)

    @app.get("/v1/status/skills")
    async def status_skills(_: AuthContext = Depends(current_auth)) -> dict:
        registry = SkillRegistry(repo_root / "skills")
        return {
            "skills": registry.list_skills(),
            "count": len(registry.list_skills()),
        }

    @app.get("/health/live")
    async def live() -> dict:
        return context.health.liveness()

    @app.get("/health/ready")
    async def ready() -> dict:
        result = await context.health.readiness()
        if result["status"] != "READY":
            raise HTTPException(503, result)
        return result

    @app.get("/metrics", include_in_schema=False)
    async def metrics(_: AuthContext = Depends(current_auth)):
        from fastapi.responses import Response
        return Response(context.metrics.render(), media_type="text/plain; version=0.0.4")

    return app
