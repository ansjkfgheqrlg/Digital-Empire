from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from orchestrator.adapters.postgres.queue import PostgresTaskQueue
from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory


async def run(args) -> None:
    engine, factory = create_engine_and_factory(args.database_url, pool_size=1, max_overflow=0)
    async with PostgresUnitOfWork(factory, args.tenant) as uow:
        task = await PostgresTaskQueue(uow.session, args.tenant).claim(
            args.worker,
            args.token_hash,
            args.lease_seconds,
        )
        if task is None:
            raise RuntimeError("No task available for chaos claim")
        await uow.commit()
    Path(args.marker).write_text(str(task["task_id"]), encoding="utf-8")
    # Simulate abrupt worker death after durable claim; no graceful engine disposal.
    os._exit(137)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database-url", required=True)
    parser.add_argument("--tenant", required=True)
    parser.add_argument("--worker", default="chaos-worker")
    parser.add_argument("--token-hash", default="sha256:chaos")
    parser.add_argument("--lease-seconds", type=int, default=5)
    parser.add_argument("--marker", required=True)
    asyncio.run(run(parser.parse_args()))


if __name__ == "__main__":
    main()
