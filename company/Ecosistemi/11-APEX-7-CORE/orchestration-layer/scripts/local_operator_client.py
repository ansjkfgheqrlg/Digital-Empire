from __future__ import annotations

import argparse
import base64
from pathlib import Path
from urllib.parse import urlparse

import httpx
from cryptography.hazmat.primitives import serialization


def session(base_url: str, operator_id: str, key_path: Path) -> str:
    host = urlparse(base_url).hostname
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise SystemExit("Local pilot client refuses non-loopback API URL")
    private = serialization.load_pem_private_key(key_path.read_bytes(), password=None)
    with httpx.Client(base_url=base_url, timeout=10) as client:
        challenge = client.post(f"/v1/auth/challenges/{operator_id}").raise_for_status().json()
        signature = private.sign(base64.b64decode(challenge["message_b64"]))
        verified = client.post(
            "/v1/auth/verify",
            json={
                "challenge_id": challenge["challenge_id"],
                "operator_id": operator_id,
                "signature_b64": base64.b64encode(signature).decode(),
            },
        ).raise_for_status().json()
        return verified["session_token"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Authenticated local OCP client")
    parser.add_argument("--url", default="http://127.0.0.1:8000")
    parser.add_argument("--operator", default="local-owner")
    parser.add_argument("--private-key", type=Path, required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("--file", action="append", required=True)
    create.add_argument("--artifact", default="adr/local.md")
    create.add_argument("--idempotency-key", required=True)
    status = sub.add_parser("status")
    status.add_argument("workflow_id")
    events = sub.add_parser("events")
    events.add_argument("workflow_id")
    args = parser.parse_args()
    token = session(args.url, args.operator, args.private_key)
    headers = {"Authorization": f"Bearer {token}"}
    with httpx.Client(base_url=args.url, headers=headers, timeout=10) as client:
        if args.command == "create":
            response = client.post(
                "/v1/workflows",
                headers={**headers, "Idempotency-Key": args.idempotency_key},
                json={
                    "workflow_type": "repository_adr",
                    "goal": "Create an evidence-linked ADR",
                    "risk_hint": "R1",
                    "skill_input": {"repository_files": args.file, "artifact_path": args.artifact},
                },
            )
        elif args.command == "status":
            response = client.get(f"/v1/workflows/{args.workflow_id}")
        else:
            response = client.get(f"/v1/workflows/{args.workflow_id}/events")
        response.raise_for_status()
        print(response.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
