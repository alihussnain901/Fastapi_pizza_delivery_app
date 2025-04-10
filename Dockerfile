FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application
COPY . .

# Install as editable package (if using relative imports)
RUN pip install -e .

# Alternative: Set Python path
ENV PYTHONPATH=/app

EXPOSE 8000

# Updated command to point to correct module
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]