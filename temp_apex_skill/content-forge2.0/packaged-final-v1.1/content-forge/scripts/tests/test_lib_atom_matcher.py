"""Test per lib/atom_matcher.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.atom_matcher import normalize, lexical_match, lexical_coverage_rate


def test_normalize_basic():
    assert normalize("Ciao! Mondo.") == "ciao mondo"


def test_normalize_accents():
    assert normalize("perché è così") == "perche e cosi"


def test_lexical_coverage_high():
    atoms = [
        {"id": "a-1", "title": "Foo Bar", "canonical_definition": "Foo bar baz qux"},
        {"id": "a-2", "title": "Hello World", "canonical_definition": "greeting message"},
    ]
    output = "Foo Bar is here and Hello World too"
    result = lexical_coverage_rate(atoms, output)
    assert result["rate"] >= 0.9


def test_lexical_coverage_low():
    atoms = [{"id": "a-1", "title": "Unique XYZ", "canonical_definition": "totally unrelated"}]
    output = "lorem ipsum dolor"
    result = lexical_coverage_rate(atoms, output)
    assert result["rate"] < 0.5
