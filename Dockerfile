# Use a modern Alpine image with Python 3
FROM python:3.9-alpine

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies and upgrade pip
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --upgrade pip

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY templates/index.html ./templates/
COPY images/uma.jpg ./images/
# Expose port 80
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
