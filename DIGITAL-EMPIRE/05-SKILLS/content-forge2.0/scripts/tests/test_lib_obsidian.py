"""Test per lib/obsidian.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.obsidian import slugify, check_wikilink_integrity, build_alias_index


def test_slugify_kebab():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("Perché Così") == "perche-cosi"


def test_slugify_long_truncated():
    title = "a" * 100
    assert len(slugify(title)) <= 60


def test_alias_index_from_frontmatter(tmp_path):
    note = tmp_path / "concept-a.md"
    note.write_text("---\ntitle: Concept A\naliases: [conceptA, concA]\n---\nbody")
    idx = build_alias_index(tmp_path)
    assert "concept-a" in idx
    assert "concepta" in idx
    assert "conca" in idx


def test_wikilink_integrity_broken(tmp_path):
    (tmp_path / "exists.md").write_text("body")
    (tmp_path / "src.md").write_text("Link to [[exists]] and [[missing]]")
    broken = check_wikilink_integrity(tmp_path)
    assert len(broken) == 1
    assert broken[0]["target"] == "missing"
