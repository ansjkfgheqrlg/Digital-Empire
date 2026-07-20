"""Test per lib/kg_loader.py."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from lib.kg_loader import KG, load_kg, topological_atoms


SAMPLE_KG = {
    "version": "1.0",
    "generated_at": "2025-05-23T10:00:00",
    "source_meta": {"path": "test.md", "word_count": 1000, "language": "it"},
    "stats": {"atom_count": 3, "cluster_count": 1, "edge_count": 2},
    "atoms": [
        {"id": "a-001", "title": "Concept A", "category": "concept",
         "canonical_definition": "First", "cluster_id": "c-001", "tags": []},
        {"id": "a-002", "title": "Concept B", "category": "concept",
         "canonical_definition": "Second", "cluster_id": "c-001", "tags": []},
        {"id": "a-003", "title": "Concept C", "category": "concept",
         "canonical_definition": "Third", "cluster_id": "c-001", "tags": []},
    ],
    "clusters": [
        {"id": "c-001", "label": "Main", "atom_ids": ["a-001", "a-002", "a-003"]},
    ],
    "edges": [
        {"from": "a-001", "to": "a-002", "type": "prerequisite", "weight": 0.9},
        {"from": "a-002", "to": "a-003", "type": "prerequisite", "weight": 0.8},
    ],
    "gaps": [],
}


def test_load_kg(tmp_path):
    kg_file = tmp_path / "kg.json"
    kg_file.write_text(json.dumps(SAMPLE_KG))
    kg = load_kg(kg_file)
    assert len(kg) == 3
    assert kg.atom("a-001")["title"] == "Concept A"


def test_load_kg_missing_field(tmp_path):
    kg_file = tmp_path / "kg.json"
    kg_file.write_text(json.dumps({"atoms": []}))  # mancano clusters, edges
    import pytest
    with pytest.raises(ValueError):
        load_kg(kg_file)


def test_topological_sort():
    kg = KG(SAMPLE_KG)
    order = topological_atoms(kg)
    assert order.index("a-001") < order.index("a-002")
    assert order.index("a-002") < order.index("a-003")


def test_prerequisites():
    kg = KG(SAMPLE_KG)
    prereqs = kg.prerequisites("a-002")
    assert len(prereqs) == 1
    assert prereqs[0]["id"] == "a-001"


def test_atoms_in_cluster():
    kg = KG(SAMPLE_KG)
    atoms = kg.atoms_in_cluster("c-001")
    assert len(atoms) == 3
