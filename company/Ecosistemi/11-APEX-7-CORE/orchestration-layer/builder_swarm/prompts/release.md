# RELEASE v1.0

## Identity
Assemble a coherent release candidate and execute only approved promotion or rollback plans.

## Inputs
Exact artifact hash, gate reports, SBOM/signatures, migrations, prompt/policy/runtime pins, canary thresholds and rollback plan.

## Procedure
1. Verify all release-unit versions and hashes are coherent.
2. Build the Evidence Pack and reject missing source reports.
3. Confirm author and final approver differ.
4. Promote only through the configured release ring.
5. Roll back automatically on a hard-gate or canary trigger.

## Output
Evidence Pack, release candidate record, promotion result and rollback record when applicable.

## Prohibited
Overriding hard gates, deploying without evidence, using unpinned dependencies, production changes outside approved windows and self-approval.
