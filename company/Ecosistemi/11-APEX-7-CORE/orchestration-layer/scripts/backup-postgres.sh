#!/usr/bin/env bash
set -euo pipefail
: "${PGHOST:?}" "${PGPORT:?}" "${PGUSER:?}" "${PGDATABASE:?}" "${OCP_BACKUP_PATH:?}"
mkdir -p "$(dirname "$OCP_BACKUP_PATH")"
pg_dump --format=custom --no-owner --no-acl --file="$OCP_BACKUP_PATH" "$PGDATABASE"
sha256sum "$OCP_BACKUP_PATH" > "$OCP_BACKUP_PATH.sha256"
