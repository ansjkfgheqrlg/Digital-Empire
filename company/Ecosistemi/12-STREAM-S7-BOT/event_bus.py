import uuid
import time
import datetime
from collections import deque
from typing import Callable, Dict, List, Any, Optional

# =============================================================================
# EVENT CATALOG — ogni evento del sistema, con priorità e garanzia di consegna.
# Un evento non presente qui viene accettato lo stesso, ma con default P2 /
# AT_LEAST_ONCE e viene contato come "non catalogato" nelle statistiche.
# =============================================================================

P0, P1, P2, P3 = "P0", "P1", "P2", "P3"
AT_LEAST_ONCE = "AT_LEAST_ONCE"
EXACTLY_ONCE = "EXACTLY_ONCE"

EVENT_CATALOG: Dict[str, Dict[str, str]] = {
    # --- TASK LIFECYCLE ---
    "task.created":    {"priority": P2, "delivery": AT_LEAST_ONCE, "publisher": "Orchestrator"},
    "task.decomposed": {"priority": P2, "delivery": EXACTLY_ONCE,  "publisher": "Planner"},
    "task.completed":  {"priority": P1, "delivery": EXACTLY_ONCE,  "publisher": "Any agent"},
    "task.failed":     {"priority": P0, "delivery": AT_LEAST_ONCE, "publisher": "Any agent"},
    "task.escalated":  {"priority": P0, "delivery": AT_LEAST_ONCE, "publisher": "Orchestrator"},

    # --- QUALITY CONTROL ---
    "gate.check.requested": {"priority": P1, "delivery": EXACTLY_ONCE,  "publisher": "Orchestrator"},
    "gate.passed":          {"priority": P1, "delivery": EXACTLY_ONCE,  "publisher": "Gate Agent"},
    "gate.failed":          {"priority": P1, "delivery": AT_LEAST_ONCE, "publisher": "Gate Agent"},
    "gate.escalated":       {"priority": P0, "delivery": AT_LEAST_ONCE, "publisher": "Gate Agent"},

    # --- MEMORY ---
    "memory.updated":               {"priority": P2, "delivery": AT_LEAST_ONCE, "publisher": "Memory Interface"},
    "memory.pattern.detected":      {"priority": P3, "delivery": AT_LEAST_ONCE, "publisher": "Meta-Agent"},
    "memory.compression.triggered": {"priority": P3, "delivery": AT_LEAST_ONCE, "publisher": "Memory Interface"},

    # --- AGENT LIFECYCLE ---
    "agent.spawned":         {"priority": P3, "delivery": AT_LEAST_ONCE, "publisher": "Meta-Agent"},
    "agent.health.degraded": {"priority": P0, "delivery": AT_LEAST_ONCE, "publisher": "Meta-Agent"},
    "agent.replaced":        {"priority": P1, "delivery": AT_LEAST_ONCE, "publisher": "Orchestrator"},

    # --- DOMINIO S7 (bot di trading) ---
    "data.raw_event_received":  {"priority": P2, "delivery": AT_LEAST_ONCE, "publisher": "Data Manager"},
    "analysis.signal_detected": {"priority": P1, "delivery": EXACTLY_ONCE,  "publisher": "Analysis Engine"},
    "trade.executed":           {"priority": P1, "delivery": EXACTLY_ONCE,  "publisher": "Execution Engine"},
    "trade.failed":             {"priority": P0, "delivery": AT_LEAST_ONCE, "publisher": "Execution Engine"},
}

# Retry policy per priorità: secondi tra i tentativi, tentativi massimi, azione finale
RETRY_POLICY: Dict[str, Dict[str, Any]] = {
    P0: {"delay_s": 1,  "max_retries": 10, "on_exhausted": "ALERT"},
    P1: {"delay_s": 5,  "max_retries": 5,  "on_exhausted": "DLQ"},
    P2: {"delay_s": 30, "max_retries": 3,  "on_exhausted": "DLQ"},
    P3: {"delay_s": 60, "max_retries": 1,  "on_exhausted": "DROP"},
}

PRIORITY_ORDER = [P0, P1, P2, P3]


class EventBus:
    """
    ⚡ EVENT BUS — APEX-7 Core Communication Layer (Level 2)
    "Nessun agente chiama un altro direttamente"

    Cosa cambia rispetto al Level 1 (consegna sincrona, zero priorità, zero retry):
      - 4 code di priorità P0→P3, drenate in ordine di severità
      - retry per singolo subscriber, con policy legata alla priorità
      - Dead Letter Queue per gli eventi che non arrivano mai
      - garanzia EXACTLY_ONCE tramite deduplica (event_id, subscriber)
      - replay dello storico per ricostruire lo stato di un agente
    """

    def __init__(self, realtime_retries: bool = False):
        # Mappa: event_type -> [(subscriber_id, callback)]
        self.subscribers: Dict[str, List[tuple]] = {}
        # Storico completo degli eventi pubblicati (fonte di verità per il replay)
        self.event_log: List[Dict[str, Any]] = []
        # Code di consegna, una per priorità
        self.queues: Dict[str, deque] = {p: deque() for p in PRIORITY_ORDER}
        # Eventi mai consegnati dopo l'esaurimento dei retry
        self.dead_letter_queue: List[Dict[str, Any]] = []
        # (event_id, subscriber_id) già consegnati — serve a EXACTLY_ONCE
        self._delivered: set = set()
        # Guardia di rientranza: una publish annidata accoda e basta, non drena
        self._draining = False
        # True = rispetta i delay reali della retry policy (produzione)
        # False = retry immediati (test e simulazioni)
        self.realtime_retries = realtime_retries
        self.stats = {
            "published": 0,
            "delivered": 0,
            "retried": 0,
            "dead_lettered": 0,
            "dropped": 0,
            "duplicates_suppressed": 0,
            "uncatalogued": 0,
        }
        self.alerts: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------ #
    # Sottoscrizione
    # ------------------------------------------------------------------ #

    def subscribe(self, event_type: str, callback: Callable, subscriber_id: Optional[str] = None) -> str:
        """
        Un agente si iscrive per ascoltare un tipo di evento.
        subscriber_id serve alla deduplica EXACTLY_ONCE; se omesso viene
        derivato dall'agente proprietario della callback.
        """
        if subscriber_id is None:
            owner = getattr(callback, "__self__", None)
            if owner is not None:
                owner_id = getattr(owner, "agent_id", None) or type(owner).__name__
            else:
                owner_id = "anon"
            subscriber_id = f"{owner_id}.{getattr(callback, '__name__', 'cb')}"

        self.subscribers.setdefault(event_type, []).append((subscriber_id, callback))
        return subscriber_id

    def unsubscribe(self, event_type: str, subscriber_id: str):
        if event_type in self.subscribers:
            self.subscribers[event_type] = [
                (sid, cb) for sid, cb in self.subscribers[event_type] if sid != subscriber_id
            ]

    # ------------------------------------------------------------------ #
    # Pubblicazione
    # ------------------------------------------------------------------ #

    def publish(self, event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Un agente pubblica un evento sulla bacheca. Non sa chi lo riceverà.
        L'evento entra nella coda della sua priorità e il drenaggio parte subito,
        se non è già in corso: una publish annidata si limita ad accodare, così
        un P0 emesso durante la gestione di un P3 viene comunque servito prima.
        """
        spec = EVENT_CATALOG.get(event_type)
        if spec is None:
            spec = {"priority": P2, "delivery": AT_LEAST_ONCE, "publisher": "unknown"}
            self.stats["uncatalogued"] += 1

        event = {
            "event_id": f"EVT-{uuid.uuid4().hex[:8].upper()}",
            "event_type": event_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "priority": spec["priority"],
            "delivery": spec["delivery"],
            "payload": payload,
            "sequence": len(self.event_log),
        }

        self.event_log.append(event)
        self.stats["published"] += 1
        self.queues[spec["priority"]].append(event)

        if not self._draining:
            self.drain()

        return event

    # ------------------------------------------------------------------ #
    # Drenaggio e consegna
    # ------------------------------------------------------------------ #

    def drain(self, max_events: int = 10000) -> int:
        """
        Svuota le code rispettando l'ordine di priorità: finché c'è un P0 in
        attesa nessun P1 viene servito. Dentro la stessa priorità vale il FIFO.
        """
        self._draining = True
        processed = 0
        try:
            while processed < max_events:
                event = self._next_event()
                if event is None:
                    break
                self._deliver(event)
                processed += 1
        finally:
            self._draining = False
        return processed

    def _next_event(self) -> Optional[Dict[str, Any]]:
        for p in PRIORITY_ORDER:
            if self.queues[p]:
                return self.queues[p].popleft()
        return None

    def _deliver(self, event: Dict[str, Any]):
        subscribers = self.subscribers.get(event["event_type"], [])

        for subscriber_id, callback in subscribers:
            key = (event["event_id"], subscriber_id)

            if event["delivery"] == EXACTLY_ONCE and key in self._delivered:
                self.stats["duplicates_suppressed"] += 1
                continue

            if self._deliver_with_retry(event, subscriber_id, callback):
                self._delivered.add(key)

    def _deliver_with_retry(self, event: Dict[str, Any], subscriber_id: str, callback: Callable) -> bool:
        """
        Consegna a un singolo subscriber applicando la retry policy della
        priorità dell'evento. Ritorna True se la consegna è riuscita.
        """
        policy = RETRY_POLICY[event["priority"]]
        attempts = 0
        last_error = None

        while attempts <= policy["max_retries"]:
            try:
                callback(event)
                self.stats["delivered"] += 1
                if attempts > 0:
                    self.stats["retried"] += attempts
                return True
            except Exception as e:
                attempts += 1
                last_error = f"{type(e).__name__}: {e}"
                if attempts <= policy["max_retries"] and self.realtime_retries:
                    time.sleep(policy["delay_s"])

        # Retry esauriti: applica l'azione finale prevista dalla policy
        self.stats["retried"] += attempts
        failure = {
            "event": event,
            "subscriber_id": subscriber_id,
            "attempts": attempts,
            "last_error": last_error,
            "failed_at": datetime.datetime.now().isoformat(),
            "action": policy["on_exhausted"],
        }

        if policy["on_exhausted"] == "DROP":
            self.stats["dropped"] += 1
        else:
            self.dead_letter_queue.append(failure)
            self.stats["dead_lettered"] += 1
            if policy["on_exhausted"] == "ALERT":
                self.alerts.append(failure)
                print(f"[EVENT BUS ALERT] {event['event_type']} non consegnato a "
                      f"{subscriber_id} dopo {attempts} tentativi: {last_error}")

        return False

    # ------------------------------------------------------------------ #
    # Ispezione, replay, manutenzione
    # ------------------------------------------------------------------ #

    def get_history(self, event_type: str = None) -> List[Dict[str, Any]]:
        """Permette al Meta-Agent di leggere lo storico della bacheca."""
        if event_type:
            return [e for e in self.event_log if e["event_type"] == event_type]
        return self.event_log

    def get_dlq(self) -> List[Dict[str, Any]]:
        """Gli eventi che non sono mai arrivati a destinazione."""
        return self.dead_letter_queue

    def replay(self, from_sequence: int = 0, event_types: List[str] = None) -> int:
        """
        Riconsegna gli eventi dallo storico. Serve a ricostruire lo stato di un
        agente appena sostituito o a rieseguire una sessione in debug.
        La deduplica EXACTLY_ONCE viene azzerata per gli eventi replayati,
        altrimenti nessuno di essi verrebbe riconsegnato.
        """
        to_replay = [e for e in self.event_log if e["sequence"] >= from_sequence]
        if event_types:
            to_replay = [e for e in to_replay if e["event_type"] in event_types]

        for e in to_replay:
            for subscriber_id, _ in self.subscribers.get(e["event_type"], []):
                self._delivered.discard((e["event_id"], subscriber_id))

        for e in to_replay:
            self._deliver(e)

        return len(to_replay)

    def retry_dlq(self) -> int:
        """Ritenta la consegna di tutto ciò che è finito in Dead Letter Queue."""
        pending, self.dead_letter_queue = self.dead_letter_queue, []
        recovered = 0
        for failure in pending:
            event = failure["event"]
            subscriber_id = failure["subscriber_id"]
            callback = next(
                (cb for sid, cb in self.subscribers.get(event["event_type"], []) if sid == subscriber_id),
                None,
            )
            if callback and self._deliver_with_retry(event, subscriber_id, callback):
                recovered += 1
                self.stats["dead_lettered"] -= 1
        return recovered

    def get_stats(self) -> Dict[str, Any]:
        return {
            **self.stats,
            "queued": {p: len(q) for p, q in self.queues.items()},
            "subscribers": {t: len(s) for t, s in self.subscribers.items()},
            "dlq_size": len(self.dead_letter_queue),
            "alerts": len(self.alerts),
        }


# Istanza globale dell'Event Bus (Singleton per tutto il sistema)
global_bus = EventBus()
