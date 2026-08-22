# M3 quarantine area

Only the public signer/trust response described by
`../contracts/release/NS-A-v22-M3-RESPONSE.schema.json` may enter this directory.

Forbidden:

- private keys, signing seeds, mnemonic phrases or passwords;
- unapproved bundles, locks or active trust configuration;
- production credentials;
- activation or deployment commands.

The expected response filename is `NS-A-v22-M3-signer-trust-response.json`. Its
presence alone proves nothing: `../scripts/verify_m3_response.py` must pass before
any candidate bundle is considered.
