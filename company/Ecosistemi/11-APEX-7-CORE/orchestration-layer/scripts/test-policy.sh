#!/usr/bin/env bash
set -euo pipefail
: "${OPA_BIN:?Set OPA_BIN to the pinned OPA binary}"
"$OPA_BIN" fmt --fail policies/
"$OPA_BIN" check --strict policies/
"$OPA_BIN" test policies/ -v
