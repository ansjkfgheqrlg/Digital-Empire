CREATE TABLE deletion_requests (
  request_id uuid PRIMARY KEY,
  tenant_id text NOT NULL CHECK (length(tenant_id) BETWEEN 3 AND 64),
  subject_ref_hashes jsonb NOT NULL,
  requested_by text NOT NULL,
  state text NOT NULL CHECK (state IN (
    'REQUESTED','IDENTITY_VERIFIED','IMPACT_ANALYZED','ACTIVE_DELETE',
    'INDEX_PURGE','VERIFIED','PARTIAL','CLOSED'
  )),
  systems jsonb NOT NULL DEFAULT '{}',
  evidence jsonb NOT NULL DEFAULT '[]',
  backup_expiry_at timestamptz,
  legal_hold boolean NOT NULL DEFAULT false,
  version bigint NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (tenant_id, request_id)
);

CREATE TABLE deletion_events (
  deletion_event_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  event_id uuid NOT NULL UNIQUE,
  tenant_id text NOT NULL,
  request_id uuid NOT NULL,
  sequence bigint NOT NULL,
  actor_id text NOT NULL,
  from_state text NOT NULL,
  to_state text NOT NULL,
  evidence jsonb NOT NULL,
  occurred_at timestamptz NOT NULL,
  FOREIGN KEY (tenant_id, request_id) REFERENCES deletion_requests(tenant_id, request_id),
  UNIQUE (tenant_id, request_id, sequence)
);

ALTER TABLE deletion_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE deletion_requests FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON deletion_requests
  USING (tenant_id = current_setting('app.tenant_id', true))
  WITH CHECK (tenant_id = current_setting('app.tenant_id', true));

ALTER TABLE deletion_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE deletion_events FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON deletion_events
  USING (tenant_id = current_setting('app.tenant_id', true))
  WITH CHECK (tenant_id = current_setting('app.tenant_id', true));

CREATE INDEX ix_deletion_state ON deletion_requests (tenant_id, state, updated_at);
