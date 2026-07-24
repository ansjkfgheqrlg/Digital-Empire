# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Event Bus Broker (Plan 1)
"""
from __future__ import annotations

import logging
import uuid
from datetime import datetime
from typing import Callable, Dict, List, Any

log = logging.getLogger("preventa-pw.event_bus")

class Event:
    def __init__(self, event_type: str, publisher: str, payload: Dict[str, Any], delivery_mode: str = "BEST_EFFORT"):
        self.event_id = f"EVT-{uuid.uuid4().hex[:8].upper()}"
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.event_type = event_type
        self.publisher = publisher
        self.payload = payload
        self.delivery_mode = delivery_mode

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Event], None]]] = {}
        self._processed_events: set[str] = set()

    def subscribe(self, event_type: str, callback: Callable[[Event], None]):
        """Registra un callback per un determinato tipo di evento."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)

    def publish(self, event_type: str, publisher: str, payload: Dict[str, Any], delivery_mode: str = "BEST_EFFORT") -> Event:
        """Pubblica un evento a tutti i sottoscrittori registrati."""
        event = Event(event_type, publisher, payload, delivery_mode)
        log.info(f"🔄 [EventBus] Pubblicato {event_type} da {publisher} | ID: {event.event_id}")

        # Deduplica per modalità EXACTLY_ONCE
        if delivery_mode == "EXACTLY_ONCE":
            if event.event_id in self._processed_events:
                log.warning(f"⚠️ [EventBus] Evento {event.event_id} già processato. Salto.")
                return event
            self._processed_events.add(event.event_id)

        subscribers = self._subscribers.get(event_type, [])
        if not subscribers:
            log.warning(f"⚠️ Nessun subscriber per l'evento: {event_type}")

        for callback in subscribers:
            try:
                callback(event)
            except Exception as e:
                log.error(f"❌ Errore nel callback di {event_type}: {e}", exc_info=True)

        return event
