"""TikTok legacy browser publisher configuration. Credentials are environment-only."""
import os

TK_EMAIL = os.environ.get("TIKTOK_EMAIL", "")
TK_PASSWORD = os.environ.get("TIKTOK_PASSWORD", "")

ALLOW_COMMENTS = True
ALLOW_DUET = False
ALLOW_STITCH = False
