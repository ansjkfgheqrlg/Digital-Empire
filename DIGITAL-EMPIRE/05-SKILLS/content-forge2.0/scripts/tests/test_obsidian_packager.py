"""Test per obsidian_packager.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from obsidian_packager import normalize_slugs, build_moc_categorical


def test_normalize_slugs_ok(tmp_path):
    (tmp_path / "good-slug.md").touch()
    (tmp_path / "Bad Slug.md").touch()
    issues = normalize_slugs(tmp_path, "kebab")
    assert any(i["current_slug"] == "Bad Slug" for i in issues)


def test_build_moc(tmp_path):
    (tmp_path / "concepts").mkdir()
    (tmp_path / "concepts" / "atom-1.md").touch()
    (tmp_path / "concepts" / "atom-2.md").touch()
    moc = build_moc_categorical(tmp_path, "Test")
    assert "MOC — Test" in moc
    assert "[[atom-1]]" in moc
    assert "[[atom-2]]" in moc
