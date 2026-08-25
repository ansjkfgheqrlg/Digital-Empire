from __future__ import annotations

import asyncio
import json
import os
import signal

from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory
from orchestrator.worker.service import OutboxPublisherService


async def serve() -> None:
    tenant = os.environ.get("OCP_TENANT_ID", "local-pilot")
    engine, factory = create_engine_and_factory(os.environ["OCP_DATABASE_URL"])
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for name in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(name, stop.set)

    async def sink(event) -> None:
        # Local pilot sink. Production must replace this with a durable broker.
        print(json.dumps({"outbox_event": event}, default=str, ensure_ascii=False), flush=True)

    publisher = OutboxPublisherService(
        lambda tenant_id: PostgresUnitOfWork(factory, tenant_id), tenant, sink
    )
    try:
        while not stop.is_set():
            count = await publisher.publish_once()
            if count == 0:
                try:
                    await asyncio.wait_for(stop.wait(), timeout=0.5)
                except TimeoutError:
                    pass
    finally:
        await engine.dispose()


def main() -> None:
    asyncio.run(serve())


if __name__ == "__main__":
    main()
