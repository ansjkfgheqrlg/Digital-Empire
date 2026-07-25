# -*- coding: utf-8 -*-
"""
Owner: GAEL · Controllore: A2-QA · Origine: FORGE
Governo: APEX-7 Framework (Event Bus Architecture)
"""
from __future__ import annotations

import logging
import uuid
from datetime import datetime
from typing import Callable, Dict, List, Any, Optional

log = logging.getLogger("preventa-pw.event_bus")

class Event:
    def __init__(self, event_type: str, publisher: str, payload: Dict[str, Any], delivery_mode: str = "AT_LEAST_ONCE"):
        self.id = f"EVT-{uuid.uuid4().hex[:8].upper()}"
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.event_type = event_type
        self.publisher = publisher
        self.payload = payload
        self.delivery_mode = delivery_mode  # "AT_LEAST_ONCE" or "EXACTLY_ONCE"
        self.handled_by: List[str] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "publisher": self.publisher,
            "payload": self.payload,
            "delivery_mode": self.delivery_mode,
            "handled_by": self.handled_by
        }


class EventBus:
    _instance: Optional[EventBus] = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EventBus, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Evita di reinizializzare la struttura se la classe è singleton ed è già stata inizializzata
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._subscribers: Dict[str, List[Callable[[Event], None]]] = {}
        self._event_history: List[Event] = []
        self._processed_exactly_once: Dict[str, List[str]] = {} # subscriber_name -> list of event_ids
        self._initialized = True
        log.info("Event Bus APEX-7 inizializzato con successo.")

    def subscribe(self, event_type: str, callback: Callable[[Event], None]):
        """Registra una callback per un tipo di evento."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
        log.debug(f"Nuovo subscriber registrato per l'evento: {event_type}")

    def unsubscribe(self, event_type: str, callback: Callable[[Event], None]):
        """Rimuove una callback per un tipo di evento."""
        if event_type in self._subscribers and callback in self._subscribers[event_type]:
            self._subscribers[event_type].remove(callback)
            log.debug(f"Subscriber rimosso per l'evento: {event_type}")

    def publish(self, event_type: str, publisher: str, payload: Dict[str, Any], delivery_mode: str = "AT_LEAST_ONCE") -> Event:
        """Pubblica un evento nel bus ed esegue il dispatch ai subscriber registrati."""
        event = Event(event_type, publisher, payload, delivery_mode)
        self._event_history.append(event)
        log.info(f"🔄 [EventBus] Pubblicato {event.event_type} da {event.publisher} | ID: {event.id}")

        subscribers = self._subscribers.get(event_type, [])
        if not subscribers:
            log.warning(f"⚠️ Nessun subscriber per l'evento: {event_type}")
            return event

        for sub in subscribers:
            sub_name = getattr(sub, "__name__", str(sub))
            # Gestione EXACTLY_ONCE deduplicazione
            if delivery_mode == "EXACTLY_ONCE":
                if sub_name not in self._processed_exactly_once:
                    self._processed_exactly_once[sub_name] = []
                if event.id in self._processed_exactly_once[sub_name]:
                    log.info(f"⏭️ Evento {event.id} già processato da {sub_name} (EXACTLY_ONCE). Skip.")
                    continue
                self._processed_exactly_once[sub_name].append(event.id)

            try:
                sub(event)
                event.handled_by.append(sub_name)
                log.debug(f"   ✓ Evento {event.id} gestito da {sub_name}")
            except Exception as e:
                log.error(f"❌ Errore durante l'esecuzione del subscriber {sub_name} per l'evento {event.id}: {e}")
                # In caso di AT_LEAST_ONCE, qui si potrebbe implementare un meccanismo di retry.
                # Per ora viene loggato come errore.

        return event

    def get_history(self) -> List[Dict[str, Any]]:
        """Ritorna lo storico degli eventi serializzati in dizionario."""
        return [evt.to_dict() for evt in self._event_history]

    def clear(self):
        """Pulisce la cronologia e i sottoscrittori (usato per i test)."""
        self._subscribers.clear()
        self._event_history.clear()
        self._processed_exactly_once.clear()
        log.debug("Event Bus pulito e resettato.")
