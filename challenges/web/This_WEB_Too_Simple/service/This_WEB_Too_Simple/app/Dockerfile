# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Install sqlite3
RUN apt-get update && apt-get install -y sqlite3

# Set the working directory in the Docker container to /app
WORKDIR /app

# Copy the contents of the service folder into the Docker container
COPY www/ .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to silence Flask's startup message
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Ensure start.sh is executable
RUN chmod +x start.sh

# Run the start.sh script when the container starts
CMD ["./start.sh"]
