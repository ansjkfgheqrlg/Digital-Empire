"""Pulizia deterministica del sorgente (timestamp, filler vocali, ripetizioni).

Used by: A1 ingestion-agent.
Part of: content-forge

Usage:
    python scripts/transcript_cleaner.py <source> --out <cleaned.md> [--language auto|it|en] [--json]
    python scripts/transcript_cleaner.py <source> --out-stdout [--json]  # cleaned su stdout, stats su stderr
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Pattern timestamp comuni (YouTube, SRT, VTT, formati custom)
TIMESTAMP_PATTERNS = [
    r"^\s*\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d{1,3})?\s*$",                # "01:23", "00:01:23.456"
    r"^\s*\[\s*\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d{1,3})?\s*\]\s*$",      # "[01:23]"
    r"^\s*\(\s*\d{1,2}:\d{2}(?::\d{2})?\s*\)\s*$",                       # "(01:23)"
    # SRT cue header: "00:00:01,000 --> 00:00:03,000"
    r"^\s*\d{2}:\d{2}:\d{2}[,.]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[,.]\d{3}\s*$",
    # SRT cue index (numero solo)
    r"^\s*\d{1,5}\s*$",
]
INLINE_TIMESTAMP_RE = re.compile(r"\[(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.,]\d+)?\]")
INLINE_TIMESTAMP_PAREN_RE = re.compile(r"\((?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.,]\d+)?\)")
# Timestamp ad inizio riga seguito da spazio + contenuto (formato YouTube tipico)
LEADING_TIMESTAMP_RE = re.compile(r"^\s*(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.,]\d+)?\s+", re.MULTILINE)

# Filler vocali (start of segment markers o stand-alone)
FILLER_PATTERNS_EN = [
    r"\b(?:um|uh|er|ah|hmm|mhm)+\b",
    r"\byou\s+know\b",
    r"\bi\s+mean\b",
    r"\bsort\s+of\b",
    r"\bkind\s+of\b",
    r"\blike,?\s+like\b",
]
FILLER_PATTERNS_IT = [
    r"\b(?:ehm|uhm|mhm|boh|cioè|tipo,?\s+tipo)+\b",
    r"\bvoglio\s+dire\b",
    r"\bdiciamo\s+(?=che|un|una)\b",
]

# Ripetizioni vocali immediate: "the, the" → "the"
IMMEDIATE_REPETITION_RE = re.compile(r"\b(\w+)(\s*,?\s+\1)+\b", re.IGNORECASE)

# Speaker labels da rimuovere (es. "Speaker 1:", "John:")
SPEAKER_LABEL_RE = re.compile(r"^[A-Z][A-Za-z ]{0,30}:\s")


def detect_language(text: str) -> str:
    """Detect lingua base sulla frequenza di stopword. Restituisce 'it', 'en', o 'other'."""
    sample = text[:5000].lower()
    it_markers = sum(sample.count(w) for w in [" il ", " la ", " che ", " di ", " un ", " una ", " per "])
    en_markers = sum(sample.count(w) for w in [" the ", " and ", " of ", " a ", " an ", " is ", " to "])
    if it_markers > en_markers * 1.5:
        return "it"
    if en_markers > it_markers * 1.5:
        return "en"
    return "auto"


def detect_source_type(text: str) -> str:
    """Heuristica per tipo di sorgente."""
    # Conta timestamp
    ts_count = sum(1 for line in text.split("\n")
                   if any(re.match(p, line) for p in TIMESTAMP_PATTERNS))
    total_lines = max(text.count("\n"), 1)
    ts_ratio = ts_count / total_lines

    if ts_ratio > 0.05:
        return "youtube_transcript"

    # Markdown structured?
    if text.count("\n## ") > 3 or text.count("\n# ") > 1:
        return "article"

    # Brief = corto, poco strutturato
    if len(text) < 5000:
        return "brief"

    return "mixed"


def remove_timestamp_lines(text: str) -> tuple[str, int]:
    """Rimuove righe che sono SOLO timestamp. Ritorna (text, count_removed)."""
    lines = text.split("\n")
    kept = []
    removed = 0
    for line in lines:
        if any(re.match(p, line) for p in TIMESTAMP_PATTERNS):
            removed += 1
            continue
        kept.append(line)
    return "\n".join(kept), removed


def remove_inline_timestamps(text: str) -> tuple[str, int]:
    """Rimuove timestamp inline tipo [01:23] o (01:23) e leading tipo '00:01:23 testo'."""
    count = len(INLINE_TIMESTAMP_RE.findall(text)) + len(INLINE_TIMESTAMP_PAREN_RE.findall(text))
    leading_matches = LEADING_TIMESTAMP_RE.findall(text)
    count += len(leading_matches)
    text = INLINE_TIMESTAMP_RE.sub("", text)
    text = INLINE_TIMESTAMP_PAREN_RE.sub("", text)
    text = LEADING_TIMESTAMP_RE.sub("", text)
    return text, count


def remove_speaker_labels(text: str) -> tuple[str, int]:
    """Rimuove label tipo 'Speaker 1:' a inizio riga."""
    lines = text.split("\n")
    count = 0
    new_lines = []
    for line in lines:
        m = SPEAKER_LABEL_RE.match(line)
        if m:
            new_lines.append(line[m.end():])
            count += 1
        else:
            new_lines.append(line)
    return "\n".join(new_lines), count


def remove_fillers(text: str, language: str) -> tuple[str, int]:
    """Rimuove filler vocali della lingua data."""
    patterns = []
    if language in ("en", "auto"):
        patterns += FILLER_PATTERNS_EN
    if language in ("it", "auto"):
        patterns += FILLER_PATTERNS_IT
    count = 0
    for pat in patterns:
        regex = re.compile(pat, re.IGNORECASE)
        matches = regex.findall(text)
        count += len(matches)
        text = regex.sub("", text)
    return text, count


def collapse_immediate_repetitions(text: str) -> tuple[str, int]:
    """Collassa 'the, the' → 'the'."""
    count = 0
    def replace(m):
        nonlocal count
        count += 1
        return m.group(1)
    text = IMMEDIATE_REPETITION_RE.sub(replace, text)
    return text, count


def normalize_whitespace(text: str) -> str:
    """Normalizza spazi multipli e righe vuote."""
    # Spazi multipli intra-riga
    text = re.sub(r"[ \t]+", " ", text)
    # Spazi prima di punteggiatura
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    # Più di 2 newline consecutive → 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Trim righe
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip() + "\n"


def normalize_markdown(text: str) -> str:
    """Normalizza markdown: heading consistenti, lista uniformi."""
    # Spazio dopo # in heading
    text = re.sub(r"^(#{1,6})([^#\s])", r"\1 \2", text, flags=re.MULTILINE)
    # Asterisks → trattini per liste
    text = re.sub(r"^(\s*)\*\s", r"\1- ", text, flags=re.MULTILINE)
    return text


def clean(text: str, language: str = "auto") -> tuple[str, dict]:
    """Pipeline completa. Ritorna (cleaned, stats)."""
    stats = {
        "original_chars": len(text),
        "original_words": len(text.split()),
        "language_detected": detect_language(text) if language == "auto" else language,
        "source_type_detected": detect_source_type(text),
    }
    effective_lang = stats["language_detected"]

    text, ts_lines = remove_timestamp_lines(text)
    text, ts_inline = remove_inline_timestamps(text)
    text, speaker_labels = remove_speaker_labels(text)
    text, fillers = remove_fillers(text, effective_lang)
    text, repetitions = collapse_immediate_repetitions(text)
    text = normalize_whitespace(text)
    text = normalize_markdown(text)

    stats.update({
        "removed_timestamp_lines": ts_lines,
        "removed_inline_timestamps": ts_inline,
        "removed_speaker_labels": speaker_labels,
        "removed_fillers": fillers,
        "collapsed_repetitions": repetitions,
        "cleaned_chars": len(text),
        "cleaned_words": len(text.split()),
        "reduction_ratio": round(1 - len(text) / max(stats["original_chars"], 1), 3),
    })
    return text, stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("source", type=Path, help="Path al file sorgente")
    parser.add_argument("--out", type=Path, help="Path output cleaned.md")
    parser.add_argument("--out-stdout", action="store_true", help="Stampa cleaned su stdout, stats su stderr")
    parser.add_argument("--language", default="auto", help="Lingua del sorgente (auto|it|en|...)")
    parser.add_argument("--json", action="store_true", help="Stampa stats JSON")
    args = parser.parse_args(argv)

    if not args.source.exists():
        print(f"ERROR: source non trovato: {args.source}", file=sys.stderr)
        return 2

    if not args.out and not args.out_stdout:
        print("ERROR: specifica --out PATH o --out-stdout", file=sys.stderr)
        return 2

    text = args.source.read_text(encoding="utf-8", errors="ignore")
    cleaned, stats = clean(text, args.language)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(cleaned, encoding="utf-8")
    if args.out_stdout:
        sys.stdout.write(cleaned)

    if args.json:
        out_stream = sys.stderr if args.out_stdout else sys.stdout
        print(json.dumps(stats, indent=2, ensure_ascii=False), file=out_stream)
    elif not args.out_stdout:
        print(f"✅ Cleaned {stats['original_words']}w → {stats['cleaned_words']}w "
              f"(reduction {stats['reduction_ratio']*100:.1f}%) | "
              f"lang={stats['language_detected']} | type={stats['source_type_detected']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
