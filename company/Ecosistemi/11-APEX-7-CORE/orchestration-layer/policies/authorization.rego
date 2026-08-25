package orchestration.authorization

import rego.v1

default decision := {"effect": "DENY", "reasons": ["POL_DEFAULT_DENY"]}

forbidden_capabilities := {"host.root", "secrets.read_all", "policy.write", "grant.issue"}

has_required_shape if {
	is_string(input.tenant_id)
	is_string(input.workflow_id)
	is_string(input.task_id)
	input.risk in {"R0", "R1", "R2", "R3"}
	is_array(input.requested_capabilities)
	is_object(input.skill)
	is_object(input.budget)
}

capability_forbidden(capability) if capability in forbidden_capabilities

capability_unknown(capability) if not capability in input.skill.capabilities

deny_reasons contains "POL_INPUT_INVALID" if not has_required_shape

deny_reasons contains "POL_SKILL_NOT_ACTIVE" if {
	has_required_shape
	input.skill.status != "ACTIVE"
}

deny_reasons contains "POL_BUDGET_EXCEEDED" if {
	has_required_shape
	input.budget.within_limit != true
}

deny_reasons contains "POL_FORBIDDEN_CAPABILITY" if {
	has_required_shape
	some capability in input.requested_capabilities
	capability_forbidden(capability)
}

deny_reasons contains "POL_UNKNOWN_CAPABILITY" if {
	has_required_shape
	some capability in input.requested_capabilities
	capability_unknown(capability)
}

deny_reasons contains "POL_EMPTY_CAPABILITY_SET" if {
	has_required_shape
	count(input.requested_capabilities) == 0
}

deny_reasons contains "POL_SEPARATION_OF_DUTIES" if {
	input.risk in {"R2", "R3"}
	is_object(input.approval)
	input.approval.requested_by == input.approval.approved_by
}

deny_reasons contains "POL_APPROVAL_HASH_MISMATCH" if {
	input.risk in {"R2", "R3"}
	is_object(input.approval)
	input.approval.plan_hash != input.plan_hash
}

deny_reasons contains "POL_POLICY_HASH_MISMATCH" if {
	input.risk in {"R2", "R3"}
	is_object(input.approval)
	input.approval.policy_hash != input.policy_hash
}

deny_reasons contains "POL_APPROVAL_EXPIRED" if {
	input.risk in {"R2", "R3"}
	is_object(input.approval)
	input.approval.unexpired != true
}

deny_reasons contains "POL_R3_STEP_UP_REQUIRED" if {
	input.risk == "R3"
	is_object(input.approval)
	input.approval.step_up_mfa != true
}

approval_valid if {
	input.risk in {"R2", "R3"}
	is_object(input.approval)
	input.approval.decision == "APPROVE"
	input.approval.requested_by != input.approval.approved_by
	input.approval.plan_hash == input.plan_hash
	input.approval.policy_hash == input.policy_hash
	input.approval.unexpired == true
	input.risk != "R3"
}

approval_valid if {
	input.risk == "R3"
	is_object(input.approval)
	input.approval.decision == "APPROVE"
	input.approval.requested_by != input.approval.approved_by
	input.approval.plan_hash == input.plan_hash
	input.approval.policy_hash == input.policy_hash
	input.approval.unexpired == true
	input.approval.step_up_mfa == true
}

decision := {"effect": "DENY", "reasons": sort([reason | reason := deny_reasons[_]])} if {
	count(deny_reasons) > 0
}

decision := {"effect": "ALLOW", "reasons": ["POL_LOW_RISK_ALLOWED"]} if {
	count(deny_reasons) == 0
	input.risk in {"R0", "R1"}
}

decision := {"effect": "REQUIRE_APPROVAL", "reasons": ["POL_HIGH_RISK_APPROVAL_REQUIRED"]} if {
	count(deny_reasons) == 0
	input.risk in {"R2", "R3"}
	not approval_valid
}

decision := {"effect": "ALLOW", "reasons": ["POL_APPROVAL_VALID"]} if {
	count(deny_reasons) == 0
	approval_valid
}
