FROM python:3.11-slim-bookworm as builder
WORKDIR /app
RUN --mount=type=cache,target=/var/cache/apt \
    set -eux; \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl-dev \
    libglib2.0-dev \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache \
    python -m pip install -U pip && \
    python -m pip install poetry

COPY main.py poetry.lock pyproject.toml .
RUN  --mount=type=cache,target=/root/.cache \
    poetry config virtualenvs.create false && \
    poetry install
ENV DATA_DIR=/app/data
CMD ["poetry", "run", "python", "main.py"]
