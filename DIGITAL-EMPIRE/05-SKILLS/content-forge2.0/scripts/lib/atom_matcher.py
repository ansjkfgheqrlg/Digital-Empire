"""Match lessicale + semantico atomo↔testo.

Usato da: scripts/coverage_check.py (C1 coverage-verifier).

Implementa due livelli:
1. **Lexical match** (sempre): cerca occorrenze del titolo dell'atomo (con normalizzazione) e dei termini chiave nel testo.
2. **Semantic match** (opzionale, se `sentence-transformers` o API embedding sono disponibili): similarità coseno tra embedding dell'atomo e finestre del testo.

Il caller (C1) può decidere quale livello usare in base a disponibilità.

Part of: content-forge / scripts/lib
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

__all__ = [
    "normalize",
    "lexical_match",
    "lexical_coverage_rate",
    "semantic_match_available",
    "semantic_coverage_rate",
]


_WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)


def normalize(text: str) -> str:
    """Normalizza per match lessicale: lowercase, no accenti, no punteggiatura extra."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def lexical_match(atom: dict, output_text: str, threshold: float = 0.5) -> dict:
    """Cerca match lessicale dell'atomo nel testo di output.

    Strategia:
    1. Match esatto del titolo (normalizzato)
    2. Match dei termini chiave della canonical_definition (>2 char, no stopword)

    Ritorna {match_type, score, evidence}.
    score 0.0 = nessun match, 1.0 = titolo presente verbatim
    """
    norm_output = normalize(output_text)
    norm_title = normalize(atom["title"])

    # 1. Titolo esatto
    if norm_title and norm_title in norm_output:
        return {
            "match_type": "title_exact",
            "score": 1.0,
            "evidence": atom["title"],
        }

    # 2. Termini chiave dal canonical_definition + title + extended_explanation
    text_sources = " ".join([
        atom.get("canonical_definition", ""),
        atom.get("title", ""),
        atom.get("extended_explanation", "")[:500],  # primi 500 char dell'extended
    ])
    terms = [t for t in _WORD_RE.findall(normalize(text_sources))
             if len(t) > 3 and t not in _ITALIAN_STOPWORDS and t not in _ENGLISH_STOPWORDS]
    if not terms:
        return {"match_type": "no_terms", "score": 0.0, "evidence": ""}

    matched = sum(1 for t in terms if t in norm_output)
    # De-duplica termini per evitare bias (es. "obiezione" che compare 10 volte)
    unique_terms = set(terms)
    unique_matched = sum(1 for t in unique_terms if t in norm_output)
    score = unique_matched / len(unique_terms) if unique_terms else 0.0

    return {
        "match_type": "term_overlap",
        "score": score,
        "evidence": f"{matched}/{len(terms)} key terms found",
    }


def lexical_coverage_rate(atoms: list[dict], output_text: str,
                          threshold: float = 0.5) -> dict:
    """Calcola coverage rate lessicale per una lista di atomi.

    Ritorna {covered, partial, missing, rate, per_atom}.
    """
    covered = 0
    partial = 0
    missing = []
    per_atom = []

    for atom in atoms:
        m = lexical_match(atom, output_text)
        per_atom.append({"atom_id": atom["id"], "title": atom["title"], **m})
        if m["score"] >= 0.55:  # was 0.8 — abbassato per contenuti italiani narrativi
            covered += 1
        elif m["score"] >= 0.3:  # was threshold — partial soglia separata
            partial += 1
        else:
            missing.append(atom["id"])

    total = len(atoms) if atoms else 1
    return {
        "total": total,
        "covered": covered,
        "partial": partial,
        "missing_count": len(missing),
        "missing_ids": missing,
        "rate": (covered + partial * 0.5) / total,
        "per_atom": per_atom,
    }


# --- Semantic match (opzionale) ---

def semantic_match_available() -> bool:
    """True se sentence-transformers è installato."""
    try:
        import sentence_transformers  # noqa: F401
        return True
    except ImportError:
        return False


def semantic_coverage_rate(atoms: list[dict], output_text: str,
                           model_name: str = "all-MiniLM-L6-v2",
                           threshold: float = 0.6) -> dict | None:
    """Calcola coverage semantica via embedding.

    Per ogni atomo, calcola cosine similarity tra l'embedding dell'atomo
    e l'embedding di ogni paragrafo del testo. Atomo "coperto" se max sim >= threshold.

    Ritorna None se sentence-transformers non installato.
    """
    try:
        from sentence_transformers import SentenceTransformer, util
    except ImportError:
        return None

    model = SentenceTransformer(model_name)

    # Spezza output in chunk
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", output_text) if p.strip()]
    if not paragraphs:
        return {"total": len(atoms), "covered": 0, "rate": 0.0, "per_atom": []}

    # Encoding batch
    para_emb = model.encode(paragraphs, convert_to_tensor=True, show_progress_bar=False)
    atom_texts = [f"{a['title']}. {a.get('canonical_definition', '')}" for a in atoms]
    atom_emb = model.encode(atom_texts, convert_to_tensor=True, show_progress_bar=False)

    sims = util.cos_sim(atom_emb, para_emb)  # [N_atoms x N_paragraphs]

    covered = 0
    per_atom = []
    missing = []
    for i, atom in enumerate(atoms):
        max_sim = float(sims[i].max().item())
        best_para_idx = int(sims[i].argmax().item())
        is_covered = max_sim >= threshold
        per_atom.append({
            "atom_id": atom["id"],
            "title": atom["title"],
            "max_similarity": round(max_sim, 3),
            "covered_semantically": is_covered,
            "best_paragraph_index": best_para_idx,
        })
        if is_covered:
            covered += 1
        else:
            missing.append(atom["id"])

    total = len(atoms) if atoms else 1
    return {
        "total": total,
        "covered": covered,
        "missing_count": len(missing),
        "missing_ids": missing,
        "rate": covered / total,
        "model": model_name,
        "threshold": threshold,
        "per_atom": per_atom,
    }


_ITALIAN_STOPWORDS = {
    "il", "la", "lo", "gli", "le", "uno", "una", "un", "del", "della", "dei", "delle",
    "che", "chi", "cui", "quale", "questo", "questa", "questi", "queste",
    "quello", "quella", "quelli", "quelle", "per", "con", "non", "sono", "essere",
    "avere", "fare", "dire", "anche", "come", "ogni", "altro", "altre", "altri", "altra",
    "molto", "molte", "molti", "alcun", "alcuni", "alcune",
}
_ENGLISH_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "for",
    "with", "by", "from", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "this", "that", "these", "those",
    "as", "at", "it", "its", "into", "than", "then", "what", "which", "who",
    "some", "any", "all", "more", "most", "other", "such", "no", "not", "only",
}
