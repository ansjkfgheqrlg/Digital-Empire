"""
RUFLO ADAPTER — il ponte tra apex7_workflow.ruflo.yaml e il sistema vivo.

RuFLO era citato come "integrato" senza esserlo. Qui l'integrazione e' una
cosa sola: una configurazione, due esecutori.

  - se il runtime RuFLO e' installato, il grafo viene consegnato a lui
  - se non lo e', lo stesso grafo gira sull'Event Bus interno

In entrambi i casi la fonte di verita' e' il file yaml: agenti, timeout,
permessi di memoria, soglie dei gate e retry policy si cambiano li' dentro,
non sparsi nel codice.
"""

import os
from typing import Dict, Any, List, Optional

import yaml

from event_bus import global_bus, RETRY_POLICY, EVENT_CATALOG
from memory_interface import global_memory
from quality_gates import GATE_DEFINITIONS

CONFIG_FILE = "apex7_workflow.ruflo.yaml"

# Le primitive RuFLO che il sistema si aspetta di trovare quando il runtime
# reale e' presente. Servono anche a verificare che la mappatura sia completa.
RUFLO_PRIMITIVES = [
    "ruflo.WorkflowEngine",
    "ruflo.AgentRuntime",
    "ruflo.TaskGraph",
    "ruflo.Router",
    "ruflo.PluginSystem",
]


class RufloAdapter:
    """
    ⚡ RUFLO INTEGRATION — configurazione unica, esecutore intercambiabile.

    Carica il workflow dichiarato nello yaml, verifica che combaci con quello
    che il codice fa davvero (soglie, retry, tetti) e lo esegue: su RuFLO se
    c'e', sull'Event Bus interno altrimenti.
    """

    def __init__(self, config_path: Optional[str] = None):
        base = os.path.dirname(os.path.abspath(__file__))
        self.config_path = config_path or os.path.join(base, CONFIG_FILE)
        self.config: Dict[str, Any] = {}
        self.backend = "internal"
        self.load()
        self._detect_backend()

    # ------------------------------------------------------------------ #
    # Caricamento
    # ------------------------------------------------------------------ #

    def load(self) -> Dict[str, Any]:
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        return self.config

    def _detect_backend(self):
        try:
            import ruflo  # noqa: F401
            self.backend = "ruflo"
        except ImportError:
            self.backend = "internal"

    # ------------------------------------------------------------------ #
    # Coerenza tra dichiarato ed eseguito
    # ------------------------------------------------------------------ #

    def validate(self) -> Dict[str, Any]:
        """
        Controlla che lo yaml e il codice raccontino la stessa storia.
        Una configurazione che diverge dal comportamento reale e' peggio di
        nessuna configurazione: da' l'illusione del controllo.
        """
        problems: List[str] = []

        # 1. Le primitive RuFLO devono essere tutte mappate
        mapped = {m["ruflo"] for m in self.config.get("mapping", [])}
        for primitive in RUFLO_PRIMITIVES:
            if primitive not in mapped:
                problems.append(f"Primitiva {primitive} non mappata su nessun componente APEX-7")

        # 2. Le soglie dei gate devono coincidere con quality_gates.py
        for rule in self.config.get("routing", {}).get("rules", []):
            gate = GATE_DEFINITIONS.get(rule["gate"])
            if gate is None:
                problems.append(f"Il routing cita il gate {rule['gate']} che non esiste")
                continue
            if abs(gate["threshold"] - float(rule["threshold"])) > 0.01:
                problems.append(
                    f"Soglia divergente su {rule['gate']}: yaml {rule['threshold']} "
                    f"vs codice {gate['threshold']}"
                )

        # 3. La retry policy dichiarata deve essere quella applicata
        for prio, declared in self.config.get("event_bus", {}).get("retry_policy", {}).items():
            actual = RETRY_POLICY.get(prio)
            if actual is None:
                problems.append(f"Priorita' {prio} dichiarata nello yaml ma assente nel bus")
                continue
            if actual["max_retries"] != declared["max_retries"]:
                problems.append(
                    f"Retry divergenti su {prio}: yaml {declared['max_retries']} "
                    f"vs bus {actual['max_retries']}"
                )

        # 4. Ogni evento dichiarato dagli agenti deve stare nel catalogo
        for name, agent in self.config.get("agents", {}).items():
            for evt in agent.get("subscribes", []) + agent.get("publishes", []):
                if evt not in EVENT_CATALOG:
                    problems.append(f"L'agente {name} usa l'evento non catalogato '{evt}'")

        # 5. I layer di memoria dichiarati devono esistere
        for layer in self.config.get("memory", {}).get("layers", []):
            if layer not in global_memory.storage:
                problems.append(f"Layer di memoria '{layer}' dichiarato ma non creato")

        return {
            "valid": not problems,
            "backend": self.backend,
            "problems": problems,
            "agents_declared": len(self.config.get("agents", {})),
            "routing_rules": len(self.config.get("routing", {}).get("rules", [])),
        }

    # ------------------------------------------------------------------ #
    # Interrogazione della configurazione
    # ------------------------------------------------------------------ #

    def agent_config(self, agent_name: str) -> Dict[str, Any]:
        return self.config.get("agents", {}).get(agent_name, {})

    def memory_permissions(self, agent_name: str) -> List[str]:
        """Cosa quell'agente ha il diritto di leggere e scrivere."""
        return self.agent_config(agent_name).get("memory_access", [])

    def can_write(self, agent_name: str, layer: str) -> bool:
        perms = self.memory_permissions(agent_name)
        if "WRITE_ALL" in perms:
            return True
        return f"WRITE_{layer.upper().rstrip('S')}" in perms or f"WRITE_{layer.upper()}" in perms

    def timeout_ms(self, agent_name: str) -> int:
        return self.agent_config(agent_name).get("timeout_ms", 30000)

    def prompt_template(self, agent_name: str) -> Optional[str]:
        """Il prompt interno dell'agente: il suo comportamento, non il suo nome."""
        rel = self.agent_config(agent_name).get("prompt_template")
        if not rel:
            return None
        path = os.path.join(os.path.dirname(self.config_path), rel)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def parallel_group(self, agent_name: str) -> List[str]:
        return self.agent_config(agent_name).get("parallel_with", [])

    def routing_rule(self, gate_id: str) -> Dict[str, Any]:
        for rule in self.config.get("routing", {}).get("rules", []):
            if rule["gate"] == gate_id:
                return rule
        return {}

    # ------------------------------------------------------------------ #
    # Esecuzione
    # ------------------------------------------------------------------ #

    def build_task_graph(self) -> Dict[str, Any]:
        """
        Costruisce il grafo dei task dalla configurazione: chi ascolta cosa,
        chi puo' girare in parallelo con chi. Su RuFLO diventa un TaskGraph,
        internamente resta una mappa di sottoscrizioni sull'Event Bus.
        """
        graph = {"nodes": [], "edges": [], "parallel_groups": []}
        agents = self.config.get("agents", {})

        for name, cfg in agents.items():
            graph["nodes"].append({
                "id": name,
                "runtime": cfg.get("runtime", "ruflo.AgentRuntime"),
                "timeout_ms": cfg.get("timeout_ms"),
                "instances": cfg.get("instances", 1),
            })
            for pub in cfg.get("publishes", []):
                for other, ocfg in agents.items():
                    if pub in ocfg.get("subscribes", []):
                        graph["edges"].append({"from": name, "to": other, "via": pub})
            if cfg.get("parallel_with"):
                group = sorted([name] + cfg["parallel_with"])
                if group not in graph["parallel_groups"]:
                    graph["parallel_groups"].append(group)

        return graph

    def execute(self, mission: str, orchestrator) -> Dict[str, Any]:
        """
        Avvia una missione con il backend disponibile. La differenza tra i due
        percorsi e' solo chi consegna gli eventi: le regole restano queste.
        """
        graph = self.build_task_graph()
        if self.backend == "ruflo":
            import ruflo
            engine = ruflo.WorkflowEngine(self.config)   # type: ignore[attr-defined]
            return {"backend": "ruflo", "run": engine.run(mission), "graph": graph}

        task_id = orchestrator.assign_mission(mission)
        return {
            "backend": "internal",
            "task_id": task_id,
            "graph_nodes": len(graph["nodes"]),
            "graph_edges": len(graph["edges"]),
            "parallel_groups": graph["parallel_groups"],
            "events_delivered": global_bus.stats["delivered"],
        }


adapter = RufloAdapter()
