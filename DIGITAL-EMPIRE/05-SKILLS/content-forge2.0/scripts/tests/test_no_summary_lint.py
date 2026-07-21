"""Test per no_summary_lint.py."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from no_summary_lint import lint_text


def test_finds_italian_smells(tmp_path):
    text = "Questo è un testo. In sintesi, dice che riassumendo ecc."
    fp = tmp_path / "test.md"
    fp.write_text(text)
    smells = lint_text(text, fp, ["it"])
    assert len(smells) >= 2


def test_finds_english_smells(tmp_path):
    text = "This is text. In summary, to summarize this all."
    fp = tmp_path / "test.md"
    fp.write_text(text)
    smells = lint_text(text, fp, ["en"])
    assert len(smells) >= 2


def test_legitimate_in_plan_files(tmp_path):
    """File chiamato PLAN-*.md è whitelisted."""
    text = "In sintesi, questo è ciò che faremo"
    fp = tmp_path / "PLAN-v1.md"
    fp.write_text(text)
    smells = lint_text(text, fp, ["it"])
    assert len(smells) == 0


def test_legitimate_with_context_marker(tmp_path):
    """Menzione vicino a 'evita' è whitelisted."""
    text = "Non usare frasi come 'in sintesi' nei documenti, sono anti-pattern"
    fp = tmp_path / "test.md"
    fp.write_text(text)
    smells = lint_text(text, fp, ["it"])
    # "in sintesi" è dentro una menzione legittima
    assert all(s["match"] != "in sintesi" for s in smells) or len(smells) == 0


def test_anti_patterns_md_whitelisted(tmp_path):
    text = "Vietato: 'in sintesi', 'riassumendo'"
    fp = tmp_path / "conventions/anti-patterns.md"
    fp.parent.mkdir(parents=True)
    fp.write_text(text)
    smells = lint_text(text, fp, ["it"])
    assert len(smells) == 0


def test_tldr_caught(tmp_path):
    text = "Some text\nTL;DR: a summary follows."
    fp = tmp_path / "test.md"
    fp.write_text(text)
    smells = lint_text(text, fp, ["en", "it"])
    assert any("tl" in s["match"].lower() for s in smells)
