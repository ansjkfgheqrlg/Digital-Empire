"""Add governed privacy deletion workflow.

Revision ID: 0002_privacy
Revises: 0001_core
"""

import importlib.util
from pathlib import Path

from alembic import op

revision = "0002_privacy"
down_revision = "0001_core"
branch_labels = None
depends_on = None


def _splitter():
    path = Path(__file__).with_name("0001_core.py")
    spec = importlib.util.spec_from_file_location("migration_0001_splitter", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module._split_postgres_sql


def upgrade() -> None:
    sql = Path(__file__).with_suffix(".sql").read_text(encoding="utf-8")
    for statement in _splitter()(sql):
        op.execute(statement)


def downgrade() -> None:
    raise RuntimeError("Privacy deletion history cannot be destructively downgraded")
