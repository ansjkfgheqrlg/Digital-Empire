"""Eccezioni del dominio.

Ogni violazione di regola ha un tipo dedicato: chi legge un traceback deve capire *quale*
vincolo e' stato infranto senza aprire il codice.
"""

from __future__ import annotations


class FactoryError(Exception):
    """Radice di tutte le eccezioni del progetto."""


class InvalidTransitionError(FactoryError):
    """Transizione di stato non ammessa dalla macchina a stati."""

    def __init__(self, current: str, target: str, reason: str = "") -> None:
        self.current = current
        self.target = target
        self.reason = reason
        dettaglio = f" — {reason}" if reason else ""
        super().__init__(f"Transizione non valida: {current} → {target}{dettaglio}")


class AuthorizationError(FactoryError):
    """Un agente ha tentato un'azione fuori dal proprio livello gerarchico."""

    def __init__(self, agent: str, level: str, action: str) -> None:
        self.agent = agent
        self.level = level
        self.action = action
        super().__init__(f"L'agente '{agent}' (livello {level}) non e' autorizzato a: {action}")


class NicheLockError(FactoryError):
    """Tentativo di modificare la nicchia primaria, che e' protetta."""

    def __init__(self, agent: str, attempted: str, primary: str) -> None:
        super().__init__(
            f"'{agent}' ha tentato di cambiare la nicchia primaria da '{primary}' a "
            f"'{attempted}'. La nicchia primaria non si cambia durante un workflow: le nuove "
            f"nicchie sono solo proposte soggette a decisione senior."
        )


class RegulatoryBlockError(FactoryError):
    """Un regolatore ha bloccato l'avanzamento."""

    def __init__(self, reasons: list[str]) -> None:
        self.reasons = reasons
        elenco = "; ".join(reasons) if reasons else "nessuna motivazione registrata"
        super().__init__(f"Blocco regolatorio: {elenco}")


class ApprovalRequiredError(FactoryError):
    """Manca un'approvazione obbligatoria per l'azione richiesta."""

    def __init__(self, subject: str, required_level: str) -> None:
        super().__init__(
            f"'{subject}' richiede un'approvazione di livello {required_level} non presente."
        )


class OriginalityCheckError(FactoryError):
    """Un asset non ha superato (o non ha eseguito) il controllo di originalita'."""


class AutomationNotConfiguredError(FactoryError):
    """L'automazione browser e' stata invocata senza configurazione completa.

    Sollevata di proposito invece di tentare con selettori inventati: dati falsi sono peggio
    di un errore esplicito.
    """

    def __init__(self, target: str, missing: list[str]) -> None:
        self.target = target
        self.missing = missing
        super().__init__(
            f"Automazione '{target}' non configurata. Mancano: {', '.join(missing)}. "
            f"Vedi .env.example e docs/architecture.md."
        )


class BrowserAutomationError(FactoryError):
    """Errore durante l'interazione con il browser."""


class FlikAdapterError(FactoryError):
    """Errore dell'integrazione di produzione video."""
