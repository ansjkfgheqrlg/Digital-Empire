from __future__ import annotations

import argparse
import base64
import os
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a local-pilot Ed25519 operator key")
    parser.add_argument("--private-key", type=Path, required=True)
    args = parser.parse_args()
    target = args.private_key.expanduser().resolve()
    if target.exists():
        raise SystemExit(f"Refusing to overwrite {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    private = Ed25519PrivateKey.generate()
    pem = private.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(pem)
    public_raw = private.public_key().public_bytes(
        serialization.Encoding.Raw,
        serialization.PublicFormat.Raw,
    )
    print("OCP_OPERATOR_PUBLIC_KEY_B64=" + base64.b64encode(public_raw).decode())
    print(f"Private key written with mode 0600: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
