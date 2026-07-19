# Test Scorecard — 2026-07-19 (final local run)

All entries below were executed in this environment. A `5/5` means every defined assertion in that test passed. It does **not** claim that unconfigured external systems were exercised.

| Test | Command / evidence | Score |
|---|---|---:|
| Python compilation | `python -m py_compile scripts/*.py tests/test_skill_tools.py` | 5/5 |
| Governance and structural validation | `validate_skill.py`: 0 errors, 0 warnings | 5/5 |
| Self-improvement loop | Validator → bounded plan → clean revalidation | 5/5 |
| Structural eval: basic swarm with memory | 4/4 assertions passed | 5/5 |
| Structural eval: meta transform knowledge pack | 4/4 assertions passed | 5/5 |
| Structural eval: full ecosystem controls | 4/4 assertions passed | 5/5 |
| Regression suite | `unittest`: 7/7 tests passed | 5/5 |
| Memory bootstrap integration | Included in unit suite; temporary target created index and checkpoint | 5/5 |
| Credential detection negative test | Included in unit suite; synthetic PAT-like value detected | 5/5 |
| GitHub Actions configuration test | Included in unit suite; required CI gates present | 5/5 |
| Git whitespace | `git diff --check` passed | 5/5 |
| Git object integrity | `git fsck --no-dangling` passed | 5/5 |

## Overall local score

**5/5** — all configured local quality gates passed.

## Not configured, therefore not scored

- GitHub remote push and live GitHub Actions execution: no token was available in this environment.
- Ruflo/AgentDB runtime execution: runtime was not configured.
- External APIs, webhooks and payment sandboxes: no safe sandbox credentials/contracts were configured.
- Browser UI, screen-reader, visual-regression and load tests: this repository has no runnable product UI/service target.

These items are explicitly **not scored**, rather than assigned an invented result.
