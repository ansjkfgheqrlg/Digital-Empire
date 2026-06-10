"""Test per lib/frontmatter.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.frontmatter import split, parse, serialize


def test_split_with_frontmatter():
    text = "---\nname: test\nvalue: 42\n---\nBody here"
    fm, body = split(text)
    assert fm["name"] == "test"
    assert "Body here" in body


def test_split_no_frontmatter():
    text = "Just body, no frontmatter"
    fm, body = split(text)
    assert fm is None
    assert body == text


def test_serialize_roundtrip():
    fm = {"name": "test", "tags": ["a", "b"]}
    body = "Body content"
    text = serialize(fm, body)
    fm2, body2 = split(text)
    assert fm2["name"] == "test"
    assert "Body content" in body2
