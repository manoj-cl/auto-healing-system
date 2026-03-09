# Use official Python image
FROM python:3.12-slim

# Create working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY app/requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y procps
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Run application
CMD ["python", "monitor.py"]