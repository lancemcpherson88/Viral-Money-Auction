# Use the official Python 3.6 slim image from Docker Hub
FROM python:3.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code and static files
COPY . .

# Expose port 8080 to match the app's port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
