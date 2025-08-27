FROM python:3.9-slim

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Create logs directory and set proper permissions
RUN mkdir -p /app/logs && chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Run with ddtrace so Datadog can auto-instrument Django + Gunicorn
CMD ["ddtrace-run", "gunicorn", "--bind", "0.0.0.0:8000", "kpa_project.wsgi:application", "--workers", "3", "--timeout", "120"]