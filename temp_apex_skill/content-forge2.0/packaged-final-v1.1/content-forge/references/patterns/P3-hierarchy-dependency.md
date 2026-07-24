# P3 — Hierarchy & Dependency Mapping

> Costruisce la **gerarchia dei prerequisiti** tra atomi: chi va capito prima di chi. Alimenta il Knowledge Graph (edges di tipo `prerequisite`).

## Cosa fa

Per ogni atomo, identifica:
- Quali altri atomi sono **prerequisiti** (devi conoscerli prima).
- Quali atomi sono **dipendenti** (richiedono questo come prerequisito).
- Quali atomi sono **fratelli concettuali** (stesso livello, correlati).
- Quali atomi sono **specializzazioni** (sotto-casi).

Il risultato è un DAG (Directed Acyclic Graph) di dipendenze concettuali.

## Chi lo applica

- **A2 `analyst-agent`** annota `implied_prerequisites` come hint.
- **A3 `knowledge-graph-agent`** consolida gli hint in `edges` formali con `type: "prerequisite"`.
- **Tutti i builder** lo usano per ordinare l'output:
  - `doc-builder`: ordine dei capitoli/sezioni
  - `wiki-builder`: struttura del MOC
  - `agent-builder`: ordine delle istruzioni in "How to act"
  - `workflow-builder`: ordine degli step

## Quando applicarlo

Sempre. Anche un sorgente "narrativo" ha gerarchia concettuale implicita.

## Quando ammorbidire

- Per sorgenti con concetti **paralleli e indipendenti** (es. catalogo di N tecniche equivalenti): nessun prerequisite, solo `see_also`.
- Per sorgenti molto brevi (<10 atomi): la gerarchia può essere lineare (lista) invece di albero.

## Cuore del pattern

```python
# Tipi di edge in P3
edge_types = {
    "prerequisite": "B richiede A (impossibile capire B senza A)",
    "depends_on": "B usa A nei suoi esempi/implementazione",
    "is_a": "B è un caso di A (sub-class)",
    "part_of": "B è componente di A (whole-part)",
    "sibling_of": "A e B sono stesso livello, stesso parent",
    "see_also": "A e B sono correlati ma indipendenti",
}
```

## Algoritmo (pseudocodice)

```python
def build_hierarchy(atoms: list[dict]) -> list[dict]:
    """Per ogni atomo, infersce prerequisites/dependencies via:
    1. Analisi degli `implied_prerequisites` annotati da A2
    2. Term overlap: se A definisce 'X' e B usa 'X' nella sua definizione → A è prereq di B
    3. Citazioni esplicite ('vedi X', 'come spiegato in X', 'X è prerequisito')
    """
    edges = []
    term_index = build_term_index(atoms)  # {term → [atoms that DEFINE it]}

    for atom in atoms:
        # 2. Term overlap
        for term in extract_terms(atom["canonical_definition"]):
            defining_atoms = term_index.get(term, [])
            for d in defining_atoms:
                if d["id"] != atom["id"]:
                    edges.append({"from": d["id"], "to": atom["id"],
                                  "type": "prerequisite", "weight": 0.7})
        # 1. Hints da A2
        for hint in atom.get("implied_prerequisites", []):
            matched = match_atom_by_title(hint, atoms)
            if matched:
                edges.append({"from": matched["id"], "to": atom["id"],
                              "type": "prerequisite", "weight": 0.9})

    # Verifica no-cycle (la gerarchia deve essere DAG)
    if has_cycle(edges, [a["id"] for a in atoms]):
        edges = break_cycles(edges)  # rimuovi edge a peso più basso nei cicli

    return edges
```

## Output: topological sort per i builder

Una volta costruito il DAG, ogni builder può chiedere:

```python
from collections import defaultdict, deque

def topological_order(atoms_ids: list[str], prereq_edges: list[tuple[str,str]]) -> list[str]:
    """Kahn topological sort → ordine in cui presentare gli atomi."""
    indeg = defaultdict(int)
    adj = defaultdict(list)
    for a, b in prereq_edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque([a for a in atoms_ids if indeg[a] == 0])
    order = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return order
```

## Visualizzazione (per `kg.md`)

```
prerequisiti                  atomi base               applicazioni
─────────────────             ────────────────         ────────────────────
in-context learning  ─────►   few-shot prompting  ──►  template parametrici
                              chain-of-thought    ──►  self-consistency
                                                  ──►  tree-of-thoughts
embedding                ─►   semantic search    ──►   RAG retrieval
```

## Anti-pattern

- **Gerarchia inventata**: forzare prerequisiti che il sorgente non implica → confonde l'utente che credeva fossero indipendenti. Usa hint del sorgente, non assunzioni a priori.
- **Cicli**: A prereq B, B prereq A → impossibile per definizione. Spezza il ciclo con criterio esplicito (es. rimuovi l'edge a peso minore).
- **Tutto è prerequisito di tutto** (eccessiva connettività): inutile per ordinare. Filtra solo edges ad alto peso.

## Riferimenti

- Concept maps (Joseph D. Novak)
- Spaced repetition prerequisites (Anki shared decks community)
