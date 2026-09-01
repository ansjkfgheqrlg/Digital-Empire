"""Test per coverage_check.py."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from coverage_check import collect_output_text
from lib.atom_matcher import lexical_match


def test_collect_output_text(tmp_path):
    (tmp_path / "a.md").write_text("Content A")
    (tmp_path / "b.md").write_text("Content B")
    (tmp_path / "c.txt").write_text("Content C")
    text = collect_output_text(tmp_path)
    assert "Content A" in text and "Content B" in text and "Content C" in text


def test_lexical_match_title_exact():
    atom = {"id": "a-001", "title": "Few-shot prompting", "canonical_definition": "Show examples"}
    result = lexical_match(atom, "We use few-shot prompting in our pipeline")
    assert result["score"] == 1.0


def test_lexical_match_term_overlap():
    atom = {"id": "a-002", "title": "Something else",
            "canonical_definition": "vector embedding semantic search retrieval"}
    result = lexical_match(atom, "We do vector embedding for semantic search")
    assert result["score"] > 0.5


def test_lexical_match_no_match():
    atom = {"id": "a-003", "title": "Unique concept xyz",
            "canonical_definition": "totally different unrelated stuff"}
    result = lexical_match(atom, "Lorem ipsum dolor sit amet")
    assert result["score"] < 0.3
