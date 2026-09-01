"""Pre-segmentazione NLP del testo pulito: chunking semantico + heuristics per atomi candidati.

Supporta multi-source: rispetta `FORGE_SOURCE_BOUNDARY` (chunk non spezza sorgenti).

Used by: A1 ingestion-agent (per il chunking); A2 analyst-agent (come supporto per atomi candidati, opzionale).
Part of: content-forge

Usage:
    python scripts/atomizer.py <cleaned_md> --out <chunks.json> [--max-words 2000] [--min-words 800]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.markdown_tools import word_count, extract_headings


SOURCE_BOUNDARY_RE = re.compile(
    r'<!--\s*FORGE_SOURCE_BOUNDARY\s+id="([^"]+)"\s+file="([^"]+)"\s*-->'
)


@dataclass
class Chunk:
    id: str
    start_offset: int
    end_offset: int
    title_heuristic: str
    word_count: int
    source_file_id: str
    source_file_path: str


def find_source_boundaries(text: str) -> list[dict]:
    """Identifica le posizioni dei FORGE_SOURCE_BOUNDARY.
    Ritorna lista di {id, file, marker_start, marker_end, content_start, content_end}.
    """
    boundaries = []
    matches = list(SOURCE_BOUNDARY_RE.finditer(text))
    for i, m in enumerate(matches):
        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        boundaries.append({
            "id": m.group(1),
            "file": m.group(2),
            "marker_start": m.start(),
            "marker_end": m.end(),
            "content_start": content_start,
            "content_end": content_end,
        })
    # Se non c'è boundary, tratta tutto come single source
    if not boundaries:
        boundaries.append({
            "id": "src-001",
            "file": "(single source)",
            "marker_start": 0, "marker_end": 0,
            "content_start": 0, "content_end": len(text),
        })
    return boundaries


def chunk_single_segment(text: str, base_offset: int,
                          src_id: str, src_path: str,
                          max_words: int, min_words: int,
                          chunk_counter: list[int]) -> list[Chunk]:
    """Chunking di un singolo segmento di sorgente.

    Strategia in ordine:
    1. Spezza su H1/H2 se i blocchi risultano >min_words
    2. Altrimenti finestra sliding di max_words
    3. Non spezza mai blocchi code (```...```)
    """
    chunks: list[Chunk] = []
    headings = extract_headings(text)

    # Filtra solo H1/H2 come candidati split point
    split_points = [h.offset for h in headings if h.level <= 2]
    if not split_points or split_points[0] > 0:
        split_points = [0] + split_points
    if split_points[-1] < len(text):
        split_points.append(len(text))

    # Crea segmenti tra split points
    segments = []
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i + 1]
        seg = text[start:end]
        wc = word_count(seg)
        segments.append((start, end, seg, wc))

    # Se un segmento è troppo grande, sub-chunk
    final_segments = []
    for start, end, seg, wc in segments:
        if wc <= max_words * 1.5:
            final_segments.append((start, end, seg, wc))
        else:
            # Sub-chunk per finestre di max_words
            sub_chunks = sub_chunk_by_words(seg, start, max_words)
            final_segments.extend(sub_chunks)

    # Crea Chunk objects
    for start, end, seg, wc in final_segments:
        if wc < 50:  # ignora segmenti tropo piccoli (probabilmente solo heading)
            continue
        chunk_counter[0] += 1
        # Titolo: primo H1/H2 o primi 80 char
        title = ""
        m = re.search(r"^#{1,2}\s+(.+)$", seg, re.MULTILINE)
        if m:
            title = m.group(1).strip()[:80]
        else:
            title = seg.strip()[:80].replace("\n", " ")
        chunks.append(Chunk(
            id=f"chunk-{chunk_counter[0]:03d}",
            start_offset=base_offset + start,
            end_offset=base_offset + end,
            title_heuristic=title,
            word_count=wc,
            source_file_id=src_id,
            source_file_path=src_path,
        ))
    return chunks


def sub_chunk_by_words(text: str, base_offset: int, max_words: int) -> list[tuple]:
    """Sub-chunking per parole, senza spezzare blocchi code."""
    # Identifica blocchi code per non spezzarli
    code_ranges = []
    for m in re.finditer(r"```.*?```", text, re.DOTALL):
        code_ranges.append((m.start(), m.end()))

    def in_code_block(offset: int) -> bool:
        return any(s <= offset < e for s, e in code_ranges)

    words_pos = [(m.start(), m.end()) for m in re.finditer(r"\b\w+\b", text)]
    result = []
    current_start = 0
    current_words = 0
    for ws, we in words_pos:
        current_words += 1
        if current_words >= max_words and not in_code_block(we):
            # cerca prossimo paragrafo (newline doppio)
            next_para = text.find("\n\n", we)
            if next_para == -1 or next_para > we + 500:
                cut_at = we
            else:
                cut_at = next_para
            seg = text[current_start:cut_at]
            result.append((base_offset + current_start, base_offset + cut_at, seg, current_words))
            current_start = cut_at
            current_words = 0
    if current_start < len(text):
        seg = text[current_start:]
        wc = word_count(seg)
        if wc > 0:
            result.append((base_offset + current_start, base_offset + len(text), seg, wc))
    return result


def chunk_text(text: str, max_words: int = 2000, min_words: int = 800) -> dict:
    """Pipeline completa di chunking.

    Rispetta FORGE_SOURCE_BOUNDARY: ogni chunk appartiene a UN solo source.
    """
    boundaries = find_source_boundaries(text)
    all_chunks: list[Chunk] = []
    chunk_counter = [0]

    for b in boundaries:
        segment_text = text[b["content_start"]:b["content_end"]]
        chunks = chunk_single_segment(
            segment_text,
            base_offset=b["content_start"],
            src_id=b["id"],
            src_path=b["file"],
            max_words=max_words,
            min_words=min_words,
            chunk_counter=chunk_counter,
        )
        all_chunks.extend(chunks)

    # Detect lingua dominante (basico)
    return {
        "total_chunks": len(all_chunks),
        "is_multi_source": len(boundaries) > 1 and boundaries[0]["file"] != "(single source)",
        "total_sources": len([b for b in boundaries if b["file"] != "(single source)"]),
        "chunks": [asdict(c) for c in all_chunks],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("cleaned_md", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--max-words", type=int, default=2000)
    parser.add_argument("--min-words", type=int, default=800)
    parser.add_argument("--json-stdout", action="store_true")
    args = parser.parse_args(argv)

    if not args.cleaned_md.exists():
        print(f"ERROR: file non trovato: {args.cleaned_md}", file=sys.stderr)
        return 2

    text = args.cleaned_md.read_text(encoding="utf-8", errors="ignore")
    result = chunk_text(text, args.max_words, args.min_words)
    result["source_path"] = str(args.cleaned_md)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.json_stdout:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"✅ {result['total_chunks']} chunk generati "
              f"(multi_source={result['is_multi_source']}, sources={result['total_sources']})")
        print(f"   Output: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
