# Local secure pilot

The pilot image now contains four entry points:

- `ocp-api` — loopback/container-scoped authenticated API;
- `ocp-worker` — PostgreSQL task worker using LocalRuntime;
- `ocp-outbox` — local JSON outbox sink;
- `ocp-local-slice` — direct CLI baseline.

Generate an Ed25519 operator key outside the repository and export only its public key:

```bash
python scripts/bootstrap_local_operator.py --private-key ~/.config/ocp/operator.pem
export OCP_OPERATOR_PUBLIC_KEY_B64='...'
docker compose -f deploy/compose/docker-compose.yml up
```

This remains a local R0/R1 pilot. R2, R3, RuFlo execution and Internet exposure are disabled. The Compose password is a local placeholder; production requires separate runtime/migration identities and a secret manager.
