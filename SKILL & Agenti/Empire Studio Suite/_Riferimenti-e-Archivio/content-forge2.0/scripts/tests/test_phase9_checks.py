"""Test per i nuovi check Phase 9 in schema_validator.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from schema_validator import (
    check_skill_min_references,
    check_agent_canonical_files,
    run_phase9_checks,
)


# === check_skill_min_references ===

def test_skill_no_references_dir(tmp_path):
    """Skill senza references/ deve fail."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("---\nname: my-skill\n---\n# Skill")
    issues = check_skill_min_references(skill_dir)
    assert len(issues) == 1
    assert issues[0]["severity"] == "error"
    assert "missing" in issues[0]["evidence"].lower()


def test_skill_only_2_references(tmp_path):
    """Skill con 2 reference < 3 deve fail."""
    skill_dir = tmp_path / "my-skill"
    refs = skill_dir / "references"
    refs.mkdir(parents=True)
    (refs / "a.md").write_text("# A")
    (refs / "b.md").write_text("# B")
    issues = check_skill_min_references(skill_dir, min_refs=3)
    assert len(issues) == 1
    assert "2 references" in issues[0]["evidence"]


def test_skill_3_references_passes(tmp_path):
    """Skill con esattamente 3 reference passa."""
    skill_dir = tmp_path / "my-skill"
    refs = skill_dir / "references"
    refs.mkdir(parents=True)
    (refs / "a.md").write_text("# A")
    (refs / "b.md").write_text("# B")
    (refs / "c.md").write_text("# C")
    issues = check_skill_min_references(skill_dir, min_refs=3)
    assert len(issues) == 0


def test_skill_nested_references(tmp_path):
    """Reference in subdirectory contano."""
    skill_dir = tmp_path / "my-skill"
    (skill_dir / "references" / "concepts").mkdir(parents=True)
    (skill_dir / "references" / "patterns").mkdir(parents=True)
    (skill_dir / "references" / "concepts" / "a.md").write_text("# A")
    (skill_dir / "references" / "patterns" / "b.md").write_text("# B")
    (skill_dir / "references" / "patterns" / "c.md").write_text("# C")
    issues = check_skill_min_references(skill_dir, min_refs=3)
    assert len(issues) == 0


# === check_agent_canonical_files ===

def _create_agent(agent_dir: Path, files_present: list[str],
                  agent_md_words: int = 500, sp_words: int = 700,
                  playbook_convs: int = 6, failure_modes: int = 8):
    """Helper per creare un agente con file selezionati."""
    agent_dir.mkdir(parents=True, exist_ok=True)
    if "agent.md" in files_present:
        (agent_dir / "agent.md").write_text("word " * agent_md_words)
    if "system_prompt.md" in files_present:
        (agent_dir / "system_prompt.md").write_text("word " * sp_words)
    if "tools.md" in files_present:
        (agent_dir / "tools.md").write_text("# Tools")
    if "playbook.md" in files_present:
        convs = "\n".join([f"## {i+1}. happy — Conv\n\n**User**: x\n\n**Agent**: y\n" for i in range(playbook_convs)])
        (agent_dir / "playbook.md").write_text(convs)
    if "failure_modes.md" in files_present:
        rows = "\n".join([f"| fm-{i+1:03d} | failure {i} | sintomo | prev | rilevamento | recupero |" for i in range(failure_modes)])
        (agent_dir / "failure_modes.md").write_text(f"# Failure Modes\n\n| ID | F | S | P | R | Re |\n|----|---|---|---|---|----|\n{rows}")
    if "eval_cases.json" in files_present:
        (agent_dir / "eval_cases.json").write_text('{"cases": []}')
    if "README.md" in files_present:
        (agent_dir / "README.md").write_text("# README")


def test_agent_all_7_files_pass(tmp_path):
    """Agente con tutti i 7 file canonici passa."""
    agent_dir = tmp_path / "my-agent"
    all_files = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    _create_agent(agent_dir, all_files)
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    assert len(issues) == 0, f"Expected no issues, got: {issues}"


def test_agent_only_3_files_fails(tmp_path):
    """Agente con solo 3/7 file fail."""
    agent_dir = tmp_path / "my-agent"
    _create_agent(agent_dir, ["agent.md", "system_prompt.md", "README.md"])
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    assert len(issues) >= 1
    file_count_issue = [i for i in issues if "files-" in i["id"]]
    assert len(file_count_issue) == 1


def test_agent_md_too_short(tmp_path):
    """Agente con agent.md < 400 parole fail."""
    agent_dir = tmp_path / "my-agent"
    all_files = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    _create_agent(agent_dir, all_files, agent_md_words=200)  # troppo corto
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    word_issues = [i for i in issues if "min-400w" in i["id"]]
    assert len(word_issues) == 1


def test_agent_sp_too_long(tmp_path):
    """Agente con SP > 1500 parole warning."""
    agent_dir = tmp_path / "my-agent"
    all_files = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    _create_agent(agent_dir, all_files, sp_words=2000)
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    max_issues = [i for i in issues if "max-1500w" in i["id"]]
    assert len(max_issues) == 1
    assert max_issues[0]["severity"] == "warning"


def test_playbook_too_few_conversations(tmp_path):
    """Playbook con < 5 conversazioni fail."""
    agent_dir = tmp_path / "my-agent"
    all_files = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    _create_agent(agent_dir, all_files, playbook_convs=3)  # solo 3
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    pb_issues = [i for i in issues if "playbook-min" in i["id"]]
    assert len(pb_issues) == 1


def test_failure_modes_too_few(tmp_path):
    """failure_modes.md con < 7 entry fail."""
    agent_dir = tmp_path / "my-agent"
    all_files = ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                 "failure_modes.md", "eval_cases.json", "README.md"]
    _create_agent(agent_dir, all_files, failure_modes=4)  # solo 4
    issues = check_agent_canonical_files(agent_dir, min_files=5)
    fm_issues = [i for i in issues if "failure-modes-min" in i["id"]]
    assert len(fm_issues) == 1


# === run_phase9_checks (integration) ===

def test_run_phase9_checks_clean_output(tmp_path):
    """Output sintatticamente valido senza skill/agent → no issues."""
    (tmp_path / "doc.md").write_text("# Document")
    issues = run_phase9_checks("doc", tmp_path)
    assert issues == []


def test_run_phase9_checks_finds_thin_skill(tmp_path):
    """Output con skill magra → detect."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("---\nname: my-skill\n---\n# Thin skill")
    # no references/ → fail
    issues = run_phase9_checks("skill", tmp_path)
    assert len(issues) >= 1
    assert any("min-3-refs" in i["id"] or "no-references" in i["id"] for i in issues)


def test_run_phase9_checks_finds_thin_agent(tmp_path):
    """Output con agent magro → detect."""
    agent_dir = tmp_path / "my-agent"
    _create_agent(agent_dir, ["agent.md", "system_prompt.md"])  # solo 2 file
    issues = run_phase9_checks("agent", tmp_path)
    assert len(issues) >= 1
