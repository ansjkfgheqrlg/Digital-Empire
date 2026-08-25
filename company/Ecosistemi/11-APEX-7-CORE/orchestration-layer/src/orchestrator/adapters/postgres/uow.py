from __future__ import annotations

from types import TracebackType
from typing import Self

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from .repositories import PostgresWorkflowRepository


class PostgresUnitOfWork:
    """Transaction boundary that installs tenant context before any repository query."""

    def __init__(self, session_factory: async_sessionmaker[AsyncSession], tenant_id: str):
        if not tenant_id or len(tenant_id) > 64:
            raise ValueError("A bounded tenant_id is required")
        self._session_factory = session_factory
        self.tenant_id = tenant_id
        self.session: AsyncSession | None = None
        self.workflows: PostgresWorkflowRepository | None = None
        self._committed = False

    async def __aenter__(self) -> Self:
        self.session = self._session_factory()
        await self.session.begin()
        await self.session.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": self.tenant_id},
        )
        self.workflows = PostgresWorkflowRepository(self.session, self.tenant_id)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self.session is None:
            return
        try:
            if exc_type is not None or not self._committed:
                await self.session.rollback()
        finally:
            await self.session.close()

    async def commit(self) -> None:
        if self.session is None:
            raise RuntimeError("Unit of Work is not active")
        await self.session.commit()
        self._committed = True

    async def rollback(self) -> None:
        if self.session is None:
            raise RuntimeError("Unit of Work is not active")
        await self.session.rollback()


def create_engine_and_factory(
    database_url: str,
    *,
    pool_size: int = 10,
    max_overflow: int = 10,
    null_pool: bool = False,
) -> tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    if not database_url.startswith("postgresql+asyncpg://"):
        raise ValueError("Only postgresql+asyncpg URLs are accepted")
    options = {"pool_pre_ping": True}
    if null_pool:
        options["poolclass"] = NullPool
    else:
        options.update({"pool_size": pool_size, "max_overflow": max_overflow})
    engine = create_async_engine(database_url, **options)
    return engine, async_sessionmaker(engine, expire_on_commit=False)
