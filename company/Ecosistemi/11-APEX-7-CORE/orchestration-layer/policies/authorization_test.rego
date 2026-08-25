package orchestration.authorization_test

import data.orchestration.authorization
import rego.v1

base := {
	"tenant_id": "tenant-a",
	"workflow_id": "w1",
	"task_id": "t1",
	"risk": "R1",
	"requested_capabilities": ["repo.read"],
	"skill": {"status": "ACTIVE", "capabilities": ["repo.read", "artifact.write:adr/**"]},
	"budget": {"within_limit": true},
	"plan_hash": "sha256:plan",
	"policy_hash": "sha256:policy",
}

test_low_risk_allow if {
	authorization.decision with input as base == {
		"effect": "ALLOW", "reasons": ["POL_LOW_RISK_ALLOWED"],
	}
}

test_default_deny_malformed_input if {
	authorization.decision with input as {} == {
		"effect": "DENY", "reasons": ["POL_INPUT_INVALID"],
	}
}

test_forbidden_capability_denied if {
	request := object.union(base, {"requested_capabilities": ["host.root"]})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_FORBIDDEN_CAPABILITY" in result.reasons
}

test_unknown_capability_denied if {
	request := object.union(base, {"requested_capabilities": ["network.any"]})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_UNKNOWN_CAPABILITY" in result.reasons
}

test_budget_denied if {
	request := object.union(base, {"budget": {"within_limit": false}})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_BUDGET_EXCEEDED" in result.reasons
}

test_r2_requires_approval if {
	request := object.union(base, {"risk": "R2"})
	authorization.decision with input as request == {
		"effect": "REQUIRE_APPROVAL", "reasons": ["POL_HIGH_RISK_APPROVAL_REQUIRED"],
	}
}

test_r2_valid_approval_allows if {
	approval := {
		"decision": "APPROVE", "requested_by": "author", "approved_by": "reviewer",
		"plan_hash": "sha256:plan", "policy_hash": "sha256:policy", "unexpired": true,
	}
	request := object.union(base, {"risk": "R2", "approval": approval})
	authorization.decision with input as request == {
		"effect": "ALLOW", "reasons": ["POL_APPROVAL_VALID"],
	}
}

test_same_author_approver_denied if {
	approval := {
		"decision": "APPROVE", "requested_by": "same", "approved_by": "same",
		"plan_hash": "sha256:plan", "policy_hash": "sha256:policy", "unexpired": true,
	}
	request := object.union(base, {"risk": "R2", "approval": approval})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_SEPARATION_OF_DUTIES" in result.reasons
}

test_r3_requires_step_up if {
	approval := {
		"decision": "APPROVE", "requested_by": "author", "approved_by": "reviewer",
		"plan_hash": "sha256:plan", "policy_hash": "sha256:policy", "unexpired": true,
		"step_up_mfa": false,
	}
	request := object.union(base, {"risk": "R3", "approval": approval})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_R3_STEP_UP_REQUIRED" in result.reasons
}

test_r3_valid_step_up_allows if {
	approval := {
		"decision": "APPROVE", "requested_by": "author", "approved_by": "reviewer",
		"plan_hash": "sha256:plan", "policy_hash": "sha256:policy", "unexpired": true,
		"step_up_mfa": true,
	}
	request := object.union(base, {"risk": "R3", "approval": approval})
	authorization.decision with input as request == {
		"effect": "ALLOW", "reasons": ["POL_APPROVAL_VALID"],
	}
}

test_stale_plan_hash_denied if {
	approval := {
		"decision": "APPROVE", "requested_by": "author", "approved_by": "reviewer",
		"plan_hash": "sha256:old", "policy_hash": "sha256:policy", "unexpired": true,
	}
	request := object.union(base, {"risk": "R2", "approval": approval})
	result := authorization.decision with input as request
	result.effect == "DENY"
	"POL_APPROVAL_HASH_MISMATCH" in result.reasons
}
