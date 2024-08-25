# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/ /app

# Expose port 80
EXPOSE 80

# Serve the HTML file using Python's built-in HTTP server
CMD ["python", "-m", "http.server", "80"]

