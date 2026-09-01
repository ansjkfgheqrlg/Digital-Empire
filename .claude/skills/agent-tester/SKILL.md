---
name: agent-tester
description: >
  Testing agent — writes and runs tests for every non-trivial implementation.
  Covers: unit tests (pytest/jest), integration tests, smoke tests.
  Run after implementation, before reviewer. No code ships without at least a smoke test.
trigger: "after implementation is complete, before agent-reviewer"
skip: "pure documentation, config files, boilerplate stubs"
---

# Tester Agent

## Role
Write tests that prove the code works. Then run them.
If tests don't exist, the code isn't done.

## Test Pyramid for Exponium

### Level 1 — Unit Tests (fast, isolated)
Test individual functions with known inputs:
```python
def test_dedup_rejects_duplicate_email():
    db = LeadStorage(":memory:")  # in-memory for speed
    lead = Lead(email="test@example.com", name="Test", source="maps")
    assert db.insert(lead) == True   # first insert succeeds
    assert db.insert(lead) == False  # duplicate rejected
```

### Level 2 — Integration Tests (slower, real components)
Test components working together:
```python
async def test_scraper_writes_to_db():
    db = LeadStorage(":memory:")
    scraper = GoogleMapsScraper(headless=True)
    leads = await scraper.search("dentista", "Milano", limit=10)
    for lead in leads:
        db.insert(lead)
    assert db.count() >= 10
```

### Level 3 — Smoke Tests (full E2E, once per feature)
Test the full flow works end-to-end:
```python
def test_full_outreach_pipeline():
    # Scrape → Store → Enrich → Send (dry run)
    result = run_pipeline(dry_run=True, limit=5)
    assert result.scraped >= 5
    assert result.stored >= 5
    assert result.errors == 0
```

## Test File Structure
```
tests/
├── unit/
│   ├── test_leads_db.py
│   ├── test_dedup.py
│   └── test_email_template.py
├── integration/
│   ├── test_scraper_pipeline.py
│   └── test_dashboard_api.py
└── smoke/
    └── test_full_pipeline.py
```

## Quick Test Templates

### Python (pytest)
```python
import pytest
from outreach.storage.leads_db import LeadStorage, Lead

@pytest.fixture
def db():
    """In-memory DB, fresh for each test"""
    return LeadStorage(":memory:")

def test_insert_returns_true_for_new_lead(db):
    lead = Lead(email="new@test.com", source="google_maps")
    assert db.insert(lead) is True

def test_insert_returns_false_for_duplicate(db):
    lead = Lead(email="dup@test.com", source="google_maps")
    db.insert(lead)
    assert db.insert(lead) is False

def test_get_uncontacted_returns_new_leads(db):
    for i in range(5):
        db.insert(Lead(email=f"lead{i}@test.com", source="maps"))
    results = db.get_uncontacted(limit=10)
    assert len(results) == 5
    assert all(l.status == 'new' for l in results)
```

### JavaScript (Jest + Next.js API)
```javascript
import { GET } from '@/app/api/leads/route'
import { NextRequest } from 'next/server'

test('GET /api/leads returns array', async () => {
  const req = new NextRequest('http://localhost/api/leads')
  const res = await GET(req)
  const data = await res.json()
  expect(Array.isArray(data.leads)).toBe(true)
  expect(res.status).toBe(200)
})
```

## Running Tests
```bash
# Python
pytest tests/ -v

# JavaScript
npm test

# Specific file
pytest tests/unit/test_leads_db.py -v
```

## Minimum Test Requirement (per chapter)
- Cap.1: DB schema creates correctly, basic CRUD works
- Cap.2A-2D: Each scraper returns ≥1 lead without error
- Cap.3: Email template renders with correct personalization
- Cap.4: Humanizer applies delays within expected range
- Cap.6-7: API endpoints return correct status codes and data shapes
- Cap.9: Pattern storage and retrieval works (key-value + semantic)
