# Master App Builder Skill

A reusable, Italian-first skill prompt for building software applications methodically, with Python-first defaults.

## Contents

- `SKILL.md` — the complete skill, ready to use.
- `docs/SRS.md` — scope and acceptance criteria for this skill.
- `scripts/session_bootstrap.py` — environment verification utility.

## Use

Copy the content of `SKILL.md` into the target agent's skill/instructions configuration. It is platform-neutral and does not assume a particular IDE, repository host, or deployment provider.

## Validation

```bash
python scripts/session_bootstrap.py
```
