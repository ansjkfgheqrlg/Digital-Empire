from __future__ import annotations

import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.config import Settings
from mb_os.models import ContentManifest
from mb_os.orchestrator import LIVE_CONFIRMATION, LiveGuardError, Operator
from mb_os.state import StateStore


class FakeMeta:
    def __init__(self):
        self.calls = []

    def account_health(self):
        self.calls.append("health")
        return {"username": "mentalita.brutale", "account_type": "BUSINESS"}

    def publishing_limit(self, user_id):
        self.calls.append("limit")
        return {"data": []}

    def create_image_container(self, user_id, url, **kwargs):
        self.calls.append("create")
        return "container-1"

    def wait_until_ready(self, container_id):
        self.calls.append("wait")

    def publish_container(self, user_id, container_id):
        self.calls.append("publish")
        return "media-1"

    def media_details(self, media_id):
        self.calls.append("details")
        return {"id": media_id, "permalink": "https://instagram.test/p/one", "timestamp": "2030-01-01T10:00:00Z"}


class FakeStager:
    def plan(self, manifest):
        return [{"action": "reuse_public_url"}]

    def stage_all(self, manifest):
        return [asset.public_url for asset in manifest.media]

    def preflight_all(self, urls):
        return [{"url": url, "status": 200, "content_type": "image/jpeg"} for url in urls]


def manifest() -> ContentManifest:
    return ContentManifest.from_dict({
        "content_id": "MB-LIVE-001",
        "brand": "mentalita-brutale",
        "format": "IMAGE",
        "caption": "Uno standard concreto. Salva questo post.",
        "scheduled_at": "2030-01-01T10:00:00Z",
        "media": [{"public_url": "https://cdn.example.test/a.jpg", "alt_text": "Testo accessibile"}],
        "quality_evidence": {key: "PASS" for key in ("format", "brand", "copy", "rights", "safety")},
        "rights": {"confirmed": True, "source_or_license": "owned"},
    })


class OperatorTests(unittest.TestCase):
    def settings(self, db: Path, live: bool) -> Settings:
        return Settings(
            api_version="v25.0", graph_host="https://graph.instagram.com",
            access_token="test-token-not-real", ig_user_id="ig-1", app_id="", app_secret="", redirect_uri="",
            public_media_dir=None, public_media_base_url="", state_db=db,
            live_publish_enabled=live, request_timeout_seconds=1,
        )

    def test_dry_run_makes_no_meta_calls(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fake = FakeMeta()
            store = StateStore(Path(tmp) / "state.sqlite")
            operator = Operator(self.settings(store.path, False), store, fake, FakeStager())
            result = operator.run(manifest())
            self.assertEqual(result["mode"], "DRY_RUN")
            self.assertEqual(fake.calls, [])

    def test_shadow_blocks_live(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fake = FakeMeta()
            store = StateStore(Path(tmp) / "state.sqlite")
            operator = Operator(self.settings(store.path, True), store, fake, FakeStager())
            with self.assertRaises(LiveGuardError):
                operator.run(manifest(), live=True, confirmation=LIVE_CONFIRMATION)
            self.assertEqual(fake.calls, [])

    def test_supervised_canary_and_idempotent_retry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fake = FakeMeta()
            store = StateStore(Path(tmp) / "state.sqlite")
            store.set_control("autonomy_mode", "SUPERVISED")
            operator = Operator(self.settings(store.path, True), store, fake, FakeStager())
            first = operator.run(manifest(), live=True, confirmation=LIVE_CONFIRMATION)
            self.assertEqual(first["status"], "PUBLISHED")
            second = operator.run(manifest(), live=True, confirmation=LIVE_CONFIRMATION)
            self.assertEqual(second["status"], "IDEMPOTENT_SKIP")
            self.assertEqual(fake.calls.count("publish"), 1)


if __name__ == "__main__":
    unittest.main()
