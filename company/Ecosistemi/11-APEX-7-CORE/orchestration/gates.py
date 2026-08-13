"""
APEX-7 Orchestration Layer — I 7 Quality Gate.

Ogni gate e' una funzione pura da evidenze a GateResult. Regole di casa:

  1. **Nessun punto regalato.** Ogni GateCheck nasce da un predicato su dati
     reali. Se una condizione non si applica al run corrente, il check NON
     viene emesso — non viene emesso "passato". Un gate che si auto-assegna
     credito misura se stesso, non il sistema.
  2. **Passare richiede zero fallimenti.** GateResult.build pretende soglia
     raggiunta E tutti i check verdi: nessun 6/7 spacciato per certificazione.
  3. **L7 dipende da L1..L6, tutti e sei.** Un livello non eseguito e' un
     livello fallito, non un livello assente.

Livelli:
  L1 FOUNDATION  — contratto d'ingresso e catena di stato Merkle   (1.00)
  L2 DAG         — grafo di calcolo, circuit breaker, numeri finiti (0.90)
  L3 BUS_MEMORY  — consegna eventi, DLQ, contratto memoria          (0.85)
  L4 SWARM       — ruoli registrati, handoff, tracce di esecuzione  (0.85)
  L5 QUALITY     — audit eseguiti e calibrazione degli esiti        (0.90)
  L6 EVOLUTION   — invarianti protetti, rollback sulle regressioni  (1.00)
  L7 APEX        — aggregazione, SLA, DLQ, healing, catena intatta  (1.00)
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from .contracts import GateBlocked, GateCheck, GateResult, StateSnapshot, is_finite_number, verify_chain
from .dag import NodeResult
from .evolution import EvolutionExperiment

THRESHOLDS: Dict[int, float] = {1: 1.00, 2: 0.90, 3: 0.85, 4: 0.85, 5: 0.90, 6: 1.00, 7: 1.00}
DEFAULT_SLA_MS: float = 500.0


# ─────────────────────────────────────────────────────────────────────────────
# Evidenze di qualita' (L5) — generiche, non legate a un dominio
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class AuditFinding:
    audit_id: str
    triggered: bool
    severity: str = "LOW"          # LOW | MEDIUM | HIGH | CRITICAL
    note: str = ""


@dataclass(frozen=True)
class Outcome:
    """Un esito di una distribuzione dichiarata (scenario, branch, variante)."""
    label: str
    probability_pct: float
    value: float


@dataclass(frozen=True)
class QualityReport:
    """
    Evidenza che il dominio consegna al gate L5.

    `outcomes` e' opzionale: chi non dichiara una distribuzione non viene
    misurato sulla calibrazione (i check relativi non vengono emessi). Chi la
    dichiara deve farla sommare a 100.
    """
    score: float
    threshold: float
    audits: Tuple[AuditFinding, ...] = ()
    outcomes: Tuple[Outcome, ...] = ()
    min_audits: int = 1


# ─────────────────────────────────────────────────────────────────────────────
# L1 — Fondamenta
# ─────────────────────────────────────────────────────────────────────────────

def gate_l1_foundation(
    chain: Sequence[StateSnapshot],
    payload: Mapping[str, Any],
    required_fields: Sequence[str] = (),
    numeric_fields: Sequence[str] = (),
) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []

    checks.append(GateCheck(
        "C1.1", "La catena di stato Merkle e' intatta",
        verify_chain(tuple(chain)),
        "" if verify_chain(tuple(chain)) else "hash di collegamento non corrispondenti o catena vuota",
    ))

    ha_payload = isinstance(payload, Mapping) and len(payload) > 0
    checks.append(GateCheck("C1.2", "Il payload d'ingresso e' un dizionario non vuoto", ha_payload,
                            "" if ha_payload else f"payload ricevuto: {type(payload).__name__} len={len(payload or {})}"))

    mancanti = [f for f in required_fields if f not in payload]
    if required_fields:
        checks.append(GateCheck("C1.3", "Tutti i campi obbligatori dichiarati sono presenti", not mancanti,
                                "" if not mancanti else f"campi mancanti: {mancanti}"))

    if numeric_fields:
        sporchi = [
            f"{f}={payload.get(f)!r}" for f in numeric_fields
            if f in payload and not is_finite_number(payload[f])
        ]
        checks.append(GateCheck("C1.4", "I campi numerici dichiarati sono numeri finiti", not sporchi,
                                "" if not sporchi else f"valori non numerici o non finiti: {sporchi}"))

    nulli = sorted(k for k, v in payload.items() if v is None) if isinstance(payload, Mapping) else []
    checks.append(GateCheck("C1.5", "Nessun campo d'ingresso e' None non dichiarato", not nulli,
                            "" if not nulli else f"campi a None: {nulli}"))

    return GateResult.build("GATE_L1_FOUNDATION", 1, THRESHOLDS[1], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# L2 — DAG
# ─────────────────────────────────────────────────────────────────────────────

def gate_l2_dag(
    results: Mapping[str, NodeResult],
    critical_nodes: Sequence[str] = (),
    non_finite: Sequence[str] = (),
) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []

    checks.append(GateCheck("C2.1", "Il grafo ha prodotto almeno un risultato", len(results) > 0,
                            "" if results else "nessun nodo eseguito"))

    if critical_nodes:
        assenti = [n for n in critical_nodes if n not in results]
        checks.append(GateCheck("C2.2", "Tutti i nodi critici sono presenti nel risultato", not assenti,
                                "" if not assenti else f"nodi critici assenti: {assenti}"))
        inutilizzabili = [n for n in critical_nodes if n in results and not results[n].usable]
        checks.append(GateCheck("C2.3", "Tutti i nodi critici sono utilizzabili", not inutilizzabili,
                                "" if not inutilizzabili else
                                f"nodi critici non utilizzabili: {[(n, results[n].status) for n in inutilizzabili]}"))

    falliti = [n for n, r in results.items() if r.status == "FAILED"]
    checks.append(GateCheck("C2.4", "Nessun nodo e' caduto senza fallback", not falliti,
                            "" if not falliti else f"nodi FAILED: {falliti}"))

    bloccati = [n for n, r in results.items() if r.status == "BLOCKED"]
    checks.append(GateCheck("C2.5", "Nessun nodo e' rimasto bloccato da dipendenze rotte", not bloccati,
                            "" if not bloccati else f"nodi BLOCKED: {bloccati}"))

    checks.append(GateCheck("C2.6", "Nessun output numerico e' NaN o Inf", not non_finite,
                            "" if not non_finite else f"valori non finiti: {list(non_finite)}"))

    return GateResult.build("GATE_L2_DAG", 2, THRESHOLDS[2], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# L3 — Event bus e memoria
# ─────────────────────────────────────────────────────────────────────────────

def gate_l3_bus_memory(bus: Any, memory: Any) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []

    dlq = int(getattr(bus, "dlq_size", 0))
    checks.append(GateCheck("C3.1", "La Dead Letter Queue e' vuota", dlq == 0,
                            "" if dlq == 0 else f"{dlq} eventi non recapitati"))

    falliti = list(getattr(bus, "failed_deliveries", []) or [])
    checks.append(GateCheck("C3.2", "Nessuna consegna di evento e' fallita in silenzio", not falliti,
                            "" if not falliti else f"{len(falliti)} consegne fallite: {falliti[:3]}"))

    ha_log = isinstance(getattr(bus, "event_log", None), list)
    checks.append(GateCheck("C3.3", "Il bus tiene un registro ispezionabile degli eventi", ha_log,
                            "" if ha_log else "event_log assente o non una lista"))

    if memory is not None:
        contratto = ["log_decision", "get_recent_decisions", "working_memory"]
        assenti = [m for m in contratto if not hasattr(memory, m)]
        checks.append(GateCheck("C3.4", "La memoria espone il contratto richiesto", not assenti,
                                "" if not assenti else f"membri mancanti: {assenti}"))

        # round-trip in working memory: reale, e non sporca il decision log
        rt_ok, rt_detail = _memory_roundtrip(memory)
        checks.append(GateCheck("C3.5", "La working memory regge un ciclo scrittura/rilettura", rt_ok, rt_detail))

    return GateResult.build("GATE_L3_BUS_MEMORY", 3, THRESHOLDS[3], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


def _memory_roundtrip(memory: Any) -> Tuple[bool, str]:
    chiave = "__gate_l3_probe__"
    try:
        wm = memory.working_memory
        if not isinstance(wm, dict):
            return False, f"working_memory e' {type(wm).__name__}, atteso dict"
        sentinella = time.time()
        wm[chiave] = sentinella
        riletto = wm.get(chiave)
        del wm[chiave]
        if riletto != sentinella:
            return False, "il valore riletto non coincide con quello scritto"
        if chiave in wm:
            return False, "la chiave di prova non e' stata rimossa"
        return True, ""
    except Exception as exc:
        return False, f"round-trip fallito: {exc}"


# ─────────────────────────────────────────────────────────────────────────────
# L4 — Swarm
# ─────────────────────────────────────────────────────────────────────────────

def gate_l4_swarm(
    registered_roles: Sequence[str],
    required_roles: Sequence[str],
    workflow_output: Mapping[str, Any],
    expected_output_keys: Sequence[str] = (),
    executed_traces: int = 0,
    min_traces: int = 0,
) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []
    registrati = set(registered_roles)

    mancanti = sorted(set(required_roles) - registrati)
    checks.append(GateCheck("C4.1", "Tutti i ruoli richiesti sono registrati nello swarm", not mancanti,
                            "" if not mancanti else f"ruoli mancanti: {mancanti}"))

    ha_output = isinstance(workflow_output, Mapping) and len(workflow_output) > 0
    checks.append(GateCheck("C4.2", "Il workflow ha prodotto un output non vuoto", ha_output,
                            "" if ha_output else "output del workflow vuoto o non un dizionario"))

    if expected_output_keys:
        assenti = [k for k in expected_output_keys if k not in (workflow_output or {})]
        checks.append(GateCheck("C4.3", "L'output rispetta il contratto di handoff dichiarato", not assenti,
                                "" if not assenti else f"chiavi assenti dall'output: {assenti}"))

    if min_traces > 0:
        ok = executed_traces >= min_traces
        checks.append(GateCheck("C4.4", "Le tracce di esecuzione degli agenti sono sufficienti", ok,
                                "" if ok else f"tracce registrate {executed_traces}, attese >= {min_traces}"))

    # un output esclusivamente mock significa che nessun agente vero ha girato
    solo_mock = bool(workflow_output) and all(
        isinstance(v, Mapping) and v.get("mock") is True
        for v in workflow_output.values() if isinstance(v, Mapping)
    ) and any(isinstance(v, Mapping) for v in workflow_output.values())
    checks.append(GateCheck("C4.5", "L'output non proviene interamente da agenti mock", not solo_mock,
                            "" if not solo_mock else "ogni contributo dell'output e' marcato mock=True"))

    return GateResult.build("GATE_L4_SWARM", 4, THRESHOLDS[4], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# L5 — Qualita' e calibrazione
# ─────────────────────────────────────────────────────────────────────────────

def gate_l5_quality(report: QualityReport) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []

    n_audit = len(report.audits)
    checks.append(GateCheck("C5.1", "Sono stati eseguiti abbastanza audit di qualita'",
                            n_audit >= report.min_audits,
                            "" if n_audit >= report.min_audits else
                            f"{n_audit} audit eseguiti, attesi >= {report.min_audits}"))

    critici = [a.audit_id for a in report.audits if a.triggered and a.severity == "CRITICAL"]
    checks.append(GateCheck("C5.2", "Nessun audit CRITICAL e' scattato", not critici,
                            "" if not critici else f"audit critici scattati: {critici}"))

    score_ok = is_finite_number(report.score) and report.score >= report.threshold
    checks.append(GateCheck("C5.3", "Lo score di qualita' raggiunge la soglia dichiarata", score_ok,
                            "" if score_ok else f"score {report.score} < soglia {report.threshold}"))

    # I check di calibrazione si emettono solo se il dominio dichiara una distribuzione.
    if report.outcomes:
        somma = sum(o.probability_pct for o in report.outcomes)
        somma_ok = abs(somma - 100.0) < 1e-6
        checks.append(GateCheck("C5.4", "Le probabilita' degli esiti sommano a 100%", somma_ok,
                                "" if somma_ok else f"somma delle probabilita' = {somma}%"))

        etichette = [o.label for o in report.outcomes]
        uniche = len(set(etichette)) == len(etichette)
        checks.append(GateCheck("C5.5", "Le etichette degli esiti sono uniche", uniche,
                                "" if uniche else f"etichette duplicate in {etichette}"))

        negative = [o.label for o in report.outcomes if o.probability_pct < 0]
        checks.append(GateCheck("C5.6", "Nessuna probabilita' e' negativa", not negative,
                                "" if not negative else f"probabilita' negative: {negative}"))

        valori_ok = all(is_finite_number(o.value) for o in report.outcomes)
        checks.append(GateCheck("C5.7", "Ogni esito porta un valore numerico finito", valori_ok,
                                "" if valori_ok else "almeno un esito ha valore NaN/Inf/non numerico"))

        distinti = len({round(o.value, 9) for o in report.outcomes}) > 1
        checks.append(GateCheck("C5.8", "La distribuzione non e' una stima puntuale travestita", distinti,
                                "" if distinti else "tutti gli esiti hanno lo stesso valore"))

    return GateResult.build("GATE_L5_QUALITY", 5, THRESHOLDS[5], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# L6 — Sicurezza dell'auto-evoluzione
# ─────────────────────────────────────────────────────────────────────────────

def gate_l6_evolution(experiments: Sequence[EvolutionExperiment]) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []
    from .evolution import SelfEvolutionSafetyGuard

    checks.append(GateCheck("C6.1", "La guardia di evoluzione e' stata effettivamente interrogata",
                            len(experiments) > 0,
                            "" if experiments else "nessun esperimento valutato: il livello L6 non ha girato"))

    violazioni = [
        e.experiment_id for e in experiments
        if e.component in SelfEvolutionSafetyGuard.IMMUTABLE and e.status != "REJECTED"
    ]
    checks.append(GateCheck("C6.2", "Nessun invariante di sistema e' stato mutato", not violazioni,
                            "" if not violazioni else f"mutazioni su componenti immutabili: {violazioni}"))

    override_mancanti = [
        e.experiment_id for e in experiments
        if e.component in SelfEvolutionSafetyGuard.IMMUTABLE and not e.human_override_required
    ]
    checks.append(GateCheck("C6.3", "Le mutazioni sugli invarianti richiedono override umano",
                            not override_mancanti,
                            "" if not override_mancanti else f"override non richiesto per: {override_mancanti}"))

    rollback_mancati = [
        e.experiment_id for e in experiments
        if e.delta_pct <= SelfEvolutionSafetyGuard.ROLLBACK_DELTA_PCT and e.status != "ROLLED_BACK"
    ]
    checks.append(GateCheck("C6.4", "Ogni regressione oltre soglia e' stata riportata indietro",
                            not rollback_mancati,
                            "" if not rollback_mancati else f"rollback non applicato per: {rollback_mancati}"))

    stati_validi = {"ADOPTED", "REJECTED", "ROLLED_BACK"}
    invalidi = [e.experiment_id for e in experiments if e.status not in stati_validi]
    checks.append(GateCheck("C6.5", "Ogni esperimento ha uno stato valido", not invalidi,
                            "" if not invalidi else f"stati fuori contratto: {invalidi}"))

    return GateResult.build("GATE_L6_EVOLUTION", 6, THRESHOLDS[6], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# L7 — Certificazione finale
# ─────────────────────────────────────────────────────────────────────────────

REQUIRED_GATE_IDS: Tuple[str, ...] = (
    "GATE_L1_FOUNDATION",
    "GATE_L2_DAG",
    "GATE_L3_BUS_MEMORY",
    "GATE_L4_SWARM",
    "GATE_L5_QUALITY",
    "GATE_L6_EVOLUTION",
)


def gate_l7_apex(
    gate_results: Mapping[str, GateResult],
    e2e_duration_ms: float,
    sla_ms: float = DEFAULT_SLA_MS,
    dlq_size: int = 0,
    unresolved_healing: Sequence[Any] = (),
    chain: Sequence[StateSnapshot] = (),
) -> GateResult:
    t0 = time.perf_counter()
    checks: List[GateCheck] = []

    assenti = [g for g in REQUIRED_GATE_IDS if g not in gate_results]
    checks.append(GateCheck("C7.1", "Tutti i gate da L1 a L6 sono stati eseguiti", not assenti,
                            "" if not assenti else f"gate mai eseguiti: {assenti}"))

    non_passati = [g for g in REQUIRED_GATE_IDS if g in gate_results and not gate_results[g].passed]
    checks.append(GateCheck("C7.2", "Tutti i gate da L1 a L6 sono passati", not non_passati,
                            "" if not non_passati else f"gate non passati: {non_passati}"))

    sotto_soglia = [
        f"{g}({gate_results[g].score:.0%}<{gate_results[g].threshold:.0%})"
        for g in REQUIRED_GATE_IDS
        if g in gate_results and gate_results[g].score < gate_results[g].threshold
    ]
    checks.append(GateCheck("C7.3", "Ogni gate rispetta la propria soglia specifica", not sotto_soglia,
                            "" if not sotto_soglia else f"soglie non rispettate: {sotto_soglia}"))

    sla_ok = e2e_duration_ms < sla_ms
    checks.append(GateCheck("C7.4", f"La latenza end-to-end resta sotto lo SLA di {sla_ms:.0f}ms", sla_ok,
                            "" if sla_ok else f"latenza {e2e_duration_ms:.1f}ms >= SLA {sla_ms:.0f}ms"))

    checks.append(GateCheck("C7.5", "Nessun evento e' finito in Dead Letter Queue", dlq_size == 0,
                            "" if dlq_size == 0 else f"{dlq_size} eventi in DLQ"))

    irrisolti = list(unresolved_healing)
    checks.append(GateCheck("C7.6", "Nessun guasto e' rimasto senza recupero", not irrisolti,
                            "" if not irrisolti else f"{len(irrisolti)} interventi di self-healing non riusciti"))

    if chain:
        intatta = verify_chain(tuple(chain))
        checks.append(GateCheck("C7.7", "La catena di stato e' ancora intatta a fine run", intatta,
                                "" if intatta else "la catena Merkle non verifica piu' a valle dell'esecuzione"))

    return GateResult.build("GATE_L7_APEX", 7, THRESHOLDS[7], tuple(checks),
                            (time.perf_counter() - t0) * 1000.0)


# ─────────────────────────────────────────────────────────────────────────────
# Esecuzione e rendicontazione
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class GateLedger:
    """Registro degli esiti. La rendicontazione si legge da qui, mai da stringhe fisse."""
    results: Dict[str, GateResult] = field(default_factory=dict)

    def record(self, result: GateResult, blocking: bool = True) -> GateResult:
        self.results[result.gate_id] = result
        if blocking and not result.passed:
            raise GateBlocked(result)
        return result

    @property
    def all_passed(self) -> bool:
        return bool(self.results) and all(r.passed for r in self.results.values())

    @property
    def certified(self) -> bool:
        """Certificato solo con L1..L7 tutti presenti e tutti passati."""
        attesi = set(REQUIRED_GATE_IDS) | {"GATE_L7_APEX"}
        return attesi.issubset(self.results) and self.all_passed

    def scorecard(self) -> List[Dict[str, Any]]:
        return [r.to_dict() for r in sorted(self.results.values(), key=lambda r: r.level)]

    def render(self) -> str:
        righe = ["QUALITY GATE SCORECARD (L1 -> L7)"]
        for r in sorted(self.results.values(), key=lambda x: x.level):
            icona = "PASS" if r.passed else "FAIL"
            righe.append(
                f"  [{icona}] L{r.level} {r.gate_id:<24} "
                f"{sum(1 for c in r.checks if c.passed)}/{len(r.checks)} check "
                f"({r.score:.0%}, soglia {r.threshold:.0%})"
            )
            for c in r.failures:
                righe.append(f"         - {c.check_id}: {c.detail or c.description}")
        stato = "CERTIFICATO" if self.certified else "NON CERTIFICATO"
        mancanti = sorted((set(REQUIRED_GATE_IDS) | {"GATE_L7_APEX"}) - set(self.results))
        if mancanti:
            righe.append(f"  gate mai eseguiti: {mancanti}")
        righe.append(f"  ESITO: {stato}")
        return "\n".join(righe)
