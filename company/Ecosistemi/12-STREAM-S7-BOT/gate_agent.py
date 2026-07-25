import os
import time
import datetime
from typing import Dict, Any, List, Optional

from event_bus import global_bus
from memory_interface import global_memory
from quality_gates import (
    MAX_ATTEMPTS_BEFORE_ESCALATION,
    get_gate,
    get_gate_criteria,
    get_threshold,
    resolve_gate_id,
)
from gate_verifiers import VERIFIERS

# Transizioni ammesse. Uno stato non elencato qui non e' raggiungibile:
# la macchina a stati e' un vincolo, non un disegno sulla lavagna.
STATE_TRANSITIONS: Dict[str, List[str]] = {
    "IDLE":        ["LOADING"],
    "LOADING":     ["CHECKING", "REPORTING"],
    "CHECKING":    ["PASSED", "FAILED"],
    "PASSED":      ["REPORTING"],
    "FAILED":      ["REMEDIATING", "ESCALATING"],
    "REMEDIATING": ["REPORTING"],
    "ESCALATING":  ["REPORTING"],
    "REPORTING":   ["IDLE"],
}


class GateAgent:
    """
    🔍 GATE AGENT (GATE-1) — Quality Checkpoint Executor
    "Io non creo. Io giudico. Senza pieta'."

    Bias pessimista costruttivo: il dubbio vale FAIL, mai PARTIAL. Ogni PASS
    porta l'evidenza che lo giustifica, ogni FAIL porta il correttivo esatto.
    Ha l'autorita' di bloccare qualunque avanzamento e risponde solo al
    Meta-Agent e alla Memoria.

    Nel Level 1 diceva PASS quando l'output non era vuoto. Adesso ogni criterio
    viene misurato con la sua rubrica: dove si puo' controllare eseguendo, si
    controlla eseguendo (vedi gate_verifiers).
    """

    def __init__(self, agent_id: str = "GATE-1", src_dir: Optional[str] = None):
        self.agent_id = agent_id
        self.state = "IDLE"
        self.src_dir = src_dir or os.path.dirname(os.path.abspath(__file__))
        # Quante volte ogni gate e' stato bocciato di fila
        self.attempts: Dict[str, int] = {}
        self.state_history: List[Dict[str, str]] = []

        global_bus.subscribe("gate.check.requested", self.handle_check_requested, subscriber_id=f"{agent_id}.check")

    # ------------------------------------------------------------------ #
    # Macchina a stati
    # ------------------------------------------------------------------ #

    def _transition(self, new_state: str):
        allowed = STATE_TRANSITIONS.get(self.state, [])
        if new_state not in allowed:
            raise RuntimeError(
                f"[{self.agent_id}] Transizione illegale {self.state} -> {new_state}. Ammesse: {allowed}"
            )
        self.state_history.append({
            "from": self.state, "to": new_state,
            "at": datetime.datetime.now().isoformat(),
        })
        self.state = new_state

    def reset(self):
        """Riporta l'ispettore a riposo qualunque sia lo stato in cui si e' inceppato."""
        self.state = "IDLE"

    # ------------------------------------------------------------------ #
    # Ingresso dall'Event Bus
    # ------------------------------------------------------------------ #

    def handle_check_requested(self, event: Dict[str, Any]):
        payload = event.get("payload", {})
        raw_gate_id = payload.get("gate_id", "")
        formal_gate_id = resolve_gate_id(raw_gate_id)

        # STEP 1 — LOAD CONTEXT
        self._transition("LOADING")
        gate_def = get_gate(formal_gate_id)
        criteria = payload.get("criteria") or get_gate_criteria(formal_gate_id)
        threshold = payload.get("threshold") or get_threshold(formal_gate_id)
        timeout_s = gate_def.get("timeout_s", 60)
        gate_history = self._load_gate_history()
        attempt = self.attempts.get(raw_gate_id, 0) + 1

        print(f"[{self.agent_id}] Ispezione {raw_gate_id} ({formal_gate_id}), "
              f"tentativo {attempt}, {len(criteria)} criteri, soglia {threshold:.0%}")

        report = self.evaluate(
            gate_id=raw_gate_id,
            formal_gate_id=formal_gate_id,
            criteria=criteria,
            output_to_check=payload.get("output_to_check"),
            threshold=threshold,
            timeout_s=timeout_s,
            gate_history=gate_history,
            attempt=attempt,
        )

        # STEP 4 — ESITO E ROUTING
        if report["result"] == "PASSED":
            self.attempts[raw_gate_id] = 0
            self._transition("REPORTING")
            global_bus.publish("gate.passed", report)
        else:
            self.attempts[raw_gate_id] = attempt
            if attempt >= MAX_ATTEMPTS_BEFORE_ESCALATION:
                self._transition("ESCALATING")
                report["next_action"] = "ESCALATE"
                report["escalation_analysis"] = self._diagnose(report, gate_history)
                self._transition("REPORTING")
                global_bus.publish("gate.escalated", report)
            else:
                self._transition("REMEDIATING")
                report["next_action"] = "REMEDIATE"
                self._transition("REPORTING")
                global_bus.publish("gate.failed", report)

        global_memory.write("gate_reports", report, self.agent_id, importance=0.9)
        self._transition("IDLE")

    # ------------------------------------------------------------------ #
    # Valutazione
    # ------------------------------------------------------------------ #

    def evaluate(self, gate_id: str, formal_gate_id: str, criteria: List[Dict[str, Any]],
                 output_to_check: Any, threshold: float, timeout_s: int,
                 gate_history: List[Dict[str, Any]], attempt: int = 1) -> Dict[str, Any]:
        """
        STEP 2 e 3 dell'algoritmo: valuta ogni criterio con la sua rubrica,
        poi aggrega. Se l'ispezione sfora il timeout del gate, quello che manca
        vale FAIL: un controllo che non finisce non e' un controllo superato.
        """
        self._transition("CHECKING")
        started = time.time()

        ctx = {
            "output": output_to_check,
            "src_dir": self.src_dir,
            "bus": global_bus,
            "memory": global_memory,
            "gate_history": gate_history,
            "gate_id": formal_gate_id,
        }

        criteria_results = []
        score = 0.0
        timed_out = False

        for c in criteria:
            elapsed = time.time() - started
            if elapsed > timeout_s:
                timed_out = True
                criteria_results.append({
                    "criterion": c.get("id", "?"),
                    "name": c.get("name", ""),
                    "status": "FAIL",
                    "evidence": f"Ispezione interrotta: superato il timeout di {timeout_s}s",
                    "fix": "Ridurre il costo del controllo o alzare il timeout del gate",
                    "confidence": 1.0,
                })
                continue

            status, evidence, fix = self._evaluate_criterion(c, ctx)
            criteria_results.append({
                "criterion": c.get("id", "?"),
                "name": c.get("name", ""),
                "status": status,
                "evidence": evidence,
                "fix": fix,
                "confidence": 0.95 if status != "PARTIAL" else 0.70,
            })
            score += 1.0 if status == "PASS" else (0.5 if status == "PARTIAL" else 0.0)

        total = len(criteria) if criteria else 1
        final_score = score / total
        result = "PASSED" if (final_score >= threshold and not timed_out) else "FAILED"

        self._transition("PASSED" if result == "PASSED" else "FAILED")

        return {
            "gate_id": gate_id,
            "formal_gate_id": formal_gate_id,
            "gate_name": get_gate(formal_gate_id).get("name", ""),
            "timestamp": datetime.datetime.now().isoformat(),
            "gate_agent": self.agent_id,
            "result": result,
            "score": round(final_score, 3),
            "threshold": threshold,
            "criteria_passed": sum(1 for r in criteria_results if r["status"] == "PASS"),
            "criteria_total": total,
            "duration_ms": int((time.time() - started) * 1000),
            "timed_out": timed_out,
            "criteria_results": criteria_results,
            "remediation_suggestions": [r["fix"] for r in criteria_results if r["fix"]],
            "attempt_number": attempt,
            "next_action": "PROCEED" if result == "PASSED" else "REMEDIATE",
        }

    def _evaluate_criterion(self, criterion: Dict[str, Any], ctx: Dict[str, Any]):
        """
        Applica la rubrica di un singolo criterio.
        Regola ferrea: il dubbio vale FAIL. Se la rubrica manca, il criterio non
        e' misurabile e quindi non e' superato — non si timbra cio' che non si sa.
        """
        rubric = criterion.get("rubric")
        if not rubric:
            return ("FAIL",
                    "Criterio senza rubrica: non e' misurabile, quindi non e' dimostrato",
                    "Definire la rubrica del criterio in quality_gates.py")

        # Il controllo eseguibile vince su tutto il resto
        verifier_name = rubric.get("verify")
        if verifier_name:
            fn = VERIFIERS.get(verifier_name)
            if fn is None:
                return ("FAIL", f"Verificatore '{verifier_name}' non trovato",
                        f"Implementare {verifier_name}() in gate_verifiers.py")
            try:
                return fn(ctx)
            except Exception as e:
                return ("FAIL", f"Il verificatore '{verifier_name}' e' esploso: {type(e).__name__}: {e}",
                        "Correggere il verificatore: un controllo rotto non puo' approvare nulla")

        text = str(ctx.get("output", "")).lower()
        if not text:
            return ("FAIL", "Nessun output da esaminare", "Fornire l'artefatto da valutare")

        missing = [t for t in rubric.get("must_contain", []) if t.lower() not in text]
        if missing:
            return ("FAIL", f"Termini obbligatori assenti nell'output: {missing}",
                    f"L'artefatto deve trattare esplicitamente: {', '.join(missing)}")

        any_of = rubric.get("any_of", [])
        if any_of and not any(t.lower() in text for t in any_of):
            return ("FAIL", f"Nessuno dei termini attesi presente: {any_of}",
                    f"Coprire almeno uno tra: {', '.join(any_of)}")

        forbidden = [t for t in rubric.get("must_not_contain", []) if t.lower() in text]
        if forbidden:
            return ("FAIL", f"Presenti indizi di lavoro non finito: {forbidden}",
                    f"Rimuovere o completare: {', '.join(forbidden)}")

        for term, minimum in rubric.get("min_occurrences", {}).items():
            found = text.count(term.lower())
            if found < minimum:
                return ("FAIL", f"'{term}' compare {found} volte, ne servono {minimum}",
                        f"Portare '{term}' ad almeno {minimum} occorrenze reali")

        min_length = rubric.get("min_length")
        if min_length and len(text) < min_length:
            return ("PARTIAL", f"Output di {len(text)} caratteri, sotto i {min_length} attesi",
                    "Approfondire: l'artefatto e' troppo scarno per essere valutato")

        return ("PASS", f"Rubrica soddisfatta su un output di {len(text)} caratteri", None)

    # ------------------------------------------------------------------ #
    # Storico e diagnosi
    # ------------------------------------------------------------------ #

    def _load_gate_history(self) -> List[Dict[str, Any]]:
        """Quante volte questo gate e' stato superato o bocciato in passato."""
        return [r["content"] for r in global_memory.storage.get("gate_reports", [])
                if isinstance(r.get("content"), dict)]

    def _diagnose(self, report: Dict[str, Any], gate_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Cosa dire al Meta-Agent quando si escala: non "ha fallito", ma quale
        criterio fallisce sempre e cosa e' gia' stato provato senza risultato.
        """
        failing = [r for r in report["criteria_results"] if r["status"] == "FAIL"]
        same_gate = [h for h in gate_history if h.get("gate_id") == report["gate_id"]]

        recurring: Dict[str, int] = {}
        for h in same_gate:
            for cr in h.get("criteria_results", []):
                if cr.get("status") == "FAIL":
                    recurring[cr.get("criterion", "?")] = recurring.get(cr.get("criterion", "?"), 0) + 1

        root = max(recurring.items(), key=lambda kv: kv[1])[0] if recurring else (
            failing[0]["criterion"] if failing else "sconosciuto")

        return {
            "root_cause_criterion": root,
            "times_this_criterion_failed": recurring.get(root, 1),
            "still_failing": [f["criterion"] for f in failing],
            "already_attempted": len(same_gate),
            "recommended_strategy_change": (
                f"Il criterio {root} non passa da {recurring.get(root, 1)} tentativi: "
                f"il problema non e' l'esecuzione ma l'approccio. Cambiare strategia, non riprovare."
            ),
        }


# Istanza globale dell'ispettore
gate_1 = GateAgent("GATE-1")
