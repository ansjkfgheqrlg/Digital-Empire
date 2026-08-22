"""Ed25519 verification adapter for signed constitution bundles."""

from __future__ import annotations

from collections.abc import Collection, Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


class Ed25519TrustStoreVerifier:
    """Read-only trust store.

    The adapter intentionally exposes verification only. Production private keys and
    signing authority belong to an external release/signing boundary.
    """

    def __init__(
        self,
        public_keys: Mapping[str, bytes],
        *,
        revoked_key_ids: Collection[str] = (),
    ) -> None:
        revoked = frozenset(revoked_key_ids)
        self._keys: dict[str, Ed25519PublicKey] = {}
        for key_id, raw_key in public_keys.items():
            if not key_id.strip():
                raise ValueError("key_id cannot be empty")
            public_key = Ed25519PublicKey.from_public_bytes(raw_key)
            if key_id not in revoked:
                self._keys[key_id] = public_key

    def verify(self, *, key_id: str, message: bytes, signature: bytes) -> bool:
        key = self._keys.get(key_id)
        if key is None:
            return False
        try:
            key.verify(signature, message)
        except (InvalidSignature, ValueError):
            return False
        return True
