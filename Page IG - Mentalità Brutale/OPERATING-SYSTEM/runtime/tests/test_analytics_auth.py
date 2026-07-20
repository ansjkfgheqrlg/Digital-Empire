from __future__ import annotations

import sys
import unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from mb_os.analytics import parse_insights, quality_action_rate
from mb_os.auth import CORE_SCOPES, authorization_url
from mb_os.config import Settings


class AnalyticsAuthTests(unittest.TestCase):
    def test_parse_preserves_missing_as_none(self) -> None:
        response = {"data": [
            {"name": "reach", "values": [{"value": 100}]},
            {"name": "saved", "values": []},
            {"name": "shares", "total_value": {"value": 5}},
        ]}
        parsed = parse_insights(response)
        self.assertEqual(parsed["reach"], 100)
        self.assertIsNone(parsed["saved"])
        self.assertEqual(parsed["shares"], 5)

    def test_quality_action_rate(self) -> None:
        score = quality_action_rate({"reach": 100, "shares": 2, "saved": 3, "comments": 1, "likes": 5})
        self.assertEqual(score, 30.0)
        self.assertIsNone(quality_action_rate({"reach": None}))

    def test_auth_url_contains_current_business_scopes_and_state(self) -> None:
        settings = Settings(
            "v25.0", "https://graph.instagram.com", "", "", "123", "", "https://example.test/callback",
            None, "", Path("/tmp/unused.sqlite"), False, 1,
        )
        url, state = authorization_url(settings, state="fixed-state")
        self.assertIn("instagram_business_content_publish", url)
        self.assertIn("instagram_business_manage_insights", url)
        self.assertEqual(state, "fixed-state")
        self.assertTrue(all(scope in url for scope in CORE_SCOPES))


if __name__ == "__main__":
    unittest.main()
