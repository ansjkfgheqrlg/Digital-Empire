from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

from .config import OS_ROOT
from .models import ContentManifest, GateResult, SUPPORTED_FORMATS

REQUIRED_GATES = ("format", "brand", "copy", "rights", "safety")


def _policy() -> dict:
    path = OS_ROOT / "config" / "quality-gates.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _asset_suffix(path_or_url: str) -> str:
    parsed = urlparse(path_or_url)
    source = parsed.path if parsed.scheme else path_or_url
    return Path(source).suffix.lower()


def validate_manifest(manifest: ContentManifest, *, for_live: bool = False) -> list[GateResult]:
    policy = _policy()["blocking_gates"]
    results: list[GateResult] = []

    def add(gate: str, ok: bool, good: str, bad: str) -> None:
        results.append(GateResult(gate, "PASS" if ok else "FAIL", good if ok else bad))

    add("identity", bool(manifest.content_id), "content_id presente", "content_id mancante")
    add("brand", manifest.brand == "mentalita-brutale", "brand canonico", "brand deve essere mentalita-brutale")
    add("format", manifest.format in SUPPORTED_FORMATS, "formato supportato", f"formato non supportato: {manifest.format}")
    add("copy", 0 < len(manifest.caption) <= policy["format"]["caption_max_chars"],
        f"caption {len(manifest.caption)} caratteri", "caption vuota o oltre 2200 caratteri")

    media_count = len(manifest.media)
    expected_count = (
        1 if manifest.format in {"IMAGE", "REEL"}
        else policy["format"]["carousel_items_min"] <= media_count <= policy["format"]["carousel_items_max"]
    )
    if manifest.format in {"IMAGE", "REEL"}:
        count_ok = media_count == 1
    else:
        count_ok = bool(expected_count)
    add("format", count_ok, f"media count conforme: {media_count}", f"media count non conforme: {media_count}")

    for index, asset in enumerate(manifest.media, start=1):
        has_one_source = bool(asset.path) ^ bool(asset.public_url)
        add("format", has_one_source, f"media {index}: una sorgente", f"media {index}: specificare path XOR public_url")
        source = asset.public_url or asset.path or ""
        if asset.public_url:
            parsed = urlparse(asset.public_url)
            add("staging", parsed.scheme == "https" and bool(parsed.netloc),
                f"media {index}: URL HTTPS", f"media {index}: public_url deve essere HTTPS")
        if asset.path:
            path = Path(asset.path).expanduser()
            add("staging", path.is_file(), f"media {index}: file locale presente", f"media {index}: file locale assente")

        suffix = _asset_suffix(source)
        if manifest.format == "REEL" or asset.media_type == "VIDEO":
            allowed = suffix in set(policy["format"]["video_extensions_live"])
            add("format", allowed, f"media {index}: estensione video conforme", f"media {index}: video non MP4/MOV")
        else:
            if for_live and asset.public_url:
                allowed = suffix in set(policy["format"]["image_extensions_live"])
                add("format", allowed, f"media {index}: JPEG live", f"media {index}: Meta richiede JPEG live")
            add("accessibility", bool(asset.alt_text), f"media {index}: alt text presente", f"media {index}: alt text mancante")

    for gate in REQUIRED_GATES:
        status = manifest.quality_evidence.get(gate)
        add(gate, status == "PASS", f"evidence {gate}=PASS", f"evidence {gate} non PASS")

    rights = manifest.rights
    add("rights", rights.get("confirmed") is True, "diritti confermati", "rights.confirmed deve essere true")
    add("rights", bool(rights.get("source_or_license")), "fonte/licenza presente", "rights.source_or_license mancante")
    if manifest.format == "REEL":
        add("rights", bool(rights.get("music_rights")), "diritti musica dichiarati", "rights.music_rights mancante")

    lowered = manifest.caption.casefold()
    forbidden = policy["copy"]["forbidden_claim_fragments"]
    hits = [fragment for fragment in forbidden if fragment.casefold() in lowered]
    add("safety", not hits, "nessun claim vietato", f"claim vietati: {', '.join(hits)}")

    try:
        manifest.scheduled_datetime()
        add("schedule", True, "scheduled_at valido", "")
    except (ValueError, TypeError) as exc:
        add("schedule", False, "", f"scheduled_at non valido: {exc}")

    return results


def gate_report(manifest: ContentManifest, *, for_live: bool = False) -> dict:
    results = validate_manifest(manifest, for_live=for_live)
    failures = [item for item in results if item.status != "PASS"]
    return {
        "content_id": manifest.content_id,
        "content_hash": manifest.content_hash,
        "mode": "LIVE_PREFLIGHT" if for_live else "DRY_PREFLIGHT",
        "status": "PASS" if not failures else "FAIL",
        "checks": [item.as_dict() for item in results],
        "failures": len(failures),
    }
