FROM python:3.9-slim

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code
COPY . .
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Gunicorn command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kpa_project.wsgi:application", "--workers", "3"]
