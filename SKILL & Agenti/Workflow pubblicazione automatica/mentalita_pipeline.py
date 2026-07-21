#!/usr/bin/env python3
"""Pipeline S4 per Mentalità Brutale.

Orchestra il motore carousel-factory senza modificarlo:
  input JSON -> QA deterministico -> render opzionale -> scheduler -> report.

Il default è sempre dry-run. La pubblicazione reale richiede esplicitamente
``--publish`` e un adapter configurato; nessuna credenziale è salvata nel repo.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
FACTORY = REPO / "Workfolw crea caroselli à" / "carousel-factory"
BRAND = "mentalita-brutale"
STATE = ROOT / "state"
REPORTS = ROOT / "reports"
FORBIDDEN = ("credi in te stesso", "vai avanti sempre", "secondo me", "forse funziona")
ALLOWED_TYPES = {"hook-cover", "text-statement", "list-items", "diagram", "quote-block", "cta-finale"}


@dataclass
class Finding:
    level: str
    code: str
    message: str


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"impossibile leggere {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path}: il JSON deve essere un oggetto")
    return value


def qa_carousel(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        data = load_json(path)
    except ValueError as exc:
        return [Finding("error", "JSON_INVALID", str(exc))]

    if data.get("brand") != BRAND:
        findings.append(Finding("error", "BRAND_MISMATCH", f"brand atteso {BRAND!r}, trovato {data.get('brand')!r}"))
    title = str(data.get("titolo", "")).strip()
    if not title:
        findings.append(Finding("error", "TITLE_EMPTY", "titolo mancante"))
    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        return findings + [Finding("error", "SLIDES_EMPTY", "slides deve essere una lista non vuota")]
    if len(slides) > 10:
        findings.append(Finding("error", "SLIDES_LIMIT", f"{len(slides)} slide: Instagram ne consente al massimo 10"))
    numbers: list[int] = []
    all_text = ""
    for index, slide in enumerate(slides, 1):
        if not isinstance(slide, dict):
            findings.append(Finding("error", "SLIDE_OBJECT", f"slide {index}: oggetto atteso"))
            continue
        number = slide.get("numero")
        if not isinstance(number, int):
            findings.append(Finding("error", "SLIDE_NUMBER", f"slide {index}: numero intero mancante"))
        else:
            numbers.append(number)
        kind = slide.get("tipo")
        if kind not in ALLOWED_TYPES:
            findings.append(Finding("error", "SLIDE_TYPE", f"slide {index}: tipo non supportato {kind!r}"))
        text = " ".join(str(slide.get(key, "")) for key in ("testo_piccolo", "testo_grande", "testo_accent"))
        if not text.strip() and not slide.get("items") and not slide.get("nodi"):
            findings.append(Finding("error", "SLIDE_EMPTY", f"slide {index}: nessun contenuto"))
        all_text += " " + text.lower()
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        findings.append(Finding("error", "SLIDE_SEQUENCE", f"numerazione non consecutiva: {numbers}"))
    caption = str(data.get("caption", "")).strip()
    if not caption:
        findings.append(Finding("error", "CAPTION_EMPTY", "caption mancante"))
    if "link in bio" not in (caption + " " + all_text).lower():
        findings.append(Finding("warning", "CTA_MISSING", "nessuna CTA 'link in bio' rilevata"))
    for phrase in FORBIDDEN:
        if phrase in (caption + " " + all_text).lower():
            findings.append(Finding("error", "COPY_FORBIDDEN", f"formula vietata: {phrase!r}"))
    return findings


def qa_batch(input_dir: Path) -> dict[str, Any]:
    files = sorted(input_dir.glob("*.json"))
    results = []
    for path in files:
        findings = qa_carousel(path)
        results.append({"file": str(path), "ok": not any(f.level == "error" for f in findings), "findings": [asdict(f) for f in findings]})
    return {"generated_at": now(), "input_dir": str(input_dir), "total": len(results), "passed": sum(r["ok"] for r in results), "results": results}


def render(path: Path) -> None:
    script = FACTORY / "scripts" / "generate.js"
    if not script.exists():
        raise RuntimeError(f"carousel-factory non trovato: {script}")
    subprocess.run(["node", str(script), str(path)], cwd=FACTORY, check=True)


def load_state() -> dict[str, Any]:
    path = STATE / "published.json"
    if not path.exists():
        return {}
    return load_json(path)


def save_state(state: dict[str, Any]) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / "published.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def schedule_dry_run(path: Path, output_dir: Path) -> dict[str, Any]:
    """Prepara un piano pubblicabile, senza chiamare Instagram/Meta."""
    data = load_json(path)
    images = sorted(output_dir.glob("slide-*.png"))
    return {
        "mode": "dry-run",
        "carousel": path.stem,
        "title": data.get("titolo", ""),
        "slides": len(images),
        "images": [str(p) for p in images],
        "caption": data.get("caption", ""),
        "requires": "public HTTPS image URLs and an explicitly configured publisher",
    }


def run(args: argparse.Namespace) -> int:
    input_dir = Path(args.input).resolve()
    report = qa_batch(input_dir)
    REPORTS.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS / f"qa-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"QA: {report['passed']}/{report['total']} pass — {report_path}")
    if report["passed"] != report["total"]:
        return 2
    if args.qa_only:
        return 0
    for item in report["results"]:
        source = Path(item["file"])
        if args.render:
            render(source)
        # Il renderer crea output con data+slug: il piano reale resta separato e non marca pubblicato.
        print(f"READY: {source.name}")
    if args.publish:
        print("ERRORE: publisher reale non attivato in questa build; usare un adapter approvato e URL HTTPS pubblici.", file=sys.stderr)
        return 3
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(FACTORY / "input"), help="cartella dei JSON carousel")
    parser.add_argument("--qa-only", action="store_true")
    parser.add_argument("--render", action="store_true", help="invoca generate.js dopo il QA")
    parser.add_argument("--publish", action="store_true", help="bloccato intenzionalmente: nessun post senza adapter esplicito")
    args = parser.parse_args()
    try:
        return run(args)
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERRORE: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
