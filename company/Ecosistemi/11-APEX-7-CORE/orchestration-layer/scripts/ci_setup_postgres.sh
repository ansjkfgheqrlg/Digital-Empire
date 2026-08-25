#!/usr/bin/env bash
set -euo pipefail
export PGPASSWORD="${POSTGRES_ADMIN_PASSWORD:-postgres}"
psql -h 127.0.0.1 -U postgres -d postgres -v ON_ERROR_STOP=1 <<'SQL'
DROP DATABASE IF EXISTS ocp_test;
DROP ROLE IF EXISTS ocp_runtime;
DROP ROLE IF EXISTS ocp_migrator;
CREATE ROLE ocp_migrator LOGIN PASSWORD 'migrator-test';
CREATE ROLE ocp_runtime LOGIN PASSWORD 'runtime-test' NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOBYPASSRLS;
CREATE DATABASE ocp_test OWNER ocp_migrator;
SQL
PGPASSWORD=migrator-test psql -h 127.0.0.1 -U ocp_migrator -d ocp_test -v ON_ERROR_STOP=1 -f migrations/versions/0001_core.sql
PGPASSWORD=migrator-test psql -h 127.0.0.1 -U ocp_migrator -d ocp_test -v ON_ERROR_STOP=1 -f migrations/versions/0002_privacy.sql
PGPASSWORD=migrator-test psql -h 127.0.0.1 -U ocp_migrator -d ocp_test -v ON_ERROR_STOP=1 <<'SQL'
GRANT USAGE ON SCHEMA public TO ocp_runtime;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO ocp_runtime;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO ocp_runtime;
SQL
