"""Test per length_check.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from length_check import count_words_in_path


def test_count_words_file(tmp_path):
    f = tmp_path / "f.md"
    f.write_text("one two three four five")
    assert count_words_in_path(f) == 5


def test_count_words_dir(tmp_path):
    (tmp_path / "a.md").write_text("one two three")
    (tmp_path / "b.md").write_text("four five")
    (tmp_path / "ignored.bin").write_text("not counted")
    assert count_words_in_path(tmp_path) == 5
