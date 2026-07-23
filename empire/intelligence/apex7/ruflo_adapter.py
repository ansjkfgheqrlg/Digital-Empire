"""RuFLO adapter — seam di integrazione con l'orchestratore Rust (ruflo).

Onesto: l'integrazione richiede il crate RuFLO + binding Python (es.
pyo3/maturin) e un toolchain Rust. Qui definiamo SOLO l'interfaccia
(RuFLOCompatible) e un adapter che solleva NotImplementedError, così
APEX-7 resta eseguibile in puro Python e il punto di innesto e' chiaro.

Per attivarlo:
  1. clonare https://github.com/ruvnet/ruflo
  2. esporre un metodo `run_workflow(graph)` via pyo3
  3. implementare _run_ruflo() qui sotto chiamando il binding.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class RufloCompatible(ABC):
    @abstractmethod
    def run_workflow(self, task_graph: list[str]) -> dict:
        ...


class RufloOrchestrator(RufloCompatible):
    def __init__(self, rust_handle=None):
        self._rust = rust_handle  # binding pyo3 verso il crate RuFLO

    def run_workflow(self, task_graph: list[str]) -> dict:
        if self._rust is None:
            raise NotImplementedError(
                "RuFLO non collegato: serve il binding Rust (pyo3/maturin) "
                "verso github.com/ruvnet/ruflo. Interfaccia pronta in "
                "RufloCompatible.run_workflow()."
            )
        # Esempio di innesto reale (da implementare col binding):
        # return self._rust.execute(json.dumps({"stages": task_graph}))
        return self._rust.run_workflow(task_graph)
