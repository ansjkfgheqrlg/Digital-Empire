"""
APEX-7 Calc Layer — nucleo: aritmetica sicura, contratti e registro.

Il layer di calcolo e' un REGISTRO di funzioni pure. Ogni calcolo:
  - dichiara i parametri che gli servono,
  - restituisce solo numeri finiti (mai NaN/Inf/None silenziosi),
  - e' serializzabile in JSON.

L'ultimo punto non e' estetico: questo layer dovra' parlare con gli altri
orchestration layer, e il ponte fra loro puo' trasportare solo dati, non
oggetti Python. Per questo l'unica interfaccia pubblica e' `esegui(dict) ->
dict` (vedi engine.py).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple


class ErroreCalcolo(ValueError):
    """Parametro assente, fuori dominio o risultato non rappresentabile."""


# ─────────────────────────────────────────────────────────────────────────────
# Aritmetica sicura (IEEE-754)
# ─────────────────────────────────────────────────────────────────────────────

class SafeMath:
    @staticmethod
    def div(num: float, den: float, default: float = 0.0) -> float:
        if abs(den) < 1e-12:
            return default
        r = num / den
        return default if not math.isfinite(r) else r

    @staticmethod
    def pow(base: float, exp: float, default: float = 0.0) -> float:
        try:
            if base < 0 and not float(exp).is_integer():
                return default
            r = math.pow(base, exp)
            return default if not math.isfinite(r) else r
        except (OverflowError, ValueError):
            return default

    @staticmethod
    def ln(x: float, default: float = 0.0) -> float:
        return math.log(x) if x > 0 else default

    @staticmethod
    def pct(parte: float, totale: float, default: float = 0.0) -> float:
        """Percentuale di `parte` su `totale`."""
        return SafeMath.div(parte, totale, default) * 100.0

    @staticmethod
    def variazione_pct(da: float, a: float, default: float = 0.0) -> float:
        """Variazione percentuale da un valore a un altro."""
        return SafeMath.div(a - da, abs(da), default) * 100.0

    @staticmethod
    def clamp(x: float, minimo: float, massimo: float) -> float:
        return max(minimo, min(massimo, x))

    @staticmethod
    def phi(z: float) -> float:
        """CDF della normale standard. Serve a tutte le probabilita' di soglia."""
        return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def num(valori: Mapping[str, Any], chiave: str, default: Optional[float] = None,
        minimo: Optional[float] = None, massimo: Optional[float] = None) -> float:
    """Estrae un parametro numerico validandolo. Fallisce forte, non in silenzio."""
    if chiave not in valori or valori[chiave] is None:
        if default is None:
            raise ErroreCalcolo(f"parametro obbligatorio mancante: '{chiave}'")
        return float(default)
    v = valori[chiave]
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ErroreCalcolo(f"'{chiave}' deve essere un numero, ricevuto {type(v).__name__}")
    v = float(v)
    if not math.isfinite(v):
        raise ErroreCalcolo(f"'{chiave}' non e' un numero finito: {v}")
    if minimo is not None and v < minimo:
        raise ErroreCalcolo(f"'{chiave}' = {v} sotto il minimo consentito ({minimo})")
    if massimo is not None and v > massimo:
        raise ErroreCalcolo(f"'{chiave}' = {v} sopra il massimo consentito ({massimo})")
    return v


def arrotonda(d: Dict[str, Any], cifre: int = 4) -> Dict[str, Any]:
    """Arrotonda i float di un risultato, lasciando intatto tutto il resto."""
    out: Dict[str, Any] = {}
    for k, v in d.items():
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            out[k] = v
        else:
            out[k] = round(float(v), cifre)
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Contratti (JSON-serializzabili: sono il ponte verso gli altri layer)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Parametro:
    nome: str
    descrizione: str
    obbligatorio: bool = True
    default: Optional[float] = None
    unita: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {"nome": self.nome, "descrizione": self.descrizione,
                "obbligatorio": self.obbligatorio, "default": self.default,
                "unita": self.unita}


@dataclass(frozen=True)
class ModuloCalcolo:
    """Un calcolo registrato. `fn` e' pura: dict -> dict di numeri finiti."""
    id: str
    categoria: str
    descrizione: str
    parametri: Tuple[Parametro, ...]
    fn: Callable[[Mapping[str, Any]], Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "categoria": self.categoria,
                "descrizione": self.descrizione,
                "parametri": [p.to_dict() for p in self.parametri]}


@dataclass(frozen=True)
class Assunzione:
    """
    Un valore che il calcolo ha usato senza che l'utente lo abbia dichiarato.

    Esiste per una ragione sola: un numero prodotto da un default non e' un
    numero misurato, e chi legge il risultato deve poterlo distinguere.
    """
    parametro: str
    valore: float
    fonte: str

    def to_dict(self) -> Dict[str, Any]:
        return {"parametro": self.parametro, "valore": self.valore, "fonte": self.fonte}


@dataclass
class RisultatoCalcolo:
    modulo: str
    ok: bool
    valori: Dict[str, Any] = field(default_factory=dict)
    assunzioni: List[Assunzione] = field(default_factory=list)
    avvisi: List[str] = field(default_factory=list)
    errore: Optional[str] = None
    durata_ms: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "modulo": self.modulo,
            "ok": self.ok,
            "valori": self.valori,
            "assunzioni": [a.to_dict() for a in self.assunzioni],
            "avvisi": self.avvisi,
            "errore": self.errore,
            "durata_ms": round(self.durata_ms, 3),
        }


# ─────────────────────────────────────────────────────────────────────────────
# Registro
# ─────────────────────────────────────────────────────────────────────────────

REGISTRO: Dict[str, ModuloCalcolo] = {}


def registra(id: str, categoria: str, descrizione: str, parametri: Sequence[Parametro]):
    """Decoratore: aggiunge una funzione pura al registro dei calcoli."""
    def wrapper(fn):
        if id in REGISTRO:
            raise ErroreCalcolo(f"modulo di calcolo gia' registrato: '{id}'")
        REGISTRO[id] = ModuloCalcolo(id, categoria, descrizione, tuple(parametri), fn)
        return fn
    return wrapper


def catalogo() -> List[Dict[str, Any]]:
    """Elenco serializzabile di tutto ciò che il layer sa calcolare."""
    return [m.to_dict() for m in sorted(REGISTRO.values(), key=lambda m: (m.categoria, m.id))]
