# BUS CONFIG — Configurazione Event Bus

> Configurazione operativa dell'Event Bus di APEX-7.

---

## Priorities

| Priority | Label | Delivery SLA | Retry Interval | Max Retries | On Exhaustion |
|---|---|---|---|---|---|
| P0 | CRITICAL | Immediate | 1 second | 10 | ESCALATE HUMAN |
| P1 | HIGH | ≤ 5 seconds | 5 seconds | 5 | ESCALATE META |
| P2 | NORMAL | ≤ 30 seconds | 30 seconds | 3 | LOG + CONTINUE |
| P3 | LOW | Best-effort | 60 seconds | 1 | DROP |

---

## Consumer Routing

| Event Pattern | Consumers |
|---|---|
| `task.*` | ORCHESTRATOR, MEMORY |
| `draft.*` | CRITIC, MEMORY |
| `critique.*` | ORCHESTRATOR, REFINER, GATE_AGENT, META_AGENT |
| `gate.*` | ORCHESTRATOR, REFINER, META_AGENT |
| `analysis.*` | WRITER, MEMORY |
| `refinement.*` | CRITIC, MEMORY |
| `memory.*` | META_AGENT |
| `system.*` | ORCHESTRATOR, META_AGENT, ALL |
| `meta.*` | ORCHESTRATOR |
| `agent.*` | ORCHESTRATOR, META_AGENT |

---

## Event Format

```json
{
  "event_id": "EVT-{uuid}",
  "event_type": "task.created",
  "priority": "P2",
  "timestamp": "ISO-8601",
  "source_agent": "ORCHESTRATOR",
  "target_agents": ["PLANNER", "MEMORY"],
  "session_id": "sess-{uuid}",
  "payload": {},
  "correlation_id": "CORR-{uuid}",
  "retry_count": 0
}
```

---

## Bus Health Monitoring

META AGENT monitora:
- Eventi in coda per priority
- Latenza media di consegna
- Eventi droppati (P3)
- Eventi in retry > 3
- Consumer non responsivi

Alert se:
- Coda P0 > 10 eventi
- Coda P1 > 50 eventi
- Evento P0 in retry > 5
- Consumer non risponde da > 120s
