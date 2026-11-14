FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies and create a non-root user
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# Copy project files with the correct ownership
COPY --chown=appuser:appuser . .

# Create logs directory and ensure ownership for runtime files
RUN mkdir -p /app/logs \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Run with ddtrace so Datadog can auto-instrument Django + Gunicorn
CMD ["ddtrace-run", "gunicorn", "--bind", "0.0.0.0:8000", "kpa_project.wsgi:application", "--workers", "3", "--timeout", "120"]
