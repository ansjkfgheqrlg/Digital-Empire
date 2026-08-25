from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.privacy import DeletionRequest, DeletionState, DeletionTransitionError


class DeletionWorkflowTests(unittest.TestCase):
    def request(self) -> DeletionRequest:
        return DeletionRequest.create("delete-1", "tenant-a", ["person@example.test"], "privacy-owner")

    def advance_to_delete(self, request: DeletionRequest) -> None:
        request.transition(DeletionState.IDENTITY_VERIFIED, actor="privacy", evidence={"identity":"verified"}, expected_version=0)
        request.transition(DeletionState.IMPACT_ANALYZED, actor="privacy", evidence={"systems":["postgres","object","index"]}, expected_version=1)
        request.transition(DeletionState.ACTIVE_DELETE, actor="privacy", evidence={"approved":True}, expected_version=2)

    def test_subject_reference_is_hashed(self) -> None:
        request = self.request()
        self.assertNotIn("person@example.test", request.subject_ref_hashes)
        self.assertRegex(request.subject_ref_hashes[0], r"^sha256:[a-f0-9]{64}$")

    def test_complete_deletion_produces_valid_receipt(self) -> None:
        request = self.request()
        self.advance_to_delete(request)
        request.record_system("postgres", "DELETED", "audit://pg")
        request.record_system("object_store", "NOT_FOUND", "audit://object")
        request.transition(DeletionState.INDEX_PURGE, actor="memory", evidence={"started":True}, expected_version=3)
        request.record_system("search_index", "PURGED", "audit://index")
        request.backup_expiry_at = "2026-09-27T00:00:00+00:00"
        request.transition(DeletionState.VERIFIED, actor="privacy", evidence={"verified":True}, expected_version=4)
        request.transition(DeletionState.CLOSED, actor="privacy-owner", evidence={"closed":True}, expected_version=5)
        receipt = request.receipt()
        schema = json.loads((PROJECT / "contracts/schemas/v1/deletion-receipt.json").read_text())
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(receipt)))

    def test_cannot_verify_failed_system(self) -> None:
        request = self.request()
        self.advance_to_delete(request)
        request.record_system("postgres", "FAILED", "incident://1")
        request.transition(DeletionState.INDEX_PURGE, actor="memory", evidence={"started":True}, expected_version=3)
        request.backup_expiry_at = "2026-09-27T00:00:00+00:00"
        with self.assertRaises(DeletionTransitionError):
            request.transition(DeletionState.VERIFIED, actor="privacy", evidence={"verified":False}, expected_version=4)

    def test_legal_hold_blocks_active_delete(self) -> None:
        request = self.request()
        request.transition(DeletionState.IDENTITY_VERIFIED, actor="privacy", evidence={"identity":"verified"}, expected_version=0)
        request.transition(DeletionState.IMPACT_ANALYZED, actor="privacy", evidence={"systems":[]}, expected_version=1)
        request.legal_hold = True
        with self.assertRaises(DeletionTransitionError):
            request.transition(DeletionState.ACTIVE_DELETE, actor="privacy", evidence={"approved":True}, expected_version=2)

    def test_stale_version_and_illegal_transition_rejected(self) -> None:
        request = self.request()
        with self.assertRaises(DeletionTransitionError):
            request.transition(DeletionState.CLOSED, actor="x", evidence={"x":1}, expected_version=0)
        with self.assertRaises(DeletionTransitionError):
            request.transition(DeletionState.IDENTITY_VERIFIED, actor="x", evidence={"x":1}, expected_version=3)

    def test_receipt_before_close_rejected(self) -> None:
        with self.assertRaises(DeletionTransitionError):
            self.request().receipt()


class PrivacyMigrationTests(unittest.TestCase):
    def test_privacy_tables_force_rls(self) -> None:
        sql = (PROJECT / "migrations/versions/0002_privacy.sql").read_text()
        self.assertIn("CREATE TABLE deletion_requests", sql)
        self.assertIn("CREATE TABLE deletion_events", sql)
        self.assertEqual(2, sql.count("FORCE ROW LEVEL SECURITY"))
        self.assertIn("app.tenant_id", sql)


if __name__ == "__main__":
    unittest.main()
