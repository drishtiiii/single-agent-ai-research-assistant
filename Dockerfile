FROM python:3.13-slim

# -----------------------------
# Environment
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# --------------------------------------
# System Dependencies
# --------------------------------------
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install Python Dependencies
# -----------------------------
COPY pyproject.toml ./

RUN pip install --upgrade pip

COPY . .

RUN pip install -e .

# -----------------------------
# Expose FastAPI port
# -----------------------------
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
