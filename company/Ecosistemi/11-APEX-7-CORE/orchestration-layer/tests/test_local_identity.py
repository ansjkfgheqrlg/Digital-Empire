from __future__ import annotations

import sys
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.identity.operator import IdentityError, OperatorIdentityService, OperatorRegistry


class LocalOperatorIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.private = Ed25519PrivateKey.generate()
        public = self.private.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        registry = OperatorRegistry()
        registry.register_raw_public_key("local-owner", public, {"LOCAL_OWNER", "TOKEN_ISSUER"})
        self.service = OperatorIdentityService(registry)
        self.now = datetime(2026, 8, 23, tzinfo=UTC)

    def test_signed_challenge_authenticates_operator(self) -> None:
        challenge_id, message = self.service.create_challenge("local-owner", now=self.now)
        context = self.service.verify(
            challenge_id,
            "local-owner",
            self.private.sign(message),
            now=self.now,
        )
        self.assertEqual("local-owner", context.operator_id)
        self.assertIn("TOKEN_ISSUER", context.roles)

    def test_replay_is_rejected(self) -> None:
        challenge_id, message = self.service.create_challenge("local-owner", now=self.now)
        signature = self.private.sign(message)
        self.service.verify(challenge_id, "local-owner", signature, now=self.now)
        with self.assertRaises(IdentityError):
            self.service.verify(challenge_id, "local-owner", signature, now=self.now)

    def test_expired_challenge_is_rejected(self) -> None:
        challenge_id, message = self.service.create_challenge(
            "local-owner", ttl_seconds=1, now=self.now
        )
        with self.assertRaises(IdentityError):
            self.service.verify(
                challenge_id,
                "local-owner",
                self.private.sign(message),
                now=self.now + timedelta(seconds=1),
            )

    def test_wrong_signature_and_anonymous_operator_are_rejected(self) -> None:
        challenge_id, _ = self.service.create_challenge("local-owner", now=self.now)
        wrong = Ed25519PrivateKey.generate().sign(b"wrong")
        with self.assertRaises(IdentityError):
            self.service.verify(challenge_id, "local-owner", wrong, now=self.now)
        with self.assertRaises(IdentityError):
            self.service.create_challenge("anonymous", now=self.now)


if __name__ == "__main__":
    unittest.main()
