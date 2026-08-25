"""Create canonical workflow, queue, audit, outbox and memory tables.

Revision ID: 0001_core
Revises: None
"""

from pathlib import Path

from alembic import op

revision = "0001_core"
down_revision = None
branch_labels = None
depends_on = None


def _split_postgres_sql(script: str) -> list[str]:
    """Split top-level statements while preserving strings and $$ blocks."""
    statements: list[str] = []
    buffer: list[str] = []
    in_single = False
    in_double = False
    in_dollar = False
    index = 0
    while index < len(script):
        pair = script[index : index + 2]
        char = script[index]
        if pair == "$$" and not in_single and not in_double:
            in_dollar = not in_dollar
            buffer.append(pair)
            index += 2
            continue
        if char == "'" and not in_double and not in_dollar:
            if in_single and index + 1 < len(script) and script[index + 1] == "'":
                buffer.extend(("'", "'"))
                index += 2
                continue
            in_single = not in_single
        elif char == '"' and not in_single and not in_dollar:
            in_double = not in_double
        if char == ";" and not in_single and not in_double and not in_dollar:
            statement = "".join(buffer).strip()
            if statement:
                statements.append(statement)
            buffer = []
        else:
            buffer.append(char)
        index += 1
    trailing = "".join(buffer).strip()
    if trailing:
        statements.append(trailing)
    if in_single or in_double or in_dollar:
        raise RuntimeError("Unterminated SQL quote/dollar block in migration")
    return statements


def upgrade() -> None:
    sql_path = Path(__file__).with_suffix(".sql")
    for statement in _split_postgres_sql(sql_path.read_text(encoding="utf-8")):
        op.execute(statement)


def downgrade() -> None:
    raise RuntimeError(
        "Destructive down migration is intentionally unsupported; restore or deploy forward"
    )
