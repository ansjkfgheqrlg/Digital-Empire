"""Test per package_target.py."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from package_target import copy_artifact, write_handoff_readme


def test_copy_artifact(tmp_path):
    src = tmp_path / "my-agent"
    src.mkdir()
    (src / "agent.md").write_text("content")
    out = tmp_path / "packaged"
    out.mkdir()
    dest = copy_artifact(src, out)
    assert dest.exists()
    assert (dest / "agent.md").exists()


def test_handoff_readme(tmp_path):
    readme = write_handoff_readme(tmp_path, "my-agent", has_mkd_bonus=True, qa_summary=None)
    text = readme.read_text()
    assert "my-agent" in text
    assert "master-knowledge-document" in text
