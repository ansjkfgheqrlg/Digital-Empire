CREATE TYPE risk_class AS ENUM ('R0','R1','R2','R3');
CREATE TYPE workflow_status AS ENUM (
  'RECEIVED','VALIDATING','PLANNING','PLAN_REVIEW','AWAITING_APPROVAL',
  'AUTHORIZED','RUNNING','PAUSED','RECOVERING','RECONCILING','COMPENSATING',
  'QUALITY_REVIEW','REMEDIATING','CANCEL_REQUESTED','CANCELLING',
  'COMPLETED','FAILED','REJECTED','CANCELLED','COMPENSATED','MANUAL_INTERVENTION'
);
CREATE TYPE task_status AS ENUM (
  'PENDING','BLOCKED','READY','LEASED','RUNNING','SUCCEEDED','FAILED',
  'RETRY_WAIT','COMPENSATING','COMPENSATED','CANCELLED'
);

CREATE TABLE workflows (
  workflow_id uuid PRIMARY KEY,
  tenant_id text NOT NULL CHECK (length(tenant_id) BETWEEN 3 AND 64),
  workflow_type text NOT NULL,
  risk risk_class NOT NULL,
  status workflow_status NOT NULL,
  goal text NOT NULL CHECK (length(goal) BETWEEN 1 AND 20000),
  constraints jsonb NOT NULL DEFAULT '{}',
  budget_limit jsonb NOT NULL,
  budget_used jsonb NOT NULL DEFAULT '{"tokens":0,"cost_usd":"0","duration_ms":0}',
  idempotency_key text NOT NULL,
  requested_by text NOT NULL,
  version bigint NOT NULL DEFAULT 0 CHECK (version >= 0),
  sequence bigint NOT NULL DEFAULT 0 CHECK (sequence >= 0),
  deadline_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (tenant_id, workflow_id),
  UNIQUE (tenant_id, idempotency_key)
);

CREATE TABLE tasks (
  task_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  workflow_id uuid NOT NULL,
  ordinal integer NOT NULL CHECK (ordinal >= 0),
  role text NOT NULL CHECK (role IN ('planner','implementer','critic','gate','compensator')),
  objective text NOT NULL CHECK (length(objective) BETWEEN 1 AND 8000),
  status task_status NOT NULL,
  depends_on uuid[] NOT NULL DEFAULT '{}',
  completion_criteria jsonb NOT NULL,
  capabilities jsonb NOT NULL DEFAULT '[]',
  side_effect jsonb NOT NULL,
  budget_limit jsonb NOT NULL,
  max_attempts smallint NOT NULL CHECK (max_attempts BETWEEN 1 AND 3),
  attempt smallint NOT NULL DEFAULT 0 CHECK (attempt >= 0 AND attempt <= max_attempts),
  ready_at timestamptz NOT NULL DEFAULT now(),
  leased_by text,
  leased_until timestamptz,
  execution_token_hash text,
  capability_grant_id uuid,
  input_ref text NOT NULL,
  output_ref text,
  failure_code text,
  version bigint NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (tenant_id, workflow_id) REFERENCES workflows(tenant_id, workflow_id),
  UNIQUE (tenant_id, task_id),
  UNIQUE (tenant_id, workflow_id, ordinal),
  CHECK ((leased_by IS NULL) = (leased_until IS NULL)),
  CHECK ((leased_by IS NULL) = (execution_token_hash IS NULL))
);
CREATE INDEX ix_tasks_claim ON tasks (tenant_id, ready_at, created_at)
  WHERE status IN ('READY','RETRY_WAIT');
CREATE INDEX ix_tasks_workflow ON tasks (tenant_id, workflow_id, ordinal);

CREATE TABLE task_runs (
  task_run_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  task_id uuid NOT NULL,
  attempt smallint NOT NULL,
  runtime text NOT NULL,
  runtime_version text NOT NULL,
  prompt_hash text NOT NULL,
  started_at timestamptz NOT NULL,
  ended_at timestamptz,
  status text NOT NULL,
  usage jsonb NOT NULL DEFAULT '{}',
  output_ref text,
  failure jsonb,
  FOREIGN KEY (tenant_id, task_id) REFERENCES tasks(tenant_id, task_id),
  UNIQUE (tenant_id, task_id, attempt)
);

CREATE TABLE approvals (
  approval_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  workflow_id uuid NOT NULL,
  subject_id text NOT NULL,
  auth_context jsonb NOT NULL,
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT')),
  plan_hash text NOT NULL,
  policy_hash text NOT NULL,
  nonce_hash text NOT NULL UNIQUE,
  expires_at timestamptz NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (tenant_id, workflow_id) REFERENCES workflows(tenant_id, workflow_id)
);

CREATE TABLE capability_grants (
  grant_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  workflow_id uuid NOT NULL,
  task_id uuid NOT NULL,
  subject text NOT NULL,
  capabilities jsonb NOT NULL,
  constraints jsonb NOT NULL,
  token_hash text NOT NULL UNIQUE,
  nonce_hash text NOT NULL UNIQUE,
  expires_at timestamptz NOT NULL,
  consumed_at timestamptz,
  revoked_at timestamptz,
  FOREIGN KEY (tenant_id, workflow_id) REFERENCES workflows(tenant_id, workflow_id),
  FOREIGN KEY (tenant_id, task_id) REFERENCES tasks(tenant_id, task_id)
);
ALTER TABLE tasks ADD CONSTRAINT fk_tasks_grant
  FOREIGN KEY (capability_grant_id) REFERENCES capability_grants(grant_id);

CREATE TABLE gate_runs (
  gate_run_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  workflow_id uuid NOT NULL,
  task_id uuid,
  gate_id text NOT NULL,
  rubric_version text NOT NULL,
  artifact_hash text NOT NULL,
  attempt smallint NOT NULL CHECK (attempt BETWEEN 1 AND 3),
  verdict text NOT NULL CHECK (verdict IN ('PASS','REMEDIATE','REJECT','ESCALATE')),
  blocking_failures jsonb NOT NULL DEFAULT '[]',
  criteria jsonb NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  FOREIGN KEY (tenant_id, workflow_id) REFERENCES workflows(tenant_id, workflow_id),
  FOREIGN KEY (tenant_id, task_id) REFERENCES tasks(tenant_id, task_id),
  UNIQUE (tenant_id, gate_id, artifact_hash, attempt)
);

CREATE TABLE audit_events (
  audit_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  event_id uuid NOT NULL UNIQUE,
  tenant_id text NOT NULL,
  workflow_id uuid NOT NULL,
  sequence bigint NOT NULL CHECK (sequence >= 1),
  actor_type text NOT NULL,
  actor_id text NOT NULL,
  event_type text NOT NULL,
  payload jsonb NOT NULL,
  payload_hash text NOT NULL,
  trace_id text NOT NULL,
  occurred_at timestamptz NOT NULL,
  FOREIGN KEY (tenant_id, workflow_id) REFERENCES workflows(tenant_id, workflow_id),
  UNIQUE (tenant_id, workflow_id, sequence)
);
CREATE INDEX ix_audit_workflow ON audit_events (tenant_id, workflow_id, sequence);

CREATE TABLE outbox_events (
  event_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  aggregate_id uuid NOT NULL,
  event_type text NOT NULL,
  schema_version text NOT NULL,
  payload jsonb NOT NULL,
  occurred_at timestamptz NOT NULL,
  published_at timestamptz,
  attempts smallint NOT NULL DEFAULT 0 CHECK (attempts >= 0),
  last_error text,
  FOREIGN KEY (tenant_id, aggregate_id) REFERENCES workflows(tenant_id, workflow_id)
);
CREATE INDEX ix_outbox_unpublished ON outbox_events (occurred_at)
  WHERE published_at IS NULL;

CREATE TABLE memory_records (
  memory_id uuid PRIMARY KEY,
  tenant_id text NOT NULL,
  namespace text NOT NULL,
  content_ref text NOT NULL,
  content_hash text NOT NULL,
  summary text NOT NULL,
  provenance jsonb NOT NULL,
  confidence numeric(4,3) NOT NULL CHECK (confidence BETWEEN 0 AND 1),
  classification text NOT NULL CHECK (classification IN ('PUBLIC','INTERNAL','CONFIDENTIAL','RESTRICTED')),
  acl jsonb NOT NULL,
  status text NOT NULL CHECK (status IN ('ACTIVE','SUPERSEDED','ARCHIVED','QUARANTINED')),
  valid_from timestamptz NOT NULL,
  valid_until timestamptz,
  supersedes uuid REFERENCES memory_records(memory_id),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (tenant_id, namespace, content_hash)
);

DO $$
DECLARE table_name text;
BEGIN
  FOREACH table_name IN ARRAY ARRAY[
    'workflows','tasks','task_runs','approvals','capability_grants',
    'gate_runs','audit_events','outbox_events','memory_records'
  ] LOOP
    EXECUTE format('ALTER TABLE %I ENABLE ROW LEVEL SECURITY', table_name);
    EXECUTE format('ALTER TABLE %I FORCE ROW LEVEL SECURITY', table_name);
    EXECUTE format(
      'CREATE POLICY tenant_isolation ON %I USING (tenant_id = current_setting(''app.tenant_id'', true)) WITH CHECK (tenant_id = current_setting(''app.tenant_id'', true))',
      table_name
    );
  END LOOP;
END $$;

-- The runtime role must not own these tables and must not have BYPASSRLS.
-- Migration ownership is assigned by deployment automation, not application code.
