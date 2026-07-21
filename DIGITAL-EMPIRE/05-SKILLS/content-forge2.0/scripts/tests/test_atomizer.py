"""Test per atomizer.py."""
import sys, json, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from atomizer import find_source_boundaries, chunk_text


def test_no_boundary_treated_as_single_source():
    text = "Just some text without boundaries."
    boundaries = find_source_boundaries(text)
    assert len(boundaries) == 1
    assert boundaries[0]["file"] == "(single source)"


def test_with_boundaries():
    text = '<!-- FORGE_SOURCE_BOUNDARY id="src-001" file="a.md" -->\nContent A\n<!-- FORGE_SOURCE_BOUNDARY id="src-002" file="b.md" -->\nContent B'
    boundaries = find_source_boundaries(text)
    assert len(boundaries) == 2
    assert boundaries[0]["id"] == "src-001"
    assert boundaries[1]["id"] == "src-002"


def test_chunk_text_basic():
    text = "## Heading 1\n" + ("Word " * 1000) + "\n## Heading 2\n" + ("Other " * 500)
    result = chunk_text(text, max_words=500, min_words=100)
    assert result["total_chunks"] >= 1
    assert all("chunk-" in c["id"] for c in result["chunks"])
