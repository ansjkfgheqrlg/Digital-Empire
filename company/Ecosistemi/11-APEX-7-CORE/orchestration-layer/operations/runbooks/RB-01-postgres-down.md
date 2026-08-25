# RB-01 PostgreSQL unavailable

1. Stop new workflow mutations and task claims; return 503 for writes.
2. Preserve application logs; do not retry side effects without canonical state.
3. Confirm managed failover status and connection health.
4. Restore/fail over through the approved database operator.
5. Run state/audit/outbox consistency checks.
6. Reopen query, then R0, then R1. R2/R3 remain disabled.
