import datetime
from typing import Dict, Any, List, Optional

from event_bus import global_bus
from memory_interface import global_memory

# Nessun pattern viene dichiarato sotto questo numero di osservazioni: due casi
# uguali sono una coincidenza, non una regola.
MIN_SAMPLES_FOR_PATTERN = 3
# Tetto agli agenti generabili. Senza un tetto, un sistema che puo' creare
# agenti finisce per creare solo agenti.
MAX_AGENTS = 12
# Sotto questo punteggio di salute un agente viene segnalato come degradato.
HEALTH_DEGRADED_THRESHOLD = 0.5


class MetaAgent:
    """
    👁️ META-AGENT — Il Direttore Strategico (Level 2)

    Non lavora: guarda lavorare. Tiene il registro di chi e' vivo, misura la
    salute di ciascuno, riconosce i fallimenti che si ripetono e cambia la
    strategia invece di far ripetere lo stesso tentativo.

    Puo' proporre modifiche al sistema stesso, ma nessuna proposta si applica
    da sola: passa da un Quality Gate e resta reversibile. In ogni momento
    human_override() ferma tutto.
    """

    def __init__(self, agent_id: str = "META-1"):
        self.agent_id = agent_id
        # Registro degli agenti vivi: non si sorveglia cio' che non si vede
        self.registry: Dict[str, Dict[str, Any]] = {}
        self.frozen = False
        self.freeze_reason: Optional[str] = None
        self.evolution_proposals: List[Dict[str, Any]] = []
        self.detected_patterns: List[Dict[str, Any]] = []

        global_bus.subscribe("task.escalated", self.handle_escalation, subscriber_id=f"{agent_id}.escalation")
        global_bus.subscribe("gate.escalated", self.handle_gate_escalated, subscriber_id=f"{agent_id}.gate_esc")
        global_bus.subscribe("task.completed", self.observe_completion, subscriber_id=f"{agent_id}.completion")
        global_bus.subscribe("task.failed", self.observe_failure, subscriber_id=f"{agent_id}.failure")
        global_bus.subscribe("agent.spawned", self.observe_spawn, subscriber_id=f"{agent_id}.spawn")

    # ------------------------------------------------------------------ #
    # Registro e salute degli agenti
    # ------------------------------------------------------------------ #

    def register_agent(self, agent_id: str, kind: str, specialization: str = "") -> bool:
        """
        Iscrive un agente al registro. Rifiuta oltre MAX_AGENTS: il limite serve
        proprio nel momento in cui il sistema avrebbe voglia di superarlo.
        """
        if len(self.registry) >= MAX_AGENTS:
            print(f"[{self.agent_id}] Registrazione di {agent_id} RIFIUTATA: "
                  f"raggiunto il tetto di {MAX_AGENTS} agenti.")
            return False
        self.registry[agent_id] = {
            "kind": kind,
            "specialization": specialization,
            "registered_at": datetime.datetime.now().isoformat(),
            "tasks_completed": 0,
            "tasks_failed": 0,
            "health_score": 1.0,
            "status": "ACTIVE",
        }
        return True

    def spawn_agent(self, agent_id: str, kind: str, reason: str, parent: str = None) -> bool:
        """Genera un agente nuovo, se il tetto lo consente."""
        if len(self.registry) >= MAX_AGENTS:
            print(f"[{self.agent_id}] Spawn di {agent_id} NEGATO: {len(self.registry)}/{MAX_AGENTS} agenti attivi.")
            return False
        if not self.register_agent(agent_id, kind):
            return False
        global_bus.publish("agent.spawned", {
            "agent_id": agent_id, "type": kind, "parent_agent": parent, "reason": reason,
        })
        return True

    def observe_spawn(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        aid = payload.get("agent_id")
        if aid and aid not in self.registry:
            self.register_agent(aid, payload.get("type", "unknown"))

    def observe_completion(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        aid = payload.get("agent_id")
        if aid:
            entry = self.registry.setdefault(aid, self._blank_entry("worker"))
            entry["tasks_completed"] += 1
            self._recompute_health(aid)

    def observe_failure(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        aid = payload.get("agent_id")
        if aid:
            entry = self.registry.setdefault(aid, self._blank_entry("worker"))
            entry["tasks_failed"] += 1
            self._recompute_health(aid)
        self._detect_patterns()

    def _blank_entry(self, kind: str) -> Dict[str, Any]:
        return {
            "kind": kind, "specialization": "",
            "registered_at": datetime.datetime.now().isoformat(),
            "tasks_completed": 0, "tasks_failed": 0,
            "health_score": 1.0, "status": "ACTIVE",
        }

    def _recompute_health(self, agent_id: str):
        e = self.registry[agent_id]
        total = e["tasks_completed"] + e["tasks_failed"]
        e["health_score"] = e["tasks_completed"] / total if total else 1.0
        if e["health_score"] < HEALTH_DEGRADED_THRESHOLD and total >= MIN_SAMPLES_FOR_PATTERN:
            e["status"] = "DEGRADED"
            global_bus.publish("agent.health.degraded", {
                "agent_id": agent_id,
                "health_score": round(e["health_score"], 2),
                "symptoms": [f"{e['tasks_failed']} fallimenti su {total} task"],
            })

    # ------------------------------------------------------------------ #
    # Riconoscimento dei pattern
    # ------------------------------------------------------------------ #

    def _detect_patterns(self):
        """
        Cerca fallimenti che si ripetono. Sotto MIN_SAMPLES_FOR_PATTERN non
        dichiara nulla: meglio nessun pattern che un pattern inventato.
        """
        failures = global_bus.get_history("task.failed") + global_bus.get_history("gate.failed")
        buckets: Dict[str, int] = {}
        for e in failures:
            key = e["payload"].get("error_type") or e["payload"].get("gate_id") or "generico"
            buckets[key] = buckets.get(key, 0) + 1

        for key, count in buckets.items():
            if count < MIN_SAMPLES_FOR_PATTERN:
                continue
            if any(p["key"] == key and p["count"] == count for p in self.detected_patterns):
                continue
            pattern = {
                "key": key,
                "count": count,
                "confidence": round(min(0.95, count / (count + 2)), 2),
                "detected_at": datetime.datetime.now().isoformat(),
            }
            self.detected_patterns.append(pattern)
            global_memory.write("patterns", pattern, self.agent_id, importance=0.8)
            global_bus.publish("memory.pattern.detected", {
                "pattern_type": key, "confidence": pattern["confidence"],
                "evidence": [f"{count} occorrenze osservate sul bus"],
            })

    # ------------------------------------------------------------------ #
    # Escalation: diagnosi e cambio di strategia
    # ------------------------------------------------------------------ #

    def handle_escalation(self, event: Dict[str, Any]):
        """Interviene quando il sistema si blocca: diagnosi, poi strategia nuova."""
        payload = event.get("payload", {})
        task_id = payload.get("task_id")
        reason = payload.get("reason")

        print(f"[{self.agent_id}] [ALLARME] ESCALATION su {task_id}. Motivo: {reason}")

        # DIAGNOSE — cosa dice la memoria di casi simili
        past = global_memory.contextual_recall([str(task_id), "FAILED", str(reason)])
        prior = global_memory.decision_lookup(f"sbloccare {reason}")
        print(f"[{self.agent_id}] Diagnosi: {len(past)} record pertinenti, "
              f"{prior['similar_decisions_found']} decisioni simili gia' prese.")

        # STRATEGY CHANGE — quella con il miglior tasso di successo misurato
        fetched = global_memory.strategy_fetch("escalation", constraints=[])
        strategy = fetched["recommended_strategy"]
        if strategy:
            choice = strategy["name"]
            note = f"success_rate {strategy['success_rate']:.0%} su {strategy['times_used']} usi"
        else:
            choice = "Semplifica e riprova"
            note = "nessuna strategia in archivio: si applica il ripiego"
        print(f"[{self.agent_id}] STRATEGY CHANGE: '{choice}' ({note})")

        decision_id = global_memory.record_decision(
            decision=f"Intervento d'emergenza su {task_id}: applicata strategia '{choice}'",
            author=self.agent_id,
            outcome="PENDING",
            rationale=f"Escalation per: {reason}. {note}",
            alternatives=[a["name"] for a in fetched["alternatives"]],
        )

        global_memory.record_strategy_outcome(choice, success=False)

        print(f"[{self.agent_id}] [STALLO] MAX, il sistema e' fermo su {task_id}. "
              f"Decisione registrata ({decision_id}). Serve conferma umana.")

    def handle_gate_escalated(self, event: Dict[str, Any]):
        """Un gate ha bocciato tre volte di fila: il problema e' l'approccio, non l'esecuzione."""
        report = event.get("payload", {})
        analysis = report.get("escalation_analysis", {})
        print(f"[{self.agent_id}] [GATE BLOCCATO] {report.get('gate_id')} — "
              f"criterio critico: {analysis.get('root_cause_criterion')}")
        print(f"[{self.agent_id}] {analysis.get('recommended_strategy_change', '')}")

        global_memory.record_decision(
            decision=f"Cambio di approccio sul gate {report.get('gate_id')}",
            author=self.agent_id,
            outcome="PENDING",
            rationale=analysis.get("recommended_strategy_change", ""),
        )

    # ------------------------------------------------------------------ #
    # Auto-evoluzione sorvegliata
    # ------------------------------------------------------------------ #

    def propose_evolution(self, target: str, change: str, rationale: str,
                          reversible: bool = True) -> Dict[str, Any]:
        """
        Il sistema propone una modifica a se stesso. Non la applica: la mette in
        coda e la manda a un Quality Gate. Le modifiche irreversibili non
        vengono proposte affatto — quello e' territorio di Max.
        """
        proposal = {
            "proposal_id": f"EVO-{len(self.evolution_proposals) + 1:03d}",
            "target": target,
            "change": change,
            "rationale": rationale,
            "reversible": reversible,
            "status": "PROPOSED",
            "proposed_by": self.agent_id,
            "proposed_at": datetime.datetime.now().isoformat(),
        }

        if not reversible:
            proposal["status"] = "REFUSED"
            proposal["refusal_reason"] = "Modifica irreversibile: decide Max, non il sistema"
            self.evolution_proposals.append(proposal)
            print(f"[{self.agent_id}] Proposta {proposal['proposal_id']} RIFIUTATA in partenza: irreversibile.")
            return proposal

        self.evolution_proposals.append(proposal)
        global_memory.write("knowledge", proposal, self.agent_id, importance=0.85)
        global_bus.publish("gate.check.requested", {
            "gate_id": f"GATE-L5-{proposal['proposal_id']}",
            "output_to_check": f"{change}\n\nMotivazione: {rationale}",
            "level": "L5",
        })
        print(f"[{self.agent_id}] Proposta {proposal['proposal_id']} inviata al gate. "
              f"Nessuna modifica applicata finche' non passa.")
        return proposal

    # ------------------------------------------------------------------ #
    # Human override
    # ------------------------------------------------------------------ #

    def human_override(self, reason: str, operator: str = "MAX") -> Dict[str, Any]:
        """
        Ferma tutto, in qualunque stato si trovi il sistema. E' l'unica funzione
        che nessun agente puo' chiamare: la usa una persona.
        """
        self.frozen = True
        self.freeze_reason = reason
        for entry in self.registry.values():
            entry["status"] = "FROZEN"
        global_memory.record_decision(
            decision=f"HUMAN OVERRIDE da {operator}: sistema congelato",
            author=f"HUMAN:{operator}",
            outcome="APPLIED",
            rationale=reason,
        )
        print(f"[{self.agent_id}] [HUMAN OVERRIDE] di {operator}: {reason}. "
              f"{len(self.registry)} agenti congelati.")
        return {"frozen": True, "reason": reason, "agents_frozen": len(self.registry)}

    def resume(self, operator: str = "MAX") -> bool:
        self.frozen = False
        self.freeze_reason = None
        for entry in self.registry.values():
            if entry["status"] == "FROZEN":
                entry["status"] = "ACTIVE"
        print(f"[{self.agent_id}] Sistema riattivato da {operator}.")
        return True

    # ------------------------------------------------------------------ #
    # Vista d'insieme
    # ------------------------------------------------------------------ #

    def system_view(self) -> Dict[str, Any]:
        return {
            "agents": len(self.registry),
            "max_agents": MAX_AGENTS,
            "degraded": [a for a, e in self.registry.items() if e["status"] == "DEGRADED"],
            "frozen": self.frozen,
            "patterns_detected": len(self.detected_patterns),
            "evolution_proposals": len(self.evolution_proposals),
            "bus": global_bus.get_stats(),
            "memory": global_memory.get_stats(),
        }


director_meta = MetaAgent()
