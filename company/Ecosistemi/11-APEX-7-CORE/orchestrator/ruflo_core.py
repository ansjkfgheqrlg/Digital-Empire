"""
APEX-7 RuFLO Core - Rust-powered Orchestration (Python Port)
Simula l'architettura ruvnet/ruflo con performance Python
Event-driven, priority queue, checkpoint, rollback, parallel execution
"""
import asyncio
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Callable, Any, Optional
from enum import Enum
import heapq
import json

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"

class TaskPriority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

@dataclass(order=True)
class PrioritizedTask:
    priority: int
    created_at: datetime = field(compare=False)
    task: Any = field(compare=False)
    
    def __init__(self, task):
        self.priority = task.priority.value if hasattr(task.priority, 'value') else task.priority
        self.created_at = task.created_at
        self.task = task

@dataclass
class Task:
    id: str
    name: str
    agent: str
    payload: Dict[str, Any]
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    dependencies: List[str] = field(default_factory=list)
    result: Any = None
    retries: int = 0
    max_retries: int = 3

class EventBus:
    """Comunicazione asincrona tra agenti - cuore del sistema swarm"""
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.event_log: List[Dict] = []
        self.queue = asyncio.Queue() if self._has_loop() else None

    def _has_loop(self):
        try:
            asyncio.get_event_loop()
            return True
        except:
            return False

    def subscribe(self, event_type: str, handler: Callable):
        self.subscribers.setdefault(event_type, []).append(handler)

    async def publish(self, event_type: str, data: Dict):
        event = {
            "id": str(uuid.uuid4())[:8],
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        self.event_log.append(event)
        # Notifica subscribers
        for handler in self.subscribers.get(event_type, []):
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except Exception as e:
                print(f"[EVENT BUS ERROR] {event_type}: {e}")
        # Broadcast a wildcard subscribers
        for handler in self.subscribers.get("*", []):
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except:
                pass
        return event

    def publish_sync(self, event_type: str, data: Dict):
        """Sync version per contesti non-async"""
        event = {
            "id": str(uuid.uuid4())[:8],
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        self.event_log.append(event)
        for handler in self.subscribers.get(event_type, []):
            if not asyncio.iscoroutinefunction(handler):
                try:
                    handler(event)
                except Exception as e:
                    print(f"[BUS SYNC ERROR] {e}")
        return event

class PriorityTaskQueue:
    def __init__(self):
        self._heap: List[PrioritizedTask] = []
        self._tasks: Dict[str, Task] = {}

    def push(self, task: Task):
        heapq.heappush(self._heap, PrioritizedTask(task))
        self._tasks[task.id] = task

    def pop(self) -> Optional[Task]:
        while self._heap:
            pt = heapq.heappop(self._heap)
            task = pt.task
            # Check dependencies
            if all(self._tasks.get(dep) and self._tasks[dep].status == TaskStatus.COMPLETED for dep in task.dependencies):
                return task
            else:
                # Re-queue if dependencies not met
                heapq.heappush(self._heap, pt)
                # Avoid infinite loop: return None if no task ready
                ready = [pt for pt in self._heap if all(self._tasks.get(d) and self._tasks[d].status == TaskStatus.COMPLETED for d in pt.task.dependencies)]
                if not ready:
                    return None
        return None

    def get(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

class DynamicWorkflowRouter:
    """Decide il prossimo stage basandosi su quality score e contesto"""
    def __init__(self):
        self.routes = {
            "INTAKE": "PARALLEL_EXECUTION",
            "PARALLEL_EXECUTION": "CRITIQUE",
            "CRITIQUE": self._route_after_critique,
            "REFINEMENT": "CRITIQUE",
            "OUTPUT": None
        }
        self.loop_count = {}

    def _route_after_critique(self, context: Dict) -> str:
        score = context.get("critique_score", 0)
        task_id = context.get("task_id", "default")
        self.loop_count[task_id] = self.loop_count.get(task_id, 0)

        if score >= 7.5:
            return "OUTPUT"
        elif score < 4.0 and self.loop_count[task_id] == 0:
            # Restart totale se disastro
            self.loop_count[task_id] += 1
            return "INTAKE"
        elif self.loop_count[task_id] < 3:
            self.loop_count[task_id] += 1
            return "REFINEMENT"
        else:
            # Max loop raggiunto, forza output con warning
            return "OUTPUT"

    def next_stage(self, current_stage: str, context: Dict = None) -> Optional[str]:
        route = self.routes.get(current_stage)
        if callable(route):
            return route(context or {})
        return route

class RuFLOOrchestrator:
    """Meta-Orchestrator che coordina tutto il flusso APEX-7"""
    def __init__(self, memory_system=None):
        self.memory = memory_system
        self.event_bus = EventBus()
        self.task_queue = PriorityTaskQueue()
        self.router = DynamicWorkflowRouter()
        self.agents_registry: Dict[str, Any] = {}
        self.checkpoints: List[Dict] = []
        self.execution_metrics = {
            "tasks_completed": 0,
            "tasks_failed": 0,
            "rollbacks": 0,
            "avg_latency_ms": 0
        }
        self._setup_event_handlers()

    def _setup_event_handlers(self):
        # Logga tutto per memory
        self.event_bus.subscribe("*", lambda e: self._log_event(e))

    def _log_event(self, event):
        if self.memory:
            self.memory.working_memory["event_bus"].append(event)

    def register_agent(self, name: str, agent_instance):
        self.agents_registry[name] = agent_instance
        print(f"[ORCHESTRATOR] Agent registered: {name}")

    def create_checkpoint(self, stage: str, context: Dict) -> str:
        cp_id = str(uuid.uuid4())[:8]
        cp = {
            "id": cp_id,
            "stage": stage,
            "context": context,
            "timestamp": datetime.now().isoformat(),
            "task_queue_state": len(self.task_queue._heap)
        }
        self.checkpoints.append(cp)
        if self.memory:
            self.memory.working_memory["checkpoints"].append(cp)
        self.event_bus.publish_sync("checkpoint_created", cp)
        return cp_id

    def rollback_to(self, checkpoint_id: str) -> bool:
        target = next((c for c in self.checkpoints if c["id"] == checkpoint_id), None)
        if not target:
            return False
        self.execution_metrics["rollbacks"] += 1
        self.event_bus.publish_sync("rollback", {"to": checkpoint_id, "from_stage": target["stage"]})
        if self.memory:
            self.memory.rollback(checkpoint_id)
        print(f"[ORCHESTRATOR] Rolled back to {checkpoint_id} [{target['stage']}]")
        return True

    def decompose_task(self, user_input: str, context: Dict = None) -> List[Task]:
        """STAGE 1: INTAKE - Task decomposition"""
        tasks = []
        base_id = str(uuid.uuid4())[:6]

        # Planner task
        tasks.append(Task(
            id=f"{base_id}-planner",
            name="Decompose & Strategize",
            agent="planner",
            payload={"input": user_input, "context": context or {}},
            priority=TaskPriority.CRITICAL
        ))

        # Analyst & Writer in parallel, dipendono dal planner
        tasks.append(Task(
            id=f"{base_id}-analyst",
            name="Context Analysis & Pattern Mining",
            agent="analyst",
            payload={"input": user_input},
            priority=TaskPriority.HIGH,
            dependencies=[f"{base_id}-planner"]
        ))
        tasks.append(Task(
            id=f"{base_id}-writer",
            name="Generate Content",
            agent="writer",
            payload={"input": user_input},
            priority=TaskPriority.HIGH,
            dependencies=[f"{base_id}-planner"]
        ))

        # Critic after writer+analyst
        tasks.append(Task(
            id=f"{base_id}-critic",
            name="Evaluate & Score",
            agent="critic",
            payload={"input": user_input},
            priority=TaskPriority.HIGH,
            dependencies=[f"{base_id}-writer", f"{base_id}-analyst"]
        ))

        # Refiner conditional
        tasks.append(Task(
            id=f"{base_id}-refiner",
            name="Refine based on Critique",
            agent="refiner",
            payload={"input": user_input},
            priority=TaskPriority.MEDIUM,
            dependencies=[f"{base_id}-critic"]
        ))

        # Meta final
        tasks.append(Task(
            id=f"{base_id}-meta",
            name="Final Quality Gate & Memory Save",
            agent="meta",
            payload={"input": user_input},
            priority=TaskPriority.CRITICAL,
            dependencies=[f"{base_id}-critic", f"{base_id}-refiner"]
        ))

        for t in tasks:
            self.task_queue.push(t)

        self.event_bus.publish_sync("tasks_decomposed", {"count": len(tasks), "base_id": base_id})
        return tasks

    async def execute_workflow(self, user_input: str, context: Dict = None):
        """Flusso completo v3 + v4 con parallelismo"""
        print(f"\n[APEX-7] START Workflow: {user_input[:60]}...")
        stages = ["INTAKE", "PARALLEL_EXECUTION", "CRITIQUE", "REFINEMENT", "OUTPUT"]
        current_context = {"input": user_input, "context": context or {}, "critique_score": 0, "task_id": str(uuid.uuid4())}

        # STAGE 1
        stage = "INTAKE"
        self.create_checkpoint(stage, current_context)
        self.event_bus.publish_sync("stage_start", {"stage": stage})
        
        tasks = self.decompose_task(user_input, context)
        
        # Simulate agent execution with dynamic routing
        for stage in stages:
            self.event_bus.publish_sync("stage_start", {"stage": stage})
            print(f"[FLOW] → {stage}")

            if stage == "PARALLEL_EXECUTION":
                # Esecuzione parallela reale
                planner_task = next((t for t in tasks if t.agent == "planner"), None)
                if planner_task and planner_task.agent in self.agents_registry:
                    planner_task.result = await self._execute_agent_task(planner_task)
                
                # Parallel: writer + analyst
                parallel_tasks = [t for t in tasks if t.agent in ("writer", "analyst") and t.status == TaskStatus.PENDING]
                if parallel_tasks:
                    results = await asyncio.gather(
                        *[self._execute_agent_task(t) for t in parallel_tasks],
                        return_exceptions=True
                    )
                    for task, res in zip(parallel_tasks, results):
                        task.result = res
                        current_context[f"{task.agent}_output"] = res

            elif stage == "CRITIQUE":
                critic_task = next((t for t in tasks if t.agent == "critic"), None)
                if critic_task:
                    critic_result = await self._execute_agent_task(critic_task, current_context)
                    current_context["critique_output"] = critic_result
                    current_context["critique_score"] = critic_result.get("score", 0) if isinstance(critic_result, dict) else 7.0
                    print(f"[CRITIC] Score: {current_context['critique_score']}")

                    # Dynamic routing decision
                    next_stage = self.router.next_stage(stage, current_context)
                    print(f"[ROUTER] Critique {current_context['critique_score']} -> {next_stage}")
                    if next_stage == "OUTPUT":
                        stage = "OUTPUT"
                        break
                    elif next_stage == "INTAKE":
                        print("[ROUTER] Score <4.0, restarting workflow...")
                        return await self.execute_workflow(user_input, context)

            elif stage == "REFINEMENT":
                refiner_task = next((t for t in tasks if t.agent == "refiner"), None)
                if refiner_task:
                    current_context["refine_input"] = current_context.get("writer_output")
                    refiner_result = await self._execute_agent_task(refiner_task, current_context)
                    current_context["writer_output"] = refiner_result  # overwrite with refined

            elif stage == "OUTPUT":
                meta_task = next((t for t in tasks if t.agent == "meta"), None)
                if meta_task:
                    final = await self._execute_agent_task(meta_task, current_context)
                    current_context["final_output"] = final

            self.create_checkpoint(stage, current_context)
            self.event_bus.publish_sync("stage_complete", {"stage": stage, "context": current_context})

        print(f"[APEX-7] END - Final Score: {current_context.get('critique_score')}")
        return current_context

    async def _execute_agent_task(self, task: Task, context: Dict = None):
        agent = self.agents_registry.get(task.agent)
        if not agent:
            print(f"[WARN] Agent {task.agent} not registered, using mock")
            task.status = TaskStatus.COMPLETED
            return {"mock": True, "content": f"Mock output from {task.agent}"}
        
        task.status = TaskStatus.RUNNING
        try:
            payload = {**task.payload, **(context or {})}
            if asyncio.iscoroutinefunction(agent.execute):
                result = await agent.execute(payload)
            else:
                result = agent.execute(payload)
            task.status = TaskStatus.COMPLETED
            task.result = result
            self.execution_metrics["tasks_completed"] += 1
            self.event_bus.publish_sync("task_completed", {"task_id": task.id, "agent": task.agent})
            return result
        except Exception as e:
            task.retries += 1
            if task.retries < task.max_retries:
                print(f"[RETRY] {task.id} attempt {task.retries}: {e}")
                task.status = TaskStatus.PENDING
                self.task_queue.push(task)
                return None
            task.status = TaskStatus.FAILED
            self.execution_metrics["tasks_failed"] += 1
            self.event_bus.publish_sync("task_failed", {"task_id": task.id, "error": str(e)})
            raise

    def get_metrics(self):
        return self.execution_metrics

# Test
if __name__ == "__main__":
    orch = RuFLOOrchestrator()
    print("RuFLO Core initialized with components:", list(orch.__dict__.keys()))
