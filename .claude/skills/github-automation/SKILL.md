---
name: github-automation
description: >
  Git and GitHub workflow automation — commit, push, branch management, PR creation.
  Handles the full git lifecycle so users never need to type git commands manually.
  Adapted from claude-flow's github-automation skill for Claude Code projects with
  sync.ps1 pattern and multi-user sync (Max + Gael on Exponium).
trigger: "when user says finito/done/basta/pusha/chiudiamo or when a feature is complete"
skip: "mid-session work, exploratory changes not ready to commit"
---

# GitHub Automation

## Core Rule
**Users never type git commands.** Claude Code handles all git operations automatically.

## Commit Pattern (standard)
```bash
git add -A
git commit -m "[DATE] [USER] — [what was built/fixed, present tense]"
git push origin master
```

## Commit Message Format
```
[2026-05-29] [Max] — implement Google Maps scraper with rate limiting
[2026-05-29] [Gael] — add Canva login automation (Canva-C complete)
[2026-05-29] [Max] — fix SQLite duplicate detection in lead pipeline
```

Rules:
- Date: YYYY-MM-DD format
- User: Max or Gael (who did the work)
- Description: imperative present tense, specific (not "fix bug")

## Session End Workflow (triggered by: "finito/basta/done/pusha/chiudiamo")

```
1. git add -A
2. git commit -m "[date] [user] — [session summary]"
3. git push origin master
4. Update GIORNATA.md with session log
5. Report to user:
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Salvato su GitHub ✓
   Commit: "[message]"
   Link: https://github.com/ansjkfgheqrlg/exponium-client
   Domani quando riapri, ti dico subito dove siamo.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Sync Pattern (multi-user — Max + Gael)
```powershell
# When push fails due to remote divergence:
git pull --rebase origin master
git push origin master
```

Never use `git merge` — always rebase to keep history linear.

## Branch Strategy for Exponium
Main branch: `master`
No feature branches needed at current stage (Max and Gael work on separate directories).

Future (Cap.7+): when features get complex, introduce:
```
master
├── feature/dashboard-ui
├── feature/email-pipeline
└── feature/canva-automation  (Gael)
```

## PR Creation (future — when branching starts)
```bash
gh pr create \
  --title "[feature] short description" \
  --body "## What\n[what was built]\n## Test\n[how to test it]" \
  --base master
```

## sync.ps1 Shortcut (Exponium)
```powershell
.\sync.ps1 "description of what was done"
# Equivalent to: git add -A && git commit -m "..." && git push
```

## Anti-patterns
- **Committing .env files**: always check `.gitignore` includes `.env*`
- **Committing broken code**: run at minimum a syntax check before pushing
- **Vague commit messages**: "fix stuff", "update" → useless history
- **Skipping push at session end**: tomorrow's session starts confused
- **--force push to master**: NEVER — rewrites shared history
