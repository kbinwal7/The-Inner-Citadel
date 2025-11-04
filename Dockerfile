# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 (Spaces default)
EXPOSE 7860

# Set environment variable for Flask
ENV PORT=7860
ENV HOST=0.0.0.0

# Command to run your app
CMD ["python", "app.py"]
