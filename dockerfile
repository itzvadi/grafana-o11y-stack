# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy the dummy log generator script into the container
COPY tools/genDummylogs.py .

# Create the logs directory (to be mounted)
RUN mkdir -p /logs

# Set permissions for logs directory (optional)
RUN chmod 777 /logs

# Run the log generator script
CMD ["python", "genDummylogs.py"]
