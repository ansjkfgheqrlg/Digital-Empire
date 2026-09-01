---
name: agent-architecture
description: >
  SPARC Phase 3 — Architecture agent. Defines system structure before writing implementation code.
  Produces: file structure, data models/schemas, function signatures, integration points.
  Gate: pseudocode must be complete before architecture. Architecture gates implementation.
trigger: "after pseudocode is written, before implementation begins"
skip: "trivial single-function implementations, config changes"
---

# Architecture Agent — SPARC Phase 3

## Role
Design the structure. Write interfaces before writing implementations.
The contract (schemas, function signatures, file tree) must be stable before any code executes.

## Architecture Outputs

### 1. File Tree
```
module-name/
├── __init__.py
├── scraper.py          ← main scraper class
├── parser.py           ← HTML/data extraction
├── storage.py          ← SQLite interface
├── humanizer.py        ← anti-detection: delays, UA rotation
└── tests/
    ├── test_scraper.py
    └── test_storage.py
```

### 2. Data Models (SQLite schemas)
```sql
-- Always define the schema FIRST, before any code
CREATE TABLE IF NOT EXISTS leads (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    email       TEXT UNIQUE,
    name        TEXT,
    company     TEXT,
    source      TEXT NOT NULL,  -- 'google_maps', 'facebook', 'linkedin', 'youtube'
    scraped_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    status      TEXT DEFAULT 'new',  -- 'new', 'contacted', 'replied', 'converted'
    bibbia_id   INTEGER  -- FK to bibbia sequence used
);
```

### 3. Function Signatures (Python)
```python
# Define signatures before implementing
class GoogleMapsScraper:
    def __init__(self, headless: bool = True, delay: float = 2.0): ...
    
    async def search(self, query: str, location: str, limit: int = 50) -> list[Lead]: ...
    
    async def extract_contact(self, business_url: str) -> dict | None: ...
    
    def _randomize_delay(self, base: float) -> float: ...

class LeadStorage:
    def __init__(self, db_path: str = "leads.db"): ...
    
    def insert(self, lead: Lead) -> bool: ...  # False if duplicate
    
    def get_uncontacted(self, limit: int = 100) -> list[Lead]: ...
    
    def mark_contacted(self, lead_id: int, bibbia_id: int) -> None: ...
```

### 4. Integration Points
```
scraper.py → storage.py → leads.db
                          ↓
                     email_pipeline.py (Cap.3)
                          ↓
                     dashboard/api/ (Cap.6)
```

## Architecture Decisions to Document
For each non-obvious decision, write WHY:
```
DECISION: SQLite over PostgreSQL
WHY: Single-machine deployment, no concurrent writes needed at 500 leads/day.
     Simpler ops (no server, just a file). Can migrate later if needed.

DECISION: Playwright over requests+BeautifulSoup
WHY: Google Maps is JS-rendered. Playwright handles dynamic content.
     Fallback: if Playwright blocked → use requests for static pages.

DECISION: Async scraping
WHY: Multiple sources run in parallel (google + facebook + linkedin).
     Sequential would be 4x slower.
```

## Exponium-Specific Architecture Patterns

### Outreach Stack
```
outreach/
├── scrapers/
│   ├── google_maps.py
│   ├── facebook_groups.py
│   ├── linkedin.py
│   └── youtube.py
├── pipeline/
│   ├── dedup.py
│   ├── validator.py
│   └── enricher.py
├── bibbia/
│   ├── sequences.py    ← email sequence templates
│   └── humanizer.py   ← personalization engine
├── storage/
│   └── leads_db.py
└── main.py            ← orchestrator
```

### Dashboard Stack (Cap.6-7)
```
dashboard/
├── app/               ← Next.js App Router
│   ├── api/
│   │   ├── leads/route.ts
│   │   └── stats/route.ts
│   ├── page.tsx        ← main dashboard
│   └── layout.tsx
├── components/
│   ├── LeadsTable.tsx
│   ├── StatCard.tsx
│   └── BibbiaPicker.tsx
└── lib/
    └── db.ts           ← SQLite via better-sqlite3
```

## Phase Gate
Before moving to Phase 4 (Implementation):
- File tree defined?
- All schemas written as SQL?
- All function signatures typed?
- Integration points mapped?
- Key decisions documented with WHY?

If yes → begin implementation (Phase 4)
