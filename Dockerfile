# Use a minimal Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8080 to match the app's port
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
