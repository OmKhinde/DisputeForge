# ── DisputeForge FastAPI Service ──────────────────────────────
# Phase 0: Health check only

FROM python:3.11-slim AS base
WORKDIR /app

# ── System deps ──────────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ── Python deps ──────────────────────────────────────────────
RUN pip install --no-cache-dir poetry==1.8.5
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# ── App code ─────────────────────────────────────────────────
COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
