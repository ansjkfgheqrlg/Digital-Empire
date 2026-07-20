"""Test per schema_validator.py."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_validator import check_required_files, check_frontmatter


def test_check_required_files_all_present(tmp_path):
    (tmp_path / "a.md").touch()
    (tmp_path / "b.md").touch()
    issues = check_required_files(tmp_path, ["a.md", "b.md"])
    assert len(issues) == 0


def test_check_required_files_missing(tmp_path):
    (tmp_path / "a.md").touch()
    issues = check_required_files(tmp_path, ["a.md", "b.md"])
    assert len(issues) == 1
    assert issues[0]["severity"] == "error"


def test_check_frontmatter_ok(tmp_path):
    f = tmp_path / "agent.md"
    f.write_text("---\nname: my-agent\ndisplay_name: My Agent\n---\n\nbody")
    issues = check_frontmatter(f, ["name", "display_name"])
    assert len(issues) == 0


def test_check_frontmatter_missing_key(tmp_path):
    f = tmp_path / "agent.md"
    f.write_text("---\nname: my-agent\n---\nbody")
    issues = check_frontmatter(f, ["name", "display_name"])
    assert any(i["id"] == "frontmatter-missing-key-display_name" for i in issues)
