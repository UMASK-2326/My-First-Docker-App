# Use a modern Alpine image with Python 3
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .
# Expose port 80
EXPOSE 5000

# Run the application
CMD ["python", "-m", "http.server", "8000", "--directory", "images"]
