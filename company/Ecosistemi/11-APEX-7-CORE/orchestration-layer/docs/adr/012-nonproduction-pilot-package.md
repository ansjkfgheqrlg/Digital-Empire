# ADR-012 — Package and rehearse a non-production CLI pilot

- **Status:** Accepted for W12
- **Date:** 2026-08-23

## Decision

Build a reproducible `ocp-0.1.0-pilot` source package and Python wheel, define a rootless container and local Compose environment, and rehearse release rings through PILOT. Production promotion is intentionally blocked by PRR `NO_GO`, then the rehearsal rolls back.

This package exposes the LocalRuntime CLI vertical slice, not a network API/worker service. RuFlo execution, R2 and R3 remain disabled.

## Consequences

- The engineering program W0–W12 is complete as a non-production implementation candidate.
- No production deployment or real traffic occurred.
- Docker/Compose definitions were statically validated but not built in this sandbox because no container runtime is available.
- Production requires resolving PRR blockers and implementing/validating the final API/worker deployment surface.
