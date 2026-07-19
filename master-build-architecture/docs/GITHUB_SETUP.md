# GitHub and CI Configuration

## What is configured in this repository

- `.github/workflows/ci.yml` runs on pushes, pull requests and manual dispatch.
- The workflow uses Python 3.11 and runs compilation, structural validation, structural evaluations, regression tests and whitespace checks.
- The workflow uses GitHub Actions' built-in read-only `GITHUB_TOKEN`; it does not need a personal access token for CI.

## Publish current local changes safely

Do **not** paste a token into Markdown, source files, Git remotes or chat. Use an environment variable only for the current terminal session.

```bash
export GH_TOKEN='token-with-minimum-required-repository-scope'
git add .
git commit -m 'Add governance, evaluation and self-improvement controls'
git push origin HEAD:main
unset GH_TOKEN
```

If the default branch is `master`, replace `main` above. If Git asks for HTTP credentials, use the token as the password or configure GitHub CLI locally. The token must be created, rotated and revoked in GitHub—not stored by this repository.

## Required checks recommendation

In GitHub repository settings, protect the default branch and require the **Repository Quality Gates / Validate skill and regression suite** job before merge.

## Manual CI verification

```bash
python -m py_compile scripts/*.py tests/test_skill_tools.py
python scripts/validate_skill.py --root .
python scripts/run_evals.py
python -m unittest discover -s tests -v
```
