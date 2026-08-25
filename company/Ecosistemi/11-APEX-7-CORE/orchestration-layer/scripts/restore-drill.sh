#!/usr/bin/env bash
set -euo pipefail
: "${PGHOST:?}" "${PGPORT:?}" "${PGUSER:?}" "${SOURCE_DATABASE:?}" "${RESTORE_DATABASE:?}" "${OCP_BACKUP_PATH:?}" "${DRILL_TENANT:?}"
[[ "$RESTORE_DATABASE" == ocp_restore_* ]] || { echo "Unsafe restore database name" >&2; exit 2; }
[[ "$DRILL_TENANT" =~ ^[A-Za-z0-9_-]{3,64}$ ]] || { echo "Unsafe drill tenant" >&2; exit 2; }
sha256sum --check "$OCP_BACKUP_PATH.sha256"
dropdb --if-exists "$RESTORE_DATABASE"
createdb "$RESTORE_DATABASE"
pg_restore --exit-on-error --no-owner --no-acl --dbname="$RESTORE_DATABASE" "$OCP_BACKUP_PATH"
psql --dbname="$RESTORE_DATABASE" --no-align --tuples-only --command="
SELECT set_config('app.tenant_id', '$DRILL_TENANT', true);
SELECT 'tables=' || count(*) FROM pg_tables WHERE schemaname='public';
SELECT 'forced_rls=' || count(*) FROM pg_class WHERE relnamespace='public'::regnamespace AND relkind='r' AND relrowsecurity AND relforcerowsecurity;
SELECT 'workflow_rows=' || count(*) FROM workflows;
SELECT 'audit_rows=' || count(*) FROM audit_events;
SELECT 'outbox_rows=' || count(*) FROM outbox_events;
"
