from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.config import Settings
from mb_os.models import ContentManifest
from mb_os.staging import AssetStager


@unittest.skipUnless(importlib.util.find_spec("PIL") is not None, "Pillow optional dependency not installed")
class StagingTests(unittest.TestCase):
    def test_png_converts_to_content_addressed_jpeg(self) -> None:
        from PIL import Image

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.png"
            Image.new("RGBA", (32, 32), (139, 0, 0, 180)).save(source)
            public = root / "public"
            settings = Settings(
                "v25.0", "https://graph.instagram.com", "", "", "", "", "",
                public, "https://media.example.test/mentalita", root / "state.sqlite", False, 5,
            )
            manifest = ContentManifest.from_dict({
                "content_id": "MB-STAGE-001", "brand": "mentalita-brutale", "format": "IMAGE",
                "caption": "Test", "scheduled_at": "2030-01-01T00:00:00Z",
                "media": [{"path": str(source), "alt_text": "Quadrato rosso"}],
                "quality_evidence": {key: "PASS" for key in ("format", "brand", "copy", "rights", "safety")},
                "rights": {"confirmed": True, "source_or_license": "owned"},
            })
            url = AssetStager(settings).stage_all(manifest)[0]
            outputs = list(public.glob("*.jpg"))
            self.assertEqual(len(outputs), 1)
            self.assertTrue(url.endswith(outputs[0].name))
            with Image.open(outputs[0]) as converted:
                self.assertEqual(converted.format, "JPEG")
                self.assertEqual(converted.mode, "RGB")


if __name__ == "__main__":
    unittest.main()
