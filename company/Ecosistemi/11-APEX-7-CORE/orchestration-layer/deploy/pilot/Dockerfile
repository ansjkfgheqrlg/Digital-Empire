FROM python:3.12-slim AS build
WORKDIR /build
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1
COPY pyproject.toml README.md ./
COPY src ./src
RUN python -m pip wheel --wheel-dir /wheels .

FROM python:3.12-slim AS runtime
RUN groupadd --gid 10001 ocp && useradd --uid 10001 --gid ocp --create-home ocp
WORKDIR /app
COPY --from=build /wheels /wheels
RUN python -m pip install --no-cache-dir /wheels/* && rm -rf /wheels
COPY alembic.ini ./alembic.ini
COPY migrations ./migrations
COPY contracts ./contracts
COPY policies ./policies
COPY prompts ./prompts
COPY skills ./skills
COPY builder_swarm ./builder_swarm
COPY memory_store/plans ./memory_store/plans
COPY memory_store/index ./memory_store/index
COPY plans ./plans
RUN chown -R ocp:ocp /app
USER 10001:10001
ENV PYTHONUNBUFFERED=1 ORCHESTRATION_ROOT=/app
ENTRYPOINT ["ocp-local-slice"]
CMD ["--help"]
