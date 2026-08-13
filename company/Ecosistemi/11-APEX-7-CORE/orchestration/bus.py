"""
APEX-7 Orchestration Layer — Event bus strumentato.

L'`EventBus` del motore condiviso inghiotte le eccezioni degli handler in un
`print`: una consegna fallita non lascia traccia ispezionabile, quindi nessun
gate puo' accorgersene.

Questa sottoclasse aggiunge i due registri che mancavano — `failed_deliveries`
e `dead_letter_queue` — SENZA toccare `orchestrator/ruflo_core.py` (ADR-003:
wrap, mai riscrittura). E' drop-in: chi si aspetta un EventBus riceve un
EventBus.

Nessun contatore di retry finto: qui non esiste un loop che riprova, quindi un
evento con anche una sola consegna fallita entra subito in DLQ. Chiamarlo
"retry" renderebbe la metrica una bugia.
"""
from __future__ import annotations

import asyncio
from datetime import datetime
from typing import Any, Callable, Dict, List
import uuid

try:  # il layer resta importabile anche fuori dall'ecosistema
    from orchestrator.ruflo_core import EventBus as _BaseEventBus
except Exception:  # pragma: no cover
    class _BaseEventBus:  # type: ignore[no-redef]
        def __init__(self):
            self.subscribers: Dict[str, List[Callable]] = {}
            self.event_log: List[Dict] = []

        def subscribe(self, event_type: str, handler: Callable):
            self.subscribers.setdefault(event_type, []).append(handler)

        def publish_sync(self, event_type: str, data: Dict):
            event = {"id": str(uuid.uuid4())[:8], "type": event_type, "data": data,
                     "timestamp": datetime.now().isoformat()}
            self.event_log.append(event)
            for h in self.subscribers.get(event_type, []):
                h(event)
            return event

        async def publish(self, event_type: str, data: Dict):
            return self.publish_sync(event_type, data)


class InstrumentedEventBus(_BaseEventBus):
    """EventBus che tiene il conto delle consegne fallite."""

    def __init__(self):
        super().__init__()
        self.dead_letter_queue: List[Dict] = []
        self.failed_deliveries: List[str] = []

    @property
    def dlq_size(self) -> int:
        return len(self.dead_letter_queue)

    # ── registrazione dei guasti ────────────────────────────────────────────

    def _record_failure(self, event: Dict, handler: Callable, exc: Exception) -> None:
        nome = getattr(handler, "__name__", repr(handler))
        self.failed_deliveries.append(f"{event.get('type')} -> {nome}: {exc}")
        event["delivery_failures"] = event.get("delivery_failures", 0) + 1
        if not any(d.get("id") == event.get("id") for d in self.dead_letter_queue):
            self.dead_letter_queue.append(event)

    def _deliver(self, event: Dict, handler: Callable) -> None:
        try:
            handler(event)
        except Exception as exc:
            self._record_failure(event, handler, exc)

    # ── override: stessa firma, stesso ritorno ──────────────────────────────

    def publish_sync(self, event_type: str, data: Dict) -> Dict:
        event = {
            "id": str(uuid.uuid4())[:8],
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
        }
        self.event_log.append(event)
        for handler in self.subscribers.get(event_type, []):
            if not asyncio.iscoroutinefunction(handler):
                self._deliver(event, handler)
        return event

    async def publish(self, event_type: str, data: Dict) -> Dict:
        event = {
            "id": str(uuid.uuid4())[:8],
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
        }
        self.event_log.append(event)
        for handler in (self.subscribers.get(event_type, []) + self.subscribers.get("*", [])):
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except Exception as exc:
                self._record_failure(event, handler, exc)
        return event


def instrument(orchestrator: Any) -> InstrumentedEventBus:
    """
    Sostituisce il bus di un orchestratore con quello strumentato,
    preservando le sottoscrizioni gia' registrate (compreso il wildcard che
    scrive in working_memory). Idempotente.
    """
    corrente = getattr(orchestrator, "event_bus", None)
    if isinstance(corrente, InstrumentedEventBus):
        return corrente

    nuovo = InstrumentedEventBus()
    if corrente is not None:
        nuovo.subscribers = dict(getattr(corrente, "subscribers", {}) or {})
        nuovo.event_log = list(getattr(corrente, "event_log", []) or [])
    orchestrator.event_bus = nuovo
    return nuovo
