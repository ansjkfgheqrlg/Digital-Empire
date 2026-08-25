from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

from .manifest import IntegrityError, PlanManifest, PlanMemoryError, PlanRecord


TOKEN_RE = re.compile(r"[\wÀ-ÿ-]+", re.UNICODE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
STOPWORDS = {
    "che", "chi", "come", "con", "dei", "del", "della", "delle", "di", "e", "gli",
    "il", "in", "la", "le", "lo", "nel", "nella", "per", "più", "quale", "quali",
    "quando", "sono", "su", "un", "una", "qual", "the", "what", "which", "with",
}
QUERY_SYNONYMS = {
    "promosso": ("promotion",), "promuovere": ("promotion",), "promozione": ("promotion",),
    "ordine": ("order",), "certificazione": ("certification",),
}


@dataclass(frozen=True)
class PlanChunk:
    chunk_id: str
    level: int
    plan_status: str
    path: str
    file_sha256: str
    heading: str
    heading_path: tuple[str, ...]
    line_start: int
    line_end: int
    text: str


@dataclass(frozen=True)
class SearchHit:
    score: float
    authoritative: bool
    citation: dict
    excerpt: str


class PlanIndex:
    """Deterministic BM25 index over immutable plan files."""

    INDEX_VERSION = "1.1"
    K1 = 1.5
    B = 0.75

    def __init__(self, root: Path, manifest: PlanManifest, chunks: tuple[PlanChunk, ...]):
        self.root = root
        self.manifest = manifest
        self.chunks = chunks
        self._terms = [Counter(self.tokenize(chunk.heading + " " + chunk.text)) for chunk in chunks]
        self._doc_lengths = [sum(counter.values()) for counter in self._terms]
        self._average_length = (
            sum(self._doc_lengths) / len(self._doc_lengths) if self._doc_lengths else 0.0
        )
        self._document_frequency: Counter[str] = Counter()
        for terms in self._terms:
            self._document_frequency.update(terms.keys())

    @staticmethod
    def tokenize(text: str) -> list[str]:
        return [
            token.casefold()
            for token in TOKEN_RE.findall(text)
            if len(token) > 1 and token.casefold() not in STOPWORDS
        ]

    @staticmethod
    def expand_query(terms: list[str]) -> list[str]:
        expanded = list(terms)
        for term in terms:
            expanded.extend(QUERY_SYNONYMS.get(term, ()))
        return list(dict.fromkeys(expanded))

    @classmethod
    def build(cls, root: Path) -> "PlanIndex":
        manifest = PlanManifest.load(root)
        chunks: list[PlanChunk] = []
        for record in manifest.records:
            chunks.extend(cls._parse_plan(root, record))
        if not chunks:
            raise PlanMemoryError("No plan chunks were produced")
        return cls(root, manifest, tuple(chunks))

    @classmethod
    def load(cls, root: Path) -> "PlanIndex":
        manifest = PlanManifest.load(root)
        path = root / "memory_store" / "index" / "plan-index.json"
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            raise PlanMemoryError(f"Invalid or missing index: {path}") from exc
        if raw.get("index_version") != cls.INDEX_VERSION:
            raise PlanMemoryError("Unsupported plan index version")
        chunks = tuple(
            PlanChunk(
                chunk_id=item["chunk_id"],
                level=int(item["level"]),
                plan_status=item["plan_status"],
                path=item["path"],
                file_sha256=item["file_sha256"],
                heading=item["heading"],
                heading_path=tuple(item["heading_path"]),
                line_start=int(item["line_start"]),
                line_end=int(item["line_end"]),
                text=item["text"],
            )
            for item in raw.get("chunks", [])
        )
        expected = {record.path: record.sha256 for record in manifest.records}
        for chunk in chunks:
            if expected.get(chunk.path) != chunk.file_sha256:
                raise IntegrityError(f"Index is stale for {chunk.path}")
        return cls(root, manifest, chunks)

    def save(self) -> Path:
        target = self.root / "memory_store" / "index" / "plan-index.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "index_version": self.INDEX_VERSION,
            "algorithm": "BM25",
            "read_only_sources": True,
            "chunks": [asdict(chunk) for chunk in self.chunks],
        }
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return target

    @classmethod
    def _parse_plan(cls, root: Path, record: PlanRecord) -> list[PlanChunk]:
        path = root / record.path
        lines = path.read_text(encoding="utf-8").splitlines()
        headings: list[str] = []
        chunks: list[PlanChunk] = []
        current_heading = "Document root"
        current_path: tuple[str, ...] = ()
        start = 1
        body: list[str] = []

        def flush(end_line: int) -> None:
            text = "\n".join(body).strip()
            if not text and current_heading == "Document root":
                return
            chunks.append(
                PlanChunk(
                    chunk_id=f"L{record.level}:{len(chunks) + 1}",
                    level=record.level,
                    plan_status=record.status,
                    path=record.path,
                    file_sha256=record.sha256,
                    heading=current_heading,
                    heading_path=current_path,
                    line_start=start,
                    line_end=max(start, end_line),
                    text=text,
                )
            )

        for number, line in enumerate(lines, start=1):
            match = HEADING_RE.match(line)
            if not match:
                body.append(line)
                continue
            flush(number - 1)
            depth = len(match.group(1))
            title = match.group(2).strip()
            headings[:] = headings[: depth - 1]
            headings.append(title)
            current_heading = title
            current_path = tuple(headings)
            start = number
            body = []
        flush(len(lines))
        return chunks

    def search(self, query: str, limit: int = 5, approved_only: bool = False) -> dict:
        self.manifest.validate()
        original_terms = self.tokenize(query)
        if not original_terms:
            return self._insufficient(query, "empty_query")
        known_terms = [term for term in original_terms if self._document_frequency.get(term, 0) > 0]
        if len(known_terms) / len(original_terms) <= 0.5:
            return self._insufficient(query, "low_query_coverage")
        query_terms = self.expand_query(original_terms)
        scored: list[tuple[float, PlanChunk]] = []
        total_docs = len(self.chunks)
        highest_approved = max(
            record.level for record in self.manifest.records if record.is_approved
        )

        for index, chunk in enumerate(self.chunks):
            if approved_only and chunk.plan_status != "APPROVED":
                continue
            score = self._bm25(query_terms, index, total_docs)
            heading_tokens = set(self.tokenize(" ".join(chunk.heading_path)))
            heading_overlap = len(set(query_terms) & heading_tokens)
            score += heading_overlap * 1.2
            authority = self.manifest.authority(
                next(record for record in self.manifest.records if record.level == chunk.level)
            )
            score *= 1.0 + authority[0] * 0.08 + authority[1] * 0.01
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda item: (item[0], item[1].level), reverse=True)
        if not scored:
            return self._insufficient(query, "no_evidence")

        hits = []
        for score, chunk in scored[: max(1, min(limit, 8))]:
            excerpt = self._excerpt(chunk.text, query_terms)
            hits.append(
                asdict(
                    SearchHit(
                        score=round(score, 5),
                        authoritative=(
                            chunk.level == highest_approved and chunk.plan_status == "APPROVED"
                        ),
                        citation={
                            "file": chunk.path,
                            "heading": chunk.heading,
                            "heading_path": list(chunk.heading_path),
                            "line_start": chunk.line_start,
                            "line_end": chunk.line_end,
                            "sha256": chunk.file_sha256,
                            "level": chunk.level,
                            "status": chunk.plan_status,
                        },
                        excerpt=excerpt,
                    )
                )
            )

        return {
            "status": "EVIDENCE_FOUND",
            "query": query,
            "authority_rule": "highest APPROVED level prevails; conflicts remain visible",
            "results": hits,
        }

    def _bm25(self, query_terms: Iterable[str], doc_index: int, total_docs: int) -> float:
        terms = self._terms[doc_index]
        doc_length = self._doc_lengths[doc_index]
        score = 0.0
        for term in query_terms:
            frequency = terms.get(term, 0)
            if not frequency:
                continue
            df = self._document_frequency[term]
            inverse = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
            normalization = frequency + self.K1 * (
                1 - self.B + self.B * doc_length / max(self._average_length, 1.0)
            )
            score += inverse * (frequency * (self.K1 + 1)) / normalization
        return score

    @staticmethod
    def _excerpt(text: str, query_terms: list[str], maximum: int = 420) -> str:
        compact = re.sub(r"\s+", " ", text).strip()
        if len(compact) <= maximum:
            return compact
        lowered = compact.casefold()
        positions = [lowered.find(term) for term in query_terms if lowered.find(term) >= 0]
        center = min(positions) if positions else 0
        start = max(0, center - maximum // 3)
        end = min(len(compact), start + maximum)
        prefix = "…" if start else ""
        suffix = "…" if end < len(compact) else ""
        return prefix + compact[start:end] + suffix

    @staticmethod
    def _insufficient(query: str, reason: str) -> dict:
        return {
            "status": "INSUFFICIENT_EVIDENCE",
            "query": query,
            "reason": reason,
            "results": [],
        }
