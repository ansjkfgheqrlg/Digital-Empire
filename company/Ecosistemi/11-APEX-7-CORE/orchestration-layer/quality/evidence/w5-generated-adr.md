# ADR: Repository analysis baseline

## Status
Accepted for local pilot evaluation.

## Context
The repository fixture contains 2 inspected file(s): README.md, src/app.py. Detected formats: Python, md.

## Decision
Use a deterministic, evidence-linked repository analysis before enabling any probabilistic runtime. Keep the repository read-only and write the ADR only to the scoped artifact store.

## Consequences
- Analysis is reproducible from the cited file hashes.
- No claim is made about files outside the supplied scope.
- RuFlo and external side effects remain disabled.

## Evidence
- `README.md` — `sha256:083bd5116c6ae8b99da14f83839ab958a2d3f50d46aa15da7c2cfd455089b665`
- `src/app.py` — `sha256:7760cf13783ad116dda2dc9bd2fd116e013ba20c7c0b53b4fa35eb8438e9d7f1`
