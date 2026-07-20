from __future__ import annotations

import sys
import unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.gates import gate_report
from mb_os.models import ContentManifest


def valid_manifest() -> ContentManifest:
    return ContentManifest.from_dict({
        "content_id": "MB-TEST-001",
        "brand": "mentalita-brutale",
        "format": "CAROUSEL",
        "caption": "Una tesi utile. Salva questo post.",
        "scheduled_at": "2030-01-01T10:00:00Z",
        "media": [
            {"public_url": "https://cdn.example.test/a.jpg", "alt_text": "Slide uno"},
            {"public_url": "https://cdn.example.test/b.jpeg", "alt_text": "Slide due"},
        ],
        "quality_evidence": {key: "PASS" for key in ("format", "brand", "copy", "rights", "safety")},
        "rights": {"confirmed": True, "source_or_license": "owned", "music_rights": "none"},
    })


class GateTests(unittest.TestCase):
    def test_valid_carousel_passes_live_preflight(self) -> None:
        report = gate_report(valid_manifest(), for_live=True)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["failures"], 0)

    def test_missing_rights_and_alt_text_fail(self) -> None:
        value = valid_manifest().canonical_dict()
        value["media"][0]["alt_text"] = None
        value["rights"]["confirmed"] = False
        report = gate_report(ContentManifest.from_dict(value), for_live=True)
        messages = " ".join(item["message"] for item in report["checks"] if item["status"] == "FAIL")
        self.assertEqual(report["status"], "FAIL")
        self.assertIn("alt text", messages)
        self.assertIn("rights.confirmed", messages)

    def test_public_png_is_dry_acceptable_but_live_blocked(self) -> None:
        value = valid_manifest().canonical_dict()
        value["media"][0]["public_url"] = "https://cdn.example.test/a.png"
        manifest = ContentManifest.from_dict(value)
        self.assertEqual(gate_report(manifest, for_live=False)["status"], "PASS")
        self.assertEqual(gate_report(manifest, for_live=True)["status"], "FAIL")

    def test_hash_is_canonical(self) -> None:
        one = valid_manifest()
        two = ContentManifest.from_dict(dict(reversed(list(one.canonical_dict().items()))))
        self.assertEqual(one.content_hash, two.content_hash)


if __name__ == "__main__":
    unittest.main()
