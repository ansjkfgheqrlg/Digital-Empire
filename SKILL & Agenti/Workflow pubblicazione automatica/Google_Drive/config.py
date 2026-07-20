"""Google Drive configuration.

SECURITY: credentials are loaded from environment variables or the local ignored .env.
Never commit account passwords, cookies, tokens, or app secrets.
"""
import os

DRIVE_EMAIL = os.environ.get("GOOGLE_DRIVE_EMAIL", "")
DRIVE_PASSWORD = os.environ.get("GOOGLE_DRIVE_PASSWORD", "")

# Shared folder URLs are identifiers, not authentication secrets.
DRIVE_CAROUSELLI_URL = os.environ.get(
    "DRIVE_CAROUSELLI_URL",
    "https://drive.google.com/drive/folders/1XnzZrj3GFovuXqOGnTy03MoK0cc8d9tq?usp=drive_link",
)
DRIVE_MENTALITA_URL = os.environ.get(
    "DRIVE_MENTALITA_URL",
    "https://drive.google.com/drive/folders/12bofTLSCbE_ceYEr4t9b2aD7PZ0t9C2l",
)

PUBLISHED_HISTORY_FILE = "published_history.json"
