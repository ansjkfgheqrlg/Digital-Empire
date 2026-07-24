"""Test per transcript_cleaner.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from transcript_cleaner import (
    clean, remove_timestamp_lines, remove_inline_timestamps,
    collapse_immediate_repetitions, detect_language, detect_source_type,
)


def test_remove_timestamp_lines():
    text = "Hello\n00:01:23\nWorld\n[00:02:45]\nFoo"
    cleaned, removed = remove_timestamp_lines(text)
    assert "00:01:23" not in cleaned
    assert "[00:02:45]" not in cleaned
    assert "Hello" in cleaned
    assert "World" in cleaned
    assert "Foo" in cleaned
    assert removed == 2


def test_remove_inline_timestamps():
    text = "Foo [01:23] bar [00:45:12] baz (12:34)"
    cleaned, count = remove_inline_timestamps(text)
    assert "[01:23]" not in cleaned
    assert "[00:45:12]" not in cleaned
    assert "(12:34)" not in cleaned
    assert count >= 3


def test_collapse_repetitions():
    text = "the, the system is is the the best"
    cleaned, count = collapse_immediate_repetitions(text)
    assert "the, the" not in cleaned
    assert "is is" not in cleaned
    assert count >= 2


def test_detect_language_italian():
    text = "il sistema è la cosa più importante per il progetto di un team di sviluppo"
    assert detect_language(text) == "it"


def test_detect_language_english():
    text = "the system is the most important thing for a team of developers"
    assert detect_language(text) == "en"


def test_detect_source_type_transcript():
    text = "\n".join([f"00:0{i}:00\nsome words" for i in range(20)])
    assert detect_source_type(text) == "youtube_transcript"


def test_clean_pipeline():
    text = "00:01:23\nIt was great great work that you know was uh fine"
    cleaned, stats = clean(text, "en")
    assert "00:01:23" not in cleaned
    # 'great great' deve essere collassato a 'great'
    import re
    assert not re.search(r"\bgreat\s+great\b", cleaned)
    assert stats["original_words"] >= stats["cleaned_words"]
    assert stats["language_detected"] == "en"


def test_remove_leading_timestamps():
    """Bug found in Phase 8 smoke test: timestamp tipo '00:01:23 testo' non rimossi."""
    from transcript_cleaner import remove_inline_timestamps
    text = "00:00:01 first line content\n00:00:30 second line\n01:23:45 third line"
    cleaned, count = remove_inline_timestamps(text)
    assert "00:00:01" not in cleaned
    assert "00:00:30" not in cleaned
    assert "01:23:45" not in cleaned
    assert "first line content" in cleaned
    assert "second line" in cleaned
    assert count >= 3
