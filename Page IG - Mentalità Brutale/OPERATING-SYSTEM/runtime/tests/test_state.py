from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.models import ContentManifest
from mb_os.state import StateStore


def manifest() -> ContentManifest:
    return ContentManifest.from_dict({
        "content_id": "MB-Q-001",
        "brand": "mentalita-brutale",
        "format": "IMAGE",
        "caption": "Test",
        "scheduled_at": "2020-01-01T00:00:00Z",
        "media": [{"public_url": "https://example.test/a.jpg", "alt_text": "Test"}],
        "quality_evidence": {key: "PASS" for key in ("format", "brand", "copy", "rights", "safety")},
        "rights": {"confirmed": True, "source_or_license": "owned"},
    })


class StateTests(unittest.TestCase):
    def test_migration_defaults_and_idempotent_enqueue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp) / "state.sqlite")
            self.assertEqual(store.get_control("autonomy_mode"), "SHADOW")
            self.assertEqual(store.get_control("kill_switch"), "ACTIVE")
            self.assertTrue(store.enqueue(manifest()))
            self.assertFalse(store.enqueue(manifest()))
            self.assertEqual(len(store.due_jobs(datetime.now(timezone.utc))), 1)

    def test_publication_unique_by_hash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp) / "state.sqlite")
            item = manifest()
            result = {"media_id": "m1", "container_id": "c1", "permalink": "https://instagram.test/p/1"}
            store.record_publication(item, result)
            store.record_publication(item, result)
            found = store.find_publication(item.content_hash)
            self.assertEqual(found["media_id"], "m1")


if __name__ == "__main__":
    unittest.main()
