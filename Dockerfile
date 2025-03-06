FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /bot/

# Install uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /bin/uv

# Place executables in the environment at the front of the path
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment
ENV PATH="/app/.venv/bin:$PATH"

COPY ./pyproject.toml ./uv.lock ./.env /bot/
COPY . /bot


# Sync the project
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN uv sync


CMD ["uv", "run", "/bot/bot.py"]