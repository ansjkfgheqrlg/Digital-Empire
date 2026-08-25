#!/usr/bin/env bash
set -euo pipefail

: "${OCP_TEST_DATABASE_URL:?Set OCP_TEST_DATABASE_URL to a disposable PostgreSQL database}"

python -m compileall -q src migrations
python -m unittest discover -s tests/integration -v
