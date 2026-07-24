# Event Bus Architecture

L'Event Bus è la colonna vertebrale della comunicazione tra gli agenti nell'ecosistema Outreach. Consente lo scambio di informazioni e la coordinazione asincrona e disaccoppiata basata sul pattern Publish-Subscribe.

## Principi Core

- **Zero Coupling**: I publisher non sanno chi riceverà l'evento. I subscriber non sanno chi ha inviato l'evento.
- **Deduplicazione**: Supporta la modalità di consegna `EXACTLY_ONCE` che garantisce che un evento venga elaborato da un subscriber specifico una sola volta, tracciando gli ID evento gestiti.
- **Auditability**: Tutti gli eventi pubblicati sono immagazzinati storicamente nel bus per scopi diagnostici e di telemetria.

---

## Catalogo degli Eventi (Event Catalog)

### Categoria: Task Lifecycle

- **EVT-001: `task.created`**
  - **Publisher**: Orchestrator
  - **Subscribers**: Planner, Memory
  - **Payload**: `{task_id, description, priority, deadline, context}`
  - **Delivery**: `AT_LEAST_ONCE`

- **EVT-002: `task.decomposed`**
  - **Publisher**: Planner
  - **Subscribers**: Writer, Analyst, Memory
  - **Payload**: `{task_id, subtasks[], priority_queue}`
  - **Delivery**: `EXACTLY_ONCE`

- **EVT-003: `task.completed`**
  - **Publisher**: Qualsiasi Agente
  - **Subscribers**: Orchestrator, Memory, Meta-Agent
  - **Payload**: `{task_id, output, quality_score, time_taken_ms}`
  - **Delivery**: `EXACTLY_ONCE`

- **EVT-004: `task.failed`**
  - **Publisher**: Qualsiasi Agente
  - **Subscribers**: Orchestrator, Meta-Agent, Memory
  - **Payload**: `{task_id, error_type, error_message, retry_count, agent_id}`
  - **Delivery**: `AT_LEAST_ONCE` (priorità alta)

---

### Categoria: Quality Control

- **EVT-010: `gate.check.requested`**
  - **Publisher**: Orchestrator
  - **Subscribers**: Gate Agent (GATE-1)
  - **Payload**: `{gate_id, output_to_check, level}`
  - **Delivery**: `EXACTLY_ONCE`

- **EVT-011: `gate.passed`**
  - **Publisher**: Gate Agent
  - **Subscribers**: Orchestrator, Memory
  - **Payload**: `{gate_id, score, criteria_results}`
  - **Delivery**: `EXACTLY_ONCE`

- **EVT-012: `gate.failed`**
  - **Publisher**: Gate Agent
  - **Subscribers**: Refiner, Orchestrator, Memory
  - **Payload**: `{gate_id, score, failed_criteria[], remediation_suggestions, attempt_num}`
  - **Delivery**: `EXACTLY_ONCE`

- **EVT-013: `gate.escalated`**
  - **Publisher**: Gate Agent / Engine
  - **Subscribers**: Meta-Agent, Orchestrator, Human operator
  - **Payload**: `{gate_id, total_attempts, diagnosis, recommended_strategy_change}`
  - **Delivery**: `EXACTLY_ONCE`
