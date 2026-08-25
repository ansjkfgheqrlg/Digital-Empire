# ADR-007 — RuFlo bridge implemented but execution routing remains disabled

- **Status:** Accepted for W7
- **Date:** 2026-08-23

## Evidence

The public repository was audited at commit `3c99b1c84a25948c42a163253bac6effed5fbbbb`; npm runtime `ruflo@3.38.19` was pinned. MCP protocol `2024-11-05` returned 333 tools. Required tool names and schema hashes were recorded.

Real MCP smoke calls passed for health, swarm initialization/status/shutdown and agent spawn/status/terminate. A credential-free `agent_execute` failed closed as expected. SIGKILL and restart preserved handshake/schema compatibility.

## Decision

The TypeScript bridge, schema guard and supervisor are accepted as implemented. RuFlo execution routing remains disabled because successful provider-backed `agent_execute`, output quality evaluation and canary comparison have not been certified. LocalRuntime remains the active baseline.

## Consequences

- No false claim that RuFlo is production-ready.
- Schema drift blocks bridge startup.
- Swarm state remains non-canonical.
- Memory, federation and autoscaling are disabled.
- W8 may activate the Builder Swarm only in sandbox after provider-backed execution evidence exists.
