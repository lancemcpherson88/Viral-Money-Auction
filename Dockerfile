# Use a minimal Python image
# Use the official slim Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY app.py .

# Expose port 8080 to match the app's port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]



