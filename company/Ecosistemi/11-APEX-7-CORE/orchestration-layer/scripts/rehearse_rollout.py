from __future__ import annotations

import json
from pathlib import Path

from orchestrator.release import ReleaseController, ReleaseRing, RolloutError


def main() -> int:
    controller = ReleaseController("ocp-0.1.0-pilot", prr_verdict="NO_GO")
    for ring in (
        ReleaseRing.TEST,
        ReleaseRing.SHADOW,
        ReleaseRing.CANARY_5,
        ReleaseRing.CANARY_25,
        ReleaseRing.PILOT,
    ):
        controller.promote(ring, hard_gates_pass=True)
    production_blocked = False
    try:
        controller.promote(ReleaseRing.PROD, hard_gates_pass=True)
    except RolloutError:
        production_blocked = True
    controller.rollback("Rehearsal complete; PRR remains NO_GO")
    report = {
        "release_id": controller.release_id,
        "production_promotion_blocked": production_blocked,
        "final_state": controller.ring.value,
        "history": controller.history,
        "real_traffic": False,
        "real_deployment": False,
        "status": "PASS" if production_blocked and controller.ring is ReleaseRing.ROLLED_BACK else "FAIL",
    }
    target = Path("quality/evidence/w12-rollout-rehearsal.json")
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
