# Dockerfile for the web application

# Use the official Python image as base
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application files
COPY . .

# Expose port 5000
EXPOSE 8000

# Command to run the application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]