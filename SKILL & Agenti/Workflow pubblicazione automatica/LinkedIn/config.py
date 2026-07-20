"""LinkedIn legacy browser publisher configuration. Credentials are environment-only."""
import os

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL", "")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD", "")
