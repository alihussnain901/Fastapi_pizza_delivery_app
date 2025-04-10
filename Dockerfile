# Use official Python image
<<<<<<< HEAD
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Set work directory
WORKDIR $APP_HOME

# Install system dependencies
=======
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies including PostgreSQL client
>>>>>>> c796fa8 (dockerfile updated)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
<<<<<<< HEAD
=======
    postgresql-client \
>>>>>>> c796fa8 (dockerfile updated)
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

<<<<<<< HEAD
# Create directory for env file
RUN mkdir -p $APP_HOME/app

# Copy .env file (remove this if using Docker secrets)
COPY .env $APP_HOME/app/

=======
>>>>>>> c796fa8 (dockerfile updated)
# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
<<<<<<< HEAD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> c796fa8 (dockerfile updated)
