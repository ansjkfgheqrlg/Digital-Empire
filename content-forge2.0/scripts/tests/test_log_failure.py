"""Test per scripts/log_failure.py."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))
import log_failure


def test_slugify_basic():
    assert log_failure.slugify("Hello World") == "hello-world"


def test_slugify_italian_with_accents():
    assert log_failure.slugify("Perché così") == "perche-cosi"


def test_slugify_special_chars():
    s = log_failure.slugify("ciao!@#$%^&*()world")
    assert s == "ciaoworld"


def test_slugify_max_length():
    long = "a" * 100
    assert len(log_failure.slugify(long, max_len=40)) <= 40


def test_extract_title():
    body = "# FM-005 — Mio bug\n\nContent..."
    assert log_failure.extract_title(body) == "Mio bug"


def test_extract_title_no_prefix():
    body = "# Just a title\n\nContent..."
    assert log_failure.extract_title(body) == "Just a title"


def test_extract_title_missing():
    body = "Body without header"
    assert log_failure.extract_title(body) == "(no title)"


def test_next_fm_id_with_no_existing(tmp_path, monkeypatch):
    monkeypatch.setattr(log_failure, "LOGGED_DIR", tmp_path / "logged")
    monkeypatch.setattr(log_failure, "TRIAGED_DIR", tmp_path / "triaged")
    monkeypatch.setattr(log_failure, "RESOLVED_DIR", tmp_path / "resolved")
    fm_id = log_failure.next_fm_id()
    assert fm_id == "FM-001"


def test_next_fm_id_increments(tmp_path, monkeypatch):
    monkeypatch.setattr(log_failure, "LOGGED_DIR", tmp_path / "logged")
    monkeypatch.setattr(log_failure, "TRIAGED_DIR", tmp_path / "triaged")
    monkeypatch.setattr(log_failure, "RESOLVED_DIR", tmp_path / "resolved")
    (tmp_path / "logged").mkdir()
    (tmp_path / "logged" / "FM-001-x.md").touch()
    (tmp_path / "logged" / "FM-007-y.md").touch()
    (tmp_path / "triaged").mkdir()
    (tmp_path / "triaged" / "FM-003-z.md").touch()
    fm_id = log_failure.next_fm_id()
    assert fm_id == "FM-008"


def test_estimate_total_effort():
    items = [
        (None, {"estimated_effort": "30min"}, None),
        (None, {"estimated_effort": "2h"}, None),
        (None, {"estimated_effort": "1d"}, None),
    ]
    days = log_failure.estimate_total_effort(items)
    # 0.05 + 0.25 + 1.0 = 1.30
    assert abs(days - 1.3) < 0.01


def test_parse_frontmatter_roundtrip(tmp_path):
    """Frontmatter scritto e ri-letto deve corrispondere."""
    target = tmp_path / "test.md"
    fm = {"fm_id": "FM-099", "status": "triaged", "severity": "major"}
    body = "# FM-099 — Test\n\nContent."
    log_failure.write_with_frontmatter(target, fm, body)

    fm2, body2 = log_failure.parse_frontmatter(target)
    assert fm2["fm_id"] == "FM-099"
    assert fm2["status"] == "triaged"
    assert fm2["severity"] == "major"
    assert "Test" in body2
