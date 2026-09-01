---
name: agent-researcher
description: >
  Research agent — explores the codebase and external references before implementation.
  Answers: what already exists, what patterns are in use, what dependencies are available,
  what could break. Always run BEFORE architect and coder agents in a SPARC workflow.
trigger: "before starting any implementation in an unfamiliar area or at the start of a chapter"
skip: "continuing work already well-understood from previous session"
---

# Research Agent

## Role
Explore before building. Never assume what exists — verify it.
Research is the antidote to "I thought it was there" bugs.

## Research Checklist (run at start of each chapter)

### Codebase Research
- [ ] Read existing files in the relevant directory
- [ ] Check for existing utilities that could be reused
- [ ] Verify import patterns used in the project
- [ ] Identify what's already wired up vs. what needs to be created

### Dependency Research
- [ ] What Python/Node packages are already installed?
- [ ] What version constraints exist?
- [ ] Are there known breaking changes in the required versions?

### Pattern Research (from memory)
- [ ] Has a similar problem been solved in a previous session?
- [ ] Check GIORNATA.md for relevant past solutions
- [ ] Check wiki/patterns/ if Second Brain exists

### External Research (for scrapers specifically)
- [ ] What's the current structure of the target website?
- [ ] What anti-scraping measures are in place?
- [ ] What selectors are reliable vs. likely to change?
- [ ] Are there rate limits or ToS concerns?

## Research Output Template
```markdown
## RESEARCH FINDINGS — [Feature]

### Existing Code
- [file]: [what it does, what's relevant]
- [file]: [what it does, what's relevant]

### Reusable Components
- [component]: [where it is, how to use it]

### Dependencies Available
- [package]: [version, relevant capabilities]

### Patterns from Memory
- [pattern]: [location, how to apply]

### Risks / Watch Out For
- [risk 1]: [what could go wrong, mitigation]
- [risk 2]: [what could go wrong, mitigation]

### Unknowns (need more research)
- [question]: [how to resolve before coding]
```

## For Exponium Research

### Before starting a scraper (Cap.2)
```
Research checklist:
1. Read existing outreach/ directory structure
2. Check if any base scraper class exists to extend
3. Test target website: load the page, check if JS-rendered
4. Identify stable CSS selectors (avoid dynamic class names)
5. Check for CAPTCHA or bot detection
6. Verify Playwright can reach the site in headless mode
```

### Before starting email pipeline (Cap.3)
```
Research checklist:
1. Read the Bibbia document (Max provides this)
2. Understand the sequence structure (n emails, timing, variants)
3. Check if SMTP library is already configured
4. Verify SPF/DKIM setup for the sending domain
```

### Before dashboard (Cap.6)
```
Research checklist:
1. Check existing Next.js setup (or create fresh)
2. Verify SQLite access from Node.js (better-sqlite3)
3. Check Tailwind config
4. Review data schema to understand what API needs to return
```
