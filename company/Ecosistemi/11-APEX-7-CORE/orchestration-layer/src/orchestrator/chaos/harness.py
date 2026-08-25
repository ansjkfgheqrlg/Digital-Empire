from __future__ import annotations

from dataclasses import dataclass
from typing import Awaitable, Callable


Probe = Callable[[], Awaitable[bool]]
Action = Callable[[], Awaitable[None]]


@dataclass(frozen=True)
class ChaosResult:
    experiment_id: str
    baseline_pass: bool
    steady_state_pass: bool
    cleanup_pass: bool
    aborted: bool

    @property
    def passed(self) -> bool:
        return self.baseline_pass and self.steady_state_pass and self.cleanup_pass and not self.aborted


class ChaosExperiment:
    """Bounded chaos experiment with mandatory baseline, abort and cleanup."""

    def __init__(
        self,
        experiment_id: str,
        baseline: Probe,
        inject: Action,
        steady_state: Probe,
        cleanup: Action,
        cleanup_probe: Probe,
        abort: Action,
    ):
        self.experiment_id = experiment_id
        self.baseline = baseline
        self.inject = inject
        self.steady_state = steady_state
        self.cleanup = cleanup
        self.cleanup_probe = cleanup_probe
        self.abort = abort

    async def run(self) -> ChaosResult:
        baseline_pass = await self.baseline()
        if not baseline_pass:
            return ChaosResult(self.experiment_id, False, False, False, True)
        aborted = False
        steady = False
        cleanup_pass = False
        try:
            await self.inject()
            steady = await self.steady_state()
            if not steady:
                aborted = True
                await self.abort()
        finally:
            await self.cleanup()
            cleanup_pass = await self.cleanup_probe()
        return ChaosResult(self.experiment_id, baseline_pass, steady, cleanup_pass, aborted)
